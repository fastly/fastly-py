# fastly.PublicIpListApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_fastly_ips**](PublicIpListApi.md#list_fastly_ips) | **GET** /public-ip-list | List Fastly&#39;s public IPs


# **list_fastly_ips**
> PublicIpList list_fastly_ips()

List Fastly's public IPs

List the public IP addresses for the Fastly network.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import public_ip_list_api
from fastly.model.public_ip_list import PublicIpList
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
    api_instance = public_ip_list_api.PublicIpListApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Fastly's public IPs
        api_response = api_instance.list_fastly_ips()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling PublicIpListApi->list_fastly_ips: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**PublicIpList**](PublicIpList.md)

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

