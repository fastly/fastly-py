# fastly.TlsBulkCertificatesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_bulk_tls_cert**](TlsBulkCertificatesApi.md#delete_bulk_tls_cert) | **DELETE** /tls/bulk/certificates/{certificate_id} | Delete a certificate
[**get_tls_bulk_cert**](TlsBulkCertificatesApi.md#get_tls_bulk_cert) | **GET** /tls/bulk/certificates/{certificate_id} | Get a certificate
[**list_tls_bulk_certs**](TlsBulkCertificatesApi.md#list_tls_bulk_certs) | **GET** /tls/bulk/certificates | List certificates
[**update_bulk_tls_cert**](TlsBulkCertificatesApi.md#update_bulk_tls_cert) | **PATCH** /tls/bulk/certificates/{certificate_id} | Update a certificate
[**upload_tls_bulk_cert**](TlsBulkCertificatesApi.md#upload_tls_bulk_cert) | **POST** /tls/bulk/certificates | Upload a certificate


# **delete_bulk_tls_cert**
> delete_bulk_tls_cert(certificate_id)

Delete a certificate

Destroy a certificate. This disables TLS for all domains listed as SAN entries.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_bulk_certificates_api
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
    api_instance = tls_bulk_certificates_api.TlsBulkCertificatesApi(api_client)
    certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS bulk certificate.

    # example passing only required values which don't have defaults set
    try:
        # Delete a certificate
        api_instance.delete_bulk_tls_cert(certificate_id)
    except fastly.ApiException as e:
        print("Exception when calling TlsBulkCertificatesApi->delete_bulk_tls_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Alphanumeric string identifying a TLS bulk certificate. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tls_bulk_cert**
> TlsBulkCertificateResponse get_tls_bulk_cert(certificate_id)

Get a certificate

Retrieve a single certificate.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_bulk_certificates_api
from fastly.model.tls_bulk_certificate_response import TlsBulkCertificateResponse
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
    api_instance = tls_bulk_certificates_api.TlsBulkCertificatesApi(api_client)
    certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS bulk certificate.

    # example passing only required values which don't have defaults set
    try:
        # Get a certificate
        api_response = api_instance.get_tls_bulk_cert(certificate_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsBulkCertificatesApi->get_tls_bulk_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Alphanumeric string identifying a TLS bulk certificate. |

### Return type

[**TlsBulkCertificateResponse**](TlsBulkCertificateResponse.md)

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

# **list_tls_bulk_certs**
> TlsBulkCertificatesResponse list_tls_bulk_certs()

List certificates

List all certificates.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_bulk_certificates_api
from fastly.model.tls_bulk_certificates_response import TlsBulkCertificatesResponse
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
    api_instance = tls_bulk_certificates_api.TlsBulkCertificatesApi(api_client)
    filter_tls_domain_id = "filter[tls_domain.id]_example" # str | Filter certificates by their matching, fully-qualified domain name. (optional)
    filter_not_before = "filter[not_before]_example" # str | Filter the returned certificates by not_before date in UTC.  Accepts parameters: lt, lte, gt, gte (e.g., filter[not_before][gte]=2020-05-05).  (optional)
    filter_not_after = "filter[not_after]_example" # str | Filter the returned certificates by expiry date in UTC.  Accepts parameters: lt, lte, gt, gte (e.g., filter[not_after][lte]=2020-05-05).  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20
    sort = "created_at" # str | The order in which to list the results by creation date. (optional) if omitted the server will use the default value of "created_at"

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List certificates
        api_response = api_instance.list_tls_bulk_certs(filter_tls_domain_id=filter_tls_domain_id, filter_not_before=filter_not_before, filter_not_after=filter_not_after, page_number=page_number, page_size=page_size, sort=sort)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsBulkCertificatesApi->list_tls_bulk_certs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_tls_domain_id** | **str**| Filter certificates by their matching, fully-qualified domain name. | [optional]
 **filter_not_before** | **str**| Filter the returned certificates by not_before date in UTC.  Accepts parameters: lt, lte, gt, gte (e.g., filter[not_before][gte]&#x3D;2020-05-05).  | [optional]
 **filter_not_after** | **str**| Filter the returned certificates by expiry date in UTC.  Accepts parameters: lt, lte, gt, gte (e.g., filter[not_after][lte]&#x3D;2020-05-05).  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20
 **sort** | **str**| The order in which to list the results by creation date. | [optional] if omitted the server will use the default value of "created_at"

### Return type

[**TlsBulkCertificatesResponse**](TlsBulkCertificatesResponse.md)

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

# **update_bulk_tls_cert**
> TlsBulkCertificateResponse update_bulk_tls_cert(certificate_id)

Update a certificate

Replace a certificate with a newly reissued certificate. By using this endpoint, the original certificate will cease to be used for future TLS handshakes. Thus, only SAN entries that appear in the replacement certificate will become TLS enabled. Any SAN entries that are missing in the replacement certificate will become disabled.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_bulk_certificates_api
from fastly.model.tls_bulk_certificate_response import TlsBulkCertificateResponse
from fastly.model.tls_bulk_certificate import TlsBulkCertificate
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
    api_instance = tls_bulk_certificates_api.TlsBulkCertificatesApi(api_client)
    certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS bulk certificate.
    tls_bulk_certificate = TlsBulkCertificate(
        data=TlsBulkCertificateData(
            type=TypeTlsBulkCertificate("tls_bulk_certificate"),
            attributes=TlsBulkCertificateDataAttributes(
                allow_untrusted_root=False,
                cert_blob="cert_blob_example",
                intermediates_blob="intermediates_blob_example",
            ),
            relationships=RelationshipsForTlsBulkCertificate(),
        ),
    ) # TlsBulkCertificate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a certificate
        api_response = api_instance.update_bulk_tls_cert(certificate_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsBulkCertificatesApi->update_bulk_tls_cert: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a certificate
        api_response = api_instance.update_bulk_tls_cert(certificate_id, tls_bulk_certificate=tls_bulk_certificate)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsBulkCertificatesApi->update_bulk_tls_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **certificate_id** | **str**| Alphanumeric string identifying a TLS bulk certificate. |
 **tls_bulk_certificate** | [**TlsBulkCertificate**](TlsBulkCertificate.md)|  | [optional]

### Return type

[**TlsBulkCertificateResponse**](TlsBulkCertificateResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/vnd.api+json
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_tls_bulk_cert**
> TlsBulkCertificateResponse upload_tls_bulk_cert()

Upload a certificate

Upload a new certificate. TLS domains are automatically enabled upon certificate creation. If a domain is already enabled on a previously uploaded certificate, that domain will be updated to use the new certificate for all future TLS handshake requests.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_bulk_certificates_api
from fastly.model.tls_bulk_certificate_response import TlsBulkCertificateResponse
from fastly.model.tls_bulk_certificate import TlsBulkCertificate
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
    api_instance = tls_bulk_certificates_api.TlsBulkCertificatesApi(api_client)
    tls_bulk_certificate = TlsBulkCertificate(
        data=TlsBulkCertificateData(
            type=TypeTlsBulkCertificate("tls_bulk_certificate"),
            attributes=TlsBulkCertificateDataAttributes(
                allow_untrusted_root=False,
                cert_blob="cert_blob_example",
                intermediates_blob="intermediates_blob_example",
            ),
            relationships=RelationshipsForTlsBulkCertificate(),
        ),
    ) # TlsBulkCertificate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Upload a certificate
        api_response = api_instance.upload_tls_bulk_cert(tls_bulk_certificate=tls_bulk_certificate)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsBulkCertificatesApi->upload_tls_bulk_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_bulk_certificate** | [**TlsBulkCertificate**](TlsBulkCertificate.md)|  | [optional]

### Return type

[**TlsBulkCertificateResponse**](TlsBulkCertificateResponse.md)

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

