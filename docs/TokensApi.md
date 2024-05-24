# fastly.TokensApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_revoke_tokens**](TokensApi.md#bulk_revoke_tokens) | **DELETE** /tokens | Revoke multiple tokens
[**create_token**](TokensApi.md#create_token) | **POST** /tokens | Create a token
[**get_token**](TokensApi.md#get_token) | **GET** /tokens/{token_id} | Get a token
[**get_token_current**](TokensApi.md#get_token_current) | **GET** /tokens/self | Get the current token
[**list_tokens_customer**](TokensApi.md#list_tokens_customer) | **GET** /customer/{customer_id}/tokens | List tokens for a customer
[**list_tokens_user**](TokensApi.md#list_tokens_user) | **GET** /tokens | List tokens for the authenticated user
[**revoke_token**](TokensApi.md#revoke_token) | **DELETE** /tokens/{token_id} | Revoke a token
[**revoke_token_current**](TokensApi.md#revoke_token_current) | **DELETE** /tokens/self | Revoke the current token


# **bulk_revoke_tokens**
> bulk_revoke_tokens()

Revoke multiple tokens

Revoke Tokens in bulk format. Users may only revoke their own tokens. Superusers may revoke tokens of others.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
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
    api_instance = tokens_api.TokensApi(api_client)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Revoke multiple tokens
        api_instance.bulk_revoke_tokens(request_body=request_body)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->bulk_revoke_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json; ext=bulk
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_token**
> TokenCreatedResponse create_token()

Create a token

Create an API token. If two-factor authentication is enabled for your account, review [the instructions](https://www.fastly.com/documentation/reference/api/auth-tokens/user/) for including a one-time password in the request. 

### Example

* Api Key Authentication (token):
* Basic Authentication (username_and_password):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.inline_response400 import InlineResponse400
from fastly.model.token_created_response import TokenCreatedResponse
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

# Configure HTTP basic authorization: username_and_password
configuration = fastly.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = tokens_api.TokensApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Create a token
        api_response = api_instance.create_token()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->create_token: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenCreatedResponse**](TokenCreatedResponse.md)

### Authorization

[token](../README.md#token), [username_and_password](../README.md#username_and_password)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**422** | The format of the date and time supplied to the `expires_at` parameter is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token**
> TokenResponse get_token(token_id)

Get a token

Get a single token by its id.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.generic_token_error import GenericTokenError
from fastly.model.token_response import TokenResponse
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
    api_instance = tokens_api.TokensApi(api_client)
    token_id = "5Yo3XXnrQpjc20u0ybrf2g" # str | Alphanumeric string identifying a token.

    # example passing only required values which don't have defaults set
    try:
        # Get a token
        api_response = api_instance.get_token(token_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->get_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| Alphanumeric string identifying a token. |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Missing or expired token. |  -  |
**403** | Invalid token. |  -  |
**404** | Token lookup failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_token_current**
> TokenResponse get_token_current()

Get the current token

Get a single token based on the access_token used in the request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.generic_token_error import GenericTokenError
from fastly.model.token_response import TokenResponse
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
    api_instance = tokens_api.TokensApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the current token
        api_response = api_instance.get_token_current()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->get_token_current: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Missing or expired token. |  -  |
**403** | Invalid token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tokens_customer**
> [TokenResponse] list_tokens_customer(customer_id)

List tokens for a customer

List all tokens belonging to a specific customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.token_response import TokenResponse
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
    api_instance = tokens_api.TokensApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # List tokens for a customer
        api_response = api_instance.list_tokens_customer(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->list_tokens_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

### Return type

[**[TokenResponse]**](TokenResponse.md)

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

# **list_tokens_user**
> [TokenResponse] list_tokens_user()

List tokens for the authenticated user

List all tokens belonging to the authenticated user.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.generic_token_error import GenericTokenError
from fastly.model.token_response import TokenResponse
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
    api_instance = tokens_api.TokensApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List tokens for the authenticated user
        api_response = api_instance.list_tokens_user()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->list_tokens_user: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[TokenResponse]**](TokenResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Missing or expired token. |  -  |
**403** | Invalid token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> revoke_token(token_id)

Revoke a token

Revoke a specific token by its id.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.generic_token_error import GenericTokenError
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
    api_instance = tokens_api.TokensApi(api_client)
    token_id = "5Yo3XXnrQpjc20u0ybrf2g" # str | Alphanumeric string identifying a token.

    # example passing only required values which don't have defaults set
    try:
        # Revoke a token
        api_instance.revoke_token(token_id)
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->revoke_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| Alphanumeric string identifying a token. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Token revocation error. |  -  |
**401** | Missing or expired token. |  -  |
**403** | Invalid token. |  -  |
**404** | Token lookup failed. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token_current**
> revoke_token_current()

Revoke the current token

Revoke a token that is used to authenticate the request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tokens_api
from fastly.model.generic_token_error import GenericTokenError
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
    api_instance = tokens_api.TokensApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Revoke the current token
        api_instance.revoke_token_current()
    except fastly.ApiException as e:
        print("Exception when calling TokensApi->revoke_token_current: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Token revocation error. |  -  |
**401** | Missing or expired token. |  -  |
**403** | Invalid token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

