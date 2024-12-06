# fastly.LogExplorerApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_records**](LogExplorerApi.md#get_log_records) | **GET** /observability/log-explorer | Retrieve log records


# **get_log_records**
> GetLogRecordsResponse get_log_records(service_id, start, end)

Retrieve log records

Retrieves log records.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import log_explorer_api
from fastly.model.get_log_records_response import GetLogRecordsResponse
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
    api_instance = log_explorer_api.LogExplorerApi(api_client)
    service_id = "service_id_example" # str | 
    start = "start_example" # str | 
    end = "end_example" # str | 
    limit = 3.14 # float |  (optional)
    next_cursor = "next_cursor_example" # str |  (optional)
    filter = "filter_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve log records
        api_response = api_instance.get_log_records(service_id, start, end)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LogExplorerApi->get_log_records: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve log records
        api_response = api_instance.get_log_records(service_id, start, end, limit=limit, next_cursor=next_cursor, filter=filter)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LogExplorerApi->get_log_records: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  |
 **start** | **str**|  |
 **end** | **str**|  |
 **limit** | **float**|  | [optional]
 **next_cursor** | **str**|  | [optional]
 **filter** | **str**|  | [optional]

### Return type

[**GetLogRecordsResponse**](GetLogRecordsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Retrieves log records. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

