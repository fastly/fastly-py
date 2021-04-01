import os
import unittest

import fastly
import fastly.models


SERVICE_ID = os.environ['FASTLY_SERVICE_ID']
API_AUTH_TOKEN = os.environ['FASTLY_API_TOKEN']
BACKEND_NAME = 'Google'
BACKEND_ADDRESS = 'google.com'
DOMAIN_NAME = 'test.fastly.redbee.dev'


class OriginUrlBoolCase(unittest.TestCase):
    def __init__(self, *args):
        super().__init__(*args)
        self.client = fastly.API(key=API_AUTH_TOKEN)

        self.service = self.client.service(SERVICE_ID)
        self.version = self.service.get_active_version_number()
        self.backend = self.client.backend(self.service.attrs['id'], self.version, BACKEND_NAME)

    def _update_backend_use_ssl(self, value):
        cloned_version = self.service.version()
        self.version = cloned_version.attrs['number']

        domain = fastly.models.Domain.construct_instance(dict(
            service_id=self.service.attrs['id'],
            version=self.version,
            name=DOMAIN_NAME,
        ), new=True)
        domain.conn = self.client.conn
        domain.save()

        backend = fastly.models.Backend.construct_instance(dict(
            service_id=self.service.attrs['id'],
            name=BACKEND_NAME,
            address=BACKEND_ADDRESS,
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
