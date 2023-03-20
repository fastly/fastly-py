# fastly.ResourceApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource**](ResourceApi.md#create_resource) | **POST** /service/{service_id}/version/{version_id}/resource | Create a resource
[**delete_resource**](ResourceApi.md#delete_resource) | **DELETE** /service/{service_id}/version/{version_id}/resource/{id} | Delete a resource
[**get_resource**](ResourceApi.md#get_resource) | **GET** /service/{service_id}/version/{version_id}/resource/{id} | Display a resource
[**list_resources**](ResourceApi.md#list_resources) | **GET** /service/{service_id}/version/{version_id}/resource | List resources
[**update_resource**](ResourceApi.md#update_resource) | **PUT** /service/{service_id}/version/{version_id}/resource/{id} | Update a resource


# **create_resource**
> ResourceResponse create_resource(service_id, version_id)

Create a resource

Create a resource.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import resource_api
from fastly.model.resource_response import ResourceResponse
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
    api_instance = resource_api.ResourceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-resource" # str | The name of the resource. (optional)
    resource_id = "3vjTN8v1O7nOAY7aNDGOL" # str | The ID of the linked resource. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a resource
        api_response = api_instance.create_resource(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->create_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a resource
        api_response = api_instance.create_resource(service_id, version_id, name=name, resource_id=resource_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->create_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name of the resource. | [optional]
 **resource_id** | **str**| The ID of the linked resource. | [optional]

### Return type

[**ResourceResponse**](ResourceResponse.md)

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

# **delete_resource**
> InlineResponse200 delete_resource(service_id, version_id, id)

Delete a resource

Delete a resource.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import resource_api
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
    api_instance = resource_api.ResourceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the resource link.

    # example passing only required values which don't have defaults set
    try:
        # Delete a resource
        api_response = api_instance.delete_resource(service_id, version_id, id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->delete_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **id** | **str**| An alphanumeric string identifying the resource link. |

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

# **get_resource**
> ResourceResponse get_resource(service_id, version_id, id)

Display a resource

Display a resource by its identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import resource_api
from fastly.model.resource_response import ResourceResponse
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
    api_instance = resource_api.ResourceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the resource link.

    # example passing only required values which don't have defaults set
    try:
        # Display a resource
        api_response = api_instance.get_resource(service_id, version_id, id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->get_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **id** | **str**| An alphanumeric string identifying the resource link. |

### Return type

[**ResourceResponse**](ResourceResponse.md)

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

# **list_resources**
> ResourceListResponse list_resources(service_id, version_id)

List resources

List resources.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import resource_api
from fastly.model.resource_list_response import ResourceListResponse
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
    api_instance = resource_api.ResourceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List resources
        api_response = api_instance.list_resources(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->list_resources: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**ResourceListResponse**](ResourceListResponse.md)

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

# **update_resource**
> ResourceResponse update_resource(service_id, version_id, id)

Update a resource

Update a resource.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import resource_api
from fastly.model.resource_response import ResourceResponse
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
    api_instance = resource_api.ResourceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    id = "7Lsb7Y76rChV9hSrv3KgFl" # str | An alphanumeric string identifying the resource link.
    name = "test-resource" # str | The name of the resource. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a resource
        api_response = api_instance.update_resource(service_id, version_id, id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->update_resource: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a resource
        api_response = api_instance.update_resource(service_id, version_id, id, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ResourceApi->update_resource: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **id** | **str**| An alphanumeric string identifying the resource link. |
 **name** | **str**| The name of the resource. | [optional]

### Return type

[**ResourceResponse**](ResourceResponse.md)

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

