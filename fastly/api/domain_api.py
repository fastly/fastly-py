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
from fastly.model.domain_check_response import DomainCheckResponse
from fastly.model.domain_check_response_list import DomainCheckResponseList
from fastly.model.domain_response import DomainResponse
from fastly.model.domains_response import DomainsResponse
from fastly.model.inline_response200 import InlineResponse200


class DomainApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.check_domain_endpoint = _Endpoint(
            settings={
                'response_type': (DomainCheckResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain/{domain_name}/check',
                'operation_id': 'check_domain',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'domain_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'domain_name',
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
                    'domain_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'domain_name': 'domain_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'domain_name': 'path',
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
        self.check_domains_endpoint = _Endpoint(
            settings={
                'response_type': (DomainCheckResponseList,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain/check_all',
                'operation_id': 'check_domains',
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
        self.create_domain_endpoint = _Endpoint(
            settings={
                'response_type': (DomainResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain',
                'operation_id': 'create_domain',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'comment',
                    'name',
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
                    'comment':
                        (str, none_type,),
                    'name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'comment': 'comment',
                    'name': 'name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'comment': 'form',
                    'name': 'form',
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
        self.delete_domain_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain/{domain_name}',
                'operation_id': 'delete_domain',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'domain_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'domain_name',
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
                    'domain_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'domain_name': 'domain_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'domain_name': 'path',
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
        self.get_domain_endpoint = _Endpoint(
            settings={
                'response_type': (DomainResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain/{domain_name}',
                'operation_id': 'get_domain',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'domain_name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'domain_name',
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
                    'domain_name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'domain_name': 'domain_name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'domain_name': 'path',
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
        self.list_domains_endpoint = _Endpoint(
            settings={
                'response_type': (DomainsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain',
                'operation_id': 'list_domains',
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
        self.update_domain_endpoint = _Endpoint(
            settings={
                'response_type': (DomainResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/version/{version_id}/domain/{domain_name}',
                'operation_id': 'update_domain',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'version_id',
                    'domain_name',
                    'comment',
                    'name',
                ],
                'required': [
                    'service_id',
                    'version_id',
                    'domain_name',
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
                    'domain_name':
                        (str,),
                    'comment':
                        (str, none_type,),
                    'name':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'version_id': 'version_id',
                    'domain_name': 'domain_name',
                    'comment': 'comment',
                    'name': 'name',
                },
                'location_map': {
                    'service_id': 'path',
                    'version_id': 'path',
                    'domain_name': 'path',
                    'comment': 'form',
                    'name': 'form',
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

    def check_domain(
        self,
        service_id,
        version_id,
        domain_name,
        **kwargs
    ):
        """Validate DNS configuration for a single domain on a service  # noqa: E501

        Checks the status of a specific domain's DNS record for a Service Version. Returns an array in the same format as domain/check_all.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_domain(service_id, version_id, domain_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            domain_name (str): The name of the domain or domains associated with this service.

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
            DomainCheckResponse
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
        kwargs['domain_name'] = \
            domain_name
        return self.check_domain_endpoint.call_with_http_info(**kwargs)

    def check_domains(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Validate DNS configuration for all domains on a service  # noqa: E501

        Checks the status of all domains' DNS records for a Service Version. Returns an array of 3 items for each domain; the first is the details for the domain, the second is the current CNAME of the domain, and the third is a boolean indicating whether or not it has been properly setup to use Fastly.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.check_domains(service_id, version_id, async_req=True)
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
            DomainCheckResponseList
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
        return self.check_domains_endpoint.call_with_http_info(**kwargs)

    def create_domain(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """Add a domain name to a service  # noqa: E501

        Create a domain for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_domain(service_id, version_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.

        Keyword Args:
            comment (str, none_type): A freeform descriptive note.. [optional]
            name (str): The name of the domain or domains associated with this service.. [optional]
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
            DomainResponse
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
        return self.create_domain_endpoint.call_with_http_info(**kwargs)

    def delete_domain(
        self,
        service_id,
        version_id,
        domain_name,
        **kwargs
    ):
        """Remove a domain from a service  # noqa: E501

        Delete the domain for a particular service and versions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_domain(service_id, version_id, domain_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            domain_name (str): The name of the domain or domains associated with this service.

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
        kwargs['domain_name'] = \
            domain_name
        return self.delete_domain_endpoint.call_with_http_info(**kwargs)

    def get_domain(
        self,
        service_id,
        version_id,
        domain_name,
        **kwargs
    ):
        """Describe a domain  # noqa: E501

        Get the domain for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain(service_id, version_id, domain_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            domain_name (str): The name of the domain or domains associated with this service.

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
            DomainResponse
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
        kwargs['domain_name'] = \
            domain_name
        return self.get_domain_endpoint.call_with_http_info(**kwargs)

    def list_domains(
        self,
        service_id,
        version_id,
        **kwargs
    ):
        """List domains  # noqa: E501

        List all the domains for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_domains(service_id, version_id, async_req=True)
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
            DomainsResponse
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
        return self.list_domains_endpoint.call_with_http_info(**kwargs)

    def update_domain(
        self,
        service_id,
        version_id,
        domain_name,
        **kwargs
    ):
        """Update a domain  # noqa: E501

        Update the domain for a particular service and version.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_domain(service_id, version_id, domain_name, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            version_id (int): Integer identifying a service version.
            domain_name (str): The name of the domain or domains associated with this service.

        Keyword Args:
            comment (str, none_type): A freeform descriptive note.. [optional]
            name (str): The name of the domain or domains associated with this service.. [optional]
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
            DomainResponse
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
        kwargs['domain_name'] = \
            domain_name
        return self.update_domain_endpoint.call_with_http_info(**kwargs)

