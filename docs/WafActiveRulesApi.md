# fastly.WafActiveRulesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_delete_waf_active_rules**](WafActiveRulesApi.md#bulk_delete_waf_active_rules) | **DELETE** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules | Delete multiple active rules from a WAF
[**bulk_update_waf_active_rules**](WafActiveRulesApi.md#bulk_update_waf_active_rules) | **PATCH** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/bulk | Update multiple active rules
[**create_waf_active_rule**](WafActiveRulesApi.md#create_waf_active_rule) | **POST** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules | Add a rule to a WAF as an active rule
[**create_waf_active_rules_tag**](WafActiveRulesApi.md#create_waf_active_rules_tag) | **POST** /waf/firewalls/{firewall_id}/versions/{version_id}/tags/{waf_tag_name}/active-rules | Create active rules by tag
[**delete_waf_active_rule**](WafActiveRulesApi.md#delete_waf_active_rule) | **DELETE** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id} | Delete an active rule
[**get_waf_active_rule**](WafActiveRulesApi.md#get_waf_active_rule) | **GET** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id} | Get an active WAF rule object
[**list_waf_active_rules**](WafActiveRulesApi.md#list_waf_active_rules) | **GET** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules | List active rules on a WAF
[**update_waf_active_rule**](WafActiveRulesApi.md#update_waf_active_rule) | **PATCH** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id} | Update an active rule


# **bulk_delete_waf_active_rules**
> bulk_delete_waf_active_rules(firewall_id, version_id)

Delete multiple active rules from a WAF

Delete many active rules on a particular firewall version using the active rule ID. Limited to 500 rules per request.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    request_body = {} # {str: (bool, date, datetime, dict, float, int, list, str, none_type)} |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Delete multiple active rules from a WAF
        api_instance.bulk_delete_waf_active_rules(firewall_id, version_id)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->bulk_delete_waf_active_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete multiple active rules from a WAF
        api_instance.bulk_delete_waf_active_rules(firewall_id, version_id, request_body=request_body)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->bulk_delete_waf_active_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **request_body** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json; ext=bulk
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_update_waf_active_rules**
> bulk_update_waf_active_rules(firewall_id, version_id)

Update multiple active rules

Bulk update all active rules on a [firewall version](https://www.fastly.com/documentation/reference/api/waf/firewall-version/). This endpoint will not add new active rules, only update existing active rules.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
from fastly.model.waf_active_rule_data import WafActiveRuleData
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    body = WafActiveRuleData(
        type=TypeWafActiveRule("waf_active_rule"),
        attributes=WafActiveRuleDataAttributes(
            modsec_rule_id=1,
            revision=WafRuleRevisionOrLatest(None),
            status="log",
        ),
        relationships=RelationshipsForWafActiveRule(),
    ) # WafActiveRuleData |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update multiple active rules
        api_instance.bulk_update_waf_active_rules(firewall_id, version_id)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->bulk_update_waf_active_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update multiple active rules
        api_instance.bulk_update_waf_active_rules(firewall_id, version_id, body=body)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->bulk_update_waf_active_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **body** | [**WafActiveRuleData**](WafActiveRuleData.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_waf_active_rule**
> WafActiveRuleCreationResponse create_waf_active_rule(firewall_id, version_id)

Add a rule to a WAF as an active rule

Create an active rule for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
from fastly.model.bulk_waf_active_rules import BulkWafActiveRules
from fastly.model.waf_active_rule_creation_response import WafActiveRuleCreationResponse
from fastly.model.waf_active_rule import WafActiveRule
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    waf_active_rule = WafActiveRule(
        data=WafActiveRuleData(
            type=TypeWafActiveRule("waf_active_rule"),
            attributes=WafActiveRuleDataAttributes(
                modsec_rule_id=1,
                revision=WafRuleRevisionOrLatest(None),
                status="log",
            ),
            relationships=RelationshipsForWafActiveRule(),
        ),
    ) # WafActiveRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Add a rule to a WAF as an active rule
        api_response = api_instance.create_waf_active_rule(firewall_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->create_waf_active_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Add a rule to a WAF as an active rule
        api_response = api_instance.create_waf_active_rule(firewall_id, version_id, waf_active_rule=waf_active_rule)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->create_waf_active_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **waf_active_rule** | [**WafActiveRule**](WafActiveRule.md)|  | [optional]

### Return type

[**WafActiveRuleCreationResponse**](WafActiveRuleCreationResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json, application/vnd.api+json; ext=bulk
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_waf_active_rules_tag**
> create_waf_active_rules_tag(firewall_id, version_id, waf_tag_name)

Create active rules by tag

Create active rules by tag. This endpoint will create active rules using the latest revision available for each rule.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
from fastly.model.waf_active_rule import WafActiveRule
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    waf_tag_name = "test-waf-tag" # str | Name of the tag.
    waf_active_rule = WafActiveRule(
        data=WafActiveRuleData(
            type=TypeWafActiveRule("waf_active_rule"),
            attributes=WafActiveRuleDataAttributes(
                modsec_rule_id=1,
                revision=WafRuleRevisionOrLatest(None),
                status="log",
            ),
            relationships=RelationshipsForWafActiveRule(),
        ),
    ) # WafActiveRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create active rules by tag
        api_instance.create_waf_active_rules_tag(firewall_id, version_id, waf_tag_name)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->create_waf_active_rules_tag: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create active rules by tag
        api_instance.create_waf_active_rules_tag(firewall_id, version_id, waf_tag_name, waf_active_rule=waf_active_rule)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->create_waf_active_rules_tag: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **waf_tag_name** | **str**| Name of the tag. |
 **waf_active_rule** | [**WafActiveRule**](WafActiveRule.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_waf_active_rule**
> delete_waf_active_rule(firewall_id, version_id, waf_rule_id)

Delete an active rule

Delete an active rule for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.

    # example passing only required values which don't have defaults set
    try:
        # Delete an active rule
        api_instance.delete_waf_active_rule(firewall_id, version_id, waf_rule_id)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->delete_waf_active_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_active_rule**
> WafActiveRuleResponse get_waf_active_rule(firewall_id, version_id, waf_rule_id)

Get an active WAF rule object

Get a specific active rule object. Includes details of the rule revision associated with the active rule object by default.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
from fastly.model.waf_active_rule_response import WafActiveRuleResponse
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    include = "waf_rule_revision,waf_firewall_version" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_rule_revision` and `waf_firewall_version`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get an active WAF rule object
        api_response = api_instance.get_waf_active_rule(firewall_id, version_id, waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->get_waf_active_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get an active WAF rule object
        api_response = api_instance.get_waf_active_rule(firewall_id, version_id, waf_rule_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->get_waf_active_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_rule_revision` and `waf_firewall_version`.  | [optional]

### Return type

[**WafActiveRuleResponse**](WafActiveRuleResponse.md)

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

# **list_waf_active_rules**
> WafActiveRulesResponse list_waf_active_rules(firewall_id, version_id)

List active rules on a WAF

List all active rules for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
from fastly.model.waf_active_rules_response import WafActiveRulesResponse
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    filter_status = "filter[status]_example" # str | Limit results to active rules with the specified status. (optional)
    filter_waf_rule_revision_message = "filter[waf_rule_revision][message]_example" # str | Limit results to active rules with the specified message. (optional)
    filter_waf_rule_revision_modsec_rule_id = "filter[waf_rule_revision][modsec_rule_id]_example" # str | Limit results to active rules that represent the specified ModSecurity modsec_rule_id. (optional)
    filter_outdated = "filter[outdated]_example" # str | Limit results to active rules referencing an outdated rule revision. (optional)
    include = "waf_rule_revision,waf_firewall_version" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_rule_revision` and `waf_firewall_version`.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List active rules on a WAF
        api_response = api_instance.list_waf_active_rules(firewall_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->list_waf_active_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List active rules on a WAF
        api_response = api_instance.list_waf_active_rules(firewall_id, version_id, filter_status=filter_status, filter_waf_rule_revision_message=filter_waf_rule_revision_message, filter_waf_rule_revision_modsec_rule_id=filter_waf_rule_revision_modsec_rule_id, filter_outdated=filter_outdated, include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->list_waf_active_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **filter_status** | **str**| Limit results to active rules with the specified status. | [optional]
 **filter_waf_rule_revision_message** | **str**| Limit results to active rules with the specified message. | [optional]
 **filter_waf_rule_revision_modsec_rule_id** | **str**| Limit results to active rules that represent the specified ModSecurity modsec_rule_id. | [optional]
 **filter_outdated** | **str**| Limit results to active rules referencing an outdated rule revision. | [optional]
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_rule_revision` and `waf_firewall_version`.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**WafActiveRulesResponse**](WafActiveRulesResponse.md)

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

# **update_waf_active_rule**
> WafActiveRuleResponse update_waf_active_rule(firewall_id, version_id, waf_rule_id)

Update an active rule

Update an active rule's status for a particular firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_active_rules_api
from fastly.model.waf_active_rule import WafActiveRule
from fastly.model.waf_active_rule_response import WafActiveRuleResponse
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
    api_instance = waf_active_rules_api.WafActiveRulesApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    version_id = 1 # int | Integer identifying a service version.
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    waf_active_rule = WafActiveRule(
        data=WafActiveRuleData(
            type=TypeWafActiveRule("waf_active_rule"),
            attributes=WafActiveRuleDataAttributes(
                modsec_rule_id=1,
                revision=WafRuleRevisionOrLatest(None),
                status="log",
            ),
            relationships=RelationshipsForWafActiveRule(),
        ),
    ) # WafActiveRule |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an active rule
        api_response = api_instance.update_waf_active_rule(firewall_id, version_id, waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->update_waf_active_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an active rule
        api_response = api_instance.update_waf_active_rule(firewall_id, version_id, waf_rule_id, waf_active_rule=waf_active_rule)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafActiveRulesApi->update_waf_active_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **version_id** | **int**| Integer identifying a service version. |
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
 **waf_active_rule** | [**WafActiveRule**](WafActiveRule.md)|  | [optional]

### Return type

[**WafActiveRuleResponse**](WafActiveRuleResponse.md)

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

