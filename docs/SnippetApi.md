# fastly.SnippetApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_snippet**](SnippetApi.md#create_snippet) | **POST** /service/{service_id}/version/{version_id}/snippet | Create a snippet
[**delete_snippet**](SnippetApi.md#delete_snippet) | **DELETE** /service/{service_id}/version/{version_id}/snippet/{name} | Delete a snippet
[**get_snippet**](SnippetApi.md#get_snippet) | **GET** /service/{service_id}/version/{version_id}/snippet/{name} | Get a versioned snippet
[**get_snippet_dynamic**](SnippetApi.md#get_snippet_dynamic) | **GET** /service/{service_id}/snippet/{id} | Get a dynamic snippet
[**list_snippets**](SnippetApi.md#list_snippets) | **GET** /service/{service_id}/version/{version_id}/snippet | List snippets
[**update_snippet**](SnippetApi.md#update_snippet) | **PUT** /service/{service_id}/version/{version_id}/snippet/{name} | Update a versioned snippet
[**update_snippet_dynamic**](SnippetApi.md#update_snippet_dynamic) | **PUT** /service/{service_id}/snippet/{id} | Update a dynamic snippet


# **create_snippet**
> SnippetResponse create_snippet(service_id, version_id)

Create a snippet

Create a snippet for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
from fastly.model.snippet_response import SnippetResponse
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-snippet" # str | The name for the snippet. (optional)
    type = "init" # str | The location in generated VCL where the snippet should be placed. (optional)
    content = "content_example" # str, none_type | The VCL code that specifies exactly what the snippet does. (optional)
    priority = "10" # str | Priority determines execution order. Lower numbers execute first. (optional) if omitted the server will use the default value of "100"
    dynamic = "0" # str | Sets the snippet version. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a snippet
        api_response = api_instance.create_snippet(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->create_snippet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a snippet
        api_response = api_instance.create_snippet(service_id, version_id, name=name, type=type, content=content, priority=priority, dynamic=dynamic)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->create_snippet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the snippet. | [optional]
 **type** | **str**| The location in generated VCL where the snippet should be placed. | [optional]
 **content** | **str, none_type**| The VCL code that specifies exactly what the snippet does. | [optional]
 **priority** | **str**| Priority determines execution order. Lower numbers execute first. | [optional] if omitted the server will use the default value of "100"
 **dynamic** | **str**| Sets the snippet version. | [optional]

### Return type

[**SnippetResponse**](SnippetResponse.md)

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

# **delete_snippet**
> InlineResponse200 delete_snippet(service_id, version_id, name)

Delete a snippet

Delete a specific snippet for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-snippet" # str | The name for the snippet.

    # example passing only required values which don't have defaults set
    try:
        # Delete a snippet
        api_response = api_instance.delete_snippet(service_id, version_id, name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->delete_snippet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the snippet. |

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

# **get_snippet**
> SnippetResponse get_snippet(service_id, version_id, name)

Get a versioned snippet

Get a single snippet for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
from fastly.model.snippet_response import SnippetResponse
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-snippet" # str | The name for the snippet.

    # example passing only required values which don't have defaults set
    try:
        # Get a versioned snippet
        api_response = api_instance.get_snippet(service_id, version_id, name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->get_snippet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the snippet. |

### Return type

[**SnippetResponse**](SnippetResponse.md)

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

# **get_snippet_dynamic**
> SnippetResponse get_snippet_dynamic(service_id, id)

Get a dynamic snippet

Get a single dynamic snippet for a particular service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
from fastly.model.snippet_response import SnippetResponse
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    id = "62Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a VCL Snippet.

    # example passing only required values which don't have defaults set
    try:
        # Get a dynamic snippet
        api_response = api_instance.get_snippet_dynamic(service_id, id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->get_snippet_dynamic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **id** | **str**| Alphanumeric string identifying a VCL Snippet. |

### Return type

[**SnippetResponse**](SnippetResponse.md)

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

# **list_snippets**
> [SnippetResponse] list_snippets(service_id, version_id)

List snippets

List all snippets for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
from fastly.model.snippet_response import SnippetResponse
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List snippets
        api_response = api_instance.list_snippets(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->list_snippets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[SnippetResponse]**](SnippetResponse.md)

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

# **update_snippet**
> SnippetResponse update_snippet(service_id, version_id, name)

Update a versioned snippet

Update a specific snippet for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
from fastly.model.snippet_response import SnippetResponse
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-snippet" # str | The name for the snippet.

    # example passing only required values which don't have defaults set
    try:
        # Update a versioned snippet
        api_response = api_instance.update_snippet(service_id, version_id, name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->update_snippet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the snippet. |

### Return type

[**SnippetResponse**](SnippetResponse.md)

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

# **update_snippet_dynamic**
> SnippetResponse update_snippet_dynamic(service_id, id)

Update a dynamic snippet

Update a dynamic snippet for a particular service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import snippet_api
from fastly.model.snippet_response import SnippetResponse
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
    api_instance = snippet_api.SnippetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    id = "62Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a VCL Snippet.
    name = "test-snippet" # str | The name for the snippet. (optional)
    type = "init" # str | The location in generated VCL where the snippet should be placed. (optional)
    content = "content_example" # str, none_type | The VCL code that specifies exactly what the snippet does. (optional)
    priority = "10" # str | Priority determines execution order. Lower numbers execute first. (optional) if omitted the server will use the default value of "100"
    dynamic = "0" # str | Sets the snippet version. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a dynamic snippet
        api_response = api_instance.update_snippet_dynamic(service_id, id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->update_snippet_dynamic: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a dynamic snippet
        api_response = api_instance.update_snippet_dynamic(service_id, id, name=name, type=type, content=content, priority=priority, dynamic=dynamic)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SnippetApi->update_snippet_dynamic: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **id** | **str**| Alphanumeric string identifying a VCL Snippet. |
 **name** | **str**| The name for the snippet. | [optional]
 **type** | **str**| The location in generated VCL where the snippet should be placed. | [optional]
 **content** | **str, none_type**| The VCL code that specifies exactly what the snippet does. | [optional]
 **priority** | **str**| Priority determines execution order. Lower numbers execute first. | [optional] if omitted the server will use the default value of "100"
 **dynamic** | **str**| Sets the snippet version. | [optional]

### Return type

[**SnippetResponse**](SnippetResponse.md)

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

