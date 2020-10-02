"""
"""
from __future__ import absolute_import

from six.moves.urllib.parse import urlencode
import warnings

class KeyAuthenticator(object):
    def __init__(self, key):
        self.key = key

    def add_auth(self, headers):
        headers['Fastly-Key'] = self.key
