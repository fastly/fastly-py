# fastly.ContactApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contacts**](ContactApi.md#create_contacts) | **POST** /customer/{customer_id}/contacts | Add a new customer contact
[**delete_contact**](ContactApi.md#delete_contact) | **DELETE** /customer/{customer_id}/contacts/{contact_id} | Delete a contact
[**list_contacts**](ContactApi.md#list_contacts) | **GET** /customer/{customer_id}/contacts | List contacts


# **create_contacts**
> ContactResponse create_contacts(customer_id)

Add a new customer contact

Create a contact.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import contact_api
from fastly.model.contact_response import ContactResponse
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
    user_id = "user_id_example" # str, none_type | The alphanumeric string representing the user for this customer contact. (optional)
    contact_type = "primary" # str | The type of contact. (optional)
    name = "name_example" # str, none_type | The name of this contact, when user_id is not provided. (optional)
    email = "email_example" # str, none_type | The email of this contact, when a user_id is not provided. (optional)
    phone = "phone_example" # str, none_type | The phone number for this contact. Required for primary, technical, and security contact types. (optional)
    customer_id2 = "customer_id_example" # str, none_type | The alphanumeric string representing the customer for this customer contact. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a new customer contact
        api_response = api_instance.create_contacts(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ContactApi->create_contacts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a new customer contact
        api_response = api_instance.create_contacts(customer_id, user_id=user_id, contact_type=contact_type, name=name, email=email, phone=phone, customer_id2=customer_id2)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ContactApi->create_contacts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **user_id** | **str, none_type**| The alphanumeric string representing the user for this customer contact. | [optional]
 **contact_type** | **str**| The type of contact. | [optional]
 **name** | **str, none_type**| The name of this contact, when user_id is not provided. | [optional]
 **email** | **str, none_type**| The email of this contact, when a user_id is not provided. | [optional]
 **phone** | **str, none_type**| The phone number for this contact. Required for primary, technical, and security contact types. | [optional]
 **customer_id2** | **str, none_type**| The alphanumeric string representing the customer for this customer contact. | [optional]

### Return type

[**ContactResponse**](ContactResponse.md)

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

