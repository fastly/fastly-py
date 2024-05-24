# fastly.TlsConfigurationsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tls_config**](TlsConfigurationsApi.md#get_tls_config) | **GET** /tls/configurations/{tls_configuration_id} | Get a TLS configuration
[**list_tls_configs**](TlsConfigurationsApi.md#list_tls_configs) | **GET** /tls/configurations | List TLS configurations
[**update_tls_config**](TlsConfigurationsApi.md#update_tls_config) | **PATCH** /tls/configurations/{tls_configuration_id} | Update a TLS configuration


# **get_tls_config**
> TlsConfigurationResponse get_tls_config(tls_configuration_id)

Get a TLS configuration

Show a TLS configuration.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_configurations_api
from fastly.model.tls_configuration_response import TlsConfigurationResponse
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
    api_instance = tls_configurations_api.TlsConfigurationsApi(api_client)
    tls_configuration_id = "t7CguUGZzb2W9Euo5FoKa" # str | Alphanumeric string identifying a TLS configuration.
    include = "dns_records" # str | Include related objects. Optional, comma-separated values. Permitted values: `dns_records`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a TLS configuration
        api_response = api_instance.get_tls_config(tls_configuration_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsConfigurationsApi->get_tls_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a TLS configuration
        api_response = api_instance.get_tls_config(tls_configuration_id, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsConfigurationsApi->get_tls_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_configuration_id** | **str**| Alphanumeric string identifying a TLS configuration. |
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `dns_records`.  | [optional]

### Return type

[**TlsConfigurationResponse**](TlsConfigurationResponse.md)

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

# **list_tls_configs**
> TlsConfigurationsResponse list_tls_configs()

List TLS configurations

List all TLS configurations.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_configurations_api
from fastly.model.tls_configurations_response import TlsConfigurationsResponse
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
    api_instance = tls_configurations_api.TlsConfigurationsApi(api_client)
    filter_bulk = "filter[bulk]_example" # str | Optionally filters by the bulk attribute. (optional)
    include = "dns_records" # str | Include related objects. Optional, comma-separated values. Permitted values: `dns_records`.  (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List TLS configurations
        api_response = api_instance.list_tls_configs(filter_bulk=filter_bulk, include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsConfigurationsApi->list_tls_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter_bulk** | **str**| Optionally filters by the bulk attribute. | [optional]
 **include** | **str**| Include related objects. Optional, comma-separated values. Permitted values: `dns_records`.  | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**TlsConfigurationsResponse**](TlsConfigurationsResponse.md)

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

# **update_tls_config**
> TlsConfigurationResponse update_tls_config(tls_configuration_id)

Update a TLS configuration

Update a TLS configuration.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import tls_configurations_api
from fastly.model.tls_configuration_response import TlsConfigurationResponse
from fastly.model.tls_configuration import TlsConfiguration
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
    api_instance = tls_configurations_api.TlsConfigurationsApi(api_client)
    tls_configuration_id = "t7CguUGZzb2W9Euo5FoKa" # str | Alphanumeric string identifying a TLS configuration.
    tls_configuration = TlsConfiguration(
        data=TlsConfigurationData(
            type=TypeTlsConfiguration("tls_configuration"),
            attributes=TlsConfigurationDataAttributes(
                name="name_example",
            ),
            relationships=RelationshipsForTlsConfiguration(),
        ),
    ) # TlsConfiguration |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a TLS configuration
        api_response = api_instance.update_tls_config(tls_configuration_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsConfigurationsApi->update_tls_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a TLS configuration
        api_response = api_instance.update_tls_config(tls_configuration_id, tls_configuration=tls_configuration)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling TlsConfigurationsApi->update_tls_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tls_configuration_id** | **str**| Alphanumeric string identifying a TLS configuration. |
 **tls_configuration** | [**TlsConfiguration**](TlsConfiguration.md)|  | [optional]

### Return type

[**TlsConfigurationResponse**](TlsConfigurationResponse.md)

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

