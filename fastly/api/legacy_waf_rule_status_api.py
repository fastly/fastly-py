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


class LegacyWafRuleStatusApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_waf_firewall_rule_status_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/wafs/{firewall_id}/rules/{waf_rule_id}/rule_status',
                'operation_id': 'get_waf_firewall_rule_status',
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
                    'firewall_id',
                    'waf_rule_id',
                ],
                'required': [
                    'service_id',
                    'firewall_id',
                    'waf_rule_id',
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
                    'firewall_id':
                        (str,),
                    'waf_rule_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'firewall_id': 'firewall_id',
                    'waf_rule_id': 'waf_rule_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'firewall_id': 'path',
                    'waf_rule_id': 'path',
                },
                'path_params_allow_reserved_map': {
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
        self.list_waf_firewall_rule_statuses_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/wafs/{firewall_id}/rule_statuses',
                'operation_id': 'list_waf_firewall_rule_statuses',
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
                    'firewall_id',
                    'filter_status',
                    'filter_rule_message',
                    'filter_rule_rule_id',
                    'filter_rule_tags',
                    'filter_rule_tags_name',
                    'include',
                    'page_number',
                    'page_size',
                ],
                'required': [
                    'service_id',
                    'firewall_id',
                ],
                'nullable': [
                ],
                'enum': [
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
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'firewall_id':
                        (str,),
                    'filter_status':
                        (str,),
                    'filter_rule_message':
                        (str,),
                    'filter_rule_rule_id':
                        (str,),
                    'filter_rule_tags':
                        (str,),
                    'filter_rule_tags_name':
                        (str,),
                    'include':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'firewall_id': 'firewall_id',
                    'filter_status': 'filter[status]',
                    'filter_rule_message': 'filter[rule][message]',
                    'filter_rule_rule_id': 'filter[rule][rule_id]',
                    'filter_rule_tags': 'filter[rule][tags]',
                    'filter_rule_tags_name': 'filter[rule][tags][name]',
                    'include': 'include',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                },
                'location_map': {
                    'service_id': 'path',
                    'firewall_id': 'path',
                    'filter_status': 'query',
                    'filter_rule_message': 'query',
                    'filter_rule_rule_id': 'query',
                    'filter_rule_tags': 'query',
                    'filter_rule_tags_name': 'query',
                    'include': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                },
                'path_params_allow_reserved_map': {
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
        self.update_waf_firewall_rule_status_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/wafs/{firewall_id}/rules/{waf_rule_id}/rule_status',
                'operation_id': 'update_waf_firewall_rule_status',
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
                    'firewall_id',
                    'waf_rule_id',
                    'request_body',
                ],
                'required': [
                    'service_id',
                    'firewall_id',
                    'waf_rule_id',
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
                    'firewall_id':
                        (str,),
                    'waf_rule_id':
                        (str,),
                    'request_body':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'firewall_id': 'firewall_id',
                    'waf_rule_id': 'waf_rule_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'firewall_id': 'path',
                    'waf_rule_id': 'path',
                    'request_body': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )
        self.update_waf_firewall_rule_statuses_tag_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/wafs/{firewall_id}/rule_statuses',
                'operation_id': 'update_waf_firewall_rule_statuses_tag',
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
                    'firewall_id',
                    'name',
                    'force',
                    'request_body',
                ],
                'required': [
                    'service_id',
                    'firewall_id',
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
                    'firewall_id':
                        (str,),
                    'name':
                        (str,),
                    'force':
                        (str,),
                    'request_body':
                        ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'firewall_id': 'firewall_id',
                    'name': 'name',
                    'force': 'force',
                },
                'location_map': {
                    'service_id': 'path',
                    'firewall_id': 'path',
                    'name': 'query',
                    'force': 'query',
                    'request_body': 'body',
                },
                'path_params_allow_reserved_map': {
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )

    def get_waf_firewall_rule_status(
        self,
        service_id,
        firewall_id,
        waf_rule_id,
        **kwargs
    ):
        """Get the status of a rule on a firewall  # noqa: E501

        Get a specific rule status object for a particular service, firewall, and rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            firewall_id (str): Alphanumeric string identifying a Firewall.
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['firewall_id'] = \
            firewall_id
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.get_waf_firewall_rule_status_endpoint.call_with_http_info(**kwargs)

    def list_waf_firewall_rule_statuses(
        self,
        service_id,
        firewall_id,
        **kwargs
    ):
        """List rule statuses  # noqa: E501

        List all rule statuses for a particular service and firewall.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_waf_firewall_rule_statuses(service_id, firewall_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            firewall_id (str): Alphanumeric string identifying a Firewall.

        Keyword Args:
            filter_status (str): Limit results to rule statuses with the specified status.. [optional]
            filter_rule_message (str): Limit results to rule statuses whose rules have the specified message.. [optional]
            filter_rule_rule_id (str): Limit results to rule statuses whose rules represent the specified ModSecurity rule_id.. [optional]
            filter_rule_tags (str): Limit results to rule statuses whose rules relate to the specified tag IDs.. [optional]
            filter_rule_tags_name (str): Limit results to rule statuses whose rules related to the named tags.. [optional]
            include (str): Include relationships. Optional, comma separated values. Permitted values: `tags`. . [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['firewall_id'] = \
            firewall_id
        return self.list_waf_firewall_rule_statuses_endpoint.call_with_http_info(**kwargs)

    def update_waf_firewall_rule_status(
        self,
        service_id,
        firewall_id,
        waf_rule_id,
        **kwargs
    ):
        """Update the status of a rule  # noqa: E501

        Update a rule status for a particular service, firewall, and rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            firewall_id (str): Alphanumeric string identifying a Firewall.
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

        Keyword Args:
            request_body ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['firewall_id'] = \
            firewall_id
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.update_waf_firewall_rule_status_endpoint.call_with_http_info(**kwargs)

    def update_waf_firewall_rule_statuses_tag(
        self,
        service_id,
        firewall_id,
        **kwargs
    ):
        """Create or update status of a tagged group of rules  # noqa: E501

        Create or update all rule statuses for a particular service and firewall, based on tag name. By default, only rule status for enabled rules (with status log or block) will be updated. To update rule statuses for disabled rules under the specified tag, use the force attribute.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_waf_firewall_rule_statuses_tag(service_id, firewall_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            firewall_id (str): Alphanumeric string identifying a Firewall.

        Keyword Args:
            name (str): The tag name to use to determine the set of rules to update. For example, OWASP or language-php.. [optional]
            force (str): Whether or not to update rule statuses for disabled rules. Optional.. [optional]
            request_body ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): [optional]
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
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
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
        kwargs['firewall_id'] = \
            firewall_id
        return self.update_waf_firewall_rule_statuses_tag_endpoint.call_with_http_info(**kwargs)

