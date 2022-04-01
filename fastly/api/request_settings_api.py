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
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.request_settings_response import RequestSettingsResponse


class RequestSettingsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_request_settings_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/request_settings/{request_settings_name}',
                'operation_id': 'delete_request_settings',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'request_settings_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'request_settings_name',
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
                    'version_id':
                        (int,),
                    'request_settings_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'request_settings_name': 'request_settings_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'request_settings_name': 'path',
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
        self.get_request_settings_endpoint = _Endpoint(
            settings={
                'response_type': (RequestSettingsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/request_settings/{request_settings_name}',
                'operation_id': 'get_request_settings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'request_settings_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'request_settings_name',
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
                    'version_id':
                        (int,),
                    'request_settings_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'request_settings_name': 'request_settings_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'request_settings_name': 'path',
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
        self.list_request_settings_endpoint = _Endpoint(
            settings={
                'response_type': ([RequestSettingsResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/request_settings',
                'operation_id': 'list_request_settings',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                ],
                'required': [
                    'service_id',
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
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
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
        self.update_request_settings_endpoint = _Endpoint(
            settings={
                'response_type': (RequestSettingsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/request_settings/{request_settings_name}',
                'operation_id': 'update_request_settings',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'request_settings_name',
                    'action',
                    'bypass_busy_wait',
                    'default_host',
                    'force_miss',
                    'force_ssl',
                    'geo_headers',
                    'hash_keys',
                    'max_stale_age',
                    'name',
                    'request_condition',
                    'timer_support',
                    'xff',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'request_settings_name',
                ],
                'nullable': [
                    'action',
                    'default_host',
                    'hash_keys',
                    'request_condition',
                ],
                'enum': [
                    'action',
                    'xff',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('action',): {
                        'None': None,
                        "LOOKUP": "lookup",
                        "PASS": "pass"
                    },
                    ('xff',): {

                        "CLEAR": "clear",
                        "LEAVE": "leave",
                        "APPEND": "append",
                        "APPEND_ALL": "append_all",
                        "OVERWRITE": "overwrite"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'request_settings_name':
                        (str,),
                    'action':
                        (str, none_type,),
                    'bypass_busy_wait':
                        (int,),
                    'default_host':
                        (str, none_type,),
                    'force_miss':
                        (int,),
                    'force_ssl':
                        (int,),
                    'geo_headers':
                        (int,),
                    'hash_keys':
                        (str, none_type,),
                    'max_stale_age':
                        (int,),
                    'name':
                        (str,),
                    'request_condition':
                        (str, none_type,),
                    'timer_support':
                        (int,),
                    'xff':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'request_settings_name': 'request_settings_name',
                    'action': 'action',
                    'bypass_busy_wait': 'bypass_busy_wait',
                    'default_host': 'default_host',
                    'force_miss': 'force_miss',
                    'force_ssl': 'force_ssl',
                    'geo_headers': 'geo_headers',
                    'hash_keys': 'hash_keys',
                    'max_stale_age': 'max_stale_age',
                    'name': 'name',
                    'request_condition': 'request_condition',
                    'timer_support': 'timer_support',
                    'xff': 'xff',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'request_settings_name': 'path',
                    'action': 'form',
                    'bypass_busy_wait': 'form',
                    'default_host': 'form',
                    'force_miss': 'form',
                    'force_ssl': 'form',
                    'geo_headers': 'form',
                    'hash_keys': 'form',
                    'max_stale_age': 'form',
                    'name': 'form',
                    'request_condition': 'form',
                    'timer_support': 'form',
                    'xff': 'form',
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

    def delete_request_settings(
        self,
        service_id,
        version_id,
        request_settings_name,
        **kwargs
    ):
        """Delete a Request Settings object  # noqa: E501

        Removes the specified Request Settings object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_request_settings(service_id, version_id, request_settings_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            request_settings_name (str): Name for the request settings.

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
        kwargs['version_id'] = \
            version_id
        kwargs['request_settings_name'] = \
            request_settings_name
        return self.delete_request_settings_endpoint.call_with_http_info(**kwargs)

    def get_request_settings(
        self,
        service_id,
        version_id,
        request_settings_name,
        **kwargs
    ):
        """Get a Request Settings object  # noqa: E501

        Gets the specified Request Settings object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_request_settings(service_id, version_id, request_settings_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            request_settings_name (str): Name for the request settings.

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
            RequestSettingsResponse
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
        kwargs['version_id'] = \
            version_id
        kwargs['request_settings_name'] = \
            request_settings_name
        return self.get_request_settings_endpoint.call_with_http_info(**kwargs)

    def list_request_settings(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List Request Settings objects  # noqa: E501

        Returns a list of all Request Settings objects for the given service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_request_settings(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

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
            [RequestSettingsResponse]
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
        kwargs['version_id'] = \
            version_id
        return self.list_request_settings_endpoint.call_with_http_info(**kwargs)

    def update_request_settings(
        self,
        service_id,
        version_id,
        request_settings_name,
        **kwargs
    ):
        """Update a Request Settings object  # noqa: E501

        Updates the specified Request Settings object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_request_settings(service_id, version_id, request_settings_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            request_settings_name (str): Name for the request settings.

        Keyword Args:
            action (str, none_type): Allows you to terminate request handling and immediately perform an action.. [optional]
            bypass_busy_wait (int): Disable collapsed forwarding, so you don't wait for other objects to origin.. [optional]
            default_host (str, none_type): Sets the host header.. [optional]
            force_miss (int): Allows you to force a cache miss for the request. Replaces the item in the cache if the content is cacheable.. [optional]
            force_ssl (int): Forces the request use SSL (redirects a non-SSL to SSL).. [optional]
            geo_headers (int): Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers.. [optional]
            hash_keys (str, none_type): Comma separated list of varnish request object fields that should be in the hash key.. [optional]
            max_stale_age (int): How old an object is allowed to be to serve stale-if-error or stale-while-revalidate.. [optional]
            name (str): Name for the request settings.. [optional]
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]
            timer_support (int): Injects the X-Timer info into the request for viewing origin fetch durations.. [optional]
            xff (str): Short for X-Forwarded-For.. [optional]
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
            RequestSettingsResponse
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
        kwargs['version_id'] = \
            version_id
        kwargs['request_settings_name'] = \
            request_settings_name
        return self.update_request_settings_endpoint.call_with_http_info(**kwargs)

