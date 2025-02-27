# fastly.ProductDdosProtectionApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_product_ddos_protection**](ProductDdosProtectionApi.md#disable_product_ddos_protection) | **DELETE** /enabled-products/v1/ddos_protection/services/{service_id} | Disable product
[**enable_product_ddos_protection**](ProductDdosProtectionApi.md#enable_product_ddos_protection) | **PUT** /enabled-products/v1/ddos_protection/services/{service_id} | Enable product
[**get_product_ddos_protection**](ProductDdosProtectionApi.md#get_product_ddos_protection) | **GET** /enabled-products/v1/ddos_protection/services/{service_id} | Get product enablement status
[**get_product_ddos_protection_configuration**](ProductDdosProtectionApi.md#get_product_ddos_protection_configuration) | **GET** /enabled-products/v1/ddos_protection/services/{service_id}/configuration | Get configuration
[**set_product_ddos_protection_configuration**](ProductDdosProtectionApi.md#set_product_ddos_protection_configuration) | **PATCH** /enabled-products/v1/ddos_protection/services/{service_id}/configuration | Update configuration


# **disable_product_ddos_protection**
> disable_product_ddos_protection(service_id)

Disable product

Disable the DDoS Protection product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ddos_protection_api
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
    api_instance = product_ddos_protection_api.ProductDdosProtectionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Disable product
        api_instance.disable_product_ddos_protection(service_id)
    except fastly.ApiException as e:
        print("Exception when calling ProductDdosProtectionApi->disable_product_ddos_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_product_ddos_protection**
> DdosProtectionResponseEnable enable_product_ddos_protection(service_id)

Enable product

Enable the DDoS Protection product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ddos_protection_api
from fastly.model.ddos_protection_response_enable import DdosProtectionResponseEnable
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
    api_instance = product_ddos_protection_api.ProductDdosProtectionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Enable product
        api_response = api_instance.enable_product_ddos_protection(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDdosProtectionApi->enable_product_ddos_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**DdosProtectionResponseEnable**](DdosProtectionResponseEnable.md)

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

# **get_product_ddos_protection**
> DdosProtectionResponseEnable get_product_ddos_protection(service_id)

Get product enablement status

Get the enablement status of the DDoS Protection product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ddos_protection_api
from fastly.model.ddos_protection_response_enable import DdosProtectionResponseEnable
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
    api_instance = product_ddos_protection_api.ProductDdosProtectionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get product enablement status
        api_response = api_instance.get_product_ddos_protection(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDdosProtectionApi->get_product_ddos_protection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**DdosProtectionResponseEnable**](DdosProtectionResponseEnable.md)

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

# **get_product_ddos_protection_configuration**
> DdosProtectionResponseConfigure get_product_ddos_protection_configuration(service_id)

Get configuration

Get configuration of the DDoS Protection product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ddos_protection_api
from fastly.model.ddos_protection_response_configure import DdosProtectionResponseConfigure
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
    api_instance = product_ddos_protection_api.ProductDdosProtectionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get configuration
        api_response = api_instance.get_product_ddos_protection_configuration(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDdosProtectionApi->get_product_ddos_protection_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**DdosProtectionResponseConfigure**](DdosProtectionResponseConfigure.md)

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

# **set_product_ddos_protection_configuration**
> DdosProtectionResponseConfigure set_product_ddos_protection_configuration(service_id)

Update configuration

Update configuration of the DDoS Protection product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ddos_protection_api
from fastly.model.ddos_protection_request_update_configuration import DdosProtectionRequestUpdateConfiguration
from fastly.model.ddos_protection_response_configure import DdosProtectionResponseConfigure
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
    api_instance = product_ddos_protection_api.ProductDdosProtectionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    ddos_protection_request_update_configuration = DdosProtectionRequestUpdateConfiguration(
        mode="false",
    ) # DdosProtectionRequestUpdateConfiguration |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update configuration
        api_response = api_instance.set_product_ddos_protection_configuration(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDdosProtectionApi->set_product_ddos_protection_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update configuration
        api_response = api_instance.set_product_ddos_protection_configuration(service_id, ddos_protection_request_update_configuration=ddos_protection_request_update_configuration)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDdosProtectionApi->set_product_ddos_protection_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **ddos_protection_request_update_configuration** | [**DdosProtectionRequestUpdateConfiguration**](DdosProtectionRequestUpdateConfiguration.md)|  | [optional]

### Return type

[**DdosProtectionResponseConfigure**](DdosProtectionResponseConfigure.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

