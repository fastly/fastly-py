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
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.server_response import ServerResponse


class ServerApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_pool_server_endpoint = _Endpoint(
            settings={
                'response_type': (ServerResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/pool/{pool_id}/server',
                'operation_id': 'create_pool_server',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'pool_id',
                    'weight',
                    'max_conn',
                    'port',
                    'address',
                    'comment',
                    'disabled',
                    'override_host',
                ],
                'required': [
                    'service_id',
                    'pool_id',
                ],
                'nullable': [
                    'comment',
                    'override_host',
                ],
                'enum': [
                ],
                'validation': [
                    'weight',
                ]
            },
            root_map={
                'validations': {
                    ('weight',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'pool_id':
                        (str,),
                    'weight':
                        (int,),
                    'max_conn':
                        (int,),
                    'port':
                        (int,),
                    'address':
                        (str,),
                    'comment':
                        (str, none_type,),
                    'disabled':
                        (bool,),
                    'override_host':
                        (str, none_type,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'pool_id': 'pool_id',
                    'weight': 'weight',
                    'max_conn': 'max_conn',
                    'port': 'port',
                    'address': 'address',
                    'comment': 'comment',
                    'disabled': 'disabled',
                    'override_host': 'override_host',
                },
                'location_map': {
                    'service_id': 'path',
                    'pool_id': 'path',
                    'weight': 'form',
                    'max_conn': 'form',
                    'port': 'form',
                    'address': 'form',
                    'comment': 'form',
                    'disabled': 'form',
                    'override_host': 'form',
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
        self.delete_pool_server_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/pool/{pool_id}/server/{server_id}',
                'operation_id': 'delete_pool_server',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'pool_id',
                    'server_id',
                ],
                'required': [
                    'service_id',
                    'pool_id',
                    'server_id',
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
                    'pool_id':
                        (str,),
                    'server_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'pool_id': 'pool_id',
                    'server_id': 'server_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'pool_id': 'path',
                    'server_id': 'path',
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
        self.get_pool_server_endpoint = _Endpoint(
            settings={
                'response_type': (ServerResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/pool/{pool_id}/server/{server_id}',
                'operation_id': 'get_pool_server',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'pool_id',
                    'server_id',
                ],
                'required': [
                    'service_id',
                    'pool_id',
                    'server_id',
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
                    'pool_id':
                        (str,),
                    'server_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'pool_id': 'pool_id',
                    'server_id': 'server_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'pool_id': 'path',
                    'server_id': 'path',
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
        self.list_pool_servers_endpoint = _Endpoint(
            settings={
                'response_type': ([ServerResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/pool/{pool_id}/servers',
                'operation_id': 'list_pool_servers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'pool_id',
                ],
                'required': [
                    'service_id',
                    'pool_id',
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
                    'pool_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'pool_id': 'pool_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'pool_id': 'path',
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
        self.update_pool_server_endpoint = _Endpoint(
            settings={
                'response_type': (ServerResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/pool/{pool_id}/server/{server_id}',
                'operation_id': 'update_pool_server',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'pool_id',
                    'server_id',
                    'weight',
                    'max_conn',
                    'port',
                    'address',
                    'comment',
                    'disabled',
                    'override_host',
                ],
                'required': [
                    'service_id',
                    'pool_id',
                    'server_id',
                ],
                'nullable': [
                    'comment',
                    'override_host',
                ],
                'enum': [
                ],
                'validation': [
                    'weight',
                ]
            },
            root_map={
                'validations': {
                    ('weight',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'pool_id':
                        (str,),
                    'server_id':
                        (str,),
                    'weight':
                        (int,),
                    'max_conn':
                        (int,),
                    'port':
                        (int,),
                    'address':
                        (str,),
                    'comment':
                        (str, none_type,),
                    'disabled':
                        (bool,),
                    'override_host':
                        (str, none_type,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'pool_id': 'pool_id',
                    'server_id': 'server_id',
                    'weight': 'weight',
                    'max_conn': 'max_conn',
                    'port': 'port',
                    'address': 'address',
                    'comment': 'comment',
                    'disabled': 'disabled',
                    'override_host': 'override_host',
                },
                'location_map': {
                    'service_id': 'path',
                    'pool_id': 'path',
                    'server_id': 'path',
                    'weight': 'form',
                    'max_conn': 'form',
                    'port': 'form',
                    'address': 'form',
                    'comment': 'form',
                    'disabled': 'form',
                    'override_host': 'form',
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

    def create_pool_server(
        self,
        service_id,
        pool_id,
        **kwargs
    ):
        """Add a server to a pool  # noqa: E501

        Creates a single server for a particular service and pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_pool_server(service_id, pool_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            pool_id (str): Alphanumeric string identifying a Pool.

        Keyword Args:
            weight (int): Weight (`1-100`) used to load balance this server against others.. [optional] if omitted the server will use the default value of 100
            max_conn (int): Maximum number of connections. If the value is `0`, it inherits the value from pool's `max_conn_default`.. [optional] if omitted the server will use the default value of 0
            port (int): Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS.. [optional] if omitted the server will use the default value of 80
            address (str): A hostname, IPv4, or IPv6 address for the server. Required.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            disabled (bool): Allows servers to be enabled and disabled in a pool.. [optional] if omitted the server will use the default value of False
            override_host (str, none_type): The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting.. [optional] if omitted the server will use the default value of "null"
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
            ServerResponse
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
        kwargs['pool_id'] = \
            pool_id
        return self.create_pool_server_endpoint.call_with_http_info(**kwargs)

    def delete_pool_server(
        self,
        service_id,
        pool_id,
        server_id,
        **kwargs
    ):
        """Delete a server from a pool  # noqa: E501

        Deletes a single server for a particular service and pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_pool_server(service_id, pool_id, server_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            pool_id (str): Alphanumeric string identifying a Pool.
            server_id (str): Alphanumeric string identifying a Server.

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
        kwargs['pool_id'] = \
            pool_id
        kwargs['server_id'] = \
            server_id
        return self.delete_pool_server_endpoint.call_with_http_info(**kwargs)

    def get_pool_server(
        self,
        service_id,
        pool_id,
        server_id,
        **kwargs
    ):
        """Get a pool server  # noqa: E501

        Gets a single server for a particular service and pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_pool_server(service_id, pool_id, server_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            pool_id (str): Alphanumeric string identifying a Pool.
            server_id (str): Alphanumeric string identifying a Server.

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
            ServerResponse
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
        kwargs['pool_id'] = \
            pool_id
        kwargs['server_id'] = \
            server_id
        return self.get_pool_server_endpoint.call_with_http_info(**kwargs)

    def list_pool_servers(
        self,
        service_id,
        pool_id,
        **kwargs
    ):
        """List servers in a pool  # noqa: E501

        Lists all servers for a particular service and pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_pool_servers(service_id, pool_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            pool_id (str): Alphanumeric string identifying a Pool.

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
            [ServerResponse]
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
        kwargs['pool_id'] = \
            pool_id
        return self.list_pool_servers_endpoint.call_with_http_info(**kwargs)

    def update_pool_server(
        self,
        service_id,
        pool_id,
        server_id,
        **kwargs
    ):
        """Update a server  # noqa: E501

        Updates a single server for a particular service and pool.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_pool_server(service_id, pool_id, server_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            pool_id (str): Alphanumeric string identifying a Pool.
            server_id (str): Alphanumeric string identifying a Server.

        Keyword Args:
            weight (int): Weight (`1-100`) used to load balance this server against others.. [optional] if omitted the server will use the default value of 100
            max_conn (int): Maximum number of connections. If the value is `0`, it inherits the value from pool's `max_conn_default`.. [optional] if omitted the server will use the default value of 0
            port (int): Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS.. [optional] if omitted the server will use the default value of 80
            address (str): A hostname, IPv4, or IPv6 address for the server. Required.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            disabled (bool): Allows servers to be enabled and disabled in a pool.. [optional] if omitted the server will use the default value of False
            override_host (str, none_type): The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting.. [optional] if omitted the server will use the default value of "null"
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
            ServerResponse
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
        kwargs['pool_id'] = \
            pool_id
        kwargs['server_id'] = \
            server_id
        return self.update_pool_server_endpoint.call_with_http_info(**kwargs)

