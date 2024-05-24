# fastly.LoggingElasticsearchApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_elasticsearch**](LoggingElasticsearchApi.md#create_log_elasticsearch) | **POST** /service/{service_id}/version/{version_id}/logging/elasticsearch | Create an Elasticsearch log endpoint
[**delete_log_elasticsearch**](LoggingElasticsearchApi.md#delete_log_elasticsearch) | **DELETE** /service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name} | Delete an Elasticsearch log endpoint
[**get_log_elasticsearch**](LoggingElasticsearchApi.md#get_log_elasticsearch) | **GET** /service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name} | Get an Elasticsearch log endpoint
[**list_log_elasticsearch**](LoggingElasticsearchApi.md#list_log_elasticsearch) | **GET** /service/{service_id}/version/{version_id}/logging/elasticsearch | List Elasticsearch log endpoints
[**update_log_elasticsearch**](LoggingElasticsearchApi.md#update_log_elasticsearch) | **PUT** /service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name} | Update an Elasticsearch log endpoint


# **create_log_elasticsearch**
> LoggingElasticsearchResponse create_log_elasticsearch(service_id, version_id)

Create an Elasticsearch log endpoint

Create a Elasticsearch logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_elasticsearch_api
from fastly.model.logging_elasticsearch_response import LoggingElasticsearchResponse
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
    api_instance = logging_elasticsearch_api.LoggingElasticsearchApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "format_example" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Elasticsearch can ingest. (optional)
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_hostname = "null" # str, none_type | The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. (optional) if omitted the server will use the default value of "null"
    request_max_entries = 0 # int | The maximum number of logs sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    request_max_bytes = 0 # int | The maximum number of bytes sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    index = "index_example" # str | The name of the Elasticsearch index to send documents (logs) to. The index must follow the Elasticsearch [index format rules](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html). We support [strftime](https://www.man7.org/linux/man-pages/man3/strftime.3.html) interpolated variables inside braces prefixed with a pound symbol. For example, `#{%F}` will interpolate as `YYYY-MM-DD` with today's date. (optional)
    url = "url_example" # str | The URL to stream logs to. Must use HTTPS. (optional)
    pipeline = "pipeline_example" # str, none_type | The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing. Learn more about creating a pipeline in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html). (optional)
    user = "user_example" # str, none_type | Basic Auth username. (optional)
    password = "password_example" # str, none_type | Basic Auth password. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an Elasticsearch log endpoint
        api_response = api_instance.create_log_elasticsearch(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->create_log_elasticsearch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an Elasticsearch log endpoint
        api_response = api_instance.create_log_elasticsearch(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, request_max_entries=request_max_entries, request_max_bytes=request_max_bytes, index=index, url=url, pipeline=pipeline, user=user, password=password)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->create_log_elasticsearch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Elasticsearch can ingest. | [optional]
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_hostname** | **str, none_type**| The hostname to verify the server&#39;s certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. | [optional] if omitted the server will use the default value of "null"
 **request_max_entries** | **int**| The maximum number of logs sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **request_max_bytes** | **int**| The maximum number of bytes sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **index** | **str**| The name of the Elasticsearch index to send documents (logs) to. The index must follow the Elasticsearch [index format rules](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html). We support [strftime](https://www.man7.org/linux/man-pages/man3/strftime.3.html) interpolated variables inside braces prefixed with a pound symbol. For example, `#{%F}` will interpolate as `YYYY-MM-DD` with today&#39;s date. | [optional]
 **url** | **str**| The URL to stream logs to. Must use HTTPS. | [optional]
 **pipeline** | **str, none_type**| The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing. Learn more about creating a pipeline in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html). | [optional]
 **user** | **str, none_type**| Basic Auth username. | [optional]
 **password** | **str, none_type**| Basic Auth password. | [optional]

### Return type

[**LoggingElasticsearchResponse**](LoggingElasticsearchResponse.md)

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

# **delete_log_elasticsearch**
> InlineResponse200 delete_log_elasticsearch(service_id, version_id, logging_elasticsearch_name)

Delete an Elasticsearch log endpoint

Delete the Elasticsearch logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_elasticsearch_api
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
    api_instance = logging_elasticsearch_api.LoggingElasticsearchApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_elasticsearch_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete an Elasticsearch log endpoint
        api_response = api_instance.delete_log_elasticsearch(service_id, version_id, logging_elasticsearch_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->delete_log_elasticsearch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_elasticsearch_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_elasticsearch**
> LoggingElasticsearchResponse get_log_elasticsearch(service_id, version_id, logging_elasticsearch_name)

Get an Elasticsearch log endpoint

Get the Elasticsearch logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_elasticsearch_api
from fastly.model.logging_elasticsearch_response import LoggingElasticsearchResponse
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
    api_instance = logging_elasticsearch_api.LoggingElasticsearchApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_elasticsearch_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get an Elasticsearch log endpoint
        api_response = api_instance.get_log_elasticsearch(service_id, version_id, logging_elasticsearch_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->get_log_elasticsearch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_elasticsearch_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingElasticsearchResponse**](LoggingElasticsearchResponse.md)

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

# **list_log_elasticsearch**
> [LoggingElasticsearchResponse] list_log_elasticsearch(service_id, version_id)

List Elasticsearch log endpoints

List all of the Elasticsearch logging endpoints for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_elasticsearch_api
from fastly.model.logging_elasticsearch_response import LoggingElasticsearchResponse
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
    api_instance = logging_elasticsearch_api.LoggingElasticsearchApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Elasticsearch log endpoints
        api_response = api_instance.list_log_elasticsearch(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->list_log_elasticsearch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingElasticsearchResponse]**](LoggingElasticsearchResponse.md)

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

# **update_log_elasticsearch**
> LoggingElasticsearchResponse update_log_elasticsearch(service_id, version_id, logging_elasticsearch_name)

Update an Elasticsearch log endpoint

Update the Elasticsearch logging endpoint for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_elasticsearch_api
from fastly.model.logging_elasticsearch_response import LoggingElasticsearchResponse
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
    api_instance = logging_elasticsearch_api.LoggingElasticsearchApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_elasticsearch_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "format_example" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Elasticsearch can ingest. (optional)
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_hostname = "null" # str, none_type | The hostname to verify the server's certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. (optional) if omitted the server will use the default value of "null"
    request_max_entries = 0 # int | The maximum number of logs sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    request_max_bytes = 0 # int | The maximum number of bytes sent in one request. Defaults `0` for unbounded. (optional) if omitted the server will use the default value of 0
    index = "index_example" # str | The name of the Elasticsearch index to send documents (logs) to. The index must follow the Elasticsearch [index format rules](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html). We support [strftime](https://www.man7.org/linux/man-pages/man3/strftime.3.html) interpolated variables inside braces prefixed with a pound symbol. For example, `#{%F}` will interpolate as `YYYY-MM-DD` with today's date. (optional)
    url = "url_example" # str | The URL to stream logs to. Must use HTTPS. (optional)
    pipeline = "pipeline_example" # str, none_type | The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing. Learn more about creating a pipeline in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html). (optional)
    user = "user_example" # str, none_type | Basic Auth username. (optional)
    password = "password_example" # str, none_type | Basic Auth password. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an Elasticsearch log endpoint
        api_response = api_instance.update_log_elasticsearch(service_id, version_id, logging_elasticsearch_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->update_log_elasticsearch: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an Elasticsearch log endpoint
        api_response = api_instance.update_log_elasticsearch(service_id, version_id, logging_elasticsearch_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_hostname=tls_hostname, request_max_entries=request_max_entries, request_max_bytes=request_max_bytes, index=index, url=url, pipeline=pipeline, user=user, password=password)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingElasticsearchApi->update_log_elasticsearch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_elasticsearch_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce valid JSON that Elasticsearch can ingest. | [optional]
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_hostname** | **str, none_type**| The hostname to verify the server&#39;s certificate. This should be one of the Subject Alternative Name (SAN) fields for the certificate. Common Names (CN) are not supported. | [optional] if omitted the server will use the default value of "null"
 **request_max_entries** | **int**| The maximum number of logs sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **request_max_bytes** | **int**| The maximum number of bytes sent in one request. Defaults `0` for unbounded. | [optional] if omitted the server will use the default value of 0
 **index** | **str**| The name of the Elasticsearch index to send documents (logs) to. The index must follow the Elasticsearch [index format rules](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-create-index.html). We support [strftime](https://www.man7.org/linux/man-pages/man3/strftime.3.html) interpolated variables inside braces prefixed with a pound symbol. For example, `#{%F}` will interpolate as `YYYY-MM-DD` with today&#39;s date. | [optional]
 **url** | **str**| The URL to stream logs to. Must use HTTPS. | [optional]
 **pipeline** | **str, none_type**| The ID of the Elasticsearch ingest pipeline to apply pre-process transformations to before indexing. Learn more about creating a pipeline in the [Elasticsearch docs](https://www.elastic.co/guide/en/elasticsearch/reference/current/ingest.html). | [optional]
 **user** | **str, none_type**| Basic Auth username. | [optional]
 **password** | **str, none_type**| Basic Auth password. | [optional]

### Return type

[**LoggingElasticsearchResponse**](LoggingElasticsearchResponse.md)

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

