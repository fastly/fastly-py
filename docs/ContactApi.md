# fastly.ContactApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /customer/{customer_id}/contact/{contact_id} | Delete a contact
[**list_contacts**](ContactApi.md#list_contacts) | **GET** /customer/{customer_id}/contacts | List contacts


# **delete_contact**
> InlineResponse200 delete_contact(customer_id, contact_id)

Delete a contact

Delete a contact.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import contact_api
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
    api_instance = contact_api.ContactApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    contact_id = "x4xCwxxJxGCx123Rx5xTx" # str | An alphanumeric string identifying the customer contact.

    # example passing only required values which don't have defaults set
    try:
        # Delete a contact
        api_response = api_instance.delete_contact(customer_id, contact_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ContactApi->delete_contact: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **contact_id** | **str**| An alphanumeric string identifying the customer contact. |

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

# **list_contacts**
> [SchemasContactResponse] list_contacts(customer_id)

List contacts

List all contacts from a specified customer ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import contact_api
from fastly.model.schemas_contact_response import SchemasContactResponse
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
    api_instance = contact_api.ContactApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # List contacts
        api_response = api_instance.list_contacts(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ContactApi->list_contacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

### Return type

[**[SchemasContactResponse]**](SchemasContactResponse.md)

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

