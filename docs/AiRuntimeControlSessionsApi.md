# fastly.AiRuntimeControlSessionsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**arc_get_session_logs**](AiRuntimeControlSessionsApi.md#arc_get_session_logs) | **GET** /ai-runtime-control/v1/sessions | Get session logs


# **arc_get_session_logs**
> ArcSessionsResponse arc_get_session_logs()

Get session logs

Returns session logs, including request and response data and metadata, for debugging and audit purposes.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_sessions_api
from fastly.model.arc_sessions_response import ArcSessionsResponse
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_sessions_api.AiRuntimeControlSessionsApi(api_client)
    key = "7fVVQb1nZaJgnzCn4B4v3B" # str | Filter results to a specific virtual key ID. (optional)
    provider = "pTfnUUBcU1yv8SoRJn5PZ2" # str | Filter results by AI provider connection ID. (optional)
    model = "claude-sonnet-4-20250514" # str | Filter results by AI model identifier. (optional)
    _from = dateutil_parser('2026-09-01T00:00:00Z') # datetime | The start of the time range, in RFC 3339 format. (optional)
    to = dateutil_parser('2026-09-22T00:00:00Z') # datetime | The end of the time range, in RFC 3339 format. Defaults to `now`. (optional)
    cursor = "MTAwOjA" # str | Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results, or the `prev_cursor` value to request the previous page.  (optional)
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    sort = "created_at" # str | Sort field. Prefix with `-` for descending order (e.g., `sort=-created_at`).  (optional) if omitted the server will use the default value of "created_at"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get session logs
        api_response = api_instance.arc_get_session_logs(key=key, provider=provider, model=model, _from=_from, to=to, cursor=cursor, limit=limit, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlSessionsApi->arc_get_session_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Filter results to a specific virtual key ID. | [optional]
 **provider** | **str**| Filter results by AI provider connection ID. | [optional]
 **model** | **str**| Filter results by AI model identifier. | [optional]
 **_from** | **datetime**| The start of the time range, in RFC 3339 format. | [optional]
 **to** | **datetime**| The end of the time range, in RFC 3339 format. Defaults to `now`. | [optional]
 **cursor** | **str**| Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results, or the `prev_cursor` value to request the previous page.  | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **sort** | **str**| Sort field. Prefix with `-` for descending order (e.g., `sort&#x3D;-created_at`).  | [optional] if omitted the server will use the default value of "created_at"

### Return type

[**ArcSessionsResponse**](ArcSessionsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Session logs matching the request. |  -  |
**400** | Request parameters are invalid, including an invalid or expired `cursor`. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

