# fastly.WafRuleRevisionsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_waf_rule_revision**](WafRuleRevisionsApi.md#get_waf_rule_revision) | **GET** /waf/rules/{waf_rule_id}/revisions/{waf_rule_revision_number} | Get a revision of a rule
[**list_waf_rule_revisions**](WafRuleRevisionsApi.md#list_waf_rule_revisions) | **GET** /waf/rules/{waf_rule_id}/revisions | List revisions for a rule


# **get_waf_rule_revision**
> WafRuleRevisionResponse get_waf_rule_revision(waf_rule_id, waf_rule_revision_number)

Get a revision of a rule

Get a specific rule revision.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_rule_revisions_api
from fastly.model.waf_rule_revision_response import WafRuleRevisionResponse
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
    api_instance = waf_rule_revisions_api.WafRuleRevisionsApi(api_client)
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    waf_rule_revision_number = 2 # int | Revision number.
    include = "source,vcl,waf_rule" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_rule`, `vcl`, and `source`. The `vcl` and `source` relationships show the WAF VCL and corresponding ModSecurity source. These fields are blank unless the relationship is included.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a revision of a rule
        api_response = api_instance.get_waf_rule_revision(waf_rule_id, waf_rule_revision_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRuleRevisionsApi->get_waf_rule_revision: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a revision of a rule
        api_response = api_instance.get_waf_rule_revision(waf_rule_id, waf_rule_revision_number, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRuleRevisionsApi->get_waf_rule_revision: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
 **waf_rule_revision_number** | **int**| Revision number. |
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_rule`, `vcl`, and `source`. The `vcl` and `source` relationships show the WAF VCL and corresponding ModSecurity source. These fields are blank unless the relationship is included.  | [optional]

### Return type

[**WafRuleRevisionResponse**](WafRuleRevisionResponse.md)

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

# **list_waf_rule_revisions**
> WafRuleRevisionsResponse list_waf_rule_revisions(waf_rule_id)

List revisions for a rule

List all revisions for a specific rule. The `rule_id` provided can be the ModSecurity Rule ID or the Fastly generated rule ID.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_rule_revisions_api
from fastly.model.waf_rule_revisions_response import WafRuleRevisionsResponse
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
    api_instance = waf_rule_revisions_api.WafRuleRevisionsApi(api_client)
    waf_rule_id = "3krg2uUGZzb2W9Euo4moOR" # str | Alphanumeric string identifying a WAF rule.
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "waf_rule" # str | Include relationships. Optional. (optional) if omitted the server will use the default value of "waf_rule"

    # example passing only required values which don't have defaults set
    try:
        # List revisions for a rule
        api_response = api_instance.list_waf_rule_revisions(waf_rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRuleRevisionsApi->list_waf_rule_revisions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List revisions for a rule
        api_response = api_instance.list_waf_rule_revisions(waf_rule_id, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafRuleRevisionsApi->list_waf_rule_revisions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waf_rule_id** | **str**| Alphanumeric string identifying a WAF rule. |
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional. | [optional] if omitted the server will use the default value of "waf_rule"

### Return type

[**WafRuleRevisionsResponse**](WafRuleRevisionsResponse.md)

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

