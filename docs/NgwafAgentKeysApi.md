# fastly.NgwafAgentKeysApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**ngwaf_list_agent_keys**](NgwafAgentKeysApi.md#ngwaf_list_agent_keys) | **GET** /ngwaf/v1/workspaces/{workspace_id}/agent-keys | List agent keys for a workspace


# **ngwaf_list_agent_keys**
> InlineResponse20019 ngwaf_list_agent_keys(workspace_id)

List agent keys for a workspace

List agent keys for a workspace.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import ngwaf_agent_keys_api
from fastly.model.inline_response20019 import InlineResponse20019
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
    api_instance = ngwaf_agent_keys_api.NgwafAgentKeysApi(api_client)
    workspace_id = "SU1Z0isxPaozGVKXdv0eY" # str | The ID of the workspace.

    # example passing only required values which don't have defaults set
    try:
        # List agent keys for a workspace
        api_response = api_instance.ngwaf_list_agent_keys(workspace_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NgwafAgentKeysApi->ngwaf_list_agent_keys: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **workspace_id** | **str**| The ID of the workspace. |

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of agent keys. |  -  |
**400** | Request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

