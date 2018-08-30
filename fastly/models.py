"""
"""

from string import Template
from copy import copy
from six.moves.urllib.parse import urlencode

class Model(object):
    def __init__(self):
        self._original_attrs = None
        self.attrs = {}

    @classmethod
    def query(cls, conn, pattern, method, suffix='', body=None, **kwargs):
        url = Template(pattern).substitute(**kwargs)
        url += suffix

        headers = { 'Content-Accept': 'application/json' }
        if method == 'POST' or method == 'PUT':
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        return conn.request(method, url, body, headers)

    def _query(self, method, suffix='', body=None):
        return self.__class__.query(self.conn, self.INSTANCE_PATTERN, method, suffix, body, **self.attrs)

    def _collection_query(self, method, suffix='', body=None):
        return self.__class__.query(self.conn, self.COLLECTION_PATTERN, method, suffix, body, **self.attrs)

    def save(self):
        if self._original_attrs:
            out = {}
            for k in self.attrs:
                if self.attrs[k] != self._original_attrs[k]:
                    out[k] = self.attrs[k]
            params_str = urlencode(out)
            resp, data = self._query('PUT', body=params_str)

        else:
            params_str = urlencode(self.attrs)
            resp, data = self._collection_query('POST', body=params_str)

        self._original_attrs = data
        self.attrs = data


    @classmethod
    def list(cls, conn, **kwargs):
        resp, data = cls.query(conn, cls.COLLECTION_PATTERN, 'GET', **kwargs)

        collection = []

        if resp.status == 200 and hasattr(data, 'sort'):
            for i in range(0, len(data)):
                obj = cls.construct_instance(data[i])
                obj.conn = conn
                collection.append(obj)

        return collection

    @classmethod
    def find(cls, conn, **kwargs):
        resp, data = cls.query(conn, cls.INSTANCE_PATTERN, 'GET', **kwargs)
        obj = cls.construct_instance(data)
        obj.conn = conn
        return obj

    @classmethod
    def construct_instance(cls, data):
        obj = cls()
        obj._original_attrs = data
        obj.attrs = copy(data)
        return obj

class Service(Model):
    COLLECTION_PATTERN = '/service'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$id'

    def purge_key(self, key):
        resp, data = self._query('POST', '/purge/%s' % key)
        return data

    def purge_all(self):
        resp, data = self._query('POST', '/purge_all')
        return data

    def version(self):
        """ Create a new version under this service. """
        ver = Version()
        ver.conn = self.conn

        ver.attrs = {
            # Parent params
            'service_id': self.attrs['id'],
        }

        ver.save()

        return ver

class Version(Model):
    COLLECTION_PATTERN = Service.COLLECTION_PATTERN + '/$service_id/version'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$number'

    def check_backends(self):
        resp, data = self._query('GET', '/backend/check_all')
        return data

    def activate(self):
        resp, data = self._query('PUT', '/activate')
        return data

    def deactivate(self):
        resp, data = self._query('PUT', '/deactivate')
        return data

    def clone(self):
        resp, data = self._query('PUT', '/clone')
        return data

    def validate(self):
        resp, data = self._query('GET', '/validate')
        return data

    def lock(self):
        resp, data = self._query('PUT', '/lock')
        return data

    def boilerplate(self):
        resp, data = self._query('GET', '/boilerplate')
        return data

    def generated_vcl(self):
        resp, data = self._query('GET', '/generated_vcl')
        return data

    def vcl(self, name, content):
        """ Create a new VCL under this version. """
        vcl = VCL()
        vcl.conn = self.conn

        vcl.attrs = {
            # Parent params
            'service_id': self.attrs['service_id'],
            'version': self.attrs['number'],

            # New instance params
            'name': name,
            'content': content,
        }

        vcl.save()

        return vcl

class Domain(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/domain'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

    def check_cname(self):
        resp, data = self._query('GET', '/check')
        return (data[1], data[2])

class Backend(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/backend'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class Director(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/director'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class Origin(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/origin'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class Healthcheck(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/healthcheck'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class Syslog(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/syslog'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class User(Model):
    COLLECTION_PATTERN = '/user/$id'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$id'

class Settings(Model):
    INSTANCE_PATTERN = Version.COLLECTION_PATTERN + '/$version/settings'
    COLLECTION_PATTERN = INSTANCE_PATTERN

class Condition(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/condition'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class Header(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/header'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

class VCL(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/vcl'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

    def download(self):
        resp, data = self._query('GET', '/download')
        return data

    def main(self):
        resp, data = self._query('PUT', '/main')
        return data
