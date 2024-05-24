# fastly.ConfigStoreApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_config_store**](ConfigStoreApi.md#create_config_store) | **POST** /resources/stores/config | Create a config store
[**delete_config_store**](ConfigStoreApi.md#delete_config_store) | **DELETE** /resources/stores/config/{config_store_id} | Delete a config store
[**get_config_store**](ConfigStoreApi.md#get_config_store) | **GET** /resources/stores/config/{config_store_id} | Describe a config store
[**get_config_store_info**](ConfigStoreApi.md#get_config_store_info) | **GET** /resources/stores/config/{config_store_id}/info | Get config store metadata
[**list_config_store_services**](ConfigStoreApi.md#list_config_store_services) | **GET** /resources/stores/config/{config_store_id}/services | List linked services
[**list_config_stores**](ConfigStoreApi.md#list_config_stores) | **GET** /resources/stores/config | List config stores
[**update_config_store**](ConfigStoreApi.md#update_config_store) | **PUT** /resources/stores/config/{config_store_id} | Update a config store


# **create_config_store**
> ConfigStoreResponse create_config_store()

Create a config store

Create a config store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
from fastly.model.config_store_response import ConfigStoreResponse
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    name = "test-config-store" # str | The name of the config store. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a config store
        api_response = api_instance.create_config_store(name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->create_config_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the config store. | [optional]

### Return type

[**ConfigStoreResponse**](ConfigStoreResponse.md)

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

# **delete_config_store**
> InlineResponse200 delete_config_store(config_store_id)

Delete a config store

Delete a config store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.

    # example passing only required values which don't have defaults set
    try:
        # Delete a config store
        api_response = api_instance.delete_config_store(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->delete_config_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |

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

# **get_config_store**
> ConfigStoreResponse get_config_store(config_store_id)

Describe a config store

Describe a config store by its identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
from fastly.model.config_store_response import ConfigStoreResponse
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.

    # example passing only required values which don't have defaults set
    try:
        # Describe a config store
        api_response = api_instance.get_config_store(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->get_config_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |

### Return type

[**ConfigStoreResponse**](ConfigStoreResponse.md)

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

# **get_config_store_info**
> ConfigStoreInfoResponse get_config_store_info(config_store_id)

Get config store metadata

Retrieve metadata for a single config store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
from fastly.model.config_store_info_response import ConfigStoreInfoResponse
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.

    # example passing only required values which don't have defaults set
    try:
        # Get config store metadata
        api_response = api_instance.get_config_store_info(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->get_config_store_info: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |

### Return type

[**ConfigStoreInfoResponse**](ConfigStoreInfoResponse.md)

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

# **list_config_store_services**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_config_store_services(config_store_id)

List linked services

List services linked to a config store

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.

    # example passing only required values which don't have defaults set
    try:
        # List linked services
        api_response = api_instance.list_config_store_services(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->list_config_store_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **list_config_stores**
> [ConfigStoreResponse] list_config_stores()

List config stores

List config stores.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
from fastly.model.config_store_response import ConfigStoreResponse
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    name = "name_example" # str | Returns a one-element array containing the details for the named config store. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List config stores
        api_response = api_instance.list_config_stores(name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->list_config_stores: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Returns a one-element array containing the details for the named config store. | [optional]

### Return type

[**[ConfigStoreResponse]**](ConfigStoreResponse.md)

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

# **update_config_store**
> ConfigStoreResponse update_config_store(config_store_id)

Update a config store

Update a config store.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import config_store_api
from fastly.model.config_store_response import ConfigStoreResponse
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
    api_instance = config_store_api.ConfigStoreApi(api_client)
    config_store_id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the config store.
    name = "test-config-store" # str | The name of the config store. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a config store
        api_response = api_instance.update_config_store(config_store_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->update_config_store: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a config store
        api_response = api_instance.update_config_store(config_store_id, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConfigStoreApi->update_config_store: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_store_id** | **str**| An alphanumeric string identifying the config store. |
 **name** | **str**| The name of the config store. | [optional]

### Return type

[**ConfigStoreResponse**](ConfigStoreResponse.md)

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

