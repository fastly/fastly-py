# fastly.DomainApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_domain**](DomainApi.md#check_domain) | **GET** /service/{service_id}/version/{version_id}/domain/{domain_name}/check | Validate DNS configuration for a single domain on a service
[**check_domains**](DomainApi.md#check_domains) | **GET** /service/{service_id}/version/{version_id}/domain/check_all | Validate DNS configuration for all domains on a service
[**create_domain**](DomainApi.md#create_domain) | **POST** /service/{service_id}/version/{version_id}/domain | Add a domain name to a service
[**delete_domain**](DomainApi.md#delete_domain) | **DELETE** /service/{service_id}/version/{version_id}/domain/{domain_name} | Remove a domain from a service
[**get_domain**](DomainApi.md#get_domain) | **GET** /service/{service_id}/version/{version_id}/domain/{domain_name} | Describe a domain
[**list_domains**](DomainApi.md#list_domains) | **GET** /service/{service_id}/version/{version_id}/domain | List domains
[**update_domain**](DomainApi.md#update_domain) | **PUT** /service/{service_id}/version/{version_id}/domain/{domain_name} | Update a domain


# **check_domain**
> DomainCheckResponse check_domain(service_id, version_id, domain_name)

Validate DNS configuration for a single domain on a service

Checks the status of a specific domain's DNS record for a Service Version. Returns an array in the same format as domain/check_all.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
from fastly.model.domain_check_response import DomainCheckResponse
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    domain_name = "www.example.com" # str | The name of the domain or domains associated with this service.

    # example passing only required values which don't have defaults set
    try:
        # Validate DNS configuration for a single domain on a service
        api_response = api_instance.check_domain(service_id, version_id, domain_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->check_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **domain_name** | **str**| The name of the domain or domains associated with this service. |

### Return type

[**DomainCheckResponse**](DomainCheckResponse.md)

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

# **check_domains**
> DomainCheckResponseList check_domains(service_id, version_id)

Validate DNS configuration for all domains on a service

Checks the status of all domains' DNS records for a Service Version. Returns an array of 3 items for each domain; the first is the details for the domain, the second is the current CNAME of the domain, and the third is a boolean indicating whether or not it has been properly setup to use Fastly.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
from fastly.model.domain_check_response_list import DomainCheckResponseList
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # Validate DNS configuration for all domains on a service
        api_response = api_instance.check_domains(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->check_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**DomainCheckResponseList**](DomainCheckResponseList.md)

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

# **create_domain**
> DomainResponse create_domain(service_id, version_id)

Add a domain name to a service

Create a domain for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
from fastly.model.domain_response import DomainResponse
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "www.example.com" # str | The name of the domain or domains associated with this service. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a domain name to a service
        api_response = api_instance.create_domain(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->create_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a domain name to a service
        api_response = api_instance.create_domain(service_id, version_id, comment=comment, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->create_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| The name of the domain or domains associated with this service. | [optional]

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **delete_domain**
> InlineResponse200 delete_domain(service_id, version_id, domain_name)

Remove a domain from a service

Delete the domain for a particular service and versions.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    domain_name = "www.example.com" # str | The name of the domain or domains associated with this service.

    # example passing only required values which don't have defaults set
    try:
        # Remove a domain from a service
        api_response = api_instance.delete_domain(service_id, version_id, domain_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->delete_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **domain_name** | **str**| The name of the domain or domains associated with this service. |

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

# **get_domain**
> DomainResponse get_domain(service_id, version_id, domain_name)

Describe a domain

Get the domain for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
from fastly.model.domain_response import DomainResponse
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    domain_name = "www.example.com" # str | The name of the domain or domains associated with this service.

    # example passing only required values which don't have defaults set
    try:
        # Describe a domain
        api_response = api_instance.get_domain(service_id, version_id, domain_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->get_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **domain_name** | **str**| The name of the domain or domains associated with this service. |

### Return type

[**DomainResponse**](DomainResponse.md)

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

# **list_domains**
> DomainsResponse list_domains(service_id, version_id)

List domains

List all the domains for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
from fastly.model.domains_response import DomainsResponse
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List domains
        api_response = api_instance.list_domains(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->list_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**DomainsResponse**](DomainsResponse.md)

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

# **update_domain**
> DomainResponse update_domain(service_id, version_id, domain_name)

Update a domain

Update the domain for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import domain_api
from fastly.model.domain_response import DomainResponse
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
    api_instance = domain_api.DomainApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    domain_name = "www.example.com" # str | The name of the domain or domains associated with this service.
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "www.example.com" # str | The name of the domain or domains associated with this service. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a domain
        api_response = api_instance.update_domain(service_id, version_id, domain_name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->update_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a domain
        api_response = api_instance.update_domain(service_id, version_id, domain_name, comment=comment, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DomainApi->update_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |
 **domain_name** | **str**| The name of the domain or domains associated with this service. |
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| The name of the domain or domains associated with this service. | [optional]

### Return type

[**DomainResponse**](DomainResponse.md)

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

