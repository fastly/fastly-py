# fastly.DmRoutingConfigsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_dm_routing_config_draft**](DmRoutingConfigsApi.md#activate_dm_routing_config_draft) | **POST** /domain-management/v1/routing-configs/{config_id}/activate | Activate the draft
[**create_dm_routing_config**](DmRoutingConfigsApi.md#create_dm_routing_config) | **POST** /domain-management/v1/routing-configs | Create a routing config
[**create_dm_routing_config_path**](DmRoutingConfigsApi.md#create_dm_routing_config_path) | **POST** /domain-management/v1/routing-configs/{config_id}/paths | Create a path
[**create_dm_routing_config_rule**](DmRoutingConfigsApi.md#create_dm_routing_config_rule) | **POST** /domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules | Create a rule
[**deactivate_dm_routing_config**](DmRoutingConfigsApi.md#deactivate_dm_routing_config) | **POST** /domain-management/v1/routing-configs/{config_id}/deactivate | Deactivate a routing config
[**delete_dm_routing_config**](DmRoutingConfigsApi.md#delete_dm_routing_config) | **DELETE** /domain-management/v1/routing-configs/{config_id} | Delete a routing config
[**delete_dm_routing_config_inactive_versions**](DmRoutingConfigsApi.md#delete_dm_routing_config_inactive_versions) | **DELETE** /domain-management/v1/routing-configs/{config_id}/versions/inactive | Delete inactive versions
[**delete_dm_routing_config_path**](DmRoutingConfigsApi.md#delete_dm_routing_config_path) | **DELETE** /domain-management/v1/routing-configs/{config_id}/paths/{path_id} | Delete a path
[**delete_dm_routing_config_rule**](DmRoutingConfigsApi.md#delete_dm_routing_config_rule) | **DELETE** /domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules/{rule_id} | Delete a rule
[**discard_dm_routing_config_draft**](DmRoutingConfigsApi.md#discard_dm_routing_config_draft) | **DELETE** /domain-management/v1/routing-configs/{config_id}/draft | Discard the draft
[**get_dm_routing_config**](DmRoutingConfigsApi.md#get_dm_routing_config) | **GET** /domain-management/v1/routing-configs/{config_id} | Get a routing config
[**get_dm_routing_config_draft_diff**](DmRoutingConfigsApi.md#get_dm_routing_config_draft_diff) | **GET** /domain-management/v1/routing-configs/{config_id}/draft/diff | Get the draft diff
[**get_dm_routing_config_path**](DmRoutingConfigsApi.md#get_dm_routing_config_path) | **GET** /domain-management/v1/routing-configs/{config_id}/paths/{path_id} | Get a path
[**get_dm_routing_config_rule**](DmRoutingConfigsApi.md#get_dm_routing_config_rule) | **GET** /domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules/{rule_id} | Get a rule
[**list_dm_routing_config_paths**](DmRoutingConfigsApi.md#list_dm_routing_config_paths) | **GET** /domain-management/v1/routing-configs/{config_id}/paths | List paths
[**list_dm_routing_config_rules**](DmRoutingConfigsApi.md#list_dm_routing_config_rules) | **GET** /domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules | List rules
[**list_dm_routing_config_versions**](DmRoutingConfigsApi.md#list_dm_routing_config_versions) | **GET** /domain-management/v1/routing-configs/{config_id}/versions | List versions
[**list_dm_routing_configs**](DmRoutingConfigsApi.md#list_dm_routing_configs) | **GET** /domain-management/v1/routing-configs | List routing configs
[**reactivate_dm_routing_config_version**](DmRoutingConfigsApi.md#reactivate_dm_routing_config_version) | **POST** /domain-management/v1/routing-configs/{config_id}/versions/{version_id}/activate | Reactivate a version
[**update_dm_routing_config_draft**](DmRoutingConfigsApi.md#update_dm_routing_config_draft) | **PATCH** /domain-management/v1/routing-configs/{config_id}/draft | Update the draft
[**update_dm_routing_config_path**](DmRoutingConfigsApi.md#update_dm_routing_config_path) | **PATCH** /domain-management/v1/routing-configs/{config_id}/paths/{path_id} | Update a path
[**update_dm_routing_config_rule**](DmRoutingConfigsApi.md#update_dm_routing_config_rule) | **PATCH** /domain-management/v1/routing-configs/{config_id}/paths/{path_id}/rules/{rule_id} | Update a rule


# **activate_dm_routing_config_draft**
> RoutingConfigVersionResponse activate_dm_routing_config_draft(config_id)

Activate the draft

Activate the current draft version. The previously active version, if any, becomes inactive but is retained in version history.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.routing_config_version_response import RoutingConfigVersionResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Activate the draft
        api_response = api_instance.activate_dm_routing_config_draft(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->activate_dm_routing_config_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |

### Return type

[**RoutingConfigVersionResponse**](RoutingConfigVersionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dm_routing_config**
> RoutingConfigResponse create_dm_routing_config()

Create a routing config

Create a new routing config. An optional `initial_version` may be provided to seed the config with paths and rules in a single request, and may also be activated immediately.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.routing_config_response import RoutingConfigResponse
from fastly.model.routing_config import RoutingConfig
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    routing_config = RoutingConfig(
        name=PropertyConfigName("name_example"),
        initial_version=InitialVersion(
            activate=False,
            comment="comment_example",
            paths=[
                InitialVersionPath(
                    path=PropertyPath("path_example"),
                    rules=[
                        RuleCreate(
                            action=Action(
                                type=ActionType("service"),
                                value="value_example",
                            ),
                            conditions=[
                                RoutingConfigCondition(
                                    type=ConditionType("header"),
                                    operator=ConditionOperator("equals"),
                                    key="key_example",
                                    value="value_example",
                                ),
                            ],
                            position=Position(
                                before="before_example",
                                after="after_example",
                            ),
                        ),
                    ],
                ),
            ],
        ),
    ) # RoutingConfig |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a routing config
        api_response = api_instance.create_dm_routing_config(routing_config=routing_config)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->create_dm_routing_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **routing_config** | [**RoutingConfig**](RoutingConfig.md)|  | [optional]

### Return type

[**RoutingConfigResponse**](RoutingConfigResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A routing config. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dm_routing_config_path**
> PathResponse create_dm_routing_config_path(config_id)

Create a path

Add a new path to the config's draft version. If no draft exists, one is created automatically by cloning the active version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.path_response import PathResponse
from fastly.model.path_create import PathCreate
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_create = PathCreate(
        path=PropertyPath("path_example"),
    ) # PathCreate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a path
        api_response = api_instance.create_dm_routing_config_path(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->create_dm_routing_config_path: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a path
        api_response = api_instance.create_dm_routing_config_path(config_id, path_create=path_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->create_dm_routing_config_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_create** | [**PathCreate**](PathCreate.md)|  | [optional]

### Return type

[**PathResponse**](PathResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_dm_routing_config_rule**
> RuleResponse create_dm_routing_config_rule(config_id, path_id)

Create a rule

Add a new rule to a path on the config's draft version. If no draft exists, one is created automatically by cloning the active version. A rule with an empty `conditions` array is a default (catch-all) rule and there can be at most one default rule per path.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.rule_response import RuleResponse
from fastly.model.rule_create import RuleCreate
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 
    rule_create = RuleCreate(
        action=Action(
            type=ActionType("service"),
            value="value_example",
        ),
        conditions=[
            RoutingConfigCondition(
                type=ConditionType("header"),
                operator=ConditionOperator("equals"),
                key="key_example",
                value="value_example",
            ),
        ],
        position=Position(
            before="before_example",
            after="after_example",
        ),
    ) # RuleCreate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Create a rule
        api_response = api_instance.create_dm_routing_config_rule(config_id, path_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->create_dm_routing_config_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a rule
        api_response = api_instance.create_dm_routing_config_rule(config_id, path_id, rule_create=rule_create)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->create_dm_routing_config_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |
 **rule_create** | [**RuleCreate**](RuleCreate.md)|  | [optional]

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A rule. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **deactivate_dm_routing_config**
> RoutingConfigResponse deactivate_dm_routing_config(config_id)

Deactivate a routing config

Clear the active version designation. This is a bookkeeping operation only — it does not stop edge traffic. Minerva continues serving the last-activated version until the domain association is removed in Spotless. Only removing the routing config from the domain (via Spotless) triggers Neptune to drop the reference, which causes Minerva to stop fetching and eventually clean up the cached config. Idempotent: returns 200 even if already deactivated.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.routing_config_response import RoutingConfigResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Deactivate a routing config
        api_response = api_instance.deactivate_dm_routing_config(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->deactivate_dm_routing_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |

### Return type

[**RoutingConfigResponse**](RoutingConfigResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A routing config. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dm_routing_config**
> delete_dm_routing_config(config_id)

Delete a routing config

Delete a routing config. By default, configs that have an active version cannot be deleted. Pass `force=true` to bypass the active-version check — this is destructive and will immediately stop traffic routing for any paths the config serves. The `force` parameter does **not** bypass the domain-association check; if domains are still associated, deletion is rejected with 409 regardless of `force`.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    force = False # bool | When `true`, allows deleting a routing config that has an active version. This is destructive — traffic routing for any paths served by the config will stop immediately. (optional) if omitted the server will use the default value of False

    # example passing only required values which don't have defaults set
    try:
        # Delete a routing config
        api_instance.delete_dm_routing_config(config_id)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->delete_dm_routing_config: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Delete a routing config
        api_instance.delete_dm_routing_config(config_id, force=force)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->delete_dm_routing_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **force** | **bool**| When `true`, allows deleting a routing config that has an active version. This is destructive — traffic routing for any paths served by the config will stop immediately. | [optional] if omitted the server will use the default value of False

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
**204** | No content. |  -  |
**409** | One or more domains are still associated with this routing configuration. Remove all domain associations first. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dm_routing_config_inactive_versions**
> delete_dm_routing_config_inactive_versions(config_id)

Delete inactive versions

Delete all inactive versions for a routing config. The currently active version, if any, is retained.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete inactive versions
        api_instance.delete_dm_routing_config_inactive_versions(config_id)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->delete_dm_routing_config_inactive_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |

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
**204** | No content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dm_routing_config_path**
> delete_dm_routing_config_path(config_id, path_id)

Delete a path

Delete a path from the config's draft version. If no draft exists, one is created automatically by cloning the active version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a path
        api_instance.delete_dm_routing_config_path(config_id, path_id)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->delete_dm_routing_config_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |

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
**204** | No content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dm_routing_config_rule**
> delete_dm_routing_config_rule(config_id, path_id, rule_id)

Delete a rule

Delete a rule from the config's draft version. If no draft exists, one is created automatically by cloning the active version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 
    rule_id = "rule_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete a rule
        api_instance.delete_dm_routing_config_rule(config_id, path_id, rule_id)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->delete_dm_routing_config_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |
 **rule_id** | **str**|  |

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
**204** | No content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discard_dm_routing_config_draft**
> discard_dm_routing_config_draft(config_id)

Discard the draft

Delete the current draft version, reverting any unactivated changes.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Discard the draft
        api_instance.discard_dm_routing_config_draft(config_id)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->discard_dm_routing_config_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |

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
**204** | No content. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dm_routing_config**
> RoutingConfigResponse get_dm_routing_config(config_id)

Get a routing config

Retrieve a single routing config by its identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.routing_config_response import RoutingConfigResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a routing config
        api_response = api_instance.get_dm_routing_config(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->get_dm_routing_config: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |

### Return type

[**RoutingConfigResponse**](RoutingConfigResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A routing config. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dm_routing_config_draft_diff**
> DraftDiff get_dm_routing_config_draft_diff(config_id)

Get the draft diff

Compare the current draft version against the active version and return the paths and rules that have been added, modified, or deleted.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.draft_diff import DraftDiff
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get the draft diff
        api_response = api_instance.get_dm_routing_config_draft_diff(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->get_dm_routing_config_draft_diff: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |

### Return type

[**DraftDiff**](DraftDiff.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A diff between the draft and active versions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dm_routing_config_path**
> PathResponse get_dm_routing_config_path(config_id, path_id)

Get a path

Retrieve a single path by its stable identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.path_response import PathResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a path
        api_response = api_instance.get_dm_routing_config_path(config_id, path_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->get_dm_routing_config_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |

### Return type

[**PathResponse**](PathResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dm_routing_config_rule**
> RuleResponse get_dm_routing_config_rule(config_id, path_id, rule_id)

Get a rule

Retrieve a single rule by its stable identifier.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.rule_response import RuleResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 
    rule_id = "rule_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Get a rule
        api_response = api_instance.get_dm_routing_config_rule(config_id, path_id, rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->get_dm_routing_config_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |
 **rule_id** | **str**|  |

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A rule. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dm_routing_config_paths**
> PathsResponse list_dm_routing_config_paths(config_id)

List paths

List paths for the config. Returns paths from the active version if one exists, otherwise from the draft.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.paths_response import PathsResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path = "path_example" # str | Filter results by path pattern. The match strategy is controlled by the `match` parameter. (optional)
    match = "exact" # str | How to match the value of the `path` filter against existing path patterns. Has no effect unless `path` is also provided. (optional) if omitted the server will use the default value of "exact"
    sort = "-created_at" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "-created_at"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List paths
        api_response = api_instance.list_dm_routing_config_paths(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_config_paths: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List paths
        api_response = api_instance.list_dm_routing_config_paths(config_id, path=path, match=match, sort=sort, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_config_paths: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path** | **str**| Filter results by path pattern. The match strategy is controlled by the `match` parameter. | [optional]
 **match** | **str**| How to match the value of the `path` filter against existing path patterns. Has no effect unless `path` is also provided. | [optional] if omitted the server will use the default value of "exact"
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "-created_at"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20

### Return type

[**PathsResponse**](PathsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of paths. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dm_routing_config_rules**
> RulesResponse list_dm_routing_config_rules(config_id, path_id)

List rules

List all rules for a path in evaluation order.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.rules_response import RulesResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 
    sort = "position" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "position"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List rules
        api_response = api_instance.list_dm_routing_config_rules(config_id, path_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_config_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List rules
        api_response = api_instance.list_dm_routing_config_rules(config_id, path_id, sort=sort, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_config_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "position"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20

### Return type

[**RulesResponse**](RulesResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of rules. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dm_routing_config_versions**
> VersionsResponse list_dm_routing_config_versions(config_id)

List versions

List all versions for a routing config.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.versions_response import VersionsResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    sort = "-activated_at" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "-activated_at"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    try:
        # List versions
        api_response = api_instance.list_dm_routing_config_versions(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_config_versions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List versions
        api_response = api_instance.list_dm_routing_config_versions(config_id, sort=sort, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_config_versions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "-activated_at"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20

### Return type

[**VersionsResponse**](VersionsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of versions. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dm_routing_configs**
> RoutingConfigsResponse list_dm_routing_configs()

List routing configs

List all routing configs for the authenticated customer.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.routing_configs_response import RoutingConfigsResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    state = [
        "draft-only",
    ] # [str] | Filter configs by lifecycle state. Accepts a comma-separated list of state values (e.g. `?state=active,active-with-draft`). Returns only configs whose current state matches one of the provided values. Returns 400 if any value is not a recognised state. (optional)
    sort = "-created_at" # str | The order in which to list the results. (optional) if omitted the server will use the default value of "-created_at"
    cursor = "cursor_example" # str | Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. (optional)
    limit = 20 # int | Limit how many results are returned. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List routing configs
        api_response = api_instance.list_dm_routing_configs(state=state, sort=sort, cursor=cursor, limit=limit)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->list_dm_routing_configs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **state** | **[str]**| Filter configs by lifecycle state. Accepts a comma-separated list of state values (e.g. `?state&#x3D;active,active-with-draft`). Returns only configs whose current state matches one of the provided values. Returns 400 if any value is not a recognised state. | [optional]
 **sort** | **str**| The order in which to list the results. | [optional] if omitted the server will use the default value of "-created_at"
 **cursor** | **str**| Cursor value from the `next_cursor` field of a previous response, used to retrieve the next page. To request the first page, this should be empty. | [optional]
 **limit** | **int**| Limit how many results are returned. | [optional] if omitted the server will use the default value of 20

### Return type

[**RoutingConfigsResponse**](RoutingConfigsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A list of routing configs. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reactivate_dm_routing_config_version**
> RoutingConfigVersionResponse reactivate_dm_routing_config_version(config_id, version_id)

Reactivate a version

Reactivate a previously-active version. The currently active version, if any, becomes inactive but is retained in version history.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.routing_config_version_response import RoutingConfigVersionResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    version_id = "version_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Reactivate a version
        api_response = api_instance.reactivate_dm_routing_config_version(config_id, version_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->reactivate_dm_routing_config_version: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **version_id** | **str**|  |

### Return type

[**RoutingConfigVersionResponse**](RoutingConfigVersionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dm_routing_config_draft**
> RoutingConfigVersionResponse update_dm_routing_config_draft(config_id)

Update the draft

Update metadata on the draft version, such as its comment. If no draft exists, one is created automatically by cloning the active version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.draft_update import DraftUpdate
from fastly.model.routing_config_version_response import RoutingConfigVersionResponse
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    draft_update = DraftUpdate(
        comment="comment_example",
    ) # DraftUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update the draft
        api_response = api_instance.update_dm_routing_config_draft(config_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->update_dm_routing_config_draft: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update the draft
        api_response = api_instance.update_dm_routing_config_draft(config_id, draft_update=draft_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->update_dm_routing_config_draft: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **draft_update** | [**DraftUpdate**](DraftUpdate.md)|  | [optional]

### Return type

[**RoutingConfigVersionResponse**](RoutingConfigVersionResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dm_routing_config_path**
> PathResponse update_dm_routing_config_path(config_id, path_id)

Update a path

Update a path on the config's draft version. If no draft exists, one is created automatically by cloning the active version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.path_response import PathResponse
from fastly.model.path_update import PathUpdate
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 
    path_update = PathUpdate(
        path=PropertyPath("path_example"),
    ) # PathUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a path
        api_response = api_instance.update_dm_routing_config_path(config_id, path_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->update_dm_routing_config_path: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a path
        api_response = api_instance.update_dm_routing_config_path(config_id, path_id, path_update=path_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->update_dm_routing_config_path: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |
 **path_update** | [**PathUpdate**](PathUpdate.md)|  | [optional]

### Return type

[**PathResponse**](PathResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A path. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dm_routing_config_rule**
> RuleResponse update_dm_routing_config_rule(config_id, path_id, rule_id)

Update a rule

Update a rule on the config's draft version. If no draft exists, one is created automatically by cloning the active version.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import dm_routing_configs_api
from fastly.model.rule_response import RuleResponse
from fastly.model.rule_update import RuleUpdate
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
    api_instance = dm_routing_configs_api.DmRoutingConfigsApi(api_client)
    config_id = "config_id_example" # str | 
    path_id = "path_id_example" # str | 
    rule_id = "rule_id_example" # str | 
    rule_update = RuleUpdate(
        action=Action(
            type=ActionType("service"),
            value="value_example",
        ),
        conditions=[
            RoutingConfigCondition(
                type=ConditionType("header"),
                operator=ConditionOperator("equals"),
                key="key_example",
                value="value_example",
            ),
        ],
        position=Position(
            before="before_example",
            after="after_example",
        ),
    ) # RuleUpdate |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update a rule
        api_response = api_instance.update_dm_routing_config_rule(config_id, path_id, rule_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->update_dm_routing_config_rule: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update a rule
        api_response = api_instance.update_dm_routing_config_rule(config_id, path_id, rule_id, rule_update=rule_update)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling DmRoutingConfigsApi->update_dm_routing_config_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **config_id** | **str**|  |
 **path_id** | **str**|  |
 **rule_id** | **str**|  |
 **rule_update** | [**RuleUpdate**](RuleUpdate.md)|  | [optional]

### Return type

[**RuleResponse**](RuleResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A rule. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

