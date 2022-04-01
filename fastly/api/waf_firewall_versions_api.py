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
from fastly.model.waf_firewall_version import WafFirewallVersion
from fastly.model.waf_firewall_version_response import WafFirewallVersionResponse
from fastly.model.waf_firewall_versions_response import WafFirewallVersionsResponse


class WafFirewallVersionsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.clone_waf_firewall_version_endpoint = _Endpoint(
            settings={
                'response_type': (WafFirewallVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/clone',
                'operation_id': 'clone_waf_firewall_version',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
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
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
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
        self.create_waf_firewall_version_endpoint = _Endpoint(
            settings={
                'response_type': (WafFirewallVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions',
                'operation_id': 'create_waf_firewall_version',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'waf_firewall_version',
                ],
                'required': [
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
                    'firewall_id':
                        (str,),
                    'waf_firewall_version':
                        (WafFirewallVersion,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'waf_firewall_version': 'body',
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
        self.deploy_activate_waf_firewall_version_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}/activate',
                'operation_id': 'deploy_activate_waf_firewall_version',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
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
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
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
        self.get_waf_firewall_version_endpoint = _Endpoint(
            settings={
                'response_type': (WafFirewallVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}',
                'operation_id': 'get_waf_firewall_version',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'include',
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
                    'include':
                        (str,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                    'include': 'include',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
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
        self.list_waf_firewall_versions_endpoint = _Endpoint(
            settings={
                'response_type': (WafFirewallVersionsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions',
                'operation_id': 'list_waf_firewall_versions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'include',
                    'page_number',
                    'page_size',
                ],
                'required': [
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
                    'firewall_id':
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
                    'include': 'include',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                },
                'location_map': {
                    'firewall_id': 'path',
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
        self.update_waf_firewall_version_endpoint = _Endpoint(
            settings={
                'response_type': (WafFirewallVersionResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/waf/firewalls/{firewall_id}/versions/{firewall_version_number}',
                'operation_id': 'update_waf_firewall_version',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'firewall_id',
                    'firewall_version_number',
                    'waf_firewall_version',
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
                    'waf_firewall_version':
                        (WafFirewallVersion,),
                },
                'attribute_map': {
                    'firewall_id': 'firewall_id',
                    'firewall_version_number': 'firewall_version_number',
                },
                'location_map': {
                    'firewall_id': 'path',
                    'firewall_version_number': 'path',
                    'waf_firewall_version': 'body',
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

    def clone_waf_firewall_version(
        self,
        firewall_id,
        firewall_version_number,
        **kwargs
    ):
        """Clone a firewall version  # noqa: E501

        Clone a specific, existing firewall version into a new, draft firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.clone_waf_firewall_version(firewall_id, firewall_version_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.

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
            WafFirewallVersionResponse
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
        return self.clone_waf_firewall_version_endpoint.call_with_http_info(**kwargs)

    def create_waf_firewall_version(
        self,
        firewall_id,
        **kwargs
    ):
        """Create a firewall version  # noqa: E501

        Create a new, draft firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_waf_firewall_version(firewall_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.

        Keyword Args:
            waf_firewall_version (WafFirewallVersion): [optional]
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
            WafFirewallVersionResponse
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
        return self.create_waf_firewall_version_endpoint.call_with_http_info(**kwargs)

    def deploy_activate_waf_firewall_version(
        self,
        firewall_id,
        firewall_version_number,
        **kwargs
    ):
        """Deploy or activate a firewall version  # noqa: E501

        Deploy or activate a specific firewall version. If a firewall has been disabled, deploying a firewall version will automatically enable the firewall again.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.deploy_activate_waf_firewall_version(firewall_id, firewall_version_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.

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
        kwargs['firewall_version_number'] = \
            firewall_version_number
        return self.deploy_activate_waf_firewall_version_endpoint.call_with_http_info(**kwargs)

    def get_waf_firewall_version(
        self,
        firewall_id,
        firewall_version_number,
        **kwargs
    ):
        """Get a firewall version  # noqa: E501

        Get details about a specific firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_waf_firewall_version(firewall_id, firewall_version_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.

        Keyword Args:
            include (str): Include relationships. Optional, comma-separated values. Permitted values: `waf_firewall` and `waf_active_rules`. . [optional]
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
            WafFirewallVersionResponse
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
        return self.get_waf_firewall_version_endpoint.call_with_http_info(**kwargs)

    def list_waf_firewall_versions(
        self,
        firewall_id,
        **kwargs
    ):
        """List firewall versions  # noqa: E501

        Get a list of firewall versions associated with a specific firewall.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_waf_firewall_versions(firewall_id, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.

        Keyword Args:
            include (str): Include relationships. Optional.. [optional]
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
            WafFirewallVersionsResponse
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
        return self.list_waf_firewall_versions_endpoint.call_with_http_info(**kwargs)

    def update_waf_firewall_version(
        self,
        firewall_id,
        firewall_version_number,
        **kwargs
    ):
        """Update a firewall version  # noqa: E501

        Update a specific firewall version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_waf_firewall_version(firewall_id, firewall_version_number, async_req=True)
        >>> result = thread.get()

        Args:
            firewall_id (str): Alphanumeric string identifying a WAF Firewall.
            firewall_version_number (int): Integer identifying a WAF firewall version.

        Keyword Args:
            waf_firewall_version (WafFirewallVersion): [optional]
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
            WafFirewallVersionResponse
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
        return self.update_waf_firewall_version_endpoint.call_with_http_info(**kwargs)

