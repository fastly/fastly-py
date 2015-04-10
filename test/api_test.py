import unittest

import fastly


class APITest(unittest.TestCase):

    def setUp(self):
        self.api = fastly.API()

    def test_purge(self):
        self.assertTrue(self.api.purge_url('test.com', '/'))

    def test_purge_by_key(self):
        self.api.deauthenticate()
        self.api.authenticate_by_key('TESTAPIKEY')
        self.assertTrue(self.api.purge_key('test.com', 'foo'))

    def test_cookie_purge_by_key(self):
        self.api.deauthenticate()
        self.api.authenticate_by_password('foo@example.com', 'password')
        with self.assertRaises(fastly.AuthenticationError):
            self.api.purge_key('test.com', 'foo')

    def test_soft_purge(self):
        self.api.deauthenticate()
        self.assertTrue(self.api.soft_purge_url('test.com', '/'))

    def test_soft_purge_by_key(self):
        self.api.deauthenticate()
        self.api.authenticate_by_key('TESTAPIKEY')
        self.assertTrue(self.api.soft_purge_key('test.com', 'foo'))

    def test_cookie_soft_purge_by_key(self):
        self.api.deauthenticate()
        self.api.authenticate_by_password('foo@example.com', 'password')
        with self.assertRaises(fastly.AuthenticationError):
            self.api.soft_purge_key('test.com', 'foo')

    def test_auth_error(self):
        self.api.deauthenticate()
        with self.assertRaises(fastly.AuthenticationError):
            self.api.conn.request('GET', '/current_customer')

    def test_auth_key_success(self):
        self.api.deauthenticate()
        self.api.authenticate_by_key('TESTAPIKEY')
        self.api.conn.request('GET', '/current_customer')

    def test_auth_session_success(self):
        self.api.deauthenticate()
        self.api.authenticate_by_password('foo@example.com', 'password')
        self.api.conn.request('GET', '/current_customer')

if __name__ == '__main__':
    unittest.main()
