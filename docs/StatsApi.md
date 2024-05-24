# fastly.StatsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_stats**](StatsApi.md#get_service_stats) | **GET** /service/{service_id}/stats/summary | Get stats for a service


# **get_service_stats**
> Stats get_service_stats(service_id)

Get stats for a service

Get the stats from a service for a block of time. This lists all stats by PoP location, starting with AMS. This call requires parameters to select block of time to query. Use either a timestamp range (using start_time and end_time) or a specified month/year combo (using month and year).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import stats_api
from fastly.model.stats import Stats
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
    api_instance = stats_api.StatsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    month = "05" # str | 2-digit month. (optional)
    year = "2020" # str | 4-digit year. (optional)
    start_time = 1608560817 # int | Epoch timestamp. Limits the results returned. (optional)
    end_time = 1608560817 # int | Epoch timestamp. Limits the results returned. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get stats for a service
        api_response = api_instance.get_service_stats(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling StatsApi->get_service_stats: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get stats for a service
        api_response = api_instance.get_service_stats(service_id, month=month, year=year, start_time=start_time, end_time=end_time)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling StatsApi->get_service_stats: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **month** | **str**| 2-digit month. | [optional]
 **year** | **str**| 4-digit year. | [optional]
 **start_time** | **int**| Epoch timestamp. Limits the results returned. | [optional]
 **end_time** | **int**| Epoch timestamp. Limits the results returned. | [optional]

### Return type

[**Stats**](Stats.md)

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

