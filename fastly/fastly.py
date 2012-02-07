import httplib
import urllib
import json

from connection import *
from auth import *
from errors import *

class API(object):
    def __init__(self, host='api.fastly.com', secure=True, port=None, root='',
                 timeout=10.0):
        self.conn = Connection(host, secure, port, root, timeout)


    def authenticate_by_key(self, key):
        self.conn.authenticator = KeyAuthenticator(key)

    def authenticate_by_password(self, login, password):
        self.conn.authenticator = SessionAuthenticator(self.conn, login, password)

    def deauthenticate(self):
        self.conn.authenticator = None


    def purge_url(self, host, path):
        resp, data = self.conn.request('PURGE', path, headers={ 'Host': host })
        return resp.status == 200

