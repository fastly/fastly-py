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
from fastly.model.waf_rule_revision_response import WafRuleRevisionResponse
from fastly.model.waf_rule_revisions_response import WafRuleRevisionsResponse


class WafRuleRevisionsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_waf_rule_revision_endpoint = _Endpoint(
            settings={
                'response_type': (WafRuleRevisionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/rules/{waf_rule_id}/revisions/{waf_rule_revision_number}',
                'operation_id': 'get_waf_rule_revision',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'waf_rule_id',
                    'waf_rule_revision_number',
                    'include',
                ],
                'required': [
                    'waf_rule_id',
                    'waf_rule_revision_number',
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
                    'waf_rule_revision_number':
                        (int,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'waf_rule_id': 'waf_rule_id',
                    'waf_rule_revision_number': 'waf_rule_revision_number',
                    'include': 'include',
                },
                'location_map': {
                    'waf_rule_id': 'path',
                    'waf_rule_revision_number': 'path',
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
        self.list_waf_rule_revisions_endpoint = _Endpoint(
            settings={
                'response_type': (WafRuleRevisionsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/rules/{waf_rule_id}/revisions',
                'operation_id': 'list_waf_rule_revisions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'waf_rule_id',
                    'page_number',
                    'page_size',
                    'include',
                ],
                'required': [
                    'waf_rule_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'include',
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
                    ('include',): {

                        "WAF_RULE": "waf_rule"
                    },
                },
                'openapi_types': {
                    'waf_rule_id':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'waf_rule_id': 'waf_rule_id',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'include': 'include',
                },
                'location_map': {
                    'waf_rule_id': 'path',
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

    def get_waf_rule_revision(
        self,
        waf_rule_id,
        waf_rule_revision_number,
        **kwargs
    ):
        """Get a revision of a rule  # noqa: E501

        Get a specific rule revision.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waf_rule_revision(waf_rule_id, waf_rule_revision_number, async_req=True)
        >>> result = thread.get()

        Args:
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.
            waf_rule_revision_number (int): Revision number.

        Keyword Args:
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_rule`, `vcl`, and `source`. The `vcl` and `source` relationships show the WAF VCL and corresponding ModSecurity source. These fields are blank unless the relationship is included. . [optional]
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
            WafRuleRevisionResponse
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
        kwargs['waf_rule_revision_number'] = \
            waf_rule_revision_number
        return self.get_waf_rule_revision_endpoint.call_with_http_info(**kwargs)

    def list_waf_rule_revisions(
        self,
        waf_rule_id,
        **kwargs
    ):
        """List revisions for a rule  # noqa: E501

        List all revisions for a specific rule. The `rule_id` provided can be the ModSecurity Rule ID or the Fastly generated rule ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_waf_rule_revisions(waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

        Keyword Args:
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            include (str): Include relationships. Optional.. [optional] if omitted the server will use the default value of "waf_rule"
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
            WafRuleRevisionsResponse
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
        return self.list_waf_rule_revisions_endpoint.call_with_http_info(**kwargs)

