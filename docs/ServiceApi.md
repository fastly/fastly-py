# fastly.ServiceApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service**](ServiceApi.md#create_service) | **POST** /service | Create a service
[**delete_service**](ServiceApi.md#delete_service) | **DELETE** /service/{service_id} | Delete a service
[**get_service**](ServiceApi.md#get_service) | **GET** /service/{service_id} | Get a service
[**get_service_detail**](ServiceApi.md#get_service_detail) | **GET** /service/{service_id}/details | Get service details
[**list_service_domains**](ServiceApi.md#list_service_domains) | **GET** /service/{service_id}/domain | List the domains within a service
[**list_services**](ServiceApi.md#list_services) | **GET** /service | List services
[**search_service**](ServiceApi.md#search_service) | **GET** /service/search | Search for a service by name
[**update_service**](ServiceApi.md#update_service) | **PUT** /service/{service_id} | Update a service


# **create_service**
> ServiceResponse create_service()

Create a service

Create a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
from fastly.model.service_response import ServiceResponse
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
    api_instance = service_api.ServiceApi(api_client)
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "test-service" # str | The name of the service. (optional)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer. (optional)
    type = "vcl" # str | The type of this service. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a service
        api_response = api_instance.create_service(comment=comment, name=name, customer_id=customer_id, type=type)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->create_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| The name of the service. | [optional]
 **customer_id** | **str**| Alphanumeric string identifying the customer. | [optional]
 **type** | **str**| The type of this service. | [optional]

### Return type

[**ServiceResponse**](ServiceResponse.md)

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

# **delete_service**
> InlineResponse200 delete_service(service_id)

Delete a service

Delete a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
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
    api_instance = service_api.ServiceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Delete a service
        api_response = api_instance.delete_service(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->delete_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

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

# **get_service**
> ServiceResponse get_service(service_id)

Get a service

Get a specific service by id.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
from fastly.model.service_response import ServiceResponse
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
    api_instance = service_api.ServiceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # Get a service
        api_response = api_instance.get_service(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->get_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**ServiceResponse**](ServiceResponse.md)

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

# **get_service_detail**
> ServiceDetail get_service_detail(service_id)

Get service details

List detailed information on a specified service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
from fastly.model.number_version import NumberVersion
from fastly.model.service_detail import ServiceDetail
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
    api_instance = service_api.ServiceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version = NumberVersion(1) # NumberVersion | Number identifying a version of the service. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get service details
        api_response = api_instance.get_service_detail(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->get_service_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get service details
        api_response = api_instance.get_service_detail(service_id, version=version)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->get_service_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version** | **NumberVersion**| Number identifying a version of the service. | [optional]

### Return type

[**ServiceDetail**](ServiceDetail.md)

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

# **list_service_domains**
> [DomainResponse] list_service_domains(service_id)

List the domains within a service

List the domains within a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
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
    api_instance = service_api.ServiceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.

    # example passing only required values which don't have defaults set
    try:
        # List the domains within a service
        api_response = api_instance.list_service_domains(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->list_service_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |

### Return type

[**[DomainResponse]**](DomainResponse.md)

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

# **list_services**
> [ServiceListResponse] list_services()

List services

List services.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
from fastly.model.service_list_response import ServiceListResponse
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
    api_instance = service_api.ServiceApi(api_client)
    page = 1 # int | Current page. (optional)
    per_page = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    sort = "created" # str | Field on which to sort. (optional) if omitted the server will use the default value of "created"
    direction = "ascend" # str | Direction in which to sort results. (optional) if omitted the server will use the default value of "ascend"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List services
        api_response = api_instance.list_services(page=page, per_page=per_page, sort=sort, direction=direction)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->list_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Current page. | [optional]
 **per_page** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Field on which to sort. | [optional] if omitted the server will use the default value of "created"
 **direction** | **str**| Direction in which to sort results. | [optional] if omitted the server will use the default value of "ascend"

### Return type

[**[ServiceListResponse]**](ServiceListResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Link - Contains URLs for fetching additional paginated results. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_service**
> ServiceResponse search_service(name)

Search for a service by name

Get a specific service by name.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
from fastly.model.service_response import ServiceResponse
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
    api_instance = service_api.ServiceApi(api_client)
    name = "test-service" # str | The name of the service.

    # example passing only required values which don't have defaults set
    try:
        # Search for a service by name
        api_response = api_instance.search_service(name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->search_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the service. |

### Return type

[**ServiceResponse**](ServiceResponse.md)

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

# **update_service**
> ServiceResponse update_service(service_id)

Update a service

Update a service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_api
from fastly.model.service_response import ServiceResponse
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
    api_instance = service_api.ServiceApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    comment = "" # str, none_type | A freeform descriptive note. (optional)
    name = "test-service" # str | The name of the service. (optional)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a service
        api_response = api_instance.update_service(service_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a service
        api_response = api_instance.update_service(service_id, comment=comment, name=name, customer_id=customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceApi->update_service: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **comment** | **str, none_type**| A freeform descriptive note. | [optional]
 **name** | **str**| The name of the service. | [optional]
 **customer_id** | **str**| Alphanumeric string identifying the customer. | [optional]

### Return type

[**ServiceResponse**](ServiceResponse.md)

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

