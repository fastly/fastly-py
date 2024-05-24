# fastly.WafRulesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_waf_rule**](WafRulesApi.md#get_waf_rule) | **GET** /waf/rules/{waf_rule_id} | Get a rule
[**list_waf_rules**](WafRulesApi.md#list_waf_rules) | **GET** /waf/rules | List available WAF rules


# **get_waf_rule**
> WafRuleResponse get_waf_rule(waf_rule_id)

Get a rule

Get a specific rule. The `id` provided can be the ModSecurity Rule ID or the Fastly generated rule ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_rules_api
from fastly.model.waf_rule_response import WafRuleResponse
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
    api_instance = waf_rules_api.WafRulesApi(api_client)
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    include = "waf_tags,waf_rule_revisions" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_tags` and `waf_rule_revisions`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a rule
        api_response = api_instance.get_waf_rule(waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRulesApi->get_waf_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a rule
        api_response = api_instance.get_waf_rule(waf_rule_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRulesApi->get_waf_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_tags` and `waf_rule_revisions`.  | [optional]

### Return type

[**WafRuleResponse**](WafRuleResponse.md)

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

# **list_waf_rules**
> WafRulesResponse list_waf_rules()

List available WAF rules

List all available WAF rules.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_rules_api
from fastly.model.waf_rules_response import WafRulesResponse
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
    api_instance = waf_rules_api.WafRulesApi(api_client)
    filter_modsec_rule_id = "filter[modsec_rule_id]_example" # str | Limit the returned rules to a specific ModSecurity rule ID. (optional)
    filter_waf_tags_name = "filter[waf_tags][name]_example" # str | Limit the returned rules to a set linked to a tag by name. (optional)
    filter_waf_rule_revisions_source = "filter[waf_rule_revisions][source]_example" # str | Limit the returned rules to a set linked to a source. (optional)
    filter_waf_firewall_id_not_match = "filter[waf_firewall.id][not][match]_example" # str | Limit the returned rules to a set not included in the active firewall version for a firewall. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "waf_tags,waf_rule_revisions" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_tags` and `waf_rule_revisions`.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List available WAF rules
        api_response = api_instance.list_waf_rules(filter_modsec_rule_id=filter_modsec_rule_id, filter_waf_tags_name=filter_waf_tags_name, filter_waf_rule_revisions_source=filter_waf_rule_revisions_source, filter_waf_firewall_id_not_match=filter_waf_firewall_id_not_match, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRulesApi->list_waf_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_modsec_rule_id** | **str**| Limit the returned rules to a specific ModSecurity rule ID. | [optional]
 **filter_waf_tags_name** | **str**| Limit the returned rules to a set linked to a tag by name. | [optional]
 **filter_waf_rule_revisions_source** | **str**| Limit the returned rules to a set linked to a source. | [optional]
 **filter_waf_firewall_id_not_match** | **str**| Limit the returned rules to a set not included in the active firewall version for a firewall. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_tags` and `waf_rule_revisions`.  | [optional]

### Return type

[**WafRulesResponse**](WafRulesResponse.md)

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

