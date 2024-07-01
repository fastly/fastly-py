# fastly.LoggingKafkaApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_kafka**](LoggingKafkaApi.md#create_log_kafka) | **POST** /service/{service_id}/version/{version_id}/logging/kafka | Create a Kafka log endpoint
[**delete_log_kafka**](LoggingKafkaApi.md#delete_log_kafka) | **DELETE** /service/{service_id}/version/{version_id}/logging/kafka/{logging_kafka_name} | Delete the Kafka log endpoint
[**get_log_kafka**](LoggingKafkaApi.md#get_log_kafka) | **GET** /service/{service_id}/version/{version_id}/logging/kafka/{logging_kafka_name} | Get a Kafka log endpoint
[**list_log_kafka**](LoggingKafkaApi.md#list_log_kafka) | **GET** /service/{service_id}/version/{version_id}/logging/kafka | List Kafka log endpoints
[**update_log_kafka**](LoggingKafkaApi.md#update_log_kafka) | **PUT** /service/{service_id}/version/{version_id}/logging/kafka/{logging_kafka_name} | Update the Kafka log endpoint


# **create_log_kafka**
> LoggingKafkaResponsePost create_log_kafka(service_id, version_id)

Create a Kafka log endpoint

Create a Kafka logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_kafka_api
from fastly.model.logging_kafka_response_post import LoggingKafkaResponsePost
from fastly.model.logging_use_tls_string import LoggingUseTlsString
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
    api_instance = logging_kafka_api.LoggingKafkaApi(api_client)
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
    topic = "topic_example" # str | The Kafka topic to send logs to. Required. (optional)
    brokers = "brokers_example" # str | A comma-separated list of IP addresses or hostnames of Kafka brokers. Required. (optional)
    compression_codec = "gzip" # str, none_type | The codec used for compression of your logs. (optional)
    required_acks = 1 # int | The number of acknowledgements a leader must receive before a write is considered successful. (optional) if omitted the server will use the default value of 1
    request_max_bytes = 0 # int | The maximum number of bytes sent in one request. Defaults `0` (no limit). (optional) if omitted the server will use the default value of 0
    parse_log_keyvals = True # bool | Enables parsing of key=value tuples from the beginning of a logline, turning them into [record headers](https://cwiki.apache.org/confluence/display/KAFKA/KIP-82+-+Add+Record+Headers). (optional)
    auth_method = "plain" # str | SASL authentication method. (optional)
    user = "user_example" # str | SASL user. (optional)
    password = "password_example" # str | SASL password. (optional)
    use_tls = LoggingUseTlsString("0") # LoggingUseTlsString |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Kafka log endpoint
        api_response = api_instance.create_log_kafka(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingKafkaApi->create_log_kafka: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Kafka log endpoint
        api_response = api_instance.create_log_kafka(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, topic=topic, brokers=brokers, compression_codec=compression_codec, required_acks=required_acks, request_max_bytes=request_max_bytes, parse_log_keyvals=parse_log_keyvals, auth_method=auth_method, user=user, password=password, use_tls=use_tls)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingKafkaApi->create_log_kafka: %s\n" % e)
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
 **topic** | **str**| The Kafka topic to send logs to. Required. | [optional]
 **brokers** | **str**| A comma-separated list of IP addresses or hostnames of Kafka brokers. Required. | [optional]
 **compression_codec** | **str, none_type**| The codec used for compression of your logs. | [optional]
 **required_acks** | **int**| The number of acknowledgements a leader must receive before a write is considered successful. | [optional] if omitted the server will use the default value of 1
 **request_max_bytes** | **int**| The maximum number of bytes sent in one request. Defaults `0` (no limit). | [optional] if omitted the server will use the default value of 0
 **parse_log_keyvals** | **bool**| Enables parsing of key&#x3D;value tuples from the beginning of a logline, turning them into [record headers](https://cwiki.apache.org/confluence/display/KAFKA/KIP-82+-+Add+Record+Headers). | [optional]
 **auth_method** | **str**| SASL authentication method. | [optional]
 **user** | **str**| SASL user. | [optional]
 **password** | **str**| SASL password. | [optional]
 **use_tls** | [**LoggingUseTlsString**](LoggingUseTlsString.md)|  | [optional]

### Return type

[**LoggingKafkaResponsePost**](LoggingKafkaResponsePost.md)

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

# **delete_log_kafka**
> InlineResponse200 delete_log_kafka(service_id, version_id, logging_kafka_name)

Delete the Kafka log endpoint

Delete the Kafka logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_kafka_api
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
    api_instance = logging_kafka_api.LoggingKafkaApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_kafka_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete the Kafka log endpoint
        api_response = api_instance.delete_log_kafka(service_id, version_id, logging_kafka_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingKafkaApi->delete_log_kafka: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_kafka_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_kafka**
> LoggingKafkaResponse get_log_kafka(service_id, version_id, logging_kafka_name)

Get a Kafka log endpoint

Get the Kafka logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_kafka_api
from fastly.model.logging_kafka_response import LoggingKafkaResponse
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
    api_instance = logging_kafka_api.LoggingKafkaApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_kafka_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a Kafka log endpoint
        api_response = api_instance.get_log_kafka(service_id, version_id, logging_kafka_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingKafkaApi->get_log_kafka: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_kafka_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingKafkaResponse**](LoggingKafkaResponse.md)

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

# **list_log_kafka**
> [LoggingKafkaResponse] list_log_kafka(service_id, version_id)

List Kafka log endpoints

List all of the Kafka logging endpoints for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_kafka_api
from fastly.model.logging_kafka_response import LoggingKafkaResponse
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
    api_instance = logging_kafka_api.LoggingKafkaApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Kafka log endpoints
        api_response = api_instance.list_log_kafka(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingKafkaApi->list_log_kafka: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingKafkaResponse]**](LoggingKafkaResponse.md)

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

# **update_log_kafka**
> LoggingKafkaResponse update_log_kafka(service_id, version_id, logging_kafka_name)

Update the Kafka log endpoint

Update the Kafka logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_kafka_api
from fastly.model.logging_kafka_response import LoggingKafkaResponse
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
    api_instance = logging_kafka_api.LoggingKafkaApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_kafka_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Update the Kafka log endpoint
        api_response = api_instance.update_log_kafka(service_id, version_id, logging_kafka_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingKafkaApi->update_log_kafka: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_kafka_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingKafkaResponse**](LoggingKafkaResponse.md)

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

