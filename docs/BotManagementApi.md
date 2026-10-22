# fastly.BotManagementApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bot_management_get_bot**](BotManagementApi.md#bot_management_get_bot) | **GET** /bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}/bots/{bot_id} | Get a bot
[**bot_management_get_category**](BotManagementApi.md#bot_management_get_category) | **GET** /bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id} | Get a category
[**bot_management_get_workspace**](BotManagementApi.md#bot_management_get_workspace) | **GET** /bot-management/v1/workspaces/{workspace_id} | Get a workspace
[**bot_management_list_bots**](BotManagementApi.md#bot_management_list_bots) | **GET** /bot-management/v1/workspaces/{workspace_id}/policy/bots | List all bots in a workspace
[**bot_management_list_categories**](BotManagementApi.md#bot_management_list_categories) | **GET** /bot-management/v1/workspaces/{workspace_id}/policy/categories | List categories
[**bot_management_list_category_bots**](BotManagementApi.md#bot_management_list_category_bots) | **GET** /bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}/bots | List bots in a category
[**bot_management_list_workspaces**](BotManagementApi.md#bot_management_list_workspaces) | **GET** /bot-management/v1/workspaces | List workspaces
[**bot_management_update_bot**](BotManagementApi.md#bot_management_update_bot) | **PATCH** /bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id}/bots/{bot_id} | Set a bot action
[**bot_management_update_category**](BotManagementApi.md#bot_management_update_category) | **PATCH** /bot-management/v1/workspaces/{workspace_id}/policy/categories/{category_id} | Set a category action
[**bot_management_update_workspace**](BotManagementApi.md#bot_management_update_workspace) | **PATCH** /bot-management/v1/workspaces/{workspace_id} | Update a workspace


# **bot_management_get_bot**
> BotManagementBotResponse bot_management_get_bot(workspace_id, category_id, bot_id)

Get a bot

Get the attributes of a bot in a category.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_bot_response import BotManagementBotResponse
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    category_id = "ai_crawlers" # str | The ID of the bot category.
    bot_id = "gptbot" # str | The ID of the bot.

    # example passing only required values which don't have defaults set
    try:
        # Get a bot
        api_response = api_instance.bot_management_get_bot(workspace_id, category_id, bot_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_get_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **category_id** | **str**| The ID of the bot category. |
 **bot_id** | **str**| The ID of the bot. |

### Return type

[**BotManagementBotResponse**](BotManagementBotResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bot. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_get_category**
> BotManagementCategoryResponse bot_management_get_category(workspace_id, category_id)

Get a category

Get the attributes of a bot category.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_category_response import BotManagementCategoryResponse
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    category_id = "ai_crawlers" # str | The ID of the bot category.

    # example passing only required values which don't have defaults set
    try:
        # Get a category
        api_response = api_instance.bot_management_get_category(workspace_id, category_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_get_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **category_id** | **str**| The ID of the bot category. |

### Return type

[**BotManagementCategoryResponse**](BotManagementCategoryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bot category. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_get_workspace**
> BotManagementWorkspaceResponse bot_management_get_workspace(workspace_id)

Get a workspace

Retrieve a bot management workspace.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_workspace_response import BotManagementWorkspaceResponse
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.

    # example passing only required values which don't have defaults set
    try:
        # Get a workspace
        api_response = api_instance.bot_management_get_workspace(workspace_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_get_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |

### Return type

[**BotManagementWorkspaceResponse**](BotManagementWorkspaceResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bot management workspace. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_list_bots**
> BotManagementWorkspaceBotsResponse bot_management_list_bots(workspace_id)

List all bots in a workspace

List all bots in a workspace's policy across all categories.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_workspace_bots_response import BotManagementWorkspaceBotsResponse
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    cursor = "MTAwOjA" # str | Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List all bots in a workspace
        api_response = api_instance.bot_management_list_bots(workspace_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_bots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List all bots in a workspace
        api_response = api_instance.bot_management_list_bots(workspace_id, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. | [optional]

### Return type

[**BotManagementWorkspaceBotsResponse**](BotManagementWorkspaceBotsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of bots in the workspace. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_list_categories**
> BotManagementCategoriesResponse bot_management_list_categories(workspace_id)

List categories

List all bot categories in a workspace's policy. Each category has an action that applies to every bot in the category. To list the bots themselves, use [list all bots in a workspace](#bot-management-list-bots) or [list bots in a category](#bot-management-list-category-bots).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_categories_response import BotManagementCategoriesResponse
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    cursor = "MTAwOjA" # str | Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List categories
        api_response = api_instance.bot_management_list_categories(workspace_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_categories: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List categories
        api_response = api_instance.bot_management_list_categories(workspace_id, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_categories: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. | [optional]

### Return type

[**BotManagementCategoriesResponse**](BotManagementCategoriesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of bot categories. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_list_category_bots**
> BotManagementBotsResponse bot_management_list_category_bots(workspace_id, category_id)

List bots in a category

List all bots in a bot category.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_bots_response import BotManagementBotsResponse
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    category_id = "ai_crawlers" # str | The ID of the bot category.
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    cursor = "MTAwOjA" # str | Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. (optional)

    # example passing only required values which don't have defaults set
    try:
        # List bots in a category
        api_response = api_instance.bot_management_list_category_bots(workspace_id, category_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_category_bots: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List bots in a category
        api_response = api_instance.bot_management_list_category_bots(workspace_id, category_id, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_category_bots: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **category_id** | **str**| The ID of the bot category. |
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. | [optional]

### Return type

[**BotManagementBotsResponse**](BotManagementBotsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of bots in the category. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_list_workspaces**
> BotManagementWorkspacesResponse bot_management_list_workspaces()

List workspaces

List bot management workspaces.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_workspaces_response import BotManagementWorkspacesResponse
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    service_id = "6oMkSHsKCMBjQJPLHgMxu1" # str | Filter results to the workspace attached to this service. Returns an empty list if the service is not attached to a workspace. (optional)
    limit = 100 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 100
    cursor = "MTAwOjA" # str | Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List workspaces
        api_response = api_instance.bot_management_list_workspaces(service_id=service_id, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_list_workspaces: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Filter results to the workspace attached to this service. Returns an empty list if the service is not attached to a workspace. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Cursor for pagination. Use the `next_cursor` value from a previous response to request the next page of results. | [optional]

### Return type

[**BotManagementWorkspacesResponse**](BotManagementWorkspacesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of bot management workspaces. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_update_bot**
> BotManagementBotResponse bot_management_update_bot(workspace_id, category_id, bot_id, bot_management_bot)

Set a bot action

Set the action for a bot. Set the action to 'inherit' to apply the category's action or to a specific value to override the category's action.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_bot_response import BotManagementBotResponse
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_bot import BotManagementBot
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    category_id = "ai_crawlers" # str | The ID of the bot category.
    bot_id = "gptbot" # str | The ID of the bot.
    bot_management_bot = BotManagementBot(
        action=BotManagementBotAction(
            type="inherit",
        ),
    ) # BotManagementBot | 

    # example passing only required values which don't have defaults set
    try:
        # Set a bot action
        api_response = api_instance.bot_management_update_bot(workspace_id, category_id, bot_id, bot_management_bot)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_update_bot: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **category_id** | **str**| The ID of the bot category. |
 **bot_id** | **str**| The ID of the bot. |
 **bot_management_bot** | [**BotManagementBot**](BotManagementBot.md)|  |

### Return type

[**BotManagementBotResponse**](BotManagementBotResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bot. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_update_category**
> BotManagementCategoryResponse bot_management_update_category(workspace_id, category_id, bot_management_category)

Set a category action

Set the action for a bot category. Every bot in the category configured with the 'inherit' action uses the action set for the category.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_category import BotManagementCategory
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_category_response import BotManagementCategoryResponse
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    category_id = "ai_crawlers" # str | The ID of the bot category.
    bot_management_category = BotManagementCategory(
        action=BotManagementAction(
            type="block",
        ),
    ) # BotManagementCategory | 

    # example passing only required values which don't have defaults set
    try:
        # Set a category action
        api_response = api_instance.bot_management_update_category(workspace_id, category_id, bot_management_category)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_update_category: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **category_id** | **str**| The ID of the bot category. |
 **bot_management_category** | [**BotManagementCategory**](BotManagementCategory.md)|  |

### Return type

[**BotManagementCategoryResponse**](BotManagementCategoryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bot category. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bot_management_update_workspace**
> BotManagementWorkspaceResponse bot_management_update_workspace(workspace_id, bot_management_workspace)

Update a workspace

Update the attributes of a bot management workspace.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import bot_management_api
from fastly.model.bot_management_not_authenticated_error import BotManagementNotAuthenticatedError
from fastly.model.bot_management_not_allowed_error import BotManagementNotAllowedError
from fastly.model.bot_management_workspace import BotManagementWorkspace
from fastly.model.bot_management_workspace_response import BotManagementWorkspaceResponse
from fastly.model.bot_management_not_found_error import BotManagementNotFoundError
from fastly.model.bot_management_invalid_request_error import BotManagementInvalidRequestError
from fastly.model.bot_management_rate_limit_error import BotManagementRateLimitError
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
    api_instance = bot_management_api.BotManagementApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the bot management workspace.
    bot_management_workspace = BotManagementWorkspace(
        name="Production bot policy",
        description="Standard protection for all production services.",
        protection_mode=BotManagementProtectionMode("block"),
    ) # BotManagementWorkspace | 

    # example passing only required values which don't have defaults set
    try:
        # Update a workspace
        api_response = api_instance.bot_management_update_workspace(workspace_id, bot_management_workspace)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BotManagementApi->bot_management_update_workspace: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the bot management workspace. |
 **bot_management_workspace** | [**BotManagementWorkspace**](BotManagementWorkspace.md)|  |

### Return type

[**BotManagementWorkspaceResponse**](BotManagementWorkspaceResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The requested bot management workspace. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

