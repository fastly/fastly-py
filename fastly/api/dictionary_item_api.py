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
from fastly.model.dictionary_item_response import DictionaryItemResponse
from fastly.model.inline_response200 import InlineResponse200


class DictionaryItemApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_dictionary_item_endpoint = _Endpoint(
            settings={
                'response_type': (DictionaryItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/dictionary/{dictionary_id}/item',
                'operation_id': 'create_dictionary_item',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'dictionary_id',
                    'item_key',
                    'item_value',
                ],
                'required': [
                    'service_id',
                    'dictionary_id',
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
                    'dictionary_id':
                        (str,),
                    'item_key':
                        (str,),
                    'item_value':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'dictionary_id': 'dictionary_id',
                    'item_key': 'item_key',
                    'item_value': 'item_value',
                },
                'location_map': {
                    'service_id': 'path',
                    'dictionary_id': 'path',
                    'item_key': 'form',
                    'item_value': 'form',
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
        self.delete_dictionary_item_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key}',
                'operation_id': 'delete_dictionary_item',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
                ],
                'required': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
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
                    'dictionary_id':
                        (str,),
                    'dictionary_item_key':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'dictionary_id': 'dictionary_id',
                    'dictionary_item_key': 'dictionary_item_key',
                },
                'location_map': {
                    'service_id': 'path',
                    'dictionary_id': 'path',
                    'dictionary_item_key': 'path',
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
        self.get_dictionary_item_endpoint = _Endpoint(
            settings={
                'response_type': (DictionaryItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key}',
                'operation_id': 'get_dictionary_item',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
                ],
                'required': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
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
                    'dictionary_id':
                        (str,),
                    'dictionary_item_key':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'dictionary_id': 'dictionary_id',
                    'dictionary_item_key': 'dictionary_item_key',
                },
                'location_map': {
                    'service_id': 'path',
                    'dictionary_id': 'path',
                    'dictionary_item_key': 'path',
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
        self.list_dictionary_items_endpoint = _Endpoint(
            settings={
                'response_type': ([DictionaryItemResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/dictionary/{dictionary_id}/items',
                'operation_id': 'list_dictionary_items',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'dictionary_id',
                    'page',
                    'per_page',
                    'sort',
                    'direction',
                ],
                'required': [
                    'service_id',
                    'dictionary_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'direction',
                ],
                'validation': [
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('direction',): {

                        "ASCEND": "ascend",
                        "DESCEND": "descend"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'dictionary_id':
                        (str,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'sort':
                        (str,),
                    'direction':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'dictionary_id': 'dictionary_id',
                    'page': 'page',
                    'per_page': 'per_page',
                    'sort': 'sort',
                    'direction': 'direction',
                },
                'location_map': {
                    'service_id': 'path',
                    'dictionary_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                    'sort': 'query',
                    'direction': 'query',
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
        self.update_dictionary_item_endpoint = _Endpoint(
            settings={
                'response_type': (DictionaryItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key}',
                'operation_id': 'update_dictionary_item',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
                    'item_key',
                    'item_value',
                ],
                'required': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
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
                    'dictionary_id':
                        (str,),
                    'dictionary_item_key':
                        (str,),
                    'item_key':
                        (str,),
                    'item_value':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'dictionary_id': 'dictionary_id',
                    'dictionary_item_key': 'dictionary_item_key',
                    'item_key': 'item_key',
                    'item_value': 'item_value',
                },
                'location_map': {
                    'service_id': 'path',
                    'dictionary_id': 'path',
                    'dictionary_item_key': 'path',
                    'item_key': 'form',
                    'item_value': 'form',
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
        self.upsert_dictionary_item_endpoint = _Endpoint(
            settings={
                'response_type': (DictionaryItemResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key}',
                'operation_id': 'upsert_dictionary_item',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
                    'item_key',
                    'item_value',
                ],
                'required': [
                    'service_id',
                    'dictionary_id',
                    'dictionary_item_key',
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
                    'dictionary_id':
                        (str,),
                    'dictionary_item_key':
                        (str,),
                    'item_key':
                        (str,),
                    'item_value':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'dictionary_id': 'dictionary_id',
                    'dictionary_item_key': 'dictionary_item_key',
                    'item_key': 'item_key',
                    'item_value': 'item_value',
                },
                'location_map': {
                    'service_id': 'path',
                    'dictionary_id': 'path',
                    'dictionary_item_key': 'path',
                    'item_key': 'form',
                    'item_value': 'form',
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

    def create_dictionary_item(
        self,
        service_id,
        dictionary_id,
        **kwargs
    ):
        """Create an entry in an edge dictionary  # noqa: E501

        Create DictionaryItem given service, dictionary ID, item key, and item value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dictionary_item(service_id, dictionary_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            dictionary_id (str): Alphanumeric string identifying a Dictionary.

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
            DictionaryItemResponse
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
        kwargs['dictionary_id'] = \
            dictionary_id
        return self.create_dictionary_item_endpoint.call_with_http_info(**kwargs)

    def delete_dictionary_item(
        self,
        service_id,
        dictionary_id,
        dictionary_item_key,
        **kwargs
    ):
        """Delete an item from an edge dictionary  # noqa: E501

        Delete DictionaryItem given service, dictionary ID, and item key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_dictionary_item(service_id, dictionary_id, dictionary_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            dictionary_id (str): Alphanumeric string identifying a Dictionary.
            dictionary_item_key (str): Item key, maximum 256 characters.

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
        kwargs['dictionary_id'] = \
            dictionary_id
        kwargs['dictionary_item_key'] = \
            dictionary_item_key
        return self.delete_dictionary_item_endpoint.call_with_http_info(**kwargs)

    def get_dictionary_item(
        self,
        service_id,
        dictionary_id,
        dictionary_item_key,
        **kwargs
    ):
        """Get an item from an edge dictionary  # noqa: E501

        Retrieve a single DictionaryItem given service, dictionary ID and item key.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dictionary_item(service_id, dictionary_id, dictionary_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            dictionary_id (str): Alphanumeric string identifying a Dictionary.
            dictionary_item_key (str): Item key, maximum 256 characters.

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
            DictionaryItemResponse
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
        kwargs['dictionary_id'] = \
            dictionary_id
        kwargs['dictionary_item_key'] = \
            dictionary_item_key
        return self.get_dictionary_item_endpoint.call_with_http_info(**kwargs)

    def list_dictionary_items(
        self,
        service_id,
        dictionary_id,
        **kwargs
    ):
        """List items in an edge dictionary  # noqa: E501

        List of DictionaryItems given service and dictionary ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_dictionary_items(service_id, dictionary_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            dictionary_id (str): Alphanumeric string identifying a Dictionary.

        Keyword Args:
            page (int): Current page.. [optional]
            per_page (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            sort (str): Field on which to sort.. [optional] if omitted the server will use the default value of "created"
            direction (str): Direction in which to sort results.. [optional] if omitted the server will use the default value of "ascend"
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
            [DictionaryItemResponse]
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
        kwargs['dictionary_id'] = \
            dictionary_id
        return self.list_dictionary_items_endpoint.call_with_http_info(**kwargs)

    def update_dictionary_item(
        self,
        service_id,
        dictionary_id,
        dictionary_item_key,
        **kwargs
    ):
        """Update an entry in an edge dictionary  # noqa: E501

        Update DictionaryItem given service, dictionary ID, item key, and item value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dictionary_item(service_id, dictionary_id, dictionary_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            dictionary_id (str): Alphanumeric string identifying a Dictionary.
            dictionary_item_key (str): Item key, maximum 256 characters.

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
            DictionaryItemResponse
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
        kwargs['dictionary_id'] = \
            dictionary_id
        kwargs['dictionary_item_key'] = \
            dictionary_item_key
        return self.update_dictionary_item_endpoint.call_with_http_info(**kwargs)

    def upsert_dictionary_item(
        self,
        service_id,
        dictionary_id,
        dictionary_item_key,
        **kwargs
    ):
        """Insert or update an entry in an edge dictionary  # noqa: E501

        Upsert DictionaryItem given service, dictionary ID, item key, and item value.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upsert_dictionary_item(service_id, dictionary_id, dictionary_item_key, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            dictionary_id (str): Alphanumeric string identifying a Dictionary.
            dictionary_item_key (str): Item key, maximum 256 characters.

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
            DictionaryItemResponse
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
        kwargs['dictionary_id'] = \
            dictionary_id
        kwargs['dictionary_item_key'] = \
            dictionary_item_key
        return self.upsert_dictionary_item_endpoint.call_with_http_info(**kwargs)

