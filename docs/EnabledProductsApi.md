# fastly.EnabledProductsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_product**](EnabledProductsApi.md#disable_product) | **DELETE** /enabled-products/v1/{product_id}/services/{service_id} | Disable a product
[**enable_product**](EnabledProductsApi.md#enable_product) | **PUT** /enabled-products/v1/{product_id}/services/{service_id} | Enable a product
[**get_enabled_product**](EnabledProductsApi.md#get_enabled_product) | **GET** /enabled-products/v1/{product_id}/services/{service_id} | Get enabled product
[**get_product_configuration**](EnabledProductsApi.md#get_product_configuration) | **GET** /enabled-products/v1/{product_id}/services/{service_id}/configuration | Get configuration for a product
[**set_product_configuration**](EnabledProductsApi.md#set_product_configuration) | **PATCH** /enabled-products/v1/{product_id}/services/{service_id}/configuration | Update configuration for a product


# **disable_product**
> disable_product(product_id, service_id)

Disable a product

Disable a product on a service. Supported product IDs: `brotli_compression`,`domain_inspector`,`fanout`,`image_optimizer`,`origin_inspector`, `websockets`, `bot_management`, and `ngwaf`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import enabled_products_api
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
    api_instance = enabled_products_api.EnabledProductsApi(api_client)
    product_id = "ngwaf" # str | 
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Disable a product
        api_instance.disable_product(product_id, service_id)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->disable_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
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

# **enable_product**
> EnabledProductResponse enable_product(product_id, service_id)

Enable a product

Enable a product on a service. Supported product IDs: `brotli_compression`,`domain_inspector`,`fanout`,`image_optimizer`,`origin_inspector`, `websockets`, `bot_management`, and `ngwaf`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import enabled_products_api
from fastly.model.enabled_product_response import EnabledProductResponse
from fastly.model.set_workspace_id import SetWorkspaceId
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
    api_instance = enabled_products_api.EnabledProductsApi(api_client)
    product_id = "ngwaf" # str | 
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    set_workspace_id = SetWorkspaceId(
        workspace_id="workspace_id_example",
    ) # SetWorkspaceId |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enable a product
        api_response = api_instance.enable_product(product_id, service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->enable_product: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable a product
        api_response = api_instance.enable_product(product_id, service_id, set_workspace_id=set_workspace_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->enable_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **set_workspace_id** | [**SetWorkspaceId**](SetWorkspaceId.md)|  | [optional]

### Return type

[**EnabledProductResponse**](EnabledProductResponse.md)

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

# **get_enabled_product**
> EnabledProductResponse get_enabled_product(product_id, service_id)

Get enabled product

Get enabled product on a service. Supported product IDs: `brotli_compression`,`domain_inspector`,`fanout`,`image_optimizer`,`origin_inspector`, `websockets`, `bot_management`, and `ngwaf`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import enabled_products_api
from fastly.model.enabled_product_response import EnabledProductResponse
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
    api_instance = enabled_products_api.EnabledProductsApi(api_client)
    product_id = "ngwaf" # str | 
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get enabled product
        api_response = api_instance.get_enabled_product(product_id, service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->get_enabled_product: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**EnabledProductResponse**](EnabledProductResponse.md)

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

# **get_product_configuration**
> ConfiguredProductResponse get_product_configuration(product_id, service_id)

Get configuration for a product

Get configuration for an enabled product on a service. Supported product IDs: `ngwaf`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import enabled_products_api
from fastly.model.configured_product_response import ConfiguredProductResponse
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
    api_instance = enabled_products_api.EnabledProductsApi(api_client)
    product_id = "ngwaf" # str | 
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get configuration for a product
        api_response = api_instance.get_product_configuration(product_id, service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->get_product_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**ConfiguredProductResponse**](ConfiguredProductResponse.md)

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

# **set_product_configuration**
> ConfiguredProductResponse set_product_configuration(product_id, service_id)

Update configuration for a product

Update configuration for an enabled product on a service. Supported product IDs: `ngwaf`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import enabled_products_api
from fastly.model.configured_product_response import ConfiguredProductResponse
from fastly.model.set_configuration import SetConfiguration
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
    api_instance = enabled_products_api.EnabledProductsApi(api_client)
    product_id = "ngwaf" # str | 
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    set_configuration = SetConfiguration(
        workspace_id="workspace_id_example",
        traffic_ramp="traffic_ramp_example",
    ) # SetConfiguration |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update configuration for a product
        api_response = api_instance.set_product_configuration(product_id, service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->set_product_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update configuration for a product
        api_response = api_instance.set_product_configuration(product_id, service_id, set_configuration=set_configuration)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling EnabledProductsApi->set_product_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**|  |
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **set_configuration** | [**SetConfiguration**](SetConfiguration.md)|  | [optional]

### Return type

[**ConfiguredProductResponse**](ConfiguredProductResponse.md)

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

