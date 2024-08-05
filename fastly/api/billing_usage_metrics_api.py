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
from fastly.model.error import Error
from fastly.model.serviceusagemetrics import Serviceusagemetrics
from fastly.model.serviceusagetypes import Serviceusagetypes


class BillingUsageMetricsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_service_level_usage_endpoint = _Endpoint(
            settings={
                'response_type': (Serviceusagemetrics,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/billing/v2/account_customers/{customer_id}/service-usage-metrics',
                'operation_id': 'get_service_level_usage',
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
                    'customer_id',
                    'product_id',
                    'usage_type_name',
                    'time_granularity',
                    'start_date',
                    'end_date',
                    'start_month',
                    'end_month',
                    'limit',
                    'cursor',
                ],
                'required': [
                    'customer_id',
                    'product_id',
                    'usage_type_name',
                    'time_granularity',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'time_granularity',
                    'start_date',
                    'end_date',
                    'start_month',
                    'end_month',
                ]
            },
            root_map={
                'validations': {
                    ('time_granularity',): {

                        'regex': {
                            'pattern': r'^day$|^month$',  # noqa: E501
                        },
                    },
                    ('start_date',): {

                        'regex': {
                            'pattern': r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',  # noqa: E501
                        },
                    },
                    ('end_date',): {

                        'regex': {
                            'pattern': r'^[0-9]{4}-[0-9]{2}-[0-9]{2}$',  # noqa: E501
                        },
                    },
                    ('start_month',): {

                        'regex': {
                            'pattern': r'^[0-9]{4}-[0-9]{2}$',  # noqa: E501
                        },
                    },
                    ('end_month',): {

                        'regex': {
                            'pattern': r'^[0-9]{4}-[0-9]{2}$',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'customer_id':
                        (str,),
                    'product_id':
                        (str,),
                    'usage_type_name':
                        (str,),
                    'time_granularity':
                        (str,),
                    'start_date':
                        (str,),
                    'end_date':
                        (str,),
                    'start_month':
                        (str,),
                    'end_month':
                        (str,),
                    'limit':
                        (str,),
                    'cursor':
                        (str,),
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                    'product_id': 'product_id',
                    'usage_type_name': 'usage_type_name',
                    'time_granularity': 'time_granularity',
                    'start_date': 'start_date',
                    'end_date': 'end_date',
                    'start_month': 'start_month',
                    'end_month': 'end_month',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'customer_id': 'path',
                    'product_id': 'query',
                    'usage_type_name': 'query',
                    'time_granularity': 'query',
                    'start_date': 'query',
                    'end_date': 'query',
                    'start_month': 'query',
                    'end_month': 'query',
                    'limit': 'query',
                    'cursor': 'query',
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
        self.get_service_level_usage_types_endpoint = _Endpoint(
            settings={
                'response_type': (Serviceusagetypes,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/billing/v2/account_customers/{customer_id}/service-usage-types',
                'operation_id': 'get_service_level_usage_types',
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
                    'customer_id',
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
                },
                'attribute_map': {
                    'customer_id': 'customer_id',
                },
                'location_map': {
                    'customer_id': 'path',
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

    def get_service_level_usage(
        self,
        customer_id,
        product_id,
        usage_type_name,
        time_granularity,
        **kwargs
    ):
        """Retrieve service-level usage metrics for a product.  # noqa: E501

        Returns product usage, broken down by service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_service_level_usage(customer_id, product_id, usage_type_name, time_granularity, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.
            product_id (str): The product identifier for the metrics returned (e.g., `cdn_usage`). This field is not required for CSV requests.
            usage_type_name (str): The usage type name for the metrics returned (e.g., `North America Requests`). This field is not required for CSV requests.
            time_granularity (str):

        Keyword Args:
            start_date (str): [optional]
            end_date (str): [optional]
            start_month (str): [optional]
            end_month (str): [optional]
            limit (str): Number of results per page. The maximum is 100.. [optional] if omitted the server will use the default value of "5"
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
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
            Serviceusagemetrics
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
        kwargs['product_id'] = \
            product_id
        kwargs['usage_type_name'] = \
            usage_type_name
        kwargs['time_granularity'] = \
            time_granularity
        return self.get_service_level_usage_endpoint.call_with_http_info(**kwargs)

    def get_service_level_usage_types(
        self,
        customer_id,
        **kwargs
    ):
        """Retrieve product usage types for a customer.  # noqa: E501

        Returns product usage types reported by the customer's services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_service_level_usage_types(customer_id, async_req=True)
        >>> result = thread.get()

        Args:
            customer_id (str): Alphanumeric string identifying the customer.

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
            Serviceusagetypes
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
        return self.get_service_level_usage_types_endpoint.call_with_http_info(**kwargs)

