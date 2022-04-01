# fastly.IamRolesApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_a_role**](IamRolesApi.md#delete_a_role) | **DELETE** /roles/{role_id} | Delete a role
[**get_a_role**](IamRolesApi.md#get_a_role) | **GET** /roles/{role_id} | Get a role
[**list_role_permissions**](IamRolesApi.md#list_role_permissions) | **GET** /roles/{role_id}/permissions | List permissions in a role
[**list_roles**](IamRolesApi.md#list_roles) | **GET** /roles | List roles


# **delete_a_role**
> delete_a_role(role_id)

Delete a role

Delete a role.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_roles_api
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
    api_instance = iam_roles_api.IamRolesApi(api_client)
    role_id = "t4Gg2uUGZzb2W9Euo4mo0R" # str | Alphanumeric string identifying the role.

    # example passing only required values which don't have defaults set
    try:
        # Delete a role
        api_instance.delete_a_role(role_id)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->delete_a_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Alphanumeric string identifying the role. |

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

# **get_a_role**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_a_role(role_id)

Get a role

Get a role.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_roles_api
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
    api_instance = iam_roles_api.IamRolesApi(api_client)
    role_id = "t4Gg2uUGZzb2W9Euo4mo0R" # str | Alphanumeric string identifying the role.

    # example passing only required values which don't have defaults set
    try:
        # Get a role
        api_response = api_instance.get_a_role(role_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->get_a_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Alphanumeric string identifying the role. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **list_role_permissions**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_role_permissions(role_id)

List permissions in a role

List all permissions in a role.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_roles_api
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
    api_instance = iam_roles_api.IamRolesApi(api_client)
    role_id = "t4Gg2uUGZzb2W9Euo4mo0R" # str | Alphanumeric string identifying the role.

    # example passing only required values which don't have defaults set
    try:
        # List permissions in a role
        api_response = api_instance.list_role_permissions(role_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->list_role_permissions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Alphanumeric string identifying the role. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **list_roles**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_roles()

List roles

List all roles.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_roles_api
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
    api_instance = iam_roles_api.IamRolesApi(api_client)
    per_page = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    page = 1 # int | Current page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List roles
        api_response = api_instance.list_roles(per_page=per_page, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->list_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **page** | **int**| Current page. | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

