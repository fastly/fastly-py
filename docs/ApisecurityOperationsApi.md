# fastly.ApisecurityOperationsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_security_bulk_add_tags_to_operations**](ApisecurityOperationsApi.md#api_security_bulk_add_tags_to_operations) | **POST** /api-security/v1/services/{service_id}/operations-bulk-tags | Bulk add tags to operations
[**api_security_bulk_create_operations**](ApisecurityOperationsApi.md#api_security_bulk_create_operations) | **POST** /api-security/v1/services/{service_id}/operations-bulk | Bulk create operations
[**api_security_bulk_delete_operations**](ApisecurityOperationsApi.md#api_security_bulk_delete_operations) | **DELETE** /api-security/v1/services/{service_id}/operations-bulk | Bulk delete operations
[**api_security_create_operation**](ApisecurityOperationsApi.md#api_security_create_operation) | **POST** /api-security/v1/services/{service_id}/operations | Create operation
[**api_security_create_operation_tag**](ApisecurityOperationsApi.md#api_security_create_operation_tag) | **POST** /api-security/v1/services/{service_id}/tags | Create operation tag
[**api_security_delete_operation**](ApisecurityOperationsApi.md#api_security_delete_operation) | **DELETE** /api-security/v1/services/{service_id}/operations/{operation_id} | Delete operation
[**api_security_delete_operation_tag**](ApisecurityOperationsApi.md#api_security_delete_operation_tag) | **DELETE** /api-security/v1/services/{service_id}/tags/{tag_id} | Delete operation tag
[**api_security_get_operation**](ApisecurityOperationsApi.md#api_security_get_operation) | **GET** /api-security/v1/services/{service_id}/operations/{operation_id} | Retrieve operation
[**api_security_get_operation_tag**](ApisecurityOperationsApi.md#api_security_get_operation_tag) | **GET** /api-security/v1/services/{service_id}/tags/{tag_id} | Retrieve operation tag
[**api_security_list_discovered_operations**](ApisecurityOperationsApi.md#api_security_list_discovered_operations) | **GET** /api-security/v1/services/{service_id}/discovered-operations | List discovered operations
[**api_security_list_operation_tags**](ApisecurityOperationsApi.md#api_security_list_operation_tags) | **GET** /api-security/v1/services/{service_id}/tags | List operation tags
[**api_security_list_operations**](ApisecurityOperationsApi.md#api_security_list_operations) | **GET** /api-security/v1/services/{service_id}/operations | List operations
[**api_security_update_operation**](ApisecurityOperationsApi.md#api_security_update_operation) | **PATCH** /api-security/v1/services/{service_id}/operations/{operation_id} | Update operation
[**api_security_update_operation_tag**](ApisecurityOperationsApi.md#api_security_update_operation_tag) | **PATCH** /api-security/v1/services/{service_id}/tags/{tag_id} | Update operation tag


# **api_security_bulk_add_tags_to_operations**
> InlineResponse2071 api_security_bulk_add_tags_to_operations(service_id)

Bulk add tags to operations

Add tags to multiple operations in a single request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.operation_bulk_add_tags import OperationBulkAddTags
from fastly.model.inline_response2071 import InlineResponse2071
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_bulk_add_tags = OperationBulkAddTags(
        operation_ids=[
            "op_abc123def456",
        ],
        tag_ids=[
            "tag_abc123def456",
        ],
    ) # OperationBulkAddTags |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Bulk add tags to operations
        api_response = api_instance.api_security_bulk_add_tags_to_operations(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_bulk_add_tags_to_operations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk add tags to operations
        api_response = api_instance.api_security_bulk_add_tags_to_operations(service_id, operation_bulk_add_tags=operation_bulk_add_tags)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_bulk_add_tags_to_operations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_bulk_add_tags** | [**OperationBulkAddTags**](OperationBulkAddTags.md)|  | [optional]

### Return type

[**InlineResponse2071**](InlineResponse2071.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status response indicating the result of each tag addition. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_bulk_create_operations**
> InlineResponse207 api_security_bulk_create_operations(service_id)

Bulk create operations

Create multiple operations associated with a specific service in a single request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.inline_response207 import InlineResponse207
from fastly.model.operation_bulk_create import OperationBulkCreate
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_bulk_create = OperationBulkCreate(
        operations=[
            OperationBulkCreateOperations(
                method="GET",
                domain="www.example.com",
                path="/api/v1/users/{var1}",
                description="Retrieve user information",
                tag_ids=[
                    "tag_abc123def456",
                ],
                status="SAVED",
            ),
        ],
    ) # OperationBulkCreate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Bulk create operations
        api_response = api_instance.api_security_bulk_create_operations(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_bulk_create_operations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk create operations
        api_response = api_instance.api_security_bulk_create_operations(service_id, operation_bulk_create=operation_bulk_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_bulk_create_operations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_bulk_create** | [**OperationBulkCreate**](OperationBulkCreate.md)|  | [optional]

### Return type

[**InlineResponse207**](InlineResponse207.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status response indicating the result of each operation creation. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_bulk_delete_operations**
> InlineResponse2071 api_security_bulk_delete_operations(service_id)

Bulk delete operations

Delete multiple operations in a single request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.operation_bulk_delete import OperationBulkDelete
from fastly.model.inline_response2071 import InlineResponse2071
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_bulk_delete = OperationBulkDelete(
        operation_ids=[
            "op_abc123def456",
        ],
    ) # OperationBulkDelete |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Bulk delete operations
        api_response = api_instance.api_security_bulk_delete_operations(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_bulk_delete_operations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Bulk delete operations
        api_response = api_instance.api_security_bulk_delete_operations(service_id, operation_bulk_delete=operation_bulk_delete)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_bulk_delete_operations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_bulk_delete** | [**OperationBulkDelete**](OperationBulkDelete.md)|  | [optional]

### Return type

[**InlineResponse2071**](InlineResponse2071.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status response indicating the result of each operation deletion. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_create_operation**
> OperationGet api_security_create_operation(service_id)

Create operation

Create a new operation associated with a specific service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.operation_get import OperationGet
from fastly.model.operation_create import OperationCreate
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_create = OperationCreate(None) # OperationCreate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create operation
        api_response = api_instance.api_security_create_operation(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_create_operation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create operation
        api_response = api_instance.api_security_create_operation(service_id, operation_create=operation_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_create_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_create** | [**OperationCreate**](OperationCreate.md)|  | [optional]

### Return type

[**OperationGet**](OperationGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The operation was successfully created. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_create_operation_tag**
> TagGet api_security_create_operation_tag(service_id)

Create operation tag

Create a new operation tag associated with a specific service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.tag_get import TagGet
from fastly.model.tag_create import TagCreate
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    tag_create = TagCreate(None) # TagCreate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create operation tag
        api_response = api_instance.api_security_create_operation_tag(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_create_operation_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create operation tag
        api_response = api_instance.api_security_create_operation_tag(service_id, tag_create=tag_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_create_operation_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **tag_create** | [**TagCreate**](TagCreate.md)|  | [optional]

### Return type

[**TagGet**](TagGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The operation tag was successfully created. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_delete_operation**
> api_security_delete_operation(service_id, operation_id)

Delete operation

Delete an existing operation associated with a specific service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_id = "op_abc123def456" # str | The unique identifier of the operation.

    # example passing only required values which don't have defaults set
    try:
        # Delete operation
        api_instance.api_security_delete_operation(service_id, operation_id)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_delete_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_id** | **str**| The unique identifier of the operation. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation was successfully deleted. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_delete_operation_tag**
> api_security_delete_operation_tag(service_id, tag_id)

Delete operation tag

Delete an existing operation tag.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    tag_id = "tag_abc123def456" # str | The unique identifier of the operation tag.

    # example passing only required values which don't have defaults set
    try:
        # Delete operation tag
        api_instance.api_security_delete_operation_tag(service_id, tag_id)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_delete_operation_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **tag_id** | **str**| The unique identifier of the operation tag. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The operation tag was successfully deleted. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_get_operation**
> OperationGet api_security_get_operation(service_id, operation_id)

Retrieve operation

Get a specific operation associated with a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.operation_get import OperationGet
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_id = "op_abc123def456" # str | The unique identifier of the operation.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve operation
        api_response = api_instance.api_security_get_operation(service_id, operation_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_get_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_id** | **str**| The unique identifier of the operation. |

### Return type

[**OperationGet**](OperationGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successfully retrieved. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_get_operation_tag**
> TagGet api_security_get_operation_tag(service_id, tag_id)

Retrieve operation tag

Get a specific operation tag by its unique identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.tag_get import TagGet
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    tag_id = "tag_abc123def456" # str | The unique identifier of the operation tag.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve operation tag
        api_response = api_instance.api_security_get_operation_tag(service_id, tag_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_get_operation_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **tag_id** | **str**| The unique identifier of the operation tag. |

### Return type

[**TagGet**](TagGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation tag was successfully retrieved. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_list_discovered_operations**
> InlineResponse2001 api_security_list_discovered_operations(service_id)

List discovered operations

List all discovered operations associated with a specific service. Optionally filter operations by status.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.inline_response2001 import InlineResponse2001
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    method = ["GET","POST"] # [str] | Filter operations by HTTP method. (optional)
    domain = ["example.com","api.example.com"] # [str] | Filter operations by fully-qualified domain name (exact match). (optional)
    path = "/api/v1/users" # str | Filter operations by path (exact match). (optional)
    limit = 100 # int | The maximum number of operations to return per page. (optional) if omitted the server will use the default value of 100
    page = 1 # int | The page number to return. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List discovered operations
        api_response = api_instance.api_security_list_discovered_operations(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_list_discovered_operations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List discovered operations
        api_response = api_instance.api_security_list_discovered_operations(service_id, method=method, domain=domain, path=path, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_list_discovered_operations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **method** | **[str]**| Filter operations by HTTP method. | [optional]
 **domain** | **[str]**| Filter operations by fully-qualified domain name (exact match). | [optional]
 **path** | **str**| Filter operations by path (exact match). | [optional]
 **limit** | **int**| The maximum number of operations to return per page. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| The page number to return. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of discovered operations for the service was successfully retrieved. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_list_operation_tags**
> InlineResponse2003 api_security_list_operation_tags(service_id)

List operation tags

List all operation tags associated with a specific service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    limit = 100 # int | The maximum number of operations to return per page. (optional) if omitted the server will use the default value of 100
    page = 1 # int | The page number to return. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List operation tags
        api_response = api_instance.api_security_list_operation_tags(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_list_operation_tags: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operation tags
        api_response = api_instance.api_security_list_operation_tags(service_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_list_operation_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **limit** | **int**| The maximum number of operations to return per page. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| The page number to return. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of operation tags was successfully retrieved. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_list_operations**
> InlineResponse2002 api_security_list_operations(service_id)

List operations

List all operations associated with a specific service. Optionally filter operations by tag ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.inline_response2002 import InlineResponse2002
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    tag_id = "tag_abc123def456" # str | Filter operations by operation tag ID. Only operations associated with this operation tag will be returned. (optional)
    status = "SAVED" # str | Filter operations by status. Defaults to SAVED if omitted. (optional) if omitted the server will use the default value of "SAVED"
    method = ["GET","POST"] # [str] | Filter operations by HTTP method. (optional)
    domain = ["example.com","api.example.com"] # [str] | Filter operations by fully-qualified domain name (exact match). (optional)
    path = "/api/v1/users" # str | Filter operations by path (exact match). (optional)
    limit = 100 # int | The maximum number of operations to return per page. (optional) if omitted the server will use the default value of 100
    page = 1 # int | The page number to return. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List operations
        api_response = api_instance.api_security_list_operations(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_list_operations: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List operations
        api_response = api_instance.api_security_list_operations(service_id, tag_id=tag_id, status=status, method=method, domain=domain, path=path, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_list_operations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **tag_id** | **str**| Filter operations by operation tag ID. Only operations associated with this operation tag will be returned. | [optional]
 **status** | **str**| Filter operations by status. Defaults to SAVED if omitted. | [optional] if omitted the server will use the default value of "SAVED"
 **method** | **[str]**| Filter operations by HTTP method. | [optional]
 **domain** | **[str]**| Filter operations by fully-qualified domain name (exact match). | [optional]
 **path** | **str**| Filter operations by path (exact match). | [optional]
 **limit** | **int**| The maximum number of operations to return per page. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| The page number to return. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of operations for the service was successfully retrieved. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_update_operation**
> OperationGet api_security_update_operation(service_id, operation_id)

Update operation

Partially update an existing operation associated with a specific service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.operation_get import OperationGet
from fastly.model.operation_update import OperationUpdate
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    operation_id = "op_abc123def456" # str | The unique identifier of the operation.
    operation_update = OperationUpdate(
        method="GET",
        domain="www.example.com",
        path="/api/v1/users/{var1}",
        description="Retrieve user information",
        tag_ids=["tag_abc123def456","tag_def456ghi789"],
        status="SAVED",
    ) # OperationUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update operation
        api_response = api_instance.api_security_update_operation(service_id, operation_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_update_operation: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update operation
        api_response = api_instance.api_security_update_operation(service_id, operation_id, operation_update=operation_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_update_operation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **operation_id** | **str**| The unique identifier of the operation. |
 **operation_update** | [**OperationUpdate**](OperationUpdate.md)|  | [optional]

### Return type

[**OperationGet**](OperationGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation was successfully updated. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_security_update_operation_tag**
> TagGet api_security_update_operation_tag(service_id, tag_id)

Update operation tag

Partially update an existing operation tag.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apisecurity_operations_api
from fastly.model.tag_get import TagGet
from fastly.model.tag_base import TagBase
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
    api_instance = apisecurity_operations_api.ApisecurityOperationsApi(api_client)
    service_id = "3NeCFuZNP1v0iyJ2vmYQI6" # str | The unique identifier of the service.
    tag_id = "tag_abc123def456" # str | The unique identifier of the operation tag.
    body = TagBase(
        name="production",
        description="Tag for production environment resources",
    ) # TagBase |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update operation tag
        api_response = api_instance.api_security_update_operation_tag(service_id, tag_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_update_operation_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update operation tag
        api_response = api_instance.api_security_update_operation_tag(service_id, tag_id, body=body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApisecurityOperationsApi->api_security_update_operation_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| The unique identifier of the service. |
 **tag_id** | **str**| The unique identifier of the operation tag. |
 **body** | [**TagBase**](TagBase.md)|  | [optional]

### Return type

[**TagGet**](TagGet.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The operation tag was successfully updated. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

