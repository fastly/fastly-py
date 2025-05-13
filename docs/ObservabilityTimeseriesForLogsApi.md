# fastly.ObservabilityTimeseriesForLogsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_timeseries_get**](ObservabilityTimeseriesForLogsApi.md#log_timeseries_get) | **GET** /observability/timeseries | Retrieve log data as time series


# **log_timeseries_get**
> LogTimeseriesGetResponse log_timeseries_get(source, service_id, start, end, granularity, series)

Retrieve log data as time series

Retrieves log data as time series.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_timeseries_for_logs_api
from fastly.model.log_timeseries_get_response import LogTimeseriesGetResponse
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
    api_instance = observability_timeseries_for_logs_api.ObservabilityTimeseriesForLogsApi(api_client)
    source = "source_example" # str | 
    service_id = "service_id_example" # str | 
    start = "start_example" # str | 
    end = "end_example" # str | 
    granularity = "second" # str | 
    series = "series_example" # str | 
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve log data as time series
        api_response = api_instance.log_timeseries_get(source, service_id, start, end, granularity, series)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityTimeseriesForLogsApi->log_timeseries_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve log data as time series
        api_response = api_instance.log_timeseries_get(source, service_id, start, end, granularity, series, filter=filter)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityTimeseriesForLogsApi->log_timeseries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  |
 **service_id** | **str**|  |
 **start** | **str**|  |
 **end** | **str**|  |
 **granularity** | **str**|  |
 **series** | **str**|  |
 **filter** | **str**|  | [optional]

### Return type

[**LogTimeseriesGetResponse**](LogTimeseriesGetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves time series results based on log data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

