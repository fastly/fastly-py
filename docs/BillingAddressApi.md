# fastly.BillingAddressApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_billing_addr**](BillingAddressApi.md#add_billing_addr) | **POST** /customer/{customer_id}/billing_address | Add a billing address to a customer
[**delete_billing_addr**](BillingAddressApi.md#delete_billing_addr) | **DELETE** /customer/{customer_id}/billing_address | Delete a billing address
[**get_billing_addr**](BillingAddressApi.md#get_billing_addr) | **GET** /customer/{customer_id}/billing_address | Get a billing address
[**update_billing_addr**](BillingAddressApi.md#update_billing_addr) | **PATCH** /customer/{customer_id}/billing_address | Update a billing address


# **add_billing_addr**
> BillingAddressResponse add_billing_addr(customer_id)

Add a billing address to a customer

Add a billing address to a customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_address_api
from fastly.model.billing_address_verification_error_response import BillingAddressVerificationErrorResponse
from fastly.model.billing_address_request import BillingAddressRequest
from fastly.model.billing_address_response import BillingAddressResponse
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
    api_instance = billing_address_api.BillingAddressApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    billing_address_request = BillingAddressRequest(
        skip_verification=True,
        data=BillingAddressRequestData(
            type=TypeBillingAddress("billing_address"),
            attributes=BillingAddressAttributes(
                address_1="80719 Dorothea Mountain",
                address_2="Apt. 652",
                city="New Rasheedville",
                country="US",
                locality="New Castle",
                postal_code="53538-5902",
                state="DE",
            ),
        ),
    ) # BillingAddressRequest | Billing address (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a billing address to a customer
        api_response = api_instance.add_billing_addr(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingAddressApi->add_billing_addr: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a billing address to a customer
        api_response = api_instance.add_billing_addr(customer_id, billing_address_request=billing_address_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingAddressApi->add_billing_addr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **billing_address_request** | [**BillingAddressRequest**](BillingAddressRequest.md)| Billing address | [optional]

### Return type

[**BillingAddressResponse**](BillingAddressResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Could not validate address |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_billing_addr**
> delete_billing_addr(customer_id)

Delete a billing address

Delete a customer's billing address.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_address_api
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
    api_instance = billing_address_api.BillingAddressApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # Delete a billing address
        api_instance.delete_billing_addr(customer_id)
    except fastly.ApiException as e:
        print("Exception when calling BillingAddressApi->delete_billing_addr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

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

# **get_billing_addr**
> BillingAddressResponse get_billing_addr(customer_id)

Get a billing address

Get a customer's billing address.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_address_api
from fastly.model.billing_address_response import BillingAddressResponse
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
    api_instance = billing_address_api.BillingAddressApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # Get a billing address
        api_response = api_instance.get_billing_addr(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingAddressApi->get_billing_addr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

### Return type

[**BillingAddressResponse**](BillingAddressResponse.md)

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

# **update_billing_addr**
> BillingAddressResponse update_billing_addr(customer_id)

Update a billing address

Update a customer's billing address. You may update only part of the customer's billing address.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_address_api
from fastly.model.billing_address_verification_error_response import BillingAddressVerificationErrorResponse
from fastly.model.update_billing_address_request import UpdateBillingAddressRequest
from fastly.model.billing_address_response import BillingAddressResponse
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
    api_instance = billing_address_api.BillingAddressApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    update_billing_address_request = UpdateBillingAddressRequest(
        skip_verification=True,
        data=UpdateBillingAddressRequestData(
            type=TypeBillingAddress("billing_address"),
            attributes=BillingAddressAttributes(
                address_1="80719 Dorothea Mountain",
                address_2="Apt. 652",
                city="New Rasheedville",
                country="US",
                locality="New Castle",
                postal_code="53538-5902",
                state="DE",
            ),
        ),
    ) # UpdateBillingAddressRequest | One or more billing address attributes (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a billing address
        api_response = api_instance.update_billing_addr(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingAddressApi->update_billing_addr: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a billing address
        api_response = api_instance.update_billing_addr(customer_id, update_billing_address_request=update_billing_address_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingAddressApi->update_billing_addr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **update_billing_address_request** | [**UpdateBillingAddressRequest**](UpdateBillingAddressRequest.md)| One or more billing address attributes | [optional]

### Return type

[**BillingAddressResponse**](BillingAddressResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Could not validate address |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

