# fastly.BotRequestsMetricsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_bot_request_metrics_service_historical**](BotRequestsMetricsApi.md#get_bot_request_metrics_service_historical) | **GET** /metrics/bots/entities/{service_id}/{granularity} | Get per-service historical time series metrics for bot requests broken down by bot-type.


# **get_bot_request_metrics_service_historical**
> BotRequestMetricsResponse get_bot_request_metrics_service_historical(granularity, service_id)

Get per-service historical time series metrics for bot requests broken down by bot-type.

Return historical time series metrics for bot requests broken down by bot-type.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_requests_metrics_api
from fastly.model.bot_request_metrics_response import BotRequestMetricsResponse
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
    api_instance = bot_requests_metrics_api.BotRequestsMetricsApi(api_client)
    granularity = "minutely" # str | Duration of sample windows.
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    _from = "2025-06-08T00:00:00.000Z" # str | A valid RFC-8339-formatted date and time indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `granularity` value. (optional)
    to = "2025-08-02T00:00:00.000Z" # str | A valid RFC-8339-formatted date and time indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `granularity` value. (optional)
    group_by = "bot_id" # str | Field to group by in the query. For example, `group_by=bot_id` will return entries grouped by `timestamp` and `bot_id`.  (optional)
    datacenter = "SJC,STP" # str | Limit query to one or more specific POPs. Values should be comma-separated. (optional)
    bot = "bot_example" # str | Filter results based by Bot ID. (optional)
    region = "usa" # str | Limit query to one or more specific geographic regions. Values should be comma-separated.  (optional)
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    metric = "status_4xx,status_5xx,ipv6,http3" # str | One or more metrics to retrieve. Multiple values should be comma-separated. (optional)
    metric_set = "content_guard" # str | The metric set to retrieve. (optional) if omitted the server will use the default value of "content_guard"
    limit = "1000" # str | Number of results per page. The maximum is 10000. (optional) if omitted the server will use the default value of "1000"

    # example passing only required values which don't have defaults set
    try:
        # Get per-service historical time series metrics for bot requests broken down by bot-type.
        api_response = api_instance.get_bot_request_metrics_service_historical(granularity, service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotRequestsMetricsApi->get_bot_request_metrics_service_historical: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get per-service historical time series metrics for bot requests broken down by bot-type.
        api_response = api_instance.get_bot_request_metrics_service_historical(granularity, service_id, _from=_from, to=to, group_by=group_by, datacenter=datacenter, bot=bot, region=region, cursor=cursor, metric=metric, metric_set=metric_set, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotRequestsMetricsApi->get_bot_request_metrics_service_historical: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **granularity** | **str**| Duration of sample windows. |
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **_from** | **str**| A valid RFC-8339-formatted date and time indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `granularity` value. | [optional]
 **to** | **str**| A valid RFC-8339-formatted date and time indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `granularity` value. | [optional]
 **group_by** | **str**| Field to group by in the query. For example, `group_by&#x3D;bot_id` will return entries grouped by `timestamp` and `bot_id`.  | [optional]
 **datacenter** | **str**| Limit query to one or more specific POPs. Values should be comma-separated. | [optional]
 **bot** | **str**| Filter results based by Bot ID. | [optional]
 **region** | **str**| Limit query to one or more specific geographic regions. Values should be comma-separated.  | [optional]
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **metric** | **str**| One or more metrics to retrieve. Multiple values should be comma-separated. | [optional]
 **metric_set** | **str**| The metric set to retrieve. | [optional] if omitted the server will use the default value of "content_guard"
 **limit** | **str**| Number of results per page. The maximum is 10000. | [optional] if omitted the server will use the default value of "1000"

### Return type

[**BotRequestMetricsResponse**](BotRequestMetricsResponse.md)

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

