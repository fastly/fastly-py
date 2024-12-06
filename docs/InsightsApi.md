# fastly.InsightsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_insights**](InsightsApi.md#get_log_insights) | **GET** /observability/log-insights | Retrieve log insights


# **get_log_insights**
> GetLogInsightsResponse get_log_insights(visualization, service_id, start, end)

Retrieve log insights

Retrieves statistics from sampled log records.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import insights_api
from fastly.model.get_log_insights_response import GetLogInsightsResponse
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
    api_instance = insights_api.InsightsApi(api_client)
    visualization = "top-url-by-bandwidth" # str | 
    service_id = "service_id_example" # str | 
    start = "start_example" # str | 
    end = "end_example" # str | 
    pops = "pops_example" # str |  (optional)
    domain = "domain_example" # str |  (optional)
    domain_exact_match = True # bool |  (optional)
    limit = 3.14 # float |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve log insights
        api_response = api_instance.get_log_insights(visualization, service_id, start, end)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling InsightsApi->get_log_insights: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve log insights
        api_response = api_instance.get_log_insights(visualization, service_id, start, end, pops=pops, domain=domain, domain_exact_match=domain_exact_match, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling InsightsApi->get_log_insights: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **visualization** | **str**|  |
 **service_id** | **str**|  |
 **start** | **str**|  |
 **end** | **str**|  |
 **pops** | **str**|  | [optional]
 **domain** | **str**|  | [optional]
 **domain_exact_match** | **bool**|  | [optional]
 **limit** | **float**|  | [optional]

### Return type

[**GetLogInsightsResponse**](GetLogInsightsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves log insights for the specified service and visualization. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

