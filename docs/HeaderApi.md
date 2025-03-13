# fastly.HeaderApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_header_object**](HeaderApi.md#create_header_object) | **POST** /service/{service_id}/version/{version_id}/header | Create a Header object
[**delete_header_object**](HeaderApi.md#delete_header_object) | **DELETE** /service/{service_id}/version/{version_id}/header/{header_name} | Delete a Header object
[**get_header_object**](HeaderApi.md#get_header_object) | **GET** /service/{service_id}/version/{version_id}/header/{header_name} | Get a Header object
[**list_header_objects**](HeaderApi.md#list_header_objects) | **GET** /service/{service_id}/version/{version_id}/header | List Header objects
[**update_header_object**](HeaderApi.md#update_header_object) | **PUT** /service/{service_id}/version/{version_id}/header/{header_name} | Update a Header object


# **create_header_object**
> HeaderResponse create_header_object(service_id, version_id)

Create a Header object

Creates a new Header object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import header_api
from fastly.model.header_response import HeaderResponse
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
    api_instance = header_api.HeaderApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    action = "set" # str | Accepts a string value. (optional)
    cache_condition = "cache_condition_example" # str, none_type | Name of the cache condition controlling when this configuration applies. (optional)
    dst = "dst_example" # str | Header to set. (optional)
    name = "test-header" # str | A handle to refer to this Header object. (optional)
    regex = "regex_example" # str, none_type | Regular expression to use. Only applies to `regex` and `regex_repeat` actions. (optional)
    request_condition = "request_condition_example" # str, none_type | Condition which, if met, will select this configuration during a request. Optional. (optional)
    response_condition = "response_condition_example" # str, none_type | Optional name of a response condition to apply. (optional)
    src = "src_example" # str, none_type | Variable to be used as a source for the header content. Does not apply to `delete` action. (optional)
    substitution = "substitution_example" # str, none_type | Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions. (optional)
    type = "request" # str | Accepts a string value. (optional)
    ignore_if_set = "ignore_if_set_example" # str | Don't add the header if it is added already. Only applies to 'set' action. Numerical value (\\\"0\\\" = false, \\\"1\\\" = true) (optional)
    priority = "100" # str | Priority determines execution order. Lower numbers execute first. (optional) if omitted the server will use the default value of "100"

    # example passing only required values which don't have defaults set
    try:
        # Create a Header object
        api_response = api_instance.create_header_object(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->create_header_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Header object
        api_response = api_instance.create_header_object(service_id, version_id, action=action, cache_condition=cache_condition, dst=dst, name=name, regex=regex, request_condition=request_condition, response_condition=response_condition, src=src, substitution=substitution, type=type, ignore_if_set=ignore_if_set, priority=priority)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->create_header_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **action** | **str**| Accepts a string value. | [optional]
 **cache_condition** | **str, none_type**| Name of the cache condition controlling when this configuration applies. | [optional]
 **dst** | **str**| Header to set. | [optional]
 **name** | **str**| A handle to refer to this Header object. | [optional]
 **regex** | **str, none_type**| Regular expression to use. Only applies to `regex` and `regex_repeat` actions. | [optional]
 **request_condition** | **str, none_type**| Condition which, if met, will select this configuration during a request. Optional. | [optional]
 **response_condition** | **str, none_type**| Optional name of a response condition to apply. | [optional]
 **src** | **str, none_type**| Variable to be used as a source for the header content. Does not apply to `delete` action. | [optional]
 **substitution** | **str, none_type**| Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions. | [optional]
 **type** | **str**| Accepts a string value. | [optional]
 **ignore_if_set** | **str**| Don&#39;t add the header if it is added already. Only applies to &#39;set&#39; action. Numerical value (\\\&quot;0\\\&quot; &#x3D; false, \\\&quot;1\\\&quot; &#x3D; true) | [optional]
 **priority** | **str**| Priority determines execution order. Lower numbers execute first. | [optional] if omitted the server will use the default value of "100"

### Return type

[**HeaderResponse**](HeaderResponse.md)

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

# **delete_header_object**
> InlineResponse200 delete_header_object(service_id, version_id, header_name)

Delete a Header object

Deletes a Header object by name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import header_api
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
    api_instance = header_api.HeaderApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    header_name = "test-header" # str | A handle to refer to this Header object.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Header object
        api_response = api_instance.delete_header_object(service_id, version_id, header_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->delete_header_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **header_name** | **str**| A handle to refer to this Header object. |

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

# **get_header_object**
> HeaderResponse get_header_object(service_id, version_id, header_name)

Get a Header object

Retrieves a Header object by name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import header_api
from fastly.model.header_response import HeaderResponse
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
    api_instance = header_api.HeaderApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    header_name = "test-header" # str | A handle to refer to this Header object.

    # example passing only required values which don't have defaults set
    try:
        # Get a Header object
        api_response = api_instance.get_header_object(service_id, version_id, header_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->get_header_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **header_name** | **str**| A handle to refer to this Header object. |

### Return type

[**HeaderResponse**](HeaderResponse.md)

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

# **list_header_objects**
> [HeaderResponse] list_header_objects(service_id, version_id)

List Header objects

Retrieves all Header objects for a particular Version of a Service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import header_api
from fastly.model.header_response import HeaderResponse
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
    api_instance = header_api.HeaderApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Header objects
        api_response = api_instance.list_header_objects(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->list_header_objects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[HeaderResponse]**](HeaderResponse.md)

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

# **update_header_object**
> HeaderResponse update_header_object(service_id, version_id, header_name)

Update a Header object

Modifies an existing Header object by name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import header_api
from fastly.model.header_response import HeaderResponse
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
    api_instance = header_api.HeaderApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    header_name = "test-header" # str | A handle to refer to this Header object.
    action = "set" # str | Accepts a string value. (optional)
    cache_condition = "cache_condition_example" # str, none_type | Name of the cache condition controlling when this configuration applies. (optional)
    dst = "dst_example" # str | Header to set. (optional)
    name = "test-header" # str | A handle to refer to this Header object. (optional)
    regex = "regex_example" # str, none_type | Regular expression to use. Only applies to `regex` and `regex_repeat` actions. (optional)
    request_condition = "request_condition_example" # str, none_type | Condition which, if met, will select this configuration during a request. Optional. (optional)
    response_condition = "response_condition_example" # str, none_type | Optional name of a response condition to apply. (optional)
    src = "src_example" # str, none_type | Variable to be used as a source for the header content. Does not apply to `delete` action. (optional)
    substitution = "substitution_example" # str, none_type | Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions. (optional)
    type = "request" # str | Accepts a string value. (optional)
    ignore_if_set = "ignore_if_set_example" # str | Don't add the header if it is added already. Only applies to 'set' action. Numerical value (\\\"0\\\" = false, \\\"1\\\" = true) (optional)
    priority = "100" # str | Priority determines execution order. Lower numbers execute first. (optional) if omitted the server will use the default value of "100"

    # example passing only required values which don't have defaults set
    try:
        # Update a Header object
        api_response = api_instance.update_header_object(service_id, version_id, header_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->update_header_object: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Header object
        api_response = api_instance.update_header_object(service_id, version_id, header_name, action=action, cache_condition=cache_condition, dst=dst, name=name, regex=regex, request_condition=request_condition, response_condition=response_condition, src=src, substitution=substitution, type=type, ignore_if_set=ignore_if_set, priority=priority)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HeaderApi->update_header_object: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **header_name** | **str**| A handle to refer to this Header object. |
 **action** | **str**| Accepts a string value. | [optional]
 **cache_condition** | **str, none_type**| Name of the cache condition controlling when this configuration applies. | [optional]
 **dst** | **str**| Header to set. | [optional]
 **name** | **str**| A handle to refer to this Header object. | [optional]
 **regex** | **str, none_type**| Regular expression to use. Only applies to `regex` and `regex_repeat` actions. | [optional]
 **request_condition** | **str, none_type**| Condition which, if met, will select this configuration during a request. Optional. | [optional]
 **response_condition** | **str, none_type**| Optional name of a response condition to apply. | [optional]
 **src** | **str, none_type**| Variable to be used as a source for the header content. Does not apply to `delete` action. | [optional]
 **substitution** | **str, none_type**| Value to substitute in place of regular expression. Only applies to `regex` and `regex_repeat` actions. | [optional]
 **type** | **str**| Accepts a string value. | [optional]
 **ignore_if_set** | **str**| Don&#39;t add the header if it is added already. Only applies to &#39;set&#39; action. Numerical value (\\\&quot;0\\\&quot; &#x3D; false, \\\&quot;1\\\&quot; &#x3D; true) | [optional]
 **priority** | **str**| Priority determines execution order. Lower numbers execute first. | [optional] if omitted the server will use the default value of "100"

### Return type

[**HeaderResponse**](HeaderResponse.md)

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

