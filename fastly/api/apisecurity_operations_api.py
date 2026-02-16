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
from fastly.model.inline_response2001 import InlineResponse2001
from fastly.model.inline_response2002 import InlineResponse2002
from fastly.model.inline_response2003 import InlineResponse2003
from fastly.model.operation_create import OperationCreate
from fastly.model.operation_get import OperationGet
from fastly.model.operation_update import OperationUpdate
from fastly.model.tag_base import TagBase
from fastly.model.tag_create import TagCreate
from fastly.model.tag_get import TagGet


class ApisecurityOperationsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.api_security_create_operation_endpoint = _Endpoint(
            settings={
                'response_type': (OperationGet,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/operations',
                'operation_id': 'api_security_create_operation',
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
                    'operation_create',
                ],
                'required': [
                    'service_id',
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
                    'operation_create':
                        (OperationCreate,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'operation_create': 'body',
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
        self.api_security_create_operation_tag_endpoint = _Endpoint(
            settings={
                'response_type': (TagGet,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/tags',
                'operation_id': 'api_security_create_operation_tag',
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
                    'tag_create',
                ],
                'required': [
                    'service_id',
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
                    'tag_create':
                        (TagCreate,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'tag_create': 'body',
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
        self.api_security_delete_operation_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/operations/{operation_id}',
                'operation_id': 'api_security_delete_operation',
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
                    'operation_id',
                ],
                'required': [
                    'service_id',
                    'operation_id',
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
                    'operation_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'operation_id': 'operation_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'operation_id': 'path',
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
        self.api_security_delete_operation_tag_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/tags/{tag_id}',
                'operation_id': 'api_security_delete_operation_tag',
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
                    'tag_id',
                ],
                'required': [
                    'service_id',
                    'tag_id',
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
                    'tag_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'tag_id': 'tag_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'tag_id': 'path',
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
        self.api_security_get_operation_endpoint = _Endpoint(
            settings={
                'response_type': (OperationGet,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/operations/{operation_id}',
                'operation_id': 'api_security_get_operation',
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
                    'operation_id',
                ],
                'required': [
                    'service_id',
                    'operation_id',
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
                    'operation_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'operation_id': 'operation_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'operation_id': 'path',
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
        self.api_security_get_operation_tag_endpoint = _Endpoint(
            settings={
                'response_type': (TagGet,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/tags/{tag_id}',
                'operation_id': 'api_security_get_operation_tag',
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
                    'tag_id',
                ],
                'required': [
                    'service_id',
                    'tag_id',
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
                    'tag_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'tag_id': 'tag_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'tag_id': 'path',
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
        self.api_security_list_discovered_operations_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/discovered-operations',
                'operation_id': 'api_security_list_discovered_operations',
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
                    'status',
                    'limit',
                    'page',
                ],
                'required': [
                    'service_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'status',
                ],
                'validation': [
                    'limit',
                    'page',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                    ('status',): {

                        "DISCOVERED": "DISCOVERED",
                        "SAVED": "SAVED",
                        "IGNORED": "IGNORED"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'status':
                        (str,),
                    'limit':
                        (int,),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'status': 'status',
                    'limit': 'limit',
                    'page': 'page',
                },
                'location_map': {
                    'service_id': 'path',
                    'status': 'query',
                    'limit': 'query',
                    'page': 'query',
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
        self.api_security_list_operation_tags_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2003,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/tags',
                'operation_id': 'api_security_list_operation_tags',
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
                ],
                'required': [
                    'service_id',
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
                },
                'attribute_map': {
                    'service_id': 'service_id',
                },
                'location_map': {
                    'service_id': 'path',
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
        self.api_security_list_operations_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2002,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/operations',
                'operation_id': 'api_security_list_operations',
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
                    'tag_id',
                    'limit',
                    'page',
                ],
                'required': [
                    'service_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                    'page',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 1000,
                        'inclusive_minimum': 1,
                    },
                    ('page',): {

                        'inclusive_minimum': 0,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'tag_id':
                        (str,),
                    'limit':
                        (int,),
                    'page':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'tag_id': 'tag_id',
                    'limit': 'limit',
                    'page': 'page',
                },
                'location_map': {
                    'service_id': 'path',
                    'tag_id': 'query',
                    'limit': 'query',
                    'page': 'query',
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
        self.api_security_update_operation_endpoint = _Endpoint(
            settings={
                'response_type': (OperationGet,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/operations/{operation_id}',
                'operation_id': 'api_security_update_operation',
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
                    'service_id',
                    'operation_id',
                    'operation_update',
                ],
                'required': [
                    'service_id',
                    'operation_id',
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
                    'operation_id':
                        (str,),
                    'operation_update':
                        (OperationUpdate,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'operation_id': 'operation_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'operation_id': 'path',
                    'operation_update': 'body',
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
        self.api_security_update_operation_tag_endpoint = _Endpoint(
            settings={
                'response_type': (TagGet,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/api-security/v1/services/{service_id}/tags/{tag_id}',
                'operation_id': 'api_security_update_operation_tag',
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
                    'service_id',
                    'tag_id',
                    'body',
                ],
                'required': [
                    'service_id',
                    'tag_id',
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
                    'tag_id':
                        (str,),
                    'body':
                        (TagBase,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'tag_id': 'tag_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'tag_id': 'path',
                    'body': 'body',
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

    def api_security_create_operation(
        self,
        service_id,
        **kwargs
    ):
        """Create operation  # noqa: E501

        Create a new operation associated with a specific service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_create_operation(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.

        Keyword Args:
            operation_create (OperationCreate): [optional]
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
            OperationGet
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
        return self.api_security_create_operation_endpoint.call_with_http_info(**kwargs)

    def api_security_create_operation_tag(
        self,
        service_id,
        **kwargs
    ):
        """Create operation tag  # noqa: E501

        Create a new operation tag associated with a specific service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_create_operation_tag(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.

        Keyword Args:
            tag_create (TagCreate): [optional]
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
            TagGet
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
        return self.api_security_create_operation_tag_endpoint.call_with_http_info(**kwargs)

    def api_security_delete_operation(
        self,
        service_id,
        operation_id,
        **kwargs
    ):
        """Delete operation  # noqa: E501

        Delete an existing operation associated with a specific service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_delete_operation(service_id, operation_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.
            operation_id (str): The unique identifier of the operation.

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
        kwargs['service_id'] = \
            service_id
        kwargs['operation_id'] = \
            operation_id
        return self.api_security_delete_operation_endpoint.call_with_http_info(**kwargs)

    def api_security_delete_operation_tag(
        self,
        service_id,
        tag_id,
        **kwargs
    ):
        """Delete operation tag  # noqa: E501

        Delete an existing operation tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_delete_operation_tag(service_id, tag_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.
            tag_id (str): The unique identifier of the operation tag.

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
        kwargs['service_id'] = \
            service_id
        kwargs['tag_id'] = \
            tag_id
        return self.api_security_delete_operation_tag_endpoint.call_with_http_info(**kwargs)

    def api_security_get_operation(
        self,
        service_id,
        operation_id,
        **kwargs
    ):
        """Retrieve operation  # noqa: E501

        Get a specific operation associated with a service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_get_operation(service_id, operation_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.
            operation_id (str): The unique identifier of the operation.

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
            OperationGet
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
        kwargs['operation_id'] = \
            operation_id
        return self.api_security_get_operation_endpoint.call_with_http_info(**kwargs)

    def api_security_get_operation_tag(
        self,
        service_id,
        tag_id,
        **kwargs
    ):
        """Retrieve operation tag  # noqa: E501

        Get a specific operation tag by its unique identifier.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_get_operation_tag(service_id, tag_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.
            tag_id (str): The unique identifier of the operation tag.

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
            TagGet
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
        kwargs['tag_id'] = \
            tag_id
        return self.api_security_get_operation_tag_endpoint.call_with_http_info(**kwargs)

    def api_security_list_discovered_operations(
        self,
        service_id,
        **kwargs
    ):
        """List discovered operations  # noqa: E501

        List all discovered operations associated with a specific service. Optionally filter operations by status.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_list_discovered_operations(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.

        Keyword Args:
            status (str): Filter operations by status. Only operations with this status will be returned.. [optional]
            limit (int): The maximum number of operations to return per page.. [optional] if omitted the server will use the default value of 100
            page (int): The page number to return.. [optional] if omitted the server will use the default value of 0
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
            InlineResponse2001
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
        return self.api_security_list_discovered_operations_endpoint.call_with_http_info(**kwargs)

    def api_security_list_operation_tags(
        self,
        service_id,
        **kwargs
    ):
        """List operation tags  # noqa: E501

        List all operation tags associated with a specific service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_list_operation_tags(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.

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
            InlineResponse2003
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
        return self.api_security_list_operation_tags_endpoint.call_with_http_info(**kwargs)

    def api_security_list_operations(
        self,
        service_id,
        **kwargs
    ):
        """List operations  # noqa: E501

        List all operations associated with a specific service. Optionally filter operations by tag ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_list_operations(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.

        Keyword Args:
            tag_id (str): Filter operations by operation tag ID. Only operations associated with this operation tag will be returned.. [optional]
            limit (int): The maximum number of operations to return per page.. [optional] if omitted the server will use the default value of 100
            page (int): The page number to return.. [optional] if omitted the server will use the default value of 0
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
            InlineResponse2002
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
        return self.api_security_list_operations_endpoint.call_with_http_info(**kwargs)

    def api_security_update_operation(
        self,
        service_id,
        operation_id,
        **kwargs
    ):
        """Update operation  # noqa: E501

        Partially update an existing operation associated with a specific service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_update_operation(service_id, operation_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.
            operation_id (str): The unique identifier of the operation.

        Keyword Args:
            operation_update (OperationUpdate): [optional]
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
            OperationGet
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
        kwargs['operation_id'] = \
            operation_id
        return self.api_security_update_operation_endpoint.call_with_http_info(**kwargs)

    def api_security_update_operation_tag(
        self,
        service_id,
        tag_id,
        **kwargs
    ):
        """Update operation tag  # noqa: E501

        Partially update an existing operation tag.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_security_update_operation_tag(service_id, tag_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): The unique identifier of the service.
            tag_id (str): The unique identifier of the operation tag.

        Keyword Args:
            body (TagBase): [optional]
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
            TagGet
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
        kwargs['tag_id'] = \
            tag_id
        return self.api_security_update_operation_tag_endpoint.call_with_http_info(**kwargs)

