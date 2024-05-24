# fastly.ApexRedirectApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_apex_redirect**](ApexRedirectApi.md#create_apex_redirect) | **POST** /service/{service_id}/version/{version_id}/apex-redirects | Create an apex redirect
[**delete_apex_redirect**](ApexRedirectApi.md#delete_apex_redirect) | **DELETE** /apex-redirects/{apex_redirect_id} | Delete an apex redirect
[**get_apex_redirect**](ApexRedirectApi.md#get_apex_redirect) | **GET** /apex-redirects/{apex_redirect_id} | Get an apex redirect
[**list_apex_redirects**](ApexRedirectApi.md#list_apex_redirects) | **GET** /service/{service_id}/version/{version_id}/apex-redirects | List apex redirects
[**update_apex_redirect**](ApexRedirectApi.md#update_apex_redirect) | **PUT** /apex-redirects/{apex_redirect_id} | Update an apex redirect


# **create_apex_redirect**
> ApexRedirect create_apex_redirect(service_id, version_id)

Create an apex redirect

Create an apex redirect for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apex_redirect_api
from fastly.model.apex_redirect import ApexRedirect
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
    api_instance = apex_redirect_api.ApexRedirectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.
    service_id2 = "service_id_example" # str |  (optional)
    version = 1 # int |  (optional)
    created_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    deleted_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    updated_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    status_code = 301 # int | HTTP status code used to redirect the client. (optional)
    domains = [
        "domains_example",
    ] # [str] | Array of apex domains that should redirect to their WWW subdomain. (optional)
    feature_revision = 1 # int | Revision number of the apex redirect feature implementation. Defaults to the most recent revision. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an apex redirect
        api_response = api_instance.create_apex_redirect(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->create_apex_redirect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an apex redirect
        api_response = api_instance.create_apex_redirect(service_id, version_id, service_id2=service_id2, version=version, created_at=created_at, deleted_at=deleted_at, updated_at=updated_at, status_code=status_code, domains=domains, feature_revision=feature_revision)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->create_apex_redirect: %s\n" % e)
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
 **status_code** | **int**| HTTP status code used to redirect the client. | [optional]
 **domains** | **[str]**| Array of apex domains that should redirect to their WWW subdomain. | [optional]
 **feature_revision** | **int**| Revision number of the apex redirect feature implementation. Defaults to the most recent revision. | [optional]

### Return type

[**ApexRedirect**](ApexRedirect.md)

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

# **delete_apex_redirect**
> InlineResponse200 delete_apex_redirect(apex_redirect_id)

Delete an apex redirect

Delete an apex redirect by its ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apex_redirect_api
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
    api_instance = apex_redirect_api.ApexRedirectApi(api_client)
    apex_redirect_id = "6QI9o6ZZrSP3y9gI0OhMwZ" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an apex redirect
        api_response = api_instance.delete_apex_redirect(apex_redirect_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->delete_apex_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apex_redirect_id** | **str**|  |

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

# **get_apex_redirect**
> ApexRedirect get_apex_redirect(apex_redirect_id)

Get an apex redirect

Get an apex redirect by its ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apex_redirect_api
from fastly.model.apex_redirect import ApexRedirect
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
    api_instance = apex_redirect_api.ApexRedirectApi(api_client)
    apex_redirect_id = "6QI9o6ZZrSP3y9gI0OhMwZ" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an apex redirect
        api_response = api_instance.get_apex_redirect(apex_redirect_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->get_apex_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apex_redirect_id** | **str**|  |

### Return type

[**ApexRedirect**](ApexRedirect.md)

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

# **list_apex_redirects**
> [ApexRedirect] list_apex_redirects(service_id, version_id)

List apex redirects

List all apex redirects for a particular service and version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apex_redirect_api
from fastly.model.apex_redirect import ApexRedirect
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
    api_instance = apex_redirect_api.ApexRedirectApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    version_id = 1 # int | Integer identifying a service version.

    # example passing only required values which don't have defaults set
    try:
        # List apex redirects
        api_response = api_instance.list_apex_redirects(service_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->list_apex_redirects: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **version_id** | **int**| Integer identifying a service version. |

### Return type

[**[ApexRedirect]**](ApexRedirect.md)

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

# **update_apex_redirect**
> ApexRedirect update_apex_redirect(apex_redirect_id)

Update an apex redirect

Update an apex redirect by its ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import apex_redirect_api
from fastly.model.apex_redirect import ApexRedirect
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
    api_instance = apex_redirect_api.ApexRedirectApi(api_client)
    apex_redirect_id = "6QI9o6ZZrSP3y9gI0OhMwZ" # str | 
    service_id = "service_id_example" # str |  (optional)
    version = 1 # int |  (optional)
    created_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    deleted_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    updated_at = dateutil_parser('2020-04-09T18:14:30Z') # datetime, none_type | Date and time in ISO 8601 format. (optional)
    status_code = 301 # int | HTTP status code used to redirect the client. (optional)
    domains = [
        "domains_example",
    ] # [str] | Array of apex domains that should redirect to their WWW subdomain. (optional)
    feature_revision = 1 # int | Revision number of the apex redirect feature implementation. Defaults to the most recent revision. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an apex redirect
        api_response = api_instance.update_apex_redirect(apex_redirect_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->update_apex_redirect: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an apex redirect
        api_response = api_instance.update_apex_redirect(apex_redirect_id, service_id=service_id, version=version, created_at=created_at, deleted_at=deleted_at, updated_at=updated_at, status_code=status_code, domains=domains, feature_revision=feature_revision)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ApexRedirectApi->update_apex_redirect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **apex_redirect_id** | **str**|  |
 **service_id** | **str**|  | [optional]
 **version** | **int**|  | [optional]
 **created_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **deleted_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **updated_at** | **datetime, none_type**| Date and time in ISO 8601 format. | [optional]
 **status_code** | **int**| HTTP status code used to redirect the client. | [optional]
 **domains** | **[str]**| Array of apex domains that should redirect to their WWW subdomain. | [optional]
 **feature_revision** | **int**| Revision number of the apex redirect feature implementation. Defaults to the most recent revision. | [optional]

### Return type

[**ApexRedirect**](ApexRedirect.md)

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

