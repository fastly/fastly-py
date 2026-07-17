# fastly.ClientSideProtectionApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**csp_create_page**](ClientSideProtectionApi.md#csp_create_page) | **POST** /client-side-protection/v1/pages | Create page
[**csp_create_policy**](ClientSideProtectionApi.md#csp_create_policy) | **POST** /client-side-protection/v1/pages/{page_id}/policies | Create policy
[**csp_create_website**](ClientSideProtectionApi.md#csp_create_website) | **POST** /client-side-protection/v1/websites | Create website
[**csp_delete_page**](ClientSideProtectionApi.md#csp_delete_page) | **DELETE** /client-side-protection/v1/pages/{page_id} | Delete page
[**csp_delete_website**](ClientSideProtectionApi.md#csp_delete_website) | **DELETE** /client-side-protection/v1/websites/{website_id} | Delete website
[**csp_get_page**](ClientSideProtectionApi.md#csp_get_page) | **GET** /client-side-protection/v1/pages/{page_id} | Get page
[**csp_get_policy**](ClientSideProtectionApi.md#csp_get_policy) | **GET** /client-side-protection/v1/pages/{page_id}/policies/{policy_id} | Get policy
[**csp_get_script**](ClientSideProtectionApi.md#csp_get_script) | **GET** /client-side-protection/v1/pages/{page_id}/scripts/{script_id} | Get script
[**csp_get_website**](ClientSideProtectionApi.md#csp_get_website) | **GET** /client-side-protection/v1/websites/{website_id} | Get website
[**csp_list_header_events**](ClientSideProtectionApi.md#csp_list_header_events) | **GET** /client-side-protection/v1/pages/{page_id}/events | List header events
[**csp_list_headers**](ClientSideProtectionApi.md#csp_list_headers) | **GET** /client-side-protection/v1/pages/{page_id}/headers | List security headers
[**csp_list_pages**](ClientSideProtectionApi.md#csp_list_pages) | **GET** /client-side-protection/v1/pages | List pages
[**csp_list_policies**](ClientSideProtectionApi.md#csp_list_policies) | **GET** /client-side-protection/v1/pages/{page_id}/policies | List policies
[**csp_list_policy_reports**](ClientSideProtectionApi.md#csp_list_policy_reports) | **GET** /client-side-protection/v1/pages/{page_id}/policies/{policy_id}/reports | List policy reports
[**csp_list_scripts**](ClientSideProtectionApi.md#csp_list_scripts) | **GET** /client-side-protection/v1/pages/{page_id}/scripts | List scripts
[**csp_list_websites**](ClientSideProtectionApi.md#csp_list_websites) | **GET** /client-side-protection/v1/websites | List websites
[**csp_update_page**](ClientSideProtectionApi.md#csp_update_page) | **PATCH** /client-side-protection/v1/pages/{page_id} | Update page
[**csp_update_policy**](ClientSideProtectionApi.md#csp_update_policy) | **PATCH** /client-side-protection/v1/pages/{page_id}/policies/{policy_id} | Update policy
[**csp_update_script**](ClientSideProtectionApi.md#csp_update_script) | **PATCH** /client-side-protection/v1/pages/{page_id}/scripts/{script_id} | Update script
[**csp_update_website**](ClientSideProtectionApi.md#csp_update_website) | **PATCH** /client-side-protection/v1/websites/{website_id} | Update website


# **csp_create_page**
> Page csp_create_page()

Create page

Create a new page for monitoring.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.page import Page
from fastly.model.page_create import PageCreate
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_create = PageCreate(
        website_id="website_id_example",
        name="name_example",
        description="description_example",
        notifications=[
            Notification(
                type="mailinglist",
                config=NotificationConfig(
                    address="address_example",
                ),
            ),
        ],
        paths=[
            "paths_example",
        ],
    ) # PageCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create page
        api_response = api_instance.csp_create_page(page_create=page_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_create_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_create** | [**PageCreate**](PageCreate.md)|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Page created |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_create_policy**
> Policy csp_create_policy(page_id)

Create policy

Create a new Content Security Policy for a page.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.policy_create import PolicyCreate
from fastly.model.policy import Policy
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    policy_create = PolicyCreate(
        name="name_example",
        description="description_example",
        mode="report",
        directives=[
            Directive(
                name="name_example",
                values=[
                    "values_example",
                ],
            ),
        ],
    ) # PolicyCreate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create policy
        api_response = api_instance.csp_create_policy(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_create_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create policy
        api_response = api_instance.csp_create_policy(page_id, policy_create=policy_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_create_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **policy_create** | [**PolicyCreate**](PolicyCreate.md)|  | [optional]

### Return type

[**Policy**](Policy.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Policy created |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_create_website**
> Website csp_create_website()

Create website

Create a new website for Client-Side Protection monitoring.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.website import Website
from fastly.model.website_create import WebsiteCreate
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    website_create = WebsiteCreate(
        domain="domain_example",
    ) # WebsiteCreate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create website
        api_response = api_instance.csp_create_website(website_create=website_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_create_website: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_create** | [**WebsiteCreate**](WebsiteCreate.md)|  | [optional]

### Return type

[**Website**](Website.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Website created |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_delete_page**
> csp_delete_page(page_id)

Delete page

Delete a page and all associated scripts and policies.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete page
        api_instance.csp_delete_page(page_id)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_delete_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Page deleted successfully |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_delete_website**
> csp_delete_website(website_id)

Delete website

Delete a website and all associated pages, scripts, and policies.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    website_id = "2Xk9JgPCkf1NzVsNmKrECp" # str | Website identifier

    # example passing only required values which don't have defaults set
    try:
        # Delete website
        api_instance.csp_delete_website(website_id)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_delete_website: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website identifier |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Website deleted successfully |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_get_page**
> Page csp_get_page(page_id)

Get page

Get details for a specific page.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.page import Page
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier

    # example passing only required values which don't have defaults set
    try:
        # Get page
        api_response = api_instance.csp_get_page(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_get_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |

### Return type

[**Page**](Page.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page details |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_get_policy**
> Policy csp_get_policy(page_id, policy_id)

Get policy

Get details for a specific policy.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.policy import Policy
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    policy_id = "7Cp4OlUHqj6SfAwSrQwJHu" # str | Policy identifier

    # example passing only required values which don't have defaults set
    try:
        # Get policy
        api_response = api_instance.csp_get_policy(page_id, policy_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_get_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **policy_id** | **str**| Policy identifier |

### Return type

[**Policy**](Policy.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy details |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_get_script**
> Script csp_get_script(page_id, script_id)

Get script

Get details for a specific script.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.script import Script
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    script_id = "5An2MjSFoh4QcYvQpNuHFs" # str | Script identifier

    # example passing only required values which don't have defaults set
    try:
        # Get script
        api_response = api_instance.csp_get_script(page_id, script_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_get_script: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **script_id** | **str**| Script identifier |

### Return type

[**Script**](Script.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Script details |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_get_website**
> Website csp_get_website(website_id)

Get website

Get details for a specific website.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.website import Website
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    website_id = "2Xk9JgPCkf1NzVsNmKrECp" # str | Website identifier

    # example passing only required values which don't have defaults set
    try:
        # Get website
        api_response = api_instance.csp_get_website(website_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_get_website: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website identifier |

### Return type

[**Website**](Website.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website details |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_header_events**
> InlineResponse20011 csp_list_header_events(page_id)

List header events

List security header change events for a page.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.inline_response20011 import InlineResponse20011
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List header events
        api_response = api_instance.csp_list_header_events(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_header_events: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List header events
        api_response = api_instance.csp_list_header_events(page_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_header_events: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse20011**](InlineResponse20011.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of header change events |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_headers**
> InlineResponse20010 csp_list_headers(page_id)

List security headers

List security headers detected on a page.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.inline_response20010 import InlineResponse20010
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List security headers
        api_response = api_instance.csp_list_headers(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_headers: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List security headers
        api_response = api_instance.csp_list_headers(page_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_headers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of security headers |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_pages**
> InlineResponse2006 csp_list_pages()

List pages

List all pages. Optionally filter by website.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.inline_response2006 import InlineResponse2006
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    website_id = "website_id_example" # str | Filter pages by website ID (optional)
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List pages
        api_response = api_instance.csp_list_pages(website_id=website_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_pages: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Filter pages by website ID | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of pages |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_policies**
> InlineResponse2008 csp_list_policies(page_id)

List policies

List all Content Security Policies for a page.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.inline_response2008 import InlineResponse2008
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List policies
        api_response = api_instance.csp_list_policies(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_policies: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List policies
        api_response = api_instance.csp_list_policies(page_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_policies: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of policies |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_policy_reports**
> InlineResponse2009 csp_list_policy_reports(page_id, policy_id)

List policy reports

List CSP violation reports for a policy.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.inline_response2009 import InlineResponse2009
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    policy_id = "7Cp4OlUHqj6SfAwSrQwJHu" # str | Policy identifier
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List policy reports
        api_response = api_instance.csp_list_policy_reports(page_id, policy_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_policy_reports: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List policy reports
        api_response = api_instance.csp_list_policy_reports(page_id, policy_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_policy_reports: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **policy_id** | **str**| Policy identifier |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2009**](InlineResponse2009.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of CSP violation reports |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_scripts**
> InlineResponse2007 csp_list_scripts(page_id)

List scripts

List all scripts detected on a page.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    try:
        # List scripts
        api_response = api_instance.csp_list_scripts(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_scripts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List scripts
        api_response = api_instance.csp_list_scripts(page_id, limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_scripts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2007**](InlineResponse2007.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of scripts |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_list_websites**
> InlineResponse2005 csp_list_websites()

List websites

List all websites configured for Client-Side Protection.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.inline_response2005 import InlineResponse2005
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    page = 1 # int | Page number of the collection to request. (optional) if omitted the server will use the default value of 0

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List websites
        api_response = api_instance.csp_list_websites(limit=limit, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_list_websites: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **page** | **int**| Page number of the collection to request. | [optional] if omitted the server will use the default value of 0

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of websites |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_update_page**
> Page csp_update_page(page_id)

Update page

Update a page's configuration.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.page import Page
from fastly.model.page_update import PageUpdate
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    page_update = PageUpdate(
        website_id="website_id_example",
        name="name_example",
        description="description_example",
        notifications=[
            Notification(
                type="mailinglist",
                config=NotificationConfig(
                    address="address_example",
                ),
            ),
        ],
        paths=[
            "paths_example",
        ],
    ) # PageUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update page
        api_response = api_instance.csp_update_page(page_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_page: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update page
        api_response = api_instance.csp_update_page(page_id, page_update=page_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_page: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **page_update** | [**PageUpdate**](PageUpdate.md)|  | [optional]

### Return type

[**Page**](Page.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Page details |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_update_policy**
> Policy csp_update_policy(page_id, policy_id)

Update policy

Update a policy's configuration.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.policy_update import PolicyUpdate
from fastly.model.policy import Policy
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    policy_id = "7Cp4OlUHqj6SfAwSrQwJHu" # str | Policy identifier
    policy_update = PolicyUpdate(
        name="name_example",
        description="description_example",
        mode="report",
        directives=[
            Directive(
                name="name_example",
                values=[
                    "values_example",
                ],
            ),
        ],
    ) # PolicyUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update policy
        api_response = api_instance.csp_update_policy(page_id, policy_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_policy: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update policy
        api_response = api_instance.csp_update_policy(page_id, policy_id, policy_update=policy_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_policy: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **policy_id** | **str**| Policy identifier |
 **policy_update** | [**PolicyUpdate**](PolicyUpdate.md)|  | [optional]

### Return type

[**Policy**](Policy.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Policy details |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_update_script**
> Script csp_update_script(page_id, script_id)

Update script

Update a script's authorization status or justification.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.script_update import ScriptUpdate
from fastly.model.script import Script
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    page_id = "3Yl0KhQDlg2OaWtOnLsFDq" # str | Page identifier
    script_id = "5An2MjSFoh4QcYvQpNuHFs" # str | Script identifier
    script_update = ScriptUpdate(
        authorization_status="authorized",
        justification="justification_example",
        authorized_hash="authorized_hash_example",
    ) # ScriptUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update script
        api_response = api_instance.csp_update_script(page_id, script_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_script: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update script
        api_response = api_instance.csp_update_script(page_id, script_id, script_update=script_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_script: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_id** | **str**| Page identifier |
 **script_id** | **str**| Script identifier |
 **script_update** | [**ScriptUpdate**](ScriptUpdate.md)|  | [optional]

### Return type

[**Script**](Script.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Script details |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **csp_update_website**
> Website csp_update_website(website_id)

Update website

Update a website's configuration.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import client_side_protection_api
from fastly.model.website import Website
from fastly.model.website_update import WebsiteUpdate
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
    api_instance = client_side_protection_api.ClientSideProtectionApi(api_client)
    website_id = "2Xk9JgPCkf1NzVsNmKrECp" # str | Website identifier
    website_update = WebsiteUpdate(
        domain="domain_example",
    ) # WebsiteUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update website
        api_response = api_instance.csp_update_website(website_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_website: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update website
        api_response = api_instance.csp_update_website(website_id, website_update=website_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ClientSideProtectionApi->csp_update_website: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **website_id** | **str**| Website identifier |
 **website_update** | [**WebsiteUpdate**](WebsiteUpdate.md)|  | [optional]

### Return type

[**Website**](Website.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Website details |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

