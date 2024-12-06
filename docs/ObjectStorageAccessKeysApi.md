# fastly.ObjectStorageAccessKeysApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_key**](ObjectStorageAccessKeysApi.md#create_access_key) | **POST** /resources/object-storage/access-keys | Create an access key
[**delete_access_key**](ObjectStorageAccessKeysApi.md#delete_access_key) | **DELETE** /resources/object-storage/access-keys/{access_key} | Delete an access key
[**get_access_key**](ObjectStorageAccessKeysApi.md#get_access_key) | **GET** /resources/object-storage/access-keys/{access_key} | Get an access key
[**list_access_keys**](ObjectStorageAccessKeysApi.md#list_access_keys) | **GET** /resources/object-storage/access-keys | List access keys


# **create_access_key**
> AccessKeyResponse create_access_key()

Create an access key

Create an access key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_storage_access_keys_api
from fastly.model.access_key_response import AccessKeyResponse
from fastly.model.access_key import AccessKey
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
    api_instance = object_storage_access_keys_api.ObjectStorageAccessKeysApi(api_client)
    access_key = AccessKey(
        description="description_example",
        permission="permission_example",
        buckets=[
            "buckets_example",
        ],
    ) # AccessKey |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an access key
        api_response = api_instance.create_access_key(access_key=access_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStorageAccessKeysApi->create_access_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | [**AccessKey**](AccessKey.md)|  | [optional]

### Return type

[**AccessKeyResponse**](AccessKeyResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_key**
> delete_access_key(access_key)

Delete an access key

Delete an access key.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_storage_access_keys_api
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
    api_instance = object_storage_access_keys_api.ObjectStorageAccessKeysApi(api_client)
    access_key = "access_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an access key
        api_instance.delete_access_key(access_key)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStorageAccessKeysApi->delete_access_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**|  |

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

# **get_access_key**
> AccessKey get_access_key(access_key)

Get an access key

Get an access key by its identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_storage_access_keys_api
from fastly.model.access_key import AccessKey
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
    api_instance = object_storage_access_keys_api.ObjectStorageAccessKeysApi(api_client)
    access_key = "access_key_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get an access key
        api_response = api_instance.get_access_key(access_key)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStorageAccessKeysApi->get_access_key: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **access_key** | **str**|  |

### Return type

[**AccessKey**](AccessKey.md)

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

# **list_access_keys**
> AccessKeyResponse list_access_keys()

List access keys

List access keys.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import object_storage_access_keys_api
from fastly.model.access_key_response import AccessKeyResponse
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
    api_instance = object_storage_access_keys_api.ObjectStorageAccessKeysApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List access keys
        api_response = api_instance.list_access_keys()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObjectStorageAccessKeysApi->list_access_keys: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessKeyResponse**](AccessKeyResponse.md)

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

