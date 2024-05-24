"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://www.fastly.com/documentation/reference/api/)   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: oss@fastly.com
"""


import re  # noqa: F401
import sys  # noqa: F401

from fastly.api_client import ApiClient, Endpoint as _Endpoint
from fastly.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.pool_response import PoolResponse
from fastly.model.pool_response_post import PoolResponsePost


class PoolApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_server_pool_endpoint = _Endpoint(
            settings={
                'response_type': (PoolResponsePost,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/pool',
                'operation_id': 'create_server_pool',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_cert_hostname',
                    'use_tls',
                    'created_at',
                    'deleted_at',
                    'updated_at',
                    'service_id2',
                    'version',
                    'name',
                    'shield',
                    'request_condition',
                    'tls_ciphers',
                    'tls_sni_hostname',
                    'min_tls_version',
                    'max_tls_version',
                    'healthcheck',
                    'comment',
                    'type',
                    'override_host',
                    'between_bytes_timeout',
                    'connect_timeout',
                    'first_byte_timeout',
                    'max_conn_default',
                    'quorum',
                    'tls_check_cert',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_cert_hostname',
                    'created_at',
                    'deleted_at',
                    'updated_at',
                    'shield',
                    'request_condition',
                    'tls_ciphers',
                    'tls_sni_hostname',
                    'min_tls_version',
                    'max_tls_version',
                    'healthcheck',
                    'comment',
                    'override_host',
                    'tls_check_cert',
                ],
                'enum': [
                    'use_tls',
                    'type',
                ],
                'validation': [
                    'quorum',
                ]
            },
            root_map={
                'validations': {
                    ('quorum',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                    ('use_tls',): {

                        "no_tls": 0,
                        "use_tls": 1
                    },
                    ('type',): {

                        "RANDOM": "random",
                        "HASH": "hash",
                        "CLIENT": "client"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'tls_ca_cert':
                        (str, none_type,),
                    'tls_client_cert':
                        (str, none_type,),
                    'tls_client_key':
                        (str, none_type,),
                    'tls_cert_hostname':
                        (str, none_type,),
                    'use_tls':
                        (int,),
                    'created_at':
                        (datetime, none_type,),
                    'deleted_at':
                        (datetime, none_type,),
                    'updated_at':
                        (datetime, none_type,),
                    'service_id2':
                        (str,),
                    'version':
                        (str,),
                    'name':
                        (str,),
                    'shield':
                        (str, none_type,),
                    'request_condition':
                        (str, none_type,),
                    'tls_ciphers':
                        (str, none_type,),
                    'tls_sni_hostname':
                        (str, none_type,),
                    'min_tls_version':
                        (int, none_type,),
                    'max_tls_version':
                        (int, none_type,),
                    'healthcheck':
                        (str, none_type,),
                    'comment':
                        (str, none_type,),
                    'type':
                        (str,),
                    'override_host':
                        (str, none_type,),
                    'between_bytes_timeout':
                        (int,),
                    'connect_timeout':
                        (int,),
                    'first_byte_timeout':
                        (int,),
                    'max_conn_default':
                        (int,),
                    'quorum':
                        (int,),
                    'tls_check_cert':
                        (int, none_type,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'tls_ca_cert': 'tls_ca_cert',
                    'tls_client_cert': 'tls_client_cert',
                    'tls_client_key': 'tls_client_key',
                    'tls_cert_hostname': 'tls_cert_hostname',
                    'use_tls': 'use_tls',
                    'created_at': 'created_at',
                    'deleted_at': 'deleted_at',
                    'updated_at': 'updated_at',
                    'service_id2': 'service_id',
                    'version': 'version',
                    'name': 'name',
                    'shield': 'shield',
                    'request_condition': 'request_condition',
                    'tls_ciphers': 'tls_ciphers',
                    'tls_sni_hostname': 'tls_sni_hostname',
                    'min_tls_version': 'min_tls_version',
                    'max_tls_version': 'max_tls_version',
                    'healthcheck': 'healthcheck',
                    'comment': 'comment',
                    'type': 'type',
                    'override_host': 'override_host',
                    'between_bytes_timeout': 'between_bytes_timeout',
                    'connect_timeout': 'connect_timeout',
                    'first_byte_timeout': 'first_byte_timeout',
                    'max_conn_default': 'max_conn_default',
                    'quorum': 'quorum',
                    'tls_check_cert': 'tls_check_cert',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'tls_ca_cert': 'form',
                    'tls_client_cert': 'form',
                    'tls_client_key': 'form',
                    'tls_cert_hostname': 'form',
                    'use_tls': 'form',
                    'created_at': 'form',
                    'deleted_at': 'form',
                    'updated_at': 'form',
                    'service_id2': 'form',
                    'version': 'form',
                    'name': 'form',
                    'shield': 'form',
                    'request_condition': 'form',
                    'tls_ciphers': 'form',
                    'tls_sni_hostname': 'form',
                    'min_tls_version': 'form',
                    'max_tls_version': 'form',
                    'healthcheck': 'form',
                    'comment': 'form',
                    'type': 'form',
                    'override_host': 'form',
                    'between_bytes_timeout': 'form',
                    'connect_timeout': 'form',
                    'first_byte_timeout': 'form',
                    'max_conn_default': 'form',
                    'quorum': 'form',
                    'tls_check_cert': 'form',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )
        self.delete_server_pool_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/pool/{pool_name}',
                'operation_id': 'delete_server_pool',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'pool_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'pool_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'pool_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'pool_name': 'pool_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'pool_name': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_server_pool_endpoint = _Endpoint(
            settings={
                'response_type': (PoolResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/pool/{pool_name}',
                'operation_id': 'get_server_pool',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'pool_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'pool_name',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'pool_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'pool_name': 'pool_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'pool_name': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_server_pools_endpoint = _Endpoint(
            settings={
                'response_type': ([PoolResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/pool',
                'operation_id': 'list_server_pools',
                'http_method': 'GET',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.update_server_pool_endpoint = _Endpoint(
            settings={
                'response_type': (PoolResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/pool/{pool_name}',
                'operation_id': 'update_server_pool',
                'http_method': 'PUT',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'pool_name',
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_cert_hostname',
                    'use_tls',
                    'created_at',
                    'deleted_at',
                    'updated_at',
                    'service_id2',
                    'version',
                    'name',
                    'shield',
                    'request_condition',
                    'tls_ciphers',
                    'tls_sni_hostname',
                    'min_tls_version',
                    'max_tls_version',
                    'healthcheck',
                    'comment',
                    'type',
                    'override_host',
                    'between_bytes_timeout',
                    'connect_timeout',
                    'first_byte_timeout',
                    'max_conn_default',
                    'quorum',
                    'tls_check_cert',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'pool_name',
                ],
                'nullable': [
                    'tls_ca_cert',
                    'tls_client_cert',
                    'tls_client_key',
                    'tls_cert_hostname',
                    'created_at',
                    'deleted_at',
                    'updated_at',
                    'shield',
                    'request_condition',
                    'tls_ciphers',
                    'tls_sni_hostname',
                    'min_tls_version',
                    'max_tls_version',
                    'healthcheck',
                    'comment',
                    'override_host',
                    'tls_check_cert',
                ],
                'enum': [
                    'use_tls',
                    'type',
                ],
                'validation': [
                    'quorum',
                ]
            },
            root_map={
                'validations': {
                    ('quorum',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                    ('use_tls',): {

                        "no_tls": 0,
                        "use_tls": 1
                    },
                    ('type',): {

                        "RANDOM": "random",
                        "HASH": "hash",
                        "CLIENT": "client"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'pool_name':
                        (str,),
                    'tls_ca_cert':
                        (str, none_type,),
                    'tls_client_cert':
                        (str, none_type,),
                    'tls_client_key':
                        (str, none_type,),
                    'tls_cert_hostname':
                        (str, none_type,),
                    'use_tls':
                        (int,),
                    'created_at':
                        (datetime, none_type,),
                    'deleted_at':
                        (datetime, none_type,),
                    'updated_at':
                        (datetime, none_type,),
                    'service_id2':
                        (str,),
                    'version':
                        (str,),
                    'name':
                        (str,),
                    'shield':
                        (str, none_type,),
                    'request_condition':
                        (str, none_type,),
                    'tls_ciphers':
                        (str, none_type,),
                    'tls_sni_hostname':
                        (str, none_type,),
                    'min_tls_version':
                        (int, none_type,),
                    'max_tls_version':
                        (int, none_type,),
                    'healthcheck':
                        (str, none_type,),
                    'comment':
                        (str, none_type,),
                    'type':
                        (str,),
                    'override_host':
                        (str, none_type,),
                    'between_bytes_timeout':
                        (int,),
                    'connect_timeout':
                        (int,),
                    'first_byte_timeout':
                        (int,),
                    'max_conn_default':
                        (int,),
                    'quorum':
                        (int,),
                    'tls_check_cert':
                        (int, none_type,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'pool_name': 'pool_name',
                    'tls_ca_cert': 'tls_ca_cert',
                    'tls_client_cert': 'tls_client_cert',
                    'tls_client_key': 'tls_client_key',
                    'tls_cert_hostname': 'tls_cert_hostname',
                    'use_tls': 'use_tls',
                    'created_at': 'created_at',
                    'deleted_at': 'deleted_at',
                    'updated_at': 'updated_at',
                    'service_id2': 'service_id',
                    'version': 'version',
                    'name': 'name',
                    'shield': 'shield',
                    'request_condition': 'request_condition',
                    'tls_ciphers': 'tls_ciphers',
                    'tls_sni_hostname': 'tls_sni_hostname',
                    'min_tls_version': 'min_tls_version',
                    'max_tls_version': 'max_tls_version',
                    'healthcheck': 'healthcheck',
                    'comment': 'comment',
                    'type': 'type',
                    'override_host': 'override_host',
                    'between_bytes_timeout': 'between_bytes_timeout',
                    'connect_timeout': 'connect_timeout',
                    'first_byte_timeout': 'first_byte_timeout',
                    'max_conn_default': 'max_conn_default',
                    'quorum': 'quorum',
                    'tls_check_cert': 'tls_check_cert',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'pool_name': 'path',
                    'tls_ca_cert': 'form',
                    'tls_client_cert': 'form',
                    'tls_client_key': 'form',
                    'tls_cert_hostname': 'form',
                    'use_tls': 'form',
                    'created_at': 'form',
                    'deleted_at': 'form',
                    'updated_at': 'form',
                    'service_id2': 'form',
                    'version': 'form',
                    'name': 'form',
                    'shield': 'form',
                    'request_condition': 'form',
                    'tls_ciphers': 'form',
                    'tls_sni_hostname': 'form',
                    'min_tls_version': 'form',
                    'max_tls_version': 'form',
                    'healthcheck': 'form',
                    'comment': 'form',
                    'type': 'form',
                    'override_host': 'form',
                    'between_bytes_timeout': 'form',
                    'connect_timeout': 'form',
                    'first_byte_timeout': 'form',
                    'max_conn_default': 'form',
                    'quorum': 'form',
                    'tls_check_cert': 'form',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/x-www-form-urlencoded'
                ]
            },
            api_client=api_client
        )

    def create_server_pool(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a server pool  # noqa: E501

        Creates a pool for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_server_pool(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_cert_hostname (str, none_type): The hostname used to verify a server's certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN).. [optional] if omitted the server will use the default value of "null"
            use_tls (int): Whether to use TLS.. [optional] if omitted the server will use the default value of 0
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            service_id2 (str): [optional]
            version (str): [optional]
            name (str): Name for the Pool.. [optional]
            shield (str, none_type): Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding.. [optional] if omitted the server will use the default value of "null"
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]
            tls_ciphers (str, none_type): List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional.. [optional]
            tls_sni_hostname (str, none_type): SNI hostname. Optional.. [optional]
            min_tls_version (int, none_type): Minimum allowed TLS version on connections to this server. Optional.. [optional]
            max_tls_version (int, none_type): Maximum allowed TLS version on connections to this server. Optional.. [optional]
            healthcheck (str, none_type): Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            type (str): What type of load balance group to use.. [optional]
            override_host (str, none_type): The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting.. [optional] if omitted the server will use the default value of "null"
            between_bytes_timeout (int): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional] if omitted the server will use the default value of 10000
            connect_timeout (int): How long to wait for a timeout in milliseconds. Optional.. [optional]
            first_byte_timeout (int): How long to wait for the first byte in milliseconds. Optional.. [optional]
            max_conn_default (int): Maximum number of connections. Optional.. [optional] if omitted the server will use the default value of 200
            quorum (int): Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up.. [optional] if omitted the server will use the default value of 75
            tls_check_cert (int, none_type): Be strict on checking TLS certs. Optional.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PoolResponsePost
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        return self.create_server_pool_endpoint.call_with_http_info(**kwargs)

    def delete_server_pool(
        self,
        service_id,
        version_id,
        pool_name,
        **kwargs
    ):
        """Delete a server pool  # noqa: E501

        Deletes a specific pool for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_server_pool(service_id, version_id, pool_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            pool_name (str): Name for the Pool.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            InlineResponse200
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['pool_name'] = \
            pool_name
        return self.delete_server_pool_endpoint.call_with_http_info(**kwargs)

    def get_server_pool(
        self,
        service_id,
        version_id,
        pool_name,
        **kwargs
    ):
        """Get a server pool  # noqa: E501

        Gets a single pool for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_server_pool(service_id, version_id, pool_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            pool_name (str): Name for the Pool.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PoolResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['pool_name'] = \
            pool_name
        return self.get_server_pool_endpoint.call_with_http_info(**kwargs)

    def list_server_pools(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List server pools  # noqa: E501

        Lists all pools for a particular service and pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_server_pools(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            [PoolResponse]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        return self.list_server_pools_endpoint.call_with_http_info(**kwargs)

    def update_server_pool(
        self,
        service_id,
        version_id,
        pool_name,
        **kwargs
    ):
        """Update a server pool  # noqa: E501

        Updates a specific pool for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_server_pool(service_id, version_id, pool_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            pool_name (str): Name for the Pool.

        Keyword Args:
            tls_ca_cert (str, none_type): A secure certificate to authenticate a server with. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_cert (str, none_type): The client certificate used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_client_key (str, none_type): The client private key used to make authenticated requests. Must be in PEM format.. [optional] if omitted the server will use the default value of "null"
            tls_cert_hostname (str, none_type): The hostname used to verify a server's certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN).. [optional] if omitted the server will use the default value of "null"
            use_tls (int): Whether to use TLS.. [optional] if omitted the server will use the default value of 0
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            service_id2 (str): [optional]
            version (str): [optional]
            name (str): Name for the Pool.. [optional]
            shield (str, none_type): Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding.. [optional] if omitted the server will use the default value of "null"
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]
            tls_ciphers (str, none_type): List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional.. [optional]
            tls_sni_hostname (str, none_type): SNI hostname. Optional.. [optional]
            min_tls_version (int, none_type): Minimum allowed TLS version on connections to this server. Optional.. [optional]
            max_tls_version (int, none_type): Maximum allowed TLS version on connections to this server. Optional.. [optional]
            healthcheck (str, none_type): Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            type (str): What type of load balance group to use.. [optional]
            override_host (str, none_type): The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting.. [optional] if omitted the server will use the default value of "null"
            between_bytes_timeout (int): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional] if omitted the server will use the default value of 10000
            connect_timeout (int): How long to wait for a timeout in milliseconds. Optional.. [optional]
            first_byte_timeout (int): How long to wait for the first byte in milliseconds. Optional.. [optional]
            max_conn_default (int): Maximum number of connections. Optional.. [optional] if omitted the server will use the default value of 200
            quorum (int): Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up.. [optional] if omitted the server will use the default value of 75
            tls_check_cert (int, none_type): Be strict on checking TLS certs. Optional.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            PoolResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['pool_name'] = \
            pool_name
        return self.update_server_pool_endpoint.call_with_http_info(**kwargs)

