# fastly.DictionaryItemApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_dictionary_item**](DictionaryItemApi.md#bulk_update_dictionary_item) | **PATCH** /service/{service_id}/dictionary/{dictionary_id}/items | Update multiple entries in an edge dictionary
[**create_dictionary_item**](DictionaryItemApi.md#create_dictionary_item) | **POST** /service/{service_id}/dictionary/{dictionary_id}/item | Create an entry in an edge dictionary
[**delete_dictionary_item**](DictionaryItemApi.md#delete_dictionary_item) | **DELETE** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Delete an item from an edge dictionary
[**get_dictionary_item**](DictionaryItemApi.md#get_dictionary_item) | **GET** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Get an item from an edge dictionary
[**list_dictionary_items**](DictionaryItemApi.md#list_dictionary_items) | **GET** /service/{service_id}/dictionary/{dictionary_id}/items | List items in an edge dictionary
[**update_dictionary_item**](DictionaryItemApi.md#update_dictionary_item) | **PATCH** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Update an entry in an edge dictionary
[**upsert_dictionary_item**](DictionaryItemApi.md#upsert_dictionary_item) | **PUT** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Insert or update an entry in an edge dictionary


# **bulk_update_dictionary_item**
> InlineResponse200 bulk_update_dictionary_item(service_id, dictionary_id)

Update multiple entries in an edge dictionary

Update multiple items in the same dictionary. For faster updates to your service, group your changes into large batches. The maximum batch size is 1000 items. [Contact support](https://support.fastly.com/) to discuss raising this limit.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.bulk_update_dictionary_list_request import BulkUpdateDictionaryListRequest
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    bulk_update_dictionary_list_request = BulkUpdateDictionaryListRequest(
        items=[
            BulkUpdateDictionaryItem(),
        ],
    ) # BulkUpdateDictionaryListRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple entries in an edge dictionary
        api_response = api_instance.bulk_update_dictionary_item(service_id, dictionary_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->bulk_update_dictionary_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple entries in an edge dictionary
        api_response = api_instance.bulk_update_dictionary_item(service_id, dictionary_id, bulk_update_dictionary_list_request=bulk_update_dictionary_list_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->bulk_update_dictionary_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **bulk_update_dictionary_list_request** | [**BulkUpdateDictionaryListRequest**](BulkUpdateDictionaryListRequest.md)|  | [optional]

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

# **create_dictionary_item**
> DictionaryItemResponse create_dictionary_item(service_id, dictionary_id)

Create an entry in an edge dictionary

Create DictionaryItem given service, dictionary ID, item key, and item value.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
from fastly.model.dictionary_item_response import DictionaryItemResponse
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    item_key = "test-key" # str | Item key, maximum 256 characters. (optional)
    item_value = "test-value" # str | Item value, maximum 8000 characters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an entry in an edge dictionary
        api_response = api_instance.create_dictionary_item(service_id, dictionary_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->create_dictionary_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an entry in an edge dictionary
        api_response = api_instance.create_dictionary_item(service_id, dictionary_id, item_key=item_key, item_value=item_value)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->create_dictionary_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **item_key** | **str**| Item key, maximum 256 characters. | [optional]
 **item_value** | **str**| Item value, maximum 8000 characters. | [optional]

### Return type

[**DictionaryItemResponse**](DictionaryItemResponse.md)

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

# **delete_dictionary_item**
> InlineResponse200 delete_dictionary_item(service_id, dictionary_id, dictionary_item_key)

Delete an item from an edge dictionary

Delete DictionaryItem given service, dictionary ID, and item key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    dictionary_item_key = "test-key" # str | Item key, maximum 256 characters.

    # example passing only required values which don't have defaults set
    try:
        # Delete an item from an edge dictionary
        api_response = api_instance.delete_dictionary_item(service_id, dictionary_id, dictionary_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->delete_dictionary_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **dictionary_item_key** | **str**| Item key, maximum 256 characters. |

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

# **get_dictionary_item**
> DictionaryItemResponse get_dictionary_item(service_id, dictionary_id, dictionary_item_key)

Get an item from an edge dictionary

Retrieve a single DictionaryItem given service, dictionary ID and item key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
from fastly.model.dictionary_item_response import DictionaryItemResponse
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    dictionary_item_key = "test-key" # str | Item key, maximum 256 characters.

    # example passing only required values which don't have defaults set
    try:
        # Get an item from an edge dictionary
        api_response = api_instance.get_dictionary_item(service_id, dictionary_id, dictionary_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->get_dictionary_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **dictionary_item_key** | **str**| Item key, maximum 256 characters. |

### Return type

[**DictionaryItemResponse**](DictionaryItemResponse.md)

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

# **list_dictionary_items**
> [DictionaryItemResponse] list_dictionary_items(service_id, dictionary_id)

List items in an edge dictionary

List of DictionaryItems given service and dictionary ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
from fastly.model.dictionary_item_response import DictionaryItemResponse
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    page = 1 # int | Current page. (optional)
    per_page = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    sort = "created" # str | Field on which to sort. (optional) if omitted the server will use the default value of "created"
    direction = "ascend" # str | Direction in which to sort results. (optional) if omitted the server will use the default value of "ascend"

    # example passing only required values which don't have defaults set
    try:
        # List items in an edge dictionary
        api_response = api_instance.list_dictionary_items(service_id, dictionary_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->list_dictionary_items: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List items in an edge dictionary
        api_response = api_instance.list_dictionary_items(service_id, dictionary_id, page=page, per_page=per_page, sort=sort, direction=direction)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->list_dictionary_items: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **page** | **int**| Current page. | [optional]
 **per_page** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Field on which to sort. | [optional] if omitted the server will use the default value of "created"
 **direction** | **str**| Direction in which to sort results. | [optional] if omitted the server will use the default value of "ascend"

### Return type

[**[DictionaryItemResponse]**](DictionaryItemResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Link - Contains URLs for fetching additional paginated results. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dictionary_item**
> DictionaryItemResponse update_dictionary_item(service_id, dictionary_id, dictionary_item_key)

Update an entry in an edge dictionary

Update DictionaryItem given service, dictionary ID, item key, and item value.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
from fastly.model.dictionary_item_response import DictionaryItemResponse
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    dictionary_item_key = "test-key" # str | Item key, maximum 256 characters.
    item_key = "test-key" # str | Item key, maximum 256 characters. (optional)
    item_value = "test-value" # str | Item value, maximum 8000 characters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an entry in an edge dictionary
        api_response = api_instance.update_dictionary_item(service_id, dictionary_id, dictionary_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->update_dictionary_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an entry in an edge dictionary
        api_response = api_instance.update_dictionary_item(service_id, dictionary_id, dictionary_item_key, item_key=item_key, item_value=item_value)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->update_dictionary_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **dictionary_item_key** | **str**| Item key, maximum 256 characters. |
 **item_key** | **str**| Item key, maximum 256 characters. | [optional]
 **item_value** | **str**| Item value, maximum 8000 characters. | [optional]

### Return type

[**DictionaryItemResponse**](DictionaryItemResponse.md)

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

# **upsert_dictionary_item**
> DictionaryItemResponse upsert_dictionary_item(service_id, dictionary_id, dictionary_item_key)

Insert or update an entry in an edge dictionary

Upsert DictionaryItem given service, dictionary ID, item key, and item value.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_item_api
from fastly.model.dictionary_item_response import DictionaryItemResponse
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
    api_instance = dictionary_item_api.DictionaryItemApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    dictionary_id = "3vjTN8v1O7nOAY7aNDGOL" # str | Alphanumeric string identifying a Dictionary.
    dictionary_item_key = "test-key" # str | Item key, maximum 256 characters.
    item_key = "test-key" # str | Item key, maximum 256 characters. (optional)
    item_value = "test-value" # str | Item value, maximum 8000 characters. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Insert or update an entry in an edge dictionary
        api_response = api_instance.upsert_dictionary_item(service_id, dictionary_id, dictionary_item_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->upsert_dictionary_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Insert or update an entry in an edge dictionary
        api_response = api_instance.upsert_dictionary_item(service_id, dictionary_id, dictionary_item_key, item_key=item_key, item_value=item_value)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryItemApi->upsert_dictionary_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **dictionary_id** | **str**| Alphanumeric string identifying a Dictionary. |
 **dictionary_item_key** | **str**| Item key, maximum 256 characters. |
 **item_key** | **str**| Item key, maximum 256 characters. | [optional]
 **item_value** | **str**| Item value, maximum 8000 characters. | [optional]

### Return type

[**DictionaryItemResponse**](DictionaryItemResponse.md)

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

