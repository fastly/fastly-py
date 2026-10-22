# fastly.ProductAiRuntimeControlApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_product_ai_runtime_control**](ProductAiRuntimeControlApi.md#disable_product_ai_runtime_control) | **DELETE** /enabled-products/v1/ai_runtime_control | Disable product
[**enable_product_ai_runtime_control**](ProductAiRuntimeControlApi.md#enable_product_ai_runtime_control) | **PUT** /enabled-products/v1/ai_runtime_control | Enable product
[**get_product_ai_runtime_control**](ProductAiRuntimeControlApi.md#get_product_ai_runtime_control) | **GET** /enabled-products/v1/ai_runtime_control | Get product enablement status


# **disable_product_ai_runtime_control**
> disable_product_ai_runtime_control()

Disable product

Disable the AI Runtime Control product

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ai_runtime_control_api
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
    api_instance = product_ai_runtime_control_api.ProductAiRuntimeControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable product
        api_instance.disable_product_ai_runtime_control()
    except fastly.ApiException as e:
        print("Exception when calling ProductAiRuntimeControlApi->disable_product_ai_runtime_control: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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

# **enable_product_ai_runtime_control**
> AiRuntimeControlResponseBodyEnable enable_product_ai_runtime_control()

Enable product

Enable the AI Runtime Control product

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ai_runtime_control_api
from fastly.model.ai_runtime_control_response_body_enable import AiRuntimeControlResponseBodyEnable
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
    api_instance = product_ai_runtime_control_api.ProductAiRuntimeControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enable product
        api_response = api_instance.enable_product_ai_runtime_control()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductAiRuntimeControlApi->enable_product_ai_runtime_control: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AiRuntimeControlResponseBodyEnable**](AiRuntimeControlResponseBodyEnable.md)

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

# **get_product_ai_runtime_control**
> AiRuntimeControlResponseBodyEnable get_product_ai_runtime_control()

Get product enablement status

Get the enablement status of the AI Runtime Control product

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_ai_runtime_control_api
from fastly.model.ai_runtime_control_response_body_enable import AiRuntimeControlResponseBodyEnable
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
    api_instance = product_ai_runtime_control_api.ProductAiRuntimeControlApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get product enablement status
        api_response = api_instance.get_product_ai_runtime_control()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductAiRuntimeControlApi->get_product_ai_runtime_control: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AiRuntimeControlResponseBodyEnable**](AiRuntimeControlResponseBodyEnable.md)

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

