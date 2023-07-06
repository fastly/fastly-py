# fastly.LegacyWafOwaspApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_owasp_settings**](LegacyWafOwaspApi.md#create_owasp_settings) | **POST** /service/{service_id}/wafs/{firewall_id}/owasp | Create an OWASP settings object
[**get_owasp_settings**](LegacyWafOwaspApi.md#get_owasp_settings) | **GET** /service/{service_id}/wafs/{firewall_id}/owasp | Get the OWASP settings object
[**update_owasp_settings**](LegacyWafOwaspApi.md#update_owasp_settings) | **PATCH** /service/{service_id}/wafs/{firewall_id}/owasp | Update the OWASP settings object


# **create_owasp_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_owasp_settings(service_id, firewall_id)

Create an OWASP settings object

Create an OWASP settings object for a particular service and firewall.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_owasp_api
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
    api_instance = legacy_waf_owasp_api.LegacyWafOwaspApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create an OWASP settings object
        api_response = api_instance.create_owasp_settings(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafOwaspApi->create_owasp_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an OWASP settings object
        api_response = api_instance.create_owasp_settings(service_id, firewall_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafOwaspApi->create_owasp_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_owasp_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_owasp_settings(service_id, firewall_id)

Get the OWASP settings object

Get the OWASP settings object for a particular service and firewall.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_owasp_api
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
    api_instance = legacy_waf_owasp_api.LegacyWafOwaspApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.

    # example passing only required values which don't have defaults set
    try:
        # Get the OWASP settings object
        api_response = api_instance.get_owasp_settings(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafOwaspApi->get_owasp_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |

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

# **update_owasp_settings**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_owasp_settings(service_id, firewall_id)

Update the OWASP settings object

Update the OWASP settings object for a particular service and firewall.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_owasp_api
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
    api_instance = legacy_waf_owasp_api.LegacyWafOwaspApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the OWASP settings object
        api_response = api_instance.update_owasp_settings(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafOwaspApi->update_owasp_settings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the OWASP settings object
        api_response = api_instance.update_owasp_settings(service_id, firewall_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafOwaspApi->update_owasp_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

