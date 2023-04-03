# fastly.ObjectStoreItemApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_key_from_store**](ObjectStoreItemApi.md#delete_key_from_store) | **DELETE** /resources/stores/object/{store_id}/keys/{key_name} | Delete object store item.
[**get_keys**](ObjectStoreItemApi.md#get_keys) | **GET** /resources/stores/object/{store_id}/keys | List object store keys.
[**get_value_for_key**](ObjectStoreItemApi.md#get_value_for_key) | **GET** /resources/stores/object/{store_id}/keys/{key_name} | Get the value of an object store item
[**set_value_for_key**](ObjectStoreItemApi.md#set_value_for_key) | **PUT** /resources/stores/object/{store_id}/keys/{key_name} | Insert an item into an object store


# **delete_key_from_store**
> delete_key_from_store(store_id, key_name)

Delete object store item.

Delete an item from an object store

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_item_api
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
    api_instance = object_store_item_api.ObjectStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    key_name = "key_name_example" # str | 
    force = True # bool |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete object store item.
        api_instance.delete_key_from_store(store_id, key_name)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->delete_key_from_store: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete object store item.
        api_instance.delete_key_from_store(store_id, key_name, force=force)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->delete_key_from_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key_name** | **str**|  |
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

# **get_keys**
> InlineResponse2003 get_keys(store_id)

List object store keys.

List the keys of all items within an object store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_item_api
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
    api_instance = object_store_item_api.ObjectStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    cursor = "cursor_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100
    prefix = "prefix_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List object store keys.
        api_response = api_instance.get_keys(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->get_keys: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List object store keys.
        api_response = api_instance.get_keys(store_id, cursor=cursor, limit=limit, prefix=prefix)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->get_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100
 **prefix** | **str**|  | [optional]

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_value_for_key**
> file_type get_value_for_key(store_id, key_name)

Get the value of an object store item

Get the value associated with a key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_item_api
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
    api_instance = object_store_item_api.ObjectStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    key_name = "key_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the value of an object store item
        api_response = api_instance.get_value_for_key(store_id, key_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->get_value_for_key: %s\n" % e)
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
**200** | OK |  * generation - A unique, non-serial 32-bit integer that can be used for testing against a specific object store value. <br>  * metadata - An arbitrary data field which can contain up to 2000B of data <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_value_for_key**
> file_type set_value_for_key(store_id, key_name)

Insert an item into an object store

Set a new value for a new or existing key in an object store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_store_item_api
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
    api_instance = object_store_item_api.ObjectStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    key_name = "key_name_example" # str | 
    if_generation_match = 1 # int |  (optional)
    time_to_live_sec = 1 # int |  (optional)
    metadata = "metadata_example" # str |  (optional)
    add = True # bool |  (optional)
    append = True # bool |  (optional)
    prepend = True # bool |  (optional)
    background_fetch = True # bool |  (optional)
    body = open('/path/to/file', 'rb') # file_type |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert an item into an object store
        api_response = api_instance.set_value_for_key(store_id, key_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->set_value_for_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert an item into an object store
        api_response = api_instance.set_value_for_key(store_id, key_name, if_generation_match=if_generation_match, time_to_live_sec=time_to_live_sec, metadata=metadata, add=add, append=append, prepend=prepend, background_fetch=background_fetch, body=body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStoreItemApi->set_value_for_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **key_name** | **str**|  |
 **if_generation_match** | **int**|  | [optional]
 **time_to_live_sec** | **int**|  | [optional]
 **metadata** | **str**|  | [optional]
 **add** | **bool**|  | [optional]
 **append** | **bool**|  | [optional]
 **prepend** | **bool**|  | [optional]
 **background_fetch** | **bool**|  | [optional]
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
**200** | OK |  * generation - A unique, non-serial 32-bit integer that can be used for testing against a specific object store value. <br>  * metadata - An arbitrary data field which can contain up to 2000B of data <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

