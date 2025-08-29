# fastly.NgwafReportsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_attacks_report**](NgwafReportsApi.md#get_attacks_report) | **GET** /ngwaf/v1/reports/attacks | Get attacks report
[**get_signals_report**](NgwafReportsApi.md#get_signals_report) | **GET** /ngwaf/v1/reports/signals | Get signals report


# **get_attacks_report**
> ListAttackReport get_attacks_report(_from)

Get attacks report

Get attacks report

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ngwaf_reports_api
from fastly.model.list_attack_report import ListAttackReport
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
    api_instance = ngwaf_reports_api.NgwafReportsApi(api_client)
    _from = dateutil_parser('2019-08-20T18:07:33Z') # datetime | The start of a time range in RFC 3339 format.
    to = dateutil_parser('2019-08-21T18:07:33Z') # datetime | The end of a time range in RFC 3339 format. Defaults to the current time. (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get attacks report
        api_response = api_instance.get_attacks_report(_from)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NgwafReportsApi->get_attacks_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get attacks report
        api_response = api_instance.get_attacks_report(_from, to=to)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NgwafReportsApi->get_attacks_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| The start of a time range in RFC 3339 format. |
 **to** | **datetime**| The end of a time range in RFC 3339 format. Defaults to the current time. | [optional]

### Return type

[**ListAttackReport**](ListAttackReport.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with attack reports. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_signals_report**
> ListSignalReport get_signals_report(_from)

Get signals report

Get signals report

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ngwaf_reports_api
from fastly.model.list_signal_report import ListSignalReport
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
    api_instance = ngwaf_reports_api.NgwafReportsApi(api_client)
    _from = dateutil_parser('2019-08-20T18:07:33Z') # datetime | The start of a time range in RFC 3339 format.
    to = dateutil_parser('2019-08-21T18:07:33Z') # datetime | The end of a time range in RFC 3339 format. Defaults to the current time. (optional)
    signal_type = "all" # str | The type of signal (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get signals report
        api_response = api_instance.get_signals_report(_from)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NgwafReportsApi->get_signals_report: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get signals report
        api_response = api_instance.get_signals_report(_from, to=to, signal_type=signal_type)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NgwafReportsApi->get_signals_report: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| The start of a time range in RFC 3339 format. |
 **to** | **datetime**| The end of a time range in RFC 3339 format. Defaults to the current time. | [optional]
 **signal_type** | **str**| The type of signal | [optional]

### Return type

[**ListSignalReport**](ListSignalReport.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response with signals report. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

