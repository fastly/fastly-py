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
from fastly.model.historical_domains_response import HistoricalDomainsResponse


class DomainInspectorHistoricalApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_domain_inspector_historical_endpoint = _Endpoint(
            settings={
                'response_type': (HistoricalDomainsResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/metrics/domains/services/{service_id}',
                'operation_id': 'get_domain_inspector_historical',
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
                    'start',
                    'end',
                    'downsample',
                    'metric',
                    'group_by',
                    'limit',
                    'cursor',
                    'region',
                    'datacenter',
                    'domain',
                ],
                'required': [
                    'service_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'downsample',
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
                    ('downsample',): {

                        "HOUR": "hour",
                        "MINUTE": "minute",
                        "DAY": "day"
                    },
                    ('group_by',): {

                        "DOMAIN": "domain",
                        "DATACENTER": "datacenter",
                        "REGION": "region",
                        "NONE": "none"
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
                    'start':
                        (str,),
                    'end':
                        (str,),
                    'downsample':
                        (str,),
                    'metric':
                        (str,),
                    'group_by':
                        (str,),
                    'limit':
                        (str,),
                    'cursor':
                        (str,),
                    'region':
                        (str,),
                    'datacenter':
                        (str,),
                    'domain':
                        (str,),
                },
                'attribute_map': {
                    'service_id': 'service_id',
                    'start': 'start',
                    'end': 'end',
                    'downsample': 'downsample',
                    'metric': 'metric',
                    'group_by': 'group_by',
                    'limit': 'limit',
                    'cursor': 'cursor',
                    'region': 'region',
                    'datacenter': 'datacenter',
                    'domain': 'domain',
                },
                'location_map': {
                    'service_id': 'path',
                    'start': 'query',
                    'end': 'query',
                    'downsample': 'query',
                    'metric': 'query',
                    'group_by': 'query',
                    'limit': 'query',
                    'cursor': 'query',
                    'region': 'query',
                    'datacenter': 'query',
                    'domain': 'query',
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

    def get_domain_inspector_historical(
        self,
        service_id,
        **kwargs
    ):
        """Get historical domain data for a service  # noqa: E501

        Fetches historical domain metrics for a given Fastly service, optionally filtering and grouping the results by domain, region, or POP.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_domain_inspector_historical(service_id, async_req=True)
        >>> result = thread.get()

        Args:
            service_id (str): Alphanumeric string identifying the service.

        Keyword Args:
            start (str): A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `downsample` value.. [optional]
            end (str): A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `downsample` value.. [optional]
            downsample (str): Duration of sample windows.. [optional] if omitted the server will use the default value of "hour"
            metric (str): The metrics to retrieve. Multiple values should be comma-separated.. [optional] if omitted the server will use the default value of "edge_requests"
            group_by (str): Dimensions to return in the query. Multiple dimensions may be separated by commas. For example, `group_by=domain` will return one timeseries for every domain, as a total across all datacenters (POPs). . [optional]
            limit (str): Number of results per page. The maximum is 200.. [optional] if omitted the server will use the default value of "100"
            cursor (str): Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty.. [optional]
            region (str): Limit query to one or more specific geographic regions. Values should be comma-separated. . [optional]
            datacenter (str): Limit query to one or more specific POPs. Values should be comma-separated.. [optional]
            domain (str): Limit query to one or more specific domains. Values should be comma-separated.. [optional]
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
            HistoricalDomainsResponse
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
        return self.get_domain_inspector_historical_endpoint.call_with_http_info(**kwargs)

