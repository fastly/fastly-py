# fastly.LoggingSplunkApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_splunk**](LoggingSplunkApi.md#create_log_splunk) | **POST** /service/{service_id}/version/{version_id}/logging/splunk | Create a Splunk log endpoint
[**delete_log_splunk**](LoggingSplunkApi.md#delete_log_splunk) | **DELETE** /service/{service_id}/version/{version_id}/logging/splunk/{logging_splunk_name} | Delete a Splunk log endpoint
[**get_log_splunk**](LoggingSplunkApi.md#get_log_splunk) | **GET** /service/{service_id}/version/{version_id}/logging/splunk/{logging_splunk_name} | Get a Splunk log endpoint
[**list_log_splunk**](LoggingSplunkApi.md#list_log_splunk) | **GET** /service/{service_id}/version/{version_id}/logging/splunk | List Splunk log endpoints
[**update_log_splunk**](LoggingSplunkApi.md#update_log_splunk) | **PUT** /service/{service_id}/version/{version_id}/logging/splunk/{logging_splunk_name} | Update a Splunk log endpoint


# **create_log_splunk**
> LoggingSplunkResponse create_log_splunk(service_id, version_id)

Create a Splunk log endpoint

Create a Splunk logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_splunk_api
from fastly.model.logging_use_tls_string import LoggingUseTlsString
from fastly.model.logging_splunk_response import LoggingSplunkResponse
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
    api_instance = logging_splunk_api.LoggingSplunkApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_hostname = "null" # str, none_type | The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. (optional) if omitted the server will use the default value of "null"
    request_max_entries = 0 # int | The maximum number of logs sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    request_max_bytes = 0 # int | The maximum number of bytes sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    url = "url_example" # str | The URL to post logs to. (optional)
    token = "token_example" # str | A Splunk token for use in posting logs over HTTP to your collector. (optional)
    use_tls = LoggingUseTlsString("0") # LoggingUseTlsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Splunk log endpoint
        api_response = api_instance.create_log_splunk(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->create_log_splunk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Splunk log endpoint
        api_response = api_instance.create_log_splunk(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, request_max_entries=request_max_entries, request_max_bytes=request_max_bytes, url=url, token=token, use_tls=use_tls)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->create_log_splunk: %s\n" % e)
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
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_hostname** | **str, none_type**| The hostname to verify the server&#39;s certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. | [optional] if omitted the server will use the default value of "null"
 **request_max_entries** | **int**| The maximum number of logs sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **request_max_bytes** | **int**| The maximum number of bytes sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **url** | **str**| The URL to post logs to. | [optional]
 **token** | **str**| A Splunk token for use in posting logs over HTTP to your collector. | [optional]
 **use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md)|  | [optional]

### Return type

[**LoggingSplunkResponse**](LoggingSplunkResponse.md)

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

# **delete_log_splunk**
> InlineResponse200 delete_log_splunk(service_id, version_id, logging_splunk_name)

Delete a Splunk log endpoint

Delete the Splunk logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_splunk_api
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
    api_instance = logging_splunk_api.LoggingSplunkApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_splunk_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Splunk log endpoint
        api_response = api_instance.delete_log_splunk(service_id, version_id, logging_splunk_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->delete_log_splunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_splunk_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_splunk**
> LoggingSplunkResponse get_log_splunk(service_id, version_id, logging_splunk_name)

Get a Splunk log endpoint

Get the details for a Splunk logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_splunk_api
from fastly.model.logging_splunk_response import LoggingSplunkResponse
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
    api_instance = logging_splunk_api.LoggingSplunkApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_splunk_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a Splunk log endpoint
        api_response = api_instance.get_log_splunk(service_id, version_id, logging_splunk_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->get_log_splunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_splunk_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingSplunkResponse**](LoggingSplunkResponse.md)

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

# **list_log_splunk**
> [LoggingSplunkResponse] list_log_splunk(service_id, version_id)

List Splunk log endpoints

List all of the Splunk logging objects for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_splunk_api
from fastly.model.logging_splunk_response import LoggingSplunkResponse
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
    api_instance = logging_splunk_api.LoggingSplunkApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Splunk log endpoints
        api_response = api_instance.list_log_splunk(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->list_log_splunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingSplunkResponse]**](LoggingSplunkResponse.md)

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

# **update_log_splunk**
> LoggingSplunkResponse update_log_splunk(service_id, version_id, logging_splunk_name)

Update a Splunk log endpoint

Update the Splunk logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_splunk_api
from fastly.model.logging_use_tls_string import LoggingUseTlsString
from fastly.model.logging_splunk_response import LoggingSplunkResponse
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
    api_instance = logging_splunk_api.LoggingSplunkApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_splunk_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_hostname = "null" # str, none_type | The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. (optional) if omitted the server will use the default value of "null"
    request_max_entries = 0 # int | The maximum number of logs sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    request_max_bytes = 0 # int | The maximum number of bytes sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    url = "url_example" # str | The URL to post logs to. (optional)
    token = "token_example" # str | A Splunk token for use in posting logs over HTTP to your collector. (optional)
    use_tls = LoggingUseTlsString("0") # LoggingUseTlsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Splunk log endpoint
        api_response = api_instance.update_log_splunk(service_id, version_id, logging_splunk_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->update_log_splunk: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Splunk log endpoint
        api_response = api_instance.update_log_splunk(service_id, version_id, logging_splunk_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, request_max_entries=request_max_entries, request_max_bytes=request_max_bytes, url=url, token=token, use_tls=use_tls)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSplunkApi->update_log_splunk: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_splunk_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_hostname** | **str, none_type**| The hostname to verify the server&#39;s certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. | [optional] if omitted the server will use the default value of "null"
 **request_max_entries** | **int**| The maximum number of logs sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **request_max_bytes** | **int**| The maximum number of bytes sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **url** | **str**| The URL to post logs to. | [optional]
 **token** | **str**| A Splunk token for use in posting logs over HTTP to your collector. | [optional]
 **use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md)|  | [optional]

### Return type

[**LoggingSplunkResponse**](LoggingSplunkResponse.md)

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

