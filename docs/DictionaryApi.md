# fastly.DictionaryApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dictionary**](DictionaryApi.md#create_dictionary) | **POST** /service/{service_id}/version/{version_id}/dictionary | Create an edge dictionary
[**delete_dictionary**](DictionaryApi.md#delete_dictionary) | **DELETE** /service/{service_id}/version/{version_id}/dictionary/{dictionary_name} | Delete an edge dictionary
[**get_dictionary**](DictionaryApi.md#get_dictionary) | **GET** /service/{service_id}/version/{version_id}/dictionary/{dictionary_name} | Get an edge dictionary
[**list_dictionaries**](DictionaryApi.md#list_dictionaries) | **GET** /service/{service_id}/version/{version_id}/dictionary | List edge dictionaries
[**update_dictionary**](DictionaryApi.md#update_dictionary) | **PUT** /service/{service_id}/version/{version_id}/dictionary/{dictionary_name} | Update an edge dictionary


# **create_dictionary**
> DictionaryResponse create_dictionary(service_id, version_id)

Create an edge dictionary

Create named dictionary for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_api
from fastly.model.dictionary_response import DictionaryResponse
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
    api_instance = dictionary_api.DictionaryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test_dictionary" # str | Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). (optional)
    write_only = False # bool | Determines if items in the dictionary are readable or not. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Create an edge dictionary
        api_response = api_instance.create_dictionary(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->create_dictionary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an edge dictionary
        api_response = api_instance.create_dictionary(service_id, version_id, name=name, write_only=write_only)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->create_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). | [optional]
 **write_only** | **bool**| Determines if items in the dictionary are readable or not. | [optional] if omitted the server will use the default value of False

### Return type

[**DictionaryResponse**](DictionaryResponse.md)

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

# **delete_dictionary**
> InlineResponse200 delete_dictionary(service_id, version_id, dictionary_name)

Delete an edge dictionary

Delete named dictionary for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_api
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
    api_instance = dictionary_api.DictionaryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    dictionary_name = "test_dictionary" # str | Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace).

    # example passing only required values which don't have defaults set
    try:
        # Delete an edge dictionary
        api_response = api_instance.delete_dictionary(service_id, version_id, dictionary_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->delete_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **dictionary_name** | **str**| Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). |

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

# **get_dictionary**
> DictionaryResponse get_dictionary(service_id, version_id, dictionary_name)

Get an edge dictionary

Retrieve a single dictionary by name for the version and service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_api
from fastly.model.dictionary_response import DictionaryResponse
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
    api_instance = dictionary_api.DictionaryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    dictionary_name = "test_dictionary" # str | Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace).

    # example passing only required values which don't have defaults set
    try:
        # Get an edge dictionary
        api_response = api_instance.get_dictionary(service_id, version_id, dictionary_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->get_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **dictionary_name** | **str**| Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). |

### Return type

[**DictionaryResponse**](DictionaryResponse.md)

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

# **list_dictionaries**
> [DictionaryResponse] list_dictionaries(service_id, version_id)

List edge dictionaries

List all dictionaries for the version of the service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_api
from fastly.model.dictionary_response import DictionaryResponse
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
    api_instance = dictionary_api.DictionaryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List edge dictionaries
        api_response = api_instance.list_dictionaries(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->list_dictionaries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[DictionaryResponse]**](DictionaryResponse.md)

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

# **update_dictionary**
> DictionaryResponse update_dictionary(service_id, version_id, dictionary_name)

Update an edge dictionary

Update named dictionary for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dictionary_api
from fastly.model.dictionary_response import DictionaryResponse
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
    api_instance = dictionary_api.DictionaryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    dictionary_name = "test_dictionary" # str | Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace).
    name = "test_dictionary" # str | Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). (optional)
    write_only = False # bool | Determines if items in the dictionary are readable or not. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Update an edge dictionary
        api_response = api_instance.update_dictionary(service_id, version_id, dictionary_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->update_dictionary: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an edge dictionary
        api_response = api_instance.update_dictionary(service_id, version_id, dictionary_name, name=name, write_only=write_only)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DictionaryApi->update_dictionary: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **dictionary_name** | **str**| Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). |
 **name** | **str**| Name for the Dictionary (must start with an alphabetic character and can contain only alphanumeric characters, underscores, and whitespace). | [optional]
 **write_only** | **bool**| Determines if items in the dictionary are readable or not. | [optional] if omitted the server will use the default value of False

### Return type

[**DictionaryResponse**](DictionaryResponse.md)

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

