# fastly.LoggingS3Api

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_aws_s3**](LoggingS3Api.md#create_log_aws_s3) | **POST** /service/{service_id}/version/{version_id}/logging/s3 | Create an AWS S3 log endpoint
[**delete_log_aws_s3**](LoggingS3Api.md#delete_log_aws_s3) | **DELETE** /service/{service_id}/version/{version_id}/logging/s3/{logging_s3_name} | Delete an AWS S3 log endpoint
[**get_log_aws_s3**](LoggingS3Api.md#get_log_aws_s3) | **GET** /service/{service_id}/version/{version_id}/logging/s3/{logging_s3_name} | Get an AWS S3 log endpoint
[**list_log_aws_s3**](LoggingS3Api.md#list_log_aws_s3) | **GET** /service/{service_id}/version/{version_id}/logging/s3 | List AWS S3 log endpoints
[**update_log_aws_s3**](LoggingS3Api.md#update_log_aws_s3) | **PUT** /service/{service_id}/version/{version_id}/logging/s3/{logging_s3_name} | Update an AWS S3 log endpoint


# **create_log_aws_s3**
> LoggingS3Response create_log_aws_s3(service_id, version_id)

Create an AWS S3 log endpoint

Create a S3 for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_s3_api
from fastly.model.logging_s3_response import LoggingS3Response
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
    api_instance = logging_s3_api.LoggingS3Api(api_client)
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
    access_key = "access_key_example" # str, none_type | The access key for your S3 account. Not required if `iam_role` is provided. (optional)
    acl = "acl_example" # str | The access control list (ACL) specific request header. See the AWS documentation for [Access Control List (ACL) Specific Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html#initiate-mpu-acl-specific-request-headers) for more information. (optional)
    bucket_name = "bucket_name_example" # str | The bucket name for S3 account. (optional)
    domain = "domain_example" # str | The domain of the Amazon S3 endpoint. (optional)
    iam_role = "iam_role_example" # str, none_type | The Amazon Resource Name (ARN) for the IAM role granting Fastly access to S3. Not required if `access_key` and `secret_key` are provided. (optional)
    path = "null" # str, none_type | The path to upload logs to. (optional) if omitted the server will use the default value of "null"
    public_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str, none_type | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. (optional) if omitted the server will use the default value of "null"
    redundancy = "null" # str, none_type | The S3 redundancy level. (optional) if omitted the server will use the default value of "null"
    secret_key = "secret_key_example" # str, none_type | The secret key for your S3 account. Not required if `iam_role` is provided. (optional)
    server_side_encryption_kms_key_id = "null" # str, none_type | Optional server-side KMS Key Id. Must be set if `server_side_encryption` is set to `aws:kms` or `AES256`. (optional) if omitted the server will use the default value of "null"
    server_side_encryption = "null" # str, none_type | Set this to `AES256` or `aws:kms` to enable S3 Server Side Encryption. (optional) if omitted the server will use the default value of "null"
    file_max_bytes = 1048576 # int | The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an AWS S3 log endpoint
        api_response = api_instance.create_log_aws_s3(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->create_log_aws_s3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an AWS S3 log endpoint
        api_response = api_instance.create_log_aws_s3(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, message_type=message_type, timestamp_format=timestamp_format, compression_codec=compression_codec, period=period, gzip_level=gzip_level, access_key=access_key, acl=acl, bucket_name=bucket_name, domain=domain, iam_role=iam_role, path=path, public_key=public_key, redundancy=redundancy, secret_key=secret_key, server_side_encryption_kms_key_id=server_side_encryption_kms_key_id, server_side_encryption=server_side_encryption, file_max_bytes=file_max_bytes)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->create_log_aws_s3: %s\n" % e)
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
 **access_key** | **str, none_type**| The access key for your S3 account. Not required if `iam_role` is provided. | [optional]
 **acl** | **str**| The access control list (ACL) specific request header. See the AWS documentation for [Access Control List (ACL) Specific Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html#initiate-mpu-acl-specific-request-headers) for more information. | [optional]
 **bucket_name** | **str**| The bucket name for S3 account. | [optional]
 **domain** | **str**| The domain of the Amazon S3 endpoint. | [optional]
 **iam_role** | **str, none_type**| The Amazon Resource Name (ARN) for the IAM role granting Fastly access to S3. Not required if `access_key` and `secret_key` are provided. | [optional]
 **path** | **str, none_type**| The path to upload logs to. | [optional] if omitted the server will use the default value of "null"
 **public_key** | **str, none_type**| A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional] if omitted the server will use the default value of "null"
 **redundancy** | **str, none_type**| The S3 redundancy level. | [optional] if omitted the server will use the default value of "null"
 **secret_key** | **str, none_type**| The secret key for your S3 account. Not required if `iam_role` is provided. | [optional]
 **server_side_encryption_kms_key_id** | **str, none_type**| Optional server-side KMS Key Id. Must be set if `server_side_encryption` is set to `aws:kms` or `AES256`. | [optional] if omitted the server will use the default value of "null"
 **server_side_encryption** | **str, none_type**| Set this to `AES256` or `aws:kms` to enable S3 Server Side Encryption. | [optional] if omitted the server will use the default value of "null"
 **file_max_bytes** | **int**| The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.) | [optional]

### Return type

[**LoggingS3Response**](LoggingS3Response.md)

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

# **delete_log_aws_s3**
> InlineResponse200 delete_log_aws_s3(service_id, version_id, logging_s3_name)

Delete an AWS S3 log endpoint

Delete the S3 for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_s3_api
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
    api_instance = logging_s3_api.LoggingS3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_s3_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete an AWS S3 log endpoint
        api_response = api_instance.delete_log_aws_s3(service_id, version_id, logging_s3_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->delete_log_aws_s3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_s3_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_aws_s3**
> LoggingS3Response get_log_aws_s3(service_id, version_id, logging_s3_name)

Get an AWS S3 log endpoint

Get the S3 for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_s3_api
from fastly.model.logging_s3_response import LoggingS3Response
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
    api_instance = logging_s3_api.LoggingS3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_s3_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get an AWS S3 log endpoint
        api_response = api_instance.get_log_aws_s3(service_id, version_id, logging_s3_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->get_log_aws_s3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_s3_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingS3Response**](LoggingS3Response.md)

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

# **list_log_aws_s3**
> [LoggingS3Response] list_log_aws_s3(service_id, version_id)

List AWS S3 log endpoints

List all of the S3s for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_s3_api
from fastly.model.logging_s3_response import LoggingS3Response
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
    api_instance = logging_s3_api.LoggingS3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List AWS S3 log endpoints
        api_response = api_instance.list_log_aws_s3(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->list_log_aws_s3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingS3Response]**](LoggingS3Response.md)

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

# **update_log_aws_s3**
> LoggingS3Response update_log_aws_s3(service_id, version_id, logging_s3_name)

Update an AWS S3 log endpoint

Update the S3 for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_s3_api
from fastly.model.logging_s3_response import LoggingS3Response
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
    api_instance = logging_s3_api.LoggingS3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_s3_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
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
    access_key = "access_key_example" # str, none_type | The access key for your S3 account. Not required if `iam_role` is provided. (optional)
    acl = "acl_example" # str | The access control list (ACL) specific request header. See the AWS documentation for [Access Control List (ACL) Specific Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html#initiate-mpu-acl-specific-request-headers) for more information. (optional)
    bucket_name = "bucket_name_example" # str | The bucket name for S3 account. (optional)
    domain = "domain_example" # str | The domain of the Amazon S3 endpoint. (optional)
    iam_role = "iam_role_example" # str, none_type | The Amazon Resource Name (ARN) for the IAM role granting Fastly access to S3. Not required if `access_key` and `secret_key` are provided. (optional)
    path = "null" # str, none_type | The path to upload logs to. (optional) if omitted the server will use the default value of "null"
    public_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str, none_type | A PGP public key that Fastly will use to encrypt your log files before writing them to disk. (optional) if omitted the server will use the default value of "null"
    redundancy = "null" # str, none_type | The S3 redundancy level. (optional) if omitted the server will use the default value of "null"
    secret_key = "secret_key_example" # str, none_type | The secret key for your S3 account. Not required if `iam_role` is provided. (optional)
    server_side_encryption_kms_key_id = "null" # str, none_type | Optional server-side KMS Key Id. Must be set if `server_side_encryption` is set to `aws:kms` or `AES256`. (optional) if omitted the server will use the default value of "null"
    server_side_encryption = "null" # str, none_type | Set this to `AES256` or `aws:kms` to enable S3 Server Side Encryption. (optional) if omitted the server will use the default value of "null"
    file_max_bytes = 1048576 # int | The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.) (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an AWS S3 log endpoint
        api_response = api_instance.update_log_aws_s3(service_id, version_id, logging_s3_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->update_log_aws_s3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an AWS S3 log endpoint
        api_response = api_instance.update_log_aws_s3(service_id, version_id, logging_s3_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, message_type=message_type, timestamp_format=timestamp_format, compression_codec=compression_codec, period=period, gzip_level=gzip_level, access_key=access_key, acl=acl, bucket_name=bucket_name, domain=domain, iam_role=iam_role, path=path, public_key=public_key, redundancy=redundancy, secret_key=secret_key, server_side_encryption_kms_key_id=server_side_encryption_kms_key_id, server_side_encryption=server_side_encryption, file_max_bytes=file_max_bytes)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingS3Api->update_log_aws_s3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_s3_name** | **str**| The name for the real-time logging configuration. |
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
 **access_key** | **str, none_type**| The access key for your S3 account. Not required if `iam_role` is provided. | [optional]
 **acl** | **str**| The access control list (ACL) specific request header. See the AWS documentation for [Access Control List (ACL) Specific Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/mpUploadInitiate.html#initiate-mpu-acl-specific-request-headers) for more information. | [optional]
 **bucket_name** | **str**| The bucket name for S3 account. | [optional]
 **domain** | **str**| The domain of the Amazon S3 endpoint. | [optional]
 **iam_role** | **str, none_type**| The Amazon Resource Name (ARN) for the IAM role granting Fastly access to S3. Not required if `access_key` and `secret_key` are provided. | [optional]
 **path** | **str, none_type**| The path to upload logs to. | [optional] if omitted the server will use the default value of "null"
 **public_key** | **str, none_type**| A PGP public key that Fastly will use to encrypt your log files before writing them to disk. | [optional] if omitted the server will use the default value of "null"
 **redundancy** | **str, none_type**| The S3 redundancy level. | [optional] if omitted the server will use the default value of "null"
 **secret_key** | **str, none_type**| The secret key for your S3 account. Not required if `iam_role` is provided. | [optional]
 **server_side_encryption_kms_key_id** | **str, none_type**| Optional server-side KMS Key Id. Must be set if `server_side_encryption` is set to `aws:kms` or `AES256`. | [optional] if omitted the server will use the default value of "null"
 **server_side_encryption** | **str, none_type**| Set this to `AES256` or `aws:kms` to enable S3 Server Side Encryption. | [optional] if omitted the server will use the default value of "null"
 **file_max_bytes** | **int**| The maximum number of bytes for each uploaded file. A value of 0 can be used to indicate there is no limit on the size of uploaded files, otherwise the minimum value is 1048576 bytes (1 MiB.) | [optional]

### Return type

[**LoggingS3Response**](LoggingS3Response.md)

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

