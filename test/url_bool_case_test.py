import os
import unittest

import fastly
import fastly.models


class OriginUrlBoolCase(unittest.TestCase):
    def setUp(self):
        self.api = fastly.API()
        self.api_key = os.environ.get('FASTLY_API_KEY', 'TESTAPIKEY')
        self.backend_address = os.environ.get('FASTLY_SERVICE_BACKEND_ADDRESS', 'example.com')
        self.backend_name = os.environ.get('FASTLY_SERVICE_BACKEND_NAME', 'Example')
        self.domain_name = os.environ.get('FASTLY_SERVICE_DOMAIN', 'test.example.com')
        self.host = os.environ.get('FASTLY_SERVICE_HOST', 'test.com')
        self.service_id = os.environ.get('FASTLY_SERVICE_ID', 'test.com')

        self.client = fastly.API(key=self.api_key)
        self.service = self.client.service(self.service_id)
        self.version = self.service.get_active_version_number()
        self.backend = self.client.backend(self.service.attrs['id'], self.version, self.backend_name)

    def _update_backend_use_ssl(self, value):
        cloned_version = self.service.version()
        self.version = cloned_version.attrs['number']

        domain = fastly.models.Domain.construct_instance(dict(
            service_id=self.service.attrs['id'],
            version=self.version,
            name=self.domain_name,
        ), new=True)
        domain.conn = self.client.conn
        domain.save()

        backend = fastly.models.Backend.construct_instance(dict(
            service_id=self.service.attrs['id'],
            name=self.backend_name,
            address=self.backend_address,
            use_ssl=value,
            version=self.version,
        ), new=True)
        backend.conn = self.client.conn
        backend.save()

        cloned_version.activate()

        return self.client.backend(self.service.attrs['id'], self.version, backend.attrs['name'])

    def test_should_update_use_ssl__for_lowercase_flag(self):
        start_state = self.backend.attrs['use_ssl']

        test_states = [
            not start_state,
            start_state,
        ]
        for new_state in test_states:
            backend = self._update_backend_use_ssl(str(new_state).lower())
            self.assertEqual(
                backend.attrs['use_ssl'],
                new_state,
                'Expected use_ssl to be {} when set to string {}'.format(new_state, str(new_state).lower()),
            )

    def test_should_update_use_ssl__for_boolean_flag(self):
        start_state = self.backend.attrs['use_ssl']

        test_states = [
            not start_state,
            start_state,
        ]
        for new_state in test_states:
            backend = self._update_backend_use_ssl(new_state)
            print('Set to', new_state, '<>', backend.attrs['use_ssl'])
            self.assertEqual(
                backend.attrs['use_ssl'],
                new_state,
                'Expected use_ssl to be {} when set to boolean {}'.format(new_state, new_state),
            )
