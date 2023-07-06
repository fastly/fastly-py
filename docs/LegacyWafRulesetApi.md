# fastly.LegacyWafRulesetApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_waf_ruleset**](LegacyWafRulesetApi.md#get_waf_ruleset) | **GET** /service/{service_id}/wafs/{firewall_id}/ruleset | Get a WAF ruleset
[**get_waf_ruleset_vcl**](LegacyWafRulesetApi.md#get_waf_ruleset_vcl) | **GET** /service/{service_id}/wafs/{firewall_id}/ruleset/preview | Generate WAF ruleset VCL
[**update_waf_ruleset**](LegacyWafRulesetApi.md#update_waf_ruleset) | **PATCH** /service/{service_id}/wafs/{firewall_id}/ruleset | Update a WAF ruleset


# **get_waf_ruleset**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_waf_ruleset(service_id, firewall_id)

Get a WAF ruleset

Get a WAF ruleset for a particular service and firewall object.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_ruleset_api
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
    api_instance = legacy_waf_ruleset_api.LegacyWafRulesetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.

    # example passing only required values which don't have defaults set
    try:
        # Get a WAF ruleset
        api_response = api_instance.get_waf_ruleset(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRulesetApi->get_waf_ruleset: %s\n" % e)
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

# **get_waf_ruleset_vcl**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_waf_ruleset_vcl(service_id, firewall_id)

Generate WAF ruleset VCL

Get a preview of the WAF ruleset VCL for a particular service and firewall object based on changes to WAF configuration before deploying the ruleset. The response will include a link to status of the background VCL generation job. Once the background job is completed, the preview WAF ruleset VCL can be retrieved from the status response.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_ruleset_api
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
    api_instance = legacy_waf_ruleset_api.LegacyWafRulesetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.

    # example passing only required values which don't have defaults set
    try:
        # Generate WAF ruleset VCL
        api_response = api_instance.get_waf_ruleset_vcl(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRulesetApi->get_waf_ruleset_vcl: %s\n" % e)
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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_waf_ruleset**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_waf_ruleset(service_id, firewall_id)

Update a WAF ruleset

Update the WAF ruleset for a particular service and firewall object. Use the URL in the response to view the WAF ruleset deploy status.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_ruleset_api
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
    api_instance = legacy_waf_ruleset_api.LegacyWafRulesetApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a WAF ruleset
        api_response = api_instance.update_waf_ruleset(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRulesetApi->update_waf_ruleset: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a WAF ruleset
        api_response = api_instance.update_waf_ruleset(service_id, firewall_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRulesetApi->update_waf_ruleset: %s\n" % e)
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
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

