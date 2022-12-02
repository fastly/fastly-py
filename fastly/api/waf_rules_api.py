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
from fastly.model.waf_rule_response import WafRuleResponse
from fastly.model.waf_rules_response import WafRulesResponse


class WafRulesApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_waf_rule_endpoint = _Endpoint(
            settings={
                'response_type': (WafRuleResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/rules/{waf_rule_id}',
                'operation_id': 'get_waf_rule',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'waf_rule_id',
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
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'waf_rule_id': 'waf_rule_id',
                    'include': 'include',
                },
                'location_map': {
                    'waf_rule_id': 'path',
                    'include': 'query',
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
        self.list_waf_rules_endpoint = _Endpoint(
            settings={
                'response_type': (WafRulesResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/rules',
                'operation_id': 'list_waf_rules',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_modsec_rule_id',
                    'filter_waf_tags_name',
                    'filter_waf_rule_revisions_source',
                    'filter_waf_firewall_id_not_match',
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
                    'filter_modsec_rule_id':
                        (str,),
                    'filter_waf_tags_name':
                        (str,),
                    'filter_waf_rule_revisions_source':
                        (str,),
                    'filter_waf_firewall_id_not_match':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'filter_modsec_rule_id': 'filter[modsec_rule_id]',
                    'filter_waf_tags_name': 'filter[waf_tags][name]',
                    'filter_waf_rule_revisions_source': 'filter[waf_rule_revisions][source]',
                    'filter_waf_firewall_id_not_match': 'filter[waf_firewall.id][not][match]',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'include': 'include',
                },
                'location_map': {
                    'filter_modsec_rule_id': 'query',
                    'filter_waf_tags_name': 'query',
                    'filter_waf_rule_revisions_source': 'query',
                    'filter_waf_firewall_id_not_match': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                    'include': 'query',
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

    def get_waf_rule(
        self,
        waf_rule_id,
        **kwargs
    ):
        """Get a rule  # noqa: E501

        Get a specific rule. The `id` provided can be the ModSecurity Rule ID or the Fastly generated rule ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waf_rule(waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

        Keyword Args:
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_tags` and `waf_rule_revisions`. . [optional]
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
            WafRuleResponse
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
        return self.get_waf_rule_endpoint.call_with_http_info(**kwargs)

    def list_waf_rules(
        self,
        **kwargs
    ):
        """List available WAF rules  # noqa: E501

        List all available WAF rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_waf_rules(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_modsec_rule_id (str): Limit the returned rules to a specific ModSecurity rule ID.. [optional]
            filter_waf_tags_name (str): Limit the returned rules to a set linked to a tag by name.. [optional]
            filter_waf_rule_revisions_source (str): Limit the returned rules to a set linked to a source.. [optional]
            filter_waf_firewall_id_not_match (str): Limit the returned rules to a set not included in the active firewall version for a firewall.. [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_tags` and `waf_rule_revisions`. . [optional]
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
            WafRulesResponse
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
        return self.list_waf_rules_endpoint.call_with_http_info(**kwargs)

