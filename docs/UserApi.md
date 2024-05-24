# fastly.UserApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user**](UserApi.md#create_user) | **POST** /user | Create a user
[**delete_user**](UserApi.md#delete_user) | **DELETE** /user/{user_id} | Delete a user
[**get_current_user**](UserApi.md#get_current_user) | **GET** /current_user | Get the current user
[**get_user**](UserApi.md#get_user) | **GET** /user/{user_id} | Get a user
[**request_password_reset**](UserApi.md#request_password_reset) | **POST** /user/{user_login}/password/request_reset | Request a password reset
[**update_user**](UserApi.md#update_user) | **PUT** /user/{user_id} | Update a user
[**update_user_password**](UserApi.md#update_user_password) | **POST** /current_user/password | Update the user&#39;s password


# **create_user**
> UserResponse create_user()

Create a user

Create a user.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import user_api
from fastly.model.user_response import UserResponse
from fastly.model.role_user import RoleUser
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
    api_instance = user_api.UserApi(api_client)
    login = "login_example" # str |  (optional)
    name = "name_example" # str | The real life name of the user. (optional)
    limit_services = True # bool | Indicates that the user has limited access to the customer's services. (optional)
    locked = True # bool, none_type | Indicates whether the is account is locked for editing or not. (optional)
    require_new_password = True # bool, none_type | Indicates if a new password is required at next login. (optional)
    role = RoleUser("user") # RoleUser |  (optional)
    two_factor_auth_enabled = True # bool, none_type | Indicates if 2FA is enabled on the user. (optional)
    two_factor_setup_required = True # bool | Indicates if 2FA is required by the user's customer account. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a user
        api_response = api_instance.create_user(login=login, name=name, limit_services=limit_services, locked=locked, require_new_password=require_new_password, role=role, two_factor_auth_enabled=two_factor_auth_enabled, two_factor_setup_required=two_factor_setup_required)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login** | **str**|  | [optional]
 **name** | **str**| The real life name of the user. | [optional]
 **limit_services** | **bool**| Indicates that the user has limited access to the customer&#39;s services. | [optional]
 **locked** | **bool, none_type**| Indicates whether the is account is locked for editing or not. | [optional]
 **require_new_password** | **bool, none_type**| Indicates if a new password is required at next login. | [optional]
 **role** | [**RoleUser**](RoleUser.md)|  | [optional]
 **two_factor_auth_enabled** | **bool, none_type**| Indicates if 2FA is enabled on the user. | [optional]
 **two_factor_setup_required** | **bool**| Indicates if 2FA is required by the user&#39;s customer account. | [optional]

### Return type

[**UserResponse**](UserResponse.md)

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

# **delete_user**
> InlineResponse200 delete_user(user_id)

Delete a user

Delete a user.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_id = "x9KzsrACXZv8tPwlEDsKb6" # str | Alphanumeric string identifying the user.

    # example passing only required values which don't have defaults set
    try:
        # Delete a user
        api_response = api_instance.delete_user(user_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Alphanumeric string identifying the user. |

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

# **get_current_user**
> UserResponse get_current_user()

Get the current user

Get the logged in user.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import user_api
from fastly.model.user_response import UserResponse
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
    api_instance = user_api.UserApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current user
        api_response = api_instance.get_current_user()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->get_current_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**UserResponse**](UserResponse.md)

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

# **get_user**
> UserResponse get_user(user_id)

Get a user

Get a specific user.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import user_api
from fastly.model.user_response import UserResponse
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
    api_instance = user_api.UserApi(api_client)
    user_id = "x9KzsrACXZv8tPwlEDsKb6" # str | Alphanumeric string identifying the user.

    # example passing only required values which don't have defaults set
    try:
        # Get a user
        api_response = api_instance.get_user(user_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Alphanumeric string identifying the user. |

### Return type

[**UserResponse**](UserResponse.md)

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

# **request_password_reset**
> InlineResponse200 request_password_reset(user_login)

Request a password reset

Requests a password reset for the specified user.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import user_api
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
    api_instance = user_api.UserApi(api_client)
    user_login = "krisowner@example.com" # str | The login associated with the user (typically, an email address).

    # example passing only required values which don't have defaults set
    try:
        # Request a password reset
        api_response = api_instance.request_password_reset(user_login)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->request_password_reset: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_login** | **str**| The login associated with the user (typically, an email address). |

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

# **update_user**
> UserResponse update_user(user_id)

Update a user

Update a user. Only users with the role of `superuser` can make changes to other users on the account. Non-superusers may use this endpoint to make changes to their own account. Two-factor attributes are not editable via this endpoint.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import user_api
from fastly.model.user_response import UserResponse
from fastly.model.role_user import RoleUser
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
    api_instance = user_api.UserApi(api_client)
    user_id = "x9KzsrACXZv8tPwlEDsKb6" # str | Alphanumeric string identifying the user.
    login = "login_example" # str |  (optional)
    name = "name_example" # str | The real life name of the user. (optional)
    limit_services = True # bool | Indicates that the user has limited access to the customer's services. (optional)
    locked = True # bool, none_type | Indicates whether the is account is locked for editing or not. (optional)
    require_new_password = True # bool, none_type | Indicates if a new password is required at next login. (optional)
    role = RoleUser("user") # RoleUser |  (optional)
    two_factor_auth_enabled = True # bool, none_type | Indicates if 2FA is enabled on the user. (optional)
    two_factor_setup_required = True # bool | Indicates if 2FA is required by the user's customer account. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a user
        api_response = api_instance.update_user(user_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a user
        api_response = api_instance.update_user(user_id, login=login, name=name, limit_services=limit_services, locked=locked, require_new_password=require_new_password, role=role, two_factor_auth_enabled=two_factor_auth_enabled, two_factor_setup_required=two_factor_setup_required)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Alphanumeric string identifying the user. |
 **login** | **str**|  | [optional]
 **name** | **str**| The real life name of the user. | [optional]
 **limit_services** | **bool**| Indicates that the user has limited access to the customer&#39;s services. | [optional]
 **locked** | **bool, none_type**| Indicates whether the is account is locked for editing or not. | [optional]
 **require_new_password** | **bool, none_type**| Indicates if a new password is required at next login. | [optional]
 **role** | [**RoleUser**](RoleUser.md)|  | [optional]
 **two_factor_auth_enabled** | **bool, none_type**| Indicates if 2FA is enabled on the user. | [optional]
 **two_factor_setup_required** | **bool**| Indicates if 2FA is required by the user&#39;s customer account. | [optional]

### Return type

[**UserResponse**](UserResponse.md)

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

# **update_user_password**
> UserResponse update_user_password()

Update the user's password

Update the user's password to a new one.

### Example

* Basic Authentication (session_password_change):

```python
import time
import fastly
from fastly.api import user_api
from fastly.model.user_response import UserResponse
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

# Configure HTTP basic authorization: session_password_change
configuration = fastly.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    old_password = "old_password_example" # str | The user's current password. (optional)
    new_password = "new_password_example" # str | The user's new password. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the user's password
        api_response = api_instance.update_user_password(old_password=old_password, new_password=new_password)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling UserApi->update_user_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **old_password** | **str**| The user&#39;s current password. | [optional]
 **new_password** | **str**| The user&#39;s new password. | [optional]

### Return type

[**UserResponse**](UserResponse.md)

### Authorization

[session_password_change](../README.md#session_password_change)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

