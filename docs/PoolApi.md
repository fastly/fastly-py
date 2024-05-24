# fastly.PoolApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_server_pool**](PoolApi.md#create_server_pool) | **POST** /service/{service_id}/version/{version_id}/pool | Create a server pool
[**delete_server_pool**](PoolApi.md#delete_server_pool) | **DELETE** /service/{service_id}/version/{version_id}/pool/{pool_name} | Delete a server pool
[**get_server_pool**](PoolApi.md#get_server_pool) | **GET** /service/{service_id}/version/{version_id}/pool/{pool_name} | Get a server pool
[**list_server_pools**](PoolApi.md#list_server_pools) | **GET** /service/{service_id}/version/{version_id}/pool | List server pools
[**update_server_pool**](PoolApi.md#update_server_pool) | **PUT** /service/{service_id}/version/{version_id}/pool/{pool_name} | Update a server pool


# **create_server_pool**
> PoolResponsePost create_server_pool(service_id, version_id)

Create a server pool

Creates a pool for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import pool_api
from fastly.model.pool_response_post import PoolResponsePost
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
    api_instance = pool_api.PoolApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_cert_hostname = "null" # str, none_type | The hostname used to verify a server's certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN). (optional) if omitted the server will use the default value of "null"
    use_tls = 0 # int | Whether to use TLS. (optional) if omitted the server will use the default value of 0
    created_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    deleted_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    updated_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    service_id2 = "service_id_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    name = "my-pool" # str | Name for the Pool. (optional)
    shield = "null" # str, none_type | Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. (optional) if omitted the server will use the default value of "null"
    request_condition = "request_condition_example" # str, none_type | Condition which, if met, will select this configuration during a request. Optional. (optional)
    tls_ciphers = "tls_ciphers_example" # str, none_type | List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional. (optional)
    tls_sni_hostname = "tls_sni_hostname_example" # str, none_type | SNI hostname. Optional. (optional)
    min_tls_version = 1 # int, none_type | Minimum allowed TLS version on connections to this server. Optional. (optional)
    max_tls_version = 1 # int, none_type | Maximum allowed TLS version on connections to this server. Optional. (optional)
    healthcheck = "healthcheck_example" # str, none_type | Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    type = "random" # str | What type of load balance group to use. (optional)
    override_host = "null" # str, none_type | The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting. (optional) if omitted the server will use the default value of "null"
    between_bytes_timeout = 10000 # int | Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. (optional) if omitted the server will use the default value of 10000
    connect_timeout = 1 # int | How long to wait for a timeout in milliseconds. Optional. (optional)
    first_byte_timeout = 1 # int | How long to wait for the first byte in milliseconds. Optional. (optional)
    max_conn_default = 200 # int | Maximum number of connections. Optional. (optional) if omitted the server will use the default value of 200
    quorum = 75 # int | Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up. (optional) if omitted the server will use the default value of 75
    tls_check_cert = 1 # int, none_type | Be strict on checking TLS certs. Optional. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a server pool
        api_response = api_instance.create_server_pool(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->create_server_pool: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a server pool
        api_response = api_instance.create_server_pool(service_id, version_id, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_cert_hostname=tls_cert_hostname, use_tls=use_tls, created_at=created_at, deleted_at=deleted_at, updated_at=updated_at, service_id2=service_id2, version=version, name=name, shield=shield, request_condition=request_condition, tls_ciphers=tls_ciphers, tls_sni_hostname=tls_sni_hostname, min_tls_version=min_tls_version, max_tls_version=max_tls_version, healthcheck=healthcheck, comment=comment, type=type, override_host=override_host, between_bytes_timeout=between_bytes_timeout, connect_timeout=connect_timeout, first_byte_timeout=first_byte_timeout, max_conn_default=max_conn_default, quorum=quorum, tls_check_cert=tls_check_cert)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->create_server_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_cert_hostname** | **str, none_type**| The hostname used to verify a server&#39;s certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN). | [optional] if omitted the server will use the default value of "null"
 **use_tls** | **int**| Whether to use TLS. | [optional] if omitted the server will use the default value of 0
 **created_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **deleted_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **updated_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **service_id2** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **name** | **str**| Name for the Pool. | [optional]
 **shield** | **str, none_type**| Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. | [optional] if omitted the server will use the default value of "null"
 **request_condition** | **str, none_type**| Condition which, if met, will select this configuration during a request. Optional. | [optional]
 **tls_ciphers** | **str, none_type**| List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional. | [optional]
 **tls_sni_hostname** | **str, none_type**| SNI hostname. Optional. | [optional]
 **min_tls_version** | **int, none_type**| Minimum allowed TLS version on connections to this server. Optional. | [optional]
 **max_tls_version** | **int, none_type**| Maximum allowed TLS version on connections to this server. Optional. | [optional]
 **healthcheck** | **str, none_type**| Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **type** | **str**| What type of load balance group to use. | [optional]
 **override_host** | **str, none_type**| The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting. | [optional] if omitted the server will use the default value of "null"
 **between_bytes_timeout** | **int**| Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. | [optional] if omitted the server will use the default value of 10000
 **connect_timeout** | **int**| How long to wait for a timeout in milliseconds. Optional. | [optional]
 **first_byte_timeout** | **int**| How long to wait for the first byte in milliseconds. Optional. | [optional]
 **max_conn_default** | **int**| Maximum number of connections. Optional. | [optional] if omitted the server will use the default value of 200
 **quorum** | **int**| Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up. | [optional] if omitted the server will use the default value of 75
 **tls_check_cert** | **int, none_type**| Be strict on checking TLS certs. Optional. | [optional]

### Return type

[**PoolResponsePost**](PoolResponsePost.md)

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

# **delete_server_pool**
> InlineResponse200 delete_server_pool(service_id, version_id, pool_name)

Delete a server pool

Deletes a specific pool for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import pool_api
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
    api_instance = pool_api.PoolApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    pool_name = "my-pool" # str | Name for the Pool.

    # example passing only required values which don't have defaults set
    try:
        # Delete a server pool
        api_response = api_instance.delete_server_pool(service_id, version_id, pool_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->delete_server_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **pool_name** | **str**| Name for the Pool. |

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

# **get_server_pool**
> PoolResponse get_server_pool(service_id, version_id, pool_name)

Get a server pool

Gets a single pool for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import pool_api
from fastly.model.pool_response import PoolResponse
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
    api_instance = pool_api.PoolApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    pool_name = "my-pool" # str | Name for the Pool.

    # example passing only required values which don't have defaults set
    try:
        # Get a server pool
        api_response = api_instance.get_server_pool(service_id, version_id, pool_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->get_server_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **pool_name** | **str**| Name for the Pool. |

### Return type

[**PoolResponse**](PoolResponse.md)

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

# **list_server_pools**
> [PoolResponse] list_server_pools(service_id, version_id)

List server pools

Lists all pools for a particular service and pool.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import pool_api
from fastly.model.pool_response import PoolResponse
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
    api_instance = pool_api.PoolApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List server pools
        api_response = api_instance.list_server_pools(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->list_server_pools: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[PoolResponse]**](PoolResponse.md)

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

# **update_server_pool**
> PoolResponse update_server_pool(service_id, version_id, pool_name)

Update a server pool

Updates a specific pool for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import pool_api
from fastly.model.pool_response import PoolResponse
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
    api_instance = pool_api.PoolApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    pool_name = "my-pool" # str | Name for the Pool.
    tls_ca_cert = "null" # str, none_type | A secure certificate to authenticate a server with. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_cert = "null" # str, none_type | The client certificate used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_client_key = "null" # str, none_type | The client private key used to make authenticated requests. Must be in PEM format. (optional) if omitted the server will use the default value of "null"
    tls_cert_hostname = "null" # str, none_type | The hostname used to verify a server's certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN). (optional) if omitted the server will use the default value of "null"
    use_tls = 0 # int | Whether to use TLS. (optional) if omitted the server will use the default value of 0
    created_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    deleted_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    updated_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    service_id2 = "service_id_example" # str |  (optional)
    version = "version_example" # str |  (optional)
    name = "my-pool" # str | Name for the Pool. (optional)
    shield = "null" # str, none_type | Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. (optional) if omitted the server will use the default value of "null"
    request_condition = "request_condition_example" # str, none_type | Condition which, if met, will select this configuration during a request. Optional. (optional)
    tls_ciphers = "tls_ciphers_example" # str, none_type | List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional. (optional)
    tls_sni_hostname = "tls_sni_hostname_example" # str, none_type | SNI hostname. Optional. (optional)
    min_tls_version = 1 # int, none_type | Minimum allowed TLS version on connections to this server. Optional. (optional)
    max_tls_version = 1 # int, none_type | Maximum allowed TLS version on connections to this server. Optional. (optional)
    healthcheck = "healthcheck_example" # str, none_type | Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools. (optional)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    type = "random" # str | What type of load balance group to use. (optional)
    override_host = "null" # str, none_type | The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting. (optional) if omitted the server will use the default value of "null"
    between_bytes_timeout = 10000 # int | Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. (optional) if omitted the server will use the default value of 10000
    connect_timeout = 1 # int | How long to wait for a timeout in milliseconds. Optional. (optional)
    first_byte_timeout = 1 # int | How long to wait for the first byte in milliseconds. Optional. (optional)
    max_conn_default = 200 # int | Maximum number of connections. Optional. (optional) if omitted the server will use the default value of 200
    quorum = 75 # int | Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up. (optional) if omitted the server will use the default value of 75
    tls_check_cert = 1 # int, none_type | Be strict on checking TLS certs. Optional. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a server pool
        api_response = api_instance.update_server_pool(service_id, version_id, pool_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->update_server_pool: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a server pool
        api_response = api_instance.update_server_pool(service_id, version_id, pool_name, tls_ca_cert=tls_ca_cert, tls_client_cert=tls_client_cert, tls_client_key=tls_client_key, tls_cert_hostname=tls_cert_hostname, use_tls=use_tls, created_at=created_at, deleted_at=deleted_at, updated_at=updated_at, service_id2=service_id2, version=version, name=name, shield=shield, request_condition=request_condition, tls_ciphers=tls_ciphers, tls_sni_hostname=tls_sni_hostname, min_tls_version=min_tls_version, max_tls_version=max_tls_version, healthcheck=healthcheck, comment=comment, type=type, override_host=override_host, between_bytes_timeout=between_bytes_timeout, connect_timeout=connect_timeout, first_byte_timeout=first_byte_timeout, max_conn_default=max_conn_default, quorum=quorum, tls_check_cert=tls_check_cert)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PoolApi->update_server_pool: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **pool_name** | **str**| Name for the Pool. |
 **tls_ca_cert** | **str, none_type**| A secure certificate to authenticate a server with. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_cert** | **str, none_type**| The client certificate used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_client_key** | **str, none_type**| The client private key used to make authenticated requests. Must be in PEM format. | [optional] if omitted the server will use the default value of "null"
 **tls_cert_hostname** | **str, none_type**| The hostname used to verify a server&#39;s certificate. It can either be the Common Name (CN) or a Subject Alternative Name (SAN). | [optional] if omitted the server will use the default value of "null"
 **use_tls** | **int**| Whether to use TLS. | [optional] if omitted the server will use the default value of 0
 **created_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **deleted_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **updated_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **service_id2** | **str**|  | [optional]
 **version** | **str**|  | [optional]
 **name** | **str**| Name for the Pool. | [optional]
 **shield** | **str, none_type**| Selected POP to serve as a shield for the servers. Defaults to `null` meaning no origin shielding if not set. Refer to the [POPs API endpoint](https://www.fastly.com/documentation/reference/api/utils/pops/) to get a list of available POPs used for shielding. | [optional] if omitted the server will use the default value of "null"
 **request_condition** | **str, none_type**| Condition which, if met, will select this configuration during a request. Optional. | [optional]
 **tls_ciphers** | **str, none_type**| List of OpenSSL ciphers (see the [openssl.org manpages](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html) for details). Optional. | [optional]
 **tls_sni_hostname** | **str, none_type**| SNI hostname. Optional. | [optional]
 **min_tls_version** | **int, none_type**| Minimum allowed TLS version on connections to this server. Optional. | [optional]
 **max_tls_version** | **int, none_type**| Maximum allowed TLS version on connections to this server. Optional. | [optional]
 **healthcheck** | **str, none_type**| Name of the healthcheck to use with this pool. Can be empty and could be reused across multiple backend and pools. | [optional]
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **type** | **str**| What type of load balance group to use. | [optional]
 **override_host** | **str, none_type**| The hostname to [override the Host header](https://docs.fastly.com/en/guides/specifying-an-override-host). Defaults to `null` meaning no override of the Host header will occur. This setting can also be added to a Server definition. If the field is set on a Server definition it will override the Pool setting. | [optional] if omitted the server will use the default value of "null"
 **between_bytes_timeout** | **int**| Maximum duration in milliseconds that Fastly will wait while receiving no data on a download from a backend. If exceeded, the response received so far will be considered complete and the fetch will end. May be set at runtime using `bereq.between_bytes_timeout`. | [optional] if omitted the server will use the default value of 10000
 **connect_timeout** | **int**| How long to wait for a timeout in milliseconds. Optional. | [optional]
 **first_byte_timeout** | **int**| How long to wait for the first byte in milliseconds. Optional. | [optional]
 **max_conn_default** | **int**| Maximum number of connections. Optional. | [optional] if omitted the server will use the default value of 200
 **quorum** | **int**| Percentage of capacity (`0-100`) that needs to be operationally available for a pool to be considered up. | [optional] if omitted the server will use the default value of 75
 **tls_check_cert** | **int, none_type**| Be strict on checking TLS certs. Optional. | [optional]

### Return type

[**PoolResponse**](PoolResponse.md)

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

