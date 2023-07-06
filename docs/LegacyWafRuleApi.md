# fastly.LegacyWafRuleApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_legacy_waf_firewall_rule_vcl**](LegacyWafRuleApi.md#get_legacy_waf_firewall_rule_vcl) | **GET** /wafs/{firewall_id}/rules/{waf_rule_id}/vcl | Get VCL for a rule associated with a firewall
[**get_legacy_waf_rule**](LegacyWafRuleApi.md#get_legacy_waf_rule) | **GET** /wafs/rules/{waf_rule_id} | Get a rule
[**get_legacy_waf_rule_vcl**](LegacyWafRuleApi.md#get_legacy_waf_rule_vcl) | **GET** /wafs/rules/{waf_rule_id}/vcl | Get VCL for a rule
[**list_legacy_waf_rules**](LegacyWafRuleApi.md#list_legacy_waf_rules) | **GET** /wafs/rules | List rules in the latest configuration set


# **get_legacy_waf_firewall_rule_vcl**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_legacy_waf_firewall_rule_vcl(firewall_id, waf_rule_id)

Get VCL for a rule associated with a firewall

Get associated VCL for a specific rule associated with a specific firewall.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_api
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
    api_instance = legacy_waf_rule_api.LegacyWafRuleApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.

    # example passing only required values which don't have defaults set
    try:
        # Get VCL for a rule associated with a firewall
        api_response = api_instance.get_legacy_waf_firewall_rule_vcl(firewall_id, waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleApi->get_legacy_waf_firewall_rule_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |

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

# **get_legacy_waf_rule**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_legacy_waf_rule(waf_rule_id)

Get a rule

Get a specific rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_api
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
    api_instance = legacy_waf_rule_api.LegacyWafRuleApi(api_client)
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    filter_configuration_set_id = "filter[configuration_set_id]_example" # str | Optional. Limit rule to a specific configuration set or pass \"all\" to search all configuration sets, including stale ones. (optional)
    include = "tags" # str | Include relationships. Optional. Comma separated values. Permitted values: `tags`, `rule_statuses`, `source`, and `vcl`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a rule
        api_response = api_instance.get_legacy_waf_rule(waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleApi->get_legacy_waf_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a rule
        api_response = api_instance.get_legacy_waf_rule(waf_rule_id, filter_configuration_set_id=filter_configuration_set_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleApi->get_legacy_waf_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
 **filter_configuration_set_id** | **str**| Optional. Limit rule to a specific configuration set or pass \&quot;all\&quot; to search all configuration sets, including stale ones. | [optional]
 **include** | **str**| Include relationships. Optional. Comma separated values. Permitted values: `tags`, `rule_statuses`, `source`, and `vcl`.  | [optional]

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

# **get_legacy_waf_rule_vcl**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_legacy_waf_rule_vcl(waf_rule_id)

Get VCL for a rule

Get associated VCL for a specific rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_api
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
    api_instance = legacy_waf_rule_api.LegacyWafRuleApi(api_client)
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.

    # example passing only required values which don't have defaults set
    try:
        # Get VCL for a rule
        api_response = api_instance.get_legacy_waf_rule_vcl(waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleApi->get_legacy_waf_rule_vcl: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |

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

# **list_legacy_waf_rules**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_legacy_waf_rules()

List rules in the latest configuration set

List all rules in the latest configuration set.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_api
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
    api_instance = legacy_waf_rule_api.LegacyWafRuleApi(api_client)
    filter_rule_id = "filter[rule_id]_example" # str | Limit the returned rules to a specific rule ID. (optional)
    filter_severity = "filter[severity]_example" # str | Limit the returned rules to a specific severity. (optional)
    filter_tags_name = "filter[tags][name]_example" # str | Limit the returned rules to a set linked to a tag by name. (optional)
    filter_configuration_set_id = "filter[configuration_set_id]_example" # str | Optional. Limit rules to specific configuration set or pass \"all\" to search all configuration sets, including stale ones. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "include_example" # str | Include relationships. Optional. Comma separated values. Permitted values: `tags`, `rule_statuses`, and `source`.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List rules in the latest configuration set
        api_response = api_instance.list_legacy_waf_rules(filter_rule_id=filter_rule_id, filter_severity=filter_severity, filter_tags_name=filter_tags_name, filter_configuration_set_id=filter_configuration_set_id, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleApi->list_legacy_waf_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_rule_id** | **str**| Limit the returned rules to a specific rule ID. | [optional]
 **filter_severity** | **str**| Limit the returned rules to a specific severity. | [optional]
 **filter_tags_name** | **str**| Limit the returned rules to a set linked to a tag by name. | [optional]
 **filter_configuration_set_id** | **str**| Optional. Limit rules to specific configuration set or pass \&quot;all\&quot; to search all configuration sets, including stale ones. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional. Comma separated values. Permitted values: `tags`, `rule_statuses`, and `source`.  | [optional]

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

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

