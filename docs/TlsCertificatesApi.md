# fastly.TlsCertificatesApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tls_cert**](TlsCertificatesApi.md#create_tls_cert) | **POST** /tls/certificates | Create a TLS certificate
[**delete_tls_cert**](TlsCertificatesApi.md#delete_tls_cert) | **DELETE** /tls/certificates/{tls_certificate_id} | Delete a TLS certificate
[**get_tls_cert**](TlsCertificatesApi.md#get_tls_cert) | **GET** /tls/certificates/{tls_certificate_id} | Get a TLS certificate
[**get_tls_cert_blob**](TlsCertificatesApi.md#get_tls_cert_blob) | **GET** /tls/certificates/{tls_certificate_id}/blob | Get a TLS certificate blob (Limited Availability)
[**list_tls_certs**](TlsCertificatesApi.md#list_tls_certs) | **GET** /tls/certificates | List TLS certificates
[**update_tls_cert**](TlsCertificatesApi.md#update_tls_cert) | **PATCH** /tls/certificates/{tls_certificate_id} | Update a TLS certificate


# **create_tls_cert**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_tls_cert()

Create a TLS certificate

Create a TLS certificate.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_certificates_api
from fastly.model.tls_certificate import TlsCertificate
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
    api_instance = tls_certificates_api.TlsCertificatesApi(api_client)
    tls_certificate = TlsCertificate(
        data=TlsCertificateData(
            type=TypeTlsCertificate("tls_certificate"),
            attributes=TlsCertificateDataAttributes(
                cert_blob="cert_blob_example",
                name="name_example",
            ),
            relationships=RelationshipTlsDomains(
                tls_domains=RelationshipTlsDomainsTlsDomains(
                    data=[
                        RelationshipMemberTlsDomain(
                            type=TypeTlsDomain("tls_domain"),
                        ),
                    ],
                ),
            ),
        ),
    ) # TlsCertificate |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a TLS certificate
        api_response = api_instance.create_tls_cert(tls_certificate=tls_certificate)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->create_tls_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_certificate** | [**TlsCertificate**](TlsCertificate.md)|  | [optional]

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

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

# **delete_tls_cert**
> delete_tls_cert(tls_certificate_id)

Delete a TLS certificate

Destroy a TLS certificate. TLS certificates already enabled for a domain cannot be destroyed.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_certificates_api
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
    api_instance = tls_certificates_api.TlsCertificatesApi(api_client)
    tls_certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS certificate.

    # example passing only required values which don't have defaults set
    try:
        # Delete a TLS certificate
        api_instance.delete_tls_cert(tls_certificate_id)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->delete_tls_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_certificate_id** | **str**| Alphanumeric string identifying a TLS certificate. |

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

# **get_tls_cert**
> TlsCertificateResponse get_tls_cert(tls_certificate_id)

Get a TLS certificate

Show a TLS certificate.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_certificates_api
from fastly.model.tls_certificate_response import TlsCertificateResponse
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
    api_instance = tls_certificates_api.TlsCertificatesApi(api_client)
    tls_certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS certificate.

    # example passing only required values which don't have defaults set
    try:
        # Get a TLS certificate
        api_response = api_instance.get_tls_cert(tls_certificate_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->get_tls_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_certificate_id** | **str**| Alphanumeric string identifying a TLS certificate. |

### Return type

[**TlsCertificateResponse**](TlsCertificateResponse.md)

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

# **get_tls_cert_blob**
> TlsCertificateBlobResponse get_tls_cert_blob(tls_certificate_id)

Get a TLS certificate blob (Limited Availability)

Retrieve a TLS certificate blob. This feature is part of a [limited availability](https://docs.fastly.com/products/fastly-product-lifecycle#limited-availability) release.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_certificates_api
from fastly.model.tls_certificate_blob_response import TlsCertificateBlobResponse
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
    api_instance = tls_certificates_api.TlsCertificatesApi(api_client)
    tls_certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS certificate.

    # example passing only required values which don't have defaults set
    try:
        # Get a TLS certificate blob (Limited Availability)
        api_response = api_instance.get_tls_cert_blob(tls_certificate_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->get_tls_cert_blob: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_certificate_id** | **str**| Alphanumeric string identifying a TLS certificate. |

### Return type

[**TlsCertificateBlobResponse**](TlsCertificateBlobResponse.md)

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

# **list_tls_certs**
> TlsCertificatesResponse list_tls_certs()

List TLS certificates

List all TLS certificates.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_certificates_api
from fastly.model.tls_certificates_response import TlsCertificatesResponse
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
    api_instance = tls_certificates_api.TlsCertificatesApi(api_client)
    filter_in_use = "filter[in_use]_example" # str | Optional. Limit the returned certificates to those currently using Fastly to terminate TLS (that is, certificates associated with an activation). Permitted values: true, false. (optional)
    filter_not_after = "filter[not_after]_example" # str | Limit the returned certificates to those that expire prior to the specified date in UTC. Accepts parameters: lte (e.g., filter[not_after][lte]=2020-05-05).  (optional)
    filter_tls_domains_id = "filter[tls_domains.id]_example" # str | Limit the returned certificates to those that include the specific domain. (optional)
    include = "include_example" # str | Include related objects. Optional, comma-separated values. Permitted values: `tls_activations`.  (optional)
    sort = "-created_at" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "-created_at"
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TLS certificates
        api_response = api_instance.list_tls_certs(filter_in_use=filter_in_use, filter_not_after=filter_not_after, filter_tls_domains_id=filter_tls_domains_id, include=include, sort=sort, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->list_tls_certs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_in_use** | **str**| Optional. Limit the returned certificates to those currently using Fastly to terminate TLS (that is, certificates associated with an activation). Permitted values: true, false. | [optional]
 **filter_not_after** | **str**| Limit the returned certificates to those that expire prior to the specified date in UTC. Accepts parameters: lte (e.g., filter[not_after][lte]&#x3D;2020-05-05).  | [optional]
 **filter_tls_domains_id** | **str**| Limit the returned certificates to those that include the specific domain. | [optional]
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `tls_activations`.  | [optional]
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "-created_at"
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**TlsCertificatesResponse**](TlsCertificatesResponse.md)

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

# **update_tls_cert**
> TlsCertificateResponse update_tls_cert(tls_certificate_id)

Update a TLS certificate

Replace a TLS certificate with a newly reissued TLS certificate, or update a TLS certificate's name. If replacing a TLS certificate, the new TLS certificate must contain all SAN entries as the current TLS certificate. It must either have an exact matching list or contain a superset.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_certificates_api
from fastly.model.tls_certificate_response import TlsCertificateResponse
from fastly.model.tls_certificate import TlsCertificate
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
    api_instance = tls_certificates_api.TlsCertificatesApi(api_client)
    tls_certificate_id = "cRTguUGZzb2W9Euo4moOr" # str | Alphanumeric string identifying a TLS certificate.
    tls_certificate = TlsCertificate(
        data=TlsCertificateData(
            type=TypeTlsCertificate("tls_certificate"),
            attributes=TlsCertificateDataAttributes(
                cert_blob="cert_blob_example",
                name="name_example",
            ),
            relationships=RelationshipTlsDomains(
                tls_domains=RelationshipTlsDomainsTlsDomains(
                    data=[
                        RelationshipMemberTlsDomain(
                            type=TypeTlsDomain("tls_domain"),
                        ),
                    ],
                ),
            ),
        ),
    ) # TlsCertificate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a TLS certificate
        api_response = api_instance.update_tls_cert(tls_certificate_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->update_tls_cert: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a TLS certificate
        api_response = api_instance.update_tls_cert(tls_certificate_id, tls_certificate=tls_certificate)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsCertificatesApi->update_tls_cert: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_certificate_id** | **str**| Alphanumeric string identifying a TLS certificate. |
 **tls_certificate** | [**TlsCertificate**](TlsCertificate.md)|  | [optional]

### Return type

[**TlsCertificateResponse**](TlsCertificateResponse.md)

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

