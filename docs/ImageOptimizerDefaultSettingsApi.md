# fastly.ImageOptimizerDefaultSettingsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_default_settings**](ImageOptimizerDefaultSettingsApi.md#get_default_settings) | **GET** /service/{service_id}/version/{version_id}/image_optimizer_default_settings | Get current Image Optimizer Default Settings
[**update_default_settings**](ImageOptimizerDefaultSettingsApi.md#update_default_settings) | **PATCH** /service/{service_id}/version/{version_id}/image_optimizer_default_settings | Update Image Optimizer Default Settings


# **get_default_settings**
> DefaultSettingsResponse get_default_settings(service_id, version_id)

Get current Image Optimizer Default Settings

Retrieve the current Image Optimizer default settings. All properties in the response will be populated. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import image_optimizer_default_settings_api
from fastly.model.default_settings_error import DefaultSettingsError
from fastly.model.default_settings_response import DefaultSettingsResponse
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
    api_instance = image_optimizer_default_settings_api.ImageOptimizerDefaultSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get current Image Optimizer Default Settings
        api_response = api_instance.get_default_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ImageOptimizerDefaultSettingsApi->get_default_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**DefaultSettingsResponse**](DefaultSettingsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**404** | This service does not have image optimizer settings. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_default_settings**
> DefaultSettingsResponse update_default_settings(service_id, version_id)

Update Image Optimizer Default Settings

Update one or more default settings. A minimum of one property is required. The endpoint will respond with the new Image Optimizer default settings, with all properties populated. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import image_optimizer_default_settings_api
from fastly.model.default_settings_error import DefaultSettingsError
from fastly.model.default_settings import DefaultSettings
from fastly.model.default_settings_response import DefaultSettingsResponse
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
    api_instance = image_optimizer_default_settings_api.ImageOptimizerDefaultSettingsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    default_settings = DefaultSettings(
        resize_filter="lanczos3",
        webp=False,
        webp_quality=85,
        jpeg_type="auto",
        jpeg_quality=85,
        upscale=False,
        allow_video=False,
    ) # DefaultSettings |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update Image Optimizer Default Settings
        api_response = api_instance.update_default_settings(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ImageOptimizerDefaultSettingsApi->update_default_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update Image Optimizer Default Settings
        api_response = api_instance.update_default_settings(service_id, version_id, default_settings=default_settings)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ImageOptimizerDefaultSettingsApi->update_default_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **default_settings** | [**DefaultSettings**](DefaultSettings.md)|  | [optional]

### Return type

[**DefaultSettingsResponse**](DefaultSettingsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Request parameters are invalid |  -  |
**403** | Not authorized to change one or more settings. No changes have been applied. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

