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
from fastly.model.acl_entry import AclEntry
from fastly.model.acl_entry_response import AclEntryResponse
from fastly.model.bulk_update_acl_entries_request import BulkUpdateAclEntriesRequest
from fastly.model.inline_response200 import InlineResponse200


class AclEntryApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.bulk_update_acl_entries_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/acl/{acl_id}/entries',
                'operation_id': 'bulk_update_acl_entries',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'acl_id',
                    'bulk_update_acl_entries_request',
                ],
                'required': [
                    'service_id',
                    'acl_id',
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
                    'acl_id':
                        (str,),
                    'bulk_update_acl_entries_request':
                        (BulkUpdateAclEntriesRequest,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'acl_id': 'acl_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'acl_id': 'path',
                    'bulk_update_acl_entries_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.create_acl_entry_endpoint = _Endpoint(
            settings={
                'response_type': (AclEntryResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/acl/{acl_id}/entry',
                'operation_id': 'create_acl_entry',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'acl_id',
                    'acl_entry',
                ],
                'required': [
                    'service_id',
                    'acl_id',
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
                    'acl_id':
                        (str,),
                    'acl_entry':
                        (AclEntry,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'acl_id': 'acl_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'acl_id': 'path',
                    'acl_entry': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self.delete_acl_entry_endpoint = _Endpoint(
            settings={
                'response_type': (InlineResponse200,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/acl/{acl_id}/entry/{acl_entry_id}',
                'operation_id': 'delete_acl_entry',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'acl_id',
                    'acl_entry_id',
                ],
                'required': [
                    'service_id',
                    'acl_id',
                    'acl_entry_id',
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
                    'acl_id':
                        (str,),
                    'acl_entry_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'acl_id': 'acl_id',
                    'acl_entry_id': 'acl_entry_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'acl_id': 'path',
                    'acl_entry_id': 'path',
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
        self.get_acl_entry_endpoint = _Endpoint(
            settings={
                'response_type': (AclEntryResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/acl/{acl_id}/entry/{acl_entry_id}',
                'operation_id': 'get_acl_entry',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'acl_id',
                    'acl_entry_id',
                ],
                'required': [
                    'service_id',
                    'acl_id',
                    'acl_entry_id',
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
                    'acl_id':
                        (str,),
                    'acl_entry_id':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'acl_id': 'acl_id',
                    'acl_entry_id': 'acl_entry_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'acl_id': 'path',
                    'acl_entry_id': 'path',
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
        self.list_acl_entries_endpoint = _Endpoint(
            settings={
                'response_type': ([AclEntryResponse],),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/acl/{acl_id}/entries',
                'operation_id': 'list_acl_entries',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'acl_id',
                    'page',
                    'per_page',
                    'sort',
                    'direction',
                ],
                'required': [
                    'service_id',
                    'acl_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'direction',
                ],
                'validation': [
                    'per_page',
                ]
            },
            root_map={
                'validations': {
                    ('per_page',): {

                        'inclusive_maximum': 100,
                        'inclusive_minimum': 1,
                    },
                },
                'allowed_values': {
                    ('direction',): {

                        "ASCEND": "ascend",
                        "DESCEND": "descend"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'acl_id':
                        (str,),
                    'page':
                        (int,),
                    'per_page':
                        (int,),
                    'sort':
                        (str,),
                    'direction':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'acl_id': 'acl_id',
                    'page': 'page',
                    'per_page': 'per_page',
                    'sort': 'sort',
                    'direction': 'direction',
                },
                'location_map': {
                    'service_id': 'path',
                    'acl_id': 'path',
                    'page': 'query',
                    'per_page': 'query',
                    'sort': 'query',
                    'direction': 'query',
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
        self.update_acl_entry_endpoint = _Endpoint(
            settings={
                'response_type': (AclEntryResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/service/{service_id}/acl/{acl_id}/entry/{acl_entry_id}',
                'operation_id': 'update_acl_entry',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'acl_id',
                    'acl_entry_id',
                    'acl_entry',
                ],
                'required': [
                    'service_id',
                    'acl_id',
                    'acl_entry_id',
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
                    'acl_id':
                        (str,),
                    'acl_entry_id':
                        (str,),
                    'acl_entry':
                        (AclEntry,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'acl_id': 'acl_id',
                    'acl_entry_id': 'acl_entry_id',
                },
                'location_map': {
                    'service_id': 'path',
                    'acl_id': 'path',
                    'acl_entry_id': 'path',
                    'acl_entry': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def bulk_update_acl_entries(
        self,
        service_id,
        acl_id,
        **kwargs
    ):
        """Update multiple ACL entries  # noqa: E501

        Update multiple ACL entries on the same ACL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.bulk_update_acl_entries(service_id, acl_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            acl_id (str): Alphanumeric string identifying a ACL.

        Keyword Args:
            bulk_update_acl_entries_request (BulkUpdateAclEntriesRequest): [optional]
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
        kwargs['acl_id'] = \
            acl_id
        return self.bulk_update_acl_entries_endpoint.call_with_http_info(**kwargs)

    def create_acl_entry(
        self,
        service_id,
        acl_id,
        **kwargs
    ):
        """Create an ACL entry  # noqa: E501

        Add an ACL entry to an ACL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_acl_entry(service_id, acl_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            acl_id (str): Alphanumeric string identifying a ACL.

        Keyword Args:
            acl_entry (AclEntry): [optional]
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
            AclEntryResponse
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
        kwargs['acl_id'] = \
            acl_id
        return self.create_acl_entry_endpoint.call_with_http_info(**kwargs)

    def delete_acl_entry(
        self,
        service_id,
        acl_id,
        acl_entry_id,
        **kwargs
    ):
        """Delete an ACL entry  # noqa: E501

        Delete an ACL entry from a specified ACL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_acl_entry(service_id, acl_id, acl_entry_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            acl_id (str): Alphanumeric string identifying a ACL.
            acl_entry_id (str): Alphanumeric string identifying an ACL Entry.

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
        kwargs['acl_id'] = \
            acl_id
        kwargs['acl_entry_id'] = \
            acl_entry_id
        return self.delete_acl_entry_endpoint.call_with_http_info(**kwargs)

    def get_acl_entry(
        self,
        service_id,
        acl_id,
        acl_entry_id,
        **kwargs
    ):
        """Describe an ACL entry  # noqa: E501

        Retrieve a single ACL entry.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_acl_entry(service_id, acl_id, acl_entry_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            acl_id (str): Alphanumeric string identifying a ACL.
            acl_entry_id (str): Alphanumeric string identifying an ACL Entry.

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
            AclEntryResponse
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
        kwargs['acl_id'] = \
            acl_id
        kwargs['acl_entry_id'] = \
            acl_entry_id
        return self.get_acl_entry_endpoint.call_with_http_info(**kwargs)

    def list_acl_entries(
        self,
        service_id,
        acl_id,
        **kwargs
    ):
        """List ACL entries  # noqa: E501

        List ACL entries for a specified ACL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_acl_entries(service_id, acl_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            acl_id (str): Alphanumeric string identifying a ACL.

        Keyword Args:
            page (int): Current page.. [optional]
            per_page (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            sort (str): Field on which to sort.. [optional] if omitted the server will use the default value of "created"
            direction (str): Direction in which to sort results.. [optional] if omitted the server will use the default value of "ascend"
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
            [AclEntryResponse]
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
        kwargs['acl_id'] = \
            acl_id
        return self.list_acl_entries_endpoint.call_with_http_info(**kwargs)

    def update_acl_entry(
        self,
        service_id,
        acl_id,
        acl_entry_id,
        **kwargs
    ):
        """Update an ACL entry  # noqa: E501

        Update an ACL entry for a specified ACL.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_acl_entry(service_id, acl_id, acl_entry_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            acl_id (str): Alphanumeric string identifying a ACL.
            acl_entry_id (str): Alphanumeric string identifying an ACL Entry.

        Keyword Args:
            acl_entry (AclEntry): [optional]
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
            AclEntryResponse
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
        kwargs['acl_id'] = \
            acl_id
        kwargs['acl_entry_id'] = \
            acl_entry_id
        return self.update_acl_entry_endpoint.call_with_http_info(**kwargs)

