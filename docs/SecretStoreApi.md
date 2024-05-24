# fastly.SecretStoreApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_key**](SecretStoreApi.md#client_key) | **POST** /resources/stores/secret/client-key | Create new client key
[**create_secret_store**](SecretStoreApi.md#create_secret_store) | **POST** /resources/stores/secret | Create new secret store
[**delete_secret_store**](SecretStoreApi.md#delete_secret_store) | **DELETE** /resources/stores/secret/{store_id} | Delete secret store
[**get_secret_store**](SecretStoreApi.md#get_secret_store) | **GET** /resources/stores/secret/{store_id} | Get secret store by ID
[**get_secret_stores**](SecretStoreApi.md#get_secret_stores) | **GET** /resources/stores/secret | Get all secret stores
[**signing_key**](SecretStoreApi.md#signing_key) | **GET** /resources/stores/secret/signing-key | Get public key


# **client_key**
> ClientKey client_key()

Create new client key

Create a new client key for encrypting secrets locally before uploading.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_api
from fastly.model.client_key import ClientKey
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
    api_instance = secret_store_api.SecretStoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create new client key
        api_response = api_instance.client_key()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreApi->client_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ClientKey**](ClientKey.md)

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

# **create_secret_store**
> SecretStoreResponse create_secret_store()

Create new secret store

Create a new secret store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_api
from fastly.model.secret_store import SecretStore
from fastly.model.secret_store_response import SecretStoreResponse
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
    api_instance = secret_store_api.SecretStoreApi(api_client)
    secret_store = SecretStore(
        name="name_example",
    ) # SecretStore |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create new secret store
        api_response = api_instance.create_secret_store(secret_store=secret_store)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreApi->create_secret_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_store** | [**SecretStore**](SecretStore.md)|  | [optional]

### Return type

[**SecretStoreResponse**](SecretStoreResponse.md)

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

# **delete_secret_store**
> delete_secret_store(store_id)

Delete secret store

Delete a secret store and all of its contents.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_api
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
    api_instance = secret_store_api.SecretStoreApi(api_client)
    store_id = "store_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete secret store
        api_instance.delete_secret_store(store_id)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreApi->delete_secret_store: %s\n" % e)
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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_secret_store**
> SecretStoreResponse get_secret_store(store_id)

Get secret store by ID

Get a secret store by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_api
from fastly.model.secret_store_response import SecretStoreResponse
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
    api_instance = secret_store_api.SecretStoreApi(api_client)
    store_id = "store_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get secret store by ID
        api_response = api_instance.get_secret_store(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreApi->get_secret_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |

### Return type

[**SecretStoreResponse**](SecretStoreResponse.md)

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

# **get_secret_stores**
> InlineResponse2005 get_secret_stores()

Get all secret stores

Get all secret stores.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_api
from fastly.model.inline_response2005 import InlineResponse2005
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
    api_instance = secret_store_api.SecretStoreApi(api_client)
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = "100" # str | Number of results per page. The maximum is 200. (optional) if omitted the server will use the default value of "100"
    name = "name_example" # str | Returns a one-element array containing the details for the named secret store. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get all secret stores
        api_response = api_instance.get_secret_stores(cursor=cursor, limit=limit, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreApi->get_secret_stores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **str**| Number of results per page. The maximum is 200. | [optional] if omitted the server will use the default value of "100"
 **name** | **str**| Returns a one-element array containing the details for the named secret store. | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

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

# **signing_key**
> SigningKey signing_key()

Get public key

Get the public key used for signing client keys.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_api
from fastly.model.signing_key import SigningKey
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
    api_instance = secret_store_api.SecretStoreApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get public key
        api_response = api_instance.signing_key()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreApi->signing_key: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**SigningKey**](SigningKey.md)

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

