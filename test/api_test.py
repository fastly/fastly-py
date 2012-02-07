import unittest
import fastly

class APITest(unittest.TestCase):
    def setUp(self):
        self.api = fastly.API()#host='127.0.0.1', port=5500, secure=False)

    def test_purge(self):
        self.assertTrue(self.api.purge_url('test.com', '/'))

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
        self.api.authenticate_by_password('foo@test.com', 'password')
        self.api.conn.request('GET', '/current_customer')

if __name__ == '__main__':
    unittest.main()
