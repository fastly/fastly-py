# fastly.AiRuntimeControlUsageMetricsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**arc_export_usage_metrics**](AiRuntimeControlUsageMetricsApi.md#arc_export_usage_metrics) | **GET** /ai-runtime-control/v1/usage-metrics/export | Export usage metrics
[**arc_get_usage_metrics**](AiRuntimeControlUsageMetricsApi.md#arc_get_usage_metrics) | **GET** /ai-runtime-control/v1/usage-metrics | Get usage metrics


# **arc_export_usage_metrics**
> ArcUsageMetricsResponse arc_export_usage_metrics()

Export usage metrics

Returns usage metrics for AI Runtime Control requests. Accepts the same filter parameters as [get usage metrics](#arc-get-usage-metrics), except `sort` and `granularity`, which aren't supported here.  Set the `Accept` header to `text/csv` to receive a CSV file download instead of a JSON response. In the CSV output, the column named `time` corresponds to the `date` field in the JSON response. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_usage_metrics_api
from fastly.model.arc_usage_metrics_response import ArcUsageMetricsResponse
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
    api_instance = ai_runtime_control_usage_metrics_api.AiRuntimeControlUsageMetricsApi(api_client)
    key = "7fVVQb1nZaJgnzCn4B4v3B" # str | Filter results to a specific virtual key ID. (optional)
    provider = "pTfnUUBcU1yv8SoRJn5PZ2" # str | Filter results by AI provider connection ID. (optional)
    model = "claude-sonnet-4-20250514" # str | Filter results by AI model identifier. (optional)
    _from = dateutil_parser('2026-09-01T00:00:00Z') # datetime | The start of the time range, in RFC 3339 format. (optional)
    to = dateutil_parser('2026-09-22T00:00:00Z') # datetime | The end of the time range, in RFC 3339 format. Defaults to now. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Export usage metrics
        api_response = api_instance.arc_export_usage_metrics(key=key, provider=provider, model=model, _from=_from, to=to)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlUsageMetricsApi->arc_export_usage_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Filter results to a specific virtual key ID. | [optional]
 **provider** | **str**| Filter results by AI provider connection ID. | [optional]
 **model** | **str**| Filter results by AI model identifier. | [optional]
 **_from** | **datetime**| The start of the time range, in RFC 3339 format. | [optional]
 **to** | **datetime**| The end of the time range, in RFC 3339 format. Defaults to now. | [optional]

### Return type

[**ArcUsageMetricsResponse**](ArcUsageMetricsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage metrics matching the request, as JSON or as a CSV file download depending on the `Accept` header. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_get_usage_metrics**
> ArcUsageMetricsResponse arc_get_usage_metrics()

Get usage metrics

Returns usage metrics for AI Runtime Control requests, including request counts, session counts, input token counts, and output token counts.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_usage_metrics_api
from fastly.model.arc_usage_metrics_response import ArcUsageMetricsResponse
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
    api_instance = ai_runtime_control_usage_metrics_api.AiRuntimeControlUsageMetricsApi(api_client)
    key = "7fVVQb1nZaJgnzCn4B4v3B" # str | Filter results to a specific virtual key ID. (optional)
    provider = "pTfnUUBcU1yv8SoRJn5PZ2" # str | Filter results by AI provider connection ID. (optional)
    model = "claude-sonnet-4-20250514" # str | Filter results by AI model identifier. (optional)
    _from = dateutil_parser('2026-09-01T00:00:00Z') # datetime | The start of the time range, in RFC 3339 format. (optional)
    to = dateutil_parser('2026-09-22T00:00:00Z') # datetime | The end of the time range, in RFC 3339 format. Defaults to now. (optional)
    granularity = "daily" # str | The time granularity to aggregate usage by. (optional) if omitted the server will use the default value of "daily"
    sort = "date" # str | Sort field. Prefix with `-` for descending order (e.g., `sort=-date`).  (optional) if omitted the server will use the default value of "date"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get usage metrics
        api_response = api_instance.arc_get_usage_metrics(key=key, provider=provider, model=model, _from=_from, to=to, granularity=granularity, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlUsageMetricsApi->arc_get_usage_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Filter results to a specific virtual key ID. | [optional]
 **provider** | **str**| Filter results by AI provider connection ID. | [optional]
 **model** | **str**| Filter results by AI model identifier. | [optional]
 **_from** | **datetime**| The start of the time range, in RFC 3339 format. | [optional]
 **to** | **datetime**| The end of the time range, in RFC 3339 format. Defaults to now. | [optional]
 **granularity** | **str**| The time granularity to aggregate usage by. | [optional] if omitted the server will use the default value of "daily"
 **sort** | **str**| Sort field. Prefix with `-` for descending order (e.g., `sort&#x3D;-date`).  | [optional] if omitted the server will use the default value of "date"

### Return type

[**ArcUsageMetricsResponse**](ArcUsageMetricsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Usage metrics matching the request. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

