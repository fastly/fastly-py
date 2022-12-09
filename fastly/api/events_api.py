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
from fastly.model.event_response import EventResponse
from fastly.model.events_response import EventsResponse


class EventsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_event_endpoint = _Endpoint(
            settings={
                'response_type': (EventResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/events/{event_id}',
                'operation_id': 'get_event',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'event_id',
                ],
                'required': [
                    'event_id',
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
                    'event_id':
                        (str,),
                },
                'attribute_map': {
                    'event_id': 'event_id',
                },
                'location_map': {
                    'event_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.list_events_endpoint = _Endpoint(
            settings={
                'response_type': (EventsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/events',
                'operation_id': 'list_events',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_customer_id',
                    'filter_event_type',
                    'filter_service_id',
                    'filter_user_id',
                    'filter_token_id',
                    'page_number',
                    'page_size',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
                ],
                'validation': [
                    'page_size',
                ]
            },
            root_map={
                'validations': {
                    ('page_size',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('sort',): {

                        "asc": "created_at",
                        "desc": "-created_at"
                    },
                },
                'openapi_types': {
                    'filter_customer_id':
                        (str,),
                    'filter_event_type':
                        (str,),
                    'filter_service_id':
                        (str,),
                    'filter_user_id':
                        (str,),
                    'filter_token_id':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'filter_customer_id': 'filter[customer_id]',
                    'filter_event_type': 'filter[event_type]',
                    'filter_service_id': 'filter[service_id]',
                    'filter_user_id': 'filter[user_id]',
                    'filter_token_id': 'filter[token_id]',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'sort': 'sort',
                },
                'location_map': {
                    'filter_customer_id': 'query',
                    'filter_event_type': 'query',
                    'filter_service_id': 'query',
                    'filter_user_id': 'query',
                    'filter_token_id': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                    'sort': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_event(
        self,
        event_id,
        **kwargs
    ):
        """Get an event  # noqa: E501

        Get a specific event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_event(event_id, async_req=True)
        >>> result = thread.get()

        Args:
            event_id (str): Alphanumeric string identifying an event.

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
            EventResponse
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
        kwargs['event_id'] = \
            event_id
        return self.get_event_endpoint.call_with_http_info(**kwargs)

    def list_events(
        self,
        **kwargs
    ):
        """List events  # noqa: E501

        List all events for a particular customer. Events can be filtered by user, customer and event type. Events can be sorted by date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_events(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_customer_id (str): Limit the results returned to a specific customer.. [optional]
            filter_event_type (str): Limit the returned events to a specific `event_type`.. [optional]
            filter_service_id (str): Limit the results returned to a specific service.. [optional]
            filter_user_id (str): Limit the results returned to a specific user.. [optional]
            filter_token_id (str): Limit the returned events to a specific token.. [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            sort (str): The order in which to list the results by creation date.. [optional] if omitted the server will use the default value of "created_at"
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
            EventsResponse
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
        return self.list_events_endpoint.call_with_http_info(**kwargs)

