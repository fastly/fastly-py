# fastly.NgwafSimulateApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**ngwaf_simulate_waf_request**](NgwafSimulateApi.md#ngwaf_simulate_waf_request) | **POST** /ngwaf/v1/workspaces/{workspace_id}/simulate | Simulate a WAF request


# **ngwaf_simulate_waf_request**
> WafSimulateResponse ngwaf_simulate_waf_request(workspace_id, waf_simulate_request)

Simulate a WAF request

Simulates a request through the workspace's WAF configuration and returns the WAF response code and any signals that would be detected. The operation is stateless — no simulation data is persisted. 

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ngwaf_simulate_api
from fastly.model.waf_simulate_request import WafSimulateRequest
from fastly.model.waf_simulate_response import WafSimulateResponse
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
    api_instance = ngwaf_simulate_api.NgwafSimulateApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the workspace.
    waf_simulate_request = WafSimulateRequest(
        request='''POST /login HTTP/1.1
Host: example.com
Content-Type: application/x-www-form-urlencoded

username=admin&password=1' OR '1'='1''',
        response='''HTTP/1.1 200 OK
Content-Type: text/html

''',
    ) # WafSimulateRequest | 

    # example passing only required values which don't have defaults set
    try:
        # Simulate a WAF request
        api_response = api_instance.ngwaf_simulate_waf_request(workspace_id, waf_simulate_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NgwafSimulateApi->ngwaf_simulate_waf_request: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the workspace. |
 **waf_simulate_request** | [**WafSimulateRequest**](WafSimulateRequest.md)|  |

### Return type

[**WafSimulateResponse**](WafSimulateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Simulation result. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

