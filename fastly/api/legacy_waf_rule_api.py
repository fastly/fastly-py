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


class LegacyWafRuleApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_legacy_waf_firewall_rule_vcl_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/wafs/{firewall_id}/rules/{waf_rule_id}/vcl',
                'operation_id': 'get_legacy_waf_firewall_rule_vcl',
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
                    'firewall_id',
                    'waf_rule_id',
                ],
                'required': [
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
                    'firewall_id':
                        (str,),
                    'waf_rule_id':
                        (str,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'waf_rule_id': 'waf_rule_id',
                },
                'location_map': {
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
        self.get_legacy_waf_rule_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/wafs/rules/{waf_rule_id}',
                'operation_id': 'get_legacy_waf_rule',
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
                    'waf_rule_id',
                    'filter_configuration_set_id',
                    'include',
                ],
                'required': [
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
                    'waf_rule_id':
                        (str,),
                    'filter_configuration_set_id':
                        (str,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'waf_rule_id': 'waf_rule_id',
                    'filter_configuration_set_id': 'filter[configuration_set_id]',
                    'include': 'include',
                },
                'location_map': {
                    'waf_rule_id': 'path',
                    'filter_configuration_set_id': 'query',
                    'include': 'query',
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
        self.get_legacy_waf_rule_vcl_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/wafs/rules/{waf_rule_id}/vcl',
                'operation_id': 'get_legacy_waf_rule_vcl',
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
                    'waf_rule_id',
                ],
                'required': [
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
                    'waf_rule_id':
                        (str,),
                },
                'attribute_map': {
                    'waf_rule_id': 'waf_rule_id',
                },
                'location_map': {
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
        self.list_legacy_waf_rules_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/wafs/rules',
                'operation_id': 'list_legacy_waf_rules',
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
                    'filter_rule_id',
                    'filter_severity',
                    'filter_tags_name',
                    'filter_configuration_set_id',
                    'page_number',
                    'page_size',
                    'include',
                ],
                'required': [],
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
                    'filter_rule_id':
                        (str,),
                    'filter_severity':
                        (str,),
                    'filter_tags_name':
                        (str,),
                    'filter_configuration_set_id':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'filter_rule_id': 'filter[rule_id]',
                    'filter_severity': 'filter[severity]',
                    'filter_tags_name': 'filter[tags][name]',
                    'filter_configuration_set_id': 'filter[configuration_set_id]',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'include': 'include',
                },
                'location_map': {
                    'filter_rule_id': 'query',
                    'filter_severity': 'query',
                    'filter_tags_name': 'query',
                    'filter_configuration_set_id': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                    'include': 'query',
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

    def get_legacy_waf_firewall_rule_vcl(
        self,
        firewall_id,
        waf_rule_id,
        **kwargs
    ):
        """Get VCL for a rule associated with a firewall  # noqa: E501

        Get associated VCL for a specific rule associated with a specific firewall.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_legacy_waf_firewall_rule_vcl(firewall_id, waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
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
        kwargs['firewall_id'] = \
            firewall_id
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.get_legacy_waf_firewall_rule_vcl_endpoint.call_with_http_info(**kwargs)

    def get_legacy_waf_rule(
        self,
        waf_rule_id,
        **kwargs
    ):
        """Get a rule  # noqa: E501

        Get a specific rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_legacy_waf_rule(waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

        Keyword Args:
            filter_configuration_set_id (str): Optional. Limit rule to a specific configuration set or pass \"all\" to search all configuration sets, including stale ones.. [optional]
            include (str): Include relationships. Optional. Comma separated values. Permitted values: `tags`, `rule_statuses`, `source`, and `vcl`. . [optional]
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
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.get_legacy_waf_rule_endpoint.call_with_http_info(**kwargs)

    def get_legacy_waf_rule_vcl(
        self,
        waf_rule_id,
        **kwargs
    ):
        """Get VCL for a rule  # noqa: E501

        Get associated VCL for a specific rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_legacy_waf_rule_vcl(waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
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
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.get_legacy_waf_rule_vcl_endpoint.call_with_http_info(**kwargs)

    def list_legacy_waf_rules(
        self,
        **kwargs
    ):
        """List rules in the latest configuration set  # noqa: E501

        List all rules in the latest configuration set.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_legacy_waf_rules(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_rule_id (str): Limit the returned rules to a specific rule ID.. [optional]
            filter_severity (str): Limit the returned rules to a specific severity.. [optional]
            filter_tags_name (str): Limit the returned rules to a set linked to a tag by name.. [optional]
            filter_configuration_set_id (str): Optional. Limit rules to specific configuration set or pass \"all\" to search all configuration sets, including stale ones.. [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            include (str): Include relationships. Optional. Comma separated values. Permitted values: `tags`, `rule_statuses`, and `source`. . [optional]
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
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
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
        return self.list_legacy_waf_rules_endpoint.call_with_http_info(**kwargs)

