# fastly.RequestSettingsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_request_settings**](RequestSettingsApi.md#create_request_settings) | **POST** /service/{service_id}/version/{version_id}/request_settings | Create a Request Settings object
[**delete_request_settings**](RequestSettingsApi.md#delete_request_settings) | **DELETE** /service/{service_id}/version/{version_id}/request_settings/{request_settings_name} | Delete a Request Settings object
[**get_request_settings**](RequestSettingsApi.md#get_request_settings) | **GET** /service/{service_id}/version/{version_id}/request_settings/{request_settings_name} | Get a Request Settings object
[**list_request_settings**](RequestSettingsApi.md#list_request_settings) | **GET** /service/{service_id}/version/{version_id}/request_settings | List Request Settings objects
[**update_request_settings**](RequestSettingsApi.md#update_request_settings) | **PUT** /service/{service_id}/version/{version_id}/request_settings/{request_settings_name} | Update a Request Settings object


# **create_request_settings**
> RequestSettingsResponse create_request_settings(service_id, version_id)

Create a Request Settings object

Creates a new Request Settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import request_settings_api
from fastly.model.request_settings_response import RequestSettingsResponse
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
    api_instance = request_settings_api.RequestSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Create a Request Settings object
        api_response = api_instance.create_request_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RequestSettingsApi->create_request_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**RequestSettingsResponse**](RequestSettingsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_request_settings**
> InlineResponse200 delete_request_settings(service_id, version_id, request_settings_name)

Delete a Request Settings object

Removes the specified Request Settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import request_settings_api
from fastly.model.inline_response200 import InlineResponse200
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
    api_instance = request_settings_api.RequestSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    request_settings_name = "test-request-setting" # str | Name for the request settings.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Request Settings object
        api_response = api_instance.delete_request_settings(service_id, version_id, request_settings_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RequestSettingsApi->delete_request_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **request_settings_name** | **str**| Name for the request settings. |

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **get_request_settings**
> RequestSettingsResponse get_request_settings(service_id, version_id, request_settings_name)

Get a Request Settings object

Gets the specified Request Settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import request_settings_api
from fastly.model.request_settings_response import RequestSettingsResponse
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
    api_instance = request_settings_api.RequestSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    request_settings_name = "test-request-setting" # str | Name for the request settings.

    # example passing only required values which don't have defaults set
    try:
        # Get a Request Settings object
        api_response = api_instance.get_request_settings(service_id, version_id, request_settings_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RequestSettingsApi->get_request_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **request_settings_name** | **str**| Name for the request settings. |

### Return type

[**RequestSettingsResponse**](RequestSettingsResponse.md)

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

# **list_request_settings**
> [RequestSettingsResponse] list_request_settings(service_id, version_id)

List Request Settings objects

Returns a list of all Request Settings objects for the given service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import request_settings_api
from fastly.model.request_settings_response import RequestSettingsResponse
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
    api_instance = request_settings_api.RequestSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Request Settings objects
        api_response = api_instance.list_request_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RequestSettingsApi->list_request_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[RequestSettingsResponse]**](RequestSettingsResponse.md)

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

# **update_request_settings**
> RequestSettingsResponse update_request_settings(service_id, version_id, request_settings_name)

Update a Request Settings object

Updates the specified Request Settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import request_settings_api
from fastly.model.request_settings_response import RequestSettingsResponse
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
    api_instance = request_settings_api.RequestSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    request_settings_name = "test-request-setting" # str | Name for the request settings.
    action = "lookup" # str, none_type | Allows you to terminate request handling and immediately perform an action. (optional)
    default_host = "default_host_example" # str, none_type | Sets the host header. (optional)
    hash_keys = "hash_keys_example" # str, none_type | Comma separated list of varnish request object fields that should be in the hash key. (optional)
    name = "test-request-setting" # str | Name for the request settings. (optional)
    request_condition = "request_condition_example" # str, none_type | Condition which, if met, will select this configuration during a request. Optional. (optional)
    xff = "clear" # str, none_type | Short for X-Forwarded-For. (optional)
    bypass_busy_wait = 1 # int | Disable collapsed forwarding, so you don't wait for other objects to origin. (optional)
    force_miss = 1 # int | Allows you to force a cache miss for the request. Replaces the item in the cache if the content is cacheable. (optional)
    force_ssl = 1 # int | Forces the request use SSL (redirects a non-SSL to SSL). (optional)
    geo_headers = 1 # int | Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers. (optional)
    max_stale_age = 1 # int | How old an object is allowed to be to serve stale-if-error or stale-while-revalidate. (optional)
    timer_support = 1 # int | Injects the X-Timer info into the request for viewing origin fetch durations. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Request Settings object
        api_response = api_instance.update_request_settings(service_id, version_id, request_settings_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RequestSettingsApi->update_request_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Request Settings object
        api_response = api_instance.update_request_settings(service_id, version_id, request_settings_name, action=action, default_host=default_host, hash_keys=hash_keys, name=name, request_condition=request_condition, xff=xff, bypass_busy_wait=bypass_busy_wait, force_miss=force_miss, force_ssl=force_ssl, geo_headers=geo_headers, max_stale_age=max_stale_age, timer_support=timer_support)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RequestSettingsApi->update_request_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **request_settings_name** | **str**| Name for the request settings. |
 **action** | **str, none_type**| Allows you to terminate request handling and immediately perform an action. | [optional]
 **default_host** | **str, none_type**| Sets the host header. | [optional]
 **hash_keys** | **str, none_type**| Comma separated list of varnish request object fields that should be in the hash key. | [optional]
 **name** | **str**| Name for the request settings. | [optional]
 **request_condition** | **str, none_type**| Condition which, if met, will select this configuration during a request. Optional. | [optional]
 **xff** | **str, none_type**| Short for X-Forwarded-For. | [optional]
 **bypass_busy_wait** | **int**| Disable collapsed forwarding, so you don&#39;t wait for other objects to origin. | [optional]
 **force_miss** | **int**| Allows you to force a cache miss for the request. Replaces the item in the cache if the content is cacheable. | [optional]
 **force_ssl** | **int**| Forces the request use SSL (redirects a non-SSL to SSL). | [optional]
 **geo_headers** | **int**| Injects Fastly-Geo-Country, Fastly-Geo-City, and Fastly-Geo-Region into the request headers. | [optional]
 **max_stale_age** | **int**| How old an object is allowed to be to serve stale-if-error or stale-while-revalidate. | [optional]
 **timer_support** | **int**| Injects the X-Timer info into the request for viewing origin fetch durations. | [optional]

### Return type

[**RequestSettingsResponse**](RequestSettingsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

