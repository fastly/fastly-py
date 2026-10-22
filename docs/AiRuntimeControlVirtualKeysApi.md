# fastly.AiRuntimeControlVirtualKeysApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**arc_create_virtual_key**](AiRuntimeControlVirtualKeysApi.md#arc_create_virtual_key) | **POST** /ai-runtime-control/v1/keys | Create a virtual key
[**arc_delete_virtual_key**](AiRuntimeControlVirtualKeysApi.md#arc_delete_virtual_key) | **DELETE** /ai-runtime-control/v1/keys/{key_id} | Delete a virtual key
[**arc_get_virtual_key**](AiRuntimeControlVirtualKeysApi.md#arc_get_virtual_key) | **GET** /ai-runtime-control/v1/keys/{key_id} | Get a virtual key
[**arc_get_virtual_key_failover**](AiRuntimeControlVirtualKeysApi.md#arc_get_virtual_key_failover) | **GET** /ai-runtime-control/v1/keys/{key_id}/failover | Get a virtual key&#39;s failover policy
[**arc_list_virtual_keys**](AiRuntimeControlVirtualKeysApi.md#arc_list_virtual_keys) | **GET** /ai-runtime-control/v1/keys | List virtual keys
[**arc_rotate_virtual_key**](AiRuntimeControlVirtualKeysApi.md#arc_rotate_virtual_key) | **POST** /ai-runtime-control/v1/keys/{key_id}/rotate | Rotate a virtual key
[**arc_update_virtual_key**](AiRuntimeControlVirtualKeysApi.md#arc_update_virtual_key) | **PATCH** /ai-runtime-control/v1/keys/{key_id} | Update a virtual key
[**arc_update_virtual_key_failover**](AiRuntimeControlVirtualKeysApi.md#arc_update_virtual_key_failover) | **PUT** /ai-runtime-control/v1/keys/{key_id}/failover | Update a virtual key&#39;s failover policy


# **arc_create_virtual_key**
> ArcCreateVirtualKeyResponse arc_create_virtual_key(arc_virtual_key)

Create a virtual key

Create a new virtual key for authenticating requests through the AI Runtime Control gateway.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_virtual_key import ArcVirtualKey
from fastly.model.arc_create_virtual_key_response import ArcCreateVirtualKeyResponse
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    arc_virtual_key = ArcVirtualKey(
        name="production-anthropic-key",
        expires_at=dateutil_parser('2027-01-01T00:00:00Z'),
        security_enabled=False,
        security_action="log",
        rpm_limit=60,
        tpm_limit=100000,
    ) # ArcVirtualKey | 

    # example passing only required values which don't have defaults set
    try:
        # Create a virtual key
        api_response = api_instance.arc_create_virtual_key(arc_virtual_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_create_virtual_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **arc_virtual_key** | [**ArcVirtualKey**](ArcVirtualKey.md)|  |

### Return type

[**ArcCreateVirtualKeyResponse**](ArcCreateVirtualKeyResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The virtual key was created. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_delete_virtual_key**
> arc_delete_virtual_key(key_id)

Delete a virtual key

Delete a virtual key. This also deletes any security configuration associated with the key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    key_id = "7fVVQb1nZaJgnzCn4B4v3B" # str | The ID of the virtual key.

    # example passing only required values which don't have defaults set
    try:
        # Delete a virtual key
        api_instance.arc_delete_virtual_key(key_id)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_delete_virtual_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the virtual key. |

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
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_get_virtual_key**
> ArcVirtualKeyResponse arc_get_virtual_key(key_id)

Get a virtual key

Retrieve a single virtual key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_virtual_key_response import ArcVirtualKeyResponse
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    key_id = "7fVVQb1nZaJgnzCn4B4v3B" # str | The ID of the virtual key.

    # example passing only required values which don't have defaults set
    try:
        # Get a virtual key
        api_response = api_instance.arc_get_virtual_key(key_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_get_virtual_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the virtual key. |

### Return type

[**ArcVirtualKeyResponse**](ArcVirtualKeyResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested virtual key. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_get_virtual_key_failover**
> ArcVirtualKeyFailoverResponse arc_get_virtual_key_failover(key_id)

Get a virtual key's failover policy

Retrieve the failover policy for a virtual key. A failover policy lists alternate provider connections to retry a request against, and which error conditions trigger a retry.  Failover is a per-account feature. If it isn't enabled on your account, this endpoint returns a 404 response. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_virtual_key_failover_response import ArcVirtualKeyFailoverResponse
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    key_id = "7fVVQb1nZaJgnzCn4B4v3B" # str | The ID of the virtual key.

    # example passing only required values which don't have defaults set
    try:
        # Get a virtual key's failover policy
        api_response = api_instance.arc_get_virtual_key_failover(key_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_get_virtual_key_failover: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the virtual key. |

### Return type

[**ArcVirtualKeyFailoverResponse**](ArcVirtualKeyFailoverResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The virtual key&#39;s failover policy. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_list_virtual_keys**
> ArcVirtualKeysResponse arc_list_virtual_keys()

List virtual keys

List the virtual keys belonging to your account.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_virtual_keys_response import ArcVirtualKeysResponse
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    include_deleted = False # bool | Include deleted virtual keys in the results. (optional) if omitted the server will use the default value of False
    search = "production" # str | Filter results to virtual keys whose name contains this substring. (optional)
    cursor = "MTA6MA" # str | Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results, or the `prev_cursor` value to request the previous page.  (optional)
    limit = 10 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 10
    sort = "created_at" # str | Sort field. Prefix with `-` for descending order (e.g., `sort=-created_at`).  (optional) if omitted the server will use the default value of "created_at"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List virtual keys
        api_response = api_instance.arc_list_virtual_keys(include_deleted=include_deleted, search=search, cursor=cursor, limit=limit, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_list_virtual_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_deleted** | **bool**| Include deleted virtual keys in the results. | [optional] if omitted the server will use the default value of False
 **search** | **str**| Filter results to virtual keys whose name contains this substring. | [optional]
 **cursor** | **str**| Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results, or the `prev_cursor` value to request the previous page.  | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 10
 **sort** | **str**| Sort field. Prefix with `-` for descending order (e.g., `sort&#x3D;-created_at`).  | [optional] if omitted the server will use the default value of "created_at"

### Return type

[**ArcVirtualKeysResponse**](ArcVirtualKeysResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of virtual keys. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_rotate_virtual_key**
> ArcRotateVirtualKeyResponse arc_rotate_virtual_key(key_id)

Rotate a virtual key

Issue a new access token for a virtual key, invalidating the previous one.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_rotate_virtual_key_request import ArcRotateVirtualKeyRequest
from fastly.model.arc_rotate_virtual_key_response import ArcRotateVirtualKeyResponse
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    key_id = "7fVVQb1nZaJgnzCn4B4v3B" # str | The ID of the virtual key.
    arc_rotate_virtual_key_request = ArcRotateVirtualKeyRequest(
        expires_at=dateutil_parser('2027-01-01T00:00:00Z'),
    ) # ArcRotateVirtualKeyRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Rotate a virtual key
        api_response = api_instance.arc_rotate_virtual_key(key_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_rotate_virtual_key: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Rotate a virtual key
        api_response = api_instance.arc_rotate_virtual_key(key_id, arc_rotate_virtual_key_request=arc_rotate_virtual_key_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_rotate_virtual_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the virtual key. |
 **arc_rotate_virtual_key_request** | [**ArcRotateVirtualKeyRequest**](ArcRotateVirtualKeyRequest.md)|  | [optional]

### Return type

[**ArcRotateVirtualKeyResponse**](ArcRotateVirtualKeyResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The virtual key was rotated. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_update_virtual_key**
> ArcUpdateVirtualKeyResponse arc_update_virtual_key(key_id, arc_update_virtual_key_request)

Update a virtual key

Update the attributes of a virtual key. Only the fields you include are changed.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_update_virtual_key_response import ArcUpdateVirtualKeyResponse
from fastly.model.arc_update_virtual_key_request import ArcUpdateVirtualKeyRequest
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    key_id = "7fVVQb1nZaJgnzCn4B4v3B" # str | The ID of the virtual key.
    arc_update_virtual_key_request = ArcUpdateVirtualKeyRequest(
        name="production-anthropic-key",
        expires_at=dateutil_parser('2027-01-01T00:00:00Z'),
        security_enabled=True,
        security_action="log",
        rpm_limit=60,
        tpm_limit=100000,
        spend_limit_enabled=True,
    ) # ArcUpdateVirtualKeyRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a virtual key
        api_response = api_instance.arc_update_virtual_key(key_id, arc_update_virtual_key_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_update_virtual_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the virtual key. |
 **arc_update_virtual_key_request** | [**ArcUpdateVirtualKeyRequest**](ArcUpdateVirtualKeyRequest.md)|  |

### Return type

[**ArcUpdateVirtualKeyResponse**](ArcUpdateVirtualKeyResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The virtual key was updated. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **arc_update_virtual_key_failover**
> ArcVirtualKeyFailoverResponse arc_update_virtual_key_failover(key_id, arc_virtual_key_failover_request)

Update a virtual key's failover policy

Replace the failover policy for a virtual key.  Failover is a per-account feature. If it isn't enabled on your account, this endpoint returns a 404 response. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ai_runtime_control_virtual_keys_api
from fastly.model.arc_virtual_key_failover_response import ArcVirtualKeyFailoverResponse
from fastly.model.arc_error import ArcError
from fastly.model.arc_virtual_key_failover_request import ArcVirtualKeyFailoverRequest
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
    api_instance = ai_runtime_control_virtual_keys_api.AiRuntimeControlVirtualKeysApi(api_client)
    key_id = "7fVVQb1nZaJgnzCn4B4v3B" # str | The ID of the virtual key.
    arc_virtual_key_failover_request = ArcVirtualKeyFailoverRequest(
        targets=[
            ArcFailoverTarget(
                provider_connection_id="pTfnUUBcU1yv8SoRJn5PZ2",
            ),
        ],
        timeout_enabled=True,
        rate_limit_429_enabled=True,
        server_error_5xx_enabled=True,
    ) # ArcVirtualKeyFailoverRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Update a virtual key's failover policy
        api_response = api_instance.arc_update_virtual_key_failover(key_id, arc_virtual_key_failover_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AiRuntimeControlVirtualKeysApi->arc_update_virtual_key_failover: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**| The ID of the virtual key. |
 **arc_virtual_key_failover_request** | [**ArcVirtualKeyFailoverRequest**](ArcVirtualKeyFailoverRequest.md)|  |

### Return type

[**ArcVirtualKeyFailoverResponse**](ArcVirtualKeyFailoverResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The virtual key&#39;s failover policy. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | Customer is not entitled to AI Runtime Control. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

