# fastly.LoggingEndpointErrorsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_log_endpoint_errors**](LoggingEndpointErrorsApi.md#get_log_endpoint_errors) | **GET** /observability/service/{service_id}/logging/errors | Stream Log Endpoint Errors


# **get_log_endpoint_errors**
> str get_log_endpoint_errors(service_id)

Stream Log Endpoint Errors

Provides a near real-time stream of log errors through a hybrid short-polling model. A client should make an initial request using the `from` parameter to specify a start time. The `to` parameter should be used alongside the `from` parameter since the default bucket is 10 seconds.  For pagination, use the URLs provided in the Link header of the response. These contain updated `from` timestamps for retrieving the next or previous page of logs.  Defaults to `application/x-ndjson` format. Use `Accept: application/json` header to request standard JSON array format instead. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_endpoint_errors_api
from fastly.model.error_response import ErrorResponse
from fastly.model.log_error_batch import LogErrorBatch
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
    api_instance = logging_endpoint_errors_api.LoggingEndpointErrorsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | 
    _from = 1756123200 # int |  (optional)
    to = 1756209600 # int |  (optional)
    filter_endpoint = "MyS3,BigQuery" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Stream Log Endpoint Errors
        api_response = api_instance.get_log_endpoint_errors(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingEndpointErrorsApi->get_log_endpoint_errors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Stream Log Endpoint Errors
        api_response = api_instance.get_log_endpoint_errors(service_id, _from=_from, to=to, filter_endpoint=filter_endpoint)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingEndpointErrorsApi->get_log_endpoint_errors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**|  |
 **_from** | **int**|  | [optional]
 **to** | **int**|  | [optional]
 **filter_endpoint** | **str**|  | [optional]

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/x-ndjson, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stream of log endpoint errors |  * Content-Type - Response content type <br>  * Link - RFC 8288-compliant links for pagination using time-based parameters <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

