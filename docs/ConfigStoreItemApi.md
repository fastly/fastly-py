# fastly.ConfigStoreItemApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_config_store_item**](ConfigStoreItemApi.md#bulk_update_config_store_item) | **PATCH** /resources/stores/config/{config_store_id}/items | Update multiple entries in a config store
[**create_config_store_item**](ConfigStoreItemApi.md#create_config_store_item) | **POST** /resources/stores/config/{config_store_id}/item | Create an entry in a config store
[**delete_config_store_item**](ConfigStoreItemApi.md#delete_config_store_item) | **DELETE** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Delete an item from a config store
[**get_config_store_item**](ConfigStoreItemApi.md#get_config_store_item) | **GET** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Get an item from a config store
[**list_config_store_items**](ConfigStoreItemApi.md#list_config_store_items) | **GET** /resources/stores/config/{config_store_id}/items | List items in a config store
[**update_config_store_item**](ConfigStoreItemApi.md#update_config_store_item) | **PATCH** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Update an entry in a config store
[**upsert_config_store_item**](ConfigStoreItemApi.md#upsert_config_store_item) | **PUT** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Insert or update an entry in a config store


# **bulk_update_config_store_item**
> InlineResponse200 bulk_update_config_store_item(config_store_id)

Update multiple entries in a config store

Add multiple key-value pairs to an individual config store, specified by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.bulk_update_config_store_list_request import BulkUpdateConfigStoreListRequest
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    bulk_update_config_store_list_request = BulkUpdateConfigStoreListRequest(
        items=[
            BulkUpdateConfigStoreItem(),
        ],
    ) # BulkUpdateConfigStoreListRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple entries in a config store
        api_response = api_instance.bulk_update_config_store_item(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->bulk_update_config_store_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple entries in a config store
        api_response = api_instance.bulk_update_config_store_item(config_store_id, bulk_update_config_store_list_request=bulk_update_config_store_list_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->bulk_update_config_store_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **bulk_update_config_store_list_request** | [**BulkUpdateConfigStoreListRequest**](BulkUpdateConfigStoreListRequest.md)|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **create_config_store_item**
> ConfigStoreItemResponse create_config_store_item(config_store_id)

Create an entry in a config store

Add a single key-value pair to an individual config store, specified by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.config_store_item_response import ConfigStoreItemResponse
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    item_key = "test-key" # str | Item key, maximum 256 characters. (optional)
    item_value = "test-value" # str | Item value, maximum 8000 characters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an entry in a config store
        api_response = api_instance.create_config_store_item(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->create_config_store_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an entry in a config store
        api_response = api_instance.create_config_store_item(config_store_id, item_key=item_key, item_value=item_value)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->create_config_store_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **item_key** | **str**| Item key, maximum 256 characters. | [optional]
 **item_value** | **str**| Item value, maximum 8000 characters. | [optional]

### Return type

[**ConfigStoreItemResponse**](ConfigStoreItemResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_config_store_item**
> InlineResponse200 delete_config_store_item(config_store_id, config_store_item_key)

Delete an item from a config store

Delete an entry in a config store given a config store ID, and item key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.inline_response200 import InlineResponse200
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    config_store_item_key = "test-key" # str | Item key, maximum 256 characters.

    # example passing only required values which don't have defaults set
    try:
        # Delete an item from a config store
        api_response = api_instance.delete_config_store_item(config_store_id, config_store_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->delete_config_store_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **config_store_item_key** | **str**| Item key, maximum 256 characters. |

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **get_config_store_item**
> ConfigStoreItemResponse get_config_store_item(config_store_id, config_store_item_key)

Get an item from a config store

Retrieve a config store entry given a config store ID and item key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.config_store_item_response import ConfigStoreItemResponse
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    config_store_item_key = "test-key" # str | Item key, maximum 256 characters.

    # example passing only required values which don't have defaults set
    try:
        # Get an item from a config store
        api_response = api_instance.get_config_store_item(config_store_id, config_store_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->get_config_store_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **config_store_item_key** | **str**| Item key, maximum 256 characters. |

### Return type

[**ConfigStoreItemResponse**](ConfigStoreItemResponse.md)

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

# **list_config_store_items**
> [ConfigStoreItemResponse] list_config_store_items(config_store_id)

List items in a config store

List the key-value pairs associated with a given config store ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.config_store_item_response import ConfigStoreItemResponse
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.

    # example passing only required values which don't have defaults set
    try:
        # List items in a config store
        api_response = api_instance.list_config_store_items(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->list_config_store_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |

### Return type

[**[ConfigStoreItemResponse]**](ConfigStoreItemResponse.md)

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

# **update_config_store_item**
> ConfigStoreItemResponse update_config_store_item(config_store_id, config_store_item_key)

Update an entry in a config store

Update an entry in a config store given a config store ID, item key, and item value.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.config_store_item_response import ConfigStoreItemResponse
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    config_store_item_key = "test-key" # str | Item key, maximum 256 characters.
    item_key = "test-key" # str | Item key, maximum 256 characters. (optional)
    item_value = "test-value" # str | Item value, maximum 8000 characters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an entry in a config store
        api_response = api_instance.update_config_store_item(config_store_id, config_store_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->update_config_store_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an entry in a config store
        api_response = api_instance.update_config_store_item(config_store_id, config_store_item_key, item_key=item_key, item_value=item_value)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->update_config_store_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **config_store_item_key** | **str**| Item key, maximum 256 characters. |
 **item_key** | **str**| Item key, maximum 256 characters. | [optional]
 **item_value** | **str**| Item value, maximum 8000 characters. | [optional]

### Return type

[**ConfigStoreItemResponse**](ConfigStoreItemResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_config_store_item**
> ConfigStoreItemResponse upsert_config_store_item(config_store_id, config_store_item_key)

Insert or update an entry in a config store

Insert or update an entry in a config store given a config store ID, item key, and item value.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_item_api
from fastly.model.config_store_item_response import ConfigStoreItemResponse
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
    api_instance = config_store_item_api.ConfigStoreItemApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    config_store_item_key = "test-key" # str | Item key, maximum 256 characters.
    item_key = "test-key" # str | Item key, maximum 256 characters. (optional)
    item_value = "test-value" # str | Item value, maximum 8000 characters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert or update an entry in a config store
        api_response = api_instance.upsert_config_store_item(config_store_id, config_store_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->upsert_config_store_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert or update an entry in a config store
        api_response = api_instance.upsert_config_store_item(config_store_id, config_store_item_key, item_key=item_key, item_value=item_value)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreItemApi->upsert_config_store_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **config_store_item_key** | **str**| Item key, maximum 256 characters. |
 **item_key** | **str**| Item key, maximum 256 characters. | [optional]
 **item_value** | **str**| Item value, maximum 8000 characters. | [optional]

### Return type

[**ConfigStoreItemResponse**](ConfigStoreItemResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

