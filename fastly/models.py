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
        url += Template(suffix).substitute(**kwargs)

        headers = { 'Content-Accept': 'application/json' }
        if method == 'POST' or method == 'PUT':
            headers['Content-Type'] = 'application/x-www-form-urlencoded'

        return conn.request(method, url, body, headers)

    def _query(self, method, suffix='', body=None):
        return self.__class__.query(self.conn, self.INSTANCE_PATTERN, method, suffix, body, **self.attrs)

    def _collection_query(self, method, suffix='', body=None):
        return self.__class__.query(self.conn, self.COLLECTION_PATTERN, method, suffix, body, **self.attrs)

    @staticmethod
    def _urlencode(attrs):
        """ Get the urlencoded representation of attributes dict, with lower-case booleans """
        def get_sanitized(value):
            """ Get value sanitized """
            if isinstance(value, bool):
                return str(value).lower()
            return value
        return urlencode({
            key: get_sanitized(value)
            for key, value in attrs.items()
        })

    def save(self):
        if self._original_attrs == self.attrs:
            return False

        if self._original_attrs:
            out = {}
            for k in self.attrs:
                if self.attrs[k] != self._original_attrs[k]:
                    out[k] = self.attrs[k]
            params_str = self._urlencode(out)
            resp, data = self._query('PUT', body=params_str)
        else:
            params_str = self._urlencode(self.attrs)
            resp, data = self._collection_query('POST', body=params_str)

        self._original_attrs = data
        self.attrs = data
        return True

    def delete(self):
        resp, data = self._query('DELETE')
        return data

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
    def create(cls, conn, data):
        instance = cls.construct_instance(data, new=True)
        instance.conn = conn
        instance.save()
        return instance

    @classmethod
    def construct_instance(cls, data, new=False):
        obj = cls()
        if not new:
            obj._original_attrs = data
        obj.attrs = copy(data)
        return obj

class Service(Model):
    COLLECTION_PATTERN = '/service'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$id'

    def details(self):
        resp, data = self._query('GET', '/details')
        return data

    def get_active_version_number(self):
        versions = self.attrs.get('versions')
        if versions:
            return list(filter(lambda x: x['active'] is True, versions))[0]['number']
        return None

    def purge_key(self, key):
        resp, data = self._query('POST', '/purge/%s' % key)
        return data

    def purge_all(self):
        resp, data = self._query('POST', '/purge_all')
        return data

    def version(self):
        """ Create a new version under this service. """
        return Version.create(self.conn, {
            # Parent params
            'service_id': self.attrs['id'],
        })


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
        return VCL.create(self.conn, {
            # Parent params
            'service_id': self.attrs['service_id'],
            'version': self.attrs['number'],
            # New instance params
            'name': name,
            'content': content,
        })

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

class Dictionary(Model):
    COLLECTION_PATTERN = Version.COLLECTION_PATTERN + '/$version/dictionary'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$name'

    def info(self):
        resp, data = self._collection_query('GET', suffix='/$id/info')
        return data

    def item(self, item_key, item_value=None):
        if item_value is not None:
            return DictionaryItem.upsert(self.conn, {
                'service_id': self.attrs['service_id'],
                'dictionary_id': self.attrs['id'],
                'item_key': item_key,
                'item_value': item_value,
            })
        return DictionaryItem.find(self.conn, service_id=self.attrs['service_id'], dictionary_id=self.attrs['id'], item_key=item_key)

    def items(self):
        return DictionaryItem.list(self.conn, service_id=self.attrs['service_id'], dictionary_id=self.attrs['id'])

class DictionaryItem(Model):
    COLLECTION_PATTERN = Service.COLLECTION_PATTERN + '/$service_id/dictionary/$dictionary_id/items'
    INSTANCE_PATTERN = Service.COLLECTION_PATTERN + '/$service_id/dictionary/$dictionary_id/item/$item_key'
    INSTANCE_CREATE_PATTERN = Service.COLLECTION_PATTERN + '/$service_id/dictionary/$dictionary_id/item'

    @classmethod
    def upsert(cls, conn, data):
        # https://docs.fastly.com/api/config#dictionary_item_34c884a7cdce84dfcfd38dac7a0b5bb0
        instance = cls.construct_instance(data)
        instance.conn = conn
        params_str = urlencode(instance.attrs)
        resp, data = instance._query('PUT', body=params_str)
        instance._original_attrs = data
        instance.attrs = data
        return instance

    def _collection_query(self, method, suffix='', body=None):
        # DictionaryItem's create API URL is inconsistent with the other APIs,
        # with the use of singular and plural ("item" and "items").
        # Only use case for POST on this Model is to create one item, so swap in that API URL.
        pattern = self.INSTANCE_CREATE_PATTERN if method == 'POST' else self.COLLECTION_PATTERN
        return self.__class__.query(self.conn, pattern, method, suffix, body, **self.attrs)
