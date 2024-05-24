# fastly.SettingsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_settings**](SettingsApi.md#get_service_settings) | **GET** /service/{service_id}/version/{version_id}/settings | Get service settings
[**update_service_settings**](SettingsApi.md#update_service_settings) | **PUT** /service/{service_id}/version/{version_id}/settings | Update service settings


# **get_service_settings**
> SettingsResponse get_service_settings(service_id, version_id)

Get service settings

Get the settings for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import settings_api
from fastly.model.settings_response import SettingsResponse
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
    api_instance = settings_api.SettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get service settings
        api_response = api_instance.get_service_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SettingsApi->get_service_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**SettingsResponse**](SettingsResponse.md)

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

# **update_service_settings**
> SettingsResponse update_service_settings(service_id, version_id)

Update service settings

Update the settings for a particular service and version. NOTE: If you override TTLs with custom VCL, any general.default_ttl value will not be honored and the expected behavior may change. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import settings_api
from fastly.model.settings_response import SettingsResponse
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
    api_instance = settings_api.SettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    general_default_host = "general_default_host_example" # str | The default host name for the version. (optional)
    general_default_ttl = 1 # int | The default time-to-live (TTL) for the version. (optional)
    general_stale_if_error = False # bool | Enables serving a stale object if there is an error. (optional) if omitted the server will use the default value of False
    general_stale_if_error_ttl = 43200 # int | The default time-to-live (TTL) for serving the stale object for the version. (optional) if omitted the server will use the default value of 43200

    # example passing only required values which don't have defaults set
    try:
        # Update service settings
        api_response = api_instance.update_service_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SettingsApi->update_service_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update service settings
        api_response = api_instance.update_service_settings(service_id, version_id, general_default_host=general_default_host, general_default_ttl=general_default_ttl, general_stale_if_error=general_stale_if_error, general_stale_if_error_ttl=general_stale_if_error_ttl)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SettingsApi->update_service_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **general_default_host** | **str**| The default host name for the version. | [optional]
 **general_default_ttl** | **int**| The default time-to-live (TTL) for the version. | [optional]
 **general_stale_if_error** | **bool**| Enables serving a stale object if there is an error. | [optional] if omitted the server will use the default value of False
 **general_stale_if_error_ttl** | **int**| The default time-to-live (TTL) for serving the stale object for the version. | [optional] if omitted the server will use the default value of 43200

### Return type

[**SettingsResponse**](SettingsResponse.md)

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

