# fastly.KvStoreItemApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**kv_store_delete_item**](KvStoreItemApi.md#kv_store_delete_item) | **DELETE** /resources/stores/kv/{store_id}/keys/{key} | Delete an item.
[**kv_store_get_item**](KvStoreItemApi.md#kv_store_get_item) | **GET** /resources/stores/kv/{store_id}/keys/{key} | Get an item.
[**kv_store_list_item_keys**](KvStoreItemApi.md#kv_store_list_item_keys) | **GET** /resources/stores/kv/{store_id}/keys | List item keys.
[**kv_store_upsert_item**](KvStoreItemApi.md#kv_store_upsert_item) | **PUT** /resources/stores/kv/{store_id}/keys/{key} | Insert or update an item.


# **kv_store_delete_item**
> kv_store_delete_item(store_id, key)

Delete an item.

Delete an item.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_item_api
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
    api_instance = kv_store_item_api.KvStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    key = "key_example" # str | 
    if_generation_match = 1 # int |  (optional)
    force = False # bool |  (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete an item.
        api_instance.kv_store_delete_item(store_id, key)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_delete_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete an item.
        api_instance.kv_store_delete_item(store_id, key, if_generation_match=if_generation_match, force=force)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_delete_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key** | **str**|  |
 **if_generation_match** | **int**|  | [optional]
 **force** | **bool**|  | [optional] if omitted the server will use the default value of False

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
**204** | Successful deletion |  -  |
**404** | Item was not found, or store was not found |  -  |
**412** | Current generation marker did not match the value provided in if-generation-match |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_store_get_item**
> str kv_store_get_item(store_id, key)

Get an item.

Get an item, including its value, metadata (if any), and generation marker.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_item_api
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
    api_instance = kv_store_item_api.KvStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    key = "key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an item.
        api_response = api_instance.kv_store_get_item(store_id, key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_get_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key** | **str**|  |

### Return type

**str**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval |  * generation - Current generation marker <br>  * metadata - Previously-stored metadata, if any. <br>  |
**404** | Item was not found, or store was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_store_list_item_keys**
> InlineResponse2004 kv_store_list_item_keys(store_id)

List item keys.

Lists the matching item keys (or all item keys, if no prefix is supplied).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_item_api
from fastly.model.inline_response2004 import InlineResponse2004
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
    api_instance = kv_store_item_api.KvStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    cursor = "cursor_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100
    prefix = "prefix_example" # str |  (optional)
    consistency = "strong" # str |  (optional) if omitted the server will use the default value of "strong"

    # example passing only required values which don't have defaults set
    try:
        # List item keys.
        api_response = api_instance.kv_store_list_item_keys(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_list_item_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List item keys.
        api_response = api_instance.kv_store_list_item_keys(store_id, cursor=cursor, limit=limit, prefix=prefix, consistency=consistency)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_list_item_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100
 **prefix** | **str**|  | [optional]
 **consistency** | **str**|  | [optional] if omitted the server will use the default value of "strong"

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful retrieval |  -  |
**404** | KV store was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **kv_store_upsert_item**
> kv_store_upsert_item(store_id, key)

Insert or update an item.

Inserts or updates an item's value and metadata.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import kv_store_item_api
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
    api_instance = kv_store_item_api.KvStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    key = "key_example" # str | 
    if_generation_match = 1 # int |  (optional)
    time_to_live_sec = 1 # int |  (optional)
    metadata = "metadata_example" # str |  (optional)
    add = False # bool |  (optional) if omitted the server will use the default value of False
    append = False # bool |  (optional) if omitted the server will use the default value of False
    prepend = False # bool |  (optional) if omitted the server will use the default value of False
    background_fetch = False # bool |  (optional) if omitted the server will use the default value of False
    body = 'YQ==' # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert or update an item.
        api_instance.kv_store_upsert_item(store_id, key)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_upsert_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert or update an item.
        api_instance.kv_store_upsert_item(store_id, key, if_generation_match=if_generation_match, time_to_live_sec=time_to_live_sec, metadata=metadata, add=add, append=append, prepend=prepend, background_fetch=background_fetch, body=body)
    except fastly.ApiException as e:
        print("Exception when calling KvStoreItemApi->kv_store_upsert_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key** | **str**|  |
 **if_generation_match** | **int**|  | [optional]
 **time_to_live_sec** | **int**|  | [optional]
 **metadata** | **str**|  | [optional]
 **add** | **bool**|  | [optional] if omitted the server will use the default value of False
 **append** | **bool**|  | [optional] if omitted the server will use the default value of False
 **prepend** | **bool**|  | [optional] if omitted the server will use the default value of False
 **background_fetch** | **bool**|  | [optional] if omitted the server will use the default value of False
 **body** | **str**|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Provided name is not valid |  -  |
**404** | KV store was not found |  -  |
**412** | Current generation marker did not match the value provided in if-generation-match, or &#39;add&#39; was set to &#39;true&#39; but the key already existed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

