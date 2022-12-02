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
from fastly.model.historical_aggregate_response import HistoricalAggregateResponse
from fastly.model.historical_field_aggregate_response import HistoricalFieldAggregateResponse
from fastly.model.historical_field_response import HistoricalFieldResponse
from fastly.model.historical_regions_response import HistoricalRegionsResponse
from fastly.model.historical_response import HistoricalResponse
from fastly.model.historical_usage_aggregate_response import HistoricalUsageAggregateResponse
from fastly.model.historical_usage_month_response import HistoricalUsageMonthResponse
from fastly.model.historical_usage_service_response import HistoricalUsageServiceResponse


class HistoricalApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_hist_stats_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats',
                'operation_id': 'get_hist_stats',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    '_from',
                    'to',
                    'by',
                    'region',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'by',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('by',): {

                        "HOUR": "hour",
                        "MINUTE": "minute",
                        "DAY": "day"
                    },
                    ('region',): {

                        "USA": "usa",
                        "EUROPE": "europe",
                        "ASIA": "asia",
                        "ASIA_INDIA": "asia_india",
                        "ASIA_SOUTHKOREA": "asia_southkorea",
                        "AFRICA_STD": "africa_std",
                        "SOUTHAMERICA_STD": "southamerica_std"
                    },
                },
                'openapi_types': {
                    '_from':
                        (str,),
                    'to':
                        (str,),
                    'by':
                        (str,),
                    'region':
                        (str,),
                },
                'attribute_map': {
                    '_from': 'from',
                    'to': 'to',
                    'by': 'by',
                    'region': 'region',
                },
                'location_map': {
                    '_from': 'query',
                    'to': 'query',
                    'by': 'query',
                    'region': 'query',
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
        self.get_hist_stats_aggregated_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalAggregateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/aggregate',
                'operation_id': 'get_hist_stats_aggregated',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    '_from',
                    'to',
                    'by',
                    'region',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'by',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('by',): {

                        "HOUR": "hour",
                        "MINUTE": "minute",
                        "DAY": "day"
                    },
                    ('region',): {

                        "USA": "usa",
                        "EUROPE": "europe",
                        "ASIA": "asia",
                        "ASIA_INDIA": "asia_india",
                        "ASIA_SOUTHKOREA": "asia_southkorea",
                        "AFRICA_STD": "africa_std",
                        "SOUTHAMERICA_STD": "southamerica_std"
                    },
                },
                'openapi_types': {
                    '_from':
                        (str,),
                    'to':
                        (str,),
                    'by':
                        (str,),
                    'region':
                        (str,),
                },
                'attribute_map': {
                    '_from': 'from',
                    'to': 'to',
                    'by': 'by',
                    'region': 'region',
                },
                'location_map': {
                    '_from': 'query',
                    'to': 'query',
                    'by': 'query',
                    'region': 'query',
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
        self.get_hist_stats_field_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalFieldResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/field/{field}',
                'operation_id': 'get_hist_stats_field',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'field',
                    '_from',
                    'to',
                    'by',
                    'region',
                ],
                'required': [
                    'field',
                ],
                'nullable': [
                ],
                'enum': [
                    'by',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('by',): {

                        "HOUR": "hour",
                        "MINUTE": "minute",
                        "DAY": "day"
                    },
                    ('region',): {

                        "USA": "usa",
                        "EUROPE": "europe",
                        "ASIA": "asia",
                        "ASIA_INDIA": "asia_india",
                        "ASIA_SOUTHKOREA": "asia_southkorea",
                        "AFRICA_STD": "africa_std",
                        "SOUTHAMERICA_STD": "southamerica_std"
                    },
                },
                'openapi_types': {
                    'field':
                        (str,),
                    '_from':
                        (str,),
                    'to':
                        (str,),
                    'by':
                        (str,),
                    'region':
                        (str,),
                },
                'attribute_map': {
                    'field': 'field',
                    '_from': 'from',
                    'to': 'to',
                    'by': 'by',
                    'region': 'region',
                },
                'location_map': {
                    'field': 'path',
                    '_from': 'query',
                    'to': 'query',
                    'by': 'query',
                    'region': 'query',
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
        self.get_hist_stats_service_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalAggregateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/service/{service_id}',
                'operation_id': 'get_hist_stats_service',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    '_from',
                    'to',
                    'by',
                    'region',
                ],
                'required': [
                    'service_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'by',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('by',): {

                        "HOUR": "hour",
                        "MINUTE": "minute",
                        "DAY": "day"
                    },
                    ('region',): {

                        "USA": "usa",
                        "EUROPE": "europe",
                        "ASIA": "asia",
                        "ASIA_INDIA": "asia_india",
                        "ASIA_SOUTHKOREA": "asia_southkorea",
                        "AFRICA_STD": "africa_std",
                        "SOUTHAMERICA_STD": "southamerica_std"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    '_from':
                        (str,),
                    'to':
                        (str,),
                    'by':
                        (str,),
                    'region':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    '_from': 'from',
                    'to': 'to',
                    'by': 'by',
                    'region': 'region',
                },
                'location_map': {
                    'service_id': 'path',
                    '_from': 'query',
                    'to': 'query',
                    'by': 'query',
                    'region': 'query',
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
        self.get_hist_stats_service_field_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalFieldAggregateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/service/{service_id}/field/{field}',
                'operation_id': 'get_hist_stats_service_field',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'service_id',
                    'field',
                    '_from',
                    'to',
                    'by',
                    'region',
                ],
                'required': [
                    'service_id',
                    'field',
                ],
                'nullable': [
                ],
                'enum': [
                    'by',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('by',): {

                        "HOUR": "hour",
                        "MINUTE": "minute",
                        "DAY": "day"
                    },
                    ('region',): {

                        "USA": "usa",
                        "EUROPE": "europe",
                        "ASIA": "asia",
                        "ASIA_INDIA": "asia_india",
                        "ASIA_SOUTHKOREA": "asia_southkorea",
                        "AFRICA_STD": "africa_std",
                        "SOUTHAMERICA_STD": "southamerica_std"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'field':
                        (str,),
                    '_from':
                        (str,),
                    'to':
                        (str,),
                    'by':
                        (str,),
                    'region':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'field': 'field',
                    '_from': 'from',
                    'to': 'to',
                    'by': 'by',
                    'region': 'region',
                },
                'location_map': {
                    'service_id': 'path',
                    'field': 'path',
                    '_from': 'query',
                    'to': 'query',
                    'by': 'query',
                    'region': 'query',
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
        self.get_regions_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalRegionsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/regions',
                'operation_id': 'get_regions',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
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
                },
                'attribute_map': {
                },
                'location_map': {
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
        self.get_usage_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalUsageAggregateResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/usage',
                'operation_id': 'get_usage',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    '_from',
                    'to',
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
                    '_from':
                        (str,),
                    'to':
                        (str,),
                },
                'attribute_map': {
                    '_from': 'from',
                    'to': 'to',
                },
                'location_map': {
                    '_from': 'query',
                    'to': 'query',
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
        self.get_usage_month_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalUsageMonthResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/usage_by_month',
                'operation_id': 'get_usage_month',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'year',
                    'month',
                    'billable_units',
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
                    'year':
                        (str,),
                    'month':
                        (str,),
                    'billable_units':
                        (bool,),
                },
                'attribute_map': {
                    'year': 'year',
                    'month': 'month',
                    'billable_units': 'billable_units',
                },
                'location_map': {
                    'year': 'query',
                    'month': 'query',
                    'billable_units': 'query',
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
        self.get_usage_service_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalUsageServiceResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/stats/usage_by_service',
                'operation_id': 'get_usage_service',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    '_from',
                    'to',
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
                    '_from':
                        (str,),
                    'to':
                        (str,),
                },
                'attribute_map': {
                    '_from': 'from',
                    'to': 'to',
                },
                'location_map': {
                    '_from': 'query',
                    'to': 'query',
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

    def get_hist_stats(
        self,
        **kwargs
    ):
        """Get historical stats  # noqa: E501

        Fetches historical stats for each of your Fastly services and groups the results by service ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_hist_stats(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
            by (str): Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day. . [optional] if omitted the server will use the default value of "day"
            region (str): Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea ([from Aug 2, 2021](https://status.fastly.com/incidents/f83m70cqm258))   * `africa_std` - Africa.   * `southamerica_std` - South America. . [optional]
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
            HistoricalResponse
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
        return self.get_hist_stats_endpoint.call_with_http_info(**kwargs)

    def get_hist_stats_aggregated(
        self,
        **kwargs
    ):
        """Get aggregated historical stats  # noqa: E501

        Fetches historical stats information aggregated across all of your Fastly services.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_hist_stats_aggregated(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
            by (str): Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day. . [optional] if omitted the server will use the default value of "day"
            region (str): Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea ([from Aug 2, 2021](https://status.fastly.com/incidents/f83m70cqm258))   * `africa_std` - Africa.   * `southamerica_std` - South America. . [optional]
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
            HistoricalAggregateResponse
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
        return self.get_hist_stats_aggregated_endpoint.call_with_http_info(**kwargs)

    def get_hist_stats_field(
        self,
        field,
        **kwargs
    ):
        """Get historical stats for a single field  # noqa: E501

        Fetches the specified field from the historical stats for each of your services and groups the results by service ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_hist_stats_field(field, async_req=True)
        >>> result = thread.get()

        Args:
            field (str): Name of the stats field.

        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
            by (str): Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day. . [optional] if omitted the server will use the default value of "day"
            region (str): Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea ([from Aug 2, 2021](https://status.fastly.com/incidents/f83m70cqm258))   * `africa_std` - Africa.   * `southamerica_std` - South America. . [optional]
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
            HistoricalFieldResponse
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
        kwargs['field'] = \
            field
        return self.get_hist_stats_field_endpoint.call_with_http_info(**kwargs)

    def get_hist_stats_service(
        self,
        service_id,
        **kwargs
    ):
        """Get historical stats for a single service  # noqa: E501

        Fetches historical stats for a given service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_hist_stats_service(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.

        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
            by (str): Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day. . [optional] if omitted the server will use the default value of "day"
            region (str): Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea ([from Aug 2, 2021](https://status.fastly.com/incidents/f83m70cqm258))   * `africa_std` - Africa.   * `southamerica_std` - South America. . [optional]
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
            HistoricalAggregateResponse
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
        return self.get_hist_stats_service_endpoint.call_with_http_info(**kwargs)

    def get_hist_stats_service_field(
        self,
        service_id,
        field,
        **kwargs
    ):
        """Get historical stats for a single service/field combination  # noqa: E501

        Fetches the specified field from the historical stats for a given service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_hist_stats_service_field(service_id, field, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            field (str): Name of the stats field.

        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
            by (str): Duration of sample windows. One of:   * `hour` - Group data by hour.   * `minute` - Group data by minute.   * `day` - Group data by day. . [optional] if omitted the server will use the default value of "day"
            region (str): Limit query to a specific geographic region. One of:   * `usa` - North America.   * `europe` - Europe.   * `anzac` - Australia and New Zealand.   * `asia` - Asia.   * `asia_india` - India.   * `asia_southkorea` - South Korea ([from Aug 2, 2021](https://status.fastly.com/incidents/f83m70cqm258))   * `africa_std` - Africa.   * `southamerica_std` - South America. . [optional]
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
            HistoricalFieldAggregateResponse
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
        kwargs['field'] = \
            field
        return self.get_hist_stats_service_field_endpoint.call_with_http_info(**kwargs)

    def get_regions(
        self,
        **kwargs
    ):
        """Get region codes  # noqa: E501

        Fetches the list of codes for regions that are covered by the Fastly CDN service.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_regions(async_req=True)
        >>> result = thread.get()


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
            HistoricalRegionsResponse
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
        return self.get_regions_endpoint.call_with_http_info(**kwargs)

    def get_usage(
        self,
        **kwargs
    ):
        """Get usage statistics  # noqa: E501

        Returns usage information aggregated across all Fastly services and grouped by region. To aggregate across all Fastly services by time period, see [`/stats/aggregate`](#get-hist-stats-aggregated).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_usage(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
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
            HistoricalUsageAggregateResponse
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
        return self.get_usage_endpoint.call_with_http_info(**kwargs)

    def get_usage_month(
        self,
        **kwargs
    ):
        """Get month-to-date usage statistics  # noqa: E501

        Returns month-to-date usage details for a given month and year. Usage details are aggregated by service and across all Fastly services, and then grouped by region. This endpoint does not use the `from` or `to` fields for selecting the date for which data is requested. Instead, it uses `month` and `year` integer fields. Both fields are optional and default to the current month and year respectively. When set, an optional `billable_units` field will convert bandwidth to GB and divide requests by 10,000.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_usage_month(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            year (str): 4-digit year.. [optional]
            month (str): 2-digit month.. [optional]
            billable_units (bool): If `true`, return results as billable units.. [optional]
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
            HistoricalUsageMonthResponse
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
        return self.get_usage_month_endpoint.call_with_http_info(**kwargs)

    def get_usage_service(
        self,
        **kwargs
    ):
        """Get usage statistics per service  # noqa: E501

        Returns usage information aggregated by service and grouped by service and region. For service stats by time period, see [`/stats`](#get-hist-stats) and [`/stats/field/:field`](#get-hist-stats-field).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_usage_service(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            _from (str): Timestamp that defines the start of the window for which to fetch statistics, including the timestamp itself. Accepts Unix timestamps, or any form of input parsable by the [Chronic Ruby library](https://github.com/mojombo/chronic), such as 'yesterday', or 'two weeks ago'. Default varies based on the value of `by`. . [optional]
            to (str): Timestamp that defines the end of the window for which to fetch statistics. Accepts the same formats as `from`. . [optional] if omitted the server will use the default value of "now"
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
            HistoricalUsageServiceResponse
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
        return self.get_usage_service_endpoint.call_with_http_info(**kwargs)

