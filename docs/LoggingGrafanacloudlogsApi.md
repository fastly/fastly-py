# fastly.LoggingGrafanacloudlogsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_grafanacloudlogs**](LoggingGrafanacloudlogsApi.md#create_log_grafanacloudlogs) | **POST** /service/{service_id}/version/{version_id}/logging/grafanacloudlogs | Create a Grafana Cloud Logs log endpoint
[**delete_log_grafanacloudlogs**](LoggingGrafanacloudlogsApi.md#delete_log_grafanacloudlogs) | **DELETE** /service/{service_id}/version/{version_id}/logging/grafanacloudlogs/{logging_grafanacloudlogs_name} | Delete the Grafana Cloud Logs log endpoint
[**get_log_grafanacloudlogs**](LoggingGrafanacloudlogsApi.md#get_log_grafanacloudlogs) | **GET** /service/{service_id}/version/{version_id}/logging/grafanacloudlogs/{logging_grafanacloudlogs_name} | Get a Grafana Cloud Logs log endpoint
[**list_log_grafanacloudlogs**](LoggingGrafanacloudlogsApi.md#list_log_grafanacloudlogs) | **GET** /service/{service_id}/version/{version_id}/logging/grafanacloudlogs | List Grafana Cloud Logs log endpoints
[**update_log_grafanacloudlogs**](LoggingGrafanacloudlogsApi.md#update_log_grafanacloudlogs) | **PUT** /service/{service_id}/version/{version_id}/logging/grafanacloudlogs/{logging_grafanacloudlogs_name} | Update a Grafana Cloud Logs log endpoint


# **create_log_grafanacloudlogs**
> LoggingGrafanacloudlogsResponse create_log_grafanacloudlogs(service_id, version_id)

Create a Grafana Cloud Logs log endpoint

Create a Grafana Cloud Logs logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_grafanacloudlogs_api
from fastly.model.logging_grafanacloudlogs_response import LoggingGrafanacloudlogsResponse
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
    api_instance = logging_grafanacloudlogs_api.LoggingGrafanacloudlogsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "format_example" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional)
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    user = "user_example" # str | The Grafana Cloud Logs Dataset you want to log to. (optional)
    url = "url_example" # str | The URL of the Loki instance in your Grafana stack. (optional)
    token = "token_example" # str | The Grafana Access Policy token with `logs:write` access scoped to your Loki instance. (optional)
    index = "index_example" # str | The Stream Labels, a JSON string used to identify the stream. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a Grafana Cloud Logs log endpoint
        api_response = api_instance.create_log_grafanacloudlogs(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->create_log_grafanacloudlogs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Grafana Cloud Logs log endpoint
        api_response = api_instance.create_log_grafanacloudlogs(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, user=user, url=url, token=token, index=index)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->create_log_grafanacloudlogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional]
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **user** | **str**| The Grafana Cloud Logs Dataset you want to log to. | [optional]
 **url** | **str**| The URL of the Loki instance in your Grafana stack. | [optional]
 **token** | **str**| The Grafana Access Policy token with `logs:write` access scoped to your Loki instance. | [optional]
 **index** | **str**| The Stream Labels, a JSON string used to identify the stream. | [optional]

### Return type

[**LoggingGrafanacloudlogsResponse**](LoggingGrafanacloudlogsResponse.md)

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

# **delete_log_grafanacloudlogs**
> InlineResponse200 delete_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name)

Delete the Grafana Cloud Logs log endpoint

Delete the Grafana Cloud Logs logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_grafanacloudlogs_api
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
    api_instance = logging_grafanacloudlogs_api.LoggingGrafanacloudlogsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_grafanacloudlogs_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete the Grafana Cloud Logs log endpoint
        api_response = api_instance.delete_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->delete_log_grafanacloudlogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_grafanacloudlogs_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_grafanacloudlogs**
> LoggingGrafanacloudlogsResponse get_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name)

Get a Grafana Cloud Logs log endpoint

Get the details of a Grafana Cloud Logs logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_grafanacloudlogs_api
from fastly.model.logging_grafanacloudlogs_response import LoggingGrafanacloudlogsResponse
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
    api_instance = logging_grafanacloudlogs_api.LoggingGrafanacloudlogsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_grafanacloudlogs_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a Grafana Cloud Logs log endpoint
        api_response = api_instance.get_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->get_log_grafanacloudlogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_grafanacloudlogs_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingGrafanacloudlogsResponse**](LoggingGrafanacloudlogsResponse.md)

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

# **list_log_grafanacloudlogs**
> [LoggingGrafanacloudlogsResponse] list_log_grafanacloudlogs(service_id, version_id)

List Grafana Cloud Logs log endpoints

List all of the Grafana Cloud Logs logging objects for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_grafanacloudlogs_api
from fastly.model.logging_grafanacloudlogs_response import LoggingGrafanacloudlogsResponse
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
    api_instance = logging_grafanacloudlogs_api.LoggingGrafanacloudlogsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List Grafana Cloud Logs log endpoints
        api_response = api_instance.list_log_grafanacloudlogs(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->list_log_grafanacloudlogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingGrafanacloudlogsResponse]**](LoggingGrafanacloudlogsResponse.md)

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

# **update_log_grafanacloudlogs**
> LoggingGrafanacloudlogsResponse update_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name)

Update a Grafana Cloud Logs log endpoint

Update a Grafana Cloud Logs logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_grafanacloudlogs_api
from fastly.model.logging_grafanacloudlogs_response import LoggingGrafanacloudlogsResponse
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
    api_instance = logging_grafanacloudlogs_api.LoggingGrafanacloudlogsApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_grafanacloudlogs_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "test-log-endpoint" # str | The name for the real-time logging configuration. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "format_example" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). (optional)
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    user = "user_example" # str | The Grafana Cloud Logs Dataset you want to log to. (optional)
    url = "url_example" # str | The URL of the Loki instance in your Grafana stack. (optional)
    token = "token_example" # str | The Grafana Access Policy token with `logs:write` access scoped to your Loki instance. (optional)
    index = "index_example" # str | The Stream Labels, a JSON string used to identify the stream. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Grafana Cloud Logs log endpoint
        api_response = api_instance.update_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->update_log_grafanacloudlogs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Grafana Cloud Logs log endpoint
        api_response = api_instance.update_log_grafanacloudlogs(service_id, version_id, logging_grafanacloudlogs_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, user=user, url=url, token=token, index=index)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingGrafanacloudlogsApi->update_log_grafanacloudlogs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_grafanacloudlogs_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name for the real-time logging configuration. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). | [optional]
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **user** | **str**| The Grafana Cloud Logs Dataset you want to log to. | [optional]
 **url** | **str**| The URL of the Loki instance in your Grafana stack. | [optional]
 **token** | **str**| The Grafana Access Policy token with `logs:write` access scoped to your Loki instance. | [optional]
 **index** | **str**| The Stream Labels, a JSON string used to identify the stream. | [optional]

### Return type

[**LoggingGrafanacloudlogsResponse**](LoggingGrafanacloudlogsResponse.md)

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

