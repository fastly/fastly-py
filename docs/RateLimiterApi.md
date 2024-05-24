# fastly.RateLimiterApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rate_limiter**](RateLimiterApi.md#create_rate_limiter) | **POST** /service/{service_id}/version/{version_id}/rate-limiters | Create a rate limiter
[**delete_rate_limiter**](RateLimiterApi.md#delete_rate_limiter) | **DELETE** /rate-limiters/{rate_limiter_id} | Delete a rate limiter
[**get_rate_limiter**](RateLimiterApi.md#get_rate_limiter) | **GET** /rate-limiters/{rate_limiter_id} | Get a rate limiter
[**list_rate_limiters**](RateLimiterApi.md#list_rate_limiters) | **GET** /service/{service_id}/version/{version_id}/rate-limiters | List rate limiters
[**update_rate_limiter**](RateLimiterApi.md#update_rate_limiter) | **PUT** /rate-limiters/{rate_limiter_id} | Update a rate limiter


# **create_rate_limiter**
> RateLimiterResponse create_rate_limiter(service_id, version_id)

Create a rate limiter

Create a rate limiter for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import rate_limiter_api
from fastly.model.rate_limiter_response import RateLimiterResponse
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
    api_instance = rate_limiter_api.RateLimiterApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "name_example" # str | A human readable name for the rate limiting rule. (optional)
    uri_dictionary_name = "uri_dictionary_name_example" # str, none_type | The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited. (optional)
    http_methods = [
        "HEAD",
    ] # [str] | Array of HTTP methods to apply rate limiting to. (optional)
    rps_limit = 10 # int | Upper limit of requests per second allowed by the rate limiter. (optional)
    window_size = 1 # int | Number of seconds during which the RPS limit must be exceeded in order to trigger a violation. (optional)
    client_key = [
        "client_key_example",
    ] # [str] | Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`. (optional)
    penalty_box_duration = 1 # int | Length of time in minutes that the rate limiter is in effect after the initial violation is detected. (optional)
    action = "response" # str | The action to take when a rate limiter violation is detected. (optional)
    response_object_name = "response_object_name_example" # str, none_type | Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration. (optional)
    logger_type = "azureblob" # str | Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries. (optional)
    feature_revision = 1 # int | Revision number of the rate limiting feature implementation. Defaults to the most recent revision. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a rate limiter
        api_response = api_instance.create_rate_limiter(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->create_rate_limiter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a rate limiter
        api_response = api_instance.create_rate_limiter(service_id, version_id, name=name, uri_dictionary_name=uri_dictionary_name, http_methods=http_methods, rps_limit=rps_limit, window_size=window_size, client_key=client_key, penalty_box_duration=penalty_box_duration, action=action, response_object_name=response_object_name, logger_type=logger_type, feature_revision=feature_revision)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->create_rate_limiter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| A human readable name for the rate limiting rule. | [optional]
 **uri_dictionary_name** | **str, none_type**| The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited. | [optional]
 **http_methods** | **[str]**| Array of HTTP methods to apply rate limiting to. | [optional]
 **rps_limit** | **int**| Upper limit of requests per second allowed by the rate limiter. | [optional]
 **window_size** | **int**| Number of seconds during which the RPS limit must be exceeded in order to trigger a violation. | [optional]
 **client_key** | **[str]**| Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`. | [optional]
 **penalty_box_duration** | **int**| Length of time in minutes that the rate limiter is in effect after the initial violation is detected. | [optional]
 **action** | **str**| The action to take when a rate limiter violation is detected. | [optional]
 **response_object_name** | **str, none_type**| Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration. | [optional]
 **logger_type** | **str**| Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries. | [optional]
 **feature_revision** | **int**| Revision number of the rate limiting feature implementation. Defaults to the most recent revision. | [optional]

### Return type

[**RateLimiterResponse**](RateLimiterResponse.md)

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

# **delete_rate_limiter**
> InlineResponse200 delete_rate_limiter(rate_limiter_id)

Delete a rate limiter

Delete a rate limiter by its ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import rate_limiter_api
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
    api_instance = rate_limiter_api.RateLimiterApi(api_client)
    rate_limiter_id = "s7aqgcJjqqKhwiTRMaP11" # str | Alphanumeric string identifying the rate limiter.

    # example passing only required values which don't have defaults set
    try:
        # Delete a rate limiter
        api_response = api_instance.delete_rate_limiter(rate_limiter_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->delete_rate_limiter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limiter_id** | **str**| Alphanumeric string identifying the rate limiter. |

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

# **get_rate_limiter**
> RateLimiterResponse get_rate_limiter(rate_limiter_id)

Get a rate limiter

Get a rate limiter by its ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import rate_limiter_api
from fastly.model.rate_limiter_response import RateLimiterResponse
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
    api_instance = rate_limiter_api.RateLimiterApi(api_client)
    rate_limiter_id = "s7aqgcJjqqKhwiTRMaP11" # str | Alphanumeric string identifying the rate limiter.

    # example passing only required values which don't have defaults set
    try:
        # Get a rate limiter
        api_response = api_instance.get_rate_limiter(rate_limiter_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->get_rate_limiter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limiter_id** | **str**| Alphanumeric string identifying the rate limiter. |

### Return type

[**RateLimiterResponse**](RateLimiterResponse.md)

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

# **list_rate_limiters**
> [RateLimiterResponse] list_rate_limiters(service_id, version_id)

List rate limiters

List all rate limiters for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import rate_limiter_api
from fastly.model.rate_limiter_response import RateLimiterResponse
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
    api_instance = rate_limiter_api.RateLimiterApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List rate limiters
        api_response = api_instance.list_rate_limiters(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->list_rate_limiters: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[RateLimiterResponse]**](RateLimiterResponse.md)

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

# **update_rate_limiter**
> RateLimiterResponse update_rate_limiter(rate_limiter_id)

Update a rate limiter

Update a rate limiter by its ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import rate_limiter_api
from fastly.model.rate_limiter_response import RateLimiterResponse
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
    api_instance = rate_limiter_api.RateLimiterApi(api_client)
    rate_limiter_id = "s7aqgcJjqqKhwiTRMaP11" # str | Alphanumeric string identifying the rate limiter.
    name = "name_example" # str | A human readable name for the rate limiting rule. (optional)
    uri_dictionary_name = "uri_dictionary_name_example" # str, none_type | The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited. (optional)
    http_methods = [
        "HEAD",
    ] # [str] | Array of HTTP methods to apply rate limiting to. (optional)
    rps_limit = 10 # int | Upper limit of requests per second allowed by the rate limiter. (optional)
    window_size = 1 # int | Number of seconds during which the RPS limit must be exceeded in order to trigger a violation. (optional)
    client_key = [
        "client_key_example",
    ] # [str] | Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`. (optional)
    penalty_box_duration = 1 # int | Length of time in minutes that the rate limiter is in effect after the initial violation is detected. (optional)
    action = "response" # str | The action to take when a rate limiter violation is detected. (optional)
    response_object_name = "response_object_name_example" # str, none_type | Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration. (optional)
    logger_type = "azureblob" # str | Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries. (optional)
    feature_revision = 1 # int | Revision number of the rate limiting feature implementation. Defaults to the most recent revision. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a rate limiter
        api_response = api_instance.update_rate_limiter(rate_limiter_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->update_rate_limiter: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a rate limiter
        api_response = api_instance.update_rate_limiter(rate_limiter_id, name=name, uri_dictionary_name=uri_dictionary_name, http_methods=http_methods, rps_limit=rps_limit, window_size=window_size, client_key=client_key, penalty_box_duration=penalty_box_duration, action=action, response_object_name=response_object_name, logger_type=logger_type, feature_revision=feature_revision)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling RateLimiterApi->update_rate_limiter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rate_limiter_id** | **str**| Alphanumeric string identifying the rate limiter. |
 **name** | **str**| A human readable name for the rate limiting rule. | [optional]
 **uri_dictionary_name** | **str, none_type**| The name of an Edge Dictionary containing URIs as keys. If not defined or `null`, all origin URIs will be rate limited. | [optional]
 **http_methods** | **[str]**| Array of HTTP methods to apply rate limiting to. | [optional]
 **rps_limit** | **int**| Upper limit of requests per second allowed by the rate limiter. | [optional]
 **window_size** | **int**| Number of seconds during which the RPS limit must be exceeded in order to trigger a violation. | [optional]
 **client_key** | **[str]**| Array of VCL variables used to generate a counter key to identify a client. Example variables include `req.http.Fastly-Client-IP`, `req.http.User-Agent`, or a custom header like `req.http.API-Key`. | [optional]
 **penalty_box_duration** | **int**| Length of time in minutes that the rate limiter is in effect after the initial violation is detected. | [optional]
 **action** | **str**| The action to take when a rate limiter violation is detected. | [optional]
 **response_object_name** | **str, none_type**| Name of existing response object. Required if `action` is `response_object`. Note that the rate limiter response is only updated to reflect the response object content when saving the rate limiter configuration. | [optional]
 **logger_type** | **str**| Name of the type of logging endpoint to be used when action is `log_only`. The logging endpoint type is used to determine the appropriate log format to use when emitting log entries. | [optional]
 **feature_revision** | **int**| Revision number of the rate limiting feature implementation. Defaults to the most recent revision. | [optional]

### Return type

[**RateLimiterResponse**](RateLimiterResponse.md)

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

