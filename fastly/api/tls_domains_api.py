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
from fastly.model.tls_domains_response import TlsDomainsResponse


class TlsDomainsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.list_tls_domains_endpoint = _Endpoint(
            settings={
                'response_type': (TlsDomainsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/tls/domains',
                'operation_id': 'list_tls_domains',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'filter_in_use',
                    'filter_tls_certificates_id',
                    'filter_tls_subscriptions_id',
                    'include',
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
                    'filter_in_use':
                        (str,),
                    'filter_tls_certificates_id':
                        (str,),
                    'filter_tls_subscriptions_id':
                        (str,),
                    'include':
                        (str,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'filter_in_use': 'filter[in_use]',
                    'filter_tls_certificates_id': 'filter[tls_certificates.id]',
                    'filter_tls_subscriptions_id': 'filter[tls_subscriptions.id]',
                    'include': 'include',
                    'page_number': 'page[number]',
                    'page_size': 'page[size]',
                    'sort': 'sort',
                },
                'location_map': {
                    'filter_in_use': 'query',
                    'filter_tls_certificates_id': 'query',
                    'filter_tls_subscriptions_id': 'query',
                    'include': 'query',
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

    def list_tls_domains(
        self,
        **kwargs
    ):
        """List TLS domains  # noqa: E501

        List all TLS domains.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_tls_domains(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            filter_in_use (str): Optional. Limit the returned domains to those currently using Fastly to terminate TLS with SNI (that is, domains considered \"in use\") Permitted values: true, false.. [optional]
            filter_tls_certificates_id (str): Optional. Limit the returned domains to those listed in the given TLS certificate's SAN list.. [optional]
            filter_tls_subscriptions_id (str): Optional. Limit the returned domains to those for a given TLS subscription.. [optional]
            include (str): Include related objects. Optional, comma-separated values. Permitted values: `tls_activations`, `tls_certificates`, `tls_subscriptions`, `tls_subscriptions.tls_authorizations`, and `tls_authorizations.globalsign_email_challenge`. . [optional]
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
            TlsDomainsResponse
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
        return self.list_tls_domains_endpoint.call_with_http_info(**kwargs)

