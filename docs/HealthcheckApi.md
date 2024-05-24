# fastly.HealthcheckApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_healthcheck**](HealthcheckApi.md#create_healthcheck) | **POST** /service/{service_id}/version/{version_id}/healthcheck | Create a health check
[**delete_healthcheck**](HealthcheckApi.md#delete_healthcheck) | **DELETE** /service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name} | Delete a health check
[**get_healthcheck**](HealthcheckApi.md#get_healthcheck) | **GET** /service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name} | Get a health check
[**list_healthchecks**](HealthcheckApi.md#list_healthchecks) | **GET** /service/{service_id}/version/{version_id}/healthcheck | List health checks
[**update_healthcheck**](HealthcheckApi.md#update_healthcheck) | **PUT** /service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name} | Update a health check


# **create_healthcheck**
> HealthcheckResponse create_healthcheck(service_id, version_id)

Create a health check

Create a health check for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import healthcheck_api
from fastly.model.healthcheck_response import HealthcheckResponse
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
    api_instance = healthcheck_api.HealthcheckApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    check_interval = 1 # int | How often to run the health check in milliseconds. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    expected_response = 1 # int | The status code expected from the host. (optional)
    headers = [
        "headers_example",
    ] # [str] | Array of custom headers that will be added to the health check probes. (optional)
    host = "host_example" # str | Which host to check. (optional)
    http_version = "http_version_example" # str | Whether to use version 1.0 or 1.1 HTTP. (optional)
    initial = 1 # int | When loading a config, the initial number of probes to be seen as OK. (optional)
    method = "method_example" # str | Which HTTP method to use. (optional)
    name = "test-healthcheck" # str | The name of the health check. (optional)
    path = "path_example" # str | The path to check. (optional)
    threshold = 1 # int | How many health checks must succeed to be considered healthy. (optional)
    timeout = 1 # int | Timeout in milliseconds. (optional)
    window = 1 # int | The number of most recent health check queries to keep for this health check. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a health check
        api_response = api_instance.create_healthcheck(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->create_healthcheck: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a health check
        api_response = api_instance.create_healthcheck(service_id, version_id, check_interval=check_interval, comment=comment, expected_response=expected_response, headers=headers, host=host, http_version=http_version, initial=initial, method=method, name=name, path=path, threshold=threshold, timeout=timeout, window=window)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->create_healthcheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **check_interval** | **int**| How often to run the health check in milliseconds. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **expected_response** | **int**| The status code expected from the host. | [optional]
 **headers** | **[str]**| Array of custom headers that will be added to the health check probes. | [optional]
 **host** | **str**| Which host to check. | [optional]
 **http_version** | **str**| Whether to use version 1.0 or 1.1 HTTP. | [optional]
 **initial** | **int**| When loading a config, the initial number of probes to be seen as OK. | [optional]
 **method** | **str**| Which HTTP method to use. | [optional]
 **name** | **str**| The name of the health check. | [optional]
 **path** | **str**| The path to check. | [optional]
 **threshold** | **int**| How many health checks must succeed to be considered healthy. | [optional]
 **timeout** | **int**| Timeout in milliseconds. | [optional]
 **window** | **int**| The number of most recent health check queries to keep for this health check. | [optional]

### Return type

[**HealthcheckResponse**](HealthcheckResponse.md)

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

# **delete_healthcheck**
> InlineResponse200 delete_healthcheck(service_id, version_id, healthcheck_name)

Delete a health check

Delete the health check for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import healthcheck_api
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
    api_instance = healthcheck_api.HealthcheckApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    healthcheck_name = "test-healthcheck" # str | The name of the health check.

    # example passing only required values which don't have defaults set
    try:
        # Delete a health check
        api_response = api_instance.delete_healthcheck(service_id, version_id, healthcheck_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->delete_healthcheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **healthcheck_name** | **str**| The name of the health check. |

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

# **get_healthcheck**
> HealthcheckResponse get_healthcheck(service_id, version_id, healthcheck_name)

Get a health check

Get the health check for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import healthcheck_api
from fastly.model.healthcheck_response import HealthcheckResponse
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
    api_instance = healthcheck_api.HealthcheckApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    healthcheck_name = "test-healthcheck" # str | The name of the health check.

    # example passing only required values which don't have defaults set
    try:
        # Get a health check
        api_response = api_instance.get_healthcheck(service_id, version_id, healthcheck_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->get_healthcheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **healthcheck_name** | **str**| The name of the health check. |

### Return type

[**HealthcheckResponse**](HealthcheckResponse.md)

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

# **list_healthchecks**
> [HealthcheckResponse] list_healthchecks(service_id, version_id)

List health checks

List all of the health checks for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import healthcheck_api
from fastly.model.healthcheck_response import HealthcheckResponse
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
    api_instance = healthcheck_api.HealthcheckApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List health checks
        api_response = api_instance.list_healthchecks(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->list_healthchecks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[HealthcheckResponse]**](HealthcheckResponse.md)

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

# **update_healthcheck**
> HealthcheckResponse update_healthcheck(service_id, version_id, healthcheck_name)

Update a health check

Update the health check for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import healthcheck_api
from fastly.model.healthcheck_response import HealthcheckResponse
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
    api_instance = healthcheck_api.HealthcheckApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    healthcheck_name = "test-healthcheck" # str | The name of the health check.
    check_interval = 1 # int | How often to run the health check in milliseconds. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    expected_response = 1 # int | The status code expected from the host. (optional)
    headers = [
        "headers_example",
    ] # [str] | Array of custom headers that will be added to the health check probes. (optional)
    host = "host_example" # str | Which host to check. (optional)
    http_version = "http_version_example" # str | Whether to use version 1.0 or 1.1 HTTP. (optional)
    initial = 1 # int | When loading a config, the initial number of probes to be seen as OK. (optional)
    method = "method_example" # str | Which HTTP method to use. (optional)
    name = "test-healthcheck" # str | The name of the health check. (optional)
    path = "path_example" # str | The path to check. (optional)
    threshold = 1 # int | How many health checks must succeed to be considered healthy. (optional)
    timeout = 1 # int | Timeout in milliseconds. (optional)
    window = 1 # int | The number of most recent health check queries to keep for this health check. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a health check
        api_response = api_instance.update_healthcheck(service_id, version_id, healthcheck_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->update_healthcheck: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a health check
        api_response = api_instance.update_healthcheck(service_id, version_id, healthcheck_name, check_interval=check_interval, comment=comment, expected_response=expected_response, headers=headers, host=host, http_version=http_version, initial=initial, method=method, name=name, path=path, threshold=threshold, timeout=timeout, window=window)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HealthcheckApi->update_healthcheck: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **healthcheck_name** | **str**| The name of the health check. |
 **check_interval** | **int**| How often to run the health check in milliseconds. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **expected_response** | **int**| The status code expected from the host. | [optional]
 **headers** | **[str]**| Array of custom headers that will be added to the health check probes. | [optional]
 **host** | **str**| Which host to check. | [optional]
 **http_version** | **str**| Whether to use version 1.0 or 1.1 HTTP. | [optional]
 **initial** | **int**| When loading a config, the initial number of probes to be seen as OK. | [optional]
 **method** | **str**| Which HTTP method to use. | [optional]
 **name** | **str**| The name of the health check. | [optional]
 **path** | **str**| The path to check. | [optional]
 **threshold** | **int**| How many health checks must succeed to be considered healthy. | [optional]
 **timeout** | **int**| Timeout in milliseconds. | [optional]
 **window** | **int**| The number of most recent health check queries to keep for this health check. | [optional]

### Return type

[**HealthcheckResponse**](HealthcheckResponse.md)

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

