# fastly.AiRuntimeControlProviderConnectionsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**arc_create_provider_connection**](AiRuntimeControlProviderConnectionsApi.md#arc_create_provider_connection) | **POST** /ai-runtime-control/v1/provider-connections | Create a provider connection
[**arc_delete_provider_connection**](AiRuntimeControlProviderConnectionsApi.md#arc_delete_provider_connection) | **DELETE** /ai-runtime-control/v1/provider-connections/{id} | Delete a provider connection
[**arc_get_provider_connection**](AiRuntimeControlProviderConnectionsApi.md#arc_get_provider_connection) | **GET** /ai-runtime-control/v1/provider-connections/{id} | Get a provider connection
[**arc_list_provider_connections**](AiRuntimeControlProviderConnectionsApi.md#arc_list_provider_connections) | **GET** /ai-runtime-control/v1/provider-connections | List provider connections
[**arc_update_provider_connection**](AiRuntimeControlProviderConnectionsApi.md#arc_update_provider_connection) | **PATCH** /ai-runtime-control/v1/provider-connections/{id} | Update a provider connection


# **arc_create_provider_connection**
> ArcProviderConnectionResponse arc_create_provider_connection(arc_provider_connection_request)

Create a provider connection

Create a provider connection. Set `auth_type` to `api-key` (the default) to connect with a provider's own API key, or to `aws-iam` to connect to Amazon Bedrock using an AWS IAM role.  Accounts are limited to 25 provider connections. Creating a 26th connection returns a 409 response. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_provider_connections_api
from fastly.model.arc_provider_connection_response import ArcProviderConnectionResponse
from fastly.model.arc_provider_connection_request import ArcProviderConnectionRequest
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_provider_connections_api.AiRuntimeControlProviderConnectionsApi(api_client)
    arc_provider_connection_request = ArcProviderConnectionRequest(None) # ArcProviderConnectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Create a provider connection
        api_response = api_instance.arc_create_provider_connection(arc_provider_connection_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProviderConnectionsApi->arc_create_provider_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arc_provider_connection_request** | [**ArcProviderConnectionRequest**](ArcProviderConnectionRequest.md)|  |

### Return type

[**ArcProviderConnectionResponse**](ArcProviderConnectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The provider connection that was created. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control, or AWS IAM authentication is not enabled for this account. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_delete_provider_connection**
> arc_delete_provider_connection(id)

Delete a provider connection

Delete a provider connection. Returns a 409 response if the connection is still referenced by a virtual key's failover policy. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_provider_connections_api
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_provider_connections_api.AiRuntimeControlProviderConnectionsApi(api_client)
    id = "pTfnUUBcU1yv8SoRJn5PZ2" # str | The ID of the provider connection.

    # example passing only required values which don't have defaults set
    try:
        # Delete a provider connection
        api_instance.arc_delete_provider_connection(id)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProviderConnectionsApi->arc_delete_provider_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the provider connection. |

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
**204** | No Content |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control, or AWS IAM authentication is not enabled for this account. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_get_provider_connection**
> ArcGetProviderConnectionResponse arc_get_provider_connection(id)

Get a provider connection

Retrieve a single provider connection.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_provider_connections_api
from fastly.model.arc_get_provider_connection_response import ArcGetProviderConnectionResponse
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_provider_connections_api.AiRuntimeControlProviderConnectionsApi(api_client)
    id = "pTfnUUBcU1yv8SoRJn5PZ2" # str | The ID of the provider connection.

    # example passing only required values which don't have defaults set
    try:
        # Get a provider connection
        api_response = api_instance.arc_get_provider_connection(id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProviderConnectionsApi->arc_get_provider_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the provider connection. |

### Return type

[**ArcGetProviderConnectionResponse**](ArcGetProviderConnectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The provider connection. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control, or AWS IAM authentication is not enabled for this account. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_list_provider_connections**
> ArcProviderConnectionsResponse arc_list_provider_connections()

List provider connections

List the provider connections belonging to your account.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_provider_connections_api
from fastly.model.arc_provider_connections_response import ArcProviderConnectionsResponse
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_provider_connections_api.AiRuntimeControlProviderConnectionsApi(api_client)
    include_deleted = False # bool | Include deleted provider connections in the results. Deleted connections have a `deleted_at` value. (optional) if omitted the server will use the default value of False
    sort = "created_at" # str | Sort field. Prefix with `-` for descending order (e.g., `sort=-name`).  (optional) if omitted the server will use the default value of "created_at"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List provider connections
        api_response = api_instance.arc_list_provider_connections(include_deleted=include_deleted, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProviderConnectionsApi->arc_list_provider_connections: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| Include deleted provider connections in the results. Deleted connections have a `deleted_at` value. | [optional] if omitted the server will use the default value of False
 **sort** | **str**| Sort field. Prefix with `-` for descending order (e.g., `sort&#x3D;-name`).  | [optional] if omitted the server will use the default value of "created_at"

### Return type

[**ArcProviderConnectionsResponse**](ArcProviderConnectionsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of provider connections. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control, or AWS IAM authentication is not enabled for this account. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_update_provider_connection**
> ArcProviderConnectionResponse arc_update_provider_connection(id, arc_update_provider_connection_request)

Update a provider connection

Update the attributes of a provider connection. Only the fields you include are changed. Which fields you can set depends on the connection's existing `auth_type`: `base_url` and `api_key` apply only to `api-key` connections, and `customer_role_arn` and `region` apply only to `aws-iam` connections. `auth_type` itself cannot be changed. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_provider_connections_api
from fastly.model.arc_provider_connection_response import ArcProviderConnectionResponse
from fastly.model.arc_update_provider_connection_request import ArcUpdateProviderConnectionRequest
from fastly.model.arc_error import ArcError
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
    api_instance = ai_runtime_control_provider_connections_api.AiRuntimeControlProviderConnectionsApi(api_client)
    id = "pTfnUUBcU1yv8SoRJn5PZ2" # str | The ID of the provider connection.
    arc_update_provider_connection_request = ArcUpdateProviderConnectionRequest(
        models=["gpt-4","gpt-4-turbo"],
        base_url="https://api.openai.com",
        api_key="sk-...",
        customer_role_arn="arn:aws:iam::123456789012:role/arc-bedrock-access",
        region="us-east-1",
    ) # ArcUpdateProviderConnectionRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a provider connection
        api_response = api_instance.arc_update_provider_connection(id, arc_update_provider_connection_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlProviderConnectionsApi->arc_update_provider_connection: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID of the provider connection. |
 **arc_update_provider_connection_request** | [**ArcUpdateProviderConnectionRequest**](ArcUpdateProviderConnectionRequest.md)|  |

### Return type

[**ArcProviderConnectionResponse**](ArcProviderConnectionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The provider connection that was updated. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control, or AWS IAM authentication is not enabled for this account. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with the current state of the resource. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

