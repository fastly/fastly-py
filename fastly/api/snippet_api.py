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
from fastly.model.snippet_response import SnippetResponse


class SnippetApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_snippet_endpoint = _Endpoint(
            settings={
                'response_type': (SnippetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/snippet',
                'operation_id': 'create_snippet',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'name',
                    'dynamic',
                    'type',
                    'content',
                    'priority',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'dynamic',
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('dynamic',): {

                        "0": 0,
                        "1": 1
                    },
                    ('type',): {

                        "INIT": "init",
                        "RECV": "recv",
                        "HASH": "hash",
                        "HIT": "hit",
                        "MISS": "miss",
                        "PASS": "pass",
                        "FETCH": "fetch",
                        "ERROR": "error",
                        "DELIVER": "deliver",
                        "LOG": "log",
                        "NONE": "none"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'name':
                        (str,),
                    'dynamic':
                        (int,),
                    'type':
                        (str,),
                    'content':
                        (str,),
                    'priority':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'name': 'name',
                    'dynamic': 'dynamic',
                    'type': 'type',
                    'content': 'content',
                    'priority': 'priority',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'name': 'form',
                    'dynamic': 'form',
                    'type': 'form',
                    'content': 'form',
                    'priority': 'form',
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
        self.delete_snippet_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/snippet/{snippet_name}',
                'operation_id': 'delete_snippet',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'snippet_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'snippet_name',
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
                    'snippet_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'snippet_name': 'snippet_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'snippet_name': 'path',
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
        self.get_snippet_endpoint = _Endpoint(
            settings={
                'response_type': (SnippetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/snippet/{snippet_name}',
                'operation_id': 'get_snippet',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'snippet_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'snippet_name',
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
                    'snippet_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'snippet_name': 'snippet_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'snippet_name': 'path',
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
        self.get_snippet_dynamic_endpoint = _Endpoint(
            settings={
                'response_type': (SnippetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/snippet/{snippet_id}',
                'operation_id': 'get_snippet_dynamic',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'snippet_id',
                ],
                'required': [
                    'service_id',
                    'snippet_id',
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
                    'snippet_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'snippet_id': 'snippet_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'snippet_id': 'path',
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
        self.list_snippets_endpoint = _Endpoint(
            settings={
                'response_type': ([SnippetResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/snippet',
                'operation_id': 'list_snippets',
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
        self.update_snippet_dynamic_endpoint = _Endpoint(
            settings={
                'response_type': (SnippetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/snippet/{snippet_id}',
                'operation_id': 'update_snippet_dynamic',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'snippet_id',
                    'name',
                    'dynamic',
                    'type',
                    'content',
                    'priority',
                ],
                'required': [
                    'service_id',
                    'snippet_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'dynamic',
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('dynamic',): {

                        "0": 0,
                        "1": 1
                    },
                    ('type',): {

                        "INIT": "init",
                        "RECV": "recv",
                        "HASH": "hash",
                        "HIT": "hit",
                        "MISS": "miss",
                        "PASS": "pass",
                        "FETCH": "fetch",
                        "ERROR": "error",
                        "DELIVER": "deliver",
                        "LOG": "log",
                        "NONE": "none"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'snippet_id':
                        (str,),
                    'name':
                        (str,),
                    'dynamic':
                        (int,),
                    'type':
                        (str,),
                    'content':
                        (str,),
                    'priority':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'snippet_id': 'snippet_id',
                    'name': 'name',
                    'dynamic': 'dynamic',
                    'type': 'type',
                    'content': 'content',
                    'priority': 'priority',
                },
                'location_map': {
                    'service_id': 'path',
                    'snippet_id': 'path',
                    'name': 'form',
                    'dynamic': 'form',
                    'type': 'form',
                    'content': 'form',
                    'priority': 'form',
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

    def create_snippet(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a snippet  # noqa: E501

        Create a snippet for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_snippet(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            name (str): The name for the snippet.. [optional]
            dynamic (int): Sets the snippet version.. [optional]
            type (str): The location in generated VCL where the snippet should be placed.. [optional]
            content (str): The VCL code that specifies exactly what the snippet does.. [optional]
            priority (int): Priority determines execution order. Lower numbers execute first.. [optional] if omitted the server will use the default value of 100
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
            SnippetResponse
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
        return self.create_snippet_endpoint.call_with_http_info(**kwargs)

    def delete_snippet(
        self,
        service_id,
        version_id,
        snippet_name,
        **kwargs
    ):
        """Delete a snippet  # noqa: E501

        Delete a specific snippet for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_snippet(service_id, version_id, snippet_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            snippet_name (str): The name for the snippet.

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
        kwargs['snippet_name'] = \
            snippet_name
        return self.delete_snippet_endpoint.call_with_http_info(**kwargs)

    def get_snippet(
        self,
        service_id,
        version_id,
        snippet_name,
        **kwargs
    ):
        """Get a versioned snippet  # noqa: E501

        Get a single snippet for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_snippet(service_id, version_id, snippet_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            snippet_name (str): The name for the snippet.

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
            SnippetResponse
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
        kwargs['snippet_name'] = \
            snippet_name
        return self.get_snippet_endpoint.call_with_http_info(**kwargs)

    def get_snippet_dynamic(
        self,
        service_id,
        snippet_id,
        **kwargs
    ):
        """Get a dynamic snippet  # noqa: E501

        Get a single dynamic snippet for a particular service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_snippet_dynamic(service_id, snippet_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            snippet_id (str): Alphanumeric string identifying a VCL Snippet.

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
            SnippetResponse
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
        kwargs['snippet_id'] = \
            snippet_id
        return self.get_snippet_dynamic_endpoint.call_with_http_info(**kwargs)

    def list_snippets(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List snippets  # noqa: E501

        List all snippets for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_snippets(service_id, version_id, async_req=True)
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
            [SnippetResponse]
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
        return self.list_snippets_endpoint.call_with_http_info(**kwargs)

    def update_snippet_dynamic(
        self,
        service_id,
        snippet_id,
        **kwargs
    ):
        """Update a dynamic snippet  # noqa: E501

        Update a dynamic snippet for a particular service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_snippet_dynamic(service_id, snippet_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            snippet_id (str): Alphanumeric string identifying a VCL Snippet.

        Keyword Args:
            name (str): The name for the snippet.. [optional]
            dynamic (int): Sets the snippet version.. [optional]
            type (str): The location in generated VCL where the snippet should be placed.. [optional]
            content (str): The VCL code that specifies exactly what the snippet does.. [optional]
            priority (int): Priority determines execution order. Lower numbers execute first.. [optional] if omitted the server will use the default value of 100
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
            SnippetResponse
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
        kwargs['snippet_id'] = \
            snippet_id
        return self.update_snippet_dynamic_endpoint.call_with_http_info(**kwargs)

