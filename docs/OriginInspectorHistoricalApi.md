# fastly.OriginInspectorHistoricalApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_origin_inspector_historical**](OriginInspectorHistoricalApi.md#get_origin_inspector_historical) | **GET** /metrics/origins/services/{service_id} | Get historical origin data for a service


# **get_origin_inspector_historical**
> HistoricalOriginsResponse get_origin_inspector_historical(service_id)

Get historical origin data for a service

Fetches historical origin metrics for a given Fastly service, optionally filtering and grouping the results by origin host, region, or POP. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import origin_inspector_historical_api
from fastly.model.historical_origins_response import HistoricalOriginsResponse
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
    api_instance = origin_inspector_historical_api.OriginInspectorHistoricalApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    start = "2021-08-01T00:00:00.000Z" # str | A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `downsample` value. (optional)
    end = "2020-08-02T00:00:00.000Z" # str | A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `downsample` value. (optional)
    downsample = "hour" # str | Duration of sample windows. (optional) if omitted the server will use the default value of "hour"
    metric = "resp_body_bytes,status_2xx" # str | The metrics to retrieve. Multiple values should be comma-separated. (optional) if omitted the server will use the default value of "responses"
    group_by = "host" # str | Dimensions to return in the query. Multiple dimensions may be separated by commas. For example, `group_by=host` will return one timeseries for every origin host, as a total across all POPs.  (optional)
    limit = "100" # str | Number of results per page. The maximum is 200. (optional) if omitted the server will use the default value of "100"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    region = "usa" # str | Limit query to one or more specific geographic regions. Values should be comma-separated.  (optional)
    datacenter = "SJC,STP" # str | Limit query to one or more specific POPs. Values should be comma-separated. (optional)
    host = "origin_1,origin_2" # str | Limit query to one or more specific origin hosts. Values should be comma-separated. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get historical origin data for a service
        api_response = api_instance.get_origin_inspector_historical(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling OriginInspectorHistoricalApi->get_origin_inspector_historical: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical origin data for a service
        api_response = api_instance.get_origin_inspector_historical(service_id, start=start, end=end, downsample=downsample, metric=metric, group_by=group_by, limit=limit, cursor=cursor, region=region, datacenter=datacenter, host=host)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling OriginInspectorHistoricalApi->get_origin_inspector_historical: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **start** | **str**| A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `downsample` value. | [optional]
 **end** | **str**| A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `downsample` value. | [optional]
 **downsample** | **str**| Duration of sample windows. | [optional] if omitted the server will use the default value of "hour"
 **metric** | **str**| The metrics to retrieve. Multiple values should be comma-separated. | [optional] if omitted the server will use the default value of "responses"
 **group_by** | **str**| Dimensions to return in the query. Multiple dimensions may be separated by commas. For example, `group_by&#x3D;host` will return one timeseries for every origin host, as a total across all POPs.  | [optional]
 **limit** | **str**| Number of results per page. The maximum is 200. | [optional] if omitted the server will use the default value of "100"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **region** | **str**| Limit query to one or more specific geographic regions. Values should be comma-separated.  | [optional]
 **datacenter** | **str**| Limit query to one or more specific POPs. Values should be comma-separated. | [optional]
 **host** | **str**| Limit query to one or more specific origin hosts. Values should be comma-separated. | [optional]

### Return type

[**HistoricalOriginsResponse**](HistoricalOriginsResponse.md)

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

