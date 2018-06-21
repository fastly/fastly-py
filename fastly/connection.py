"""
"""
from __future__ import absolute_import

import json
import ssl

from six.moves import http_client

from fastly._version import __version__
from fastly import errors

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
            ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
            self.http_conn = http_client.HTTPSConnection(self.host, self.port,
                                           timeout=self.timeout, context=ctx)
        else:
            self.http_conn = http_client.HTTPConnection(self.host, self.port,
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

        if response.status in [401, 403]:
            raise errors.AuthenticationError()
        elif response.status == 500:
            raise errors.InternalServerError()
        elif response.status == 400:
            raise errors.BadRequestError(body)
        elif response.status == 404:
            raise errors.NotFoundError()

        return (response, data)
