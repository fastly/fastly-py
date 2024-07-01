# fastly.ContentApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**content_check**](ContentApi.md#content_check) | **GET** /content/edge_check | Check status of content in each POP&#39;s cache


# **content_check**
> [Content] content_check()

Check status of content in each POP's cache

Retrieve headers and MD5 hash of the content for a particular URL from each Fastly edge server. This API is limited to 200 requests per hour. If the content takes too long to download, the hash will be set to `error-timeout-$pop`. If the response is too large, it will be set to `warning-too-large-$pop`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import content_api
from fastly.model.content import Content
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
    api_instance = content_api.ContentApi(api_client)
    url = "https://www.example.com/foo/bar" # str | Full URL (host and path) to check on all nodes. if protocol is omitted, http will be assumed. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Check status of content in each POP's cache
        api_response = api_instance.content_check(url=url)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ContentApi->content_check: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **url** | **str**| Full URL (host and path) to check on all nodes. if protocol is omitted, http will be assumed. | [optional]

### Return type

[**[Content]**](Content.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

