"""
    Fastly API

    Via the Fastly API you can perform any of the operations that are possible within the management console,  including creating services, domains, and backends, configuring rules or uploading your own application code, as well as account operations such as user administration and billing reports. The API is organized into collections of endpoints that allow manipulation of objects related to Fastly services and accounts. For the most accurate and up-to-date API reference content, visit our [Developer Hub](https://www.fastly.com/documentation/reference/api/)   # noqa: E501

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
from fastly.model.header_response import HeaderResponse
from fastly.model.inline_response200 import InlineResponse200


class HeaderApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_header_object_endpoint = _Endpoint(
            settings={
                'response_type': (HeaderResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/header',
                'operation_id': 'create_header_object',
                'http_method': 'POST',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'action',
                    'cache_condition',
                    'dst',
                    'name',
                    'regex',
                    'request_condition',
                    'response_condition',
                    'src',
                    'substitution',
                    'type',
                    'ignore_if_set',
                    'priority',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'cache_condition',
                    'regex',
                    'request_condition',
                    'response_condition',
                    'src',
                    'substitution',
                ],
                'enum': [
                    'action',
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('action',): {

                        "SET": "set",
                        "APPEND": "append",
                        "DELETE": "delete",
                        "REGEX": "regex",
                        "REGEX_REPEAT": "regex_repeat"
                    },
                    ('type',): {

                        "REQUEST": "request",
                        "CACHE": "cache",
                        "RESPONSE": "response"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'action':
                        (str,),
                    'cache_condition':
                        (str, none_type,),
                    'dst':
                        (str,),
                    'name':
                        (str,),
                    'regex':
                        (str, none_type,),
                    'request_condition':
                        (str, none_type,),
                    'response_condition':
                        (str, none_type,),
                    'src':
                        (str, none_type,),
                    'substitution':
                        (str, none_type,),
                    'type':
                        (str,),
                    'ignore_if_set':
                        (str,),
                    'priority':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'action': 'action',
                    'cache_condition': 'cache_condition',
                    'dst': 'dst',
                    'name': 'name',
                    'regex': 'regex',
                    'request_condition': 'request_condition',
                    'response_condition': 'response_condition',
                    'src': 'src',
                    'substitution': 'substitution',
                    'type': 'type',
                    'ignore_if_set': 'ignore_if_set',
                    'priority': 'priority',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'action': 'form',
                    'cache_condition': 'form',
                    'dst': 'form',
                    'name': 'form',
                    'regex': 'form',
                    'request_condition': 'form',
                    'response_condition': 'form',
                    'src': 'form',
                    'substitution': 'form',
                    'type': 'form',
                    'ignore_if_set': 'form',
                    'priority': 'form',
                },
                'path_params_allow_reserved_map': {
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
        self.delete_header_object_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/header/{header_name}',
                'operation_id': 'delete_header_object',
                'http_method': 'DELETE',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'header_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'header_name',
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
                    'header_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'header_name': 'header_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'header_name': 'path',
                },
                'path_params_allow_reserved_map': {
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
        self.get_header_object_endpoint = _Endpoint(
            settings={
                'response_type': (HeaderResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/header/{header_name}',
                'operation_id': 'get_header_object',
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
                    'service_id',
                    'version_id',
                    'header_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'header_name',
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
                    'header_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'header_name': 'header_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'header_name': 'path',
                },
                'path_params_allow_reserved_map': {
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
        self.list_header_objects_endpoint = _Endpoint(
            settings={
                'response_type': ([HeaderResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/header',
                'operation_id': 'list_header_objects',
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
                'path_params_allow_reserved_map': {
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
        self.update_header_object_endpoint = _Endpoint(
            settings={
                'response_type': (HeaderResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/header/{header_name}',
                'operation_id': 'update_header_object',
                'http_method': 'PUT',
                'servers': [
                    {
                        'url': "https://api.fastly.com",
                        'description': "No description provided",
                    },
                ]
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'header_name',
                    'action',
                    'cache_condition',
                    'dst',
                    'name',
                    'regex',
                    'request_condition',
                    'response_condition',
                    'src',
                    'substitution',
                    'type',
                    'ignore_if_set',
                    'priority',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'header_name',
                ],
                'nullable': [
                    'cache_condition',
                    'regex',
                    'request_condition',
                    'response_condition',
                    'src',
                    'substitution',
                ],
                'enum': [
                    'action',
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('action',): {

                        "SET": "set",
                        "APPEND": "append",
                        "DELETE": "delete",
                        "REGEX": "regex",
                        "REGEX_REPEAT": "regex_repeat"
                    },
                    ('type',): {

                        "REQUEST": "request",
                        "CACHE": "cache",
                        "RESPONSE": "response"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'version_id':
                        (int,),
                    'header_name':
                        (str,),
                    'action':
                        (str,),
                    'cache_condition':
                        (str, none_type,),
                    'dst':
                        (str,),
                    'name':
                        (str,),
                    'regex':
                        (str, none_type,),
                    'request_condition':
                        (str, none_type,),
                    'response_condition':
                        (str, none_type,),
                    'src':
                        (str, none_type,),
                    'substitution':
                        (str, none_type,),
                    'type':
                        (str,),
                    'ignore_if_set':
                        (str,),
                    'priority':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'header_name': 'header_name',
                    'action': 'action',
                    'cache_condition': 'cache_condition',
                    'dst': 'dst',
                    'name': 'name',
                    'regex': 'regex',
                    'request_condition': 'request_condition',
                    'response_condition': 'response_condition',
                    'src': 'src',
                    'substitution': 'substitution',
                    'type': 'type',
                    'ignore_if_set': 'ignore_if_set',
                    'priority': 'priority',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'header_name': 'path',
                    'action': 'form',
                    'cache_condition': 'form',
                    'dst': 'form',
                    'name': 'form',
                    'regex': 'form',
                    'request_condition': 'form',
                    'response_condition': 'form',
                    'src': 'form',
                    'substitution': 'form',
                    'type': 'form',
                    'ignore_if_set': 'form',
                    'priority': 'form',
                },
                'path_params_allow_reserved_map': {
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

    def create_header_object(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a Header object  # noqa: E501

        Creates a new Header object.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_header_object(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            action (str): Accepts a string value.. [optional]
            cache_condition (str, none_type): Name of the cache condition controlling when this configuration applies.. [optional]
            dst (str): Header to set.. [optional]
            name (str): A handle to refer to this Header object.. [optional]
            regex (str, none_type): Regular expression to use. Only applies to `regex` and `regex_repeat` actions.. [optional]
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]
            response_condition (str, none_type): Optional name of a response condition to apply.. [optional]
            src (str, none_type): Variable to be used as a source for the header content. Does not apply to `delete` action.. [optional]
            substitution (str, none_type): Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions.. [optional]
            type (str): Accepts a string value.. [optional]
            ignore_if_set (str): Don't add the header if it is added already. Only applies to 'set' action. Numerical value (\\\"0\\\" = false, \\\"1\\\" = true). [optional]
            priority (str): Priority determines execution order. Lower numbers execute first.. [optional] if omitted the server will use the default value of "100"
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
            HeaderResponse
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
        return self.create_header_object_endpoint.call_with_http_info(**kwargs)

    def delete_header_object(
        self,
        service_id,
        version_id,
        header_name,
        **kwargs
    ):
        """Delete a Header object  # noqa: E501

        Deletes a Header object by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_header_object(service_id, version_id, header_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            header_name (str): A handle to refer to this Header object.

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
        kwargs['header_name'] = \
            header_name
        return self.delete_header_object_endpoint.call_with_http_info(**kwargs)

    def get_header_object(
        self,
        service_id,
        version_id,
        header_name,
        **kwargs
    ):
        """Get a Header object  # noqa: E501

        Retrieves a Header object by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_header_object(service_id, version_id, header_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            header_name (str): A handle to refer to this Header object.

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
            HeaderResponse
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
        kwargs['header_name'] = \
            header_name
        return self.get_header_object_endpoint.call_with_http_info(**kwargs)

    def list_header_objects(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List Header objects  # noqa: E501

        Retrieves all Header objects for a particular Version of a Service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_header_objects(service_id, version_id, async_req=True)
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
            [HeaderResponse]
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
        return self.list_header_objects_endpoint.call_with_http_info(**kwargs)

    def update_header_object(
        self,
        service_id,
        version_id,
        header_name,
        **kwargs
    ):
        """Update a Header object  # noqa: E501

        Modifies an existing Header object by name.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_header_object(service_id, version_id, header_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            header_name (str): A handle to refer to this Header object.

        Keyword Args:
            action (str): Accepts a string value.. [optional]
            cache_condition (str, none_type): Name of the cache condition controlling when this configuration applies.. [optional]
            dst (str): Header to set.. [optional]
            name (str): A handle to refer to this Header object.. [optional]
            regex (str, none_type): Regular expression to use. Only applies to `regex` and `regex_repeat` actions.. [optional]
            request_condition (str, none_type): Condition which, if met, will select this configuration during a request. Optional.. [optional]
            response_condition (str, none_type): Optional name of a response condition to apply.. [optional]
            src (str, none_type): Variable to be used as a source for the header content. Does not apply to `delete` action.. [optional]
            substitution (str, none_type): Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions.. [optional]
            type (str): Accepts a string value.. [optional]
            ignore_if_set (str): Don't add the header if it is added already. Only applies to 'set' action. Numerical value (\\\"0\\\" = false, \\\"1\\\" = true). [optional]
            priority (str): Priority determines execution order. Lower numbers execute first.. [optional] if omitted the server will use the default value of "100"
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
            HeaderResponse
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
        kwargs['header_name'] = \
            header_name
        return self.update_header_object_endpoint.call_with_http_info(**kwargs)

