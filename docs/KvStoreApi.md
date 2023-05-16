# fastly.KvStoreApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_store**](KvStoreApi.md#create_store) | **POST** /resources/stores/kv | Create an kv store.
[**delete_store**](KvStoreApi.md#delete_store) | **DELETE** /resources/stores/kv/{store_id} | Delete an kv store.
[**get_store**](KvStoreApi.md#get_store) | **GET** /resources/stores/kv/{store_id} | Describe an kv store.
[**get_stores**](KvStoreApi.md#get_stores) | **GET** /resources/stores/kv | List kv stores.


# **create_store**
> StoreResponse create_store()

Create an kv store.

Create a new kv store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
from fastly.model.store_response import StoreResponse
from fastly.model.store import Store
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
    api_instance = kv_store_api.KvStoreApi(api_client)
    location = "location_example" # str |  (optional)
    store = Store(
        name="name_example",
    ) # Store |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an kv store.
        api_response = api_instance.create_store(location=location, store=store)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->create_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**|  | [optional]
 **store** | [**Store**](Store.md)|  | [optional]

### Return type

[**StoreResponse**](StoreResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store**
> delete_store(store_id)

Delete an kv store.

An kv store must be empty before it can be deleted.  Deleting an kv store that still contains keys will result in a `409` (Conflict).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
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
    api_instance = kv_store_api.KvStoreApi(api_client)
    store_id = "store_id_example" # str | 
    force = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete an kv store.
        api_instance.delete_store(store_id)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->delete_store: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an kv store.
        api_instance.delete_store(store_id, force=force)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->delete_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **force** | **bool**|  | [optional]

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

# **get_store**
> StoreResponse get_store(store_id)

Describe an kv store.

Get an kv store by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
from fastly.model.store_response import StoreResponse
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
    api_instance = kv_store_api.KvStoreApi(api_client)
    store_id = "store_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Describe an kv store.
        api_response = api_instance.get_store(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->get_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |

### Return type

[**StoreResponse**](StoreResponse.md)

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

# **get_stores**
> InlineResponse2002 get_stores()

List kv stores.

Get all stores for a given customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
from fastly.model.inline_response2002 import InlineResponse2002
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
    api_instance = kv_store_api.KvStoreApi(api_client)
    cursor = "cursor_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List kv stores.
        api_response = api_instance.get_stores(cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->get_stores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

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

