# fastly.DmDomainsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dm_domain**](DmDomainsApi.md#create_dm_domain) | **POST** /domain-management/v1/domains | Create a domain
[**delete_dm_domain**](DmDomainsApi.md#delete_dm_domain) | **DELETE** /domain-management/v1/domains/{domain_id} | Delete a domain
[**get_dm_domain**](DmDomainsApi.md#get_dm_domain) | **GET** /domain-management/v1/domains/{domain_id} | Get a domain
[**list_dm_domains**](DmDomainsApi.md#list_dm_domains) | **GET** /domain-management/v1/domains | List domains
[**update_dm_domain**](DmDomainsApi.md#update_dm_domain) | **PATCH** /domain-management/v1/domains/{domain_id} | Update a domain


# **create_dm_domain**
> SuccessfulResponseAsObject create_dm_domain()

Create a domain

Create a domain

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_domains_api
from fastly.model.request_body_for_create import RequestBodyForCreate
from fastly.model.successful_response_as_object import SuccessfulResponseAsObject
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
    api_instance = dm_domains_api.DmDomainsApi(api_client)
    request_body_for_create = RequestBodyForCreate(
        fqdn="fqdn_example",
        service_id="service_id_example",
        description="description_example",
    ) # RequestBodyForCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a domain
        api_response = api_instance.create_dm_domain(request_body_for_create=request_body_for_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmDomainsApi->create_dm_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body_for_create** | [**RequestBodyForCreate**](RequestBodyForCreate.md)|  | [optional]

### Return type

[**SuccessfulResponseAsObject**](SuccessfulResponseAsObject.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A domain. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dm_domain**
> delete_dm_domain(domain_id)

Delete a domain

Delete a domain

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_domains_api
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
    api_instance = dm_domains_api.DmDomainsApi(api_client)
    domain_id = "domain_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a domain
        api_instance.delete_dm_domain(domain_id)
    except fastly.ApiException as e:
        print("Exception when calling DmDomainsApi->delete_dm_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dm_domain**
> SuccessfulResponseAsObject get_dm_domain(domain_id)

Get a domain

Show a domain

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_domains_api
from fastly.model.successful_response_as_object import SuccessfulResponseAsObject
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
    api_instance = dm_domains_api.DmDomainsApi(api_client)
    domain_id = "domain_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a domain
        api_response = api_instance.get_dm_domain(domain_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmDomainsApi->get_dm_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  |

### Return type

[**SuccessfulResponseAsObject**](SuccessfulResponseAsObject.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A domain. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dm_domains**
> InlineResponse2004 list_dm_domains()

List domains

List all domains

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_domains_api
from fastly.model.inline_response2004 import InlineResponse2004
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
    api_instance = dm_domains_api.DmDomainsApi(api_client)
    fqdn = "fqdn_example" # str |  (optional)
    service_id = "service_id_example" # str | Filter results based on a service_id. (optional)
    sort = "fqdn" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "fqdn"
    activated = True # bool |  (optional)
    verified = True # bool |  (optional)
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List domains
        api_response = api_instance.list_dm_domains(fqdn=fqdn, service_id=service_id, sort=sort, activated=activated, verified=verified, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmDomainsApi->list_dm_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fqdn** | **str**|  | [optional]
 **service_id** | **str**| Filter results based on a service_id. | [optional]
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "fqdn"
 **activated** | **bool**|  | [optional]
 **verified** | **bool**|  | [optional]
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of domains. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dm_domain**
> SuccessfulResponseAsObject update_dm_domain(domain_id)

Update a domain

Update a domain

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_domains_api
from fastly.model.request_body_for_update import RequestBodyForUpdate
from fastly.model.successful_response_as_object import SuccessfulResponseAsObject
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
    api_instance = dm_domains_api.DmDomainsApi(api_client)
    domain_id = "domain_id_example" # str | 
    request_body_for_update = RequestBodyForUpdate(
        service_id="service_id_example",
        description="description_example",
    ) # RequestBodyForUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a domain
        api_response = api_instance.update_dm_domain(domain_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmDomainsApi->update_dm_domain: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a domain
        api_response = api_instance.update_dm_domain(domain_id, request_body_for_update=request_body_for_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmDomainsApi->update_dm_domain: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **domain_id** | **str**|  |
 **request_body_for_update** | [**RequestBodyForUpdate**](RequestBodyForUpdate.md)|  | [optional]

### Return type

[**SuccessfulResponseAsObject**](SuccessfulResponseAsObject.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A domain. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

