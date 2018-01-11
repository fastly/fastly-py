"""
"""

import http.client
import json
from ._version import __version__

from .errors import *

class Connection(object):
    def __init__(self, host='api.fastly.com', secure=True, port=None, root='',
                 timeout=10.0):
        self.host = host
        self.secure = secure
        self.port = port
        self.root = root
        self.timeout = timeout

        self.authenticator = None
        self.http_conn = None
        self.default_headers = { 'User-Agent': 'fastly-py-v{}'.format(__version__) }

    def request(self, method, path, body=None, headers={}):
        headers.update(self.default_headers)

        if not self.port:
            self.port = 443 if self.secure else 80

        if self.secure:
            self.http_conn = http.client.HTTPSConnection(self.host, self.port,
                                           timeout=self.timeout)
        else:
            self.http_conn = http.client.HTTPConnection(self.host, self.port,
                                          timeout=self.timeout)

        if self.authenticator:
            self.authenticator.add_auth(headers)

        self.http_conn.request(method, self.root + path, body, headers=headers)
        response = self.http_conn.getresponse()
        body = response.read()
        try:
            data = json.loads(body)
        except ValueError:
            data = body

        if response.status == 403:
            raise AuthenticationError()
        elif response.status == 500:
            raise InternalServerError()
        elif response.status == 400:
            raise BadRequestError(body)
        elif response.status == 404:
            raise NotFoundError()

        return (response, data)
