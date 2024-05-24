# fastly.ServerApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pool_server**](ServerApi.md#create_pool_server) | **POST** /service/{service_id}/pool/{pool_id}/server | Add a server to a pool
[**delete_pool_server**](ServerApi.md#delete_pool_server) | **DELETE** /service/{service_id}/pool/{pool_id}/server/{server_id} | Delete a server from a pool
[**get_pool_server**](ServerApi.md#get_pool_server) | **GET** /service/{service_id}/pool/{pool_id}/server/{server_id} | Get a pool server
[**list_pool_servers**](ServerApi.md#list_pool_servers) | **GET** /service/{service_id}/pool/{pool_id}/servers | List servers in a pool
[**update_pool_server**](ServerApi.md#update_pool_server) | **PUT** /service/{service_id}/pool/{pool_id}/server/{server_id} | Update a server


# **create_pool_server**
> ServerResponse create_pool_server(service_id, pool_id)

Add a server to a pool

Creates a single server for a particular service and pool.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import server_api
from fastly.model.server_response import ServerResponse
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
    api_instance = server_api.ServerApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    pool_id = "2Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a Pool.
    weight = 100 # int | Weight (`1-100`) used to load balance this server against others. (optional) if omitted the server will use the default value of 100
    max_conn = 0 # int | Maximum number of connections. If the value is `0`, it inherits the value from pool's `max_conn_default`. (optional) if omitted the server will use the default value of 0
    port = 80 # int | Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS. (optional) if omitted the server will use the default value of 80
    address = "address_example" # str | A hostname, IPv4, or IPv6 address for the server. Required. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    disabled = False # bool | Allows servers to be enabled and disabled in a pool. (optional) if omitted the server will use the default value of False
    override_host = "null" # str, none_type | The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting. (optional) if omitted the server will use the default value of "null"

    # example passing only required values which don't have defaults set
    try:
        # Add a server to a pool
        api_response = api_instance.create_pool_server(service_id, pool_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->create_pool_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a server to a pool
        api_response = api_instance.create_pool_server(service_id, pool_id, weight=weight, max_conn=max_conn, port=port, address=address, comment=comment, disabled=disabled, override_host=override_host)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->create_pool_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **pool_id** | **str**| Alphanumeric string identifying a Pool. |
 **weight** | **int**| Weight (`1-100`) used to load balance this server against others. | [optional] if omitted the server will use the default value of 100
 **max_conn** | **int**| Maximum number of connections. If the value is `0`, it inherits the value from pool&#39;s `max_conn_default`. | [optional] if omitted the server will use the default value of 0
 **port** | **int**| Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS. | [optional] if omitted the server will use the default value of 80
 **address** | **str**| A hostname, IPv4, or IPv6 address for the server. Required. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **disabled** | **bool**| Allows servers to be enabled and disabled in a pool. | [optional] if omitted the server will use the default value of False
 **override_host** | **str, none_type**| The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting. | [optional] if omitted the server will use the default value of "null"

### Return type

[**ServerResponse**](ServerResponse.md)

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

# **delete_pool_server**
> InlineResponse200 delete_pool_server(service_id, pool_id, server_id)

Delete a server from a pool

Deletes a single server for a particular service and pool.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import server_api
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
    api_instance = server_api.ServerApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    pool_id = "2Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a Pool.
    server_id = "6kEuoknxiaDBCLiAjKqyXq" # str | Alphanumeric string identifying a Server.

    # example passing only required values which don't have defaults set
    try:
        # Delete a server from a pool
        api_response = api_instance.delete_pool_server(service_id, pool_id, server_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->delete_pool_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **pool_id** | **str**| Alphanumeric string identifying a Pool. |
 **server_id** | **str**| Alphanumeric string identifying a Server. |

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

# **get_pool_server**
> ServerResponse get_pool_server(service_id, pool_id, server_id)

Get a pool server

Gets a single server for a particular service and pool.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import server_api
from fastly.model.server_response import ServerResponse
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
    api_instance = server_api.ServerApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    pool_id = "2Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a Pool.
    server_id = "6kEuoknxiaDBCLiAjKqyXq" # str | Alphanumeric string identifying a Server.

    # example passing only required values which don't have defaults set
    try:
        # Get a pool server
        api_response = api_instance.get_pool_server(service_id, pool_id, server_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->get_pool_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **pool_id** | **str**| Alphanumeric string identifying a Pool. |
 **server_id** | **str**| Alphanumeric string identifying a Server. |

### Return type

[**ServerResponse**](ServerResponse.md)

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

# **list_pool_servers**
> [ServerResponse] list_pool_servers(service_id, pool_id)

List servers in a pool

Lists all servers for a particular service and pool.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import server_api
from fastly.model.server_response import ServerResponse
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
    api_instance = server_api.ServerApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    pool_id = "2Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a Pool.

    # example passing only required values which don't have defaults set
    try:
        # List servers in a pool
        api_response = api_instance.list_pool_servers(service_id, pool_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->list_pool_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **pool_id** | **str**| Alphanumeric string identifying a Pool. |

### Return type

[**[ServerResponse]**](ServerResponse.md)

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

# **update_pool_server**
> ServerResponse update_pool_server(service_id, pool_id, server_id)

Update a server

Updates a single server for a particular service and pool.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import server_api
from fastly.model.server_response import ServerResponse
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
    api_instance = server_api.ServerApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    pool_id = "2Yd1WfiCBPENLloXfXmlO" # str | Alphanumeric string identifying a Pool.
    server_id = "6kEuoknxiaDBCLiAjKqyXq" # str | Alphanumeric string identifying a Server.
    weight = 100 # int | Weight (`1-100`) used to load balance this server against others. (optional) if omitted the server will use the default value of 100
    max_conn = 0 # int | Maximum number of connections. If the value is `0`, it inherits the value from pool's `max_conn_default`. (optional) if omitted the server will use the default value of 0
    port = 80 # int | Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS. (optional) if omitted the server will use the default value of 80
    address = "address_example" # str | A hostname, IPv4, or IPv6 address for the server. Required. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    disabled = False # bool | Allows servers to be enabled and disabled in a pool. (optional) if omitted the server will use the default value of False
    override_host = "null" # str, none_type | The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting. (optional) if omitted the server will use the default value of "null"

    # example passing only required values which don't have defaults set
    try:
        # Update a server
        api_response = api_instance.update_pool_server(service_id, pool_id, server_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->update_pool_server: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a server
        api_response = api_instance.update_pool_server(service_id, pool_id, server_id, weight=weight, max_conn=max_conn, port=port, address=address, comment=comment, disabled=disabled, override_host=override_host)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServerApi->update_pool_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **pool_id** | **str**| Alphanumeric string identifying a Pool. |
 **server_id** | **str**| Alphanumeric string identifying a Server. |
 **weight** | **int**| Weight (`1-100`) used to load balance this server against others. | [optional] if omitted the server will use the default value of 100
 **max_conn** | **int**| Maximum number of connections. If the value is `0`, it inherits the value from pool&#39;s `max_conn_default`. | [optional] if omitted the server will use the default value of 0
 **port** | **int**| Port number. Setting port `443` does not force TLS. Set `use_tls` in pool to force TLS. | [optional] if omitted the server will use the default value of 80
 **address** | **str**| A hostname, IPv4, or IPv6 address for the server. Required. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **disabled** | **bool**| Allows servers to be enabled and disabled in a pool. | [optional] if omitted the server will use the default value of False
 **override_host** | **str, none_type**| The hostname to override the Host header. Defaults to `null` meaning no override of the Host header if not set. This setting can also be added to a Pool definition. However, the server setting will override the Pool setting. | [optional] if omitted the server will use the default value of "null"

### Return type

[**ServerResponse**](ServerResponse.md)

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

