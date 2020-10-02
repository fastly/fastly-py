from __future__ import absolute_import

import json
import os

from fastly.connection import Connection
from fastly.auth import KeyAuthenticator
from fastly.errors import AuthenticationError
from fastly.models import (
    Service, Version, Domain, Backend,
    Settings, Condition, Header, VCL,
    Dictionary, DictionaryItem
)


class API(object):
    def __init__(self, host=os.environ.get('FASTLY_HOST', 'api.fastly.com'), secure=os.environ.get('FASTLY_SECURE', 'true'), port=None, root='',
                 timeout=5.0, key=None):
        secure = secure.lower() in ['true', '1', 't', 'y', 'yes']

        self.conn = Connection(host, secure, port, root, timeout)

        if key:
            self.authenticate_by_key(key)

    def authenticate_by_key(self, key):
        self.conn.authenticator = KeyAuthenticator(key)

    def deauthenticate(self):
        self.conn.authenticator = None

    def services(self):
        return Service.list(self.conn)

    def service(self, id):
        return Service.find(self.conn, id=id)

    def versions(self, service_id):
        return Version.list(self.conn, service_id=service_id)

    def version(self, service_id, version):
        return Version.find(self.conn, service_id=service_id, number=version)

    def domains(self, service_id, version):
        return Domain.list(self.conn, service_id=service_id, version=version)

    def domain(self, service_id, version, name):
        return Domain.find(self.conn, service_id=service_id, version=version, name=name)

    def backends(self, service_id, version):
        return Backend.list(self.conn, service_id=service_id, version=version)

    def backend(self, service_id, version, name):
        return Backend.find(self.conn, service_id=service_id, version=version, name=name)

    def settings(self, service_id, version):
        return Settings.find(self.conn, service_id=service_id, version=version)

    def condition(self, service_id, version, name):
        return Condition.find(self.conn, service_id=service_id, version=version, name=name)

    def header(self, service_id, version, name):
        return Header.find(self.conn, service_id=service_id, version=version, name=name)

    def vcls(self, service_id, version):
        return VCL.list(self.conn, service_id=service_id, version=version)

    def vcl(self, service_id, version, name):
        return VCL.find(self.conn, service_id=service_id, version=version, name=name)

    def dictionaries(self, service_id, version):
        return Dictionary.list(self.conn, service_id=service_id, version=version)

    def dictionary(self, service_id, version, name):
        return Dictionary.find(self.conn, service_id=service_id, version=version, name=name)

    def dictionary_items(self, service_id, dictionary_id):
        return DictionaryItem.list(self.conn, service_id=service_id, dictionary_id=dictionary_id)

    def dictionary_item(self, service_id, dictionary_id, item_key):
        return DictionaryItem.find(self.conn, service_id=service_id, dictionary_id=dictionary_id, item_key=item_key)

    def purge_url(self, host, path, soft=False):
        headers = {}
        if soft:
            headers['Fastly-Soft-Purge'] = 1

        purge_path = "/purge/%s%s" % (host, path)
        resp, data = self.conn.request(
            'POST', purge_path, body='', headers=headers)
        return resp.status == 200

    def soft_purge_url(self, host, path):
        return self.purge_url(host, path, True)

    def purge_service(self, service, soft=False):
        headers = {}
        if soft:
            headers['Fastly-Soft-Purge'] = 1

        resp, data = self.conn.request('POST','/service/%s/purge_all' % service, headers=headers)
        return resp.status == 200

    def soft_purge_service(self, service):
        return self.purge_service(service, True)

    def purge_key(self, service, key, soft=False):
        if not isinstance(self.conn.authenticator, KeyAuthenticator):
            raise AuthenticationError("This request requires an API key")

        headers = {}
        if soft:
            headers['Fastly-Soft-Purge'] = 1

        resp, data = self.conn.request('POST', '/service/%s/purge/%s' % (service, key), headers=headers)
        return resp.status == 200

    def soft_purge_key(self, service, key):
        return self.purge_key(service, key, True)

    def batch_purge_key(self, service, keys, soft=False):
        if not isinstance(self.conn.authenticator, KeyAuthenticator):
            raise AuthenticationError("This request requires an API key")

        body = json.dumps({"surrogate_keys": keys})
        headers = {'Content-Type': 'application/json'}

        if soft:
            headers['Fastly-Soft-Purge'] = 1

        resp, data = self.conn.request('POST', '/service/%s/purge' % (service),
                                       body=body, headers=headers)
        return resp.status == 200

    def soft_batch_purge_key(self, service, keys):
        return self.batch_purge_key(service, keys, True)
