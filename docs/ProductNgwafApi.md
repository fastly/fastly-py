# fastly.ProductNgwafApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_product_ngwaf**](ProductNgwafApi.md#disable_product_ngwaf) | **DELETE** /enabled-products/v1/ngwaf/services/{service_id} | Disable product
[**enable_product_ngwaf**](ProductNgwafApi.md#enable_product_ngwaf) | **PUT** /enabled-products/v1/ngwaf/services/{service_id} | Enable product
[**get_product_ngwaf**](ProductNgwafApi.md#get_product_ngwaf) | **GET** /enabled-products/v1/ngwaf/services/{service_id} | Get product enablement status
[**get_product_ngwaf_configuration**](ProductNgwafApi.md#get_product_ngwaf_configuration) | **GET** /enabled-products/v1/ngwaf/services/{service_id}/configuration | Get configuration
[**set_product_ngwaf_configuration**](ProductNgwafApi.md#set_product_ngwaf_configuration) | **PATCH** /enabled-products/v1/ngwaf/services/{service_id}/configuration | Update configuration


# **disable_product_ngwaf**
> disable_product_ngwaf(service_id)

Disable product

Disable the Next-Gen WAF product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ngwaf_api
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
    api_instance = product_ngwaf_api.ProductNgwafApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Disable product
        api_instance.disable_product_ngwaf(service_id)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->disable_product_ngwaf: %s\n" % e)
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

# **enable_product_ngwaf**
> NgwafResponseEnable enable_product_ngwaf(service_id)

Enable product

Enable the Next-Gen WAF product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ngwaf_api
from fastly.model.ngwaf_response_enable import NgwafResponseEnable
from fastly.model.ngwaf_request_enable import NgwafRequestEnable
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
    api_instance = product_ngwaf_api.ProductNgwafApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    ngwaf_request_enable = NgwafRequestEnable(
        workspace_id="workspace_id_example",
    ) # NgwafRequestEnable |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enable product
        api_response = api_instance.enable_product_ngwaf(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->enable_product_ngwaf: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable product
        api_response = api_instance.enable_product_ngwaf(service_id, ngwaf_request_enable=ngwaf_request_enable)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->enable_product_ngwaf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **ngwaf_request_enable** | [**NgwafRequestEnable**](NgwafRequestEnable.md)|  | [optional]

### Return type

[**NgwafResponseEnable**](NgwafResponseEnable.md)

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

# **get_product_ngwaf**
> NgwafResponseEnable get_product_ngwaf(service_id)

Get product enablement status

Get the enablement status of the Next-Gen WAF product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ngwaf_api
from fastly.model.ngwaf_response_enable import NgwafResponseEnable
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
    api_instance = product_ngwaf_api.ProductNgwafApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get product enablement status
        api_response = api_instance.get_product_ngwaf(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->get_product_ngwaf: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**NgwafResponseEnable**](NgwafResponseEnable.md)

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

# **get_product_ngwaf_configuration**
> NgwafResponseConfigure get_product_ngwaf_configuration(service_id)

Get configuration

Get configuration of the Next-Gen WAF product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ngwaf_api
from fastly.model.ngwaf_response_configure import NgwafResponseConfigure
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
    api_instance = product_ngwaf_api.ProductNgwafApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get configuration
        api_response = api_instance.get_product_ngwaf_configuration(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->get_product_ngwaf_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**NgwafResponseConfigure**](NgwafResponseConfigure.md)

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

# **set_product_ngwaf_configuration**
> NgwafResponseConfigure set_product_ngwaf_configuration(service_id)

Update configuration

Update configuration of the Next-Gen WAF product on a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ngwaf_api
from fastly.model.ngwaf_request_update_configuration import NgwafRequestUpdateConfiguration
from fastly.model.ngwaf_response_configure import NgwafResponseConfigure
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
    api_instance = product_ngwaf_api.ProductNgwafApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    ngwaf_request_update_configuration = NgwafRequestUpdateConfiguration(
        workspace_id="workspace_id_example",
        traffic_ramp="traffic_ramp_example",
    ) # NgwafRequestUpdateConfiguration |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update configuration
        api_response = api_instance.set_product_ngwaf_configuration(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->set_product_ngwaf_configuration: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update configuration
        api_response = api_instance.set_product_ngwaf_configuration(service_id, ngwaf_request_update_configuration=ngwaf_request_update_configuration)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductNgwafApi->set_product_ngwaf_configuration: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **ngwaf_request_update_configuration** | [**NgwafRequestUpdateConfiguration**](NgwafRequestUpdateConfiguration.md)|  | [optional]

### Return type

[**NgwafResponseConfigure**](NgwafResponseConfigure.md)

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

