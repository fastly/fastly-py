# fastly.AclsInComputeApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_acl_create_acls**](AclsInComputeApi.md#compute_acl_create_acls) | **POST** /resources/acls | Create a new ACL
[**compute_acl_delete_s_acl_id**](AclsInComputeApi.md#compute_acl_delete_s_acl_id) | **DELETE** /resources/acls/{acl_id} | Delete an ACL
[**compute_acl_list_acl_entries**](AclsInComputeApi.md#compute_acl_list_acl_entries) | **GET** /resources/acls/{acl_id}/entries | List an ACL
[**compute_acl_list_acls**](AclsInComputeApi.md#compute_acl_list_acls) | **GET** /resources/acls | List ACLs
[**compute_acl_list_acls_s_acl_id**](AclsInComputeApi.md#compute_acl_list_acls_s_acl_id) | **GET** /resources/acls/{acl_id} | Describe an ACL
[**compute_acl_lookup_acls**](AclsInComputeApi.md#compute_acl_lookup_acls) | **GET** /resources/acls/{acl_id}/entry/{acl_ip} | Lookup an ACL
[**compute_acl_update_acls**](AclsInComputeApi.md#compute_acl_update_acls) | **PATCH** /resources/acls/{acl_id}/entries | Update an ACL


# **compute_acl_create_acls**
> ComputeAclCreateAclsResponse compute_acl_create_acls()

Create a new ACL

Create a new ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
from fastly.model.compute_acl_create_acls_response import ComputeAclCreateAclsResponse
from fastly.model.compute_acl_create_acls_request import ComputeAclCreateAclsRequest
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)
    compute_acl_create_acls_request = ComputeAclCreateAclsRequest(
        name="name_example",
    ) # ComputeAclCreateAclsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new ACL
        api_response = api_instance.compute_acl_create_acls(compute_acl_create_acls_request=compute_acl_create_acls_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_create_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **compute_acl_create_acls_request** | [**ComputeAclCreateAclsRequest**](ComputeAclCreateAclsRequest.md)|  | [optional]

### Return type

[**ComputeAclCreateAclsResponse**](ComputeAclCreateAclsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_acl_delete_s_acl_id**
> compute_acl_delete_s_acl_id(acl_id)

Delete an ACL

Delete an ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)
    acl_id = "acl_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an ACL
        api_instance.compute_acl_delete_s_acl_id(acl_id)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_delete_s_acl_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**|  |

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
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_acl_list_acl_entries**
> ComputeAclListEntries compute_acl_list_acl_entries(acl_id)

List an ACL

List an ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
from fastly.model.compute_acl_list_entries import ComputeAclListEntries
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)
    acl_id = "acl_id_example" # str | 
    cursor = "cursor_example" # str |  (optional)
    limit = 100 # int |  (optional) if omitted the server will use the default value of 100

    # example passing only required values which don't have defaults set
    try:
        # List an ACL
        api_response = api_instance.compute_acl_list_acl_entries(acl_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_list_acl_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List an ACL
        api_response = api_instance.compute_acl_list_acl_entries(acl_id, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_list_acl_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**|  |
 **cursor** | **str**|  | [optional]
 **limit** | **int**|  | [optional] if omitted the server will use the default value of 100

### Return type

[**ComputeAclListEntries**](ComputeAclListEntries.md)

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

# **compute_acl_list_acls**
> ComputeAclList compute_acl_list_acls()

List ACLs

List all ACLs.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
from fastly.model.compute_acl_list import ComputeAclList
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List ACLs
        api_response = api_instance.compute_acl_list_acls()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_list_acls: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ComputeAclList**](ComputeAclList.md)

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

# **compute_acl_list_acls_s_acl_id**
> ComputeAclCreateAclsResponse compute_acl_list_acls_s_acl_id(acl_id)

Describe an ACL

Describe an ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
from fastly.model.compute_acl_create_acls_response import ComputeAclCreateAclsResponse
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)
    acl_id = "acl_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Describe an ACL
        api_response = api_instance.compute_acl_list_acls_s_acl_id(acl_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_list_acls_s_acl_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**|  |

### Return type

[**ComputeAclCreateAclsResponse**](ComputeAclCreateAclsResponse.md)

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

# **compute_acl_lookup_acls**
> ComputeAclLookup compute_acl_lookup_acls(acl_id, acl_ip)

Lookup an ACL

Find a matching ACL entry for an IP address.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
from fastly.model.compute_acl_lookup import ComputeAclLookup
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)
    acl_id = "acl_id_example" # str | 
    acl_ip = "acl_ip_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Lookup an ACL
        api_response = api_instance.compute_acl_lookup_acls(acl_id, acl_ip)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_lookup_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**|  |
 **acl_ip** | **str**|  |

### Return type

[**ComputeAclLookup**](ComputeAclLookup.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_acl_update_acls**
> compute_acl_update_acls(acl_id)

Update an ACL

Update an ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acls_in_compute_api
from fastly.model.compute_acl_update import ComputeAclUpdate
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
    api_instance = acls_in_compute_api.AclsInComputeApi(api_client)
    acl_id = "acl_id_example" # str | 
    compute_acl_update = ComputeAclUpdate(
        entries=[
            ComputeAclUpdateEntry(
                op="op_example",
                prefix="prefix_example",
                action="action_example",
            ),
        ],
    ) # ComputeAclUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an ACL
        api_instance.compute_acl_update_acls(acl_id)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_update_acls: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an ACL
        api_instance.compute_acl_update_acls(acl_id, compute_acl_update=compute_acl_update)
    except fastly.ApiException as e:
        print("Exception when calling AclsInComputeApi->compute_acl_update_acls: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **acl_id** | **str**|  |
 **compute_acl_update** | [**ComputeAclUpdate**](ComputeAclUpdate.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

