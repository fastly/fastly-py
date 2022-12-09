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
from fastly.model.apex_redirect import ApexRedirect
from fastly.model.inline_response200 import InlineResponse200


class ApexRedirectApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_apex_redirect_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/apex-redirects/{apex_redirect_id}',
                'operation_id': 'delete_apex_redirect',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'apex_redirect_id',
                ],
                'required': [
                    'apex_redirect_id',
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
                    'apex_redirect_id':
                        (str,),
                },
                'attribute_map': {
                    'apex_redirect_id': 'apex_redirect_id',
                },
                'location_map': {
                    'apex_redirect_id': 'path',
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
        self.get_apex_redirect_endpoint = _Endpoint(
            settings={
                'response_type': (ApexRedirect,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/apex-redirects/{apex_redirect_id}',
                'operation_id': 'get_apex_redirect',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'apex_redirect_id',
                ],
                'required': [
                    'apex_redirect_id',
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
                    'apex_redirect_id':
                        (str,),
                },
                'attribute_map': {
                    'apex_redirect_id': 'apex_redirect_id',
                },
                'location_map': {
                    'apex_redirect_id': 'path',
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
        self.list_apex_redirects_endpoint = _Endpoint(
            settings={
                'response_type': ([ApexRedirect],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/apex-redirects',
                'operation_id': 'list_apex_redirects',
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
        self.update_apex_redirect_endpoint = _Endpoint(
            settings={
                'response_type': (ApexRedirect,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/apex-redirects/{apex_redirect_id}',
                'operation_id': 'update_apex_redirect',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'apex_redirect_id',
                    'service_id',
                    'version',
                    'created_at',
                    'deleted_at',
                    'updated_at',
                    'status_code',
                    'domains',
                    'feature_revision',
                ],
                'required': [
                    'apex_redirect_id',
                ],
                'nullable': [
                    'created_at',
                    'deleted_at',
                    'updated_at',
                ],
                'enum': [
                    'status_code',
                ],
                'validation': [
                    'domains',
                    'feature_revision',
                ]
            },
            root_map={
                'validations': {
                    ('domains',): {

                        'min_items': 1,
                    },
                    ('feature_revision',): {

                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('status_code',): {

                        "301": 301,
                        "302": 302,
                        "307": 307,
                        "308": 308
                    },
                },
                'openapi_types': {
                    'apex_redirect_id':
                        (str,),
                    'service_id':
                        (str,),
                    'version':
                        (int,),
                    'created_at':
                        (datetime, none_type,),
                    'deleted_at':
                        (datetime, none_type,),
                    'updated_at':
                        (datetime, none_type,),
                    'status_code':
                        (int,),
                    'domains':
                        ([str],),
                    'feature_revision':
                        (int,),
                },
                'attribute_map': {
                    'apex_redirect_id': 'apex_redirect_id',
                    'service_id': 'service_id',
                    'version': 'version',
                    'created_at': 'created_at',
                    'deleted_at': 'deleted_at',
                    'updated_at': 'updated_at',
                    'status_code': 'status_code',
                    'domains': 'domains',
                    'feature_revision': 'feature_revision',
                },
                'location_map': {
                    'apex_redirect_id': 'path',
                    'service_id': 'form',
                    'version': 'form',
                    'created_at': 'form',
                    'deleted_at': 'form',
                    'updated_at': 'form',
                    'status_code': 'form',
                    'domains': 'form',
                    'feature_revision': 'form',
                },
                'collection_format_map': {
                    'domains': 'csv',
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

    def delete_apex_redirect(
        self,
        apex_redirect_id,
        **kwargs
    ):
        """Delete an apex redirect  # noqa: E501

        Delete an apex redirect by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_apex_redirect(apex_redirect_id, async_req=True)
        >>> result = thread.get()

        Args:
            apex_redirect_id (str):

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
        kwargs['apex_redirect_id'] = \
            apex_redirect_id
        return self.delete_apex_redirect_endpoint.call_with_http_info(**kwargs)

    def get_apex_redirect(
        self,
        apex_redirect_id,
        **kwargs
    ):
        """Get an apex redirect  # noqa: E501

        Get an apex redirect by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_apex_redirect(apex_redirect_id, async_req=True)
        >>> result = thread.get()

        Args:
            apex_redirect_id (str):

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
            ApexRedirect
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
        kwargs['apex_redirect_id'] = \
            apex_redirect_id
        return self.get_apex_redirect_endpoint.call_with_http_info(**kwargs)

    def list_apex_redirects(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List apex redirects  # noqa: E501

        List all apex redirects for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_apex_redirects(service_id, version_id, async_req=True)
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
            [ApexRedirect]
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
        return self.list_apex_redirects_endpoint.call_with_http_info(**kwargs)

    def update_apex_redirect(
        self,
        apex_redirect_id,
        **kwargs
    ):
        """Update an apex redirect  # noqa: E501

        Update an apex redirect by its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_apex_redirect(apex_redirect_id, async_req=True)
        >>> result = thread.get()

        Args:
            apex_redirect_id (str):

        Keyword Args:
            service_id (str): [optional]
            version (int): [optional]
            created_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            deleted_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            updated_at (datetime, none_type): Date and time in ISO 8601 format.. [optional]
            status_code (int): HTTP status code used to redirect the client.. [optional]
            domains ([str]): Array of apex domains that should redirect to their WWW subdomain.. [optional]
            feature_revision (int): Revision number of the apex redirect feature implementation. Defaults to the most recent revision.. [optional]
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
            ApexRedirect
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
        kwargs['apex_redirect_id'] = \
            apex_redirect_id
        return self.update_apex_redirect_endpoint.call_with_http_info(**kwargs)

