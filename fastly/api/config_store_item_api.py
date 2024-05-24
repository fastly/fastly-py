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
from fastly.model.bulk_update_config_store_list_request import BulkUpdateConfigStoreListRequest
from fastly.model.config_store_item_response import ConfigStoreItemResponse
from fastly.model.inline_response200 import InlineResponse200


class ConfigStoreItemApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bulk_update_config_store_item_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/items',
                'operation_id': 'bulk_update_config_store_item',
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
                    'config_store_id',
                    'bulk_update_config_store_list_request',
                ],
                'required': [
                    'config_store_id',
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
                    'config_store_id':
                        (str,),
                    'bulk_update_config_store_list_request':
                        (BulkUpdateConfigStoreListRequest,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                },
                'location_map': {
                    'config_store_id': 'path',
                    'bulk_update_config_store_list_request': 'body',
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
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_config_store_item_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigStoreItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/item',
                'operation_id': 'create_config_store_item',
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
                    'config_store_id',
                    'item_key',
                    'item_value',
                ],
                'required': [
                    'config_store_id',
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
                    'config_store_id':
                        (str,),
                    'item_key':
                        (str,),
                    'item_value':
                        (str,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                    'item_key': 'item_key',
                    'item_value': 'item_value',
                },
                'location_map': {
                    'config_store_id': 'path',
                    'item_key': 'form',
                    'item_value': 'form',
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
        self.delete_config_store_item_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/item/{config_store_item_key}',
                'operation_id': 'delete_config_store_item',
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
                    'config_store_id',
                    'config_store_item_key',
                ],
                'required': [
                    'config_store_id',
                    'config_store_item_key',
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
                    'config_store_id':
                        (str,),
                    'config_store_item_key':
                        (str,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                    'config_store_item_key': 'config_store_item_key',
                },
                'location_map': {
                    'config_store_id': 'path',
                    'config_store_item_key': 'path',
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
        self.get_config_store_item_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigStoreItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/item/{config_store_item_key}',
                'operation_id': 'get_config_store_item',
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
                    'config_store_id',
                    'config_store_item_key',
                ],
                'required': [
                    'config_store_id',
                    'config_store_item_key',
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
                    'config_store_id':
                        (str,),
                    'config_store_item_key':
                        (str,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                    'config_store_item_key': 'config_store_item_key',
                },
                'location_map': {
                    'config_store_id': 'path',
                    'config_store_item_key': 'path',
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
        self.list_config_store_items_endpoint = _Endpoint(
            settings={
                'response_type': ([ConfigStoreItemResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/items',
                'operation_id': 'list_config_store_items',
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
                    'config_store_id',
                ],
                'required': [
                    'config_store_id',
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
                    'config_store_id':
                        (str,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                },
                'location_map': {
                    'config_store_id': 'path',
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
        self.update_config_store_item_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigStoreItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/item/{config_store_item_key}',
                'operation_id': 'update_config_store_item',
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
                    'config_store_id',
                    'config_store_item_key',
                    'item_key',
                    'item_value',
                ],
                'required': [
                    'config_store_id',
                    'config_store_item_key',
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
                    'config_store_id':
                        (str,),
                    'config_store_item_key':
                        (str,),
                    'item_key':
                        (str,),
                    'item_value':
                        (str,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                    'config_store_item_key': 'config_store_item_key',
                    'item_key': 'item_key',
                    'item_value': 'item_value',
                },
                'location_map': {
                    'config_store_id': 'path',
                    'config_store_item_key': 'path',
                    'item_key': 'form',
                    'item_value': 'form',
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
        self.upsert_config_store_item_endpoint = _Endpoint(
            settings={
                'response_type': (ConfigStoreItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/resources/stores/config/{config_store_id}/item/{config_store_item_key}',
                'operation_id': 'upsert_config_store_item',
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
                    'config_store_id',
                    'config_store_item_key',
                    'item_key',
                    'item_value',
                ],
                'required': [
                    'config_store_id',
                    'config_store_item_key',
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
                    'config_store_id':
                        (str,),
                    'config_store_item_key':
                        (str,),
                    'item_key':
                        (str,),
                    'item_value':
                        (str,),
                },
                'attribute_map': {
                    'config_store_id': 'config_store_id',
                    'config_store_item_key': 'config_store_item_key',
                    'item_key': 'item_key',
                    'item_value': 'item_value',
                },
                'location_map': {
                    'config_store_id': 'path',
                    'config_store_item_key': 'path',
                    'item_key': 'form',
                    'item_value': 'form',
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

    def bulk_update_config_store_item(
        self,
        config_store_id,
        **kwargs
    ):
        """Update multiple entries in a config store  # noqa: E501

        Add multiple key-value pairs to an individual config store, specified by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_update_config_store_item(config_store_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.

        Keyword Args:
            bulk_update_config_store_list_request (BulkUpdateConfigStoreListRequest): [optional]
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
        kwargs['config_store_id'] = \
            config_store_id
        return self.bulk_update_config_store_item_endpoint.call_with_http_info(**kwargs)

    def create_config_store_item(
        self,
        config_store_id,
        **kwargs
    ):
        """Create an entry in a config store  # noqa: E501

        Add a single key-value pair to an individual config store, specified by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_config_store_item(config_store_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.

        Keyword Args:
            item_key (str): Item key, maximum 256 characters.. [optional]
            item_value (str): Item value, maximum 8000 characters.. [optional]
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
            ConfigStoreItemResponse
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
        kwargs['config_store_id'] = \
            config_store_id
        return self.create_config_store_item_endpoint.call_with_http_info(**kwargs)

    def delete_config_store_item(
        self,
        config_store_id,
        config_store_item_key,
        **kwargs
    ):
        """Delete an item from a config store  # noqa: E501

        Delete an entry in a config store given a config store ID, and item key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_config_store_item(config_store_id, config_store_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.
            config_store_item_key (str): Item key, maximum 256 characters.

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
        kwargs['config_store_id'] = \
            config_store_id
        kwargs['config_store_item_key'] = \
            config_store_item_key
        return self.delete_config_store_item_endpoint.call_with_http_info(**kwargs)

    def get_config_store_item(
        self,
        config_store_id,
        config_store_item_key,
        **kwargs
    ):
        """Get an item from a config store  # noqa: E501

        Retrieve a config store entry given a config store ID and item key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_config_store_item(config_store_id, config_store_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.
            config_store_item_key (str): Item key, maximum 256 characters.

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
            ConfigStoreItemResponse
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
        kwargs['config_store_id'] = \
            config_store_id
        kwargs['config_store_item_key'] = \
            config_store_item_key
        return self.get_config_store_item_endpoint.call_with_http_info(**kwargs)

    def list_config_store_items(
        self,
        config_store_id,
        **kwargs
    ):
        """List items in a config store  # noqa: E501

        List the key-value pairs associated with a given config store ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_config_store_items(config_store_id, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.

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
            [ConfigStoreItemResponse]
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
        kwargs['config_store_id'] = \
            config_store_id
        return self.list_config_store_items_endpoint.call_with_http_info(**kwargs)

    def update_config_store_item(
        self,
        config_store_id,
        config_store_item_key,
        **kwargs
    ):
        """Update an entry in a config store  # noqa: E501

        Update an entry in a config store given a config store ID, item key, and item value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_config_store_item(config_store_id, config_store_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.
            config_store_item_key (str): Item key, maximum 256 characters.

        Keyword Args:
            item_key (str): Item key, maximum 256 characters.. [optional]
            item_value (str): Item value, maximum 8000 characters.. [optional]
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
            ConfigStoreItemResponse
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
        kwargs['config_store_id'] = \
            config_store_id
        kwargs['config_store_item_key'] = \
            config_store_item_key
        return self.update_config_store_item_endpoint.call_with_http_info(**kwargs)

    def upsert_config_store_item(
        self,
        config_store_id,
        config_store_item_key,
        **kwargs
    ):
        """Insert or update an entry in a config store  # noqa: E501

        Insert or update an entry in a config store given a config store ID, item key, and item value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upsert_config_store_item(config_store_id, config_store_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            config_store_id (str): An alphanumeric string identifying the config store.
            config_store_item_key (str): Item key, maximum 256 characters.

        Keyword Args:
            item_key (str): Item key, maximum 256 characters.. [optional]
            item_value (str): Item value, maximum 8000 characters.. [optional]
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
            ConfigStoreItemResponse
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
        kwargs['config_store_id'] = \
            config_store_id
        kwargs['config_store_item_key'] = \
            config_store_item_key
        return self.upsert_config_store_item_endpoint.call_with_http_info(**kwargs)

