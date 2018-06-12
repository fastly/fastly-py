"""
"""
from __future__ import absolute_import

from six.moves.urllib.parse import urlencode

from fastly import errors


class KeyAuthenticator(object):
    def __init__(self, key):
        self.key = key

    def add_auth(self, headers):
        headers['Fastly-Key'] = self.key

class SessionAuthenticator(object):
    def __init__(self, conn, login, password):
        body = urlencode({ 'user': login, 'password': password })
        resp, data = conn.request('POST', '/login', body)
        self.session_key = resp.getheader('Set-Cookie')

    def add_auth(self, headers):
        headers['Cookie'] = self.session_key
