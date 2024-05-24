# fastly.CustomerApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer**](CustomerApi.md#delete_customer) | **DELETE** /customer/{customer_id} | Delete a customer
[**get_customer**](CustomerApi.md#get_customer) | **GET** /customer/{customer_id} | Get a customer
[**get_logged_in_customer**](CustomerApi.md#get_logged_in_customer) | **GET** /current_customer | Get the logged in customer
[**list_users**](CustomerApi.md#list_users) | **GET** /customer/{customer_id}/users | List users
[**update_customer**](CustomerApi.md#update_customer) | **PUT** /customer/{customer_id} | Update a customer


# **delete_customer**
> InlineResponse200 delete_customer(customer_id)

Delete a customer

Delete a customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_api
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
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # Delete a customer
        api_response = api_instance.delete_customer(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerApi->delete_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

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

# **get_customer**
> CustomerResponse get_customer(customer_id)

Get a customer

Get a specific customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_api
from fastly.model.customer_response import CustomerResponse
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
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # Get a customer
        api_response = api_instance.get_customer(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerApi->get_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **get_logged_in_customer**
> CustomerResponse get_logged_in_customer()

Get the logged in customer

Get the logged in customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_api
from fastly.model.customer_response import CustomerResponse
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
    api_instance = customer_api.CustomerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get the logged in customer
        api_response = api_instance.get_logged_in_customer()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerApi->get_logged_in_customer: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

# **list_users**
> [SchemasUserResponse] list_users(customer_id)

List users

List all users from a specified customer id.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_api
from fastly.model.schemas_user_response import SchemasUserResponse
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
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # List users
        api_response = api_instance.list_users(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

### Return type

[**[SchemasUserResponse]**](SchemasUserResponse.md)

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

# **update_customer**
> CustomerResponse update_customer(customer_id)

Update a customer

Update a customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_api
from fastly.model.customer_response import CustomerResponse
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
    api_instance = customer_api.CustomerApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    billing_contact_id = "billing_contact_id_example" # str, none_type | The alphanumeric string representing the primary billing contact. (optional)
    billing_network_type = "public" # str | Customer's current network revenue type. (optional)
    billing_ref = "billing_ref_example" # str, none_type | Used for adding purchased orders to customer's account. (optional)
    can_configure_wordpress = True # bool, none_type | Whether this customer can view or edit wordpress. (optional)
    can_reset_passwords = True # bool | Whether this customer can reset passwords. (optional)
    can_upload_vcl = True # bool | Whether this customer can upload VCL. (optional)
    force_2fa = True # bool | Specifies whether 2FA is forced or not forced on the customer account. Logs out non-2FA users once 2FA is force enabled. (optional)
    force_sso = True # bool | Specifies whether SSO is forced or not forced on the customer account. (optional)
    has_account_panel = True # bool | Specifies whether the account has access or does not have access to the account panel. (optional)
    has_improved_events = True # bool | Specifies whether the account has access or does not have access to the improved events. (optional)
    has_improved_ssl_config = True # bool | Whether this customer can view or edit the SSL config. (optional)
    has_openstack_logging = True # bool | Specifies whether the account has enabled or not enabled openstack logging. (optional)
    has_pci = True # bool | Specifies whether the account can edit PCI for a service. (optional)
    has_pci_passwords = True # bool | Specifies whether PCI passwords are required for the account. (optional)
    ip_whitelist = "ip_whitelist_example" # str | The range of IP addresses authorized to access the customer account. (optional)
    legal_contact_id = "legal_contact_id_example" # str, none_type | The alphanumeric string identifying the account's legal contact. (optional)
    name = "name_example" # str | The name of the customer, generally the company name. (optional)
    owner_id = "owner_id_example" # str | The alphanumeric string identifying the account owner. (optional)
    phone_number = "phone_number_example" # str | The phone number associated with the account. (optional)
    postal_address = "postal_address_example" # str, none_type | The postal address associated with the account. (optional)
    pricing_plan = "pricing_plan_example" # str | The pricing plan this customer is under. (optional)
    pricing_plan_id = "pricing_plan_id_example" # str | The alphanumeric string identifying the pricing plan. (optional)
    security_contact_id = "security_contact_id_example" # str, none_type | The alphanumeric string identifying the account's security contact. (optional)
    technical_contact_id = "technical_contact_id_example" # str, none_type | The alphanumeric string identifying the account's technical contact. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a customer
        api_response = api_instance.update_customer(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerApi->update_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a customer
        api_response = api_instance.update_customer(customer_id, billing_contact_id=billing_contact_id, billing_network_type=billing_network_type, billing_ref=billing_ref, can_configure_wordpress=can_configure_wordpress, can_reset_passwords=can_reset_passwords, can_upload_vcl=can_upload_vcl, force_2fa=force_2fa, force_sso=force_sso, has_account_panel=has_account_panel, has_improved_events=has_improved_events, has_improved_ssl_config=has_improved_ssl_config, has_openstack_logging=has_openstack_logging, has_pci=has_pci, has_pci_passwords=has_pci_passwords, ip_whitelist=ip_whitelist, legal_contact_id=legal_contact_id, name=name, owner_id=owner_id, phone_number=phone_number, postal_address=postal_address, pricing_plan=pricing_plan, pricing_plan_id=pricing_plan_id, security_contact_id=security_contact_id, technical_contact_id=technical_contact_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerApi->update_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **billing_contact_id** | **str, none_type**| The alphanumeric string representing the primary billing contact. | [optional]
 **billing_network_type** | **str**| Customer&#39;s current network revenue type. | [optional]
 **billing_ref** | **str, none_type**| Used for adding purchased orders to customer&#39;s account. | [optional]
 **can_configure_wordpress** | **bool, none_type**| Whether this customer can view or edit wordpress. | [optional]
 **can_reset_passwords** | **bool**| Whether this customer can reset passwords. | [optional]
 **can_upload_vcl** | **bool**| Whether this customer can upload VCL. | [optional]
 **force_2fa** | **bool**| Specifies whether 2FA is forced or not forced on the customer account. Logs out non-2FA users once 2FA is force enabled. | [optional]
 **force_sso** | **bool**| Specifies whether SSO is forced or not forced on the customer account. | [optional]
 **has_account_panel** | **bool**| Specifies whether the account has access or does not have access to the account panel. | [optional]
 **has_improved_events** | **bool**| Specifies whether the account has access or does not have access to the improved events. | [optional]
 **has_improved_ssl_config** | **bool**| Whether this customer can view or edit the SSL config. | [optional]
 **has_openstack_logging** | **bool**| Specifies whether the account has enabled or not enabled openstack logging. | [optional]
 **has_pci** | **bool**| Specifies whether the account can edit PCI for a service. | [optional]
 **has_pci_passwords** | **bool**| Specifies whether PCI passwords are required for the account. | [optional]
 **ip_whitelist** | **str**| The range of IP addresses authorized to access the customer account. | [optional]
 **legal_contact_id** | **str, none_type**| The alphanumeric string identifying the account&#39;s legal contact. | [optional]
 **name** | **str**| The name of the customer, generally the company name. | [optional]
 **owner_id** | **str**| The alphanumeric string identifying the account owner. | [optional]
 **phone_number** | **str**| The phone number associated with the account. | [optional]
 **postal_address** | **str, none_type**| The postal address associated with the account. | [optional]
 **pricing_plan** | **str**| The pricing plan this customer is under. | [optional]
 **pricing_plan_id** | **str**| The alphanumeric string identifying the pricing plan. | [optional]
 **security_contact_id** | **str, none_type**| The alphanumeric string identifying the account&#39;s security contact. | [optional]
 **technical_contact_id** | **str, none_type**| The alphanumeric string identifying the account&#39;s technical contact. | [optional]

### Return type

[**CustomerResponse**](CustomerResponse.md)

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

