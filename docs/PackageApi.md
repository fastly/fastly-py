# fastly.PackageApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_package**](PackageApi.md#get_package) | **GET** /service/{service_id}/version/{version_id}/package | Get details of the service&#39;s Compute package.
[**put_package**](PackageApi.md#put_package) | **PUT** /service/{service_id}/version/{version_id}/package | Upload a Compute package.


# **get_package**
> PackageResponse get_package(service_id, version_id)

Get details of the service's Compute package.

List detailed information about the Compute package for the specified service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import package_api
from fastly.model.package_response import PackageResponse
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
    api_instance = package_api.PackageApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get details of the service's Compute package.
        api_response = api_instance.get_package(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PackageApi->get_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**PackageResponse**](PackageResponse.md)

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

# **put_package**
> PackageResponse put_package(service_id, version_id)

Upload a Compute package.

Upload a Compute package associated with the specified service version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import package_api
from fastly.model.package_response import PackageResponse
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
    api_instance = package_api.PackageApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    expect = "100-continue" # str | We recommend using the Expect header because it may identify issues with the request based upon the headers alone instead of requiring you to wait until the entire binary package upload has completed. (optional)
    package = open('/path/to/file', 'rb') # file_type | The content of the Wasm binary package. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Upload a Compute package.
        api_response = api_instance.put_package(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PackageApi->put_package: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a Compute package.
        api_response = api_instance.put_package(service_id, version_id, expect=expect, package=package)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PackageApi->put_package: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **expect** | **str**| We recommend using the Expect header because it may identify issues with the request based upon the headers alone instead of requiring you to wait until the entire binary package upload has completed. | [optional]
 **package** | **file_type**| The content of the Wasm binary package. | [optional]

### Return type

[**PackageResponse**](PackageResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

