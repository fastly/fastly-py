# fastly.NetworkProtectApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_network_protect_endpoint**](NetworkProtectApi.md#create_network_protect_endpoint) | **POST** /network-protect/v1/endpoints | Create a Network Protect endpoint
[**create_network_protect_network**](NetworkProtectApi.md#create_network_protect_network) | **POST** /network-protect/v1/networks | Create a Network Protect network
[**create_network_protect_prefix_list**](NetworkProtectApi.md#create_network_protect_prefix_list) | **POST** /network-protect/v1/prefix-lists | Create a Network Protect prefix list
[**create_network_protect_rule_set**](NetworkProtectApi.md#create_network_protect_rule_set) | **POST** /network-protect/v1/rule-sets | Create a Network Protect rule set
[**delete_network_protect_endpoint**](NetworkProtectApi.md#delete_network_protect_endpoint) | **DELETE** /network-protect/v1/endpoints/{endpoint_id} | Delete a Network Protect endpoint
[**delete_network_protect_network**](NetworkProtectApi.md#delete_network_protect_network) | **DELETE** /network-protect/v1/networks/{network_id} | Delete a Network Protect network
[**delete_network_protect_prefix_list**](NetworkProtectApi.md#delete_network_protect_prefix_list) | **DELETE** /network-protect/v1/prefix-lists/{prefix_list_id} | Delete a Network Protect prefix list
[**delete_network_protect_rule_set**](NetworkProtectApi.md#delete_network_protect_rule_set) | **DELETE** /network-protect/v1/rule-sets/{rule_set_id} | Delete a Network Protect rule set
[**get_network_protect_endpoint**](NetworkProtectApi.md#get_network_protect_endpoint) | **GET** /network-protect/v1/endpoints/{endpoint_id} | Get a Network Protect endpoint
[**get_network_protect_network**](NetworkProtectApi.md#get_network_protect_network) | **GET** /network-protect/v1/networks/{network_id} | Get a Network Protect network
[**get_network_protect_prefix_list**](NetworkProtectApi.md#get_network_protect_prefix_list) | **GET** /network-protect/v1/prefix-lists/{prefix_list_id} | Get a Network Protect prefix list
[**get_network_protect_rule_set**](NetworkProtectApi.md#get_network_protect_rule_set) | **GET** /network-protect/v1/rule-sets/{rule_set_id} | Get a Network Protect rule set
[**list_network_protect_endpoints**](NetworkProtectApi.md#list_network_protect_endpoints) | **GET** /network-protect/v1/endpoints | List Network Protect endpoints
[**list_network_protect_networks**](NetworkProtectApi.md#list_network_protect_networks) | **GET** /network-protect/v1/networks | List Network Protect networks
[**list_network_protect_prefix_lists**](NetworkProtectApi.md#list_network_protect_prefix_lists) | **GET** /network-protect/v1/prefix-lists | List Network Protect prefix lists
[**list_network_protect_rule_sets**](NetworkProtectApi.md#list_network_protect_rule_sets) | **GET** /network-protect/v1/rule-sets | List Network Protect rule sets
[**update_network_protect_endpoint**](NetworkProtectApi.md#update_network_protect_endpoint) | **PATCH** /network-protect/v1/endpoints/{endpoint_id} | Update a Network Protect endpoint
[**update_network_protect_network**](NetworkProtectApi.md#update_network_protect_network) | **PATCH** /network-protect/v1/networks/{network_id} | Update a Network Protect network
[**update_network_protect_prefix_list**](NetworkProtectApi.md#update_network_protect_prefix_list) | **PATCH** /network-protect/v1/prefix-lists/{prefix_list_id} | Update a Network Protect prefix list
[**update_network_protect_rule_set**](NetworkProtectApi.md#update_network_protect_rule_set) | **PATCH** /network-protect/v1/rule-sets/{rule_set_id} | Update a Network Protect rule set


# **create_network_protect_endpoint**
> NetworkProtectEndpointResponse create_network_protect_endpoint(network_protect_endpoint_create)

Create a Network Protect endpoint

Creates a GRE delivery destination. A new endpoint is not attached to a network until it is added to an endpoint policy.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_endpoint_create import NetworkProtectEndpointCreate
from fastly.model.network_protect_endpoint_response import NetworkProtectEndpointResponse
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_protect_endpoint_create = NetworkProtectEndpointCreate(
        name=NetworkProtectName("Transit network"),
        ip_address="192.0.2.10",
    ) # NetworkProtectEndpointCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Network Protect endpoint
        api_response = api_instance.create_network_protect_endpoint(network_protect_endpoint_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->create_network_protect_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_protect_endpoint_create** | [**NetworkProtectEndpointCreate**](NetworkProtectEndpointCreate.md)|  |

### Return type

[**NetworkProtectEndpointResponse**](NetworkProtectEndpointResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Protect endpoint was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_protect_network**
> NetworkProtectNetworkResponse create_network_protect_network(network_protect_network_create)

Create a Network Protect network

Registers customer-owned IP space for protection. The network starts with advertisement disabled and Fastly does not announce its prefix. Turn advertisement on after LOA and ROA authorization are ready. The create request cannot include advertise; sending it returns a `400 Bad Request` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_network_create import NetworkProtectNetworkCreate
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_conflict import NetworkProtectConflict
from fastly.model.network_protect_network_response import NetworkProtectNetworkResponse
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_protect_network_create = NetworkProtectNetworkCreate(
        description=NetworkProtectNetworkDescription("Primary application ingress"),
        name=NetworkProtectName("Transit network"),
        prefix="198.51.100.0/24",
        rule_set_id=NetworkProtectNetworkRuleSetIdCreate(""),
        endpoint_policies=NetworkProtectNetworkEndpointPolicies([
            NetworkProtectEndpointPolicy(
                region=NetworkProtectRegion("default"),
                endpoints=NetworkProtectPolicyEndpoints([
                    NetworkProtectPolicyEndpoint(
                        endpoint_id=NetworkProtectId("an7NWnhOjjOkwSNvrwphTd"),
                        preference=NetworkProtectPreference(100),
                    ),
                ]),
            ),
        ]),
    ) # NetworkProtectNetworkCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Network Protect network
        api_response = api_instance.create_network_protect_network(network_protect_network_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->create_network_protect_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_protect_network_create** | [**NetworkProtectNetworkCreate**](NetworkProtectNetworkCreate.md)|  |

### Return type

[**NetworkProtectNetworkResponse**](NetworkProtectNetworkResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Protect network was created. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_protect_prefix_list**
> NetworkProtectPrefixListResponse create_network_protect_prefix_list(network_protect_prefix_list_create)

Create a Network Protect prefix list

Creates a typed list of addresses that rules can reference. The family is required and cannot be changed. The addresses list may remain empty.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_prefix_list_create import NetworkProtectPrefixListCreate
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_prefix_list_response import NetworkProtectPrefixListResponse
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_protect_prefix_list_create = NetworkProtectPrefixListCreate(
        name=NetworkProtectName("Transit network"),
        family=NetworkProtectPrefixListFamily("v4"),
        addresses=NetworkProtectPrefixListRequestAddresses(["192.0.2.20","203.0.113.0/24"]),
    ) # NetworkProtectPrefixListCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Network Protect prefix list
        api_response = api_instance.create_network_protect_prefix_list(network_protect_prefix_list_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->create_network_protect_prefix_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_protect_prefix_list_create** | [**NetworkProtectPrefixListCreate**](NetworkProtectPrefixListCreate.md)|  |

### Return type

[**NetworkProtectPrefixListResponse**](NetworkProtectPrefixListResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Protect prefix list was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_network_protect_rule_set**
> NetworkProtectRuleSetResponse create_network_protect_rule_set(network_protect_rule_set_create)

Create a Network Protect rule set

Creates an ordered rule set and stores its filtering intent. A rule set has at most 64 rules and uses the default action when no rule matches. Custom attachment and detachment are restricted in this release.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_rule_set_response import NetworkProtectRuleSetResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_rule_set_create import NetworkProtectRuleSetCreate
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_protect_rule_set_create = NetworkProtectRuleSetCreate(
        default_action=NetworkProtectRuleSetDefaultAction("block"),
        rules=NetworkProtectRules([
            NetworkProtectRule(
                comment=NetworkProtectRuleComment("Allow application HTTPS traffic"),
                ip_protocol=NetworkProtectRuleIpProtocol("tcp"),
                source_prefix_list_id=NetworkProtectRuleSourcePrefixListId("QoavyX1BHOMGQm2zmVyEbS"),
                destination_ip_address="198.51.100.10",
                source_ports=NetworkProtectRuleSourcePorts(None),
                destination_ports=NetworkProtectRuleDestinationPorts(None),
                action=NetworkProtectRuleAction("allow"),
            ),
        ]),
    ) # NetworkProtectRuleSetCreate | 

    # example passing only required values which don't have defaults set
    try:
        # Create a Network Protect rule set
        api_response = api_instance.create_network_protect_rule_set(network_protect_rule_set_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->create_network_protect_rule_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_protect_rule_set_create** | [**NetworkProtectRuleSetCreate**](NetworkProtectRuleSetCreate.md)|  |

### Return type

[**NetworkProtectRuleSetResponse**](NetworkProtectRuleSetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A Network Protect rule set was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_protect_endpoint**
> delete_network_protect_endpoint(endpoint_id)

Delete a Network Protect endpoint

Deletes an endpoint. The endpoint must first be removed from every network policy; active references return a `409 Conflict` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    endpoint_id = "DBOEWyMXebAir5qwjWEwK1" # str | Unique identifier of the Network Protect endpoint.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Network Protect endpoint
        api_instance.delete_network_protect_endpoint(endpoint_id)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->delete_network_protect_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**| Unique identifier of the Network Protect endpoint. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The endpoint was successfully deleted. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_protect_network**
> delete_network_protect_network(network_id)

Delete a Network Protect network

Deletes a network and stops its advertisement and filtering. Endpoints and rule sets used by the network are not deleted.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_id = "an7NWnhOjjOkwSNvrwphTd" # str | Unique identifier of the Network Protect network.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Network Protect network
        api_instance.delete_network_protect_network(network_id)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->delete_network_protect_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Unique identifier of the Network Protect network. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The network was successfully deleted. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_protect_prefix_list**
> delete_network_protect_prefix_list(prefix_list_id)

Delete a Network Protect prefix list

Deletes a prefix list. Active rule references must be removed first; referenced lists return a `409 Conflict` error. Unknown and foreign IDs are indistinguishable and return a `404 Not Found` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    prefix_list_id = "QoavyX1BHOMGQm2zmVyEbS" # str | Unique identifier of the Network Protect prefix list.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Network Protect prefix list
        api_instance.delete_network_protect_prefix_list(prefix_list_id)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->delete_network_protect_prefix_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix_list_id** | **str**| Unique identifier of the Network Protect prefix list. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The prefix list was successfully deleted. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_network_protect_rule_set**
> delete_network_protect_rule_set(rule_set_id)

Delete a Network Protect rule set

Deletes a rule set. Attached rule sets cannot be deleted and return a `409 Conflict` error until their references are removed.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    rule_set_id = "Z4xQoBznwNb5GJfdJbp58Y" # str | Unique identifier of the Network Protect rule set.

    # example passing only required values which don't have defaults set
    try:
        # Delete a Network Protect rule set
        api_instance.delete_network_protect_rule_set(rule_set_id)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->delete_network_protect_rule_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_set_id** | **str**| Unique identifier of the Network Protect rule set. |

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The rule set was successfully deleted. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_protect_endpoint**
> NetworkProtectEndpointResponse get_network_protect_endpoint(endpoint_id)

Get a Network Protect endpoint

Retrieves a single endpoint by its identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_endpoint_response import NetworkProtectEndpointResponse
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    endpoint_id = "DBOEWyMXebAir5qwjWEwK1" # str | Unique identifier of the Network Protect endpoint.

    # example passing only required values which don't have defaults set
    try:
        # Get a Network Protect endpoint
        api_response = api_instance.get_network_protect_endpoint(endpoint_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->get_network_protect_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**| Unique identifier of the Network Protect endpoint. |

### Return type

[**NetworkProtectEndpointResponse**](NetworkProtectEndpointResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect endpoint was returned. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_protect_network**
> NetworkProtectNetworkResponse get_network_protect_network(network_id)

Get a Network Protect network

Retrieves a single network by its identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_network_response import NetworkProtectNetworkResponse
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_id = "an7NWnhOjjOkwSNvrwphTd" # str | Unique identifier of the Network Protect network.

    # example passing only required values which don't have defaults set
    try:
        # Get a Network Protect network
        api_response = api_instance.get_network_protect_network(network_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->get_network_protect_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Unique identifier of the Network Protect network. |

### Return type

[**NetworkProtectNetworkResponse**](NetworkProtectNetworkResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect network was returned. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_protect_prefix_list**
> NetworkProtectPrefixListResponse get_network_protect_prefix_list(prefix_list_id)

Get a Network Protect prefix list

Retrieves a single prefix list by its identifier. Unknown and foreign IDs are indistinguishable and return a `404 Not Found` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_prefix_list_response import NetworkProtectPrefixListResponse
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    prefix_list_id = "QoavyX1BHOMGQm2zmVyEbS" # str | Unique identifier of the Network Protect prefix list.

    # example passing only required values which don't have defaults set
    try:
        # Get a Network Protect prefix list
        api_response = api_instance.get_network_protect_prefix_list(prefix_list_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->get_network_protect_prefix_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix_list_id** | **str**| Unique identifier of the Network Protect prefix list. |

### Return type

[**NetworkProtectPrefixListResponse**](NetworkProtectPrefixListResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect prefix list was returned. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_network_protect_rule_set**
> NetworkProtectRuleSetResponse get_network_protect_rule_set(rule_set_id)

Get a Network Protect rule set

Retrieves a single rule set with rules in evaluation order.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_rule_set_response import NetworkProtectRuleSetResponse
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    rule_set_id = "Z4xQoBznwNb5GJfdJbp58Y" # str | Unique identifier of the Network Protect rule set.

    # example passing only required values which don't have defaults set
    try:
        # Get a Network Protect rule set
        api_response = api_instance.get_network_protect_rule_set(rule_set_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->get_network_protect_rule_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_set_id** | **str**| Unique identifier of the Network Protect rule set. |

### Return type

[**NetworkProtectRuleSetResponse**](NetworkProtectRuleSetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect rule set was returned. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_protect_endpoints**
> NetworkProtectEndpointsResponse list_network_protect_endpoints()

List Network Protect endpoints

Lists the customer's GRE delivery endpoints in ascending ID order. The response is cursor-paginated and includes the effective page limit.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_endpoints_response import NetworkProtectEndpointsResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    limit = 100 # int | Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. (optional) if omitted the server will use the default value of 100
    cursor = "network-cursor-next" # str | Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Network Protect endpoints
        api_response = api_instance.list_network_protect_endpoints(limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->list_network_protect_endpoints: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Continuation value from a previous response&#39;s meta.next_cursor. Omit this parameter to request the first page. | [optional]

### Return type

[**NetworkProtectEndpointsResponse**](NetworkProtectEndpointsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Protect endpoints were returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_protect_networks**
> NetworkProtectNetworksResponse list_network_protect_networks()

List Network Protect networks

Lists the customer's networks in ascending ID order. The response is cursor-paginated and includes the effective page limit.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_networks_response import NetworkProtectNetworksResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    limit = 100 # int | Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. (optional) if omitted the server will use the default value of 100
    cursor = "network-cursor-next" # str | Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Network Protect networks
        api_response = api_instance.list_network_protect_networks(limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->list_network_protect_networks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Continuation value from a previous response&#39;s meta.next_cursor. Omit this parameter to request the first page. | [optional]

### Return type

[**NetworkProtectNetworksResponse**](NetworkProtectNetworksResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Protect networks were returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_protect_prefix_lists**
> NetworkProtectPrefixListsResponse list_network_protect_prefix_lists()

List Network Protect prefix lists

Lists prefix lists in ascending ID order. Positive limits above 1000 are accepted and clamped to 1000. Invalid limits return a `400 Bad Request` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_prefix_lists_response import NetworkProtectPrefixListsResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    limit = 100 # int | Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. (optional) if omitted the server will use the default value of 100
    cursor = "network-cursor-next" # str | Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Network Protect prefix lists
        api_response = api_instance.list_network_protect_prefix_lists(limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->list_network_protect_prefix_lists: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Continuation value from a previous response&#39;s meta.next_cursor. Omit this parameter to request the first page. | [optional]

### Return type

[**NetworkProtectPrefixListsResponse**](NetworkProtectPrefixListsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Protect prefix lists were returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_network_protect_rule_sets**
> NetworkProtectRuleSetsResponse list_network_protect_rule_sets()

List Network Protect rule sets

Lists rule sets in ascending ID order. Positive limits above 1000 are accepted and clamped to 1000; invalid limits return a `400 Bad Request` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_rule_sets_response import NetworkProtectRuleSetsResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    limit = 100 # int | Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. (optional) if omitted the server will use the default value of 100
    cursor = "network-cursor-next" # str | Continuation value from a previous response's meta.next_cursor. Omit this parameter to request the first page. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List Network Protect rule sets
        api_response = api_instance.list_network_protect_rule_sets(limit=limit, cursor=cursor)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->list_network_protect_rule_sets: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum resources to return. Defaults to 100. Positive values above 1000 are accepted and clamped to 1000; the effective value is reported in meta.limit. Zero, negative, and non-integer values return a `400 Bad Request` error. | [optional] if omitted the server will use the default value of 100
 **cursor** | **str**| Continuation value from a previous response&#39;s meta.next_cursor. Omit this parameter to request the first page. | [optional]

### Return type

[**NetworkProtectRuleSetsResponse**](NetworkProtectRuleSetsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Network Protect rule sets were returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_protect_endpoint**
> NetworkProtectEndpointResponse update_network_protect_endpoint(endpoint_id, network_protect_endpoint_update)

Update a Network Protect endpoint

Updates an endpoint. Omitted fields remain unchanged. The IP address cannot be changed; create a new endpoint if the destination changes.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_endpoint_response import NetworkProtectEndpointResponse
from fastly.model.network_protect_endpoint_update import NetworkProtectEndpointUpdate
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    endpoint_id = "DBOEWyMXebAir5qwjWEwK1" # str | Unique identifier of the Network Protect endpoint.
    network_protect_endpoint_update = NetworkProtectEndpointUpdate(
        name=NetworkProtectName("Transit network"),
    ) # NetworkProtectEndpointUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Network Protect endpoint
        api_response = api_instance.update_network_protect_endpoint(endpoint_id, network_protect_endpoint_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->update_network_protect_endpoint: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **endpoint_id** | **str**| Unique identifier of the Network Protect endpoint. |
 **network_protect_endpoint_update** | [**NetworkProtectEndpointUpdate**](NetworkProtectEndpointUpdate.md)|  |

### Return type

[**NetworkProtectEndpointResponse**](NetworkProtectEndpointResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect endpoint was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_protect_network**
> NetworkProtectNetworkResponse update_network_protect_network(network_id, network_protect_network_update)

Update a Network Protect network

Updates a network. Omitted fields remain unchanged. The prefix cannot be changed. Sending `endpoint_policies` replaces the complete policy list; an empty array removes every policy. Advertisement is desired state. Enabling it requires an approved LOA, a valid ROA, and a ready default-region delivery policy. A readiness failure returns a `409 Conflict` error.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_network_update import NetworkProtectNetworkUpdate
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_conflict import NetworkProtectConflict
from fastly.model.network_protect_network_response import NetworkProtectNetworkResponse
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    network_id = "an7NWnhOjjOkwSNvrwphTd" # str | Unique identifier of the Network Protect network.
    network_protect_network_update = NetworkProtectNetworkUpdate(
        description=NetworkProtectNetworkDescription("Primary application ingress"),
        name=NetworkProtectName("Transit network"),
        rule_set_id=NetworkProtectNetworkRuleSetIdUpdate("u2LC4aWwWL9Y864DZtaGRy"),
        endpoint_policies=NetworkProtectNetworkEndpointPolicies([
            NetworkProtectEndpointPolicy(
                region=NetworkProtectRegion("default"),
                endpoints=NetworkProtectPolicyEndpoints([
                    NetworkProtectPolicyEndpoint(
                        endpoint_id=NetworkProtectId("an7NWnhOjjOkwSNvrwphTd"),
                        preference=NetworkProtectPreference(100),
                    ),
                ]),
            ),
        ]),
        advertise=True,
    ) # NetworkProtectNetworkUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Network Protect network
        api_response = api_instance.update_network_protect_network(network_id, network_protect_network_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->update_network_protect_network: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**| Unique identifier of the Network Protect network. |
 **network_protect_network_update** | [**NetworkProtectNetworkUpdate**](NetworkProtectNetworkUpdate.md)|  |

### Return type

[**NetworkProtectNetworkResponse**](NetworkProtectNetworkResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect network was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_protect_prefix_list**
> NetworkProtectPrefixListResponse update_network_protect_prefix_list(prefix_list_id, network_protect_prefix_list_update)

Update a Network Protect prefix list

Updates a prefix list. The family cannot be changed. Sending addresses replaces the complete list; an empty array clears it when no active source-list restriction applies. Addresses are canonicalized, deduplicated, and sorted by the backend.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_prefix_list_update import NetworkProtectPrefixListUpdate
from fastly.model.network_protect_prefix_list_response import NetworkProtectPrefixListResponse
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    prefix_list_id = "QoavyX1BHOMGQm2zmVyEbS" # str | Unique identifier of the Network Protect prefix list.
    network_protect_prefix_list_update = NetworkProtectPrefixListUpdate(
        name=NetworkProtectName("Transit network"),
        addresses=NetworkProtectPrefixListRequestAddresses(["192.0.2.20","203.0.113.0/24"]),
    ) # NetworkProtectPrefixListUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Network Protect prefix list
        api_response = api_instance.update_network_protect_prefix_list(prefix_list_id, network_protect_prefix_list_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->update_network_protect_prefix_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prefix_list_id** | **str**| Unique identifier of the Network Protect prefix list. |
 **network_protect_prefix_list_update** | [**NetworkProtectPrefixListUpdate**](NetworkProtectPrefixListUpdate.md)|  |

### Return type

[**NetworkProtectPrefixListResponse**](NetworkProtectPrefixListResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect prefix list was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_network_protect_rule_set**
> NetworkProtectRuleSetResponse update_network_protect_rule_set(rule_set_id, network_protect_rule_set_update)

Update a Network Protect rule set

Updates a rule set. Omitted fields remain unchanged. Sending rules replaces the complete ordered list; an empty array removes every rule. Custom attachment and detachment remain restricted in this release.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import network_protect_api
from fastly.model.network_protect_rule_set_response import NetworkProtectRuleSetResponse
from fastly.model.network_protect_invalid_request import NetworkProtectInvalidRequest
from fastly.model.network_protect_rule_set_update import NetworkProtectRuleSetUpdate
from fastly.model.network_protect_conflict import NetworkProtectConflict
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
    api_instance = network_protect_api.NetworkProtectApi(api_client)
    rule_set_id = "Z4xQoBznwNb5GJfdJbp58Y" # str | Unique identifier of the Network Protect rule set.
    network_protect_rule_set_update = NetworkProtectRuleSetUpdate(
        default_action=NetworkProtectRuleSetDefaultAction("block"),
        rules=NetworkProtectRules([
            NetworkProtectRule(
                comment=NetworkProtectRuleComment("Allow application HTTPS traffic"),
                ip_protocol=NetworkProtectRuleIpProtocol("tcp"),
                source_prefix_list_id=NetworkProtectRuleSourcePrefixListId("QoavyX1BHOMGQm2zmVyEbS"),
                destination_ip_address="198.51.100.10",
                source_ports=NetworkProtectRuleSourcePorts(None),
                destination_ports=NetworkProtectRuleDestinationPorts(None),
                action=NetworkProtectRuleAction("allow"),
            ),
        ]),
    ) # NetworkProtectRuleSetUpdate | 

    # example passing only required values which don't have defaults set
    try:
        # Update a Network Protect rule set
        api_response = api_instance.update_network_protect_rule_set(rule_set_id, network_protect_rule_set_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling NetworkProtectApi->update_network_protect_rule_set: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_set_id** | **str**| Unique identifier of the Network Protect rule set. |
 **network_protect_rule_set_update** | [**NetworkProtectRuleSetUpdate**](NetworkProtectRuleSetUpdate.md)|  |

### Return type

[**NetworkProtectRuleSetResponse**](NetworkProtectRuleSetResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A Network Protect rule set was returned. |  -  |
**400** | The request parameters are invalid. |  -  |
**401** | User is not authenticated. |  -  |
**403** | User is not allowed to perform this request. |  -  |
**404** | Entity not found. |  -  |
**409** | The request conflicts with current resource state. |  -  |
**429** | Request was not processed and should be retried later. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

