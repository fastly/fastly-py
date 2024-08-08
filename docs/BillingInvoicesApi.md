# fastly.BillingInvoicesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_by_invoice_id**](BillingInvoicesApi.md#get_invoice_by_invoice_id) | **GET** /billing/v3/invoices/{invoice_id} | Get invoice by ID.
[**get_month_to_date_invoice**](BillingInvoicesApi.md#get_month_to_date_invoice) | **GET** /billing/v3/invoices/month-to-date | Get month-to-date invoice.
[**list_invoices**](BillingInvoicesApi.md#list_invoices) | **GET** /billing/v3/invoices | List of invoices.


# **get_invoice_by_invoice_id**
> EomInvoiceResponse get_invoice_by_invoice_id(invoice_id)

Get invoice by ID.

Returns invoice associated with the invoice id.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_invoices_api
from fastly.model.eom_invoice_response import EomInvoiceResponse
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
    api_instance = billing_invoices_api.BillingInvoicesApi(api_client)
    invoice_id = 4183280 # int | 

    # example passing only required values which don't have defaults set
    try:
        # Get invoice by ID.
        api_response = api_instance.get_invoice_by_invoice_id(invoice_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingInvoicesApi->get_invoice_by_invoice_id: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **int**|  |

### Return type

[**EomInvoiceResponse**](EomInvoiceResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_month_to_date_invoice**
> MtdInvoiceResponse get_month_to_date_invoice()

Get month-to-date invoice.

Returns month-to-date invoice for the current month.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_invoices_api
from fastly.model.mtd_invoice_response import MtdInvoiceResponse
from fastly.model.error import Error
from fastly.model.async_response import AsyncResponse
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
    api_instance = billing_invoices_api.BillingInvoicesApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get month-to-date invoice.
        api_response = api_instance.get_month_to_date_invoice()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingInvoicesApi->get_month_to_date_invoice: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**MtdInvoiceResponse**](MtdInvoiceResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**202** | Accepted |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_invoices**
> ListEomInvoicesResponse list_invoices()

List of invoices.

Returns the list of invoices, sorted by billing start date (newest to oldest).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_invoices_api
from fastly.model.list_eom_invoices_response import ListEomInvoicesResponse
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
    api_instance = billing_invoices_api.BillingInvoicesApi(api_client)
    billing_start_date = "2023-01-01" # str |  (optional)
    billing_end_date = "2023-01-31" # str |  (optional)
    limit = "100" # str | Number of results per page. The maximum is 200. (optional) if omitted the server will use the default value of "100"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List of invoices.
        api_response = api_instance.list_invoices(billing_start_date=billing_start_date, billing_end_date=billing_end_date, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingInvoicesApi->list_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **billing_start_date** | **str**|  | [optional]
 **billing_end_date** | **str**|  | [optional]
 **limit** | **str**| Number of results per page. The maximum is 200. | [optional] if omitted the server will use the default value of "100"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]

### Return type

[**ListEomInvoicesResponse**](ListEomInvoicesResponse.md)

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
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

