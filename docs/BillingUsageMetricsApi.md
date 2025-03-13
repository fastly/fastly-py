# fastly.BillingUsageMetricsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_level_usage**](BillingUsageMetricsApi.md#get_service_level_usage) | **GET** /billing/v3/service-usage-metrics | Retrieve service-level usage metrics for services with non-zero usage units.
[**get_usage_metrics**](BillingUsageMetricsApi.md#get_usage_metrics) | **GET** /billing/v3/usage-metrics | Get monthly usage metrics


# **get_service_level_usage**
> Serviceusagemetrics get_service_level_usage()

Retrieve service-level usage metrics for services with non-zero usage units.

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
    product_id = "product_id_example" # str | The product identifier for the metrics returned (e.g., `cdn_usage`). This should be used along with `usage_type_name`. (optional)
    service = "service_example" # str | The service identifier for the metrics being requested. (optional)
    usage_type_name = "usage_type_name_example" # str | The usage type name for the metrics returned (e.g., `North America Requests`). This should be used along with `product_id`. (optional)
    start_month = "2023-01" # str |  (optional)
    end_month = "2023-03" # str |  (optional)
    limit = "1000" # str | Number of results per page. The maximum is 10000. (optional) if omitted the server will use the default value of "1000"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve service-level usage metrics for services with non-zero usage units.
        api_response = api_instance.get_service_level_usage(product_id=product_id, service=service, usage_type_name=usage_type_name, start_month=start_month, end_month=end_month, limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingUsageMetricsApi->get_service_level_usage: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **str**| The product identifier for the metrics returned (e.g., `cdn_usage`). This should be used along with `usage_type_name`. | [optional]
 **service** | **str**| The service identifier for the metrics being requested. | [optional]
 **usage_type_name** | **str**| The usage type name for the metrics returned (e.g., `North America Requests`). This should be used along with `product_id`. | [optional]
 **start_month** | **str**|  | [optional]
 **end_month** | **str**|  | [optional]
 **limit** | **str**| Number of results per page. The maximum is 10000. | [optional] if omitted the server will use the default value of "1000"
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

# **get_usage_metrics**
> Usagemetric get_usage_metrics(start_month, end_month)

Get monthly usage metrics

Returns monthly usage metrics for customer by product.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import billing_usage_metrics_api
from fastly.model.error import Error
from fastly.model.usagemetric import Usagemetric
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
    start_month = "2024-05" # str | 
    end_month = "2024-06" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get monthly usage metrics
        api_response = api_instance.get_usage_metrics(start_month, end_month)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling BillingUsageMetricsApi->get_usage_metrics: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_month** | **str**|  |
 **end_month** | **str**|  |

### Return type

[**Usagemetric**](Usagemetric.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A response containing usage metric elements. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

