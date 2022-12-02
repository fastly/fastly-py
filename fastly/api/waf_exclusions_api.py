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
from fastly.model.waf_exclusion import WafExclusion
from fastly.model.waf_exclusion_response import WafExclusionResponse
from fastly.model.waf_exclusions_response import WafExclusionsResponse


class WafExclusionsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_waf_rule_exclusion_endpoint = _Endpoint(
            settings={
                'response_type': (WafExclusionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions',
                'operation_id': 'create_waf_rule_exclusion',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'waf_exclusion',
                ],
                'required': [
                    'firewall_id',
                    'firewall_version_number',
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
                    'firewall_version_number':
                        (int,),
                    'waf_exclusion':
                        (WafExclusion,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
                    'waf_exclusion': 'body',
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
        self.delete_waf_rule_exclusion_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number}',
                'operation_id': 'delete_waf_rule_exclusion',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'exclusion_number',
                ],
                'required': [
                    'firewall_id',
                    'firewall_version_number',
                    'exclusion_number',
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
                    'firewall_version_number':
                        (int,),
                    'exclusion_number':
                        (int,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                    'exclusion_number': 'exclusion_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
                    'exclusion_number': 'path',
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
        self.get_waf_rule_exclusion_endpoint = _Endpoint(
            settings={
                'response_type': (WafExclusionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number}',
                'operation_id': 'get_waf_rule_exclusion',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'exclusion_number',
                ],
                'required': [
                    'firewall_id',
                    'firewall_version_number',
                    'exclusion_number',
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
                    'firewall_version_number':
                        (int,),
                    'exclusion_number':
                        (int,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                    'exclusion_number': 'exclusion_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
                    'exclusion_number': 'path',
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
        self.list_waf_rule_exclusions_endpoint = _Endpoint(
            settings={
                'response_type': (WafExclusionsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions',
                'operation_id': 'list_waf_rule_exclusions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'filter_exclusion_type',
                    'filter_name',
                    'filter_waf_rules_modsec_rule_id',
                    'page_number',
                    'page_size',
                    'include',
                ],
                'required': [
                    'firewall_id',
                    'firewall_version_number',
                ],
                'nullable': [
                ],
                'enum': [
                    'filter_exclusion_type',
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
                    ('filter_exclusion_type',): {

                        "RULE": "rule",
                        "VARIABLE": "variable",
                        "WAF": "waf"
                    },
                },
                'openapi_types': {
                    'firewall_id':
                        (str,),
                    'firewall_version_number':
                        (int,),
                    'filter_exclusion_type':
                        (str,),
                    'filter_name':
                        (str,),
                    'filter_waf_rules_modsec_rule_id':
                        (int,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                    'filter_exclusion_type': 'filter[exclusion_type]',
                    'filter_name': 'filter[name]',
                    'filter_waf_rules_modsec_rule_id': 'filter[waf_rules.modsec_rule_id]',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'include': 'include',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
                    'filter_exclusion_type': 'query',
                    'filter_name': 'query',
                    'filter_waf_rules_modsec_rule_id': 'query',
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
        self.update_waf_rule_exclusion_endpoint = _Endpoint(
            settings={
                'response_type': (WafExclusionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number}',
                'operation_id': 'update_waf_rule_exclusion',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'exclusion_number',
                    'waf_exclusion',
                ],
                'required': [
                    'firewall_id',
                    'firewall_version_number',
                    'exclusion_number',
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
                    'firewall_version_number':
                        (int,),
                    'exclusion_number':
                        (int,),
                    'waf_exclusion':
                        (WafExclusion,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                    'exclusion_number': 'exclusion_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
                    'exclusion_number': 'path',
                    'waf_exclusion': 'body',
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

    def create_waf_rule_exclusion(
        self,
        firewall_id,
        firewall_version_number,
        **kwargs
    ):
        """Create a WAF rule exclusion  # noqa: E501

        Create a WAF exclusion for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_waf_rule_exclusion(firewall_id, firewall_version_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.

        Keyword Args:
            waf_exclusion (WafExclusion): [optional]
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
            WafExclusionResponse
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
        kwargs['firewall_version_number'] = \
            firewall_version_number
        return self.create_waf_rule_exclusion_endpoint.call_with_http_info(**kwargs)

    def delete_waf_rule_exclusion(
        self,
        firewall_id,
        firewall_version_number,
        exclusion_number,
        **kwargs
    ):
        """Delete a WAF rule exclusion  # noqa: E501

        Delete a WAF exclusion for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.
            exclusion_number (int): A numeric ID identifying a WAF exclusion.

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
        kwargs['firewall_version_number'] = \
            firewall_version_number
        kwargs['exclusion_number'] = \
            exclusion_number
        return self.delete_waf_rule_exclusion_endpoint.call_with_http_info(**kwargs)

    def get_waf_rule_exclusion(
        self,
        firewall_id,
        firewall_version_number,
        exclusion_number,
        **kwargs
    ):
        """Get a WAF rule exclusion  # noqa: E501

        Get a specific WAF exclusion object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.
            exclusion_number (int): A numeric ID identifying a WAF exclusion.

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
            WafExclusionResponse
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
        kwargs['firewall_version_number'] = \
            firewall_version_number
        kwargs['exclusion_number'] = \
            exclusion_number
        return self.get_waf_rule_exclusion_endpoint.call_with_http_info(**kwargs)

    def list_waf_rule_exclusions(
        self,
        firewall_id,
        firewall_version_number,
        **kwargs
    ):
        """List WAF rule exclusions  # noqa: E501

        List all exclusions for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_waf_rule_exclusions(firewall_id, firewall_version_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.

        Keyword Args:
            filter_exclusion_type (str): Filters the results based on this exclusion type.. [optional]
            filter_name (str): Filters the results based on name.. [optional]
            filter_waf_rules_modsec_rule_id (int): Filters the results based on this ModSecurity rule ID.. [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_rules` and `waf_rule_revisions`. . [optional]
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
            WafExclusionsResponse
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
        kwargs['firewall_version_number'] = \
            firewall_version_number
        return self.list_waf_rule_exclusions_endpoint.call_with_http_info(**kwargs)

    def update_waf_rule_exclusion(
        self,
        firewall_id,
        firewall_version_number,
        exclusion_number,
        **kwargs
    ):
        """Update a WAF rule exclusion  # noqa: E501

        Update a WAF exclusion for a particular firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_waf_rule_exclusion(firewall_id, firewall_version_number, exclusion_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.
            exclusion_number (int): A numeric ID identifying a WAF exclusion.

        Keyword Args:
            waf_exclusion (WafExclusion): [optional]
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
            WafExclusionResponse
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
        kwargs['firewall_version_number'] = \
            firewall_version_number
        kwargs['exclusion_number'] = \
            exclusion_number
        return self.update_waf_rule_exclusion_endpoint.call_with_http_info(**kwargs)

