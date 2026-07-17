# fastly.ProductKvStoreApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**disable_product_kv_store**](ProductKvStoreApi.md#disable_product_kv_store) | **DELETE** /enabled-products/v1/kv_store | Disable product
[**enable_kv_store**](ProductKvStoreApi.md#enable_kv_store) | **PUT** /enabled-products/v1/kv_store | Enable product
[**get_kv_store**](ProductKvStoreApi.md#get_kv_store) | **GET** /enabled-products/v1/kv_store | Get product enablement status


# **disable_product_kv_store**
> disable_product_kv_store()

Disable product

Disable the KV Store product

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_kv_store_api
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
    api_instance = product_kv_store_api.ProductKvStoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Disable product
        api_instance.disable_product_kv_store()
    except fastly.ApiException as e:
        print("Exception when calling ProductKvStoreApi->disable_product_kv_store: %s\n" % e)
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

# **enable_kv_store**
> KvStoreResponseBodyEnable enable_kv_store()

Enable product

Enable the KV Store product

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_kv_store_api
from fastly.model.kv_store_response_body_enable import KvStoreResponseBodyEnable
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
    api_instance = product_kv_store_api.ProductKvStoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Enable product
        api_response = api_instance.enable_kv_store()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductKvStoreApi->enable_kv_store: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**KvStoreResponseBodyEnable**](KvStoreResponseBodyEnable.md)

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

# **get_kv_store**
> KvStoreResponseBodyEnable get_kv_store()

Get product enablement status

Get the enablement status of the KV Store product

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import product_kv_store_api
from fastly.model.kv_store_response_body_enable import KvStoreResponseBodyEnable
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
    api_instance = product_kv_store_api.ProductKvStoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get product enablement status
        api_response = api_instance.get_kv_store()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ProductKvStoreApi->get_kv_store: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**KvStoreResponseBodyEnable**](KvStoreResponseBodyEnable.md)

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

