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
from fastly.model.arc_create_virtual_key_response import ArcCreateVirtualKeyResponse
from fastly.model.arc_error import ArcError
from fastly.model.arc_rotate_virtual_key_request import ArcRotateVirtualKeyRequest
from fastly.model.arc_rotate_virtual_key_response import ArcRotateVirtualKeyResponse
from fastly.model.arc_update_virtual_key_request import ArcUpdateVirtualKeyRequest
from fastly.model.arc_update_virtual_key_response import ArcUpdateVirtualKeyResponse
from fastly.model.arc_virtual_key import ArcVirtualKey
from fastly.model.arc_virtual_key_failover_request import ArcVirtualKeyFailoverRequest
from fastly.model.arc_virtual_key_failover_response import ArcVirtualKeyFailoverResponse
from fastly.model.arc_virtual_key_response import ArcVirtualKeyResponse
from fastly.model.arc_virtual_keys_response import ArcVirtualKeysResponse


class AiRuntimeControlVirtualKeysApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.arc_create_virtual_key_endpoint = _Endpoint(
            settings={
                'response_type': (ArcCreateVirtualKeyResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys',
                'operation_id': 'arc_create_virtual_key',
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
                    'arc_virtual_key',
                ],
                'required': [
                    'arc_virtual_key',
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
                    'arc_virtual_key':
                        (ArcVirtualKey,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'arc_virtual_key': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.arc_delete_virtual_key_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys/{key_id}',
                'operation_id': 'arc_delete_virtual_key',
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
                    'key_id',
                ],
                'required': [
                    'key_id',
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
                    'key_id':
                        (str,),
                },
                'attribute_map': {
                    'key_id': 'key_id',
                },
                'location_map': {
                    'key_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.arc_get_virtual_key_endpoint = _Endpoint(
            settings={
                'response_type': (ArcVirtualKeyResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys/{key_id}',
                'operation_id': 'arc_get_virtual_key',
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
                    'key_id',
                ],
                'required': [
                    'key_id',
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
                    'key_id':
                        (str,),
                },
                'attribute_map': {
                    'key_id': 'key_id',
                },
                'location_map': {
                    'key_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.arc_get_virtual_key_failover_endpoint = _Endpoint(
            settings={
                'response_type': (ArcVirtualKeyFailoverResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys/{key_id}/failover',
                'operation_id': 'arc_get_virtual_key_failover',
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
                    'key_id',
                ],
                'required': [
                    'key_id',
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
                    'key_id':
                        (str,),
                },
                'attribute_map': {
                    'key_id': 'key_id',
                },
                'location_map': {
                    'key_id': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.arc_list_virtual_keys_endpoint = _Endpoint(
            settings={
                'response_type': (ArcVirtualKeysResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys',
                'operation_id': 'arc_list_virtual_keys',
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
                    'include_deleted',
                    'search',
                    'cursor',
                    'limit',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "CREATED_AT": "created_at",
                        "-CREATED_AT": "-created_at",
                        "UPDATED_AT": "updated_at",
                        "-UPDATED_AT": "-updated_at",
                        "NAME": "name",
                        "-NAME": "-name",
                        "EXPIRES_AT": "expires_at",
                        "-EXPIRES_AT": "-expires_at",
                        "USER_NAME": "user_name",
                        "-USER_NAME": "-user_name",
                        "LAST_USED_AT": "last_used_at",
                        "-LAST_USED_AT": "-last_used_at"
                    },
                },
                'openapi_types': {
                    'include_deleted':
                        (bool,),
                    'search':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'include_deleted': 'include_deleted',
                    'search': 'search',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'sort': 'sort',
                },
                'location_map': {
                    'include_deleted': 'query',
                    'search': 'query',
                    'cursor': 'query',
                    'limit': 'query',
                    'sort': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.arc_rotate_virtual_key_endpoint = _Endpoint(
            settings={
                'response_type': (ArcRotateVirtualKeyResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys/{key_id}/rotate',
                'operation_id': 'arc_rotate_virtual_key',
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
                    'key_id',
                    'arc_rotate_virtual_key_request',
                ],
                'required': [
                    'key_id',
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
                    'key_id':
                        (str,),
                    'arc_rotate_virtual_key_request':
                        (ArcRotateVirtualKeyRequest,),
                },
                'attribute_map': {
                    'key_id': 'key_id',
                },
                'location_map': {
                    'key_id': 'path',
                    'arc_rotate_virtual_key_request': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.arc_update_virtual_key_endpoint = _Endpoint(
            settings={
                'response_type': (ArcUpdateVirtualKeyResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys/{key_id}',
                'operation_id': 'arc_update_virtual_key',
                'http_method': 'PATCH',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'key_id',
                    'arc_update_virtual_key_request',
                ],
                'required': [
                    'key_id',
                    'arc_update_virtual_key_request',
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
                    'key_id':
                        (str,),
                    'arc_update_virtual_key_request':
                        (ArcUpdateVirtualKeyRequest,),
                },
                'attribute_map': {
                    'key_id': 'key_id',
                },
                'location_map': {
                    'key_id': 'path',
                    'arc_update_virtual_key_request': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.arc_update_virtual_key_failover_endpoint = _Endpoint(
            settings={
                'response_type': (ArcVirtualKeyFailoverResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ai-runtime-control/v1/keys/{key_id}/failover',
                'operation_id': 'arc_update_virtual_key_failover',
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
                    'key_id',
                    'arc_virtual_key_failover_request',
                ],
                'required': [
                    'key_id',
                    'arc_virtual_key_failover_request',
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
                    'key_id':
                        (str,),
                    'arc_virtual_key_failover_request':
                        (ArcVirtualKeyFailoverRequest,),
                },
                'attribute_map': {
                    'key_id': 'key_id',
                },
                'location_map': {
                    'key_id': 'path',
                    'arc_virtual_key_failover_request': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/problem+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def arc_create_virtual_key(
        self,
        arc_virtual_key,
        **kwargs
    ):
        """Create a virtual key  # noqa: E501

        Create a new virtual key for authenticating requests through the AI Runtime Control gateway.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_create_virtual_key(arc_virtual_key, async_req=True)
        >>> result = thread.get()

        Args:
            arc_virtual_key (ArcVirtualKey):

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
            ArcCreateVirtualKeyResponse
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
        kwargs['arc_virtual_key'] = \
            arc_virtual_key
        return self.arc_create_virtual_key_endpoint.call_with_http_info(**kwargs)

    def arc_delete_virtual_key(
        self,
        key_id,
        **kwargs
    ):
        """Delete a virtual key  # noqa: E501

        Delete a virtual key. This also deletes any security configuration associated with the key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_delete_virtual_key(key_id, async_req=True)
        >>> result = thread.get()

        Args:
            key_id (str): The ID of the virtual key.

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
            None
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
        kwargs['key_id'] = \
            key_id
        return self.arc_delete_virtual_key_endpoint.call_with_http_info(**kwargs)

    def arc_get_virtual_key(
        self,
        key_id,
        **kwargs
    ):
        """Get a virtual key  # noqa: E501

        Retrieve a single virtual key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_get_virtual_key(key_id, async_req=True)
        >>> result = thread.get()

        Args:
            key_id (str): The ID of the virtual key.

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
            ArcVirtualKeyResponse
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
        kwargs['key_id'] = \
            key_id
        return self.arc_get_virtual_key_endpoint.call_with_http_info(**kwargs)

    def arc_get_virtual_key_failover(
        self,
        key_id,
        **kwargs
    ):
        """Get a virtual key's failover policy  # noqa: E501

        Retrieve the failover policy for a virtual key. A failover policy lists alternate provider connections to retry a request against, and which error conditions trigger a retry.  Failover is a per-account feature. If it isn't enabled on your account, this endpoint returns a 404 response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_get_virtual_key_failover(key_id, async_req=True)
        >>> result = thread.get()

        Args:
            key_id (str): The ID of the virtual key.

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
            ArcVirtualKeyFailoverResponse
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
        kwargs['key_id'] = \
            key_id
        return self.arc_get_virtual_key_failover_endpoint.call_with_http_info(**kwargs)

    def arc_list_virtual_keys(
        self,
        **kwargs
    ):
        """List virtual keys  # noqa: E501

        List the virtual keys belonging to your account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_list_virtual_keys(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            include_deleted (bool): Include deleted virtual keys in the results.. [optional] if omitted the server will use the default value of False
            search (str): Filter results to virtual keys whose name contains this substring.. [optional]
            cursor (str): Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results, or the `prev_cursor` value to request the previous page. . [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 10
            sort (str): Sort field. Prefix with `-` for descending order (e.g., `sort=-created_at`). . [optional] if omitted the server will use the default value of "created_at"
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
            ArcVirtualKeysResponse
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
        return self.arc_list_virtual_keys_endpoint.call_with_http_info(**kwargs)

    def arc_rotate_virtual_key(
        self,
        key_id,
        **kwargs
    ):
        """Rotate a virtual key  # noqa: E501

        Issue a new access token for a virtual key, invalidating the previous one.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_rotate_virtual_key(key_id, async_req=True)
        >>> result = thread.get()

        Args:
            key_id (str): The ID of the virtual key.

        Keyword Args:
            arc_rotate_virtual_key_request (ArcRotateVirtualKeyRequest): [optional]
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
            ArcRotateVirtualKeyResponse
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
        kwargs['key_id'] = \
            key_id
        return self.arc_rotate_virtual_key_endpoint.call_with_http_info(**kwargs)

    def arc_update_virtual_key(
        self,
        key_id,
        arc_update_virtual_key_request,
        **kwargs
    ):
        """Update a virtual key  # noqa: E501

        Update the attributes of a virtual key. Only the fields you include are changed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_update_virtual_key(key_id, arc_update_virtual_key_request, async_req=True)
        >>> result = thread.get()

        Args:
            key_id (str): The ID of the virtual key.
            arc_update_virtual_key_request (ArcUpdateVirtualKeyRequest):

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
            ArcUpdateVirtualKeyResponse
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
        kwargs['key_id'] = \
            key_id
        kwargs['arc_update_virtual_key_request'] = \
            arc_update_virtual_key_request
        return self.arc_update_virtual_key_endpoint.call_with_http_info(**kwargs)

    def arc_update_virtual_key_failover(
        self,
        key_id,
        arc_virtual_key_failover_request,
        **kwargs
    ):
        """Update a virtual key's failover policy  # noqa: E501

        Replace the failover policy for a virtual key.  Failover is a per-account feature. If it isn't enabled on your account, this endpoint returns a 404 response.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.arc_update_virtual_key_failover(key_id, arc_virtual_key_failover_request, async_req=True)
        >>> result = thread.get()

        Args:
            key_id (str): The ID of the virtual key.
            arc_virtual_key_failover_request (ArcVirtualKeyFailoverRequest):

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
            ArcVirtualKeyFailoverResponse
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
        kwargs['key_id'] = \
            key_id
        kwargs['arc_virtual_key_failover_request'] = \
            arc_virtual_key_failover_request
        return self.arc_update_virtual_key_failover_endpoint.call_with_http_info(**kwargs)

