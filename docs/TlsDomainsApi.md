# fastly.TlsDomainsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_tls_domains**](TlsDomainsApi.md#list_tls_domains) | **GET** /tls/domains | List TLS domains


# **list_tls_domains**
> TlsDomainsResponse list_tls_domains()

List TLS domains

List all TLS domains.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_domains_api
from fastly.model.tls_domains_response import TlsDomainsResponse
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
    api_instance = tls_domains_api.TlsDomainsApi(api_client)
    filter_in_use = "filter[in_use]_example" # str | Optional. Limit the returned domains to those currently using Fastly to terminate TLS with SNI (that is, domains considered \"in use\") Permitted values: true, false. (optional)
    filter_tls_certificates_id = "filter[tls_certificates.id]_example" # str | Optional. Limit the returned domains to those listed in the given TLS certificate's SAN list. (optional)
    filter_tls_subscriptions_id = "filter[tls_subscriptions.id]_example" # str | Optional. Limit the returned domains to those for a given TLS subscription. (optional)
    include = "include_example" # str | Include related objects. Optional, comma-separated values. Permitted values: `tls_activations`, `tls_certificates`, `tls_subscriptions`, `tls_subscriptions.tls_authorizations`, `tls_authorizations.globalsign_email_challenge`, and `tls_authorizations.self_managed_http_challenge`.  (optional)
    sort = "id" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "id"
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TLS domains
        api_response = api_instance.list_tls_domains(filter_in_use=filter_in_use, filter_tls_certificates_id=filter_tls_certificates_id, filter_tls_subscriptions_id=filter_tls_subscriptions_id, include=include, sort=sort, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsDomainsApi->list_tls_domains: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_in_use** | **str**| Optional. Limit the returned domains to those currently using Fastly to terminate TLS with SNI (that is, domains considered \&quot;in use\&quot;) Permitted values: true, false. | [optional]
 **filter_tls_certificates_id** | **str**| Optional. Limit the returned domains to those listed in the given TLS certificate&#39;s SAN list. | [optional]
 **filter_tls_subscriptions_id** | **str**| Optional. Limit the returned domains to those for a given TLS subscription. | [optional]
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `tls_activations`, `tls_certificates`, `tls_subscriptions`, `tls_subscriptions.tls_authorizations`, `tls_authorizations.globalsign_email_challenge`, and `tls_authorizations.self_managed_http_challenge`.  | [optional]
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "id"
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**TlsDomainsResponse**](TlsDomainsResponse.md)

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

