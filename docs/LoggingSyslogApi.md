# fastly.LoggingSyslogApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_syslog**](LoggingSyslogApi.md#create_log_syslog) | **POST** /service/{service_id}/version/{version_id}/logging/syslog | Create a syslog log endpoint
[**delete_log_syslog**](LoggingSyslogApi.md#delete_log_syslog) | **DELETE** /service/{service_id}/version/{version_id}/logging/syslog/{logging_syslog_name} | Delete a syslog log endpoint
[**get_log_syslog**](LoggingSyslogApi.md#get_log_syslog) | **GET** /service/{service_id}/version/{version_id}/logging/syslog/{logging_syslog_name} | Get a syslog log endpoint
[**list_log_syslog**](LoggingSyslogApi.md#list_log_syslog) | **GET** /service/{service_id}/version/{version_id}/logging/syslog | List Syslog log endpoints
[**update_log_syslog**](LoggingSyslogApi.md#update_log_syslog) | **PUT** /service/{service_id}/version/{version_id}/logging/syslog/{logging_syslog_name} | Update a syslog log endpoint


# **create_log_syslog**
> LoggingSyslogResponse create_log_syslog(service_id, version_id)

Create a syslog log endpoint

Create a Syslog for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_syslog_api
from fastly.model.logging_use_tls_string import LoggingUseTlsString
from fastly.model.logging_message_type import LoggingMessageType
from fastly.model.logging_syslog_response import LoggingSyslogResponse
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
    api_instance = logging_syslog_api.LoggingSyslogApi(api_client)
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
    address = "example.com" # str | A hostname or IPv4 address. (optional)
    port = 514 # int | The port number. (optional) if omitted the server will use the default value of 514
    message_type = LoggingMessageType("classic") # LoggingMessageType |  (optional)
    hostname = "hostname_example" # str | The hostname used for the syslog endpoint. (optional)
    ipv4 = "ipv4_example" # str, none_type | The IPv4 address used for the syslog endpoint. (optional)
    token = "null" # str, none_type | Whether to prepend each message with a specific token. (optional) if omitted the server will use the default value of "null"
    use_tls = LoggingUseTlsString("0") # LoggingUseTlsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a syslog log endpoint
        api_response = api_instance.create_log_syslog(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->create_log_syslog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a syslog log endpoint
        api_response = api_instance.create_log_syslog(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, address=address, port=port, message_type=message_type, hostname=hostname, ipv4=ipv4, token=token, use_tls=use_tls)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->create_log_syslog: %s\n" % e)
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
 **address** | **str**| A hostname or IPv4 address. | [optional]
 **port** | **int**| The port number. | [optional] if omitted the server will use the default value of 514
 **message_type** | [**LoggingMessageType**](LoggingMessageType.md)|  | [optional]
 **hostname** | **str**| The hostname used for the syslog endpoint. | [optional]
 **ipv4** | **str, none_type**| The IPv4 address used for the syslog endpoint. | [optional]
 **token** | **str, none_type**| Whether to prepend each message with a specific token. | [optional] if omitted the server will use the default value of "null"
 **use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md)|  | [optional]

### Return type

[**LoggingSyslogResponse**](LoggingSyslogResponse.md)

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

# **delete_log_syslog**
> InlineResponse200 delete_log_syslog(service_id, version_id, logging_syslog_name)

Delete a syslog log endpoint

Delete the Syslog for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_syslog_api
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
    api_instance = logging_syslog_api.LoggingSyslogApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_syslog_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete a syslog log endpoint
        api_response = api_instance.delete_log_syslog(service_id, version_id, logging_syslog_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->delete_log_syslog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_syslog_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_syslog**
> LoggingSyslogResponse get_log_syslog(service_id, version_id, logging_syslog_name)

Get a syslog log endpoint

Get the Syslog for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_syslog_api
from fastly.model.logging_syslog_response import LoggingSyslogResponse
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
    api_instance = logging_syslog_api.LoggingSyslogApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_syslog_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a syslog log endpoint
        api_response = api_instance.get_log_syslog(service_id, version_id, logging_syslog_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->get_log_syslog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_syslog_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingSyslogResponse**](LoggingSyslogResponse.md)

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

# **list_log_syslog**
> [LoggingSyslogResponse] list_log_syslog(service_id, version_id)

List Syslog log endpoints

List all of the Syslogs for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_syslog_api
from fastly.model.logging_syslog_response import LoggingSyslogResponse
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
    api_instance = logging_syslog_api.LoggingSyslogApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Syslog log endpoints
        api_response = api_instance.list_log_syslog(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->list_log_syslog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingSyslogResponse]**](LoggingSyslogResponse.md)

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

# **update_log_syslog**
> LoggingSyslogResponse update_log_syslog(service_id, version_id, logging_syslog_name)

Update a syslog log endpoint

Update the Syslog for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_syslog_api
from fastly.model.logging_use_tls_string import LoggingUseTlsString
from fastly.model.logging_message_type import LoggingMessageType
from fastly.model.logging_syslog_response import LoggingSyslogResponse
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
    api_instance = logging_syslog_api.LoggingSyslogApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_syslog_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_hostname = "null" # str, none_type | The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. (optional) if omitted the server will use the default value of "null"
    address = "example.com" # str | A hostname or IPv4 address. (optional)
    port = 514 # int | The port number. (optional) if omitted the server will use the default value of 514
    message_type = LoggingMessageType("classic") # LoggingMessageType |  (optional)
    hostname = "hostname_example" # str | The hostname used for the syslog endpoint. (optional)
    ipv4 = "ipv4_example" # str, none_type | The IPv4 address used for the syslog endpoint. (optional)
    token = "null" # str, none_type | Whether to prepend each message with a specific token. (optional) if omitted the server will use the default value of "null"
    use_tls = LoggingUseTlsString("0") # LoggingUseTlsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a syslog log endpoint
        api_response = api_instance.update_log_syslog(service_id, version_id, logging_syslog_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->update_log_syslog: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a syslog log endpoint
        api_response = api_instance.update_log_syslog(service_id, version_id, logging_syslog_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, address=address, port=port, message_type=message_type, hostname=hostname, ipv4=ipv4, token=token, use_tls=use_tls)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingSyslogApi->update_log_syslog: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_syslog_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_hostname** | **str, none_type**| The hostname to verify the server&#39;s certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. | [optional] if omitted the server will use the default value of "null"
 **address** | **str**| A hostname or IPv4 address. | [optional]
 **port** | **int**| The port number. | [optional] if omitted the server will use the default value of 514
 **message_type** | [**LoggingMessageType**](LoggingMessageType.md)|  | [optional]
 **hostname** | **str**| The hostname used for the syslog endpoint. | [optional]
 **ipv4** | **str, none_type**| The IPv4 address used for the syslog endpoint. | [optional]
 **token** | **str, none_type**| Whether to prepend each message with a specific token. | [optional] if omitted the server will use the default value of "null"
 **use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md)|  | [optional]

### Return type

[**LoggingSyslogResponse**](LoggingSyslogResponse.md)

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

