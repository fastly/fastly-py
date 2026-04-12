# fastly.MetricsPlatformApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform_metrics_service_historical**](MetricsPlatformApi.md#get_platform_metrics_service_historical) | **GET** /metrics/platform/services/{service_id}/{granularity} | Get historical time series metrics for a single service


# **get_platform_metrics_service_historical**
> PlatformMetricsResponse get_platform_metrics_service_historical(service_id, granularity)

Get historical time series metrics for a single service

Fetches historical metrics for a single service for a given granularity.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import metrics_platform_api
from fastly.model.platform_metrics_response import PlatformMetricsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://api.fastly.com
# See configuration.py for a list of all supported configuration parameters.
configuration = fastly.Configuration(
    host = "https://api.fastly.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: token
configuration.api_key['token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['token'] = 'Bearer'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metrics_platform_api.MetricsPlatformApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    granularity = "daily" # str | Duration of sample windows.
    _from = "2025-06-08T00:00:00.000Z" # str | A valid RFC-8339-formatted date and time indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `granularity` value. (optional)
    to = "2025-08-02T00:00:00.000Z" # str | A valid RFC-8339-formatted date and time indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `granularity` value. (optional)
    metric = "ttfb_edge_p95_us,ttfb_edge_p99_us" # str | The metric(s) to retrieve. Multiple values should be comma-separated. (optional)
    metric_set = "ttfb" # str | The metric set(s) to retrieve. Multiple values should be comma-separated. (optional) if omitted the server will use the default value of "ttfb"
    group_by = "region" # str | Field to group_by in the query. For example, `group_by=region` will return entries for grouped by timestamp and region.  (optional)
    region = "usa" # str | Limit query to one or more specific geographic regions. Values should be comma-separated.  (optional)
    datacenter = "SJC,STP" # str | Limit query to one or more specific POPs. Values should be comma-separated. (optional)
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = "1000" # str | Number of results per page. The maximum is 10000. (optional) if omitted the server will use the default value of "1000"

    # example passing only required values which don't have defaults set
    try:
        # Get historical time series metrics for a single service
        api_response = api_instance.get_platform_metrics_service_historical(service_id, granularity)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MetricsPlatformApi->get_platform_metrics_service_historical: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical time series metrics for a single service
        api_response = api_instance.get_platform_metrics_service_historical(service_id, granularity, _from=_from, to=to, metric=metric, metric_set=metric_set, group_by=group_by, region=region, datacenter=datacenter, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MetricsPlatformApi->get_platform_metrics_service_historical: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **granularity** | **str**| Duration of sample windows. |
 **_from** | **str**| A valid RFC-8339-formatted date and time indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `granularity` value. | [optional]
 **to** | **str**| A valid RFC-8339-formatted date and time indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `granularity` value. | [optional]
 **metric** | **str**| The metric(s) to retrieve. Multiple values should be comma-separated. | [optional]
 **metric_set** | **str**| The metric set(s) to retrieve. Multiple values should be comma-separated. | [optional] if omitted the server will use the default value of "ttfb"
 **group_by** | **str**| Field to group_by in the query. For example, `group_by&#x3D;region` will return entries for grouped by timestamp and region.  | [optional]
 **region** | **str**| Limit query to one or more specific geographic regions. Values should be comma-separated.  | [optional]
 **datacenter** | **str**| Limit query to one or more specific POPs. Values should be comma-separated. | [optional]
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **str**| Number of results per page. The maximum is 10000. | [optional] if omitted the server will use the default value of "1000"

### Return type

[**PlatformMetricsResponse**](PlatformMetricsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

