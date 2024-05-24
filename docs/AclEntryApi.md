# fastly.AclEntryApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_acl_entries**](AclEntryApi.md#bulk_update_acl_entries) | **PATCH** /service/{service_id}/acl/{acl_id}/entries | Update multiple ACL entries
[**create_acl_entry**](AclEntryApi.md#create_acl_entry) | **POST** /service/{service_id}/acl/{acl_id}/entry | Create an ACL entry
[**delete_acl_entry**](AclEntryApi.md#delete_acl_entry) | **DELETE** /service/{service_id}/acl/{acl_id}/entry/{acl_entry_id} | Delete an ACL entry
[**get_acl_entry**](AclEntryApi.md#get_acl_entry) | **GET** /service/{service_id}/acl/{acl_id}/entry/{acl_entry_id} | Describe an ACL entry
[**list_acl_entries**](AclEntryApi.md#list_acl_entries) | **GET** /service/{service_id}/acl/{acl_id}/entries | List ACL entries
[**update_acl_entry**](AclEntryApi.md#update_acl_entry) | **PATCH** /service/{service_id}/acl/{acl_id}/entry/{acl_entry_id} | Update an ACL entry


# **bulk_update_acl_entries**
> InlineResponse200 bulk_update_acl_entries(service_id, acl_id)

Update multiple ACL entries

Update multiple ACL entries on the same ACL. For faster updates to your service, group your changes into large batches. The maximum batch size is 1000 entries. [Contact support](https://support.fastly.com/) to discuss raising this limit.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acl_entry_api
from fastly.model.inline_response200 import InlineResponse200
from fastly.model.bulk_update_acl_entries_request import BulkUpdateAclEntriesRequest
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
    api_instance = acl_entry_api.AclEntryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    acl_id = "6tUXdegLTf5BCig0zGFrU3" # str | Alphanumeric string identifying a ACL.
    bulk_update_acl_entries_request = BulkUpdateAclEntriesRequest(
        entries=[
            BulkUpdateAclEntry(),
        ],
    ) # BulkUpdateAclEntriesRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple ACL entries
        api_response = api_instance.bulk_update_acl_entries(service_id, acl_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->bulk_update_acl_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple ACL entries
        api_response = api_instance.bulk_update_acl_entries(service_id, acl_id, bulk_update_acl_entries_request=bulk_update_acl_entries_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->bulk_update_acl_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **acl_id** | **str**| Alphanumeric string identifying a ACL. |
 **bulk_update_acl_entries_request** | [**BulkUpdateAclEntriesRequest**](BulkUpdateAclEntriesRequest.md)|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

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

# **create_acl_entry**
> AclEntryResponse create_acl_entry(service_id, acl_id)

Create an ACL entry

Add an ACL entry to an ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acl_entry_api
from fastly.model.acl_entry_response import AclEntryResponse
from fastly.model.acl_entry import AclEntry
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
    api_instance = acl_entry_api.AclEntryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    acl_id = "6tUXdegLTf5BCig0zGFrU3" # str | Alphanumeric string identifying a ACL.
    acl_entry = AclEntry(
        negated=0,
        comment="",
        ip="127.0.0.1",
        subnet=8,
    ) # AclEntry |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an ACL entry
        api_response = api_instance.create_acl_entry(service_id, acl_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->create_acl_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an ACL entry
        api_response = api_instance.create_acl_entry(service_id, acl_id, acl_entry=acl_entry)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->create_acl_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **acl_id** | **str**| Alphanumeric string identifying a ACL. |
 **acl_entry** | [**AclEntry**](AclEntry.md)|  | [optional]

### Return type

[**AclEntryResponse**](AclEntryResponse.md)

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

# **delete_acl_entry**
> InlineResponse200 delete_acl_entry(service_id, acl_id, acl_entry_id)

Delete an ACL entry

Delete an ACL entry from a specified ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acl_entry_api
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
    api_instance = acl_entry_api.AclEntryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    acl_id = "6tUXdegLTf5BCig0zGFrU3" # str | Alphanumeric string identifying a ACL.
    acl_entry_id = "6yxNzlOpW1V7JfSwvLGtOc" # str | Alphanumeric string identifying an ACL Entry.

    # example passing only required values which don't have defaults set
    try:
        # Delete an ACL entry
        api_response = api_instance.delete_acl_entry(service_id, acl_id, acl_entry_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->delete_acl_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **acl_id** | **str**| Alphanumeric string identifying a ACL. |
 **acl_entry_id** | **str**| Alphanumeric string identifying an ACL Entry. |

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

# **get_acl_entry**
> AclEntryResponse get_acl_entry(service_id, acl_id, acl_entry_id)

Describe an ACL entry

Retrieve a single ACL entry.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acl_entry_api
from fastly.model.acl_entry_response import AclEntryResponse
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
    api_instance = acl_entry_api.AclEntryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    acl_id = "6tUXdegLTf5BCig0zGFrU3" # str | Alphanumeric string identifying a ACL.
    acl_entry_id = "6yxNzlOpW1V7JfSwvLGtOc" # str | Alphanumeric string identifying an ACL Entry.

    # example passing only required values which don't have defaults set
    try:
        # Describe an ACL entry
        api_response = api_instance.get_acl_entry(service_id, acl_id, acl_entry_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->get_acl_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **acl_id** | **str**| Alphanumeric string identifying a ACL. |
 **acl_entry_id** | **str**| Alphanumeric string identifying an ACL Entry. |

### Return type

[**AclEntryResponse**](AclEntryResponse.md)

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

# **list_acl_entries**
> [AclEntryResponse] list_acl_entries(service_id, acl_id)

List ACL entries

List ACL entries for a specified ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acl_entry_api
from fastly.model.acl_entry_response import AclEntryResponse
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
    api_instance = acl_entry_api.AclEntryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    acl_id = "6tUXdegLTf5BCig0zGFrU3" # str | Alphanumeric string identifying a ACL.
    page = 1 # int | Current page. (optional)
    per_page = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    sort = "created" # str | Field on which to sort. (optional) if omitted the server will use the default value of "created"
    direction = "ascend" # str | Direction in which to sort results. (optional) if omitted the server will use the default value of "ascend"

    # example passing only required values which don't have defaults set
    try:
        # List ACL entries
        api_response = api_instance.list_acl_entries(service_id, acl_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->list_acl_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List ACL entries
        api_response = api_instance.list_acl_entries(service_id, acl_id, page=page, per_page=per_page, sort=sort, direction=direction)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->list_acl_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **acl_id** | **str**| Alphanumeric string identifying a ACL. |
 **page** | **int**| Current page. | [optional]
 **per_page** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| Field on which to sort. | [optional] if omitted the server will use the default value of "created"
 **direction** | **str**| Direction in which to sort results. | [optional] if omitted the server will use the default value of "ascend"

### Return type

[**[AclEntryResponse]**](AclEntryResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Link - Contains URLs for fetching additional paginated results. <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_acl_entry**
> AclEntryResponse update_acl_entry(service_id, acl_id, acl_entry_id)

Update an ACL entry

Update an ACL entry for a specified ACL.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import acl_entry_api
from fastly.model.acl_entry_response import AclEntryResponse
from fastly.model.acl_entry import AclEntry
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
    api_instance = acl_entry_api.AclEntryApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    acl_id = "6tUXdegLTf5BCig0zGFrU3" # str | Alphanumeric string identifying a ACL.
    acl_entry_id = "6yxNzlOpW1V7JfSwvLGtOc" # str | Alphanumeric string identifying an ACL Entry.
    acl_entry = AclEntry(
        negated=0,
        comment="",
        ip="127.0.0.1",
        subnet=8,
    ) # AclEntry |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an ACL entry
        api_response = api_instance.update_acl_entry(service_id, acl_id, acl_entry_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->update_acl_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an ACL entry
        api_response = api_instance.update_acl_entry(service_id, acl_id, acl_entry_id, acl_entry=acl_entry)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclEntryApi->update_acl_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **acl_id** | **str**| Alphanumeric string identifying a ACL. |
 **acl_entry_id** | **str**| Alphanumeric string identifying an ACL Entry. |
 **acl_entry** | [**AclEntry**](AclEntry.md)|  | [optional]

### Return type

[**AclEntryResponse**](AclEntryResponse.md)

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

