# fastly.LoggingPapertrailApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_papertrail**](LoggingPapertrailApi.md#create_log_papertrail) | **POST** /service/{service_id}/version/{version_id}/logging/papertrail | Create a Papertrail log endpoint
[**delete_log_papertrail**](LoggingPapertrailApi.md#delete_log_papertrail) | **DELETE** /service/{service_id}/version/{version_id}/logging/papertrail/{logging_papertrail_name} | Delete a Papertrail log endpoint
[**get_log_papertrail**](LoggingPapertrailApi.md#get_log_papertrail) | **GET** /service/{service_id}/version/{version_id}/logging/papertrail/{logging_papertrail_name} | Get a Papertrail log endpoint
[**list_log_papertrail**](LoggingPapertrailApi.md#list_log_papertrail) | **GET** /service/{service_id}/version/{version_id}/logging/papertrail | List Papertrail log endpoints
[**update_log_papertrail**](LoggingPapertrailApi.md#update_log_papertrail) | **PUT** /service/{service_id}/version/{version_id}/logging/papertrail/{logging_papertrail_name} | Update a Papertrail log endpoint


# **create_log_papertrail**
> LoggingPapertrailResponse create_log_papertrail(service_id, version_id)

Create a Papertrail log endpoint

Create a Papertrail for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_papertrail_api
from fastly.model.logging_papertrail_response import LoggingPapertrailResponse
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
    api_instance = logging_papertrail_api.LoggingPapertrailApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    address = "example.com" # str | A hostname or IPv4 address. (optional)
    port = 514 # int | The port number. (optional) if omitted the server will use the default value of 514

    # example passing only required values which don't have defaults set
    try:
        # Create a Papertrail log endpoint
        api_response = api_instance.create_log_papertrail(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->create_log_papertrail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Papertrail log endpoint
        api_response = api_instance.create_log_papertrail(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, address=address, port=port)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->create_log_papertrail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **address** | **str**| A hostname or IPv4 address. | [optional]
 **port** | **int**| The port number. | [optional] if omitted the server will use the default value of 514

### Return type

[**LoggingPapertrailResponse**](LoggingPapertrailResponse.md)

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

# **delete_log_papertrail**
> InlineResponse200 delete_log_papertrail(service_id, version_id, logging_papertrail_name)

Delete a Papertrail log endpoint

Delete the Papertrail for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_papertrail_api
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
    api_instance = logging_papertrail_api.LoggingPapertrailApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_papertrail_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Papertrail log endpoint
        api_response = api_instance.delete_log_papertrail(service_id, version_id, logging_papertrail_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->delete_log_papertrail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_papertrail_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_papertrail**
> LoggingPapertrailResponse get_log_papertrail(service_id, version_id, logging_papertrail_name)

Get a Papertrail log endpoint

Get the Papertrail for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_papertrail_api
from fastly.model.logging_papertrail_response import LoggingPapertrailResponse
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
    api_instance = logging_papertrail_api.LoggingPapertrailApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_papertrail_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a Papertrail log endpoint
        api_response = api_instance.get_log_papertrail(service_id, version_id, logging_papertrail_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->get_log_papertrail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_papertrail_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingPapertrailResponse**](LoggingPapertrailResponse.md)

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

# **list_log_papertrail**
> [LoggingPapertrailResponse] list_log_papertrail(service_id, version_id)

List Papertrail log endpoints

List all of the Papertrails for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_papertrail_api
from fastly.model.logging_papertrail_response import LoggingPapertrailResponse
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
    api_instance = logging_papertrail_api.LoggingPapertrailApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Papertrail log endpoints
        api_response = api_instance.list_log_papertrail(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->list_log_papertrail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingPapertrailResponse]**](LoggingPapertrailResponse.md)

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

# **update_log_papertrail**
> LoggingPapertrailResponse update_log_papertrail(service_id, version_id, logging_papertrail_name)

Update a Papertrail log endpoint

Update the Papertrail for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_papertrail_api
from fastly.model.logging_papertrail_response import LoggingPapertrailResponse
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
    api_instance = logging_papertrail_api.LoggingPapertrailApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_papertrail_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    address = "example.com" # str | A hostname or IPv4 address. (optional)
    port = 514 # int | The port number. (optional) if omitted the server will use the default value of 514

    # example passing only required values which don't have defaults set
    try:
        # Update a Papertrail log endpoint
        api_response = api_instance.update_log_papertrail(service_id, version_id, logging_papertrail_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->update_log_papertrail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Papertrail log endpoint
        api_response = api_instance.update_log_papertrail(service_id, version_id, logging_papertrail_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, address=address, port=port)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingPapertrailApi->update_log_papertrail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_papertrail_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **address** | **str**| A hostname or IPv4 address. | [optional]
 **port** | **int**| The port number. | [optional] if omitted the server will use the default value of 514

### Return type

[**LoggingPapertrailResponse**](LoggingPapertrailResponse.md)

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

