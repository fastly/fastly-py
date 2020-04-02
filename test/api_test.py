import unittest
import os
from fastly import fastly, errors
from fastly._version import __version__


class APITest(unittest.TestCase):

    def setUp(self):
        self.api = fastly.API()
        self.host = os.environ.get('FASTLY_SERVICE_HOST', 'test.com')
        self.service_id = os.environ.get('FASTLY_SERVICE_ID', 'test.com')
        self.api_key = os.environ.get('FASTLY_API_KEY', 'TESTAPIKEY')
        self.user = os.environ.get('FASTLY_USER', 'foo@example.com')
        self.password = os.environ.get('FASTLY_PASSWORD', 'password')
        self.api.deauthenticate()

    def tearDown(self):
        if self.api.conn.http_conn is not None:
            self.api.conn.http_conn.close()

    # NOTE: Authentication is optional for purging. if your service that you're
    # testing against requires authentication, then it's necessary to do this
    # self.api.authenticate_by_key() call or the test_purge and test_soft_purge
    # tests will fail
    def test_purge(self):
        self.api.authenticate_by_key(self.api_key)
        self.assertTrue(self.api.purge_url(self.host, '/'))

    def test_soft_purge(self):
        self.api.authenticate_by_key(self.api_key)
        self.assertTrue(self.api.soft_purge_url(self.host, '/'))

    def test_purge_by_key(self):
        self.api.authenticate_by_key(self.api_key)
        self.assertTrue(self.api.purge_key(self.service_id, 'foo'))

    def test_cookie_purge_by_key(self):
        self.api.authenticate_by_password(self.user, self.password)
        with self.assertRaises(fastly.AuthenticationError):
            self.api.purge_key(self.service_id, 'foo')

    def test_soft_purge_by_key(self):
        self.api.authenticate_by_key(self.api_key)
        self.assertTrue(self.api.soft_purge_key(self.service_id, 'foo'))

    def test_cookie_soft_purge_by_key(self):
        self.api.authenticate_by_password(self.user, self.password)
        with self.assertRaises(fastly.AuthenticationError):
            self.api.soft_purge_key(self.service_id, 'foo')

    def test_auth_error(self):
        with self.assertRaises(errors.AuthenticationError):
            self.api.conn.request('GET', '/current_customer')

    def test_auth_session_success(self):
        self.api.authenticate_by_password(self.user, self.password)
        self.api.conn.request('GET', '/current_customer')

    def test_auth_key_success(self):
        self.api.authenticate_by_key(self.api_key)
        self.api.conn.request('GET', '/current_customer')

    def test_sets_default_user_agent_header(self):
        default_headers = self.api.conn.default_headers
        self.assertEqual(
            default_headers['User-Agent'], 'fastly-py-v{}'.format(__version__))


if __name__ == '__main__':
    unittest.main()
