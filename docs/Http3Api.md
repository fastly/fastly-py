# fastly.Http3Api

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_http3**](Http3Api.md#create_http3) | **POST** /service/{service_id}/version/{version_id}/http3 | Enable support for HTTP/3
[**delete_http3**](Http3Api.md#delete_http3) | **DELETE** /service/{service_id}/version/{version_id}/http3 | Disable support for HTTP/3
[**get_http3**](Http3Api.md#get_http3) | **GET** /service/{service_id}/version/{version_id}/http3 | Get HTTP/3 status


# **create_http3**
> Http3 create_http3(service_id, version_id)

Enable support for HTTP/3

Enable HTTP/3 (QUIC) support for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import http3_api
from fastly.model.http3 import Http3
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
    api_instance = http3_api.Http3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    service_id2 = "service_id_example" # str |  (optional)
    version = 1 # int |  (optional)
    created_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    deleted_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    updated_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    feature_revision = 1 # int | Revision number of the HTTP/3 feature implementation. Defaults to the most recent revision. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Enable support for HTTP/3
        api_response = api_instance.create_http3(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling Http3Api->create_http3: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Enable support for HTTP/3
        api_response = api_instance.create_http3(service_id, version_id, service_id2=service_id2, version=version, created_at=created_at, deleted_at=deleted_at, updated_at=updated_at, feature_revision=feature_revision)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling Http3Api->create_http3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **service_id2** | **str**|  | [optional]
 **version** | **int**|  | [optional]
 **created_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **deleted_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **updated_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **feature_revision** | **int**| Revision number of the HTTP/3 feature implementation. Defaults to the most recent revision. | [optional]

### Return type

[**Http3**](Http3.md)

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

# **delete_http3**
> InlineResponse200 delete_http3(service_id, version_id)

Disable support for HTTP/3

Disable HTTP/3 (QUIC) support for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import http3_api
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
    api_instance = http3_api.Http3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Disable support for HTTP/3
        api_response = api_instance.delete_http3(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling Http3Api->delete_http3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

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

# **get_http3**
> Http3 get_http3(service_id, version_id)

Get HTTP/3 status

Get the status of HTTP/3 (QUIC) support for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import http3_api
from fastly.model.http3 import Http3
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
    api_instance = http3_api.Http3Api(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Get HTTP/3 status
        api_response = api_instance.get_http3(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling Http3Api->get_http3: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**Http3**](Http3.md)

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

