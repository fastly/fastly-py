# fastly.ResponseObjectApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_response_object**](ResponseObjectApi.md#create_response_object) | **POST** /service/{service_id}/version/{version_id}/response_object | Create a Response object
[**delete_response_object**](ResponseObjectApi.md#delete_response_object) | **DELETE** /service/{service_id}/version/{version_id}/response_object/{response_object_name} | Delete a Response Object
[**get_response_object**](ResponseObjectApi.md#get_response_object) | **GET** /service/{service_id}/version/{version_id}/response_object/{response_object_name} | Get a Response object
[**list_response_objects**](ResponseObjectApi.md#list_response_objects) | **GET** /service/{service_id}/version/{version_id}/response_object | List Response objects
[**update_response_object**](ResponseObjectApi.md#update_response_object) | **PUT** /service/{service_id}/version/{version_id}/response_object/{response_object_name} | Update a Response object


# **create_response_object**
> ResponseObjectResponse create_response_object(service_id, version_id)

Create a Response object

Creates a new Response Object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import response_object_api
from fastly.model.response_object_response import ResponseObjectResponse
from fastly.model.create_response_object_request import CreateResponseObjectRequest
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
    api_instance = response_object_api.ResponseObjectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    create_response_object_request = CreateResponseObjectRequest(
        name="name_example",
        status="status_example",
        response="response_example",
        content="content_example",
        content_type="content_type_example",
        request_condition="request_condition_example",
        cache_condition="cache_condition_example",
    ) # CreateResponseObjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Response object
        api_response = api_instance.create_response_object(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->create_response_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Response object
        api_response = api_instance.create_response_object(service_id, version_id, create_response_object_request=create_response_object_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->create_response_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **create_response_object_request** | [**CreateResponseObjectRequest**](CreateResponseObjectRequest.md)|  | [optional]

### Return type

[**ResponseObjectResponse**](ResponseObjectResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Service or version not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_response_object**
> InlineResponse200 delete_response_object(service_id, version_id, response_object_name)

Delete a Response Object

Deletes the specified Response Object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import response_object_api
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
    api_instance = response_object_api.ResponseObjectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    response_object_name = "test-response" # str | Name for the request settings.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Response Object
        api_response = api_instance.delete_response_object(service_id, version_id, response_object_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->delete_response_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **response_object_name** | **str**| Name for the request settings. |

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

# **get_response_object**
> ResponseObjectResponse get_response_object(service_id, version_id, response_object_name)

Get a Response object

Gets the specified Response Object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import response_object_api
from fastly.model.response_object_response import ResponseObjectResponse
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
    api_instance = response_object_api.ResponseObjectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    response_object_name = "test-response" # str | Name for the request settings.

    # example passing only required values which don't have defaults set
    try:
        # Get a Response object
        api_response = api_instance.get_response_object(service_id, version_id, response_object_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->get_response_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **response_object_name** | **str**| Name for the request settings. |

### Return type

[**ResponseObjectResponse**](ResponseObjectResponse.md)

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

# **list_response_objects**
> [ResponseObjectResponse] list_response_objects(service_id, version_id)

List Response objects

Returns all Response Objects for the specified service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import response_object_api
from fastly.model.response_object_response import ResponseObjectResponse
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
    api_instance = response_object_api.ResponseObjectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Response objects
        api_response = api_instance.list_response_objects(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->list_response_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[ResponseObjectResponse]**](ResponseObjectResponse.md)

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

# **update_response_object**
> ResponseObjectResponse update_response_object(service_id, version_id, response_object_name)

Update a Response object

Updates the specified Response Object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import response_object_api
from fastly.model.response_object_response import ResponseObjectResponse
from fastly.model.create_response_object_request import CreateResponseObjectRequest
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
    api_instance = response_object_api.ResponseObjectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    response_object_name = "test-response" # str | Name for the request settings.
    create_response_object_request = CreateResponseObjectRequest(
        name="name_example",
        status="status_example",
        response="response_example",
        content="content_example",
        content_type="content_type_example",
        request_condition="request_condition_example",
        cache_condition="cache_condition_example",
    ) # CreateResponseObjectRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Response object
        api_response = api_instance.update_response_object(service_id, version_id, response_object_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->update_response_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Response object
        api_response = api_instance.update_response_object(service_id, version_id, response_object_name, create_response_object_request=create_response_object_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResponseObjectApi->update_response_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **response_object_name** | **str**| Name for the request settings. |
 **create_response_object_request** | [**CreateResponseObjectRequest**](CreateResponseObjectRequest.md)|  | [optional]

### Return type

[**ResponseObjectResponse**](ResponseObjectResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Service, version, or response object not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

