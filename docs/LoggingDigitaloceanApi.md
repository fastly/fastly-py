# fastly.LoggingDigitaloceanApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_digocean**](LoggingDigitaloceanApi.md#create_log_digocean) | **POST** /service/{service_id}/version/{version_id}/logging/digitalocean | Create a DigitalOcean Spaces log endpoint
[**delete_log_digocean**](LoggingDigitaloceanApi.md#delete_log_digocean) | **DELETE** /service/{service_id}/version/{version_id}/logging/digitalocean/{logging_digitalocean_name} | Delete a DigitalOcean Spaces log endpoint
[**get_log_digocean**](LoggingDigitaloceanApi.md#get_log_digocean) | **GET** /service/{service_id}/version/{version_id}/logging/digitalocean/{logging_digitalocean_name} | Get a DigitalOcean Spaces log endpoint
[**list_log_digocean**](LoggingDigitaloceanApi.md#list_log_digocean) | **GET** /service/{service_id}/version/{version_id}/logging/digitalocean | List DigitalOcean Spaces log endpoints
[**update_log_digocean**](LoggingDigitaloceanApi.md#update_log_digocean) | **PUT** /service/{service_id}/version/{version_id}/logging/digitalocean/{logging_digitalocean_name} | Update a DigitalOcean Spaces log endpoint


# **create_log_digocean**
> LoggingDigitaloceanResponse create_log_digocean(service_id, version_id)

Create a DigitalOcean Spaces log endpoint

Create a DigitalOcean Space for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_digitalocean_api
from fastly.model.logging_digitalocean_response import LoggingDigitaloceanResponse
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
    api_instance = logging_digitalocean_api.LoggingDigitaloceanApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    message_type = "classic" # str | How the message should be formatted. (optional) if omitted the server will use the default value of "classic"
    timestamp_format = "%Y-%m-%dT%H:%M:%S.000" # str, none_type | A timestamp format (optional)
    compression_codec = "zstd" # str | The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. (optional)
    period = 3600 # int | How frequently log files are finalized so they can be available for reading (in seconds). (optional) if omitted the server will use the default value of 3600
    gzip_level = 0 # int | The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. (optional) if omitted the server will use the default value of 0
    bucket_name = "bucket_name_example" # str | The name of the DigitalOcean Space. (optional)
    access_key = "access_key_example" # str | Your DigitalOcean Spaces account access key. (optional)
    secret_key = "secret_key_example" # str | Your DigitalOcean Spaces account secret key. (optional)
    domain = "nyc3.digitaloceanspaces.com" # str | The domain of the DigitalOcean Spaces endpoint. (optional) if omitted the server will use the default value of "nyc3.digitaloceanspaces.com"
    path = "null" # str, none_type | The path to upload logs to. (optional) if omitted the server will use the default value of "null"
    public_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str, none_type | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. (optional) if omitted the server will use the default value of "null"

    # example passing only required values which don't have defaults set
    try:
        # Create a DigitalOcean Spaces log endpoint
        api_response = api_instance.create_log_digocean(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->create_log_digocean: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a DigitalOcean Spaces log endpoint
        api_response = api_instance.create_log_digocean(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, message_type=message_type, timestamp_format=timestamp_format, compression_codec=compression_codec, period=period, gzip_level=gzip_level, bucket_name=bucket_name, access_key=access_key, secret_key=secret_key, domain=domain, path=path, public_key=public_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->create_log_digocean: %s\n" % e)
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
 **message_type** | **str**| How the message should be formatted. | [optional] if omitted the server will use the default value of "classic"
 **timestamp_format** | **str, none_type**| A timestamp format | [optional]
 **compression_codec** | **str**| The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional]
 **period** | **int**| How frequently log files are finalized so they can be available for reading (in seconds). | [optional] if omitted the server will use the default value of 3600
 **gzip_level** | **int**| The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional] if omitted the server will use the default value of 0
 **bucket_name** | **str**| The name of the DigitalOcean Space. | [optional]
 **access_key** | **str**| Your DigitalOcean Spaces account access key. | [optional]
 **secret_key** | **str**| Your DigitalOcean Spaces account secret key. | [optional]
 **domain** | **str**| The domain of the DigitalOcean Spaces endpoint. | [optional] if omitted the server will use the default value of "nyc3.digitaloceanspaces.com"
 **path** | **str, none_type**| The path to upload logs to. | [optional] if omitted the server will use the default value of "null"
 **public_key** | **str, none_type**| A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional] if omitted the server will use the default value of "null"

### Return type

[**LoggingDigitaloceanResponse**](LoggingDigitaloceanResponse.md)

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

# **delete_log_digocean**
> InlineResponse200 delete_log_digocean(service_id, version_id, logging_digitalocean_name)

Delete a DigitalOcean Spaces log endpoint

Delete the DigitalOcean Space for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_digitalocean_api
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
    api_instance = logging_digitalocean_api.LoggingDigitaloceanApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_digitalocean_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete a DigitalOcean Spaces log endpoint
        api_response = api_instance.delete_log_digocean(service_id, version_id, logging_digitalocean_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->delete_log_digocean: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_digitalocean_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_digocean**
> LoggingDigitaloceanResponse get_log_digocean(service_id, version_id, logging_digitalocean_name)

Get a DigitalOcean Spaces log endpoint

Get the DigitalOcean Space for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_digitalocean_api
from fastly.model.logging_digitalocean_response import LoggingDigitaloceanResponse
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
    api_instance = logging_digitalocean_api.LoggingDigitaloceanApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_digitalocean_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a DigitalOcean Spaces log endpoint
        api_response = api_instance.get_log_digocean(service_id, version_id, logging_digitalocean_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->get_log_digocean: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_digitalocean_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingDigitaloceanResponse**](LoggingDigitaloceanResponse.md)

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

# **list_log_digocean**
> [LoggingDigitaloceanResponse] list_log_digocean(service_id, version_id)

List DigitalOcean Spaces log endpoints

List all of the DigitalOcean Spaces for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_digitalocean_api
from fastly.model.logging_digitalocean_response import LoggingDigitaloceanResponse
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
    api_instance = logging_digitalocean_api.LoggingDigitaloceanApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List DigitalOcean Spaces log endpoints
        api_response = api_instance.list_log_digocean(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->list_log_digocean: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingDigitaloceanResponse]**](LoggingDigitaloceanResponse.md)

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

# **update_log_digocean**
> LoggingDigitaloceanResponse update_log_digocean(service_id, version_id, logging_digitalocean_name)

Update a DigitalOcean Spaces log endpoint

Update the DigitalOcean Space for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_digitalocean_api
from fastly.model.logging_digitalocean_response import LoggingDigitaloceanResponse
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
    api_instance = logging_digitalocean_api.LoggingDigitaloceanApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_digitalocean_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "%h %l %u %t "%r" %&gt;s %b" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional) if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    message_type = "classic" # str | How the message should be formatted. (optional) if omitted the server will use the default value of "classic"
    timestamp_format = "%Y-%m-%dT%H:%M:%S.000" # str, none_type | A timestamp format (optional)
    compression_codec = "zstd" # str | The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. (optional)
    period = 3600 # int | How frequently log files are finalized so they can be available for reading (in seconds). (optional) if omitted the server will use the default value of 3600
    gzip_level = 0 # int | The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. (optional) if omitted the server will use the default value of 0
    bucket_name = "bucket_name_example" # str | The name of the DigitalOcean Space. (optional)
    access_key = "access_key_example" # str | Your DigitalOcean Spaces account access key. (optional)
    secret_key = "secret_key_example" # str | Your DigitalOcean Spaces account secret key. (optional)
    domain = "nyc3.digitaloceanspaces.com" # str | The domain of the DigitalOcean Spaces endpoint. (optional) if omitted the server will use the default value of "nyc3.digitaloceanspaces.com"
    path = "null" # str, none_type | The path to upload logs to. (optional) if omitted the server will use the default value of "null"
    public_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str, none_type | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. (optional) if omitted the server will use the default value of "null"

    # example passing only required values which don't have defaults set
    try:
        # Update a DigitalOcean Spaces log endpoint
        api_response = api_instance.update_log_digocean(service_id, version_id, logging_digitalocean_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->update_log_digocean: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a DigitalOcean Spaces log endpoint
        api_response = api_instance.update_log_digocean(service_id, version_id, logging_digitalocean_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, message_type=message_type, timestamp_format=timestamp_format, compression_codec=compression_codec, period=period, gzip_level=gzip_level, bucket_name=bucket_name, access_key=access_key, secret_key=secret_key, domain=domain, path=path, public_key=public_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingDigitaloceanApi->update_log_digocean: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_digitalocean_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional] if omitted the server will use the default value of "%h %l %u %t "%r" %&gt;s %b"
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **message_type** | **str**| How the message should be formatted. | [optional] if omitted the server will use the default value of "classic"
 **timestamp_format** | **str, none_type**| A timestamp format | [optional]
 **compression_codec** | **str**| The codec used for compressing your logs. Valid values are `zstd`, `snappy`, and `gzip`. Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional]
 **period** | **int**| How frequently log files are finalized so they can be available for reading (in seconds). | [optional] if omitted the server will use the default value of 3600
 **gzip_level** | **int**| The level of gzip encoding when sending logs (default `0`, no compression). Specifying both `compression_codec` and `gzip_level` in the same API request will result in an error. | [optional] if omitted the server will use the default value of 0
 **bucket_name** | **str**| The name of the DigitalOcean Space. | [optional]
 **access_key** | **str**| Your DigitalOcean Spaces account access key. | [optional]
 **secret_key** | **str**| Your DigitalOcean Spaces account secret key. | [optional]
 **domain** | **str**| The domain of the DigitalOcean Spaces endpoint. | [optional] if omitted the server will use the default value of "nyc3.digitaloceanspaces.com"
 **path** | **str, none_type**| The path to upload logs to. | [optional] if omitted the server will use the default value of "null"
 **public_key** | **str, none_type**| A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional] if omitted the server will use the default value of "null"

### Return type

[**LoggingDigitaloceanResponse**](LoggingDigitaloceanResponse.md)

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

