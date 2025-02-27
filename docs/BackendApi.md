# fastly.BackendApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_backend**](BackendApi.md#create_backend) | **POST** /service/{service_id}/version/{version_id}/backend | Create a backend
[**delete_backend**](BackendApi.md#delete_backend) | **DELETE** /service/{service_id}/version/{version_id}/backend/{backend_name} | Delete a backend
[**get_backend**](BackendApi.md#get_backend) | **GET** /service/{service_id}/version/{version_id}/backend/{backend_name} | Describe a backend
[**list_backends**](BackendApi.md#list_backends) | **GET** /service/{service_id}/version/{version_id}/backend | List backends
[**update_backend**](BackendApi.md#update_backend) | **PUT** /service/{service_id}/version/{version_id}/backend/{backend_name} | Update a backend


# **create_backend**
> BackendResponse create_backend(service_id, version_id)

Create a backend

Create a backend for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import backend_api
from fastly.model.backend_response import BackendResponse
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
    api_instance = backend_api.BackendApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    address = "address_example" # str | A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend. (optional)
    auto_loadbalance = True # bool | Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a `request_condition` will be selected based on their `weight`. (optional)
    between_bytes_timeout = 1 # int | Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. (optional)
    client_cert = "client_cert_example" # str, none_type | Unused. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    connect_timeout = 1 # int | Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`. (optional)
    first_byte_timeout = 1 # int | Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`. (optional)
    healthcheck = "healthcheck_example" # str, none_type | The name of the healthcheck to use with this backend. (optional)
    hostname = "hostname_example" # str, none_type | The hostname of the backend. May be used as an alternative to `address` to set the backend location. (optional)
    ipv4 = "ipv4_example" # str, none_type | IPv4 address of the backend. May be used as an alternative to `address` to set the backend location. (optional)
    ipv6 = "ipv6_example" # str, none_type | IPv6 address of the backend. May be used as an alternative to `address` to set the backend location. (optional)
    keepalive_time = 1 # int, none_type | How long in seconds to keep a persistent connection to the backend between requests. By default, Varnish keeps connections open as long as it can. (optional)
    max_conn = 1 # int | Maximum number of concurrent connections this backend will accept. (optional)
    max_tls_version = "max_tls_version_example" # str, none_type | Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. (optional)
    min_tls_version = "min_tls_version_example" # str, none_type | Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. (optional)
    name = "test-backend" # str | The name of the backend. (optional)
    override_host = "override_host_example" # str, none_type | If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL. (optional)
    port = 1 # int | Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request. (optional)
    request_condition = "request_condition_example" # str | Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests. (optional)
    share_key = "C" # str, none_type | Value that when shared across backends will enable those backends to share the same health check. (optional)
    shield = "shield_example" # str, none_type | Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding). (optional)
    ssl_ca_cert = "ssl_ca_cert_example" # str, none_type | CA certificate attached to origin. (optional)
    ssl_cert_hostname = "ssl_cert_hostname_example" # str, none_type | Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all. (optional)
    ssl_check_cert = True # bool, none_type | Be strict on checking SSL certs. (optional) if omitted the server will use the default value of True
    ssl_ciphers = "ssl_ciphers_example" # str, none_type | List of [OpenSSL ciphers](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. (optional)
    ssl_client_cert = "ssl_client_cert_example" # str, none_type | Client certificate attached to origin. (optional)
    ssl_client_key = "ssl_client_key_example" # str, none_type | Client key attached to origin. (optional)
    ssl_hostname = "ssl_hostname_example" # str, none_type | Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation. (optional)
    ssl_sni_hostname = "ssl_sni_hostname_example" # str, none_type | Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all. (optional)
    tcp_keepalive_enable = True # bool, none_type | Whether to enable TCP keepalives for backend connections. Varnish defaults to using keepalives if this is unspecified. (optional)
    tcp_keepalive_interval = 1 # int, none_type | Interval in seconds between subsequent keepalive probes. (optional)
    tcp_keepalive_probes = 1 # int, none_type | Number of unacknowledged probes to send before considering the connection dead. (optional)
    tcp_keepalive_time = 1 # int, none_type | Interval in seconds between the last data packet sent and the first keepalive probe. (optional)
    use_ssl = True # bool | Whether or not to require TLS for connections to this backend. (optional)
    weight = 1 # int | Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a backend
        api_response = api_instance.create_backend(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->create_backend: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a backend
        api_response = api_instance.create_backend(service_id, version_id, address=address, auto_loadbalance=auto_loadbalance, between_bytes_timeout=between_bytes_timeout, client_cert=client_cert, comment=comment, connect_timeout=connect_timeout, first_byte_timeout=first_byte_timeout, healthcheck=healthcheck, hostname=hostname, ipv4=ipv4, ipv6=ipv6, keepalive_time=keepalive_time, max_conn=max_conn, max_tls_version=max_tls_version, min_tls_version=min_tls_version, name=name, override_host=override_host, port=port, request_condition=request_condition, share_key=share_key, shield=shield, ssl_ca_cert=ssl_ca_cert, ssl_cert_hostname=ssl_cert_hostname, ssl_check_cert=ssl_check_cert, ssl_ciphers=ssl_ciphers, ssl_client_cert=ssl_client_cert, ssl_client_key=ssl_client_key, ssl_hostname=ssl_hostname, ssl_sni_hostname=ssl_sni_hostname, tcp_keepalive_enable=tcp_keepalive_enable, tcp_keepalive_interval=tcp_keepalive_interval, tcp_keepalive_probes=tcp_keepalive_probes, tcp_keepalive_time=tcp_keepalive_time, use_ssl=use_ssl, weight=weight)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->create_backend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **address** | **str**| A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend. | [optional]
 **auto_loadbalance** | **bool**| Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don&#39;t have a `request_condition` will be selected based on their `weight`. | [optional]
 **between_bytes_timeout** | **int**| Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. | [optional]
 **client_cert** | **str, none_type**| Unused. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **connect_timeout** | **int**| Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`. | [optional]
 **first_byte_timeout** | **int**| Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`. | [optional]
 **healthcheck** | **str, none_type**| The name of the healthcheck to use with this backend. | [optional]
 **hostname** | **str, none_type**| The hostname of the backend. May be used as an alternative to `address` to set the backend location. | [optional]
 **ipv4** | **str, none_type**| IPv4 address of the backend. May be used as an alternative to `address` to set the backend location. | [optional]
 **ipv6** | **str, none_type**| IPv6 address of the backend. May be used as an alternative to `address` to set the backend location. | [optional]
 **keepalive_time** | **int, none_type**| How long in seconds to keep a persistent connection to the backend between requests. By default, Varnish keeps connections open as long as it can. | [optional]
 **max_conn** | **int**| Maximum number of concurrent connections this backend will accept. | [optional]
 **max_tls_version** | **str, none_type**| Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. | [optional]
 **min_tls_version** | **str, none_type**| Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. | [optional]
 **name** | **str**| The name of the backend. | [optional]
 **override_host** | **str, none_type**| If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL. | [optional]
 **port** | **int**| Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request. | [optional]
 **request_condition** | **str**| Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests. | [optional]
 **share_key** | **str, none_type**| Value that when shared across backends will enable those backends to share the same health check. | [optional]
 **shield** | **str, none_type**| Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding). | [optional]
 **ssl_ca_cert** | **str, none_type**| CA certificate attached to origin. | [optional]
 **ssl_cert_hostname** | **str, none_type**| Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all. | [optional]
 **ssl_check_cert** | **bool, none_type**| Be strict on checking SSL certs. | [optional] if omitted the server will use the default value of True
 **ssl_ciphers** | **str, none_type**| List of [OpenSSL ciphers](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. | [optional]
 **ssl_client_cert** | **str, none_type**| Client certificate attached to origin. | [optional]
 **ssl_client_key** | **str, none_type**| Client key attached to origin. | [optional]
 **ssl_hostname** | **str, none_type**| Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation. | [optional]
 **ssl_sni_hostname** | **str, none_type**| Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all. | [optional]
 **tcp_keepalive_enable** | **bool, none_type**| Whether to enable TCP keepalives for backend connections. Varnish defaults to using keepalives if this is unspecified. | [optional]
 **tcp_keepalive_interval** | **int, none_type**| Interval in seconds between subsequent keepalive probes. | [optional]
 **tcp_keepalive_probes** | **int, none_type**| Number of unacknowledged probes to send before considering the connection dead. | [optional]
 **tcp_keepalive_time** | **int, none_type**| Interval in seconds between the last data packet sent and the first keepalive probe. | [optional]
 **use_ssl** | **bool**| Whether or not to require TLS for connections to this backend. | [optional]
 **weight** | **int**| Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true. | [optional]

### Return type

[**BackendResponse**](BackendResponse.md)

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

# **delete_backend**
> InlineResponse200 delete_backend(service_id, version_id, backend_name)

Delete a backend

Delete the backend for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import backend_api
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
    api_instance = backend_api.BackendApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    backend_name = "test-backend" # str | The name of the backend.

    # example passing only required values which don't have defaults set
    try:
        # Delete a backend
        api_response = api_instance.delete_backend(service_id, version_id, backend_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->delete_backend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **backend_name** | **str**| The name of the backend. |

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

# **get_backend**
> BackendResponse get_backend(service_id, version_id, backend_name)

Describe a backend

Get the backend for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import backend_api
from fastly.model.backend_response import BackendResponse
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
    api_instance = backend_api.BackendApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    backend_name = "test-backend" # str | The name of the backend.

    # example passing only required values which don't have defaults set
    try:
        # Describe a backend
        api_response = api_instance.get_backend(service_id, version_id, backend_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->get_backend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **backend_name** | **str**| The name of the backend. |

### Return type

[**BackendResponse**](BackendResponse.md)

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

# **list_backends**
> [BackendResponse] list_backends(service_id, version_id)

List backends

List all backends for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import backend_api
from fastly.model.backend_response import BackendResponse
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
    api_instance = backend_api.BackendApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List backends
        api_response = api_instance.list_backends(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->list_backends: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[BackendResponse]**](BackendResponse.md)

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

# **update_backend**
> BackendResponse update_backend(service_id, version_id, backend_name)

Update a backend

Update the backend for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import backend_api
from fastly.model.backend_response import BackendResponse
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
    api_instance = backend_api.BackendApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    backend_name = "test-backend" # str | The name of the backend.
    address = "address_example" # str | A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend. (optional)
    auto_loadbalance = True # bool | Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don't have a `request_condition` will be selected based on their `weight`. (optional)
    between_bytes_timeout = 1 # int | Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. (optional)
    client_cert = "client_cert_example" # str, none_type | Unused. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    connect_timeout = 1 # int | Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`. (optional)
    first_byte_timeout = 1 # int | Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`. (optional)
    healthcheck = "healthcheck_example" # str, none_type | The name of the healthcheck to use with this backend. (optional)
    hostname = "hostname_example" # str, none_type | The hostname of the backend. May be used as an alternative to `address` to set the backend location. (optional)
    ipv4 = "ipv4_example" # str, none_type | IPv4 address of the backend. May be used as an alternative to `address` to set the backend location. (optional)
    ipv6 = "ipv6_example" # str, none_type | IPv6 address of the backend. May be used as an alternative to `address` to set the backend location. (optional)
    keepalive_time = 1 # int, none_type | How long in seconds to keep a persistent connection to the backend between requests. By default, Varnish keeps connections open as long as it can. (optional)
    max_conn = 1 # int | Maximum number of concurrent connections this backend will accept. (optional)
    max_tls_version = "max_tls_version_example" # str, none_type | Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. (optional)
    min_tls_version = "min_tls_version_example" # str, none_type | Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. (optional)
    name = "test-backend" # str | The name of the backend. (optional)
    override_host = "override_host_example" # str, none_type | If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL. (optional)
    port = 1 # int | Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request. (optional)
    request_condition = "request_condition_example" # str | Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests. (optional)
    share_key = "C" # str, none_type | Value that when shared across backends will enable those backends to share the same health check. (optional)
    shield = "shield_example" # str, none_type | Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding). (optional)
    ssl_ca_cert = "ssl_ca_cert_example" # str, none_type | CA certificate attached to origin. (optional)
    ssl_cert_hostname = "ssl_cert_hostname_example" # str, none_type | Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all. (optional)
    ssl_check_cert = True # bool, none_type | Be strict on checking SSL certs. (optional) if omitted the server will use the default value of True
    ssl_ciphers = "ssl_ciphers_example" # str, none_type | List of [OpenSSL ciphers](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. (optional)
    ssl_client_cert = "ssl_client_cert_example" # str, none_type | Client certificate attached to origin. (optional)
    ssl_client_key = "ssl_client_key_example" # str, none_type | Client key attached to origin. (optional)
    ssl_hostname = "ssl_hostname_example" # str, none_type | Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation. (optional)
    ssl_sni_hostname = "ssl_sni_hostname_example" # str, none_type | Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all. (optional)
    tcp_keepalive_enable = True # bool, none_type | Whether to enable TCP keepalives for backend connections. Varnish defaults to using keepalives if this is unspecified. (optional)
    tcp_keepalive_interval = 1 # int, none_type | Interval in seconds between subsequent keepalive probes. (optional)
    tcp_keepalive_probes = 1 # int, none_type | Number of unacknowledged probes to send before considering the connection dead. (optional)
    tcp_keepalive_time = 1 # int, none_type | Interval in seconds between the last data packet sent and the first keepalive probe. (optional)
    use_ssl = True # bool | Whether or not to require TLS for connections to this backend. (optional)
    weight = 1 # int | Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a backend
        api_response = api_instance.update_backend(service_id, version_id, backend_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->update_backend: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a backend
        api_response = api_instance.update_backend(service_id, version_id, backend_name, address=address, auto_loadbalance=auto_loadbalance, between_bytes_timeout=between_bytes_timeout, client_cert=client_cert, comment=comment, connect_timeout=connect_timeout, first_byte_timeout=first_byte_timeout, healthcheck=healthcheck, hostname=hostname, ipv4=ipv4, ipv6=ipv6, keepalive_time=keepalive_time, max_conn=max_conn, max_tls_version=max_tls_version, min_tls_version=min_tls_version, name=name, override_host=override_host, port=port, request_condition=request_condition, share_key=share_key, shield=shield, ssl_ca_cert=ssl_ca_cert, ssl_cert_hostname=ssl_cert_hostname, ssl_check_cert=ssl_check_cert, ssl_ciphers=ssl_ciphers, ssl_client_cert=ssl_client_cert, ssl_client_key=ssl_client_key, ssl_hostname=ssl_hostname, ssl_sni_hostname=ssl_sni_hostname, tcp_keepalive_enable=tcp_keepalive_enable, tcp_keepalive_interval=tcp_keepalive_interval, tcp_keepalive_probes=tcp_keepalive_probes, tcp_keepalive_time=tcp_keepalive_time, use_ssl=use_ssl, weight=weight)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BackendApi->update_backend: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **backend_name** | **str**| The name of the backend. |
 **address** | **str**| A hostname, IPv4, or IPv6 address for the backend. This is the preferred way to specify the location of your backend. | [optional]
 **auto_loadbalance** | **bool**| Whether or not this backend should be automatically load balanced. If true, all backends with this setting that don&#39;t have a `request_condition` will be selected based on their `weight`. | [optional]
 **between_bytes_timeout** | **int**| Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. | [optional]
 **client_cert** | **str, none_type**| Unused. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **connect_timeout** | **int**| Maximum duration in milliseconds to wait for a connection to this backend to be established. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.connect_timeout`. | [optional]
 **first_byte_timeout** | **int**| Maximum duration in milliseconds to wait for the server response to begin after a TCP connection is established and the request has been sent. If exceeded, the connection is aborted and a synthetic `503` response will be presented instead. May be set at runtime using `bereq.first_byte_timeout`. | [optional]
 **healthcheck** | **str, none_type**| The name of the healthcheck to use with this backend. | [optional]
 **hostname** | **str, none_type**| The hostname of the backend. May be used as an alternative to `address` to set the backend location. | [optional]
 **ipv4** | **str, none_type**| IPv4 address of the backend. May be used as an alternative to `address` to set the backend location. | [optional]
 **ipv6** | **str, none_type**| IPv6 address of the backend. May be used as an alternative to `address` to set the backend location. | [optional]
 **keepalive_time** | **int, none_type**| How long in seconds to keep a persistent connection to the backend between requests. By default, Varnish keeps connections open as long as it can. | [optional]
 **max_conn** | **int**| Maximum number of concurrent connections this backend will accept. | [optional]
 **max_tls_version** | **str, none_type**| Maximum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. | [optional]
 **min_tls_version** | **str, none_type**| Minimum allowed TLS version on SSL connections to this backend. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. | [optional]
 **name** | **str**| The name of the backend. | [optional]
 **override_host** | **str, none_type**| If set, will replace the client-supplied HTTP `Host` header on connections to this backend. Applied after VCL has been processed, so this setting will take precedence over changing `bereq.http.Host` in VCL. | [optional]
 **port** | **int**| Port on which the backend server is listening for connections from Fastly. Setting `port` to 80 or 443 will also set `use_ssl` automatically (to false and true respectively), unless explicitly overridden by setting `use_ssl` in the same request. | [optional]
 **request_condition** | **str**| Name of a Condition, which if satisfied, will select this backend during a request. If set, will override any `auto_loadbalance` setting. By default, the first backend added to a service is selected for all requests. | [optional]
 **share_key** | **str, none_type**| Value that when shared across backends will enable those backends to share the same health check. | [optional]
 **shield** | **str, none_type**| Identifier of the POP to use as a [shield](https://docs.fastly.com/en/guides/shielding). | [optional]
 **ssl_ca_cert** | **str, none_type**| CA certificate attached to origin. | [optional]
 **ssl_cert_hostname** | **str, none_type**| Overrides `ssl_hostname`, but only for cert verification. Does not affect SNI at all. | [optional]
 **ssl_check_cert** | **bool, none_type**| Be strict on checking SSL certs. | [optional] if omitted the server will use the default value of True
 **ssl_ciphers** | **str, none_type**| List of [OpenSSL ciphers](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) to support for connections to this origin. If your backend server is not able to negotiate a connection meeting this constraint, a synthetic `503` error response will be generated. | [optional]
 **ssl_client_cert** | **str, none_type**| Client certificate attached to origin. | [optional]
 **ssl_client_key** | **str, none_type**| Client key attached to origin. | [optional]
 **ssl_hostname** | **str, none_type**| Use `ssl_cert_hostname` and `ssl_sni_hostname` to configure certificate validation. | [optional]
 **ssl_sni_hostname** | **str, none_type**| Overrides `ssl_hostname`, but only for SNI in the handshake. Does not affect cert validation at all. | [optional]
 **tcp_keepalive_enable** | **bool, none_type**| Whether to enable TCP keepalives for backend connections. Varnish defaults to using keepalives if this is unspecified. | [optional]
 **tcp_keepalive_interval** | **int, none_type**| Interval in seconds between subsequent keepalive probes. | [optional]
 **tcp_keepalive_probes** | **int, none_type**| Number of unacknowledged probes to send before considering the connection dead. | [optional]
 **tcp_keepalive_time** | **int, none_type**| Interval in seconds between the last data packet sent and the first keepalive probe. | [optional]
 **use_ssl** | **bool**| Whether or not to require TLS for connections to this backend. | [optional]
 **weight** | **int**| Weight used to load balance this backend against others. May be any positive integer. If `auto_loadbalance` is true, the chance of this backend being selected is equal to its own weight over the sum of all weights for backends that have `auto_loadbalance` set to true. | [optional]

### Return type

[**BackendResponse**](BackendResponse.md)

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

