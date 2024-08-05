# fastly.BillingUsageMetricsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_level_usage**](BillingUsageMetricsApi.md#get_service_level_usage) | **GET** /billing/v2/account_customers/{customer_id}/service-usage-metrics | Retrieve service-level usage metrics for a product.
[**get_service_level_usage_types**](BillingUsageMetricsApi.md#get_service_level_usage_types) | **GET** /billing/v2/account_customers/{customer_id}/service-usage-types | Retrieve product usage types for a customer.


# **get_service_level_usage**
> Serviceusagemetrics get_service_level_usage(customer_id, product_id, usage_type_name, time_granularity)

Retrieve service-level usage metrics for a product.

Returns product usage, broken down by service.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_usage_metrics_api
from fastly.model.serviceusagemetrics import Serviceusagemetrics
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
    api_instance = billing_usage_metrics_api.BillingUsageMetricsApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.
    product_id = "product_id_example" # str | The product identifier for the metrics returned (e.g., `cdn_usage`). This field is not required for CSV requests.
    usage_type_name = "usage_type_name_example" # str | The usage type name for the metrics returned (e.g., `North America Requests`). This field is not required for CSV requests.
    time_granularity = "month" # str | 
    start_date = "2023-01-01" # str |  (optional)
    end_date = "2023-01-31" # str |  (optional)
    start_month = "2023-01" # str |  (optional)
    end_month = "2023-03" # str |  (optional)
    limit = "5" # str | Number of results per page. The maximum is 100. (optional) if omitted the server will use the default value of "5"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve service-level usage metrics for a product.
        api_response = api_instance.get_service_level_usage(customer_id, product_id, usage_type_name, time_granularity)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingUsageMetricsApi->get_service_level_usage: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve service-level usage metrics for a product.
        api_response = api_instance.get_service_level_usage(customer_id, product_id, usage_type_name, time_granularity, start_date=start_date, end_date=end_date, start_month=start_month, end_month=end_month, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingUsageMetricsApi->get_service_level_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |
 **product_id** | **str**| The product identifier for the metrics returned (e.g., `cdn_usage`). This field is not required for CSV requests. |
 **usage_type_name** | **str**| The usage type name for the metrics returned (e.g., `North America Requests`). This field is not required for CSV requests. |
 **time_granularity** | **str**|  |
 **start_date** | **str**|  | [optional]
 **end_date** | **str**|  | [optional]
 **start_month** | **str**|  | [optional]
 **end_month** | **str**|  | [optional]
 **limit** | **str**| Number of results per page. The maximum is 100. | [optional] if omitted the server will use the default value of "5"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]

### Return type

[**Serviceusagemetrics**](Serviceusagemetrics.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing usage elements. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_level_usage_types**
> Serviceusagetypes get_service_level_usage_types(customer_id)

Retrieve product usage types for a customer.

Returns product usage types reported by the customer's services.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_usage_metrics_api
from fastly.model.error import Error
from fastly.model.serviceusagetypes import Serviceusagetypes
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
    api_instance = billing_usage_metrics_api.BillingUsageMetricsApi(api_client)
    customer_id = "x4xCwxxJxGCx123Rx5xTx" # str | Alphanumeric string identifying the customer.

    # example passing only required values which don't have defaults set
    try:
        # Retrieve product usage types for a customer.
        api_response = api_instance.get_service_level_usage_types(customer_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingUsageMetricsApi->get_service_level_usage_types: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_id** | **str**| Alphanumeric string identifying the customer. |

### Return type

[**Serviceusagetypes**](Serviceusagetypes.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing usage elements. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

