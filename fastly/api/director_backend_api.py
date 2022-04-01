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
from fastly.model.director_backend import DirectorBackend
from fastly.model.inline_response200 import InlineResponse200


class DirectorBackendApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_director_backend_endpoint = _Endpoint(
            settings={
                'response_type': (DirectorBackend,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/director/{director_name}/backend/{backend_name}',
                'operation_id': 'create_director_backend',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'director_name',
                    'service_id',
                    'version_id',
                    'backend_name',
                ],
                'required': [
                    'director_name',
                    'service_id',
                    'version_id',
                    'backend_name',
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
                    'director_name':
                        (str,),
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'backend_name':
                        (str,),
                },
                'attribute_map': {
                    'director_name': 'director_name',
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'backend_name': 'backend_name',
                },
                'location_map': {
                    'director_name': 'path',
                    'service_id': 'path',
                    'version_id': 'path',
                    'backend_name': 'path',
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
        self.delete_director_backend_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/director/{director_name}/backend/{backend_name}',
                'operation_id': 'delete_director_backend',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'director_name',
                    'service_id',
                    'version_id',
                    'backend_name',
                ],
                'required': [
                    'director_name',
                    'service_id',
                    'version_id',
                    'backend_name',
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
                    'director_name':
                        (str,),
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'backend_name':
                        (str,),
                },
                'attribute_map': {
                    'director_name': 'director_name',
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'backend_name': 'backend_name',
                },
                'location_map': {
                    'director_name': 'path',
                    'service_id': 'path',
                    'version_id': 'path',
                    'backend_name': 'path',
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
        self.get_director_backend_endpoint = _Endpoint(
            settings={
                'response_type': (DirectorBackend,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/director/{director_name}/backend/{backend_name}',
                'operation_id': 'get_director_backend',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'director_name',
                    'service_id',
                    'version_id',
                    'backend_name',
                ],
                'required': [
                    'director_name',
                    'service_id',
                    'version_id',
                    'backend_name',
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
                    'director_name':
                        (str,),
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'backend_name':
                        (str,),
                },
                'attribute_map': {
                    'director_name': 'director_name',
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'backend_name': 'backend_name',
                },
                'location_map': {
                    'director_name': 'path',
                    'service_id': 'path',
                    'version_id': 'path',
                    'backend_name': 'path',
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

    def create_director_backend(
        self,
        director_name,
        service_id,
        version_id,
        backend_name,
        **kwargs
    ):
        """Create a director-backend relationship  # noqa: E501

        Establishes a relationship between a Backend and a Director. The Backend is then considered a member of the Director and can be used to balance traffic onto.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_director_backend(director_name, service_id, version_id, backend_name, async_req=True)
        >>> result = thread.get()

        Args:
            director_name (str): Name for the Director.
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            backend_name (str): The name of the backend.

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
            DirectorBackend
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
        kwargs['director_name'] = \
            director_name
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['backend_name'] = \
            backend_name
        return self.create_director_backend_endpoint.call_with_http_info(**kwargs)

    def delete_director_backend(
        self,
        director_name,
        service_id,
        version_id,
        backend_name,
        **kwargs
    ):
        """Delete a director-backend relationship  # noqa: E501

        Deletes the relationship between a Backend and a Director. The Backend is no longer considered a member of the Director and thus will not have traffic balanced onto it from this Director.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_director_backend(director_name, service_id, version_id, backend_name, async_req=True)
        >>> result = thread.get()

        Args:
            director_name (str): Name for the Director.
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            backend_name (str): The name of the backend.

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
        kwargs['director_name'] = \
            director_name
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['backend_name'] = \
            backend_name
        return self.delete_director_backend_endpoint.call_with_http_info(**kwargs)

    def get_director_backend(
        self,
        director_name,
        service_id,
        version_id,
        backend_name,
        **kwargs
    ):
        """Get a director-backend relationship  # noqa: E501

        Returns the relationship between a Backend and a Director. If the Backend has been associated with the Director, it returns a simple record indicating this. Otherwise, returns a 404.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_director_backend(director_name, service_id, version_id, backend_name, async_req=True)
        >>> result = thread.get()

        Args:
            director_name (str): Name for the Director.
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            backend_name (str): The name of the backend.

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
            DirectorBackend
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
        kwargs['director_name'] = \
            director_name
        kwargs['service_id'] = \
            service_id
        kwargs['version_id'] = \
            version_id
        kwargs['backend_name'] = \
            backend_name
        return self.get_director_backend_endpoint.call_with_http_info(**kwargs)

