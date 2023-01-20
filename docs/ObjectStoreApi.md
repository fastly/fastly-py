# fastly.ObjectStoreApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_store**](ObjectStoreApi.md#create_store) | **POST** /resources/stores/object | Create an object store.
[**delete_key_from_store**](ObjectStoreApi.md#delete_key_from_store) | **DELETE** /resources/stores/object/{store_id}/keys/{key_name} | Delete object store key.
[**delete_store**](ObjectStoreApi.md#delete_store) | **DELETE** /resources/stores/object/{store_id} | Delete an object store.
[**get_keys**](ObjectStoreApi.md#get_keys) | **GET** /resources/stores/object/{store_id}/keys | List object store keys.
[**get_store**](ObjectStoreApi.md#get_store) | **GET** /resources/stores/object/{store_id} | Describe an object store.
[**get_stores**](ObjectStoreApi.md#get_stores) | **GET** /resources/stores/object | List object stores.
[**get_value_for_key**](ObjectStoreApi.md#get_value_for_key) | **GET** /resources/stores/object/{store_id}/keys/{key_name} | Get object store key value.
[**set_value_for_key**](ObjectStoreApi.md#set_value_for_key) | **PUT** /resources/stores/object/{store_id}/keys/{key_name} | Insert object store key-value.


# **create_store**
> StoreResponse create_store()

Create an object store.

Create a new object store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store = Store(
        name="name_example",
    ) # Store |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an object store.
        api_response = api_instance.create_store(store=store)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->create_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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

# **delete_key_from_store**
> delete_key_from_store(store_id, key_name)

Delete object store key.

Delete a key from a customer store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store_id = "store_id_example" # str | 
    key_name = "key_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete object store key.
        api_instance.delete_key_from_store(store_id, key_name)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->delete_key_from_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key_name** | **str**|  |

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
**204** | NO CONTENT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_store**
> delete_store(store_id)

Delete an object store.

An object store must be empty before it can be deleted.  Deleting an object store that still contains keys will result in a 409 Conflict.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store_id = "store_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an object store.
        api_instance.delete_store(store_id)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->delete_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |

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
**204** | NO CONTENT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_keys**
> KeyResponse get_keys(store_id)

List object store keys.

List all keys within an object store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
from fastly.model.key_response import KeyResponse
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store_id = "store_id_example" # str | 
    cursor = "cursor_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # List object store keys.
        api_response = api_instance.get_keys(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->get_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List object store keys.
        api_response = api_instance.get_keys(store_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->get_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**KeyResponse**](KeyResponse.md)

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

# **get_store**
> StoreResponse get_store(store_id)

Describe an object store.

Get an object store by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store_id = "store_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Describe an object store.
        api_response = api_instance.get_store(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->get_store: %s\n" % e)
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
> GetStoresResponse get_stores()

List object stores.

Get all stores for a given customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
from fastly.model.get_stores_response import GetStoresResponse
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    cursor = "cursor_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List object stores.
        api_response = api_instance.get_stores(cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->get_stores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**GetStoresResponse**](GetStoresResponse.md)

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

# **get_value_for_key**
> file_type get_value_for_key(store_id, key_name)

Get object store key value.

Get the value associated with a key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store_id = "store_id_example" # str | 
    key_name = "key_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get object store key value.
        api_response = api_instance.get_value_for_key(store_id, key_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->get_value_for_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key_name** | **str**|  |

### Return type

**file_type**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_value_for_key**
> file_type set_value_for_key(store_id, key_name)

Insert object store key-value.

Insert a new key-value pair into an object store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_api
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
    api_instance = object_store_api.ObjectStoreApi(api_client)
    store_id = "store_id_example" # str | 
    key_name = "key_name_example" # str | 
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert object store key-value.
        api_response = api_instance.set_value_for_key(store_id, key_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->set_value_for_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert object store key-value.
        api_response = api_instance.set_value_for_key(store_id, key_name, body=body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreApi->set_value_for_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key_name** | **str**|  |
 **body** | **file_type**|  | [optional]

### Return type

**file_type**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

