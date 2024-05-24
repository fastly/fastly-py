# fastly.SecretStoreItemApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_secret**](SecretStoreItemApi.md#create_secret) | **POST** /resources/stores/secret/{store_id}/secrets | Create a new secret in a store.
[**delete_secret**](SecretStoreItemApi.md#delete_secret) | **DELETE** /resources/stores/secret/{store_id}/secrets/{secret_name} | Delete a secret from a store.
[**get_secret**](SecretStoreItemApi.md#get_secret) | **GET** /resources/stores/secret/{store_id}/secrets/{secret_name} | Get secret metadata.
[**get_secrets**](SecretStoreItemApi.md#get_secrets) | **GET** /resources/stores/secret/{store_id}/secrets | List secrets within a store.
[**must_recreate_secret**](SecretStoreItemApi.md#must_recreate_secret) | **PATCH** /resources/stores/secret/{store_id}/secrets | Recreate a secret in a store.
[**recreate_secret**](SecretStoreItemApi.md#recreate_secret) | **PUT** /resources/stores/secret/{store_id}/secrets | Create or recreate a secret in a store.


# **create_secret**
> SecretResponse create_secret(store_id)

Create a new secret in a store.

Create a new secret in a store. Returns an error if a secret already exists with the same name. See `PUT` and `PATCH` methods for ways to recreate an existing secret.  The `secret` field must be Base64-encoded because a secret can contain binary data. In the example below, the unencoded secret is \"Hello, world!\" 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_item_api
from fastly.model.secret import Secret
from fastly.model.secret_response import SecretResponse
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
    api_instance = secret_store_item_api.SecretStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    secret = Secret(
        name="name_example",
        secret="secret_example",
        client_key="client_key_example",
    ) # Secret |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a new secret in a store.
        api_response = api_instance.create_secret(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->create_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new secret in a store.
        api_response = api_instance.create_secret(store_id, secret=secret)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->create_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **secret** | [**Secret**](Secret.md)|  | [optional]

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **delete_secret**
> delete_secret(store_id, secret_name)

Delete a secret from a store.

Delete a secret from a store by name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_item_api
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
    api_instance = secret_store_item_api.SecretStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    secret_name = "secret_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a secret from a store.
        api_instance.delete_secret(store_id, secret_name)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->delete_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **secret_name** | **str**|  |

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

# **get_secret**
> SecretResponse get_secret(store_id, secret_name)

Get secret metadata.

Get metadata about a secret by name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_item_api
from fastly.model.secret_response import SecretResponse
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
    api_instance = secret_store_item_api.SecretStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    secret_name = "secret_name_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get secret metadata.
        api_response = api_instance.get_secret(store_id, secret_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->get_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **secret_name** | **str**|  |

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **get_secrets**
> InlineResponse2006 get_secrets(store_id)

List secrets within a store.

List all secrets within a store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_item_api
from fastly.model.inline_response2006 import InlineResponse2006
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
    api_instance = secret_store_item_api.SecretStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = "100" # str | Number of results per page. The maximum is 200. (optional) if omitted the server will use the default value of "100"

    # example passing only required values which don't have defaults set
    try:
        # List secrets within a store.
        api_response = api_instance.get_secrets(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->get_secrets: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List secrets within a store.
        api_response = api_instance.get_secrets(store_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->get_secrets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **str**| Number of results per page. The maximum is 200. | [optional] if omitted the server will use the default value of "100"

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

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

# **must_recreate_secret**
> SecretResponse must_recreate_secret(store_id)

Recreate a secret in a store.

Recreate a secret based on the secret's name. Returns an error if there is no existing secret with the same name.  The `secret` field must be Base64-encoded because a secret can contain binary data. In the example below, the unencoded secret is \"Hello, world!\" 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_item_api
from fastly.model.secret import Secret
from fastly.model.secret_response import SecretResponse
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
    api_instance = secret_store_item_api.SecretStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    secret = Secret(
        name="name_example",
        secret="secret_example",
        client_key="client_key_example",
    ) # Secret |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Recreate a secret in a store.
        api_response = api_instance.must_recreate_secret(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->must_recreate_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Recreate a secret in a store.
        api_response = api_instance.must_recreate_secret(store_id, secret=secret)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->must_recreate_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **secret** | [**Secret**](Secret.md)|  | [optional]

### Return type

[**SecretResponse**](SecretResponse.md)

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

# **recreate_secret**
> SecretResponse recreate_secret(store_id)

Create or recreate a secret in a store.

Create or recreate a secret based on the secret's name. The response object's `recreated` field will be true if the secret was recreated.  The `secret` field must be Base64-encoded because a secret can contain binary data. In the example below, the unencoded secret is \"Hello, world!\" 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import secret_store_item_api
from fastly.model.secret import Secret
from fastly.model.secret_response import SecretResponse
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
    api_instance = secret_store_item_api.SecretStoreItemApi(api_client)
    store_id = "store_id_example" # str | 
    secret = Secret(
        name="name_example",
        secret="secret_example",
        client_key="client_key_example",
    ) # Secret |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or recreate a secret in a store.
        api_response = api_instance.recreate_secret(store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->recreate_secret: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or recreate a secret in a store.
        api_response = api_instance.recreate_secret(store_id, secret=secret)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SecretStoreItemApi->recreate_secret: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**|  |
 **secret** | [**Secret**](Secret.md)|  | [optional]

### Return type

[**SecretResponse**](SecretResponse.md)

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

