# fastly.IamServiceGroupsApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_a_service_group**](IamServiceGroupsApi.md#delete_a_service_group) | **DELETE** /service-groups/{service_group_id} | Delete a service group
[**get_a_service_group**](IamServiceGroupsApi.md#get_a_service_group) | **GET** /service-groups/{service_group_id} | Get a service group
[**list_service_group_services**](IamServiceGroupsApi.md#list_service_group_services) | **GET** /service-groups/{service_group_id}/services | List services to a service group
[**list_service_groups**](IamServiceGroupsApi.md#list_service_groups) | **GET** /service-groups | List service groups


# **delete_a_service_group**
> delete_a_service_group(service_group_id)

Delete a service group

Delete a service group.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_service_groups_api
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
    api_instance = iam_service_groups_api.IamServiceGroupsApi(api_client)
    service_group_id = "t4Gg2uUGZzb2W9Euo4mo0R" # str | Alphanumeric string identifying the service group.

    # example passing only required values which don't have defaults set
    try:
        # Delete a service group
        api_instance.delete_a_service_group(service_group_id)
    except fastly.ApiException as e:
        print("Exception when calling IamServiceGroupsApi->delete_a_service_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_group_id** | **str**| Alphanumeric string identifying the service group. |

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

# **get_a_service_group**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_a_service_group(service_group_id)

Get a service group

Get a service group.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_service_groups_api
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
    api_instance = iam_service_groups_api.IamServiceGroupsApi(api_client)
    service_group_id = "t4Gg2uUGZzb2W9Euo4mo0R" # str | Alphanumeric string identifying the service group.

    # example passing only required values which don't have defaults set
    try:
        # Get a service group
        api_response = api_instance.get_a_service_group(service_group_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamServiceGroupsApi->get_a_service_group: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_group_id** | **str**| Alphanumeric string identifying the service group. |

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

# **list_service_group_services**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_service_group_services(service_group_id)

List services to a service group

List services to a service group.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_service_groups_api
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
    api_instance = iam_service_groups_api.IamServiceGroupsApi(api_client)
    service_group_id = "t4Gg2uUGZzb2W9Euo4mo0R" # str | Alphanumeric string identifying the service group.
    per_page = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    page = 1 # int | Current page. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List services to a service group
        api_response = api_instance.list_service_group_services(service_group_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamServiceGroupsApi->list_service_group_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List services to a service group
        api_response = api_instance.list_service_group_services(service_group_id, per_page=per_page, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamServiceGroupsApi->list_service_group_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_group_id** | **str**| Alphanumeric string identifying the service group. |
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

# **list_service_groups**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_service_groups()

List service groups

List all service groups.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import iam_service_groups_api
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
    api_instance = iam_service_groups_api.IamServiceGroupsApi(api_client)
    per_page = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    page = 1 # int | Current page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List service groups
        api_response = api_instance.list_service_groups(per_page=per_page, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling IamServiceGroupsApi->list_service_groups: %s\n" % e)
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

