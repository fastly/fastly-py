"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://developer.fastly.com/reference/api/)   # noqa: E501

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
from fastly.model.backend_response import BackendResponse
from fastly.model.inline_response200 import InlineResponse200


class BackendApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_backend_endpoint = _Endpoint(
            settings={
                'response_type': (BackendResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/backend',
                'operation_id': 'create_backend',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'address',
                    'auto_loadbalance',
                    'between_bytes_timeout',
                    'client_cert',
                    'comment',
                    'connect_timeout',
                    'first_byte_timeout',
                    'healthcheck',
                    'hostname',
                    'ipv4',
                    'ipv6',
                    'keepalive_time',
                    'max_conn',
                    'max_tls_version',
                    'min_tls_version',
                    'name',
                    'override_host',
                    'port',
                    'request_condition',
                    'shield',
                    'ssl_ca_cert',
                    'ssl_cert_hostname',
                    'ssl_check_cert',
                    'ssl_ciphers',
                    'ssl_client_cert',
                    'ssl_client_key',
                    'ssl_hostname',
                    'ssl_sni_hostname',
                    'use_ssl',
                    'weight',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'client_cert',
                    'comment',
                    'healthcheck',
                    'hostname',
                    'ipv4',
                    'ipv6',
                    'keepalive_time',
                    'max_tls_version',
                    'min_tls_version',
                    'override_host',
                    'shield',
                    'ssl_ca_cert',
                    'ssl_cert_hostname',
                    'ssl_ciphers',
                    'ssl_client_cert',
                    'ssl_client_key',
                    'ssl_hostname',
                    'ssl_sni_hostname',
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
                    'address':
                        (str,),
                    'auto_loadbalance':
                        (bool,),
                    'between_bytes_timeout':
                        (int,),
                    'client_cert':
                        (str, none_type,),
                    'comment':
                        (str, none_type,),
                    'connect_timeout':
                        (int,),
                    'first_byte_timeout':
                        (int,),
                    'healthcheck':
                        (str, none_type,),
                    'hostname':
                        (str, none_type,),
                    'ipv4':
                        (str, none_type,),
                    'ipv6':
                        (str, none_type,),
                    'keepalive_time':
                        (int, none_type,),
                    'max_conn':
                        (int,),
                    'max_tls_version':
                        (str, none_type,),
                    'min_tls_version':
                        (str, none_type,),
                    'name':
                        (str,),
                    'override_host':
                        (str, none_type,),
                    'port':
                        (int,),
                    'request_condition':
                        (str,),
                    'shield':
                        (str, none_type,),
                    'ssl_ca_cert':
                        (str, none_type,),
                    'ssl_cert_hostname':
                        (str, none_type,),
                    'ssl_check_cert':
                        (bool,),
                    'ssl_ciphers':
                        (str, none_type,),
                    'ssl_client_cert':
                        (str, none_type,),
                    'ssl_client_key':
                        (str, none_type,),
                    'ssl_hostname':
                        (str, none_type,),
                    'ssl_sni_hostname':
                        (str, none_type,),
                    'use_ssl':
                        (bool,),
                    'weight':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'address': 'address',
                    'auto_loadbalance': 'auto_loadbalance',
                    'between_bytes_timeout': 'between_bytes_timeout',
                    'client_cert': 'client_cert',
                    'comment': 'comment',
                    'connect_timeout': 'connect_timeout',
                    'first_byte_timeout': 'first_byte_timeout',
                    'healthcheck': 'healthcheck',
                    'hostname': 'hostname',
                    'ipv4': 'ipv4',
                    'ipv6': 'ipv6',
                    'keepalive_time': 'keepalive_time',
                    'max_conn': 'max_conn',
                    'max_tls_version': 'max_tls_version',
                    'min_tls_version': 'min_tls_version',
                    'name': 'name',
                    'override_host': 'override_host',
                    'port': 'port',
                    'request_condition': 'request_condition',
                    'shield': 'shield',
                    'ssl_ca_cert': 'ssl_ca_cert',
                    'ssl_cert_hostname': 'ssl_cert_hostname',
                    'ssl_check_cert': 'ssl_check_cert',
                    'ssl_ciphers': 'ssl_ciphers',
                    'ssl_client_cert': 'ssl_client_cert',
                    'ssl_client_key': 'ssl_client_key',
                    'ssl_hostname': 'ssl_hostname',
                    'ssl_sni_hostname': 'ssl_sni_hostname',
                    'use_ssl': 'use_ssl',
                    'weight': 'weight',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'address': 'form',
                    'auto_loadbalance': 'form',
                    'between_bytes_timeout': 'form',
                    'client_cert': 'form',
                    'comment': 'form',
                    'connect_timeout': 'form',
                    'first_byte_timeout': 'form',
                    'healthcheck': 'form',
                    'hostname': 'form',
                    'ipv4': 'form',
                    'ipv6': 'form',
                    'keepalive_time': 'form',
                    'max_conn': 'form',
                    'max_tls_version': 'form',
                    'min_tls_version': 'form',
                    'name': 'form',
                    'override_host': 'form',
                    'port': 'form',
                    'request_condition': 'form',
                    'shield': 'form',
                    'ssl_ca_cert': 'form',
                    'ssl_cert_hostname': 'form',
                    'ssl_check_cert': 'form',
                    'ssl_ciphers': 'form',
                    'ssl_client_cert': 'form',
                    'ssl_client_key': 'form',
                    'ssl_hostname': 'form',
                    'ssl_sni_hostname': 'form',
                    'use_ssl': 'form',
                    'weight': 'form',
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
        self.delete_backend_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/backend/{backend_name}',
                'operation_id': 'delete_backend',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'backend_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'backend_name',
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
                    'backend_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'backend_name': 'backend_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'backend_name': 'path',
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
        self.get_backend_endpoint = _Endpoint(
            settings={
                'response_type': (BackendResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/backend/{backend_name}',
                'operation_id': 'get_backend',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'backend_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'backend_name',
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
                    'backend_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'backend_name': 'backend_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'backend_name': 'path',
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
        self.list_backends_endpoint = _Endpoint(
            settings={
                'response_type': ([BackendResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/backend',
                'operation_id': 'list_backends',
                'http_method': 'GET',
                'servers': None,
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
        self.update_backend_endpoint = _Endpoint(
            settings={
                'response_type': (BackendResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/backend/{backend_name}',
                'operation_id': 'update_backend',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'backend_name',
                    'address',
                    'auto_loadbalance',
                    'between_bytes_timeout',
                    'client_cert',
                    'comment',
                    'connect_timeout',
                    'first_byte_timeout',
                    'healthcheck',
                    'hostname',
                    'ipv4',
                    'ipv6',
                    'keepalive_time',
                    'max_conn',
                    'max_tls_version',
                    'min_tls_version',
                    'name',
                    'override_host',
                    'port',
                    'request_condition',
                    'shield',
                    'ssl_ca_cert',
                    'ssl_cert_hostname',
                    'ssl_check_cert',
                    'ssl_ciphers',
                    'ssl_client_cert',
                    'ssl_client_key',
                    'ssl_hostname',
                    'ssl_sni_hostname',
                    'use_ssl',
                    'weight',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'backend_name',
                ],
                'nullable': [
                    'client_cert',
                    'comment',
                    'healthcheck',
                    'hostname',
                    'ipv4',
                    'ipv6',
                    'keepalive_time',
                    'max_tls_version',
                    'min_tls_version',
                    'override_host',
                    'shield',
                    'ssl_ca_cert',
                    'ssl_cert_hostname',
                    'ssl_ciphers',
                    'ssl_client_cert',
                    'ssl_client_key',
                    'ssl_hostname',
                    'ssl_sni_hostname',
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
                    'backend_name':
                        (str,),
                    'address':
                        (str,),
                    'auto_loadbalance':
                        (bool,),
                    'between_bytes_timeout':
                        (int,),
                    'client_cert':
                        (str, none_type,),
                    'comment':
                        (str, none_type,),
                    'connect_timeout':
                        (int,),
                    'first_byte_timeout':
                        (int,),
                    'healthcheck':
                        (str, none_type,),
                    'hostname':
                        (str, none_type,),
                    'ipv4':
                        (str, none_type,),
                    'ipv6':
                        (str, none_type,),
                    'keepalive_time':
                        (int, none_type,),
                    'max_conn':
                        (int,),
                    'max_tls_version':
                        (str, none_type,),
                    'min_tls_version':
                        (str, none_type,),
                    'name':
                        (str,),
                    'override_host':
                        (str, none_type,),
                    'port':
                        (int,),
                    'request_condition':
                        (str,),
                    'shield':
                        (str, none_type,),
                    'ssl_ca_cert':
                        (str, none_type,),
                    'ssl_cert_hostname':
                        (str, none_type,),
                    'ssl_check_cert':
                        (bool,),
                    'ssl_ciphers':
                        (str, none_type,),
                    'ssl_client_cert':
                        (str, none_type,),
                    'ssl_client_key':
                        (str, none_type,),
                    'ssl_hostname':
                        (str, none_type,),
                    'ssl_sni_hostname':
                        (str, none_type,),
                    'use_ssl':
                        (bool,),
                    'weight':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'backend_name': 'backend_name',
                    'address': 'address',
                    'auto_loadbalance': 'auto_loadbalance',
                    'between_bytes_timeout': 'between_bytes_timeout',
                    'client_cert': 'client_cert',
                    'comment': 'comment',
                    'connect_timeout': 'connect_timeout',
                    'first_byte_timeout': 'first_byte_timeout',
                    'healthcheck': 'healthcheck',
                    'hostname': 'hostname',
                    'ipv4': 'ipv4',
                    'ipv6': 'ipv6',
                    'keepalive_time': 'keepalive_time',
                    'max_conn': 'max_conn',
                    'max_tls_version': 'max_tls_version',
                    'min_tls_version': 'min_tls_version',
                    'name': 'name',
                    'override_host': 'override_host',
                    'port': 'port',
                    'request_condition': 'request_condition',
                    'shield': 'shield',
                    'ssl_ca_cert': 'ssl_ca_cert',
                    'ssl_cert_hostname': 'ssl_cert_hostname',
                    'ssl_check_cert': 'ssl_check_cert',
                    'ssl_ciphers': 'ssl_ciphers',
                    'ssl_client_cert': 'ssl_client_cert',
                    'ssl_client_key': 'ssl_client_key',
                    'ssl_hostname': 'ssl_hostname',
                    'ssl_sni_hostname': 'ssl_sni_hostname',
                    'use_ssl': 'use_ssl',
                    'weight': 'weight',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'backend_name': 'path',
                    'address': 'form',
                    'auto_loadbalance': 'form',
                    'between_bytes_timeout': 'form',
                    'client_cert': 'form',
                    'comment': 'form',
                    'connect_timeout': 'form',
                    'first_byte_timeout': 'form',
                    'healthcheck': 'form',
                    'hostname': 'form',
                    'ipv4': 'form',
                    'ipv6': 'form',
                    'keepalive_time': 'form',
                    'max_conn': 'form',
                    'max_tls_version': 'form',
                    'min_tls_version': 'form',
                    'name': 'form',
                    'override_host': 'form',
                    'port': 'form',
                    'request_condition': 'form',
                    'shield': 'form',
                    'ssl_ca_cert': 'form',
                    'ssl_cert_hostname': 'form',
                    'ssl_check_cert': 'form',
                    'ssl_ciphers': 'form',
                    'ssl_client_cert': 'form',
                    'ssl_client_key': 'form',
                    'ssl_hostname': 'form',
                    'ssl_sni_hostname': 'form',
                    'use_ssl': 'form',
                    'weight': 'form',
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

    def create_backend(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a backend  # noqa: E501

        Create a backend for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_backend(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            address (str): A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend.. [optional]
            auto_loadbalance (bool): Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a `request_condition` will be selected based on their `weight`.. [optional]
            between_bytes_timeout (int): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional]
            client_cert (str, none_type): Unused.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            connect_timeout (int): Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`.. [optional]
            first_byte_timeout (int): Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`.. [optional]
            healthcheck (str, none_type): The name of the healthcheck to use with this backend.. [optional]
            hostname (str, none_type): The hostname of the backend. May be used as an alternative to `address` to set the backend location.. [optional]
            ipv4 (str, none_type): IPv4 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]
            ipv6 (str, none_type): IPv6 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]
            keepalive_time (int, none_type): How long to keep a persistent connection to the backend between requests.. [optional]
            max_conn (int): Maximum number of concurrent connections this backend will accept.. [optional]
            max_tls_version (str, none_type): Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]
            min_tls_version (str, none_type): Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]
            name (str): The name of the backend.. [optional]
            override_host (str, none_type): If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL.. [optional]
            port (int): Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request.. [optional]
            request_condition (str): Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests.. [optional]
            shield (str, none_type): Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding).. [optional]
            ssl_ca_cert (str, none_type): CA certificate attached to origin.. [optional]
            ssl_cert_hostname (str, none_type): Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all.. [optional]
            ssl_check_cert (bool): Be strict on checking SSL certs.. [optional] if omitted the server will use the default value of True
            ssl_ciphers (str, none_type): List of [OpenSSL ciphers](https://www.openssl.org/docs/manmaster/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]
            ssl_client_cert (str, none_type): Client certificate attached to origin.. [optional]
            ssl_client_key (str, none_type): Client key attached to origin.. [optional]
            ssl_hostname (str, none_type): Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation.. [optional]
            ssl_sni_hostname (str, none_type): Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all.. [optional]
            use_ssl (bool): Whether or not to require TLS for connections to this backend.. [optional]
            weight (int): Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true.. [optional]
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
            BackendResponse
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
        return self.create_backend_endpoint.call_with_http_info(**kwargs)

    def delete_backend(
        self,
        service_id,
        version_id,
        backend_name,
        **kwargs
    ):
        """Delete a backend  # noqa: E501

        Delete the backend for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_backend(service_id, version_id, backend_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            backend_name (str): The name of the backend.

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
        kwargs['backend_name'] = \
            backend_name
        return self.delete_backend_endpoint.call_with_http_info(**kwargs)

    def get_backend(
        self,
        service_id,
        version_id,
        backend_name,
        **kwargs
    ):
        """Describe a backend  # noqa: E501

        Get the backend for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_backend(service_id, version_id, backend_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            backend_name (str): The name of the backend.

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
            BackendResponse
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
        kwargs['backend_name'] = \
            backend_name
        return self.get_backend_endpoint.call_with_http_info(**kwargs)

    def list_backends(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List backends  # noqa: E501

        List all backends for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_backends(service_id, version_id, async_req=True)
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
            [BackendResponse]
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
        return self.list_backends_endpoint.call_with_http_info(**kwargs)

    def update_backend(
        self,
        service_id,
        version_id,
        backend_name,
        **kwargs
    ):
        """Update a backend  # noqa: E501

        Update the backend for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_backend(service_id, version_id, backend_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            backend_name (str): The name of the backend.

        Keyword Args:
            address (str): A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend.. [optional]
            auto_loadbalance (bool): Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a `request_condition` will be selected based on their `weight`.. [optional]
            between_bytes_timeout (int): Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`.. [optional]
            client_cert (str, none_type): Unused.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            connect_timeout (int): Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`.. [optional]
            first_byte_timeout (int): Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthethic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`.. [optional]
            healthcheck (str, none_type): The name of the healthcheck to use with this backend.. [optional]
            hostname (str, none_type): The hostname of the backend. May be used as an alternative to `address` to set the backend location.. [optional]
            ipv4 (str, none_type): IPv4 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]
            ipv6 (str, none_type): IPv6 address of the backend. May be used as an alternative to `address` to set the backend location.. [optional]
            keepalive_time (int, none_type): How long to keep a persistent connection to the backend between requests.. [optional]
            max_conn (int): Maximum number of concurrent connections this backend will accept.. [optional]
            max_tls_version (str, none_type): Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]
            min_tls_version (str, none_type): Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]
            name (str): The name of the backend.. [optional]
            override_host (str, none_type): If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL.. [optional]
            port (int): Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request.. [optional]
            request_condition (str): Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests.. [optional]
            shield (str, none_type): Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding).. [optional]
            ssl_ca_cert (str, none_type): CA certificate attached to origin.. [optional]
            ssl_cert_hostname (str, none_type): Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all.. [optional]
            ssl_check_cert (bool): Be strict on checking SSL certs.. [optional] if omitted the server will use the default value of True
            ssl_ciphers (str, none_type): List of [OpenSSL ciphers](https://www.openssl.org/docs/manmaster/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated.. [optional]
            ssl_client_cert (str, none_type): Client certificate attached to origin.. [optional]
            ssl_client_key (str, none_type): Client key attached to origin.. [optional]
            ssl_hostname (str, none_type): Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation.. [optional]
            ssl_sni_hostname (str, none_type): Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all.. [optional]
            use_ssl (bool): Whether or not to require TLS for connections to this backend.. [optional]
            weight (int): Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true.. [optional]
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
            BackendResponse
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
        kwargs['backend_name'] = \
            backend_name
        return self.update_backend_endpoint.call_with_http_info(**kwargs)

