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
from fastly.model.log_aggregations_get_response import LogAggregationsGetResponse


class ObservabilityAggregationsForLogsApi(object):
    """NOTE: This class is auto generated.
    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.log_aggregations_get_endpoint = _Endpoint(
            settings={
                'response_type': (LogAggregationsGetResponse,),
                'auth': [
                    'token'
                ],
                'endpoint_path': '/observability/aggregations',
                'operation_id': 'log_aggregations_get',
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
                    'source',
                    'service_id',
                    'start',
                    'end',
                    'series',
                    'limit',
                    'filter',
                    'dimensions',
                    'sort',
                ],
                'required': [
                    'source',
                    'service_id',
                    'start',
                    'end',
                    'series',
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
                    'source':
                        (str,),
                    'service_id':
                        (str,),
                    'start':
                        (str,),
                    'end':
                        (str,),
                    'series':
                        (str,),
                    'limit':
                        (float,),
                    'filter':
                        (str,),
                    'dimensions':
                        (str,),
                    'sort':
                        (str,),
                },
                'attribute_map': {
                    'source': 'source',
                    'service_id': 'service_id',
                    'start': 'start',
                    'end': 'end',
                    'series': 'series',
                    'limit': 'limit',
                    'filter': 'filter',
                    'dimensions': 'dimensions',
                    'sort': 'sort',
                },
                'location_map': {
                    'source': 'query',
                    'service_id': 'query',
                    'start': 'query',
                    'end': 'query',
                    'series': 'query',
                    'limit': 'query',
                    'filter': 'query',
                    'dimensions': 'query',
                    'sort': 'query',
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

    def log_aggregations_get(
        self,
        source,
        service_id,
        start,
        end,
        series,
        **kwargs
    ):
        """Retrieve aggregated log results  # noqa: E501

        Retrieves aggregated log results.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.log_aggregations_get(source, service_id, start, end, series, async_req=True)
        >>> result = thread.get()

        Args:
            source (str):
            service_id (str):
            start (str):
            end (str):
            series (str):

        Keyword Args:
            limit (float): [optional]
            filter (str): [optional]
            dimensions (str): [optional]
            sort (str): [optional]
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
            LogAggregationsGetResponse
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
        kwargs['source'] = \
            source
        kwargs['service_id'] = \
            service_id
        kwargs['start'] = \
            start
        kwargs['end'] = \
            end
        kwargs['series'] = \
            series
        return self.log_aggregations_get_endpoint.call_with_http_info(**kwargs)

