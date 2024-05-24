# fastly.ServiceAuthorizationsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_service_authorization**](ServiceAuthorizationsApi.md#create_service_authorization) | **POST** /service-authorizations | Create service authorization
[**delete_service_authorization**](ServiceAuthorizationsApi.md#delete_service_authorization) | **DELETE** /service-authorizations/{service_authorization_id} | Delete service authorization
[**delete_service_authorization2**](ServiceAuthorizationsApi.md#delete_service_authorization2) | **DELETE** /service-authorizations | Delete service authorizations
[**list_service_authorization**](ServiceAuthorizationsApi.md#list_service_authorization) | **GET** /service-authorizations | List service authorizations
[**show_service_authorization**](ServiceAuthorizationsApi.md#show_service_authorization) | **GET** /service-authorizations/{service_authorization_id} | Show service authorization
[**update_service_authorization**](ServiceAuthorizationsApi.md#update_service_authorization) | **PATCH** /service-authorizations/{service_authorization_id} | Update service authorization
[**update_service_authorization2**](ServiceAuthorizationsApi.md#update_service_authorization2) | **PATCH** /service-authorizations | Update service authorizations


# **create_service_authorization**
> ServiceAuthorizationResponse create_service_authorization()

Create service authorization

Create service authorization.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
from fastly.model.service_authorization import ServiceAuthorization
from fastly.model.service_authorization_response import ServiceAuthorizationResponse
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    service_authorization = ServiceAuthorization(
        data=ServiceAuthorizationData(
            type=TypeServiceAuthorization("service_authorization"),
            attributes=ServiceAuthorizationDataAttributes(
                permission=Permission("full"),
            ),
            relationships=ServiceAuthorizationDataRelationships(
                service=RelationshipMemberService(
                    type=TypeService("service"),
                ),
                user=ServiceAuthorizationDataRelationshipsUser(
                    data=ServiceAuthorizationDataRelationshipsUserData(
                        type=TypeUser("user"),
                    ),
                ),
            ),
        ),
    ) # ServiceAuthorization |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create service authorization
        api_response = api_instance.create_service_authorization(service_authorization=service_authorization)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->create_service_authorization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_authorization** | [**ServiceAuthorization**](ServiceAuthorization.md)|  | [optional]

### Return type

[**ServiceAuthorizationResponse**](ServiceAuthorizationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_authorization**
> delete_service_authorization(service_authorization_id)

Delete service authorization

Delete service authorization.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    service_authorization_id = "3krg2uUGZzb2W9Euo4moOY" # str | Alphanumeric string identifying a service authorization.

    # example passing only required values which don't have defaults set
    try:
        # Delete service authorization
        api_instance.delete_service_authorization(service_authorization_id)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->delete_service_authorization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_authorization_id** | **str**| Alphanumeric string identifying a service authorization. |

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
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_service_authorization2**
> InlineResponse2007 delete_service_authorization2()

Delete service authorizations

Delete service authorizations.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
from fastly.model.inline_response2007 import InlineResponse2007
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete service authorizations
        api_response = api_instance.delete_service_authorization2(request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->delete_service_authorization2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json; ext=bulk
 - **Accept**: application/vnd.api+json; ext=bulk


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_authorization**
> ServiceAuthorizationsResponse list_service_authorization()

List service authorizations

List service authorizations.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
from fastly.model.service_authorizations_response import ServiceAuthorizationsResponse
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List service authorizations
        api_response = api_instance.list_service_authorization(page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->list_service_authorization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**ServiceAuthorizationsResponse**](ServiceAuthorizationsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **show_service_authorization**
> ServiceAuthorizationResponse show_service_authorization(service_authorization_id)

Show service authorization

Show service authorization.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
from fastly.model.service_authorization_response import ServiceAuthorizationResponse
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    service_authorization_id = "3krg2uUGZzb2W9Euo4moOY" # str | Alphanumeric string identifying a service authorization.

    # example passing only required values which don't have defaults set
    try:
        # Show service authorization
        api_response = api_instance.show_service_authorization(service_authorization_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->show_service_authorization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_authorization_id** | **str**| Alphanumeric string identifying a service authorization. |

### Return type

[**ServiceAuthorizationResponse**](ServiceAuthorizationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_authorization**
> ServiceAuthorizationResponse update_service_authorization(service_authorization_id)

Update service authorization

Update service authorization.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
from fastly.model.service_authorization import ServiceAuthorization
from fastly.model.service_authorization_response import ServiceAuthorizationResponse
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    service_authorization_id = "3krg2uUGZzb2W9Euo4moOY" # str | Alphanumeric string identifying a service authorization.
    service_authorization = ServiceAuthorization(
        data=ServiceAuthorizationData(
            type=TypeServiceAuthorization("service_authorization"),
            attributes=ServiceAuthorizationDataAttributes(
                permission=Permission("full"),
            ),
            relationships=ServiceAuthorizationDataRelationships(
                service=RelationshipMemberService(
                    type=TypeService("service"),
                ),
                user=ServiceAuthorizationDataRelationshipsUser(
                    data=ServiceAuthorizationDataRelationshipsUserData(
                        type=TypeUser("user"),
                    ),
                ),
            ),
        ),
    ) # ServiceAuthorization |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update service authorization
        api_response = api_instance.update_service_authorization(service_authorization_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->update_service_authorization: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update service authorization
        api_response = api_instance.update_service_authorization(service_authorization_id, service_authorization=service_authorization)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->update_service_authorization: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_authorization_id** | **str**| Alphanumeric string identifying a service authorization. |
 **service_authorization** | [**ServiceAuthorization**](ServiceAuthorization.md)|  | [optional]

### Return type

[**ServiceAuthorizationResponse**](ServiceAuthorizationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_service_authorization2**
> ServiceAuthorizationsResponse update_service_authorization2()

Update service authorizations

Update service authorizations.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import service_authorizations_api
from fastly.model.service_authorizations_response import ServiceAuthorizationsResponse
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
    api_instance = service_authorizations_api.ServiceAuthorizationsApi(api_client)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update service authorizations
        api_response = api_instance.update_service_authorization2(request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ServiceAuthorizationsApi->update_service_authorization2: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

[**ServiceAuthorizationsResponse**](ServiceAuthorizationsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json; ext=bulk
 - **Accept**: application/vnd.api+json; ext=bulk


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

