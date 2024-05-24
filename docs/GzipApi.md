# fastly.GzipApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_gzip_config**](GzipApi.md#create_gzip_config) | **POST** /service/{service_id}/version/{version_id}/gzip | Create a gzip configuration
[**delete_gzip_config**](GzipApi.md#delete_gzip_config) | **DELETE** /service/{service_id}/version/{version_id}/gzip/{gzip_name} | Delete a gzip configuration
[**get_gzip_configs**](GzipApi.md#get_gzip_configs) | **GET** /service/{service_id}/version/{version_id}/gzip/{gzip_name} | Get a gzip configuration
[**list_gzip_configs**](GzipApi.md#list_gzip_configs) | **GET** /service/{service_id}/version/{version_id}/gzip | List gzip configurations
[**update_gzip_config**](GzipApi.md#update_gzip_config) | **PUT** /service/{service_id}/version/{version_id}/gzip/{gzip_name} | Update a gzip configuration


# **create_gzip_config**
> GzipResponse create_gzip_config(service_id, version_id)

Create a gzip configuration

Create a named gzip configuration on a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import gzip_api
from fastly.model.gzip_response import GzipResponse
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
    api_instance = gzip_api.GzipApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    cache_condition = "cache_condition_example" # str, none_type | Name of the cache condition controlling when this configuration applies. (optional)
    content_types = "content_types_example" # str, none_type | Space-separated list of content types to compress. If you omit this field a default list will be used. (optional)
    extensions = "extensions_example" # str, none_type | Space-separated list of file extensions to compress. If you omit this field a default list will be used. (optional)
    name = "test-gzip" # str | Name of the gzip configuration. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a gzip configuration
        api_response = api_instance.create_gzip_config(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->create_gzip_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a gzip configuration
        api_response = api_instance.create_gzip_config(service_id, version_id, cache_condition=cache_condition, content_types=content_types, extensions=extensions, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->create_gzip_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **cache_condition** | **str, none_type**| Name of the cache condition controlling when this configuration applies. | [optional]
 **content_types** | **str, none_type**| Space-separated list of content types to compress. If you omit this field a default list will be used. | [optional]
 **extensions** | **str, none_type**| Space-separated list of file extensions to compress. If you omit this field a default list will be used. | [optional]
 **name** | **str**| Name of the gzip configuration. | [optional]

### Return type

[**GzipResponse**](GzipResponse.md)

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

# **delete_gzip_config**
> InlineResponse200 delete_gzip_config(service_id, version_id, gzip_name)

Delete a gzip configuration

Delete a named gzip configuration on a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import gzip_api
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
    api_instance = gzip_api.GzipApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    gzip_name = "test-gzip" # str | Name of the gzip configuration.

    # example passing only required values which don't have defaults set
    try:
        # Delete a gzip configuration
        api_response = api_instance.delete_gzip_config(service_id, version_id, gzip_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->delete_gzip_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **gzip_name** | **str**| Name of the gzip configuration. |

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

# **get_gzip_configs**
> GzipResponse get_gzip_configs(service_id, version_id, gzip_name)

Get a gzip configuration

Get the gzip configuration for a particular service, version, and name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import gzip_api
from fastly.model.gzip_response import GzipResponse
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
    api_instance = gzip_api.GzipApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    gzip_name = "test-gzip" # str | Name of the gzip configuration.

    # example passing only required values which don't have defaults set
    try:
        # Get a gzip configuration
        api_response = api_instance.get_gzip_configs(service_id, version_id, gzip_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->get_gzip_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **gzip_name** | **str**| Name of the gzip configuration. |

### Return type

[**GzipResponse**](GzipResponse.md)

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

# **list_gzip_configs**
> [GzipResponse] list_gzip_configs(service_id, version_id)

List gzip configurations

List all gzip configurations for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import gzip_api
from fastly.model.gzip_response import GzipResponse
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
    api_instance = gzip_api.GzipApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List gzip configurations
        api_response = api_instance.list_gzip_configs(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->list_gzip_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[GzipResponse]**](GzipResponse.md)

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

# **update_gzip_config**
> GzipResponse update_gzip_config(service_id, version_id, gzip_name)

Update a gzip configuration

Update a named gzip configuration on a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import gzip_api
from fastly.model.gzip_response import GzipResponse
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
    api_instance = gzip_api.GzipApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    gzip_name = "test-gzip" # str | Name of the gzip configuration.
    cache_condition = "cache_condition_example" # str, none_type | Name of the cache condition controlling when this configuration applies. (optional)
    content_types = "content_types_example" # str, none_type | Space-separated list of content types to compress. If you omit this field a default list will be used. (optional)
    extensions = "extensions_example" # str, none_type | Space-separated list of file extensions to compress. If you omit this field a default list will be used. (optional)
    name = "test-gzip" # str | Name of the gzip configuration. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a gzip configuration
        api_response = api_instance.update_gzip_config(service_id, version_id, gzip_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->update_gzip_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a gzip configuration
        api_response = api_instance.update_gzip_config(service_id, version_id, gzip_name, cache_condition=cache_condition, content_types=content_types, extensions=extensions, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling GzipApi->update_gzip_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **gzip_name** | **str**| Name of the gzip configuration. |
 **cache_condition** | **str, none_type**| Name of the cache condition controlling when this configuration applies. | [optional]
 **content_types** | **str, none_type**| Space-separated list of content types to compress. If you omit this field a default list will be used. | [optional]
 **extensions** | **str, none_type**| Space-separated list of file extensions to compress. If you omit this field a default list will be used. | [optional]
 **name** | **str**| Name of the gzip configuration. | [optional]

### Return type

[**GzipResponse**](GzipResponse.md)

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

