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
from fastly.model.billing_estimate_response import BillingEstimateResponse
from fastly.model.billing_response import BillingResponse


class BillingApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_invoice_endpoint = _Endpoint(
            settings={
                'response_type': (BillingResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/billing/v2/year/{year}/month/{month}',
                'operation_id': 'get_invoice',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'month',
                    'year',
                ],
                'required': [
                    'month',
                    'year',
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
                    'month':
                        (str,),
                    'year':
                        (str,),
                },
                'attribute_map': {
                    'month': 'month',
                    'year': 'year',
                },
                'location_map': {
                    'month': 'path',
                    'year': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/csv',
                    'application/pdf'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_invoice_by_id_endpoint = _Endpoint(
            settings={
                'response_type': (BillingResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/billing/v2/account_customers/{customer_id}/invoices/{invoice_id}',
                'operation_id': 'get_invoice_by_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'invoice_id',
                ],
                'required': [
                    'customer_id',
                    'invoice_id',
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
                    'customer_id':
                        (str,),
                    'invoice_id':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                    'invoice_id': 'invoice_id',
                },
                'location_map': {
                    'customer_id': 'path',
                    'invoice_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'text/csv',
                    'application/pdf'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_invoice_mtd_endpoint = _Endpoint(
            settings={
                'response_type': (BillingEstimateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/billing/v2/account_customers/{customer_id}/mtd_invoice',
                'operation_id': 'get_invoice_mtd',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'customer_id',
                    'month',
                    'year',
                ],
                'required': [
                    'customer_id',
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
                    'customer_id':
                        (str,),
                    'month':
                        (str,),
                    'year':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                    'month': 'month',
                    'year': 'year',
                },
                'location_map': {
                    'customer_id': 'path',
                    'month': 'query',
                    'year': 'query',
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

    def get_invoice(
        self,
        month,
        year,
        **kwargs
    ):
        """Get an invoice  # noqa: E501

        Get the invoice for a given year and month. Can be any month from when the Customer was created to the current month.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice(month, year, async_req=True)
        >>> result = thread.get()

        Args:
            month (str): 2-digit month.
            year (str): 4-digit year.

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
            BillingResponse
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
        kwargs['month'] = \
            month
        kwargs['year'] = \
            year
        return self.get_invoice_endpoint.call_with_http_info(**kwargs)

    def get_invoice_by_id(
        self,
        customer_id,
        invoice_id,
        **kwargs
    ):
        """Get an invoice  # noqa: E501

        Get the invoice for the given invoice_id.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice_by_id(customer_id, invoice_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.
            invoice_id (str): Alphanumeric string identifying the invoice.

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
            BillingResponse
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
        kwargs['customer_id'] = \
            customer_id
        kwargs['invoice_id'] = \
            invoice_id
        return self.get_invoice_by_id_endpoint.call_with_http_info(**kwargs)

    def get_invoice_mtd(
        self,
        customer_id,
        **kwargs
    ):
        """Get month-to-date billing estimate  # noqa: E501

        Get the current month-to-date estimate. This endpoint has two different responses. Under normal circumstances, it generally takes less than 5 seconds to generate but in certain cases can take up to 60 seconds. Once generated the month-to-date estimate is cached for 4 hours, and is available the next request will return the JSON representation of the month-to-date estimate. While a report is being generated in the background, this endpoint will return a `202 Accepted` response. The full format of which can be found in detail in our [billing calculation guide](https://docs.fastly.com/en/guides/how-we-calculate-your-bill). There are certain accounts for which we are unable to generate a month-to-date estimate. For example, accounts who have parent-pay are unable to generate an MTD estimate. The parent accounts are able to generate a month-to-date estimate but that estimate will not include the child accounts amounts at this time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_invoice_mtd(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.

        Keyword Args:
            month (str): 2-digit month.. [optional]
            year (str): 4-digit year.. [optional]
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
            BillingEstimateResponse
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
        kwargs['customer_id'] = \
            customer_id
        return self.get_invoice_mtd_endpoint.call_with_http_info(**kwargs)

