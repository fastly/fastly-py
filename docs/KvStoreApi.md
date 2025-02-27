# fastly.KvStoreApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**kv_store_create**](KvStoreApi.md#kv_store_create) | **POST** /resources/stores/kv | Create a KV store.
[**kv_store_delete**](KvStoreApi.md#kv_store_delete) | **DELETE** /resources/stores/kv/{store_id} | Delete a KV store.
[**kv_store_get**](KvStoreApi.md#kv_store_get) | **GET** /resources/stores/kv/{store_id} | Describe a KV store.
[**kv_store_list**](KvStoreApi.md#kv_store_list) | **GET** /resources/stores/kv | List all KV stores.


# **kv_store_create**
> KvStoreDetails kv_store_create()

Create a KV store.

Create a KV store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
from fastly.model.kv_store_request_create import KvStoreRequestCreate
from fastly.model.kv_store_details import KvStoreDetails
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
    location = "US" # str |  (optional)
    kv_store_request_create = KvStoreRequestCreate(
        name="name_example",
    ) # KvStoreRequestCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a KV store.
        api_response = api_instance.kv_store_create(location=location, kv_store_request_create=kv_store_request_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->kv_store_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **location** | **str**|  | [optional]
 **kv_store_request_create** | [**KvStoreRequestCreate**](KvStoreRequestCreate.md)|  | [optional]

### Return type

[**KvStoreDetails**](KvStoreDetails.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Store created. |  -  |
**400** | Provided name is not valid or already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_store_delete**
> kv_store_delete(store_id)

Delete a KV store.

A KV store must be empty before it can be deleted. Attempting to delete a KV store that contains items will result in a response with a `409` status code.

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

    # example passing only required values which don't have defaults set
    try:
        # Delete a KV store.
        api_instance.kv_store_delete(store_id)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->kv_store_delete: %s\n" % e)
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
**204** | Deletion succeeded |  -  |
**404** | KV store was not found |  -  |
**409** | Deletion failed because the store contains items |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_store_get**
> KvStoreDetails kv_store_get(store_id)

Describe a KV store.

Get details of a KV store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
from fastly.model.kv_store_details import KvStoreDetails
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
        # Describe a KV store.
        api_response = api_instance.kv_store_get(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->kv_store_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |

### Return type

[**KvStoreDetails**](KvStoreDetails.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Store was found. |  -  |
**404** | KV store was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_store_list**
> InlineResponse2003 kv_store_list()

List all KV stores.

List all KV stores.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_api
from fastly.model.inline_response2003 import InlineResponse2003
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
    limit = 1000 # int |  (optional) if omitted the server will use the default value of 1000

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all KV stores.
        api_response = api_instance.kv_store_list(cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreApi->kv_store_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 1000

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Stores listed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

