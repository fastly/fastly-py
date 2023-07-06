# fastly.LegacyWafTagApi

All URIs are relative to *https://api.fastly.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_legacy_waf_tags**](LegacyWafTagApi.md#list_legacy_waf_tags) | **GET** /wafs/tags | List WAF tags


# **list_legacy_waf_tags**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} list_legacy_waf_tags()

List WAF tags

List all tags.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import legacy_waf_tag_api
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
    api_instance = legacy_waf_tag_api.LegacyWafTagApi(api_client)
    filter_name = "filter[name]_example" # str | Limit the returned tags to a specific name. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    include = "rules" # str | Include relationships. Optional, comma separated values. Permitted values: `rules`.  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List WAF tags
        api_response = api_instance.list_legacy_waf_tags(filter_name=filter_name, page_number=page_number, page_size=page_size, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling LegacyWafTagApi->list_legacy_waf_tags: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_name** | **str**| Limit the returned tags to a specific name. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **include** | **str**| Include relationships. Optional, comma separated values. Permitted values: `rules`.  | [optional]

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

