# fastly.TlsCsrsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_csr**](TlsCsrsApi.md#create_csr) | **POST** /tls/certificate_signing_requests | Create CSR


# **create_csr**
> TlsCsrResponse create_csr()

Create CSR

Creates a certificate signing request (CSR).

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_csrs_api
from fastly.model.tls_csr_response import TlsCsrResponse
from fastly.model.tls_csr import TlsCsr
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
    api_instance = tls_csrs_api.TlsCsrsApi(api_client)
    tls_csr = TlsCsr(
        data=TlsCsrData(
            type=TypeTlsCsr("csr"),
            attributes=TlsCsrDataAttributes(
                sans=[
                    "sans_example",
                ],
                common_name="common_name_example",
                country="country_example",
                state="state_example",
                city="city_example",
                postal_code="postal_code_example",
                street_address="street_address_example",
                organization="organization_example",
                organizational_unit="organizational_unit_example",
                email="email_example",
                key_type="RSA2048",
            ),
            relationships=RelationshipTlsPrivateKey(
                tls_private_key=RelationshipTlsPrivateKeyTlsPrivateKey(
                    data=RelationshipMemberTlsPrivateKey(
                        type=TypeTlsPrivateKey("tls_private_key"),
                    ),
                ),
            ),
        ),
    ) # TlsCsr |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create CSR
        api_response = api_instance.create_csr(tls_csr=tls_csr)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCsrsApi->create_csr: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_csr** | [**TlsCsr**](TlsCsr.md)|  | [optional]

### Return type

[**TlsCsrResponse**](TlsCsrResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

