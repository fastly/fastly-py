# fastly.IamRolesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**iam_v1_roles_get**](IamRolesApi.md#iam_v1_roles_get) | **GET** /iam/v1/roles/{role_id} | Get IAM role by ID
[**iam_v1_roles_list**](IamRolesApi.md#iam_v1_roles_list) | **GET** /iam/v1/roles | List IAM roles


# **iam_v1_roles_get**
> IamV1RoleResponse iam_v1_roles_get(role_id)

Get IAM role by ID

Retrieve a single IAM role by its unique identifier. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_roles_api
from fastly.model.iam_v1_role_response import IamV1RoleResponse
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
    role_id = "Q4rXe9vN1szK8a2fUjYtWp" # str | Alphanumeric string identifying the role.
    include = "permissions" # str | Include related data (i.e., permissions). (optional) if omitted the server will use the default value of "permissions"

    # example passing only required values which don't have defaults set
    try:
        # Get IAM role by ID
        api_response = api_instance.iam_v1_roles_get(role_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->iam_v1_roles_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get IAM role by ID
        api_response = api_instance.iam_v1_roles_get(role_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->iam_v1_roles_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Alphanumeric string identifying the role. |
 **include** | **str**| Include related data (i.e., permissions). | [optional] if omitted the server will use the default value of "permissions"

### Return type

[**IamV1RoleResponse**](IamV1RoleResponse.md)

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

# **iam_v1_roles_list**
> IamV1RoleListResponse iam_v1_roles_list()

List IAM roles

Retrieve a paginated list of IAM roles available in the account. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_roles_api
from fastly.model.iam_v1_role_list_response import IamV1RoleListResponse
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
    limit = 100 # int | Number of results per page. The maximum is 1000. (optional) if omitted the server will use the default value of 100
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List IAM roles
        api_response = api_instance.iam_v1_roles_list(limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamRolesApi->iam_v1_roles_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Number of results per page. The maximum is 1000. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]

### Return type

[**IamV1RoleListResponse**](IamV1RoleListResponse.md)

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

