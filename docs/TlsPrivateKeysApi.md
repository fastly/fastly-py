# fastly.TlsPrivateKeysApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tls_key**](TlsPrivateKeysApi.md#create_tls_key) | **POST** /tls/private_keys | Create a TLS private key
[**delete_tls_key**](TlsPrivateKeysApi.md#delete_tls_key) | **DELETE** /tls/private_keys/{tls_private_key_id} | Delete a TLS private key
[**get_tls_key**](TlsPrivateKeysApi.md#get_tls_key) | **GET** /tls/private_keys/{tls_private_key_id} | Get a TLS private key
[**list_tls_keys**](TlsPrivateKeysApi.md#list_tls_keys) | **GET** /tls/private_keys | List TLS private keys


# **create_tls_key**
> TlsPrivateKeyResponse create_tls_key()

Create a TLS private key

Create a TLS private key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_private_keys_api
from fastly.model.tls_private_key import TlsPrivateKey
from fastly.model.tls_private_key_response import TlsPrivateKeyResponse
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
    api_instance = tls_private_keys_api.TlsPrivateKeysApi(api_client)
    tls_private_key = TlsPrivateKey(
        data=TlsPrivateKeyData(
            type=TypeTlsPrivateKey("tls_private_key"),
            attributes=TlsPrivateKeyDataAttributes(
                name="name_example",
                key="key_example",
            ),
            relationships=RelationshipsForTlsPrivateKey(),
        ),
    ) # TlsPrivateKey |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a TLS private key
        api_response = api_instance.create_tls_key(tls_private_key=tls_private_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsPrivateKeysApi->create_tls_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_private_key** | [**TlsPrivateKey**](TlsPrivateKey.md)|  | [optional]

### Return type

[**TlsPrivateKeyResponse**](TlsPrivateKeyResponse.md)

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

# **delete_tls_key**
> delete_tls_key(tls_private_key_id)

Delete a TLS private key

Destroy a TLS private key. Only private keys not already matched to any certificates can be deleted.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_private_keys_api
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
    api_instance = tls_private_keys_api.TlsPrivateKeysApi(api_client)
    tls_private_key_id = "KeYguUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a private Key.

    # example passing only required values which don't have defaults set
    try:
        # Delete a TLS private key
        api_instance.delete_tls_key(tls_private_key_id)
    except fastly.ApiException as e:
        print("Exception when calling TlsPrivateKeysApi->delete_tls_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_private_key_id** | **str**| Alphanumeric string identifying a private Key. |

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

# **get_tls_key**
> TlsPrivateKeyResponse get_tls_key(tls_private_key_id)

Get a TLS private key

Show a TLS private key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_private_keys_api
from fastly.model.tls_private_key_response import TlsPrivateKeyResponse
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
    api_instance = tls_private_keys_api.TlsPrivateKeysApi(api_client)
    tls_private_key_id = "KeYguUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a private Key.

    # example passing only required values which don't have defaults set
    try:
        # Get a TLS private key
        api_response = api_instance.get_tls_key(tls_private_key_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsPrivateKeysApi->get_tls_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_private_key_id** | **str**| Alphanumeric string identifying a private Key. |

### Return type

[**TlsPrivateKeyResponse**](TlsPrivateKeyResponse.md)

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

# **list_tls_keys**
> TlsPrivateKeysResponse list_tls_keys()

List TLS private keys

List all TLS private keys.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_private_keys_api
from fastly.model.tls_private_keys_response import TlsPrivateKeysResponse
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
    api_instance = tls_private_keys_api.TlsPrivateKeysApi(api_client)
    filter_in_use = "filter[in_use]_example" # str | Limit the returned keys to those without any matching TLS certificates. The only valid value is false. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TLS private keys
        api_response = api_instance.list_tls_keys(filter_in_use=filter_in_use, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsPrivateKeysApi->list_tls_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_in_use** | **str**| Limit the returned keys to those without any matching TLS certificates. The only valid value is false. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**TlsPrivateKeysResponse**](TlsPrivateKeysResponse.md)

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

