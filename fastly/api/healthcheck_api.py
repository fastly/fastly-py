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
from fastly.model.healthcheck_response import HealthcheckResponse
from fastly.model.inline_response200 import InlineResponse200


class HealthcheckApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_healthcheck_endpoint = _Endpoint(
            settings={
                'response_type': (HealthcheckResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/healthcheck',
                'operation_id': 'create_healthcheck',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'check_interval',
                    'comment',
                    'expected_response',
                    'headers',
                    'host',
                    'http_version',
                    'initial',
                    'method',
                    'name',
                    'path',
                    'threshold',
                    'timeout',
                    'window',
                ],
                'required': [
                    'service_id',
                    'version_id',
                ],
                'nullable': [
                    'comment',
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
                    'check_interval':
                        (int,),
                    'comment':
                        (str, none_type,),
                    'expected_response':
                        (int,),
                    'headers':
                        ([str],),
                    'host':
                        (str,),
                    'http_version':
                        (str,),
                    'initial':
                        (int,),
                    'method':
                        (str,),
                    'name':
                        (str,),
                    'path':
                        (str,),
                    'threshold':
                        (int,),
                    'timeout':
                        (int,),
                    'window':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'check_interval': 'check_interval',
                    'comment': 'comment',
                    'expected_response': 'expected_response',
                    'headers': 'headers',
                    'host': 'host',
                    'http_version': 'http_version',
                    'initial': 'initial',
                    'method': 'method',
                    'name': 'name',
                    'path': 'path',
                    'threshold': 'threshold',
                    'timeout': 'timeout',
                    'window': 'window',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'check_interval': 'form',
                    'comment': 'form',
                    'expected_response': 'form',
                    'headers': 'form',
                    'host': 'form',
                    'http_version': 'form',
                    'initial': 'form',
                    'method': 'form',
                    'name': 'form',
                    'path': 'form',
                    'threshold': 'form',
                    'timeout': 'form',
                    'window': 'form',
                },
                'collection_format_map': {
                    'headers': 'csv',
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
        self.delete_healthcheck_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name}',
                'operation_id': 'delete_healthcheck',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'healthcheck_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'healthcheck_name',
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
                    'healthcheck_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'healthcheck_name': 'healthcheck_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'healthcheck_name': 'path',
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
        self.get_healthcheck_endpoint = _Endpoint(
            settings={
                'response_type': (HealthcheckResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name}',
                'operation_id': 'get_healthcheck',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'healthcheck_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'healthcheck_name',
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
                    'healthcheck_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'healthcheck_name': 'healthcheck_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'healthcheck_name': 'path',
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
        self.list_healthchecks_endpoint = _Endpoint(
            settings={
                'response_type': ([HealthcheckResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/healthcheck',
                'operation_id': 'list_healthchecks',
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
        self.update_healthcheck_endpoint = _Endpoint(
            settings={
                'response_type': (HealthcheckResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name}',
                'operation_id': 'update_healthcheck',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'healthcheck_name',
                    'check_interval',
                    'comment',
                    'expected_response',
                    'headers',
                    'host',
                    'http_version',
                    'initial',
                    'method',
                    'name',
                    'path',
                    'threshold',
                    'timeout',
                    'window',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'healthcheck_name',
                ],
                'nullable': [
                    'comment',
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
                    'healthcheck_name':
                        (str,),
                    'check_interval':
                        (int,),
                    'comment':
                        (str, none_type,),
                    'expected_response':
                        (int,),
                    'headers':
                        ([str],),
                    'host':
                        (str,),
                    'http_version':
                        (str,),
                    'initial':
                        (int,),
                    'method':
                        (str,),
                    'name':
                        (str,),
                    'path':
                        (str,),
                    'threshold':
                        (int,),
                    'timeout':
                        (int,),
                    'window':
                        (int,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'healthcheck_name': 'healthcheck_name',
                    'check_interval': 'check_interval',
                    'comment': 'comment',
                    'expected_response': 'expected_response',
                    'headers': 'headers',
                    'host': 'host',
                    'http_version': 'http_version',
                    'initial': 'initial',
                    'method': 'method',
                    'name': 'name',
                    'path': 'path',
                    'threshold': 'threshold',
                    'timeout': 'timeout',
                    'window': 'window',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'healthcheck_name': 'path',
                    'check_interval': 'form',
                    'comment': 'form',
                    'expected_response': 'form',
                    'headers': 'form',
                    'host': 'form',
                    'http_version': 'form',
                    'initial': 'form',
                    'method': 'form',
                    'name': 'form',
                    'path': 'form',
                    'threshold': 'form',
                    'timeout': 'form',
                    'window': 'form',
                },
                'collection_format_map': {
                    'headers': 'csv',
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

    def create_healthcheck(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Create a health check  # noqa: E501

        Create a health check for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_healthcheck(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            check_interval (int): How often to run the health check in milliseconds.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            expected_response (int): The status code expected from the host.. [optional]
            headers ([str]): Array of custom headers that will be added to the health check probes.. [optional]
            host (str): Which host to check.. [optional]
            http_version (str): Whether to use version 1.0 or 1.1 HTTP.. [optional]
            initial (int): When loading a config, the initial number of probes to be seen as OK.. [optional]
            method (str): Which HTTP method to use.. [optional]
            name (str): The name of the health check.. [optional]
            path (str): The path to check.. [optional]
            threshold (int): How many health checks must succeed to be considered healthy.. [optional]
            timeout (int): Timeout in milliseconds.. [optional]
            window (int): The number of most recent health check queries to keep for this health check.. [optional]
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
            HealthcheckResponse
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
        return self.create_healthcheck_endpoint.call_with_http_info(**kwargs)

    def delete_healthcheck(
        self,
        service_id,
        version_id,
        healthcheck_name,
        **kwargs
    ):
        """Delete a health check  # noqa: E501

        Delete the health check for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_healthcheck(service_id, version_id, healthcheck_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            healthcheck_name (str): The name of the health check.

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
        kwargs['healthcheck_name'] = \
            healthcheck_name
        return self.delete_healthcheck_endpoint.call_with_http_info(**kwargs)

    def get_healthcheck(
        self,
        service_id,
        version_id,
        healthcheck_name,
        **kwargs
    ):
        """Get a health check  # noqa: E501

        Get the health check for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_healthcheck(service_id, version_id, healthcheck_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            healthcheck_name (str): The name of the health check.

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
            HealthcheckResponse
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
        kwargs['healthcheck_name'] = \
            healthcheck_name
        return self.get_healthcheck_endpoint.call_with_http_info(**kwargs)

    def list_healthchecks(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List health checks  # noqa: E501

        List all of the health checks for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_healthchecks(service_id, version_id, async_req=True)
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
            [HealthcheckResponse]
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
        return self.list_healthchecks_endpoint.call_with_http_info(**kwargs)

    def update_healthcheck(
        self,
        service_id,
        version_id,
        healthcheck_name,
        **kwargs
    ):
        """Update a health check  # noqa: E501

        Update the health check for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_healthcheck(service_id, version_id, healthcheck_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            healthcheck_name (str): The name of the health check.

        Keyword Args:
            check_interval (int): How often to run the health check in milliseconds.. [optional]
            comment (str, none_type): A freeform descriptive note.. [optional]
            expected_response (int): The status code expected from the host.. [optional]
            headers ([str]): Array of custom headers that will be added to the health check probes.. [optional]
            host (str): Which host to check.. [optional]
            http_version (str): Whether to use version 1.0 or 1.1 HTTP.. [optional]
            initial (int): When loading a config, the initial number of probes to be seen as OK.. [optional]
            method (str): Which HTTP method to use.. [optional]
            name (str): The name of the health check.. [optional]
            path (str): The path to check.. [optional]
            threshold (int): How many health checks must succeed to be considered healthy.. [optional]
            timeout (int): Timeout in milliseconds.. [optional]
            window (int): The number of most recent health check queries to keep for this health check.. [optional]
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
            HealthcheckResponse
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
        kwargs['healthcheck_name'] = \
            healthcheck_name
        return self.update_healthcheck_endpoint.call_with_http_info(**kwargs)

