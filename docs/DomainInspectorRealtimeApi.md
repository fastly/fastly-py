# fastly.DomainInspectorRealtimeApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_domain_inspector_last120_seconds**](DomainInspectorRealtimeApi.md#get_domain_inspector_last120_seconds) | **GET** /v1/domains/{service_id}/ts/h | Get real-time domain data for the last 120 seconds
[**get_domain_inspector_last_max_entries**](DomainInspectorRealtimeApi.md#get_domain_inspector_last_max_entries) | **GET** /v1/domains/{service_id}/ts/h/limit/{max_entries} | Get a limited number of real-time domain data entries
[**get_domain_inspector_last_second**](DomainInspectorRealtimeApi.md#get_domain_inspector_last_second) | **GET** /v1/domains/{service_id}/ts/{start_timestamp} | Get real-time domain data from a specified time


# **get_domain_inspector_last120_seconds**
> DomainInspector get_domain_inspector_last120_seconds(service_id)

Get real-time domain data for the last 120 seconds

Get data for the 120 seconds preceding the latest timestamp available for a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_inspector_realtime_api
from fastly.model.domain_inspector import DomainInspector
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
    api_instance = domain_inspector_realtime_api.DomainInspectorRealtimeApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get real-time domain data for the last 120 seconds
        api_response = api_instance.get_domain_inspector_last120_seconds(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainInspectorRealtimeApi->get_domain_inspector_last120_seconds: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**DomainInspector**](DomainInspector.md)

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

# **get_domain_inspector_last_max_entries**
> DomainInspector get_domain_inspector_last_max_entries(service_id, max_entries)

Get a limited number of real-time domain data entries

Get data for the `max_entries` seconds preceding the latest timestamp available for a service, up to a maximum of 120 entries.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_inspector_realtime_api
from fastly.model.domain_inspector import DomainInspector
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
    api_instance = domain_inspector_realtime_api.DomainInspectorRealtimeApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    max_entries = 1 # int | Maximum number of results to show.

    # example passing only required values which don't have defaults set
    try:
        # Get a limited number of real-time domain data entries
        api_response = api_instance.get_domain_inspector_last_max_entries(service_id, max_entries)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainInspectorRealtimeApi->get_domain_inspector_last_max_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **max_entries** | **int**| Maximum number of results to show. |

### Return type

[**DomainInspector**](DomainInspector.md)

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

# **get_domain_inspector_last_second**
> DomainInspector get_domain_inspector_last_second(service_id, start_timestamp)

Get real-time domain data from a specified time

Get real-time domain data for the specified reporting period. Specify `0` to get a single entry for the last complete second. The `Timestamp` field included in the response provides the time index of the latest entry in the dataset and can be provided as the `start_timestamp` of the next request for a seamless continuation of the dataset from one request to the next. Due to processing latency, the earliest entry in the response dataset may be earlier than `start_timestamp` by the value of `AggregateDelay`. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_inspector_realtime_api
from fastly.model.domain_inspector import DomainInspector
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
    api_instance = domain_inspector_realtime_api.DomainInspectorRealtimeApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    start_timestamp = 1608560817 # int | Timestamp in seconds (Unix epoch time).

    # example passing only required values which don't have defaults set
    try:
        # Get real-time domain data from a specified time
        api_response = api_instance.get_domain_inspector_last_second(service_id, start_timestamp)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainInspectorRealtimeApi->get_domain_inspector_last_second: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **start_timestamp** | **int**| Timestamp in seconds (Unix epoch time). |

### Return type

[**DomainInspector**](DomainInspector.md)

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

