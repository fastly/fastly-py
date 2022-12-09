# fastly.BillingApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice**](BillingApi.md#get_invoice) | **GET** /billing/v2/year/{year}/month/{month} | Get an invoice
[**get_invoice_by_id**](BillingApi.md#get_invoice_by_id) | **GET** /billing/v2/account_customers/{customer_id}/invoices/{invoice_id} | Get an invoice
[**get_invoice_mtd**](BillingApi.md#get_invoice_mtd) | **GET** /billing/v2/account_customers/{customer_id}/mtd_invoice | Get month-to-date billing estimate


# **get_invoice**
> BillingResponse get_invoice(month, year)

Get an invoice

Get the invoice for a given year and month. Can be any month from when the Customer was created to the current month.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_api
from fastly.model.billing_response import BillingResponse
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
    api_instance = billing_api.BillingApi(api_client)
    month = "05" # str | 2-digit month.
    year = "2020" # str | 4-digit year.

    # example passing only required values which don't have defaults set
    try:
        # Get an invoice
        api_response = api_instance.get_invoice(month, year)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingApi->get_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **month** | **str**| 2-digit month. |
 **year** | **str**| 4-digit year. |

### Return type

[**BillingResponse**](BillingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_by_id**
> BillingResponse get_invoice_by_id(customer_id, invoice_id)

Get an invoice

Get the invoice for the given invoice_id.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_api
from fastly.model.billing_response import BillingResponse
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
    api_instance = billing_api.BillingApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    invoice_id = "7SlAESxcJ2zxHOV4gQ9y9X" # str | Alphanumeric string identifying the invoice.

    # example passing only required values which don't have defaults set
    try:
        # Get an invoice
        api_response = api_instance.get_invoice_by_id(customer_id, invoice_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingApi->get_invoice_by_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **invoice_id** | **str**| Alphanumeric string identifying the invoice. |

### Return type

[**BillingResponse**](BillingResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/csv, application/pdf


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_mtd**
> BillingEstimateResponse get_invoice_mtd(customer_id)

Get month-to-date billing estimate

Get the current month-to-date estimate. This endpoint has two different responses. Under normal circumstances, it generally takes less than 5 seconds to generate but in certain cases can take up to 60 seconds. Once generated the month-to-date estimate is cached for 4 hours, and is available the next request will return the JSON representation of the month-to-date estimate. While a report is being generated in the background, this endpoint will return a `202 Accepted` response. The full format of which can be found in detail in our [billing calculation guide](https://docs.fastly.com/en/guides/how-we-calculate-your-bill). There are certain accounts for which we are unable to generate a month-to-date estimate. For example, accounts who have parent-pay are unable to generate an MTD estimate. The parent accounts are able to generate a month-to-date estimate but that estimate will not include the child accounts amounts at this time.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_api
from fastly.model.billing_estimate_response import BillingEstimateResponse
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
    api_instance = billing_api.BillingApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    month = "05" # str | 2-digit month. (optional)
    year = "2020" # str | 4-digit year. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get month-to-date billing estimate
        api_response = api_instance.get_invoice_mtd(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingApi->get_invoice_mtd: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get month-to-date billing estimate
        api_response = api_instance.get_invoice_mtd(customer_id, month=month, year=year)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingApi->get_invoice_mtd: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **month** | **str**| 2-digit month. | [optional]
 **year** | **str**| 4-digit year. | [optional]

### Return type

[**BillingEstimateResponse**](BillingEstimateResponse.md)

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

