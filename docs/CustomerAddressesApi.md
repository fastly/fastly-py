# fastly.CustomerAddressesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_address**](CustomerAddressesApi.md#create_customer_address) | **POST** /billing/v3/customer-addresses | Creates an address associated with a customer account.
[**list_customer_addresses**](CustomerAddressesApi.md#list_customer_addresses) | **GET** /billing/v3/customer-addresses | Return the list of addresses associated with a customer account.
[**update_customer_address**](CustomerAddressesApi.md#update_customer_address) | **PUT** /billing/v3/customer-addresses/{type} | Updates an address associated with a customer account.


# **create_customer_address**
> InlineResponse201 create_customer_address(customer_address)

Creates an address associated with a customer account.

Creates an address associated with a customer account.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_addresses_api
from fastly.model.customer_address import CustomerAddress
from fastly.model.inline_response201 import InlineResponse201
from fastly.model.error import Error
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
    api_instance = customer_addresses_api.CustomerAddressesApi(api_client)
    customer_address = CustomerAddress(
        type="billing",
        address_1="address_1_example",
        address_2="address_2_example",
        locality="locality_example",
        region="region_example",
        country="country_example",
        postal_code="postal_code_example",
    ) # CustomerAddress | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an address associated with a customer account.
        api_response = api_instance.create_customer_address(customer_address)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerAddressesApi->create_customer_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_address** | [**CustomerAddress**](CustomerAddress.md)|  |

### Return type

[**InlineResponse201**](InlineResponse201.md)

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_addresses**
> ListCustomerAddressesResponse list_customer_addresses()

Return the list of addresses associated with a customer account.

Return the list of addresses associated with a customer account.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_addresses_api
from fastly.model.list_customer_addresses_response import ListCustomerAddressesResponse
from fastly.model.error import Error
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
    api_instance = customer_addresses_api.CustomerAddressesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Return the list of addresses associated with a customer account.
        api_response = api_instance.list_customer_addresses()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling CustomerAddressesApi->list_customer_addresses: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListCustomerAddressesResponse**](ListCustomerAddressesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_customer_address**
> update_customer_address(type, customer_address)

Updates an address associated with a customer account.

Updates an address associated with a customer account.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import customer_addresses_api
from fastly.model.customer_address import CustomerAddress
from fastly.model.error import Error
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
    api_instance = customer_addresses_api.CustomerAddressesApi(api_client)
    type = "billing" # str | Alphanumeric type of the address being modified.
    customer_address = CustomerAddress(
        type="billing",
        address_1="address_1_example",
        address_2="address_2_example",
        locality="locality_example",
        region="region_example",
        country="country_example",
        postal_code="postal_code_example",
    ) # CustomerAddress | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an address associated with a customer account.
        api_instance.update_customer_address(type, customer_address)
    except fastly.ApiException as e:
        print("Exception when calling CustomerAddressesApi->update_customer_address: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| Alphanumeric type of the address being modified. |
 **customer_address** | [**CustomerAddress**](CustomerAddress.md)|  |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

