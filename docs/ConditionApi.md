# fastly.ConditionApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_condition**](ConditionApi.md#create_condition) | **POST** /service/{service_id}/version/{version_id}/condition | Create a condition
[**delete_condition**](ConditionApi.md#delete_condition) | **DELETE** /service/{service_id}/version/{version_id}/condition/{condition_name} | Delete a condition
[**get_condition**](ConditionApi.md#get_condition) | **GET** /service/{service_id}/version/{version_id}/condition/{condition_name} | Describe a condition
[**list_conditions**](ConditionApi.md#list_conditions) | **GET** /service/{service_id}/version/{version_id}/condition | List conditions
[**update_condition**](ConditionApi.md#update_condition) | **PUT** /service/{service_id}/version/{version_id}/condition/{condition_name} | Update a condition


# **create_condition**
> ConditionResponse create_condition(service_id, version_id)

Create a condition

Creates a new condition.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import condition_api
from fastly.model.condition_response import ConditionResponse
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
    api_instance = condition_api.ConditionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "test-condition" # str | Name of the condition. Required. (optional)
    priority = "10" # str | A numeric string. Priority determines execution order. Lower numbers execute first. (optional) if omitted the server will use the default value of "100"
    statement = "statement_example" # str | A conditional expression in VCL used to determine if the condition is met. (optional)
    service_id2 = "service_id_example" # str |  (optional)
    version = "version_example" # str | A numeric string that represents the service version. (optional)
    type = "REQUEST" # str | Type of the condition. Required. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a condition
        api_response = api_instance.create_condition(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->create_condition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a condition
        api_response = api_instance.create_condition(service_id, version_id, comment=comment, name=name, priority=priority, statement=statement, service_id2=service_id2, version=version, type=type)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->create_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| Name of the condition. Required. | [optional]
 **priority** | **str**| A numeric string. Priority determines execution order. Lower numbers execute first. | [optional] if omitted the server will use the default value of "100"
 **statement** | **str**| A conditional expression in VCL used to determine if the condition is met. | [optional]
 **service_id2** | **str**|  | [optional]
 **version** | **str**| A numeric string that represents the service version. | [optional]
 **type** | **str**| Type of the condition. Required. | [optional]

### Return type

[**ConditionResponse**](ConditionResponse.md)

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

# **delete_condition**
> InlineResponse200 delete_condition(service_id, version_id, condition_name)

Delete a condition

Deletes the specified condition.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import condition_api
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
    api_instance = condition_api.ConditionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    condition_name = "test-condition" # str | Name of the condition. Required.

    # example passing only required values which don't have defaults set
    try:
        # Delete a condition
        api_response = api_instance.delete_condition(service_id, version_id, condition_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->delete_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **condition_name** | **str**| Name of the condition. Required. |

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

# **get_condition**
> ConditionResponse get_condition(service_id, version_id, condition_name)

Describe a condition

Gets the specified condition.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import condition_api
from fastly.model.condition_response import ConditionResponse
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
    api_instance = condition_api.ConditionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    condition_name = "test-condition" # str | Name of the condition. Required.

    # example passing only required values which don't have defaults set
    try:
        # Describe a condition
        api_response = api_instance.get_condition(service_id, version_id, condition_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->get_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **condition_name** | **str**| Name of the condition. Required. |

### Return type

[**ConditionResponse**](ConditionResponse.md)

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

# **list_conditions**
> ConditionsResponse list_conditions(service_id, version_id)

List conditions

Gets all conditions for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import condition_api
from fastly.model.conditions_response import ConditionsResponse
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
    api_instance = condition_api.ConditionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List conditions
        api_response = api_instance.list_conditions(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->list_conditions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**ConditionsResponse**](ConditionsResponse.md)

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

# **update_condition**
> ConditionResponse update_condition(service_id, version_id, condition_name)

Update a condition

Updates the specified condition.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import condition_api
from fastly.model.condition_response import ConditionResponse
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
    api_instance = condition_api.ConditionApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    condition_name = "test-condition" # str | Name of the condition. Required.
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "test-condition" # str | Name of the condition. Required. (optional)
    priority = "10" # str | A numeric string. Priority determines execution order. Lower numbers execute first. (optional) if omitted the server will use the default value of "100"
    statement = "statement_example" # str | A conditional expression in VCL used to determine if the condition is met. (optional)
    service_id2 = "service_id_example" # str |  (optional)
    version = "version_example" # str | A numeric string that represents the service version. (optional)
    type = "REQUEST" # str | Type of the condition. Required. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a condition
        api_response = api_instance.update_condition(service_id, version_id, condition_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->update_condition: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a condition
        api_response = api_instance.update_condition(service_id, version_id, condition_name, comment=comment, name=name, priority=priority, statement=statement, service_id2=service_id2, version=version, type=type)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ConditionApi->update_condition: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **condition_name** | **str**| Name of the condition. Required. |
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| Name of the condition. Required. | [optional]
 **priority** | **str**| A numeric string. Priority determines execution order. Lower numbers execute first. | [optional] if omitted the server will use the default value of "100"
 **statement** | **str**| A conditional expression in VCL used to determine if the condition is met. | [optional]
 **service_id2** | **str**|  | [optional]
 **version** | **str**| A numeric string that represents the service version. | [optional]
 **type** | **str**| Type of the condition. Required. | [optional]

### Return type

[**ConditionResponse**](ConditionResponse.md)

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

