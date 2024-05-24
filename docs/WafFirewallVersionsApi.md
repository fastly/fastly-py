# fastly.WafFirewallVersionsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**clone_waf_firewall_version**](WafFirewallVersionsApi.md#clone_waf_firewall_version) | **PUT** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/clone | Clone a firewall version
[**create_waf_firewall_version**](WafFirewallVersionsApi.md#create_waf_firewall_version) | **POST** /waf/firewalls/{firewall_id}/versions | Create a firewall version
[**deploy_activate_waf_firewall_version**](WafFirewallVersionsApi.md#deploy_activate_waf_firewall_version) | **PUT** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/activate | Deploy or activate a firewall version
[**get_waf_firewall_version**](WafFirewallVersionsApi.md#get_waf_firewall_version) | **GET** /waf/firewalls/{firewall_id}/versions/{firewall_version_number} | Get a firewall version
[**list_waf_firewall_versions**](WafFirewallVersionsApi.md#list_waf_firewall_versions) | **GET** /waf/firewalls/{firewall_id}/versions | List firewall versions
[**update_waf_firewall_version**](WafFirewallVersionsApi.md#update_waf_firewall_version) | **PATCH** /waf/firewalls/{firewall_id}/versions/{firewall_version_number} | Update a firewall version


# **clone_waf_firewall_version**
> WafFirewallVersionResponse clone_waf_firewall_version(firewall_id, firewall_version_number)

Clone a firewall version

Clone a specific, existing firewall version into a new, draft firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewall_versions_api
from fastly.model.waf_firewall_version_response import WafFirewallVersionResponse
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
    api_instance = waf_firewall_versions_api.WafFirewallVersionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.

    # example passing only required values which don't have defaults set
    try:
        # Clone a firewall version
        api_response = api_instance.clone_waf_firewall_version(firewall_id, firewall_version_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->clone_waf_firewall_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |

### Return type

[**WafFirewallVersionResponse**](WafFirewallVersionResponse.md)

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

# **create_waf_firewall_version**
> WafFirewallVersionResponse create_waf_firewall_version(firewall_id)

Create a firewall version

Create a new, draft firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewall_versions_api
from fastly.model.waf_firewall_version_response import WafFirewallVersionResponse
from fastly.model.waf_firewall_version import WafFirewallVersion
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
    api_instance = waf_firewall_versions_api.WafFirewallVersionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    waf_firewall_version = WafFirewallVersion(
        data=WafFirewallVersionData(
            type=TypeWafFirewallVersion("waf_firewall_version"),
            attributes=WafFirewallVersionDataAttributes(
                allowed_http_versions="HTTP/1.0 HTTP/1.1 HTTP/2",
                allowed_methods="GET HEAD POST OPTIONS PUT PATCH DELETE",
                allowed_request_content_type="application/x-www-form-urlencoded|multipart/form-data|text/xml|application/xml|application/x-amf|application/json|text/plain",
                allowed_request_content_type_charset="utf-8|iso-8859-1|iso-8859-15|windows-1252",
                arg_name_length=100,
                arg_length=400,
                combined_file_sizes=10000000,
                comment="",
                critical_anomaly_score=6,
                crs_validate_utf8_encoding=True,
                error_anomaly_score=5,
                high_risk_country_codes="high_risk_country_codes_example",
                http_violation_score_threshold=1,
                inbound_anomaly_score_threshold=1,
                lfi_score_threshold=1,
                locked=False,
                max_file_size=10000000,
                max_num_args=255,
                notice_anomaly_score=4,
                paranoia_level=1,
                php_injection_score_threshold=1,
                rce_score_threshold=1,
                restricted_extensions=".asa/ .asax/ .ascx/ .axd/ .backup/ .bak/ .bat/ .cdx/ .cer/ .cfg/ .cmd/ .com/ .config/ .conf/ .cs/ .csproj/ .csr/ .dat/ .db/ .dbf/ .dll/ .dos/ .htr/ .htw/ .ida/ .idc/ .idq/ .inc/ .ini/ .key/ .licx/ .lnk/ .log/ .mdb/ .old/ .pass/ .pdb/ .pol/ .printer/ .pwd/ .resources/ .resx/ .sql/ .sys/ .vb/ .vbs/ .vbproj/ .vsdisco/ .webinfo/ .xsd/ .xsx",
                restricted_headers="/proxy/ /lock-token/ /content-range/ /translate/ /if/",
                rfi_score_threshold=1,
                session_fixation_score_threshold=1,
                sql_injection_score_threshold=1,
                total_arg_length=6400,
                warning_anomaly_score=1,
                xss_score_threshold=1,
            ),
        ),
    ) # WafFirewallVersion |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a firewall version
        api_response = api_instance.create_waf_firewall_version(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->create_waf_firewall_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a firewall version
        api_response = api_instance.create_waf_firewall_version(firewall_id, waf_firewall_version=waf_firewall_version)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->create_waf_firewall_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **waf_firewall_version** | [**WafFirewallVersion**](WafFirewallVersion.md)|  | [optional]

### Return type

[**WafFirewallVersionResponse**](WafFirewallVersionResponse.md)

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

# **deploy_activate_waf_firewall_version**
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} deploy_activate_waf_firewall_version(firewall_id, firewall_version_number)

Deploy or activate a firewall version

Deploy or activate a specific firewall version. If a firewall has been disabled, deploying a firewall version will automatically enable the firewall again.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewall_versions_api
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
    api_instance = waf_firewall_versions_api.WafFirewallVersionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.

    # example passing only required values which don't have defaults set
    try:
        # Deploy or activate a firewall version
        api_response = api_instance.deploy_activate_waf_firewall_version(firewall_id, firewall_version_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->deploy_activate_waf_firewall_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |

### Return type

**{str: (bool, date, datetime, dict, float, int, list, str, none_type)}**

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.api+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waf_firewall_version**
> WafFirewallVersionResponse get_waf_firewall_version(firewall_id, firewall_version_number)

Get a firewall version

Get details about a specific firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewall_versions_api
from fastly.model.waf_firewall_version_response import WafFirewallVersionResponse
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
    api_instance = waf_firewall_versions_api.WafFirewallVersionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    include = "waf_firewall,waf_active_rules" # str | Include relationships. Optional, comma-separated values. Permitted values: `waf_firewall` and `waf_active_rules`.  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get a firewall version
        api_response = api_instance.get_waf_firewall_version(firewall_id, firewall_version_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->get_waf_firewall_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get a firewall version
        api_response = api_instance.get_waf_firewall_version(firewall_id, firewall_version_number, include=include)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->get_waf_firewall_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **include** | **str**| Include relationships. Optional, comma-separated values. Permitted values: `waf_firewall` and `waf_active_rules`.  | [optional]

### Return type

[**WafFirewallVersionResponse**](WafFirewallVersionResponse.md)

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

# **list_waf_firewall_versions**
> WafFirewallVersionsResponse list_waf_firewall_versions(firewall_id)

List firewall versions

Get a list of firewall versions associated with a specific firewall.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewall_versions_api
from fastly.model.waf_firewall_versions_response import WafFirewallVersionsResponse
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
    api_instance = waf_firewall_versions_api.WafFirewallVersionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    include = "waf_firewall" # str | Include relationships. Optional. (optional)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List firewall versions
        api_response = api_instance.list_waf_firewall_versions(firewall_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->list_waf_firewall_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List firewall versions
        api_response = api_instance.list_waf_firewall_versions(firewall_id, include=include, page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->list_waf_firewall_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **include** | **str**| Include relationships. Optional. | [optional]
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**WafFirewallVersionsResponse**](WafFirewallVersionsResponse.md)

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

# **update_waf_firewall_version**
> WafFirewallVersionResponse update_waf_firewall_version(firewall_id, firewall_version_number)

Update a firewall version

Update a specific firewall version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import waf_firewall_versions_api
from fastly.model.waf_firewall_version_response import WafFirewallVersionResponse
from fastly.model.waf_firewall_version import WafFirewallVersion
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
    api_instance = waf_firewall_versions_api.WafFirewallVersionsApi(api_client)
    firewall_id = "fW7g2uUGZzb2W9Euo4Mo0r" # str | Alphanumeric string identifying a WAF Firewall.
    firewall_version_number = 1 # int | Integer identifying a WAF firewall version.
    waf_firewall_version = WafFirewallVersion(
        data=WafFirewallVersionData(
            type=TypeWafFirewallVersion("waf_firewall_version"),
            attributes=WafFirewallVersionDataAttributes(
                allowed_http_versions="HTTP/1.0 HTTP/1.1 HTTP/2",
                allowed_methods="GET HEAD POST OPTIONS PUT PATCH DELETE",
                allowed_request_content_type="application/x-www-form-urlencoded|multipart/form-data|text/xml|application/xml|application/x-amf|application/json|text/plain",
                allowed_request_content_type_charset="utf-8|iso-8859-1|iso-8859-15|windows-1252",
                arg_name_length=100,
                arg_length=400,
                combined_file_sizes=10000000,
                comment="",
                critical_anomaly_score=6,
                crs_validate_utf8_encoding=True,
                error_anomaly_score=5,
                high_risk_country_codes="high_risk_country_codes_example",
                http_violation_score_threshold=1,
                inbound_anomaly_score_threshold=1,
                lfi_score_threshold=1,
                locked=False,
                max_file_size=10000000,
                max_num_args=255,
                notice_anomaly_score=4,
                paranoia_level=1,
                php_injection_score_threshold=1,
                rce_score_threshold=1,
                restricted_extensions=".asa/ .asax/ .ascx/ .axd/ .backup/ .bak/ .bat/ .cdx/ .cer/ .cfg/ .cmd/ .com/ .config/ .conf/ .cs/ .csproj/ .csr/ .dat/ .db/ .dbf/ .dll/ .dos/ .htr/ .htw/ .ida/ .idc/ .idq/ .inc/ .ini/ .key/ .licx/ .lnk/ .log/ .mdb/ .old/ .pass/ .pdb/ .pol/ .printer/ .pwd/ .resources/ .resx/ .sql/ .sys/ .vb/ .vbs/ .vbproj/ .vsdisco/ .webinfo/ .xsd/ .xsx",
                restricted_headers="/proxy/ /lock-token/ /content-range/ /translate/ /if/",
                rfi_score_threshold=1,
                session_fixation_score_threshold=1,
                sql_injection_score_threshold=1,
                total_arg_length=6400,
                warning_anomaly_score=1,
                xss_score_threshold=1,
            ),
        ),
    ) # WafFirewallVersion |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a firewall version
        api_response = api_instance.update_waf_firewall_version(firewall_id, firewall_version_number)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->update_waf_firewall_version: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a firewall version
        api_response = api_instance.update_waf_firewall_version(firewall_id, firewall_version_number, waf_firewall_version=waf_firewall_version)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling WafFirewallVersionsApi->update_waf_firewall_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firewall_id** | **str**| Alphanumeric string identifying a WAF Firewall. |
 **firewall_version_number** | **int**| Integer identifying a WAF firewall version. |
 **waf_firewall_version** | [**WafFirewallVersion**](WafFirewallVersion.md)|  | [optional]

### Return type

[**WafFirewallVersionResponse**](WafFirewallVersionResponse.md)

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

