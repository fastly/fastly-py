# fastly.ObservabilityAggregationsForLogsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**log_aggregations_get**](ObservabilityAggregationsForLogsApi.md#log_aggregations_get) | **GET** /observability/aggregations | Retrieve aggregated log results


# **log_aggregations_get**
> LogAggregationsGetResponse log_aggregations_get(source, service_id, start, end, series)

Retrieve aggregated log results

Retrieves aggregated log results.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_aggregations_for_logs_api
from fastly.model.log_aggregations_get_response import LogAggregationsGetResponse
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
    api_instance = observability_aggregations_for_logs_api.ObservabilityAggregationsForLogsApi(api_client)
    source = "source_example" # str | 
    service_id = "service_id_example" # str | 
    start = "start_example" # str | 
    end = "end_example" # str | 
    series = "series_example" # str | 
    limit = 3.14 # float |  (optional)
    filter = "filter_example" # str |  (optional)
    dimensions = "dimensions_example" # str |  (optional)
    sort = "sort_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve aggregated log results
        api_response = api_instance.log_aggregations_get(source, service_id, start, end, series)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityAggregationsForLogsApi->log_aggregations_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve aggregated log results
        api_response = api_instance.log_aggregations_get(source, service_id, start, end, series, limit=limit, filter=filter, dimensions=dimensions, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityAggregationsForLogsApi->log_aggregations_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source** | **str**|  |
 **service_id** | **str**|  |
 **start** | **str**|  |
 **end** | **str**|  |
 **series** | **str**|  |
 **limit** | **float**|  | [optional]
 **filter** | **str**|  | [optional]
 **dimensions** | **str**|  | [optional]
 **sort** | **str**|  | [optional]

### Return type

[**LogAggregationsGetResponse**](LogAggregationsGetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves aggregated log records. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

