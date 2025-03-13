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
from fastly.model.usagemetric import Usagemetric


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
                'endpoint_path': '/billing/v3/service-usage-metrics',
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
                    'product_id',
                    'service',
                    'usage_type_name',
                    'start_month',
                    'end_month',
                    'limit',
                    'cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'start_month',
                    'end_month',
                ]
            },
            root_map={
                'validations': {
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
                    'product_id':
                        (str,),
                    'service':
                        (str,),
                    'usage_type_name':
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
                    'product_id': 'product_id',
                    'service': 'service',
                    'usage_type_name': 'usage_type_name',
                    'start_month': 'start_month',
                    'end_month': 'end_month',
                    'limit': 'limit',
                    'cursor': 'cursor',
                },
                'location_map': {
                    'product_id': 'query',
                    'service': 'query',
                    'usage_type_name': 'query',
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
        self.get_usage_metrics_endpoint = _Endpoint(
            settings={
                'response_type': (Usagemetric,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/billing/v3/usage-metrics',
                'operation_id': 'get_usage_metrics',
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
                    'start_month',
                    'end_month',
                ],
                'required': [
                    'start_month',
                    'end_month',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'start_month',
                    'end_month',
                ]
            },
            root_map={
                'validations': {
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
                    'start_month':
                        (str,),
                    'end_month':
                        (str,),
                },
                'attribute_map': {
                    'start_month': 'start_month',
                    'end_month': 'end_month',
                },
                'location_map': {
                    'start_month': 'query',
                    'end_month': 'query',
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
        **kwargs
    ):
        """Retrieve service-level usage metrics for services with non-zero usage units.  # noqa: E501

        Returns product usage, broken down by service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_service_level_usage(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            product_id (str): The product identifier for the metrics returned (e.g., `cdn_usage`). This should be used along with `usage_type_name`.. [optional]
            service (str): The service identifier for the metrics being requested.. [optional]
            usage_type_name (str): The usage type name for the metrics returned (e.g., `North America Requests`). This should be used along with `product_id`.. [optional]
            start_month (str): [optional]
            end_month (str): [optional]
            limit (str): Number of results per page. The maximum is 10000.. [optional] if omitted the server will use the default value of "1000"
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
        return self.get_service_level_usage_endpoint.call_with_http_info(**kwargs)

    def get_usage_metrics(
        self,
        start_month,
        end_month,
        **kwargs
    ):
        """Get monthly usage metrics  # noqa: E501

        Returns monthly usage metrics for customer by product.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_usage_metrics(start_month, end_month, async_req=True)
        >>> result = thread.get()

        Args:
            start_month (str):
            end_month (str):

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
            Usagemetric
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
        kwargs['start_month'] = \
            start_month
        kwargs['end_month'] = \
            end_month
        return self.get_usage_metrics_endpoint.call_with_http_info(**kwargs)

