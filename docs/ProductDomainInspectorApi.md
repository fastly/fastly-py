# fastly.ProductDomainInspectorApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_product_domain_inspector**](ProductDomainInspectorApi.md#disable_product_domain_inspector) | **DELETE** /enabled-products/v1/domain_inspector/services/{service_id} | Disable product
[**enable_product_domain_inspector**](ProductDomainInspectorApi.md#enable_product_domain_inspector) | **PUT** /enabled-products/v1/domain_inspector/services/{service_id} | Enable product
[**get_product_domain_inspector**](ProductDomainInspectorApi.md#get_product_domain_inspector) | **GET** /enabled-products/v1/domain_inspector/services/{service_id} | Get product enablement status


# **disable_product_domain_inspector**
> disable_product_domain_inspector(service_id)

Disable product

Disable the Domain Inspector product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_domain_inspector_api
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
    api_instance = product_domain_inspector_api.ProductDomainInspectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Disable product
        api_instance.disable_product_domain_inspector(service_id)
    except fastly.ApiException as e:
        print("Exception when calling ProductDomainInspectorApi->disable_product_domain_inspector: %s\n" % e)
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

# **enable_product_domain_inspector**
> DomainInspectorResponseBodyEnable enable_product_domain_inspector(service_id)

Enable product

Enable the Domain Inspector product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_domain_inspector_api
from fastly.model.domain_inspector_response_body_enable import DomainInspectorResponseBodyEnable
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
    api_instance = product_domain_inspector_api.ProductDomainInspectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Enable product
        api_response = api_instance.enable_product_domain_inspector(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDomainInspectorApi->enable_product_domain_inspector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**DomainInspectorResponseBodyEnable**](DomainInspectorResponseBodyEnable.md)

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

# **get_product_domain_inspector**
> DomainInspectorResponseBodyEnable get_product_domain_inspector(service_id)

Get product enablement status

Get the enablement status of the Domain Inspector product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_domain_inspector_api
from fastly.model.domain_inspector_response_body_enable import DomainInspectorResponseBodyEnable
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
    api_instance = product_domain_inspector_api.ProductDomainInspectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get product enablement status
        api_response = api_instance.get_product_domain_inspector(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductDomainInspectorApi->get_product_domain_inspector: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**DomainInspectorResponseBodyEnable**](DomainInspectorResponseBodyEnable.md)

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

