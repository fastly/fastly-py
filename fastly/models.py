"""
"""

from string import Template
from copy import copy

class Model(object):
    @classmethod
    def query(cls, conn, pattern, method, suffix='', body=None, **kwargs):
        url = Template(pattern).substitute(**kwargs)
        url += suffix
        return conn.request(method, url, body)

    def _query(self, method, suffix='', body=None):
        return self.__class__.query(self.conn, self.INSTANCE_PATTERN, method, suffix, body, **self.attrs)

    def _collection_query(self, method, suffix='', body=None):
        return self.__class__.query(self.conn, self.COLLECTION_PATTERN, method, suffix, body, **self.attrs)

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
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$service_id'

    def purge_key(self, key):
        self._query('POST', '/purge/%s' % key)

    def purge_all(self):
        self._query('POST', '/purge_all')

class Version(Model):
    COLLECTION_PATTERN = Service.INSTANCE_PATTERN + '/version'
    INSTANCE_PATTERN = COLLECTION_PATTERN + '/$number'

    def check_backends(self):
        resp, data = self._query('GET', '/backend/check_all')
        return data
        

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
