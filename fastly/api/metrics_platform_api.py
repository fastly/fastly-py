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
from fastly.model.platform_metrics_response import PlatformMetricsResponse


class MetricsPlatformApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_platform_metrics_service_historical_endpoint = _Endpoint(
            settings={
                'response_type': (PlatformMetricsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/metrics/platform/services/{service_id}/{granularity}',
                'operation_id': 'get_platform_metrics_service_historical',
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
                    'granularity',
                    '_from',
                    'to',
                    'metric',
                    'metric_set',
                    'group_by',
                    'region',
                    'datacenter',
                    'cursor',
                    'limit',
                ],
                'required': [
                    'service_id',
                    'granularity',
                ],
                'nullable': [
                ],
                'enum': [
                    'granularity',
                    'metric_set',
                    'group_by',
                    'region',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('granularity',): {

                        "MINUTELY": "minutely",
                        "HOURLY": "hourly",
                        "DAILY": "daily"
                    },
                    ('metric_set',): {

                        "TTFB": "ttfb"
                    },
                    ('group_by',): {

                        "DATACENTER": "datacenter",
                        "REGION": "region"
                    },
                    ('region',): {

                        "AFRICA_STD": "africa_std",
                        "ANZAC": "anzac",
                        "ASIA": "asia",
                        "ASIA_INDIA": "asia_india",
                        "ASIA_SOUTHKOREA": "asia_southkorea",
                        "EUROPE": "europe",
                        "MEXICO": "mexico",
                        "SOUTHAMERICA_STD": "southamerica_std",
                        "USA": "usa"
                    },
                },
                'openapi_types': {
                    'service_id':
                        (str,),
                    'granularity':
                        (str,),
                    '_from':
                        (str,),
                    'to':
                        (str,),
                    'metric':
                        (str,),
                    'metric_set':
                        (str,),
                    'group_by':
                        (str,),
                    'region':
                        (str,),
                    'datacenter':
                        (str,),
                    'cursor':
                        (str,),
                    'limit':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'granularity': 'granularity',
                    '_from': 'from',
                    'to': 'to',
                    'metric': 'metric',
                    'metric_set': 'metric_set',
                    'group_by': 'group_by',
                    'region': 'region',
                    'datacenter': 'datacenter',
                    'cursor': 'cursor',
                    'limit': 'limit',
                },
                'location_map': {
                    'service_id': 'path',
                    'granularity': 'path',
                    '_from': 'query',
                    'to': 'query',
                    'metric': 'query',
                    'metric_set': 'query',
                    'group_by': 'query',
                    'region': 'query',
                    'datacenter': 'query',
                    'cursor': 'query',
                    'limit': 'query',
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

    def get_platform_metrics_service_historical(
        self,
        service_id,
        granularity,
        **kwargs
    ):
        """Get historical time series metrics for a single service  # noqa: E501

        Fetches historical metrics for a single service for a given granularity.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_platform_metrics_service_historical(service_id, granularity, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.
            granularity (str): Duration of sample windows.

        Keyword Args:
            _from (str): A valid RFC-8339-formatted date and time indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `granularity` value.. [optional]
            to (str): A valid RFC-8339-formatted date and time indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `granularity` value.. [optional]
            metric (str): The metric(s) to retrieve. Multiple values should be comma-separated.. [optional]
            metric_set (str): The metric set(s) to retrieve. Multiple values should be comma-separated.. [optional] if omitted the server will use the default value of "ttfb"
            group_by (str): Field to group_by in the query. For example, `group_by=region` will return entries for grouped by timestamp and region. . [optional]
            region (str): Limit query to one or more specific geographic regions. Values should be comma-separated. . [optional]
            datacenter (str): Limit query to one or more specific POPs. Values should be comma-separated.. [optional]
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            limit (str): Number of results per page. The maximum is 10000.. [optional] if omitted the server will use the default value of "1000"
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
            PlatformMetricsResponse
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
        kwargs['granularity'] = \
            granularity
        return self.get_platform_metrics_service_historical_endpoint.call_with_http_info(**kwargs)

