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
from fastly.model.inline_response2004 import InlineResponse2004


class KvStoreItemApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.kv_store_delete_item_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/kv/{store_id}/keys/{key}',
                'operation_id': 'kv_store_delete_item',
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
                    'store_id',
                    'key',
                    'if_generation_match',
                    'force',
                ],
                'required': [
                    'store_id',
                    'key',
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
                    'key':
                        (str,),
                    'if_generation_match':
                        (int,),
                    'force':
                        (bool,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'key': 'key',
                    'if_generation_match': 'if-generation-match',
                    'force': 'force',
                },
                'location_map': {
                    'store_id': 'path',
                    'key': 'path',
                    'if_generation_match': 'header',
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
        self.kv_store_get_item_endpoint = _Endpoint(
            settings={
                'response_type': (str,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/kv/{store_id}/keys/{key}',
                'operation_id': 'kv_store_get_item',
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
                    'store_id',
                    'key',
                ],
                'required': [
                    'store_id',
                    'key',
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
                    'key':
                        (str,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'key': 'key',
                },
                'location_map': {
                    'store_id': 'path',
                    'key': 'path',
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
        self.kv_store_list_item_keys_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2004,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/kv/{store_id}/keys',
                'operation_id': 'kv_store_list_item_keys',
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
                    'store_id',
                    'cursor',
                    'limit',
                    'prefix',
                    'consistency',
                ],
                'required': [
                    'store_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'consistency',
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('consistency',): {

                        "STRONG": "strong",
                        "EVENTUAL": "eventual"
                    },
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
                    'consistency':
                        (str,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'prefix': 'prefix',
                    'consistency': 'consistency',
                },
                'location_map': {
                    'store_id': 'path',
                    'cursor': 'query',
                    'limit': 'query',
                    'prefix': 'query',
                    'consistency': 'query',
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
        self.kv_store_upsert_item_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/kv/{store_id}/keys/{key}',
                'operation_id': 'kv_store_upsert_item',
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
                    'store_id',
                    'key',
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
                    'key',
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
                    'key':
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
                        (str,),
                },
                'attribute_map': {
                    'store_id': 'store_id',
                    'key': 'key',
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
                    'key': 'path',
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
                'accept': [],
                'content_type': [
                    'application/octet-stream'
                ]
            },
            api_client=api_client
        )

    def kv_store_delete_item(
        self,
        store_id,
        key,
        **kwargs
    ):
        """Delete an item.  # noqa: E501

        Delete an item.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.kv_store_delete_item(store_id, key, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):
            key (str):

        Keyword Args:
            if_generation_match (int): [optional]
            force (bool): [optional] if omitted the server will use the default value of False
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
        kwargs['key'] = \
            key
        return self.kv_store_delete_item_endpoint.call_with_http_info(**kwargs)

    def kv_store_get_item(
        self,
        store_id,
        key,
        **kwargs
    ):
        """Get an item.  # noqa: E501

        Get an item, including its value, metadata (if any), and generation marker.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.kv_store_get_item(store_id, key, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):
            key (str):

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
            str
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
        kwargs['key'] = \
            key
        return self.kv_store_get_item_endpoint.call_with_http_info(**kwargs)

    def kv_store_list_item_keys(
        self,
        store_id,
        **kwargs
    ):
        """List item keys.  # noqa: E501

        Lists the matching item keys (or all item keys, if no prefix is supplied).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.kv_store_list_item_keys(store_id, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):

        Keyword Args:
            cursor (str): [optional]
            limit (int): [optional] if omitted the server will use the default value of 100
            prefix (str): [optional]
            consistency (str): [optional] if omitted the server will use the default value of "strong"
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
            InlineResponse2004
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
        return self.kv_store_list_item_keys_endpoint.call_with_http_info(**kwargs)

    def kv_store_upsert_item(
        self,
        store_id,
        key,
        **kwargs
    ):
        """Insert or update an item.  # noqa: E501

        Inserts or updates an item's value and metadata.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.kv_store_upsert_item(store_id, key, async_req=True)
        >>> result = thread.get()

        Args:
            store_id (str):
            key (str):

        Keyword Args:
            if_generation_match (int): [optional]
            time_to_live_sec (int): [optional]
            metadata (str): [optional]
            add (bool): [optional] if omitted the server will use the default value of False
            append (bool): [optional] if omitted the server will use the default value of False
            prepend (bool): [optional] if omitted the server will use the default value of False
            background_fetch (bool): [optional] if omitted the server will use the default value of False
            body (str): [optional]
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
        kwargs['key'] = \
            key
        return self.kv_store_upsert_item_endpoint.call_with_http_info(**kwargs)

