# fastly.WholePlatformDdosHistoricalApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_platform_ddos_historical**](WholePlatformDdosHistoricalApi.md#get_platform_ddos_historical) | **GET** /metrics/platform/ddos | Get historical DDoS metrics for the entire Fastly platform


# **get_platform_ddos_historical**
> PlatformDdosResponse get_platform_ddos_historical()

Get historical DDoS metrics for the entire Fastly platform

Fetches historical DDoS metrics for the entire Fastly platform.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import whole_platform_ddos_historical_api
from fastly.model.platform_ddos_response import PlatformDdosResponse
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
    api_instance = whole_platform_ddos_historical_api.WholePlatformDdosHistoricalApi(api_client)
    start = "2021-08-01T00:00:00.000Z" # str | A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `downsample` value. (optional)
    end = "2020-08-02T00:00:00.000Z" # str | A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `downsample` value. (optional)
    downsample = "hour" # str | Duration of sample windows. (optional) if omitted the server will use the default value of "hour"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get historical DDoS metrics for the entire Fastly platform
        api_response = api_instance.get_platform_ddos_historical(start=start, end=end, downsample=downsample)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WholePlatformDdosHistoricalApi->get_platform_ddos_historical: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | **str**| A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the inclusive start of the query time range. If not provided, a default is chosen based on the provided `downsample` value. | [optional]
 **end** | **str**| A valid ISO-8601-formatted date and time, or UNIX timestamp, indicating the exclusive end of the query time range. If not provided, a default is chosen based on the provided `downsample` value. | [optional]
 **downsample** | **str**| Duration of sample windows. | [optional] if omitted the server will use the default value of "hour"

### Return type

[**PlatformDdosResponse**](PlatformDdosResponse.md)

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

