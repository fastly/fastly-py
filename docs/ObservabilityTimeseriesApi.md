# fastly.ObservabilityTimeseriesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**timeseries_get**](ObservabilityTimeseriesApi.md#timeseries_get) | **GET** /observability/timeseries | Retrieve observability data as a time series


# **timeseries_get**
> TimeseriesGetResponse timeseries_get(source, _from, to, granularity, series)

Retrieve observability data as a time series

Retrieves observability data as a time series.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_timeseries_api
from fastly.model.timeseries_get_response import TimeseriesGetResponse
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
    api_instance = observability_timeseries_api.ObservabilityTimeseriesApi(api_client)
    source = "logs" # str | 
    _from = "2024-01-03T16:00:00Z" # str | 
    to = "2024-01-03T18:00:00Z" # str | 
    granularity = "hour" # str | 
    series = "avg[response_time],p99[response_time]" # str | 
    dimensions = "dimensions_example" # str |  (optional)
    filter = "filter[response_status]=200" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve observability data as a time series
        api_response = api_instance.timeseries_get(source, _from, to, granularity, series)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityTimeseriesApi->timeseries_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve observability data as a time series
        api_response = api_instance.timeseries_get(source, _from, to, granularity, series, dimensions=dimensions, filter=filter)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityTimeseriesApi->timeseries_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  |
 **_from** | **str**|  |
 **to** | **str**|  |
 **granularity** | **str**|  |
 **series** | **str**|  |
 **dimensions** | **str**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**TimeseriesGetResponse**](TimeseriesGetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves the time series results based on observability data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

