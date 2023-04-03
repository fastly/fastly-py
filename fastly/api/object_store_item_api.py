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
from fastly.model.inline_response2003 import InlineResponse2003


class ObjectStoreItemApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_key_from_store_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/object/{store_id}/keys/{key_name}',
                'operation_id': 'delete_key_from_store',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'store_id',
                    'key_name',
                    'force',
                ],
                'required': [
                    'store_id',
                    'key_name',
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
                    'store_id':
                        (str,),
                    'key_name':
                        (str,),
                    'force':
                        (bool,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'key_name': 'key_name',
                    'force': 'force',
                },
                'location_map': {
                    'store_id': 'path',
                    'key_name': 'path',
                    'force': 'query',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_keys_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2003,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/object/{store_id}/keys',
                'operation_id': 'get_keys',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'store_id',
                    'cursor',
                    'limit',
                    'prefix',
                ],
                'required': [
                    'store_id',
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
                    'store_id':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                    'prefix':
                        (str,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'prefix': 'prefix',
                },
                'location_map': {
                    'store_id': 'path',
                    'cursor': 'query',
                    'limit': 'query',
                    'prefix': 'query',
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
        self.get_value_for_key_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/object/{store_id}/keys/{key_name}',
                'operation_id': 'get_value_for_key',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'store_id',
                    'key_name',
                ],
                'required': [
                    'store_id',
                    'key_name',
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
                    'store_id':
                        (str,),
                    'key_name':
                        (str,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'key_name': 'key_name',
                },
                'location_map': {
                    'store_id': 'path',
                    'key_name': 'path',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.set_value_for_key_endpoint = _Endpoint(
            settings={
                'response_type': (file_type,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/object/{store_id}/keys/{key_name}',
                'operation_id': 'set_value_for_key',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'store_id',
                    'key_name',
                    'if_generation_match',
                    'time_to_live_sec',
                    'metadata',
                    'add',
                    'append',
                    'prepend',
                    'background_fetch',
                    'body',
                ],
                'required': [
                    'store_id',
                    'key_name',
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
                    'store_id':
                        (str,),
                    'key_name':
                        (str,),
                    'if_generation_match':
                        (int,),
                    'time_to_live_sec':
                        (int,),
                    'metadata':
                        (str,),
                    'add':
                        (bool,),
                    'append':
                        (bool,),
                    'prepend':
                        (bool,),
                    'background_fetch':
                        (bool,),
                    'body':
                        (file_type,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'key_name': 'key_name',
                    'if_generation_match': 'if-generation-match',
                    'time_to_live_sec': 'time_to_live_sec',
                    'metadata': 'metadata',
                    'add': 'add',
                    'append': 'append',
                    'prepend': 'prepend',
                    'background_fetch': 'background_fetch',
                },
                'location_map': {
                    'store_id': 'path',
                    'key_name': 'path',
                    'if_generation_match': 'header',
                    'time_to_live_sec': 'header',
                    'metadata': 'header',
                    'add': 'query',
                    'append': 'query',
                    'prepend': 'query',
                    'background_fetch': 'query',
                    'body': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream'
                ],
                'content_type': [
                    'application/octet-stream'
                ]
            },
            api_client=api_client
        )

    def delete_key_from_store(
        self,
        store_id,
        key_name,
        **kwargs
    ):
        """Delete object store item.  # noqa: E501

        Delete an item from an object store  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_key_from_store(store_id, key_name, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):
            key_name (str):

        Keyword Args:
            force (bool): [optional]
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
        kwargs['store_id'] = \
            store_id
        kwargs['key_name'] = \
            key_name
        return self.delete_key_from_store_endpoint.call_with_http_info(**kwargs)

    def get_keys(
        self,
        store_id,
        **kwargs
    ):
        """List object store keys.  # noqa: E501

        List the keys of all items within an object store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_keys(store_id, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):

        Keyword Args:
            cursor (str): [optional]
            limit (int): [optional] if omitted the server will use the default value of 100
            prefix (str): [optional]
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
        kwargs['store_id'] = \
            store_id
        return self.get_keys_endpoint.call_with_http_info(**kwargs)

    def get_value_for_key(
        self,
        store_id,
        key_name,
        **kwargs
    ):
        """Get the value of an object store item  # noqa: E501

        Get the value associated with a key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_value_for_key(store_id, key_name, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):
            key_name (str):

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
            file_type
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
        kwargs['store_id'] = \
            store_id
        kwargs['key_name'] = \
            key_name
        return self.get_value_for_key_endpoint.call_with_http_info(**kwargs)

    def set_value_for_key(
        self,
        store_id,
        key_name,
        **kwargs
    ):
        """Insert an item into an object store  # noqa: E501

        Set a new value for a new or existing key in an object store.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.set_value_for_key(store_id, key_name, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):
            key_name (str):

        Keyword Args:
            if_generation_match (int): [optional]
            time_to_live_sec (int): [optional]
            metadata (str): [optional]
            add (bool): [optional]
            append (bool): [optional]
            prepend (bool): [optional]
            background_fetch (bool): [optional]
            body (file_type): [optional]
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
            file_type
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
        kwargs['store_id'] = \
            store_id
        kwargs['key_name'] = \
            key_name
        return self.set_value_for_key_endpoint.call_with_http_info(**kwargs)

