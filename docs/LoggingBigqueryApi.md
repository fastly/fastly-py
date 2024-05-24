# fastly.LoggingBigqueryApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_log_bigquery**](LoggingBigqueryApi.md#create_log_bigquery) | **POST** /service/{service_id}/version/{version_id}/logging/bigquery | Create a BigQuery log endpoint
[**delete_log_bigquery**](LoggingBigqueryApi.md#delete_log_bigquery) | **DELETE** /service/{service_id}/version/{version_id}/logging/bigquery/{logging_bigquery_name} | Delete a BigQuery log endpoint
[**get_log_bigquery**](LoggingBigqueryApi.md#get_log_bigquery) | **GET** /service/{service_id}/version/{version_id}/logging/bigquery/{logging_bigquery_name} | Get a BigQuery log endpoint
[**list_log_bigquery**](LoggingBigqueryApi.md#list_log_bigquery) | **GET** /service/{service_id}/version/{version_id}/logging/bigquery | List BigQuery log endpoints
[**update_log_bigquery**](LoggingBigqueryApi.md#update_log_bigquery) | **PUT** /service/{service_id}/version/{version_id}/logging/bigquery/{logging_bigquery_name} | Update a BigQuery log endpoint


# **create_log_bigquery**
> LoggingBigqueryResponse create_log_bigquery(service_id, version_id)

Create a BigQuery log endpoint

Create a BigQuery logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_bigquery_api
from fastly.model.logging_bigquery_response import LoggingBigqueryResponse
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
    api_instance = logging_bigquery_api.LoggingBigqueryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    name = "name_example" # str | The name of the BigQuery logging object. Used as a primary key for API access. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "format_example" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce JSON that matches the schema of your BigQuery table. (optional)
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    user = "test-user@test-project-id.iam.gserviceaccount.com" # str | Your Google Cloud Platform service account email address. The `client_email` field in your service account authentication JSON. Not required if `account_name` is specified. (optional)
    secret_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str | Your Google Cloud Platform account secret key. The `private_key` field in your service account authentication JSON. Not required if `account_name` is specified. (optional)
    account_name = "test-user@test-project-id.iam.gserviceaccount.com" # str | The name of the Google Cloud Platform service account associated with the target log collection service. Not required if `user` and `secret_key` are provided. (optional)
    dataset = "dataset_example" # str | Your BigQuery dataset. (optional)
    table = "table_example" # str | Your BigQuery table. (optional)
    template_suffix = "template_suffix_example" # str, none_type | BigQuery table name suffix template. Optional. (optional)
    project_id = "test-project-id" # str | Your Google Cloud Platform project ID. Required (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a BigQuery log endpoint
        api_response = api_instance.create_log_bigquery(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->create_log_bigquery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a BigQuery log endpoint
        api_response = api_instance.create_log_bigquery(service_id, version_id, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, user=user, secret_key=secret_key, account_name=account_name, dataset=dataset, table=table, template_suffix=template_suffix, project_id=project_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->create_log_bigquery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **name** | **str**| The name of the BigQuery logging object. Used as a primary key for API access. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce JSON that matches the schema of your BigQuery table. | [optional]
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **user** | **str**| Your Google Cloud Platform service account email address. The `client_email` field in your service account authentication JSON. Not required if `account_name` is specified. | [optional]
 **secret_key** | **str**| Your Google Cloud Platform account secret key. The `private_key` field in your service account authentication JSON. Not required if `account_name` is specified. | [optional]
 **account_name** | **str**| The name of the Google Cloud Platform service account associated with the target log collection service. Not required if `user` and `secret_key` are provided. | [optional]
 **dataset** | **str**| Your BigQuery dataset. | [optional]
 **table** | **str**| Your BigQuery table. | [optional]
 **template_suffix** | **str, none_type**| BigQuery table name suffix template. Optional. | [optional]
 **project_id** | **str**| Your Google Cloud Platform project ID. Required | [optional]

### Return type

[**LoggingBigqueryResponse**](LoggingBigqueryResponse.md)

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

# **delete_log_bigquery**
> InlineResponse200 delete_log_bigquery(service_id, version_id, logging_bigquery_name)

Delete a BigQuery log endpoint

Delete a BigQuery logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_bigquery_api
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
    api_instance = logging_bigquery_api.LoggingBigqueryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_bigquery_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete a BigQuery log endpoint
        api_response = api_instance.delete_log_bigquery(service_id, version_id, logging_bigquery_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->delete_log_bigquery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_bigquery_name** | **str**| The name for the real-time logging configuration. |

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

# **get_log_bigquery**
> LoggingBigqueryResponse get_log_bigquery(service_id, version_id, logging_bigquery_name)

Get a BigQuery log endpoint

Get the details for a BigQuery logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_bigquery_api
from fastly.model.logging_bigquery_response import LoggingBigqueryResponse
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
    api_instance = logging_bigquery_api.LoggingBigqueryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_bigquery_name = "test-log-endpoint" # str | The name for the real-time logging configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a BigQuery log endpoint
        api_response = api_instance.get_log_bigquery(service_id, version_id, logging_bigquery_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->get_log_bigquery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_bigquery_name** | **str**| The name for the real-time logging configuration. |

### Return type

[**LoggingBigqueryResponse**](LoggingBigqueryResponse.md)

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

# **list_log_bigquery**
> [LoggingBigqueryResponse] list_log_bigquery(service_id, version_id)

List BigQuery log endpoints

List all of the BigQuery logging objects for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_bigquery_api
from fastly.model.logging_bigquery_response import LoggingBigqueryResponse
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
    api_instance = logging_bigquery_api.LoggingBigqueryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List BigQuery log endpoints
        api_response = api_instance.list_log_bigquery(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->list_log_bigquery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[LoggingBigqueryResponse]**](LoggingBigqueryResponse.md)

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

# **update_log_bigquery**
> LoggingBigqueryResponse update_log_bigquery(service_id, version_id, logging_bigquery_name)

Update a BigQuery log endpoint

Update a BigQuery logging object for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import logging_bigquery_api
from fastly.model.logging_bigquery_response import LoggingBigqueryResponse
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
    api_instance = logging_bigquery_api.LoggingBigqueryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    logging_bigquery_name = "test-log-endpoint" # str | The name for the real-time logging configuration.
    name = "name_example" # str | The name of the BigQuery logging object. Used as a primary key for API access. (optional)
    placement = "none" # str, none_type | Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  (optional)
    response_condition = "response_condition_example" # str, none_type | The name of an existing condition in the configured endpoint, or leave blank to always execute. (optional)
    format = "format_example" # str | A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce JSON that matches the schema of your BigQuery table. (optional)
    format_version = 2 # int | The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  (optional) if omitted the server will use the default value of 2
    user = "test-user@test-project-id.iam.gserviceaccount.com" # str | Your Google Cloud Platform service account email address. The `client_email` field in your service account authentication JSON. Not required if `account_name` is specified. (optional)
    secret_key = '''-----BEGIN PRIVATE KEY-----
...
-----END PRIVATE KEY-----
''' # str | Your Google Cloud Platform account secret key. The `private_key` field in your service account authentication JSON. Not required if `account_name` is specified. (optional)
    account_name = "test-user@test-project-id.iam.gserviceaccount.com" # str | The name of the Google Cloud Platform service account associated with the target log collection service. Not required if `user` and `secret_key` are provided. (optional)
    dataset = "dataset_example" # str | Your BigQuery dataset. (optional)
    table = "table_example" # str | Your BigQuery table. (optional)
    template_suffix = "template_suffix_example" # str, none_type | BigQuery table name suffix template. Optional. (optional)
    project_id = "test-project-id" # str | Your Google Cloud Platform project ID. Required (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a BigQuery log endpoint
        api_response = api_instance.update_log_bigquery(service_id, version_id, logging_bigquery_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->update_log_bigquery: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a BigQuery log endpoint
        api_response = api_instance.update_log_bigquery(service_id, version_id, logging_bigquery_name, name=name, placement=placement, response_condition=response_condition, format=format, format_version=format_version, user=user, secret_key=secret_key, account_name=account_name, dataset=dataset, table=table, template_suffix=template_suffix, project_id=project_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LoggingBigqueryApi->update_log_bigquery: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **logging_bigquery_name** | **str**| The name for the real-time logging configuration. |
 **name** | **str**| The name of the BigQuery logging object. Used as a primary key for API access. | [optional]
 **placement** | **str, none_type**| Where in the generated VCL the logging call should be placed. If not set, endpoints with `format_version` of 2 are placed in `vcl_log` and those with `format_version` of 1 are placed in `vcl_deliver`.  | [optional]
 **response_condition** | **str, none_type**| The name of an existing condition in the configured endpoint, or leave blank to always execute. | [optional]
 **format** | **str**| A Fastly [log format string](https://docs.fastly.com/en/guides/custom-log-formats). Must produce JSON that matches the schema of your BigQuery table. | [optional]
 **format_version** | **int**| The version of the custom logging format used for the configured endpoint. The logging call gets placed by default in `vcl_log` if `format_version` is set to `2` and in `vcl_deliver` if `format_version` is set to `1`.  | [optional] if omitted the server will use the default value of 2
 **user** | **str**| Your Google Cloud Platform service account email address. The `client_email` field in your service account authentication JSON. Not required if `account_name` is specified. | [optional]
 **secret_key** | **str**| Your Google Cloud Platform account secret key. The `private_key` field in your service account authentication JSON. Not required if `account_name` is specified. | [optional]
 **account_name** | **str**| The name of the Google Cloud Platform service account associated with the target log collection service. Not required if `user` and `secret_key` are provided. | [optional]
 **dataset** | **str**| Your BigQuery dataset. | [optional]
 **table** | **str**| Your BigQuery table. | [optional]
 **template_suffix** | **str, none_type**| BigQuery table name suffix template. Optional. | [optional]
 **project_id** | **str**| Your Google Cloud Platform project ID. Required | [optional]

### Return type

[**LoggingBigqueryResponse**](LoggingBigqueryResponse.md)

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

