# fastly.MutualAuthenticationApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mutual_tls_authentication**](MutualAuthenticationApi.md#create_mutual_tls_authentication) | **POST** /tls/mutual_authentications | Create a Mutual Authentication
[**delete_mutual_tls**](MutualAuthenticationApi.md#delete_mutual_tls) | **DELETE** /tls/mutual_authentications/{mutual_authentication_id} | Delete a Mutual TLS
[**get_mutual_authentication**](MutualAuthenticationApi.md#get_mutual_authentication) | **GET** /tls/mutual_authentications/{mutual_authentication_id} | Get a Mutual Authentication
[**list_mutual_authentications**](MutualAuthenticationApi.md#list_mutual_authentications) | **GET** /tls/mutual_authentications | List Mutual Authentications
[**patch_mutual_authentication**](MutualAuthenticationApi.md#patch_mutual_authentication) | **PATCH** /tls/mutual_authentications/{mutual_authentication_id} | Update a Mutual Authentication


# **create_mutual_tls_authentication**
> MutualAuthenticationResponse create_mutual_tls_authentication()

Create a Mutual Authentication

Create a mutual authentication using a bundle of certificates to enable client-to-server mutual TLS.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import mutual_authentication_api
from fastly.model.mutual_authentication import MutualAuthentication
from fastly.model.mutual_authentication_response import MutualAuthenticationResponse
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
    api_instance = mutual_authentication_api.MutualAuthenticationApi(api_client)
    mutual_authentication = MutualAuthentication(
        data=MutualAuthenticationData(
            type=TypeMutualAuthentication("mutual_authentication"),
            attributes=MutualAuthenticationDataAttributes(
                cert_bundle="cert_bundle_example",
                enforced=True,
                name="name_example",
            ),
            relationships=RelationshipsForMutualAuthentication(),
        ),
    ) # MutualAuthentication |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a Mutual Authentication
        api_response = api_instance.create_mutual_tls_authentication(mutual_authentication=mutual_authentication)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->create_mutual_tls_authentication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mutual_authentication** | [**MutualAuthentication**](MutualAuthentication.md)|  | [optional]

### Return type

[**MutualAuthenticationResponse**](MutualAuthenticationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mutual_tls**
> delete_mutual_tls(mutual_authentication_id)

Delete a Mutual TLS

Remove a Mutual TLS authentication

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import mutual_authentication_api
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
    api_instance = mutual_authentication_api.MutualAuthenticationApi(api_client)
    mutual_authentication_id = "SEAwSOsP7dEpTgGZdP7ZFw" # str | Alphanumeric string identifying a mutual authentication.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Mutual TLS
        api_instance.delete_mutual_tls(mutual_authentication_id)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->delete_mutual_tls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mutual_authentication_id** | **str**| Alphanumeric string identifying a mutual authentication. |

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

# **get_mutual_authentication**
> MutualAuthenticationResponse get_mutual_authentication(mutual_authentication_id)

Get a Mutual Authentication

Show a Mutual Authentication.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import mutual_authentication_api
from fastly.model.mutual_authentication_response import MutualAuthenticationResponse
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
    api_instance = mutual_authentication_api.MutualAuthenticationApi(api_client)
    mutual_authentication_id = "SEAwSOsP7dEpTgGZdP7ZFw" # str | Alphanumeric string identifying a mutual authentication.
    include = "include_example" # str | Comma-separated list of related objects to include (optional). Permitted values: `tls_activations`. Including TLS activations will provide you with the TLS domain names that are related to your Mutual TLS authentication.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a Mutual Authentication
        api_response = api_instance.get_mutual_authentication(mutual_authentication_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->get_mutual_authentication: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a Mutual Authentication
        api_response = api_instance.get_mutual_authentication(mutual_authentication_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->get_mutual_authentication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mutual_authentication_id** | **str**| Alphanumeric string identifying a mutual authentication. |
 **include** | **str**| Comma-separated list of related objects to include (optional). Permitted values: `tls_activations`. Including TLS activations will provide you with the TLS domain names that are related to your Mutual TLS authentication.  | [optional]

### Return type

[**MutualAuthenticationResponse**](MutualAuthenticationResponse.md)

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

# **list_mutual_authentications**
> MutualAuthenticationsResponse list_mutual_authentications()

List Mutual Authentications

List all mutual authentications.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import mutual_authentication_api
from fastly.model.mutual_authentications_response import MutualAuthenticationsResponse
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
    api_instance = mutual_authentication_api.MutualAuthenticationApi(api_client)
    include = "include_example" # str | Comma-separated list of related objects to include (optional). Permitted values: `tls_activations`. Including TLS activations will provide you with the TLS domain names that are related to your Mutual TLS authentication.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Mutual Authentications
        api_response = api_instance.list_mutual_authentications(include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->list_mutual_authentications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | **str**| Comma-separated list of related objects to include (optional). Permitted values: `tls_activations`. Including TLS activations will provide you with the TLS domain names that are related to your Mutual TLS authentication.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**MutualAuthenticationsResponse**](MutualAuthenticationsResponse.md)

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

# **patch_mutual_authentication**
> MutualAuthenticationResponse patch_mutual_authentication(mutual_authentication_id)

Update a Mutual Authentication

Update a Mutual Authentication.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import mutual_authentication_api
from fastly.model.mutual_authentication import MutualAuthentication
from fastly.model.mutual_authentication_response import MutualAuthenticationResponse
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
    api_instance = mutual_authentication_api.MutualAuthenticationApi(api_client)
    mutual_authentication_id = "SEAwSOsP7dEpTgGZdP7ZFw" # str | Alphanumeric string identifying a mutual authentication.
    mutual_authentication = MutualAuthentication(
        data=MutualAuthenticationData(
            type=TypeMutualAuthentication("mutual_authentication"),
            attributes=MutualAuthenticationDataAttributes(
                cert_bundle="cert_bundle_example",
                enforced=True,
                name="name_example",
            ),
            relationships=RelationshipsForMutualAuthentication(),
        ),
    ) # MutualAuthentication |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a Mutual Authentication
        api_response = api_instance.patch_mutual_authentication(mutual_authentication_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->patch_mutual_authentication: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a Mutual Authentication
        api_response = api_instance.patch_mutual_authentication(mutual_authentication_id, mutual_authentication=mutual_authentication)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling MutualAuthenticationApi->patch_mutual_authentication: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mutual_authentication_id** | **str**| Alphanumeric string identifying a mutual authentication. |
 **mutual_authentication** | [**MutualAuthentication**](MutualAuthentication.md)|  | [optional]

### Return type

[**MutualAuthenticationResponse**](MutualAuthenticationResponse.md)

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

