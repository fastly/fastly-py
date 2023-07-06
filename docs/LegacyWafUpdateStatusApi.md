# fastly.LegacyWafUpdateStatusApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_waf_update_status**](LegacyWafUpdateStatusApi.md#get_waf_update_status) | **GET** /service/{service_id}/wafs/{firewall_id}/update_statuses/{update_status_id} | Get the status of a WAF update
[**list_waf_update_statuses**](LegacyWafUpdateStatusApi.md#list_waf_update_statuses) | **GET** /service/{service_id}/wafs/{firewall_id}/update_statuses | List update statuses


# **get_waf_update_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_waf_update_status(service_id, firewall_id, update_status_id)

Get the status of a WAF update

Get a specific update status object for a particular service and firewall object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_update_status_api
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
    api_instance = legacy_waf_update_status_api.LegacyWafUpdateStatusApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    update_status_id = "Up5SguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a WAF update status.

    # example passing only required values which don't have defaults set
    try:
        # Get the status of a WAF update
        api_response = api_instance.get_waf_update_status(service_id, firewall_id, update_status_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafUpdateStatusApi->get_waf_update_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **update_status_id** | **str**| Alphanumeric string identifying a WAF update status. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **list_waf_update_statuses**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_waf_update_statuses(service_id, firewall_id)

List update statuses

List all update statuses for a particular service and firewall object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_update_status_api
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
    api_instance = legacy_waf_update_status_api.LegacyWafUpdateStatusApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "waf" # str | Include relationships. Optional, comma separated values. Permitted values: `waf`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # List update statuses
        api_response = api_instance.list_waf_update_statuses(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafUpdateStatusApi->list_waf_update_statuses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List update statuses
        api_response = api_instance.list_waf_update_statuses(service_id, firewall_id, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafUpdateStatusApi->list_waf_update_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional, comma separated values. Permitted values: `waf`.  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

