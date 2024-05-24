# fastly.CacheSettingsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_cache_settings**](CacheSettingsApi.md#create_cache_settings) | **POST** /service/{service_id}/version/{version_id}/cache_settings | Create a cache settings object
[**delete_cache_settings**](CacheSettingsApi.md#delete_cache_settings) | **DELETE** /service/{service_id}/version/{version_id}/cache_settings/{cache_settings_name} | Delete a cache settings object
[**get_cache_settings**](CacheSettingsApi.md#get_cache_settings) | **GET** /service/{service_id}/version/{version_id}/cache_settings/{cache_settings_name} | Get a cache settings object
[**list_cache_settings**](CacheSettingsApi.md#list_cache_settings) | **GET** /service/{service_id}/version/{version_id}/cache_settings | List cache settings objects
[**update_cache_settings**](CacheSettingsApi.md#update_cache_settings) | **PUT** /service/{service_id}/version/{version_id}/cache_settings/{cache_settings_name} | Update a cache settings object


# **create_cache_settings**
> CacheSettingResponse create_cache_settings(service_id, version_id)

Create a cache settings object

Create a cache settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import cache_settings_api
from fastly.model.cache_setting_response import CacheSettingResponse
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
    api_instance = cache_settings_api.CacheSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    action = "pass" # str, none_type | If set, will cause vcl_fetch to terminate after processing this rule with the return state specified. If not set, other configuration logic in vcl_fetch with a lower priority will run after this rule.  (optional)
    cache_condition = "cache_condition_example" # str, none_type | Name of the cache condition controlling when this configuration applies. (optional)
    name = "test-cache-setting" # str | Name for the cache settings object. (optional)
    stale_ttl = "stale_ttl_example" # str | Maximum time in seconds to continue to use a stale version of the object if future requests to your backend server fail (also known as 'stale if error'). (optional)
    ttl = "ttl_example" # str | Maximum time to consider the object fresh in the cache (the cache 'time to live'). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a cache settings object
        api_response = api_instance.create_cache_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->create_cache_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a cache settings object
        api_response = api_instance.create_cache_settings(service_id, version_id, action=action, cache_condition=cache_condition, name=name, stale_ttl=stale_ttl, ttl=ttl)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->create_cache_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **action** | **str, none_type**| If set, will cause vcl_fetch to terminate after processing this rule with the return state specified. If not set, other configuration logic in vcl_fetch with a lower priority will run after this rule.  | [optional]
 **cache_condition** | **str, none_type**| Name of the cache condition controlling when this configuration applies. | [optional]
 **name** | **str**| Name for the cache settings object. | [optional]
 **stale_ttl** | **str**| Maximum time in seconds to continue to use a stale version of the object if future requests to your backend server fail (also known as &#39;stale if error&#39;). | [optional]
 **ttl** | **str**| Maximum time to consider the object fresh in the cache (the cache &#39;time to live&#39;). | [optional]

### Return type

[**CacheSettingResponse**](CacheSettingResponse.md)

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

# **delete_cache_settings**
> InlineResponse200 delete_cache_settings(service_id, version_id, cache_settings_name)

Delete a cache settings object

Delete a specific cache settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import cache_settings_api
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
    api_instance = cache_settings_api.CacheSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    cache_settings_name = "test-cache-setting" # str | Name for the cache settings object.

    # example passing only required values which don't have defaults set
    try:
        # Delete a cache settings object
        api_response = api_instance.delete_cache_settings(service_id, version_id, cache_settings_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->delete_cache_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **cache_settings_name** | **str**| Name for the cache settings object. |

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

# **get_cache_settings**
> CacheSettingResponse get_cache_settings(service_id, version_id, cache_settings_name)

Get a cache settings object

Get a specific cache settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import cache_settings_api
from fastly.model.cache_setting_response import CacheSettingResponse
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
    api_instance = cache_settings_api.CacheSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    cache_settings_name = "test-cache-setting" # str | Name for the cache settings object.

    # example passing only required values which don't have defaults set
    try:
        # Get a cache settings object
        api_response = api_instance.get_cache_settings(service_id, version_id, cache_settings_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->get_cache_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **cache_settings_name** | **str**| Name for the cache settings object. |

### Return type

[**CacheSettingResponse**](CacheSettingResponse.md)

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

# **list_cache_settings**
> [CacheSettingResponse] list_cache_settings(service_id, version_id)

List cache settings objects

Get a list of all cache settings for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import cache_settings_api
from fastly.model.cache_setting_response import CacheSettingResponse
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
    api_instance = cache_settings_api.CacheSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List cache settings objects
        api_response = api_instance.list_cache_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->list_cache_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[CacheSettingResponse]**](CacheSettingResponse.md)

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

# **update_cache_settings**
> CacheSettingResponse update_cache_settings(service_id, version_id, cache_settings_name)

Update a cache settings object

Update a specific cache settings object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import cache_settings_api
from fastly.model.cache_setting_response import CacheSettingResponse
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
    api_instance = cache_settings_api.CacheSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    cache_settings_name = "test-cache-setting" # str | Name for the cache settings object.
    action = "pass" # str, none_type | If set, will cause vcl_fetch to terminate after processing this rule with the return state specified. If not set, other configuration logic in vcl_fetch with a lower priority will run after this rule.  (optional)
    cache_condition = "cache_condition_example" # str, none_type | Name of the cache condition controlling when this configuration applies. (optional)
    name = "test-cache-setting" # str | Name for the cache settings object. (optional)
    stale_ttl = "stale_ttl_example" # str | Maximum time in seconds to continue to use a stale version of the object if future requests to your backend server fail (also known as 'stale if error'). (optional)
    ttl = "ttl_example" # str | Maximum time to consider the object fresh in the cache (the cache 'time to live'). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a cache settings object
        api_response = api_instance.update_cache_settings(service_id, version_id, cache_settings_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->update_cache_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a cache settings object
        api_response = api_instance.update_cache_settings(service_id, version_id, cache_settings_name, action=action, cache_condition=cache_condition, name=name, stale_ttl=stale_ttl, ttl=ttl)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CacheSettingsApi->update_cache_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **cache_settings_name** | **str**| Name for the cache settings object. |
 **action** | **str, none_type**| If set, will cause vcl_fetch to terminate after processing this rule with the return state specified. If not set, other configuration logic in vcl_fetch with a lower priority will run after this rule.  | [optional]
 **cache_condition** | **str, none_type**| Name of the cache condition controlling when this configuration applies. | [optional]
 **name** | **str**| Name for the cache settings object. | [optional]
 **stale_ttl** | **str**| Maximum time in seconds to continue to use a stale version of the object if future requests to your backend server fail (also known as &#39;stale if error&#39;). | [optional]
 **ttl** | **str**| Maximum time to consider the object fresh in the cache (the cache &#39;time to live&#39;). | [optional]

### Return type

[**CacheSettingResponse**](CacheSettingResponse.md)

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

