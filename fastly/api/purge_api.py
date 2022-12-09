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
from fastly.model.purge_response import PurgeResponse


class PurgeApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.purge_all_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/purge_all',
                'operation_id': 'purge_all',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                ],
                'required': [
                    'service_id',
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
                },
                'attribute_map': {
                    'service_id': 'service_id',
                },
                'location_map': {
                    'service_id': 'path',
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
        self.purge_single_url_endpoint = _Endpoint(
            settings={
                'response_type': (PurgeResponse,),
                'auth': [
                    'url_purge'
                ],
                'endpoint_path': '/purge/{cached_url}',
                'operation_id': 'purge_single_url',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'cached_url',
                    'fastly_soft_purge',
                ],
                'required': [
                    'cached_url',
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
                    'cached_url':
                        (str,),
                    'fastly_soft_purge':
                        (int,),
                },
                'attribute_map': {
                    'cached_url': 'cached_url',
                    'fastly_soft_purge': 'fastly-soft-purge',
                },
                'location_map': {
                    'cached_url': 'path',
                    'fastly_soft_purge': 'header',
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
        self.purge_tag_endpoint = _Endpoint(
            settings={
                'response_type': (PurgeResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/purge/{surrogate_key}',
                'operation_id': 'purge_tag',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'surrogate_key',
                    'fastly_soft_purge',
                ],
                'required': [
                    'service_id',
                    'surrogate_key',
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
                    'surrogate_key':
                        (str,),
                    'fastly_soft_purge':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'surrogate_key': 'surrogate_key',
                    'fastly_soft_purge': 'fastly-soft-purge',
                },
                'location_map': {
                    'service_id': 'path',
                    'surrogate_key': 'path',
                    'fastly_soft_purge': 'header',
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

    def purge_all(
        self,
        service_id,
        **kwargs
    ):
        """Purge everything from a service  # noqa: E501

        Instant Purge everything from a service.  Purge-all requests cannot be done in soft mode and will always immediately invalidate all cached content associated with the service. To do a soft-purge-all, consider applying a constant [surrogate key](https://docs.fastly.com/en/guides/getting-started-with-surrogate-keys) tag (e.g., `\"all\"`) to all objects.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.purge_all(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.

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
        return self.purge_all_endpoint.call_with_http_info(**kwargs)

    def purge_single_url(
        self,
        cached_url,
        **kwargs
    ):
        """Purge a URL  # noqa: E501

        Instant Purge an individual URL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.purge_single_url(cached_url, async_req=True)
        >>> result = thread.get()

        Args:
            cached_url (str): URL of object in cache to be purged.

        Keyword Args:
            fastly_soft_purge (int): If present, this header triggers the purge to be 'soft', which marks the affected object as stale rather than making it inaccessible.  Typically set to \"1\" when used, but the value is not important.. [optional]
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
            PurgeResponse
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
        kwargs['cached_url'] = \
            cached_url
        return self.purge_single_url_endpoint.call_with_http_info(**kwargs)

    def purge_tag(
        self,
        service_id,
        surrogate_key,
        **kwargs
    ):
        """Purge by surrogate key tag  # noqa: E501

        Instant Purge a particular service of items tagged with a Surrogate Key. Only one surrogate key can be purged at a time. Multiple keys can be purged using a batch surrogate key purge request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.purge_tag(service_id, surrogate_key, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            surrogate_key (str): Surrogate keys are used to efficiently purge content from cache. Instead of purging your entire site or individual URLs, you can tag related assets (like all images and descriptions associated with a single product) with surrogate keys, and these grouped URLs can be purged in a single request.

        Keyword Args:
            fastly_soft_purge (int): If present, this header triggers the purge to be 'soft', which marks the affected object as stale rather than making it inaccessible.  Typically set to \"1\" when used, but the value is not important.. [optional]
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
            PurgeResponse
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
        kwargs['surrogate_key'] = \
            surrogate_key
        return self.purge_tag_endpoint.call_with_http_info(**kwargs)

