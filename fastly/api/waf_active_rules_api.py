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
from fastly.model.bulk_waf_active_rules import BulkWafActiveRules
from fastly.model.waf_active_rule import WafActiveRule
from fastly.model.waf_active_rule_creation_response import WafActiveRuleCreationResponse
from fastly.model.waf_active_rule_data import WafActiveRuleData
from fastly.model.waf_active_rule_response import WafActiveRuleResponse
from fastly.model.waf_active_rules_response import WafActiveRulesResponse


class WafActiveRulesApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bulk_update_waf_active_rules_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/bulk',
                'operation_id': 'bulk_update_waf_active_rules',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'body',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
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
                    'version_id':
                        (int,),
                    'body':
                        (WafActiveRuleData,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
                    'body': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )
        self.create_waf_active_rule_endpoint = _Endpoint(
            settings={
                'response_type': (WafActiveRuleCreationResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/active-rules',
                'operation_id': 'create_waf_active_rule',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'waf_active_rule',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
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
                    'version_id':
                        (int,),
                    'waf_active_rule':
                        (WafActiveRule,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
                    'waf_active_rule': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/vnd.api+json'
                ],
                'content_type': [
                    'application/vnd.api+json',
                    'application/vnd.api+json; ext=bulk'
                ]
            },
            api_client=api_client
        )
        self.create_waf_active_rules_tag_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/tags/{waf_tag_name}/active-rules',
                'operation_id': 'create_waf_active_rules_tag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'waf_tag_name',
                    'waf_active_rule',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
                    'waf_tag_name',
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
                    'version_id':
                        (int,),
                    'waf_tag_name':
                        (str,),
                    'waf_active_rule':
                        (WafActiveRule,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                    'waf_tag_name': 'waf_tag_name',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
                    'waf_tag_name': 'path',
                    'waf_active_rule': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [
                    'application/vnd.api+json'
                ]
            },
            api_client=api_client
        )
        self.delete_waf_active_rule_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id}',
                'operation_id': 'delete_waf_active_rule',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'waf_rule_id',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
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
                    'version_id':
                        (int,),
                    'waf_rule_id':
                        (str,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                    'waf_rule_id': 'waf_rule_id',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
                    'waf_rule_id': 'path',
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
        self.get_waf_active_rule_endpoint = _Endpoint(
            settings={
                'response_type': (WafActiveRuleResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id}',
                'operation_id': 'get_waf_active_rule',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'waf_rule_id',
                    'include',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
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
                    'version_id':
                        (int,),
                    'waf_rule_id':
                        (str,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                    'waf_rule_id': 'waf_rule_id',
                    'include': 'include',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
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
        self.list_waf_active_rules_endpoint = _Endpoint(
            settings={
                'response_type': (WafActiveRulesResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/active-rules',
                'operation_id': 'list_waf_active_rules',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'filter_status',
                    'filter_waf_rule_revision_message',
                    'filter_waf_rule_revision_modsec_rule_id',
                    'filter_outdated',
                    'include',
                    'page_number',
                    'page_size',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
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
                    'firewall_id':
                        (str,),
                    'version_id':
                        (int,),
                    'filter_status':
                        (str,),
                    'filter_waf_rule_revision_message':
                        (str,),
                    'filter_waf_rule_revision_modsec_rule_id':
                        (str,),
                    'filter_outdated':
                        (str,),
                    'include':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                    'filter_status': 'filter[status]',
                    'filter_waf_rule_revision_message': 'filter[waf_rule_revision][message]',
                    'filter_waf_rule_revision_modsec_rule_id': 'filter[waf_rule_revision][modsec_rule_id]',
                    'filter_outdated': 'filter[outdated]',
                    'include': 'include',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
                    'filter_status': 'query',
                    'filter_waf_rule_revision_message': 'query',
                    'filter_waf_rule_revision_modsec_rule_id': 'query',
                    'filter_outdated': 'query',
                    'include': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
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
        self.update_waf_active_rule_endpoint = _Endpoint(
            settings={
                'response_type': (WafActiveRuleResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id}',
                'operation_id': 'update_waf_active_rule',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'version_id',
                    'waf_rule_id',
                    'waf_active_rule',
                ],
                'required': [
                    'firewall_id',
                    'version_id',
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
                    'version_id':
                        (int,),
                    'waf_rule_id':
                        (str,),
                    'waf_active_rule':
                        (WafActiveRule,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'version_id': 'version_id',
                    'waf_rule_id': 'waf_rule_id',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'version_id': 'path',
                    'waf_rule_id': 'path',
                    'waf_active_rule': 'body',
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

    def bulk_update_waf_active_rules(
        self,
        firewall_id,
        version_id,
        **kwargs
    ):
        """Update multiple active rules  # noqa: E501

        Bulk update all active rules on a [firewall version](https://developer.fastly.com/reference/api/waf/firewall-version/). This endpoint will not add new active rules, only update existing active rules.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_update_waf_active_rules(firewall_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            body (WafActiveRuleData): [optional]
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
        kwargs['firewall_id'] = \
            firewall_id
        kwargs['version_id'] = \
            version_id
        return self.bulk_update_waf_active_rules_endpoint.call_with_http_info(**kwargs)

    def create_waf_active_rule(
        self,
        firewall_id,
        version_id,
        **kwargs
    ):
        """Add a rule to a WAF as an active rule  # noqa: E501

        Create an active rule for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_waf_active_rule(firewall_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            waf_active_rule (WafActiveRule): [optional]
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
            WafActiveRuleCreationResponse
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
        kwargs['version_id'] = \
            version_id
        return self.create_waf_active_rule_endpoint.call_with_http_info(**kwargs)

    def create_waf_active_rules_tag(
        self,
        firewall_id,
        version_id,
        waf_tag_name,
        **kwargs
    ):
        """Create active rules by tag  # noqa: E501

        Create active rules by tag. This endpoint will create active rules using the latest revision available for each rule.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_waf_active_rules_tag(firewall_id, version_id, waf_tag_name, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.
            waf_tag_name (str): Name of the tag.

        Keyword Args:
            waf_active_rule (WafActiveRule): [optional]
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
        kwargs['firewall_id'] = \
            firewall_id
        kwargs['version_id'] = \
            version_id
        kwargs['waf_tag_name'] = \
            waf_tag_name
        return self.create_waf_active_rules_tag_endpoint.call_with_http_info(**kwargs)

    def delete_waf_active_rule(
        self,
        firewall_id,
        version_id,
        waf_rule_id,
        **kwargs
    ):
        """Delete an active rule  # noqa: E501

        Delete an active rule for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_waf_active_rule(firewall_id, version_id, waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.
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
        kwargs['firewall_id'] = \
            firewall_id
        kwargs['version_id'] = \
            version_id
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.delete_waf_active_rule_endpoint.call_with_http_info(**kwargs)

    def get_waf_active_rule(
        self,
        firewall_id,
        version_id,
        waf_rule_id,
        **kwargs
    ):
        """Get an active WAF rule object  # noqa: E501

        Get a specific active rule object. Includes details of the rule revision associated with the active rule object by default.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waf_active_rule(firewall_id, version_id, waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

        Keyword Args:
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_rule_revision` and `waf_firewall_version`. . [optional]
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
            WafActiveRuleResponse
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
        kwargs['version_id'] = \
            version_id
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.get_waf_active_rule_endpoint.call_with_http_info(**kwargs)

    def list_waf_active_rules(
        self,
        firewall_id,
        version_id,
        **kwargs
    ):
        """List active rules on a WAF  # noqa: E501

        List all active rules for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_waf_active_rules(firewall_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            filter_status (str): Limit results to active rules with the specified status.. [optional]
            filter_waf_rule_revision_message (str): Limit results to active rules with the specified message.. [optional]
            filter_waf_rule_revision_modsec_rule_id (str): Limit results to active rules that represent the specified ModSecurity modsec_rule_id.. [optional]
            filter_outdated (str): Limit results to active rules referencing an outdated rule revision.. [optional]
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_rule_revision` and `waf_firewall_version`. . [optional]
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
            WafActiveRulesResponse
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
        kwargs['version_id'] = \
            version_id
        return self.list_waf_active_rules_endpoint.call_with_http_info(**kwargs)

    def update_waf_active_rule(
        self,
        firewall_id,
        version_id,
        waf_rule_id,
        **kwargs
    ):
        """Update an active rule  # noqa: E501

        Update an active rule's status for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_waf_active_rule(firewall_id, version_id, waf_rule_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            version_id (int): Integer identifying a service version.
            waf_rule_id (str): Alphanumeric string identifying a WAF rule.

        Keyword Args:
            waf_active_rule (WafActiveRule): [optional]
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
            WafActiveRuleResponse
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
        kwargs['version_id'] = \
            version_id
        kwargs['waf_rule_id'] = \
            waf_rule_id
        return self.update_waf_active_rule_endpoint.call_with_http_info(**kwargs)

