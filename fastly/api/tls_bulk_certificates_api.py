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
from fastly.model.tls_bulk_certificate import TlsBulkCertificate
from fastly.model.tls_bulk_certificate_response import TlsBulkCertificateResponse
from fastly.model.tls_bulk_certificates_response import TlsBulkCertificatesResponse


class TlsBulkCertificatesApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.delete_bulk_tls_cert_endpoint = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/bulk/certificates/{certificate_id}',
                'operation_id': 'delete_bulk_tls_cert',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'certificate_id',
                ],
                'required': [
                    'certificate_id',
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
                    'certificate_id':
                        (str,),
                },
                'attribute_map': {
                    'certificate_id': 'certificate_id',
                },
                'location_map': {
                    'certificate_id': 'path',
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
        self.get_tls_bulk_cert_endpoint = _Endpoint(
            settings={
                'response_type': (TlsBulkCertificateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/bulk/certificates/{certificate_id}',
                'operation_id': 'get_tls_bulk_cert',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'certificate_id',
                ],
                'required': [
                    'certificate_id',
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
                    'certificate_id':
                        (str,),
                },
                'attribute_map': {
                    'certificate_id': 'certificate_id',
                },
                'location_map': {
                    'certificate_id': 'path',
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
        self.list_tls_bulk_certs_endpoint = _Endpoint(
            settings={
                'response_type': (TlsBulkCertificatesResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/bulk/certificates',
                'operation_id': 'list_tls_bulk_certs',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_tls_domain_id',
                    'page_number',
                    'page_size',
                    'sort',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'sort',
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
                    ('sort',): {

                        "asc": "created_at",
                        "desc": "-created_at"
                    },
                },
                'openapi_types': {
                    'filter_tls_domain_id':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'filter_tls_domain_id': 'filter[tls_domain.id]',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'sort': 'sort',
                },
                'location_map': {
                    'filter_tls_domain_id': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                    'sort': 'query',
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
        self.update_bulk_tls_cert_endpoint = _Endpoint(
            settings={
                'response_type': (TlsBulkCertificateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/bulk/certificates/{certificate_id}',
                'operation_id': 'update_bulk_tls_cert',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'certificate_id',
                    'tls_bulk_certificate',
                ],
                'required': [
                    'certificate_id',
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
                    'certificate_id':
                        (str,),
                    'tls_bulk_certificate':
                        (TlsBulkCertificate,),
                },
                'attribute_map': {
                    'certificate_id': 'certificate_id',
                },
                'location_map': {
                    'certificate_id': 'path',
                    'tls_bulk_certificate': 'body',
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
        self.upload_tls_bulk_cert_endpoint = _Endpoint(
            settings={
                'response_type': (TlsBulkCertificateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/bulk/certificates',
                'operation_id': 'upload_tls_bulk_cert',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'tls_bulk_certificate',
                ],
                'required': [],
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
                    'tls_bulk_certificate':
                        (TlsBulkCertificate,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'tls_bulk_certificate': 'body',
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

    def delete_bulk_tls_cert(
        self,
        certificate_id,
        **kwargs
    ):
        """Delete a certificate  # noqa: E501

        Destroy a certificate. This disables TLS for all domains listed as SAN entries.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_bulk_tls_cert(certificate_id, async_req=True)
        >>> result = thread.get()

        Args:
            certificate_id (str): Alphanumeric string identifying a TLS bulk certificate.

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
        kwargs['certificate_id'] = \
            certificate_id
        return self.delete_bulk_tls_cert_endpoint.call_with_http_info(**kwargs)

    def get_tls_bulk_cert(
        self,
        certificate_id,
        **kwargs
    ):
        """Get a certificate  # noqa: E501

        Retrieve a single certificate.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_tls_bulk_cert(certificate_id, async_req=True)
        >>> result = thread.get()

        Args:
            certificate_id (str): Alphanumeric string identifying a TLS bulk certificate.

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
            TlsBulkCertificateResponse
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
        kwargs['certificate_id'] = \
            certificate_id
        return self.get_tls_bulk_cert_endpoint.call_with_http_info(**kwargs)

    def list_tls_bulk_certs(
        self,
        **kwargs
    ):
        """List certificates  # noqa: E501

        List all certificates.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tls_bulk_certs(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_tls_domain_id (str): Filter certificates by their matching, fully-qualified domain name.. [optional]
            page_number (int): Current page.. [optional]
            page_size (int): Number of records per page.. [optional] if omitted the server will use the default value of 20
            sort (str): The order in which to list the results by creation date.. [optional] if omitted the server will use the default value of "created_at"
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
            TlsBulkCertificatesResponse
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
        return self.list_tls_bulk_certs_endpoint.call_with_http_info(**kwargs)

    def update_bulk_tls_cert(
        self,
        certificate_id,
        **kwargs
    ):
        """Update a certificate  # noqa: E501

        Replace a certificate with a newly reissued certificate. By using this endpoint, the original certificate will cease to be used for future TLS handshakes. Thus, only SAN entries that appear in the replacement certificate will become TLS enabled. Any SAN entries that are missing in the replacement certificate will become disabled.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_bulk_tls_cert(certificate_id, async_req=True)
        >>> result = thread.get()

        Args:
            certificate_id (str): Alphanumeric string identifying a TLS bulk certificate.

        Keyword Args:
            tls_bulk_certificate (TlsBulkCertificate): [optional]
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
            TlsBulkCertificateResponse
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
        kwargs['certificate_id'] = \
            certificate_id
        return self.update_bulk_tls_cert_endpoint.call_with_http_info(**kwargs)

    def upload_tls_bulk_cert(
        self,
        **kwargs
    ):
        """Upload a certificate  # noqa: E501

        Upload a new certificate. TLS domains are automatically enabled upon certificate creation. If a domain is already enabled on a previously uploaded certificate, that domain will be updated to use the new certificate for all future TLS handshake requests.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_tls_bulk_cert(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            tls_bulk_certificate (TlsBulkCertificate): [optional]
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
            TlsBulkCertificateResponse
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
        return self.upload_tls_bulk_cert_endpoint.call_with_http_info(**kwargs)

