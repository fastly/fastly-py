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
from fastly.model.ddos_protection_error import DdosProtectionError
from fastly.model.ddos_protection_event import DdosProtectionEvent
from fastly.model.ddos_protection_invalid_request import DdosProtectionInvalidRequest
from fastly.model.ddos_protection_not_authenticated import DdosProtectionNotAuthenticated
from fastly.model.ddos_protection_not_authorized import DdosProtectionNotAuthorized
from fastly.model.ddos_protection_not_found import DdosProtectionNotFound
from fastly.model.ddos_protection_rule import DdosProtectionRule
from fastly.model.ddos_protection_rule_patch import DdosProtectionRulePatch
from fastly.model.ddos_protection_traffic_stats import DdosProtectionTrafficStats
from fastly.model.inline_response2002 import InlineResponse2002
from fastly.model.inline_response2003 import InlineResponse2003


class DdosProtectionApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.ddos_protection_event_get_endpoint = _Endpoint(
            settings={
                'response_type': (DdosProtectionEvent,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ddos-protection/v1/events/{event_id}',
                'operation_id': 'ddos_protection_event_get',
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
        self.ddos_protection_event_list_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2002,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ddos-protection/v1/events',
                'operation_id': 'ddos_protection_event_list',
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
                    'cursor',
                    'limit',
                    'service_id',
                    '_from',
                    'to',
                    'name',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                    'service_id':
                        (str,),
                    '_from':
                        (datetime,),
                    'to':
                        (datetime,),
                    'name':
                        (str,),
                },
                'attribute_map': {
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'service_id': 'service_id',
                    '_from': 'from',
                    'to': 'to',
                    'name': 'name',
                },
                'location_map': {
                    'cursor': 'query',
                    'limit': 'query',
                    'service_id': 'query',
                    '_from': 'query',
                    'to': 'query',
                    'name': 'query',
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
        self.ddos_protection_event_rule_list_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse2003,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ddos-protection/v1/events/{event_id}/rules',
                'operation_id': 'ddos_protection_event_rule_list',
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
                    'event_id',
                    'cursor',
                    'limit',
                    'include',
                ],
                'required': [
                    'event_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'limit',
                ]
            },
            root_map={
                'validations': {
                    ('limit',): {

                        'inclusive_maximum': 100,
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'event_id':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (int,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'event_id': 'event_id',
                    'cursor': 'cursor',
                    'limit': 'limit',
                    'include': 'include',
                },
                'location_map': {
                    'event_id': 'path',
                    'cursor': 'query',
                    'limit': 'query',
                    'include': 'query',
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
        self.ddos_protection_rule_get_endpoint = _Endpoint(
            settings={
                'response_type': (DdosProtectionRule,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ddos-protection/v1/rules/{rule_id}',
                'operation_id': 'ddos_protection_rule_get',
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
                    'rule_id',
                ],
                'required': [
                    'rule_id',
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
                    'rule_id':
                        (str,),
                },
                'attribute_map': {
                    'rule_id': 'rule_id',
                },
                'location_map': {
                    'rule_id': 'path',
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
        self.ddos_protection_rule_patch_endpoint = _Endpoint(
            settings={
                'response_type': (DdosProtectionRule,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ddos-protection/v1/rules/{rule_id}',
                'operation_id': 'ddos_protection_rule_patch',
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
                    'rule_id',
                    'ddos_protection_rule_patch',
                ],
                'required': [
                    'rule_id',
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
                    'rule_id':
                        (str,),
                    'ddos_protection_rule_patch':
                        (DdosProtectionRulePatch,),
                },
                'attribute_map': {
                    'rule_id': 'rule_id',
                },
                'location_map': {
                    'rule_id': 'path',
                    'ddos_protection_rule_patch': 'body',
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
        self.ddos_protection_traffic_stats_rule_get_endpoint = _Endpoint(
            settings={
                'response_type': (DdosProtectionTrafficStats,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/ddos-protection/v1/events/{event_id}/rules/{rule_id}/traffic-stats',
                'operation_id': 'ddos_protection_traffic_stats_rule_get',
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
                    'event_id',
                    'rule_id',
                ],
                'required': [
                    'event_id',
                    'rule_id',
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
                    'rule_id':
                        (str,),
                },
                'attribute_map': {
                    'event_id': 'event_id',
                    'rule_id': 'rule_id',
                },
                'location_map': {
                    'event_id': 'path',
                    'rule_id': 'path',
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

    def ddos_protection_event_get(
        self,
        event_id,
        **kwargs
    ):
        """Get event by ID  # noqa: E501

        Get event by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ddos_protection_event_get(event_id, async_req=True)
        >>> result = thread.get()

        Args:
            event_id (str): Unique ID of the event.

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
            DdosProtectionEvent
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
        return self.ddos_protection_event_get_endpoint.call_with_http_info(**kwargs)

    def ddos_protection_event_list(
        self,
        **kwargs
    ):
        """Get events  # noqa: E501

        Get events.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ddos_protection_event_list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 20
            service_id (str): Filter results based on a service_id.. [optional]
            _from (datetime): Represents the start of a date-time range expressed in RFC 3339 format.. [optional]
            to (datetime): Represents the end of a date-time range expressed in RFC 3339 format.. [optional]
            name (str): [optional]
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
        return self.ddos_protection_event_list_endpoint.call_with_http_info(**kwargs)

    def ddos_protection_event_rule_list(
        self,
        event_id,
        **kwargs
    ):
        """Get all rules for an event  # noqa: E501

        Get all rules for an event.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ddos_protection_event_rule_list(event_id, async_req=True)
        >>> result = thread.get()

        Args:
            event_id (str): Unique ID of the event.

        Keyword Args:
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (int): Limit how many results are returned.. [optional] if omitted the server will use the default value of 20
            include (str): Include relationships. Optional. Comma-separated values.. [optional]
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
        kwargs['event_id'] = \
            event_id
        return self.ddos_protection_event_rule_list_endpoint.call_with_http_info(**kwargs)

    def ddos_protection_rule_get(
        self,
        rule_id,
        **kwargs
    ):
        """Get a rule by ID  # noqa: E501

        Get a rule by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ddos_protection_rule_get(rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            rule_id (str): Unique ID of the rule.

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
            DdosProtectionRule
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
        kwargs['rule_id'] = \
            rule_id
        return self.ddos_protection_rule_get_endpoint.call_with_http_info(**kwargs)

    def ddos_protection_rule_patch(
        self,
        rule_id,
        **kwargs
    ):
        """Update rule  # noqa: E501

        Update rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ddos_protection_rule_patch(rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            rule_id (str): Unique ID of the rule.

        Keyword Args:
            ddos_protection_rule_patch (DdosProtectionRulePatch): [optional]
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
            DdosProtectionRule
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
        kwargs['rule_id'] = \
            rule_id
        return self.ddos_protection_rule_patch_endpoint.call_with_http_info(**kwargs)

    def ddos_protection_traffic_stats_rule_get(
        self,
        event_id,
        rule_id,
        **kwargs
    ):
        """Get traffic stats for a rule  # noqa: E501

        Get traffic stats for a rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.ddos_protection_traffic_stats_rule_get(event_id, rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            event_id (str): Unique ID of the event.
            rule_id (str): Unique ID of the rule.

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
            DdosProtectionTrafficStats
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
        kwargs['rule_id'] = \
            rule_id
        return self.ddos_protection_traffic_stats_rule_get_endpoint.call_with_http_info(**kwargs)

