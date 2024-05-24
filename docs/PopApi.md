# fastly.PopApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_pops**](PopApi.md#list_pops) | **GET** /datacenters | List Fastly POPs


# **list_pops**
> [Pop] list_pops()

List Fastly POPs

Get a list of all Fastly POPs.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import pop_api
from fastly.model.pop import Pop
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
    api_instance = pop_api.PopApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Fastly POPs
        api_response = api_instance.list_pops()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PopApi->list_pops: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**[Pop]**](Pop.md)

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

