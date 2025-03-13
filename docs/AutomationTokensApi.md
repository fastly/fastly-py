# fastly.AutomationTokensApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_automation_token**](AutomationTokensApi.md#create_automation_token) | **POST** /automation-tokens | Create Automation Token
[**get_automation_token_id**](AutomationTokensApi.md#get_automation_token_id) | **GET** /automation-tokens/{id} | Retrieve an Automation Token by ID
[**get_automation_tokens_id_services**](AutomationTokensApi.md#get_automation_tokens_id_services) | **GET** /automation-tokens/{id}/services | List Automation Token Services
[**list_automation_tokens**](AutomationTokensApi.md#list_automation_tokens) | **GET** /automation-tokens | List Customer Automation Tokens
[**revoke_automation_token_id**](AutomationTokensApi.md#revoke_automation_token_id) | **DELETE** /automation-tokens/{id} | Revoke an Automation Token by ID


# **create_automation_token**
> AutomationTokenCreateResponse create_automation_token()

Create Automation Token

Creates a new automation token.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import automation_tokens_api
from fastly.model.automation_token_create_request import AutomationTokenCreateRequest
from fastly.model.automation_token_create_response import AutomationTokenCreateResponse
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
    api_instance = automation_tokens_api.AutomationTokensApi(api_client)
    automation_token_create_request = AutomationTokenCreateRequest(
        attributes=AutomationTokenCreateRequestAttributes(
            name="name_example",
            role="engineer",
            services=[
                "services_example",
            ],
            scope="global",
            expires_at=dateutil_parser('1970-01-01T00:00:00.00Z'),
            tls_access=True,
        ),
    ) # AutomationTokenCreateRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create Automation Token
        api_response = api_instance.create_automation_token(automation_token_create_request=automation_token_create_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AutomationTokensApi->create_automation_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **automation_token_create_request** | [**AutomationTokenCreateRequest**](AutomationTokenCreateRequest.md)|  | [optional]

### Return type

[**AutomationTokenCreateResponse**](AutomationTokenCreateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automation_token_id**
> AutomationTokenResponse get_automation_token_id(id)

Retrieve an Automation Token by ID

Retrieves an automation token by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import automation_tokens_api
from fastly.model.automation_token_response import AutomationTokenResponse
from fastly.model.automation_token_error_response import AutomationTokenErrorResponse
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
    api_instance = automation_tokens_api.AutomationTokensApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve an Automation Token by ID
        api_response = api_instance.get_automation_token_id(id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AutomationTokensApi->get_automation_token_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**AutomationTokenResponse**](AutomationTokenResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized response is returned on an expired token. |  -  |
**403** | Forbidden response is returned on an invalid access token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_automation_tokens_id_services**
> InlineResponse2001 get_automation_tokens_id_services(id)

List Automation Token Services

List of services associated with the automation token.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import automation_tokens_api
from fastly.model.automation_token_error_response import AutomationTokenErrorResponse
from fastly.model.inline_response2001 import InlineResponse2001
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
    api_instance = automation_tokens_api.AutomationTokensApi(api_client)
    id = "id_example" # str | 
    per_page = 1 # int |  (optional)
    page = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List Automation Token Services
        api_response = api_instance.get_automation_tokens_id_services(id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AutomationTokensApi->get_automation_tokens_id_services: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Automation Token Services
        api_response = api_instance.get_automation_tokens_id_services(id, per_page=per_page, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AutomationTokensApi->get_automation_tokens_id_services: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |
 **per_page** | **int**|  | [optional]
 **page** | **int**|  | [optional]

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized response is returned on an expired token. |  -  |
**403** | Forbidden response is returned on an invalid access token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_automation_tokens**
> [AutomationTokenResponse] list_automation_tokens()

List Customer Automation Tokens

Lists all automation tokens for a customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import automation_tokens_api
from fastly.model.automation_token_response import AutomationTokenResponse
from fastly.model.automation_token_error_response import AutomationTokenErrorResponse
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
    api_instance = automation_tokens_api.AutomationTokensApi(api_client)
    per_page = 1 # int |  (optional)
    page = 1 # int |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Customer Automation Tokens
        api_response = api_instance.list_automation_tokens(per_page=per_page, page=page)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AutomationTokensApi->list_automation_tokens: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**|  | [optional]
 **page** | **int**|  | [optional]

### Return type

[**[AutomationTokenResponse]**](AutomationTokenResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized response is returned on an expired token. |  -  |
**403** | Forbidden response is returned on an invalid access token. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_automation_token_id**
> AutomationTokenErrorResponse revoke_automation_token_id(id)

Revoke an Automation Token by ID

Revoke an automation token by ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import automation_tokens_api
from fastly.model.automation_token_error_response import AutomationTokenErrorResponse
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
    api_instance = automation_tokens_api.AutomationTokensApi(api_client)
    id = "id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Revoke an Automation Token by ID
        api_response = api_instance.revoke_automation_token_id(id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AutomationTokensApi->revoke_automation_token_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  |

### Return type

[**AutomationTokenErrorResponse**](AutomationTokenErrorResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request response is returned on a revocation error. |  -  |
**401** | Unauthorized response is returned on an expired token. |  -  |
**403** | Forbidden response is returned on an invalid access token. |  -  |
**404** | Not Found response is returned on a failed token lookup. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

