# fastly.LegacyWafRuleStatusApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_waf_firewall_rule_status**](LegacyWafRuleStatusApi.md#get_waf_firewall_rule_status) | **GET** /service/{service_id}/wafs/{firewall_id}/rules/{waf_rule_id}/rule_status | Get the status of a rule on a firewall
[**list_waf_firewall_rule_statuses**](LegacyWafRuleStatusApi.md#list_waf_firewall_rule_statuses) | **GET** /service/{service_id}/wafs/{firewall_id}/rule_statuses | List rule statuses
[**update_waf_firewall_rule_status**](LegacyWafRuleStatusApi.md#update_waf_firewall_rule_status) | **PATCH** /service/{service_id}/wafs/{firewall_id}/rules/{waf_rule_id}/rule_status | Update the status of a rule
[**update_waf_firewall_rule_statuses_tag**](LegacyWafRuleStatusApi.md#update_waf_firewall_rule_statuses_tag) | **POST** /service/{service_id}/wafs/{firewall_id}/rule_statuses | Create or update status of a tagged group of rules


# **get_waf_firewall_rule_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id)

Get the status of a rule on a firewall

Get a specific rule status object for a particular service, firewall, and rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_status_api
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
    api_instance = legacy_waf_rule_status_api.LegacyWafRuleStatusApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.

    # example passing only required values which don't have defaults set
    try:
        # Get the status of a rule on a firewall
        api_response = api_instance.get_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->get_waf_firewall_rule_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
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

# **list_waf_firewall_rule_statuses**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_waf_firewall_rule_statuses(service_id, firewall_id)

List rule statuses

List all rule statuses for a particular service and firewall.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_status_api
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
    api_instance = legacy_waf_rule_status_api.LegacyWafRuleStatusApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    filter_status = "filter[status]_example" # str | Limit results to rule statuses with the specified status. (optional)
    filter_rule_message = "filter[rule][message]_example" # str | Limit results to rule statuses whose rules have the specified message. (optional)
    filter_rule_rule_id = "filter[rule][rule_id]_example" # str | Limit results to rule statuses whose rules represent the specified ModSecurity rule_id. (optional)
    filter_rule_tags = "filter[rule][tags]_example" # str | Limit results to rule statuses whose rules relate to the specified tag IDs. (optional)
    filter_rule_tags_name = "application-FBC Market" # str | Limit results to rule statuses whose rules related to the named tags. (optional)
    include = "include_example" # str | Include relationships. Optional, comma separated values. Permitted values: `tags`.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List rule statuses
        api_response = api_instance.list_waf_firewall_rule_statuses(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->list_waf_firewall_rule_statuses: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List rule statuses
        api_response = api_instance.list_waf_firewall_rule_statuses(service_id, firewall_id, filter_status=filter_status, filter_rule_message=filter_rule_message, filter_rule_rule_id=filter_rule_rule_id, filter_rule_tags=filter_rule_tags, filter_rule_tags_name=filter_rule_tags_name, include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->list_waf_firewall_rule_statuses: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **filter_status** | **str**| Limit results to rule statuses with the specified status. | [optional]
 **filter_rule_message** | **str**| Limit results to rule statuses whose rules have the specified message. | [optional]
 **filter_rule_rule_id** | **str**| Limit results to rule statuses whose rules represent the specified ModSecurity rule_id. | [optional]
 **filter_rule_tags** | **str**| Limit results to rule statuses whose rules relate to the specified tag IDs. | [optional]
 **filter_rule_tags_name** | **str**| Limit results to rule statuses whose rules related to the named tags. | [optional]
 **include** | **str**| Include relationships. Optional, comma separated values. Permitted values: `tags`.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

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

# **update_waf_firewall_rule_status**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id)

Update the status of a rule

Update a rule status for a particular service, firewall, and rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_status_api
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
    api_instance = legacy_waf_rule_status_api.LegacyWafRuleStatusApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the status of a rule
        api_response = api_instance.update_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->update_waf_firewall_rule_status: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the status of a rule
        api_response = api_instance.update_waf_firewall_rule_status(service_id, firewall_id, waf_rule_id, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->update_waf_firewall_rule_status: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
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

# **update_waf_firewall_rule_statuses_tag**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} update_waf_firewall_rule_statuses_tag(service_id, firewall_id)

Create or update status of a tagged group of rules

Create or update all rule statuses for a particular service and firewall, based on tag name. By default, only rule status for enabled rules (with status log or block) will be updated. To update rule statuses for disabled rules under the specified tag, use the force attribute.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_rule_status_api
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
    api_instance = legacy_waf_rule_status_api.LegacyWafRuleStatusApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str | Alphanumeric string identifying the service.
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a Firewall.
    name = "name_example" # str | The tag name to use to determine the set of rules to update. For example, OWASP or language-php. (optional)
    force = "force_example" # str | Whether or not to update rule statuses for disabled rules. Optional. (optional)
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create or update status of a tagged group of rules
        api_response = api_instance.update_waf_firewall_rule_statuses_tag(service_id, firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->update_waf_firewall_rule_statuses_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create or update status of a tagged group of rules
        api_response = api_instance.update_waf_firewall_rule_statuses_tag(service_id, firewall_id, name=name, force=force, request_body=request_body)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafRuleStatusApi->update_waf_firewall_rule_statuses_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| Alphanumeric string identifying the service. |
 **firewall_id** | **str**| Alphanumeric string identifying a Firewall. |
 **name** | **str**| The tag name to use to determine the set of rules to update. For example, OWASP or language-php. | [optional]
 **force** | **str**| Whether or not to update rule statuses for disabled rules. Optional. | [optional]
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

