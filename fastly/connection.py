from __future__ import absolute_import

from fastly._version import __version__
from fastly import errors
from requests_toolbelt.sessions import BaseUrlSession


class Session(object):
    def __init__(self, host='api.fastly.com', secure=True, port=None, root='', timeout=10.0):
        self.host = host
        self.secure = secure
        self.scheme = 'https://' if secure is True else 'http://'
        self.port = port if port is not None else (443 if secure is True else 80)
        self.root = root
        self.timeout = timeout
        self.url = '{scheme}{host}:{port}'.format(scheme=self.scheme, host=self.host, port=self.port)
        self.authenticator = None
        # self.http_conn = None
        self.default_headers = {'User-Agent': 'fastly-py-v{}'.format(__version__)}
        self.session = BaseUrlSession(self.url)
        self.session.headers.update(self.default_headers)

    def request(self, method, path, body=None, headers=None):
        if not headers:
            headers = {}

        if headers is not None:
            self.session.headers.update(headers)

        if self.authenticator:
            self.authenticator.add_auth(self.session.headers)

        response = self.session.request(method, path, data=body, headers=headers)

        try:
            data = response.json()
        except ValueError:
            data = response.content

        if response.status_code in [401, 403]:
            raise errors.AuthenticationError()
        elif response.status_code == 500:
            raise errors.InternalServerError()
        elif response.status_code == 400:
            raise errors.BadRequestError(body)
        elif response.status_code == 404:
            raise errors.NotFoundError()

        return response, data
