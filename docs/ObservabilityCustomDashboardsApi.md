# fastly.ObservabilityCustomDashboardsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dashboard**](ObservabilityCustomDashboardsApi.md#create_dashboard) | **POST** /observability/dashboards | Create a new dashboard
[**delete_dashboard**](ObservabilityCustomDashboardsApi.md#delete_dashboard) | **DELETE** /observability/dashboards/{dashboard_id} | Delete an existing dashboard
[**get_dashboard**](ObservabilityCustomDashboardsApi.md#get_dashboard) | **GET** /observability/dashboards/{dashboard_id} | Retrieve a dashboard by ID
[**list_dashboards**](ObservabilityCustomDashboardsApi.md#list_dashboards) | **GET** /observability/dashboards | List all custom dashboards
[**update_dashboard**](ObservabilityCustomDashboardsApi.md#update_dashboard) | **PATCH** /observability/dashboards/{dashboard_id} | Update an existing dashboard


# **create_dashboard**
> Dashboard create_dashboard()

Create a new dashboard

Create a new dashboard

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_custom_dashboards_api
from fastly.model.dashboard import Dashboard
from fastly.model.create_dashboard_request import CreateDashboardRequest
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
    api_instance = observability_custom_dashboards_api.ObservabilityCustomDashboardsApi(api_client)
    create_dashboard_request = CreateDashboardRequest(
        name="name_example",
        description="description_example",
        items=DashboardPropertyItems([
            DashboardItem(
                title=DashboardItemPropertyTitle("title_example"),
                subtitle=DashboardItemPropertySubtitle("subtitle_example"),
                data_source=DashboardItemPropertyDataSource(
                    type="stats.edge",
                    config=DashboardItemPropertyDataSourcePropertyConfig(
                        metrics=[
                            "metrics_example",
                        ],
                    ),
                ),
                visualization=DashboardItemPropertyVisualization(
                    type="chart",
                    config=DashboardItemPropertyVisualizationPropertyConfig(
                        plot_type="line",
                        format="number",
                        calculation_method="avg",
                    ),
                ),
                span=DashboardItemPropertySpan(4),
            ),
        ]),
    ) # CreateDashboardRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create a new dashboard
        api_response = api_instance.create_dashboard(create_dashboard_request=create_dashboard_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityCustomDashboardsApi->create_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_dashboard_request** | [**CreateDashboardRequest**](CreateDashboardRequest.md)|  | [optional]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dashboard**
> delete_dashboard(dashboard_id)

Delete an existing dashboard

Delete an existing dashboard

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_custom_dashboards_api
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
    api_instance = observability_custom_dashboards_api.ObservabilityCustomDashboardsApi(api_client)
    dashboard_id = "2eGFXF4F4kTxd4gU39Bg3e" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Delete an existing dashboard
        api_instance.delete_dashboard(dashboard_id)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityCustomDashboardsApi->delete_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  |

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

# **get_dashboard**
> Dashboard get_dashboard(dashboard_id)

Retrieve a dashboard by ID

Retrieve a dashboard by ID

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_custom_dashboards_api
from fastly.model.dashboard import Dashboard
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
    api_instance = observability_custom_dashboards_api.ObservabilityCustomDashboardsApi(api_client)
    dashboard_id = "2eGFXF4F4kTxd4gU39Bg3e" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Retrieve a dashboard by ID
        api_response = api_instance.get_dashboard(dashboard_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityCustomDashboardsApi->get_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  |

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Requested dashboard |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dashboards**
> ListDashboardsResponse list_dashboards()

List all custom dashboards

List all custom dashboards

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_custom_dashboards_api
from fastly.model.list_dashboards_response import ListDashboardsResponse
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
    api_instance = observability_custom_dashboards_api.ObservabilityCustomDashboardsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List all custom dashboards
        api_response = api_instance.list_dashboards()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityCustomDashboardsApi->list_dashboards: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**ListDashboardsResponse**](ListDashboardsResponse.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all custom dashboards |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dashboard**
> Dashboard update_dashboard(dashboard_id)

Update an existing dashboard

Update an existing dashboard

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import observability_custom_dashboards_api
from fastly.model.dashboard import Dashboard
from fastly.model.update_dashboard_request import UpdateDashboardRequest
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
    api_instance = observability_custom_dashboards_api.ObservabilityCustomDashboardsApi(api_client)
    dashboard_id = "2eGFXF4F4kTxd4gU39Bg3e" # str | 
    update_dashboard_request = UpdateDashboardRequest(
        name="name_example",
        description="description_example",
        items=DashboardPropertyItems([
            DashboardItem(
                title=DashboardItemPropertyTitle("title_example"),
                subtitle=DashboardItemPropertySubtitle("subtitle_example"),
                data_source=DashboardItemPropertyDataSource(
                    type="stats.edge",
                    config=DashboardItemPropertyDataSourcePropertyConfig(
                        metrics=[
                            "metrics_example",
                        ],
                    ),
                ),
                visualization=DashboardItemPropertyVisualization(
                    type="chart",
                    config=DashboardItemPropertyVisualizationPropertyConfig(
                        plot_type="line",
                        format="number",
                        calculation_method="avg",
                    ),
                ),
                span=DashboardItemPropertySpan(4),
            ),
        ]),
    ) # UpdateDashboardRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        # Update an existing dashboard
        api_response = api_instance.update_dashboard(dashboard_id)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityCustomDashboardsApi->update_dashboard: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Update an existing dashboard
        api_response = api_instance.update_dashboard(dashboard_id, update_dashboard_request=update_dashboard_request)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling ObservabilityCustomDashboardsApi->update_dashboard: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **str**|  |
 **update_dashboard_request** | [**UpdateDashboardRequest**](UpdateDashboardRequest.md)|  | [optional]

### Return type

[**Dashboard**](Dashboard.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update was successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

