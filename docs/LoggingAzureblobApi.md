# fastly.LoggingAzureblobApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_azure**](LoggingAzureblobApi.md#create_log_azure) | **POST** /service/{service_id}/version/{version_id}/logging/azureblob | Create an Azure Blob Storage log endpoint
[**delete_log_azure**](LoggingAzureblobApi.md#delete_log_azure) | **DELETE** /service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name} | Delete the Azure Blob Storage log endpoint
[**get_log_azure**](LoggingAzureblobApi.md#get_log_azure) | **GET** /service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name} | Get an Azure Blob Storage log endpoint
[**list_log_azure**](LoggingAzureblobApi.md#list_log_azure) | **GET** /service/{service_id}/version/{version_id}/logging/azureblob | List Azure Blob Storage log endpoints
[**update_log_azure**](LoggingAzureblobApi.md#update_log_azure) | **PUT** /service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name} | Update an Azure Blob Storage log endpoint


# **create_log_azure**
> LoggingAzureblobResponse create_log_azure(service_id, version_id)

Create an Azure Blob Storage log endpoint

Create an Azure Blob Storage logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_azureblob_api
from fastly.model.logging_azureblob_response import LoggingAzureblobResponse
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
    api_instance = logging_azureblob_api.LoggingAzureblobApi(api_client)
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
    path = "null" # str, none_type | The path to upload logs to. (optional) if omitted the server will use the default value of "null"
    account_name = "account_name_example" # str | The unique Azure Blob Storage namespace in which your data objects are stored. Required. (optional)
    container = "container_example" # str | The name of the Azure Blob Storage container in which to store logs. Required. (optional)
    sas_token = "sas_token_example" # str | The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required. (optional)
    public_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str, none_type | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. (optional) if omitted the server will use the default value of "null"
    file_max_bytes = 1048576 # int | The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB). Note that Microsoft Azure Storage has [block size limits](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block?tabs=microsoft-entra-id#remarks). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an Azure Blob Storage log endpoint
        api_response = api_instance.create_log_azure(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->create_log_azure: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an Azure Blob Storage log endpoint
        api_response = api_instance.create_log_azure(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, message_type=message_type, timestamp_format=timestamp_format, compression_codec=compression_codec, period=period, gzip_level=gzip_level, path=path, account_name=account_name, container=container, sas_token=sas_token, public_key=public_key, file_max_bytes=file_max_bytes)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->create_log_azure: %s\n" % e)
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
 **path** | **str, none_type**| The path to upload logs to. | [optional] if omitted the server will use the default value of "null"
 **account_name** | **str**| The unique Azure Blob Storage namespace in which your data objects are stored. Required. | [optional]
 **container** | **str**| The name of the Azure Blob Storage container in which to store logs. Required. | [optional]
 **sas_token** | **str**| The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required. | [optional]
 **public_key** | **str, none_type**| A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional] if omitted the server will use the default value of "null"
 **file_max_bytes** | **int**| The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB). Note that Microsoft Azure Storage has [block size limits](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block?tabs&#x3D;microsoft-entra-id#remarks). | [optional]

### Return type

[**LoggingAzureblobResponse**](LoggingAzureblobResponse.md)

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

# **delete_log_azure**
> InlineResponse200 delete_log_azure(service_id, version_id, logging_azureblob_name)

Delete the Azure Blob Storage log endpoint

Delete the Azure Blob Storage logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_azureblob_api
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
    api_instance = logging_azureblob_api.LoggingAzureblobApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_azureblob_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete the Azure Blob Storage log endpoint
        api_response = api_instance.delete_log_azure(service_id, version_id, logging_azureblob_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->delete_log_azure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_azureblob_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_azure**
> LoggingAzureblobResponse get_log_azure(service_id, version_id, logging_azureblob_name)

Get an Azure Blob Storage log endpoint

Get the Azure Blob Storage logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_azureblob_api
from fastly.model.logging_azureblob_response import LoggingAzureblobResponse
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
    api_instance = logging_azureblob_api.LoggingAzureblobApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_azureblob_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get an Azure Blob Storage log endpoint
        api_response = api_instance.get_log_azure(service_id, version_id, logging_azureblob_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->get_log_azure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_azureblob_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingAzureblobResponse**](LoggingAzureblobResponse.md)

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

# **list_log_azure**
> [LoggingAzureblobResponse] list_log_azure(service_id, version_id)

List Azure Blob Storage log endpoints

List all of the Azure Blob Storage logging endpoints for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_azureblob_api
from fastly.model.logging_azureblob_response import LoggingAzureblobResponse
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
    api_instance = logging_azureblob_api.LoggingAzureblobApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Azure Blob Storage log endpoints
        api_response = api_instance.list_log_azure(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->list_log_azure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingAzureblobResponse]**](LoggingAzureblobResponse.md)

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

# **update_log_azure**
> LoggingAzureblobResponse update_log_azure(service_id, version_id, logging_azureblob_name)

Update an Azure Blob Storage log endpoint

Update the Azure Blob Storage logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_azureblob_api
from fastly.model.logging_azureblob_response import LoggingAzureblobResponse
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
    api_instance = logging_azureblob_api.LoggingAzureblobApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_azureblob_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
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
    path = "null" # str, none_type | The path to upload logs to. (optional) if omitted the server will use the default value of "null"
    account_name = "account_name_example" # str | The unique Azure Blob Storage namespace in which your data objects are stored. Required. (optional)
    container = "container_example" # str | The name of the Azure Blob Storage container in which to store logs. Required. (optional)
    sas_token = "sas_token_example" # str | The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required. (optional)
    public_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str, none_type | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. (optional) if omitted the server will use the default value of "null"
    file_max_bytes = 1048576 # int | The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB). Note that Microsoft Azure Storage has [block size limits](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block?tabs=microsoft-entra-id#remarks). (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Azure Blob Storage log endpoint
        api_response = api_instance.update_log_azure(service_id, version_id, logging_azureblob_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->update_log_azure: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Azure Blob Storage log endpoint
        api_response = api_instance.update_log_azure(service_id, version_id, logging_azureblob_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, message_type=message_type, timestamp_format=timestamp_format, compression_codec=compression_codec, period=period, gzip_level=gzip_level, path=path, account_name=account_name, container=container, sas_token=sas_token, public_key=public_key, file_max_bytes=file_max_bytes)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingAzureblobApi->update_log_azure: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_azureblob_name** | **str**| The name for the real-time logging configuration. |
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
 **path** | **str, none_type**| The path to upload logs to. | [optional] if omitted the server will use the default value of "null"
 **account_name** | **str**| The unique Azure Blob Storage namespace in which your data objects are stored. Required. | [optional]
 **container** | **str**| The name of the Azure Blob Storage container in which to store logs. Required. | [optional]
 **sas_token** | **str**| The Azure shared access signature providing write access to the blob service objects. Be sure to update your token before it expires or the logging functionality will not work. Required. | [optional]
 **public_key** | **str, none_type**| A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional] if omitted the server will use the default value of "null"
 **file_max_bytes** | **int**| The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB). Note that Microsoft Azure Storage has [block size limits](https://learn.microsoft.com/en-us/rest/api/storageservices/put-block?tabs&#x3D;microsoft-entra-id#remarks). | [optional]

### Return type

[**LoggingAzureblobResponse**](LoggingAzureblobResponse.md)

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

