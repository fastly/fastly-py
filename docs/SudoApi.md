# fastly.SudoApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_sudo_access**](SudoApi.md#request_sudo_access) | **POST** /sudo | Request Sudo access


# **request_sudo_access**
> SudoResponse request_sudo_access()

Request Sudo access

Re-authenticate to allow the provided user to obtain sudo access.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import sudo_api
from fastly.model.sudo_response import SudoResponse
from fastly.model.sudo_request import SudoRequest
from fastly.model.sudo_generic_token_error import SudoGenericTokenError
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
    api_instance = sudo_api.SudoApi(api_client)
    sudo_request = SudoRequest(
        username="username_example",
        password="password_example",
        expiry_time="expiry_time_example",
    ) # SudoRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Request Sudo access
        api_response = api_instance.request_sudo_access(sudo_request=sudo_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling SudoApi->request_sudo_access: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sudo_request** | [**SudoRequest**](SudoRequest.md)|  | [optional]

### Return type

[**SudoResponse**](SudoResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.api+json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**403** | Forbidden. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

