# fastly.DirectorApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_director**](DirectorApi.md#create_director) | **POST** /service/{service_id}/version/{version_id}/director | Create a director
[**delete_director**](DirectorApi.md#delete_director) | **DELETE** /service/{service_id}/version/{version_id}/director/{director_name} | Delete a director
[**get_director**](DirectorApi.md#get_director) | **GET** /service/{service_id}/version/{version_id}/director/{director_name} | Get a director
[**list_directors**](DirectorApi.md#list_directors) | **GET** /service/{service_id}/version/{version_id}/director | List directors
[**update_director**](DirectorApi.md#update_director) | **PUT** /service/{service_id}/version/{version_id}/director/{director_name} | Update a director


# **create_director**
> DirectorResponse create_director(service_id, version_id)

Create a director

Create a director for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import director_api
from fastly.model.backend import Backend
from fastly.model.director_response import DirectorResponse
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
    api_instance = director_api.DirectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    backends = [
        Backend(
            address="address_example",
            auto_loadbalance=True,
            between_bytes_timeout=1,
            client_cert="client_cert_example",
            comment="",
            connect_timeout=1,
            first_byte_timeout=1,
            healthcheck="healthcheck_example",
            hostname="hostname_example",
            ipv4="ipv4_example",
            ipv6="ipv6_example",
            keepalive_time=1,
            max_conn=1,
            max_tls_version="max_tls_version_example",
            min_tls_version="min_tls_version_example",
            name="test-backend",
            override_host="override_host_example",
            port=1,
            request_condition="request_condition_example",
            share_key="C",
            shield="shield_example",
            ssl_ca_cert="ssl_ca_cert_example",
            ssl_cert_hostname="ssl_cert_hostname_example",
            ssl_check_cert=True,
            ssl_ciphers="ssl_ciphers_example",
            ssl_client_cert="ssl_client_cert_example",
            ssl_client_key="ssl_client_key_example",
            ssl_hostname="ssl_hostname_example",
            ssl_sni_hostname="ssl_sni_hostname_example",
            tcp_keepalive_enable=True,
            tcp_keepalive_interval=1,
            tcp_keepalive_probes=1,
            tcp_keepalive_time=1,
            use_ssl=True,
            weight=1,
        ),
    ] # [Backend] | List of backends associated to a director. (optional)
    capacity = 1 # int | Unused. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "test-director" # str | Name for the Director. (optional)
    quorum = 75 # int | The percentage of capacity that needs to be up for a director to be considered up. `0` to `100`. (optional) if omitted the server will use the default value of 75
    shield = "null" # str, none_type | Selected POP to serve as a shield for the backends. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. (optional) if omitted the server will use the default value of "null"
    type = 1 # int | What type of load balance group to use. (optional) if omitted the server will use the default value of 1
    retries = 5 # int | How many backends to search if it fails. (optional) if omitted the server will use the default value of 5

    # example passing only required values which don't have defaults set
    try:
        # Create a director
        api_response = api_instance.create_director(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DirectorApi->create_director: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a director
        api_response = api_instance.create_director(service_id, version_id, backends=backends, capacity=capacity, comment=comment, name=name, quorum=quorum, shield=shield, type=type, retries=retries)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DirectorApi->create_director: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **backends** | [**[Backend]**](Backend.md)| List of backends associated to a director. | [optional]
 **capacity** | **int**| Unused. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| Name for the Director. | [optional]
 **quorum** | **int**| The percentage of capacity that needs to be up for a director to be considered up. `0` to `100`. | [optional] if omitted the server will use the default value of 75
 **shield** | **str, none_type**| Selected POP to serve as a shield for the backends. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. | [optional] if omitted the server will use the default value of "null"
 **type** | **int**| What type of load balance group to use. | [optional] if omitted the server will use the default value of 1
 **retries** | **int**| How many backends to search if it fails. | [optional] if omitted the server will use the default value of 5

### Return type

[**DirectorResponse**](DirectorResponse.md)

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

# **delete_director**
> InlineResponse200 delete_director(service_id, version_id, director_name)

Delete a director

Delete the director for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import director_api
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
    api_instance = director_api.DirectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    director_name = "test-director" # str | Name for the Director.

    # example passing only required values which don't have defaults set
    try:
        # Delete a director
        api_response = api_instance.delete_director(service_id, version_id, director_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DirectorApi->delete_director: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **director_name** | **str**| Name for the Director. |

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

# **get_director**
> DirectorResponse get_director(service_id, version_id, director_name)

Get a director

Get the director for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import director_api
from fastly.model.director_response import DirectorResponse
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
    api_instance = director_api.DirectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    director_name = "test-director" # str | Name for the Director.

    # example passing only required values which don't have defaults set
    try:
        # Get a director
        api_response = api_instance.get_director(service_id, version_id, director_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DirectorApi->get_director: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **director_name** | **str**| Name for the Director. |

### Return type

[**DirectorResponse**](DirectorResponse.md)

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

# **list_directors**
> [DirectorResponse] list_directors(service_id, version_id)

List directors

List the directors for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import director_api
from fastly.model.director_response import DirectorResponse
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
    api_instance = director_api.DirectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List directors
        api_response = api_instance.list_directors(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DirectorApi->list_directors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[DirectorResponse]**](DirectorResponse.md)

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

# **update_director**
> DirectorResponse update_director(service_id, version_id, director_name)

Update a director

Update the director for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import director_api
from fastly.model.director_response import DirectorResponse
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
    api_instance = director_api.DirectorApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    director_name = "test-director" # str | Name for the Director.

    # example passing only required values which don't have defaults set
    try:
        # Update a director
        api_response = api_instance.update_director(service_id, version_id, director_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DirectorApi->update_director: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **director_name** | **str**| Name for the Director. |

### Return type

[**DirectorResponse**](DirectorResponse.md)

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

