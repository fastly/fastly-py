"""
"""

from .errors import *

import urllib.request, urllib.parse, urllib.error

class KeyAuthenticator(object):
    def __init__(self, key):
        self.key = key

    def add_auth(self, headers):
        headers['Fastly-Key'] = self.key

class SessionAuthenticator(object):
    def __init__(self, conn, login, password):
        body = urllib.parse.urlencode({ 'user': login, 'password': password })
        resp, data = conn.request('POST', '/login', body)
        self.session_key = resp.getheader('Set-Cookie')

    def add_auth(self, headers):
        headers['Cookie'] = self.session_key
