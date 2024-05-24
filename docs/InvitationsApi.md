# fastly.InvitationsApi

> [!NOTE]
> All URIs are relative to `https://api.fastly.com`

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invitation**](InvitationsApi.md#create_invitation) | **POST** /invitations | Create an invitation
[**delete_invitation**](InvitationsApi.md#delete_invitation) | **DELETE** /invitations/{invitation_id} | Delete an invitation
[**list_invitations**](InvitationsApi.md#list_invitations) | **GET** /invitations | List invitations


# **create_invitation**
> InvitationResponse create_invitation()

Create an invitation

Create an invitation.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import invitations_api
from fastly.model.invitation_response import InvitationResponse
from fastly.model.invitation import Invitation
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
    api_instance = invitations_api.InvitationsApi(api_client)
    invitation = Invitation(
        data=InvitationData(
            type=TypeInvitation("invitation"),
            attributes=InvitationDataAttributes(
                email="email_example",
                limit_services=True,
                role=RoleUser("user"),
                status_code=0,
            ),
            relationships=RelationshipServiceInvitationsCreate(
                service_invitations=RelationshipServiceInvitationsCreateServiceInvitations(
                    data=[
                        ServiceInvitation(
                            data=ServiceInvitationData(
                                type=TypeServiceInvitation("service_invitation"),
                                attributes=ServiceInvitationDataAttributes(
                                    permission="full",
                                ),
                                relationships=ServiceInvitationDataRelationships(
                                    service=RelationshipMemberService(
                                        type=TypeService("service"),
                                    ),
                                ),
                            ),
                        ),
                    ],
                ),
            ),
        ),
    ) # Invitation |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Create an invitation
        api_response = api_instance.create_invitation(invitation=invitation)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling InvitationsApi->create_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**Invitation**](Invitation.md)|  | [optional]

### Return type

[**InvitationResponse**](InvitationResponse.md)

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

# **delete_invitation**
> delete_invitation(invitation_id)

Delete an invitation

Delete an invitation.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import invitations_api
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
    api_instance = invitations_api.InvitationsApi(api_client)
    invitation_id = "3krg2uUGZzb2W9Euo4moOY" # str | Alphanumeric string identifying an invitation.

    # example passing only required values which don't have defaults set
    try:
        # Delete an invitation
        api_instance.delete_invitation(invitation_id)
    except fastly.ApiException as e:
        print("Exception when calling InvitationsApi->delete_invitation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation_id** | **str**| Alphanumeric string identifying an invitation. |

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

# **list_invitations**
> InvitationsResponse list_invitations()

List invitations

List all invitations.

### Example

* Api Key Authentication (token):

```python
import time
import fastly
from fastly.api import invitations_api
from fastly.model.invitations_response import InvitationsResponse
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
    api_instance = invitations_api.InvitationsApi(api_client)
    page_number = 1 # int | Current page. (optional)
    page_size = 20 # int | Number of records per page. (optional) if omitted the server will use the default value of 20

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # List invitations
        api_response = api_instance.list_invitations(page_number=page_number, page_size=page_size)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling InvitationsApi->list_invitations: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page_number** | **int**| Current page. | [optional]
 **page_size** | **int**| Number of records per page. | [optional] if omitted the server will use the default value of 20

### Return type

[**InvitationsResponse**](InvitationsResponse.md)

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

