# fastly-py

A Python client library for interacting with most facets of the [Fastly API](https://www.fastly.com/documentation/reference/api/).


## Requirements

Python >=3.6

## Installation

```sh
python3 -m pip install fastly
```

## Usage

```python
import fastly
from fastly.api import acl_api
from pprint import pprint

# Authorize the client with a Fastly API token.
configuration = fastly.Configuration()
configuration.api_token = 'YOUR_API_KEY'

# Enter a context with an instance of the API client
with fastly.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = acl_api.AclApi(api_client)
    service_id = "SU1Z0isxPaozGVKXdv0eY" # str
    version_id = 1 # int
    name = "test-acl" # str

    try:
        # Create a new ACL
        api_response = api_instance.create_acl(service_id, version_id, name=name)
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling AclApi->create_acl: %s\n" % e)
```

## Authorization

> [!NOTE]
> The Fastly API requires an [API token](https://www.fastly.com/documentation/reference/api/#authentication) for most operations.

Set it by assigning `api_token` to a configuration as shown:

```python
# Authorize the client with a Fastly API token.
configuration = fastly.Configuration()
configuration.api_token = 'YOUR_API_KEY'
```

Alternatively, set the `FASTLY_API_TOKEN` environment variable.

## API Endpoints

<details>

<summary>Table of API endpoints</summary>

Class | Method | Description
----- | ------ | -----------
*AclApi* | [**create_acl**](docs/AclApi.md#create_acl) | Create a new ACL
*AclApi* | [**delete_acl**](docs/AclApi.md#delete_acl) | Delete an ACL
*AclApi* | [**get_acl**](docs/AclApi.md#get_acl) | Describe an ACL
*AclApi* | [**list_acls**](docs/AclApi.md#list_acls) | List ACLs
*AclApi* | [**update_acl**](docs/AclApi.md#update_acl) | Update an ACL
*AclEntryApi* | [**bulk_update_acl_entries**](docs/AclEntryApi.md#bulk_update_acl_entries) | Update multiple ACL entries
*AclEntryApi* | [**create_acl_entry**](docs/AclEntryApi.md#create_acl_entry) | Create an ACL entry
*AclEntryApi* | [**delete_acl_entry**](docs/AclEntryApi.md#delete_acl_entry) | Delete an ACL entry
*AclEntryApi* | [**get_acl_entry**](docs/AclEntryApi.md#get_acl_entry) | Describe an ACL entry
*AclEntryApi* | [**list_acl_entries**](docs/AclEntryApi.md#list_acl_entries) | List ACL entries
*AclEntryApi* | [**update_acl_entry**](docs/AclEntryApi.md#update_acl_entry) | Update an ACL entry
*AclsInComputeApi* | [**compute_acl_create_acls**](docs/AclsInComputeApi.md#compute_acl_create_acls) | Create a new ACL
*AclsInComputeApi* | [**compute_acl_delete_s_acl_id**](docs/AclsInComputeApi.md#compute_acl_delete_s_acl_id) | Delete an ACL
*AclsInComputeApi* | [**compute_acl_list_acl_entries**](docs/AclsInComputeApi.md#compute_acl_list_acl_entries) | List an ACL
*AclsInComputeApi* | [**compute_acl_list_acls**](docs/AclsInComputeApi.md#compute_acl_list_acls) | List ACLs
*AclsInComputeApi* | [**compute_acl_list_acls_s_acl_id**](docs/AclsInComputeApi.md#compute_acl_list_acls_s_acl_id) | Describe an ACL
*AclsInComputeApi* | [**compute_acl_lookup_acls**](docs/AclsInComputeApi.md#compute_acl_lookup_acls) | Lookup an ACL
*AclsInComputeApi* | [**compute_acl_update_acls**](docs/AclsInComputeApi.md#compute_acl_update_acls) | Update an ACL
*ApexRedirectApi* | [**create_apex_redirect**](docs/ApexRedirectApi.md#create_apex_redirect) | Create an apex redirect
*ApexRedirectApi* | [**delete_apex_redirect**](docs/ApexRedirectApi.md#delete_apex_redirect) | Delete an apex redirect
*ApexRedirectApi* | [**get_apex_redirect**](docs/ApexRedirectApi.md#get_apex_redirect) | Get an apex redirect
*ApexRedirectApi* | [**list_apex_redirects**](docs/ApexRedirectApi.md#list_apex_redirects) | List apex redirects
*ApexRedirectApi* | [**update_apex_redirect**](docs/ApexRedirectApi.md#update_apex_redirect) | Update an apex redirect
*AutomationTokensApi* | [**create_automation_token**](docs/AutomationTokensApi.md#create_automation_token) | Create Automation Token
*AutomationTokensApi* | [**get_automation_token_id**](docs/AutomationTokensApi.md#get_automation_token_id) | Retrieve an Automation Token by ID
*AutomationTokensApi* | [**get_automation_tokens_id_services**](docs/AutomationTokensApi.md#get_automation_tokens_id_services) | List Automation Token Services
*AutomationTokensApi* | [**list_automation_tokens**](docs/AutomationTokensApi.md#list_automation_tokens) | List Customer Automation Tokens
*AutomationTokensApi* | [**revoke_automation_token_id**](docs/AutomationTokensApi.md#revoke_automation_token_id) | Revoke an Automation Token by ID
*BackendApi* | [**create_backend**](docs/BackendApi.md#create_backend) | Create a backend
*BackendApi* | [**delete_backend**](docs/BackendApi.md#delete_backend) | Delete a backend
*BackendApi* | [**get_backend**](docs/BackendApi.md#get_backend) | Describe a backend
*BackendApi* | [**list_backends**](docs/BackendApi.md#list_backends) | List backends
*BackendApi* | [**update_backend**](docs/BackendApi.md#update_backend) | Update a backend
*BillingAddressApi* | [**add_billing_addr**](docs/BillingAddressApi.md#add_billing_addr) | Add a billing address to a customer
*BillingAddressApi* | [**delete_billing_addr**](docs/BillingAddressApi.md#delete_billing_addr) | Delete a billing address
*BillingAddressApi* | [**get_billing_addr**](docs/BillingAddressApi.md#get_billing_addr) | Get a billing address
*BillingAddressApi* | [**update_billing_addr**](docs/BillingAddressApi.md#update_billing_addr) | Update a billing address
*BillingInvoicesApi* | [**get_invoice_by_invoice_id**](docs/BillingInvoicesApi.md#get_invoice_by_invoice_id) | Get invoice by ID.
*BillingInvoicesApi* | [**get_month_to_date_invoice**](docs/BillingInvoicesApi.md#get_month_to_date_invoice) | Get month-to-date invoice.
*BillingInvoicesApi* | [**list_invoices**](docs/BillingInvoicesApi.md#list_invoices) | List of invoices.
*BillingUsageMetricsApi* | [**get_service_level_usage**](docs/BillingUsageMetricsApi.md#get_service_level_usage) | Retrieve service-level usage metrics for services with non-zero usage units.
*BillingUsageMetricsApi* | [**get_usage_metrics**](docs/BillingUsageMetricsApi.md#get_usage_metrics) | Get monthly usage metrics
*CacheSettingsApi* | [**create_cache_settings**](docs/CacheSettingsApi.md#create_cache_settings) | Create a cache settings object
*CacheSettingsApi* | [**delete_cache_settings**](docs/CacheSettingsApi.md#delete_cache_settings) | Delete a cache settings object
*CacheSettingsApi* | [**get_cache_settings**](docs/CacheSettingsApi.md#get_cache_settings) | Get a cache settings object
*CacheSettingsApi* | [**list_cache_settings**](docs/CacheSettingsApi.md#list_cache_settings) | List cache settings objects
*CacheSettingsApi* | [**update_cache_settings**](docs/CacheSettingsApi.md#update_cache_settings) | Update a cache settings object
*ConditionApi* | [**create_condition**](docs/ConditionApi.md#create_condition) | Create a condition
*ConditionApi* | [**delete_condition**](docs/ConditionApi.md#delete_condition) | Delete a condition
*ConditionApi* | [**get_condition**](docs/ConditionApi.md#get_condition) | Describe a condition
*ConditionApi* | [**list_conditions**](docs/ConditionApi.md#list_conditions) | List conditions
*ConditionApi* | [**update_condition**](docs/ConditionApi.md#update_condition) | Update a condition
*ConfigStoreApi* | [**create_config_store**](docs/ConfigStoreApi.md#create_config_store) | Create a config store
*ConfigStoreApi* | [**delete_config_store**](docs/ConfigStoreApi.md#delete_config_store) | Delete a config store
*ConfigStoreApi* | [**get_config_store**](docs/ConfigStoreApi.md#get_config_store) | Describe a config store
*ConfigStoreApi* | [**get_config_store_info**](docs/ConfigStoreApi.md#get_config_store_info) | Get config store metadata
*ConfigStoreApi* | [**list_config_store_services**](docs/ConfigStoreApi.md#list_config_store_services) | List linked services
*ConfigStoreApi* | [**list_config_stores**](docs/ConfigStoreApi.md#list_config_stores) | List config stores
*ConfigStoreApi* | [**update_config_store**](docs/ConfigStoreApi.md#update_config_store) | Update a config store
*ConfigStoreItemApi* | [**bulk_update_config_store_item**](docs/ConfigStoreItemApi.md#bulk_update_config_store_item) | Update multiple entries in a config store
*ConfigStoreItemApi* | [**create_config_store_item**](docs/ConfigStoreItemApi.md#create_config_store_item) | Create an entry in a config store
*ConfigStoreItemApi* | [**delete_config_store_item**](docs/ConfigStoreItemApi.md#delete_config_store_item) | Delete an item from a config store
*ConfigStoreItemApi* | [**get_config_store_item**](docs/ConfigStoreItemApi.md#get_config_store_item) | Get an item from a config store
*ConfigStoreItemApi* | [**list_config_store_items**](docs/ConfigStoreItemApi.md#list_config_store_items) | List items in a config store
*ConfigStoreItemApi* | [**update_config_store_item**](docs/ConfigStoreItemApi.md#update_config_store_item) | Update an entry in a config store
*ConfigStoreItemApi* | [**upsert_config_store_item**](docs/ConfigStoreItemApi.md#upsert_config_store_item) | Insert or update an entry in a config store
*ContactApi* | [**create_contacts**](docs/ContactApi.md#create_contacts) | Add a new customer contact
*ContactApi* | [**delete_contact**](docs/ContactApi.md#delete_contact) | Delete a contact
*ContactApi* | [**list_contacts**](docs/ContactApi.md#list_contacts) | List contacts
*ContentApi* | [**content_check**](docs/ContentApi.md#content_check) | Check status of content in each POP&#39;s cache
*CustomerApi* | [**delete_customer**](docs/CustomerApi.md#delete_customer) | Delete a customer
*CustomerApi* | [**get_customer**](docs/CustomerApi.md#get_customer) | Get a customer
*CustomerApi* | [**get_logged_in_customer**](docs/CustomerApi.md#get_logged_in_customer) | Get the logged in customer
*CustomerApi* | [**list_users**](docs/CustomerApi.md#list_users) | List users
*CustomerApi* | [**update_customer**](docs/CustomerApi.md#update_customer) | Update a customer
*CustomerAddressesApi* | [**create_customer_address**](docs/CustomerAddressesApi.md#create_customer_address) | Creates an address associated with a customer account.
*CustomerAddressesApi* | [**list_customer_addresses**](docs/CustomerAddressesApi.md#list_customer_addresses) | Return the list of addresses associated with a customer account.
*CustomerAddressesApi* | [**update_customer_address**](docs/CustomerAddressesApi.md#update_customer_address) | Updates an address associated with a customer account.
*DictionaryApi* | [**create_dictionary**](docs/DictionaryApi.md#create_dictionary) | Create an edge dictionary
*DictionaryApi* | [**delete_dictionary**](docs/DictionaryApi.md#delete_dictionary) | Delete an edge dictionary
*DictionaryApi* | [**get_dictionary**](docs/DictionaryApi.md#get_dictionary) | Get an edge dictionary
*DictionaryApi* | [**list_dictionaries**](docs/DictionaryApi.md#list_dictionaries) | List edge dictionaries
*DictionaryApi* | [**update_dictionary**](docs/DictionaryApi.md#update_dictionary) | Update an edge dictionary
*DictionaryInfoApi* | [**get_dictionary_info**](docs/DictionaryInfoApi.md#get_dictionary_info) | Get edge dictionary metadata
*DictionaryItemApi* | [**bulk_update_dictionary_item**](docs/DictionaryItemApi.md#bulk_update_dictionary_item) | Update multiple entries in an edge dictionary
*DictionaryItemApi* | [**create_dictionary_item**](docs/DictionaryItemApi.md#create_dictionary_item) | Create an entry in an edge dictionary
*DictionaryItemApi* | [**delete_dictionary_item**](docs/DictionaryItemApi.md#delete_dictionary_item) | Delete an item from an edge dictionary
*DictionaryItemApi* | [**get_dictionary_item**](docs/DictionaryItemApi.md#get_dictionary_item) | Get an item from an edge dictionary
*DictionaryItemApi* | [**list_dictionary_items**](docs/DictionaryItemApi.md#list_dictionary_items) | List items in an edge dictionary
*DictionaryItemApi* | [**update_dictionary_item**](docs/DictionaryItemApi.md#update_dictionary_item) | Update an entry in an edge dictionary
*DictionaryItemApi* | [**upsert_dictionary_item**](docs/DictionaryItemApi.md#upsert_dictionary_item) | Insert or update an entry in an edge dictionary
*DiffApi* | [**diff_service_versions**](docs/DiffApi.md#diff_service_versions) | Diff two service versions
*DirectorApi* | [**create_director**](docs/DirectorApi.md#create_director) | Create a director
*DirectorApi* | [**delete_director**](docs/DirectorApi.md#delete_director) | Delete a director
*DirectorApi* | [**get_director**](docs/DirectorApi.md#get_director) | Get a director
*DirectorApi* | [**list_directors**](docs/DirectorApi.md#list_directors) | List directors
*DirectorApi* | [**update_director**](docs/DirectorApi.md#update_director) | Update a director
*DirectorBackendApi* | [**create_director_backend**](docs/DirectorBackendApi.md#create_director_backend) | Create a director-backend relationship
*DirectorBackendApi* | [**delete_director_backend**](docs/DirectorBackendApi.md#delete_director_backend) | Delete a director-backend relationship
*DirectorBackendApi* | [**get_director_backend**](docs/DirectorBackendApi.md#get_director_backend) | Get a director-backend relationship
*DomainApi* | [**check_domain**](docs/DomainApi.md#check_domain) | Validate DNS configuration for a single domain on a service
*DomainApi* | [**check_domains**](docs/DomainApi.md#check_domains) | Validate DNS configuration for all domains on a service
*DomainApi* | [**create_domain**](docs/DomainApi.md#create_domain) | Add a domain name to a service
*DomainApi* | [**delete_domain**](docs/DomainApi.md#delete_domain) | Remove a domain from a service
*DomainApi* | [**get_domain**](docs/DomainApi.md#get_domain) | Describe a domain
*DomainApi* | [**list_domains**](docs/DomainApi.md#list_domains) | List domains
*DomainApi* | [**update_domain**](docs/DomainApi.md#update_domain) | Update a domain
*DomainInspectorHistoricalApi* | [**get_domain_inspector_historical**](docs/DomainInspectorHistoricalApi.md#get_domain_inspector_historical) | Get historical domain data for a service
*DomainInspectorRealtimeApi* | [**get_domain_inspector_last120_seconds**](docs/DomainInspectorRealtimeApi.md#get_domain_inspector_last120_seconds) | Get real-time domain data for the last 120 seconds
*DomainInspectorRealtimeApi* | [**get_domain_inspector_last_max_entries**](docs/DomainInspectorRealtimeApi.md#get_domain_inspector_last_max_entries) | Get a limited number of real-time domain data entries
*DomainInspectorRealtimeApi* | [**get_domain_inspector_last_second**](docs/DomainInspectorRealtimeApi.md#get_domain_inspector_last_second) | Get real-time domain data from a specified time
*DomainOwnershipsApi* | [**list_domain_ownerships**](docs/DomainOwnershipsApi.md#list_domain_ownerships) | List domain-ownerships
*EventsApi* | [**get_event**](docs/EventsApi.md#get_event) | Get an event
*EventsApi* | [**list_events**](docs/EventsApi.md#list_events) | List events
*GzipApi* | [**create_gzip_config**](docs/GzipApi.md#create_gzip_config) | Create a gzip configuration
*GzipApi* | [**delete_gzip_config**](docs/GzipApi.md#delete_gzip_config) | Delete a gzip configuration
*GzipApi* | [**get_gzip_configs**](docs/GzipApi.md#get_gzip_configs) | Get a gzip configuration
*GzipApi* | [**list_gzip_configs**](docs/GzipApi.md#list_gzip_configs) | List gzip configurations
*GzipApi* | [**update_gzip_config**](docs/GzipApi.md#update_gzip_config) | Update a gzip configuration
*HeaderApi* | [**create_header_object**](docs/HeaderApi.md#create_header_object) | Create a Header object
*HeaderApi* | [**delete_header_object**](docs/HeaderApi.md#delete_header_object) | Delete a Header object
*HeaderApi* | [**get_header_object**](docs/HeaderApi.md#get_header_object) | Get a Header object
*HeaderApi* | [**list_header_objects**](docs/HeaderApi.md#list_header_objects) | List Header objects
*HeaderApi* | [**update_header_object**](docs/HeaderApi.md#update_header_object) | Update a Header object
*HealthcheckApi* | [**create_healthcheck**](docs/HealthcheckApi.md#create_healthcheck) | Create a health check
*HealthcheckApi* | [**delete_healthcheck**](docs/HealthcheckApi.md#delete_healthcheck) | Delete a health check
*HealthcheckApi* | [**get_healthcheck**](docs/HealthcheckApi.md#get_healthcheck) | Get a health check
*HealthcheckApi* | [**list_healthchecks**](docs/HealthcheckApi.md#list_healthchecks) | List health checks
*HealthcheckApi* | [**update_healthcheck**](docs/HealthcheckApi.md#update_healthcheck) | Update a health check
*HistoricalApi* | [**get_hist_stats**](docs/HistoricalApi.md#get_hist_stats) | Get historical stats
*HistoricalApi* | [**get_hist_stats_aggregated**](docs/HistoricalApi.md#get_hist_stats_aggregated) | Get aggregated historical stats
*HistoricalApi* | [**get_hist_stats_field**](docs/HistoricalApi.md#get_hist_stats_field) | Get historical stats for a single field
*HistoricalApi* | [**get_hist_stats_service**](docs/HistoricalApi.md#get_hist_stats_service) | Get historical stats for a single service
*HistoricalApi* | [**get_hist_stats_service_field**](docs/HistoricalApi.md#get_hist_stats_service_field) | Get historical stats for a single service/field combination
*HistoricalApi* | [**get_regions**](docs/HistoricalApi.md#get_regions) | Get region codes
*HistoricalApi* | [**get_usage**](docs/HistoricalApi.md#get_usage) | Get usage statistics
*HistoricalApi* | [**get_usage_month**](docs/HistoricalApi.md#get_usage_month) | Get month-to-date usage statistics
*HistoricalApi* | [**get_usage_service**](docs/HistoricalApi.md#get_usage_service) | Get usage statistics per service
*Http3Api* | [**create_http3**](docs/Http3Api.md#create_http3) | Enable support for HTTP/3
*Http3Api* | [**delete_http3**](docs/Http3Api.md#delete_http3) | Disable support for HTTP/3
*Http3Api* | [**get_http3**](docs/Http3Api.md#get_http3) | Get HTTP/3 status
*IamPermissionsApi* | [**list_permissions**](docs/IamPermissionsApi.md#list_permissions) | List permissions
*IamRolesApi* | [**add_role_permissions**](docs/IamRolesApi.md#add_role_permissions) | Add permissions to a role
*IamRolesApi* | [**create_a_role**](docs/IamRolesApi.md#create_a_role) | Create a role
*IamRolesApi* | [**delete_a_role**](docs/IamRolesApi.md#delete_a_role) | Delete a role
*IamRolesApi* | [**get_a_role**](docs/IamRolesApi.md#get_a_role) | Get a role
*IamRolesApi* | [**list_role_permissions**](docs/IamRolesApi.md#list_role_permissions) | List permissions in a role
*IamRolesApi* | [**list_roles**](docs/IamRolesApi.md#list_roles) | List roles
*IamRolesApi* | [**remove_role_permissions**](docs/IamRolesApi.md#remove_role_permissions) | Remove permissions from a role
*IamRolesApi* | [**update_a_role**](docs/IamRolesApi.md#update_a_role) | Update a role
*IamServiceGroupsApi* | [**add_service_group_services**](docs/IamServiceGroupsApi.md#add_service_group_services) | Add services in a service group
*IamServiceGroupsApi* | [**create_a_service_group**](docs/IamServiceGroupsApi.md#create_a_service_group) | Create a service group
*IamServiceGroupsApi* | [**delete_a_service_group**](docs/IamServiceGroupsApi.md#delete_a_service_group) | Delete a service group
*IamServiceGroupsApi* | [**get_a_service_group**](docs/IamServiceGroupsApi.md#get_a_service_group) | Get a service group
*IamServiceGroupsApi* | [**list_service_group_services**](docs/IamServiceGroupsApi.md#list_service_group_services) | List services to a service group
*IamServiceGroupsApi* | [**list_service_groups**](docs/IamServiceGroupsApi.md#list_service_groups) | List service groups
*IamServiceGroupsApi* | [**remove_service_group_services**](docs/IamServiceGroupsApi.md#remove_service_group_services) | Remove services from a service group
*IamServiceGroupsApi* | [**update_a_service_group**](docs/IamServiceGroupsApi.md#update_a_service_group) | Update a service group
*IamUserGroupsApi* | [**add_user_group_members**](docs/IamUserGroupsApi.md#add_user_group_members) | Add members to a user group
*IamUserGroupsApi* | [**add_user_group_roles**](docs/IamUserGroupsApi.md#add_user_group_roles) | Add roles to a user group
*IamUserGroupsApi* | [**add_user_group_service_groups**](docs/IamUserGroupsApi.md#add_user_group_service_groups) | Add service groups to a user group
*IamUserGroupsApi* | [**create_a_user_group**](docs/IamUserGroupsApi.md#create_a_user_group) | Create a user group
*IamUserGroupsApi* | [**delete_a_user_group**](docs/IamUserGroupsApi.md#delete_a_user_group) | Delete a user group
*IamUserGroupsApi* | [**get_a_user_group**](docs/IamUserGroupsApi.md#get_a_user_group) | Get a user group
*IamUserGroupsApi* | [**list_user_group_members**](docs/IamUserGroupsApi.md#list_user_group_members) | List members of a user group
*IamUserGroupsApi* | [**list_user_group_roles**](docs/IamUserGroupsApi.md#list_user_group_roles) | List roles in a user group
*IamUserGroupsApi* | [**list_user_group_service_groups**](docs/IamUserGroupsApi.md#list_user_group_service_groups) | List service groups in a user group
*IamUserGroupsApi* | [**list_user_groups**](docs/IamUserGroupsApi.md#list_user_groups) | List user groups
*IamUserGroupsApi* | [**remove_user_group_members**](docs/IamUserGroupsApi.md#remove_user_group_members) | Remove members of a user group
*IamUserGroupsApi* | [**remove_user_group_roles**](docs/IamUserGroupsApi.md#remove_user_group_roles) | Remove roles from a user group
*IamUserGroupsApi* | [**remove_user_group_service_groups**](docs/IamUserGroupsApi.md#remove_user_group_service_groups) | Remove service groups from a user group
*IamUserGroupsApi* | [**update_a_user_group**](docs/IamUserGroupsApi.md#update_a_user_group) | Update a user group
*ImageOptimizerDefaultSettingsApi* | [**get_default_settings**](docs/ImageOptimizerDefaultSettingsApi.md#get_default_settings) | Get current Image Optimizer Default Settings
*ImageOptimizerDefaultSettingsApi* | [**update_default_settings**](docs/ImageOptimizerDefaultSettingsApi.md#update_default_settings) | Update Image Optimizer Default Settings
*InsightsApi* | [**get_log_insights**](docs/InsightsApi.md#get_log_insights) | Retrieve log insights
*InvitationsApi* | [**create_invitation**](docs/InvitationsApi.md#create_invitation) | Create an invitation
*InvitationsApi* | [**delete_invitation**](docs/InvitationsApi.md#delete_invitation) | Delete an invitation
*InvitationsApi* | [**list_invitations**](docs/InvitationsApi.md#list_invitations) | List invitations
*KvStoreApi* | [**kv_store_create**](docs/KvStoreApi.md#kv_store_create) | Create a KV store.
*KvStoreApi* | [**kv_store_delete**](docs/KvStoreApi.md#kv_store_delete) | Delete a KV store.
*KvStoreApi* | [**kv_store_get**](docs/KvStoreApi.md#kv_store_get) | Describe a KV store.
*KvStoreApi* | [**kv_store_list**](docs/KvStoreApi.md#kv_store_list) | List all KV stores.
*KvStoreItemApi* | [**kv_store_delete_item**](docs/KvStoreItemApi.md#kv_store_delete_item) | Delete an item.
*KvStoreItemApi* | [**kv_store_get_item**](docs/KvStoreItemApi.md#kv_store_get_item) | Get an item.
*KvStoreItemApi* | [**kv_store_list_item_keys**](docs/KvStoreItemApi.md#kv_store_list_item_keys) | List item keys.
*KvStoreItemApi* | [**kv_store_upsert_item**](docs/KvStoreItemApi.md#kv_store_upsert_item) | Insert or update an item.
*LogExplorerApi* | [**get_log_records**](docs/LogExplorerApi.md#get_log_records) | Retrieve log records
*LoggingAzureblobApi* | [**create_log_azure**](docs/LoggingAzureblobApi.md#create_log_azure) | Create an Azure Blob Storage log endpoint
*LoggingAzureblobApi* | [**delete_log_azure**](docs/LoggingAzureblobApi.md#delete_log_azure) | Delete the Azure Blob Storage log endpoint
*LoggingAzureblobApi* | [**get_log_azure**](docs/LoggingAzureblobApi.md#get_log_azure) | Get an Azure Blob Storage log endpoint
*LoggingAzureblobApi* | [**list_log_azure**](docs/LoggingAzureblobApi.md#list_log_azure) | List Azure Blob Storage log endpoints
*LoggingAzureblobApi* | [**update_log_azure**](docs/LoggingAzureblobApi.md#update_log_azure) | Update an Azure Blob Storage log endpoint
*LoggingBigqueryApi* | [**create_log_bigquery**](docs/LoggingBigqueryApi.md#create_log_bigquery) | Create a BigQuery log endpoint
*LoggingBigqueryApi* | [**delete_log_bigquery**](docs/LoggingBigqueryApi.md#delete_log_bigquery) | Delete a BigQuery log endpoint
*LoggingBigqueryApi* | [**get_log_bigquery**](docs/LoggingBigqueryApi.md#get_log_bigquery) | Get a BigQuery log endpoint
*LoggingBigqueryApi* | [**list_log_bigquery**](docs/LoggingBigqueryApi.md#list_log_bigquery) | List BigQuery log endpoints
*LoggingBigqueryApi* | [**update_log_bigquery**](docs/LoggingBigqueryApi.md#update_log_bigquery) | Update a BigQuery log endpoint
*LoggingCloudfilesApi* | [**create_log_cloudfiles**](docs/LoggingCloudfilesApi.md#create_log_cloudfiles) | Create a Cloud Files log endpoint
*LoggingCloudfilesApi* | [**delete_log_cloudfiles**](docs/LoggingCloudfilesApi.md#delete_log_cloudfiles) | Delete the Cloud Files log endpoint
*LoggingCloudfilesApi* | [**get_log_cloudfiles**](docs/LoggingCloudfilesApi.md#get_log_cloudfiles) | Get a Cloud Files log endpoint
*LoggingCloudfilesApi* | [**list_log_cloudfiles**](docs/LoggingCloudfilesApi.md#list_log_cloudfiles) | List Cloud Files log endpoints
*LoggingCloudfilesApi* | [**update_log_cloudfiles**](docs/LoggingCloudfilesApi.md#update_log_cloudfiles) | Update the Cloud Files log endpoint
*LoggingDatadogApi* | [**create_log_datadog**](docs/LoggingDatadogApi.md#create_log_datadog) | Create a Datadog log endpoint
*LoggingDatadogApi* | [**delete_log_datadog**](docs/LoggingDatadogApi.md#delete_log_datadog) | Delete a Datadog log endpoint
*LoggingDatadogApi* | [**get_log_datadog**](docs/LoggingDatadogApi.md#get_log_datadog) | Get a Datadog log endpoint
*LoggingDatadogApi* | [**list_log_datadog**](docs/LoggingDatadogApi.md#list_log_datadog) | List Datadog log endpoints
*LoggingDatadogApi* | [**update_log_datadog**](docs/LoggingDatadogApi.md#update_log_datadog) | Update a Datadog log endpoint
*LoggingDigitaloceanApi* | [**create_log_digocean**](docs/LoggingDigitaloceanApi.md#create_log_digocean) | Create a DigitalOcean Spaces log endpoint
*LoggingDigitaloceanApi* | [**delete_log_digocean**](docs/LoggingDigitaloceanApi.md#delete_log_digocean) | Delete a DigitalOcean Spaces log endpoint
*LoggingDigitaloceanApi* | [**get_log_digocean**](docs/LoggingDigitaloceanApi.md#get_log_digocean) | Get a DigitalOcean Spaces log endpoint
*LoggingDigitaloceanApi* | [**list_log_digocean**](docs/LoggingDigitaloceanApi.md#list_log_digocean) | List DigitalOcean Spaces log endpoints
*LoggingDigitaloceanApi* | [**update_log_digocean**](docs/LoggingDigitaloceanApi.md#update_log_digocean) | Update a DigitalOcean Spaces log endpoint
*LoggingElasticsearchApi* | [**create_log_elasticsearch**](docs/LoggingElasticsearchApi.md#create_log_elasticsearch) | Create an Elasticsearch log endpoint
*LoggingElasticsearchApi* | [**delete_log_elasticsearch**](docs/LoggingElasticsearchApi.md#delete_log_elasticsearch) | Delete an Elasticsearch log endpoint
*LoggingElasticsearchApi* | [**get_log_elasticsearch**](docs/LoggingElasticsearchApi.md#get_log_elasticsearch) | Get an Elasticsearch log endpoint
*LoggingElasticsearchApi* | [**list_log_elasticsearch**](docs/LoggingElasticsearchApi.md#list_log_elasticsearch) | List Elasticsearch log endpoints
*LoggingElasticsearchApi* | [**update_log_elasticsearch**](docs/LoggingElasticsearchApi.md#update_log_elasticsearch) | Update an Elasticsearch log endpoint
*LoggingFtpApi* | [**create_log_ftp**](docs/LoggingFtpApi.md#create_log_ftp) | Create an FTP log endpoint
*LoggingFtpApi* | [**delete_log_ftp**](docs/LoggingFtpApi.md#delete_log_ftp) | Delete an FTP log endpoint
*LoggingFtpApi* | [**get_log_ftp**](docs/LoggingFtpApi.md#get_log_ftp) | Get an FTP log endpoint
*LoggingFtpApi* | [**list_log_ftp**](docs/LoggingFtpApi.md#list_log_ftp) | List FTP log endpoints
*LoggingFtpApi* | [**update_log_ftp**](docs/LoggingFtpApi.md#update_log_ftp) | Update an FTP log endpoint
*LoggingGcsApi* | [**create_log_gcs**](docs/LoggingGcsApi.md#create_log_gcs) | Create a GCS log endpoint
*LoggingGcsApi* | [**delete_log_gcs**](docs/LoggingGcsApi.md#delete_log_gcs) | Delete a GCS log endpoint
*LoggingGcsApi* | [**get_log_gcs**](docs/LoggingGcsApi.md#get_log_gcs) | Get a GCS log endpoint
*LoggingGcsApi* | [**list_log_gcs**](docs/LoggingGcsApi.md#list_log_gcs) | List GCS log endpoints
*LoggingGcsApi* | [**update_log_gcs**](docs/LoggingGcsApi.md#update_log_gcs) | Update a GCS log endpoint
*LoggingGrafanacloudlogsApi* | [**create_log_grafanacloudlogs**](docs/LoggingGrafanacloudlogsApi.md#create_log_grafanacloudlogs) | Create a Grafana Cloud Logs log endpoint
*LoggingGrafanacloudlogsApi* | [**delete_log_grafanacloudlogs**](docs/LoggingGrafanacloudlogsApi.md#delete_log_grafanacloudlogs) | Delete the Grafana Cloud Logs log endpoint
*LoggingGrafanacloudlogsApi* | [**get_log_grafanacloudlogs**](docs/LoggingGrafanacloudlogsApi.md#get_log_grafanacloudlogs) | Get a Grafana Cloud Logs log endpoint
*LoggingGrafanacloudlogsApi* | [**list_log_grafanacloudlogs**](docs/LoggingGrafanacloudlogsApi.md#list_log_grafanacloudlogs) | List Grafana Cloud Logs log endpoints
*LoggingGrafanacloudlogsApi* | [**update_log_grafanacloudlogs**](docs/LoggingGrafanacloudlogsApi.md#update_log_grafanacloudlogs) | Update a Grafana Cloud Logs log endpoint
*LoggingHerokuApi* | [**create_log_heroku**](docs/LoggingHerokuApi.md#create_log_heroku) | Create a Heroku log endpoint
*LoggingHerokuApi* | [**delete_log_heroku**](docs/LoggingHerokuApi.md#delete_log_heroku) | Delete the Heroku log endpoint
*LoggingHerokuApi* | [**get_log_heroku**](docs/LoggingHerokuApi.md#get_log_heroku) | Get a Heroku log endpoint
*LoggingHerokuApi* | [**list_log_heroku**](docs/LoggingHerokuApi.md#list_log_heroku) | List Heroku log endpoints
*LoggingHerokuApi* | [**update_log_heroku**](docs/LoggingHerokuApi.md#update_log_heroku) | Update the Heroku log endpoint
*LoggingHoneycombApi* | [**create_log_honeycomb**](docs/LoggingHoneycombApi.md#create_log_honeycomb) | Create a Honeycomb log endpoint
*LoggingHoneycombApi* | [**delete_log_honeycomb**](docs/LoggingHoneycombApi.md#delete_log_honeycomb) | Delete the Honeycomb log endpoint
*LoggingHoneycombApi* | [**get_log_honeycomb**](docs/LoggingHoneycombApi.md#get_log_honeycomb) | Get a Honeycomb log endpoint
*LoggingHoneycombApi* | [**list_log_honeycomb**](docs/LoggingHoneycombApi.md#list_log_honeycomb) | List Honeycomb log endpoints
*LoggingHoneycombApi* | [**update_log_honeycomb**](docs/LoggingHoneycombApi.md#update_log_honeycomb) | Update a Honeycomb log endpoint
*LoggingHttpsApi* | [**create_log_https**](docs/LoggingHttpsApi.md#create_log_https) | Create an HTTPS log endpoint
*LoggingHttpsApi* | [**delete_log_https**](docs/LoggingHttpsApi.md#delete_log_https) | Delete an HTTPS log endpoint
*LoggingHttpsApi* | [**get_log_https**](docs/LoggingHttpsApi.md#get_log_https) | Get an HTTPS log endpoint
*LoggingHttpsApi* | [**list_log_https**](docs/LoggingHttpsApi.md#list_log_https) | List HTTPS log endpoints
*LoggingHttpsApi* | [**update_log_https**](docs/LoggingHttpsApi.md#update_log_https) | Update an HTTPS log endpoint
*LoggingKafkaApi* | [**create_log_kafka**](docs/LoggingKafkaApi.md#create_log_kafka) | Create a Kafka log endpoint
*LoggingKafkaApi* | [**delete_log_kafka**](docs/LoggingKafkaApi.md#delete_log_kafka) | Delete the Kafka log endpoint
*LoggingKafkaApi* | [**get_log_kafka**](docs/LoggingKafkaApi.md#get_log_kafka) | Get a Kafka log endpoint
*LoggingKafkaApi* | [**list_log_kafka**](docs/LoggingKafkaApi.md#list_log_kafka) | List Kafka log endpoints
*LoggingKafkaApi* | [**update_log_kafka**](docs/LoggingKafkaApi.md#update_log_kafka) | Update the Kafka log endpoint
*LoggingKinesisApi* | [**create_log_kinesis**](docs/LoggingKinesisApi.md#create_log_kinesis) | Create  an Amazon Kinesis log endpoint
*LoggingKinesisApi* | [**delete_log_kinesis**](docs/LoggingKinesisApi.md#delete_log_kinesis) | Delete the Amazon Kinesis log endpoint
*LoggingKinesisApi* | [**get_log_kinesis**](docs/LoggingKinesisApi.md#get_log_kinesis) | Get an Amazon Kinesis log endpoint
*LoggingKinesisApi* | [**list_log_kinesis**](docs/LoggingKinesisApi.md#list_log_kinesis) | List Amazon Kinesis log endpoints
*LoggingKinesisApi* | [**update_log_kinesis**](docs/LoggingKinesisApi.md#update_log_kinesis) | Update the Amazon Kinesis log endpoint
*LoggingLogentriesApi* | [**create_log_logentries**](docs/LoggingLogentriesApi.md#create_log_logentries) | Create a Logentries log endpoint
*LoggingLogentriesApi* | [**delete_log_logentries**](docs/LoggingLogentriesApi.md#delete_log_logentries) | Delete a Logentries log endpoint
*LoggingLogentriesApi* | [**get_log_logentries**](docs/LoggingLogentriesApi.md#get_log_logentries) | Get a Logentries log endpoint
*LoggingLogentriesApi* | [**list_log_logentries**](docs/LoggingLogentriesApi.md#list_log_logentries) | List Logentries log endpoints
*LoggingLogentriesApi* | [**update_log_logentries**](docs/LoggingLogentriesApi.md#update_log_logentries) | Update a Logentries log endpoint
*LoggingLogglyApi* | [**create_log_loggly**](docs/LoggingLogglyApi.md#create_log_loggly) | Create a Loggly log endpoint
*LoggingLogglyApi* | [**delete_log_loggly**](docs/LoggingLogglyApi.md#delete_log_loggly) | Delete a Loggly log endpoint
*LoggingLogglyApi* | [**get_log_loggly**](docs/LoggingLogglyApi.md#get_log_loggly) | Get a Loggly log endpoint
*LoggingLogglyApi* | [**list_log_loggly**](docs/LoggingLogglyApi.md#list_log_loggly) | List Loggly log endpoints
*LoggingLogglyApi* | [**update_log_loggly**](docs/LoggingLogglyApi.md#update_log_loggly) | Update a Loggly log endpoint
*LoggingLogshuttleApi* | [**create_log_logshuttle**](docs/LoggingLogshuttleApi.md#create_log_logshuttle) | Create a Log Shuttle log endpoint
*LoggingLogshuttleApi* | [**delete_log_logshuttle**](docs/LoggingLogshuttleApi.md#delete_log_logshuttle) | Delete a Log Shuttle log endpoint
*LoggingLogshuttleApi* | [**get_log_logshuttle**](docs/LoggingLogshuttleApi.md#get_log_logshuttle) | Get a Log Shuttle log endpoint
*LoggingLogshuttleApi* | [**list_log_logshuttle**](docs/LoggingLogshuttleApi.md#list_log_logshuttle) | List Log Shuttle log endpoints
*LoggingLogshuttleApi* | [**update_log_logshuttle**](docs/LoggingLogshuttleApi.md#update_log_logshuttle) | Update a Log Shuttle log endpoint
*LoggingNewrelicApi* | [**create_log_newrelic**](docs/LoggingNewrelicApi.md#create_log_newrelic) | Create a New Relic log endpoint
*LoggingNewrelicApi* | [**delete_log_newrelic**](docs/LoggingNewrelicApi.md#delete_log_newrelic) | Delete a New Relic log endpoint
*LoggingNewrelicApi* | [**get_log_newrelic**](docs/LoggingNewrelicApi.md#get_log_newrelic) | Get a New Relic log endpoint
*LoggingNewrelicApi* | [**list_log_newrelic**](docs/LoggingNewrelicApi.md#list_log_newrelic) | List New Relic log endpoints
*LoggingNewrelicApi* | [**update_log_newrelic**](docs/LoggingNewrelicApi.md#update_log_newrelic) | Update a New Relic log endpoint
*LoggingNewrelicotlpApi* | [**create_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#create_log_newrelicotlp) | Create a New Relic OTLP endpoint
*LoggingNewrelicotlpApi* | [**delete_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#delete_log_newrelicotlp) | Delete a New Relic OTLP endpoint
*LoggingNewrelicotlpApi* | [**get_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#get_log_newrelicotlp) | Get a New Relic OTLP endpoint
*LoggingNewrelicotlpApi* | [**list_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#list_log_newrelicotlp) | List New Relic OTLP endpoints
*LoggingNewrelicotlpApi* | [**update_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#update_log_newrelicotlp) | Update a New Relic log endpoint
*LoggingOpenstackApi* | [**create_log_openstack**](docs/LoggingOpenstackApi.md#create_log_openstack) | Create an OpenStack log endpoint
*LoggingOpenstackApi* | [**delete_log_openstack**](docs/LoggingOpenstackApi.md#delete_log_openstack) | Delete an OpenStack log endpoint
*LoggingOpenstackApi* | [**get_log_openstack**](docs/LoggingOpenstackApi.md#get_log_openstack) | Get an OpenStack log endpoint
*LoggingOpenstackApi* | [**list_log_openstack**](docs/LoggingOpenstackApi.md#list_log_openstack) | List OpenStack log endpoints
*LoggingOpenstackApi* | [**update_log_openstack**](docs/LoggingOpenstackApi.md#update_log_openstack) | Update an OpenStack log endpoint
*LoggingPapertrailApi* | [**create_log_papertrail**](docs/LoggingPapertrailApi.md#create_log_papertrail) | Create a Papertrail log endpoint
*LoggingPapertrailApi* | [**delete_log_papertrail**](docs/LoggingPapertrailApi.md#delete_log_papertrail) | Delete a Papertrail log endpoint
*LoggingPapertrailApi* | [**get_log_papertrail**](docs/LoggingPapertrailApi.md#get_log_papertrail) | Get a Papertrail log endpoint
*LoggingPapertrailApi* | [**list_log_papertrail**](docs/LoggingPapertrailApi.md#list_log_papertrail) | List Papertrail log endpoints
*LoggingPapertrailApi* | [**update_log_papertrail**](docs/LoggingPapertrailApi.md#update_log_papertrail) | Update a Papertrail log endpoint
*LoggingPubsubApi* | [**create_log_gcp_pubsub**](docs/LoggingPubsubApi.md#create_log_gcp_pubsub) | Create a GCP Cloud Pub/Sub log endpoint
*LoggingPubsubApi* | [**delete_log_gcp_pubsub**](docs/LoggingPubsubApi.md#delete_log_gcp_pubsub) | Delete a GCP Cloud Pub/Sub log endpoint
*LoggingPubsubApi* | [**get_log_gcp_pubsub**](docs/LoggingPubsubApi.md#get_log_gcp_pubsub) | Get a GCP Cloud Pub/Sub log endpoint
*LoggingPubsubApi* | [**list_log_gcp_pubsub**](docs/LoggingPubsubApi.md#list_log_gcp_pubsub) | List GCP Cloud Pub/Sub log endpoints
*LoggingPubsubApi* | [**update_log_gcp_pubsub**](docs/LoggingPubsubApi.md#update_log_gcp_pubsub) | Update a GCP Cloud Pub/Sub log endpoint
*LoggingS3Api* | [**create_log_aws_s3**](docs/LoggingS3Api.md#create_log_aws_s3) | Create an AWS S3 log endpoint
*LoggingS3Api* | [**delete_log_aws_s3**](docs/LoggingS3Api.md#delete_log_aws_s3) | Delete an AWS S3 log endpoint
*LoggingS3Api* | [**get_log_aws_s3**](docs/LoggingS3Api.md#get_log_aws_s3) | Get an AWS S3 log endpoint
*LoggingS3Api* | [**list_log_aws_s3**](docs/LoggingS3Api.md#list_log_aws_s3) | List AWS S3 log endpoints
*LoggingS3Api* | [**update_log_aws_s3**](docs/LoggingS3Api.md#update_log_aws_s3) | Update an AWS S3 log endpoint
*LoggingScalyrApi* | [**create_log_scalyr**](docs/LoggingScalyrApi.md#create_log_scalyr) | Create a Scalyr log endpoint
*LoggingScalyrApi* | [**delete_log_scalyr**](docs/LoggingScalyrApi.md#delete_log_scalyr) | Delete the Scalyr log endpoint
*LoggingScalyrApi* | [**get_log_scalyr**](docs/LoggingScalyrApi.md#get_log_scalyr) | Get a Scalyr log endpoint
*LoggingScalyrApi* | [**list_log_scalyr**](docs/LoggingScalyrApi.md#list_log_scalyr) | List Scalyr log endpoints
*LoggingScalyrApi* | [**update_log_scalyr**](docs/LoggingScalyrApi.md#update_log_scalyr) | Update the Scalyr log endpoint
*LoggingSftpApi* | [**create_log_sftp**](docs/LoggingSftpApi.md#create_log_sftp) | Create an SFTP log endpoint
*LoggingSftpApi* | [**delete_log_sftp**](docs/LoggingSftpApi.md#delete_log_sftp) | Delete an SFTP log endpoint
*LoggingSftpApi* | [**get_log_sftp**](docs/LoggingSftpApi.md#get_log_sftp) | Get an SFTP log endpoint
*LoggingSftpApi* | [**list_log_sftp**](docs/LoggingSftpApi.md#list_log_sftp) | List SFTP log endpoints
*LoggingSftpApi* | [**update_log_sftp**](docs/LoggingSftpApi.md#update_log_sftp) | Update an SFTP log endpoint
*LoggingSplunkApi* | [**create_log_splunk**](docs/LoggingSplunkApi.md#create_log_splunk) | Create a Splunk log endpoint
*LoggingSplunkApi* | [**delete_log_splunk**](docs/LoggingSplunkApi.md#delete_log_splunk) | Delete a Splunk log endpoint
*LoggingSplunkApi* | [**get_log_splunk**](docs/LoggingSplunkApi.md#get_log_splunk) | Get a Splunk log endpoint
*LoggingSplunkApi* | [**list_log_splunk**](docs/LoggingSplunkApi.md#list_log_splunk) | List Splunk log endpoints
*LoggingSplunkApi* | [**update_log_splunk**](docs/LoggingSplunkApi.md#update_log_splunk) | Update a Splunk log endpoint
*LoggingSumologicApi* | [**create_log_sumologic**](docs/LoggingSumologicApi.md#create_log_sumologic) | Create a Sumologic log endpoint
*LoggingSumologicApi* | [**delete_log_sumologic**](docs/LoggingSumologicApi.md#delete_log_sumologic) | Delete a Sumologic log endpoint
*LoggingSumologicApi* | [**get_log_sumologic**](docs/LoggingSumologicApi.md#get_log_sumologic) | Get a Sumologic log endpoint
*LoggingSumologicApi* | [**list_log_sumologic**](docs/LoggingSumologicApi.md#list_log_sumologic) | List Sumologic log endpoints
*LoggingSumologicApi* | [**update_log_sumologic**](docs/LoggingSumologicApi.md#update_log_sumologic) | Update a Sumologic log endpoint
*LoggingSyslogApi* | [**create_log_syslog**](docs/LoggingSyslogApi.md#create_log_syslog) | Create a syslog log endpoint
*LoggingSyslogApi* | [**delete_log_syslog**](docs/LoggingSyslogApi.md#delete_log_syslog) | Delete a syslog log endpoint
*LoggingSyslogApi* | [**get_log_syslog**](docs/LoggingSyslogApi.md#get_log_syslog) | Get a syslog log endpoint
*LoggingSyslogApi* | [**list_log_syslog**](docs/LoggingSyslogApi.md#list_log_syslog) | List Syslog log endpoints
*LoggingSyslogApi* | [**update_log_syslog**](docs/LoggingSyslogApi.md#update_log_syslog) | Update a syslog log endpoint
*MutualAuthenticationApi* | [**create_mutual_tls_authentication**](docs/MutualAuthenticationApi.md#create_mutual_tls_authentication) | Create a Mutual Authentication
*MutualAuthenticationApi* | [**delete_mutual_tls**](docs/MutualAuthenticationApi.md#delete_mutual_tls) | Delete a Mutual TLS
*MutualAuthenticationApi* | [**get_mutual_authentication**](docs/MutualAuthenticationApi.md#get_mutual_authentication) | Get a Mutual Authentication
*MutualAuthenticationApi* | [**list_mutual_authentications**](docs/MutualAuthenticationApi.md#list_mutual_authentications) | List Mutual Authentications
*MutualAuthenticationApi* | [**patch_mutual_authentication**](docs/MutualAuthenticationApi.md#patch_mutual_authentication) | Update a Mutual Authentication
*ObjectStorageAccessKeysApi* | [**create_access_key**](docs/ObjectStorageAccessKeysApi.md#create_access_key) | Create an access key
*ObjectStorageAccessKeysApi* | [**delete_access_key**](docs/ObjectStorageAccessKeysApi.md#delete_access_key) | Delete an access key
*ObjectStorageAccessKeysApi* | [**get_access_key**](docs/ObjectStorageAccessKeysApi.md#get_access_key) | Get an access key
*ObjectStorageAccessKeysApi* | [**list_access_keys**](docs/ObjectStorageAccessKeysApi.md#list_access_keys) | List access keys
*ObservabilityCustomDashboardsApi* | [**create_dashboard**](docs/ObservabilityCustomDashboardsApi.md#create_dashboard) | Create a new dashboard
*ObservabilityCustomDashboardsApi* | [**delete_dashboard**](docs/ObservabilityCustomDashboardsApi.md#delete_dashboard) | Delete an existing dashboard
*ObservabilityCustomDashboardsApi* | [**get_dashboard**](docs/ObservabilityCustomDashboardsApi.md#get_dashboard) | Retrieve a dashboard by ID
*ObservabilityCustomDashboardsApi* | [**list_dashboards**](docs/ObservabilityCustomDashboardsApi.md#list_dashboards) | List all custom dashboards
*ObservabilityCustomDashboardsApi* | [**update_dashboard**](docs/ObservabilityCustomDashboardsApi.md#update_dashboard) | Update an existing dashboard
*OriginInspectorHistoricalApi* | [**get_origin_inspector_historical**](docs/OriginInspectorHistoricalApi.md#get_origin_inspector_historical) | Get historical origin data for a service
*OriginInspectorRealtimeApi* | [**get_origin_inspector_last120_seconds**](docs/OriginInspectorRealtimeApi.md#get_origin_inspector_last120_seconds) | Get real-time origin data for the last 120 seconds
*OriginInspectorRealtimeApi* | [**get_origin_inspector_last_max_entries**](docs/OriginInspectorRealtimeApi.md#get_origin_inspector_last_max_entries) | Get a limited number of real-time origin data entries
*OriginInspectorRealtimeApi* | [**get_origin_inspector_last_second**](docs/OriginInspectorRealtimeApi.md#get_origin_inspector_last_second) | Get real-time origin data from specific time.
*PackageApi* | [**get_package**](docs/PackageApi.md#get_package) | Get details of the service&#39;s Compute package.
*PackageApi* | [**put_package**](docs/PackageApi.md#put_package) | Upload a Compute package.
*PoolApi* | [**create_server_pool**](docs/PoolApi.md#create_server_pool) | Create a server pool
*PoolApi* | [**delete_server_pool**](docs/PoolApi.md#delete_server_pool) | Delete a server pool
*PoolApi* | [**get_server_pool**](docs/PoolApi.md#get_server_pool) | Get a server pool
*PoolApi* | [**list_server_pools**](docs/PoolApi.md#list_server_pools) | List server pools
*PoolApi* | [**update_server_pool**](docs/PoolApi.md#update_server_pool) | Update a server pool
*PopApi* | [**list_pops**](docs/PopApi.md#list_pops) | List Fastly POPs
*ProductAiAcceleratorApi* | [**disable_product_ai_accelerator**](docs/ProductAiAcceleratorApi.md#disable_product_ai_accelerator) | Disable product
*ProductAiAcceleratorApi* | [**enable_ai_accelerator**](docs/ProductAiAcceleratorApi.md#enable_ai_accelerator) | Enable product
*ProductAiAcceleratorApi* | [**get_ai_accelerator**](docs/ProductAiAcceleratorApi.md#get_ai_accelerator) | Get product enablement status
*ProductBotManagementApi* | [**disable_product_bot_management**](docs/ProductBotManagementApi.md#disable_product_bot_management) | Disable product
*ProductBotManagementApi* | [**enable_product_bot_management**](docs/ProductBotManagementApi.md#enable_product_bot_management) | Enable product
*ProductBotManagementApi* | [**get_product_bot_management**](docs/ProductBotManagementApi.md#get_product_bot_management) | Get product enablement status
*ProductBrotliCompressionApi* | [**disable_product_brotli_compression**](docs/ProductBrotliCompressionApi.md#disable_product_brotli_compression) | Disable product
*ProductBrotliCompressionApi* | [**enable_product_brotli_compression**](docs/ProductBrotliCompressionApi.md#enable_product_brotli_compression) | Enable product
*ProductBrotliCompressionApi* | [**get_product_brotli_compression**](docs/ProductBrotliCompressionApi.md#get_product_brotli_compression) | Get product enablement status
*ProductDdosProtectionApi* | [**disable_product_ddos_protection**](docs/ProductDdosProtectionApi.md#disable_product_ddos_protection) | Disable product
*ProductDdosProtectionApi* | [**enable_product_ddos_protection**](docs/ProductDdosProtectionApi.md#enable_product_ddos_protection) | Enable product
*ProductDdosProtectionApi* | [**get_product_ddos_protection**](docs/ProductDdosProtectionApi.md#get_product_ddos_protection) | Get product enablement status
*ProductDdosProtectionApi* | [**get_product_ddos_protection_configuration**](docs/ProductDdosProtectionApi.md#get_product_ddos_protection_configuration) | Get configuration
*ProductDdosProtectionApi* | [**set_product_ddos_protection_configuration**](docs/ProductDdosProtectionApi.md#set_product_ddos_protection_configuration) | Update configuration
*ProductDomainInspectorApi* | [**disable_product_domain_inspector**](docs/ProductDomainInspectorApi.md#disable_product_domain_inspector) | Disable product
*ProductDomainInspectorApi* | [**enable_product_domain_inspector**](docs/ProductDomainInspectorApi.md#enable_product_domain_inspector) | Enable product
*ProductDomainInspectorApi* | [**get_product_domain_inspector**](docs/ProductDomainInspectorApi.md#get_product_domain_inspector) | Get product enablement status
*ProductFanoutApi* | [**disable_product_fanout**](docs/ProductFanoutApi.md#disable_product_fanout) | Disable product
*ProductFanoutApi* | [**enable_product_fanout**](docs/ProductFanoutApi.md#enable_product_fanout) | Enable product
*ProductFanoutApi* | [**get_product_fanout**](docs/ProductFanoutApi.md#get_product_fanout) | Get product enablement status
*ProductImageOptimizerApi* | [**disable_product_image_optimizer**](docs/ProductImageOptimizerApi.md#disable_product_image_optimizer) | Disable product
*ProductImageOptimizerApi* | [**enable_product_image_optimizer**](docs/ProductImageOptimizerApi.md#enable_product_image_optimizer) | Enable product
*ProductImageOptimizerApi* | [**get_product_image_optimizer**](docs/ProductImageOptimizerApi.md#get_product_image_optimizer) | Get product enablement status
*ProductLogExplorerInsightsApi* | [**disable_product_log_explorer_insights**](docs/ProductLogExplorerInsightsApi.md#disable_product_log_explorer_insights) | Disable product
*ProductLogExplorerInsightsApi* | [**enable_product_log_explorer_insights**](docs/ProductLogExplorerInsightsApi.md#enable_product_log_explorer_insights) | Enable product
*ProductLogExplorerInsightsApi* | [**get_product_log_explorer_insights**](docs/ProductLogExplorerInsightsApi.md#get_product_log_explorer_insights) | Get product enablement status
*ProductNgwafApi* | [**disable_product_ngwaf**](docs/ProductNgwafApi.md#disable_product_ngwaf) | Disable product
*ProductNgwafApi* | [**enable_product_ngwaf**](docs/ProductNgwafApi.md#enable_product_ngwaf) | Enable product
*ProductNgwafApi* | [**get_product_ngwaf**](docs/ProductNgwafApi.md#get_product_ngwaf) | Get product enablement status
*ProductNgwafApi* | [**get_product_ngwaf_configuration**](docs/ProductNgwafApi.md#get_product_ngwaf_configuration) | Get configuration
*ProductNgwafApi* | [**set_product_ngwaf_configuration**](docs/ProductNgwafApi.md#set_product_ngwaf_configuration) | Update configuration
*ProductObjectStorageApi* | [**disable_product_object_storage**](docs/ProductObjectStorageApi.md#disable_product_object_storage) | Disable product
*ProductObjectStorageApi* | [**enable_object_storage**](docs/ProductObjectStorageApi.md#enable_object_storage) | Enable product
*ProductObjectStorageApi* | [**get_object_storage**](docs/ProductObjectStorageApi.md#get_object_storage) | Get product enablement status
*ProductOriginInspectorApi* | [**disable_product_origin_inspector**](docs/ProductOriginInspectorApi.md#disable_product_origin_inspector) | Disable product
*ProductOriginInspectorApi* | [**enable_product_origin_inspector**](docs/ProductOriginInspectorApi.md#enable_product_origin_inspector) | Enable product
*ProductOriginInspectorApi* | [**get_product_origin_inspector**](docs/ProductOriginInspectorApi.md#get_product_origin_inspector) | Get product enablement status
*ProductWebsocketsApi* | [**disable_product_websockets**](docs/ProductWebsocketsApi.md#disable_product_websockets) | Disable product
*ProductWebsocketsApi* | [**enable_product_websockets**](docs/ProductWebsocketsApi.md#enable_product_websockets) | Enable product
*ProductWebsocketsApi* | [**get_product_websockets**](docs/ProductWebsocketsApi.md#get_product_websockets) | Get product enablement status
*PublicIpListApi* | [**list_fastly_ips**](docs/PublicIpListApi.md#list_fastly_ips) | List Fastly&#39;s public IPs
*PublishApi* | [**publish**](docs/PublishApi.md#publish) | Send messages to Fanout subscribers
*PurgeApi* | [**bulk_purge_tag**](docs/PurgeApi.md#bulk_purge_tag) | Purge multiple surrogate key tags
*PurgeApi* | [**purge_all**](docs/PurgeApi.md#purge_all) | Purge everything from a service
*PurgeApi* | [**purge_single_url**](docs/PurgeApi.md#purge_single_url) | Purge a URL
*PurgeApi* | [**purge_tag**](docs/PurgeApi.md#purge_tag) | Purge by surrogate key tag
*RateLimiterApi* | [**create_rate_limiter**](docs/RateLimiterApi.md#create_rate_limiter) | Create a rate limiter
*RateLimiterApi* | [**delete_rate_limiter**](docs/RateLimiterApi.md#delete_rate_limiter) | Delete a rate limiter
*RateLimiterApi* | [**get_rate_limiter**](docs/RateLimiterApi.md#get_rate_limiter) | Get a rate limiter
*RateLimiterApi* | [**list_rate_limiters**](docs/RateLimiterApi.md#list_rate_limiters) | List rate limiters
*RateLimiterApi* | [**update_rate_limiter**](docs/RateLimiterApi.md#update_rate_limiter) | Update a rate limiter
*RealtimeApi* | [**get_stats_last120_seconds**](docs/RealtimeApi.md#get_stats_last120_seconds) | Get real-time data for the last 120 seconds
*RealtimeApi* | [**get_stats_last120_seconds_limit_entries**](docs/RealtimeApi.md#get_stats_last120_seconds_limit_entries) | Get a limited number of real-time data entries
*RealtimeApi* | [**get_stats_last_second**](docs/RealtimeApi.md#get_stats_last_second) | Get real-time data from specified time
*RequestSettingsApi* | [**create_request_settings**](docs/RequestSettingsApi.md#create_request_settings) | Create a Request Settings object
*RequestSettingsApi* | [**delete_request_settings**](docs/RequestSettingsApi.md#delete_request_settings) | Delete a Request Settings object
*RequestSettingsApi* | [**get_request_settings**](docs/RequestSettingsApi.md#get_request_settings) | Get a Request Settings object
*RequestSettingsApi* | [**list_request_settings**](docs/RequestSettingsApi.md#list_request_settings) | List Request Settings objects
*RequestSettingsApi* | [**update_request_settings**](docs/RequestSettingsApi.md#update_request_settings) | Update a Request Settings object
*ResourceApi* | [**create_resource**](docs/ResourceApi.md#create_resource) | Create a resource link
*ResourceApi* | [**delete_resource**](docs/ResourceApi.md#delete_resource) | Delete a resource link
*ResourceApi* | [**get_resource**](docs/ResourceApi.md#get_resource) | Display a resource link
*ResourceApi* | [**list_resources**](docs/ResourceApi.md#list_resources) | List resource links
*ResourceApi* | [**update_resource**](docs/ResourceApi.md#update_resource) | Update a resource link
*ResponseObjectApi* | [**create_response_object**](docs/ResponseObjectApi.md#create_response_object) | Create a Response object
*ResponseObjectApi* | [**delete_response_object**](docs/ResponseObjectApi.md#delete_response_object) | Delete a Response Object
*ResponseObjectApi* | [**get_response_object**](docs/ResponseObjectApi.md#get_response_object) | Get a Response object
*ResponseObjectApi* | [**list_response_objects**](docs/ResponseObjectApi.md#list_response_objects) | List Response objects
*ResponseObjectApi* | [**update_response_object**](docs/ResponseObjectApi.md#update_response_object) | Update a Response object
*SecretStoreApi* | [**client_key**](docs/SecretStoreApi.md#client_key) | Create new client key
*SecretStoreApi* | [**create_secret_store**](docs/SecretStoreApi.md#create_secret_store) | Create new secret store
*SecretStoreApi* | [**delete_secret_store**](docs/SecretStoreApi.md#delete_secret_store) | Delete secret store
*SecretStoreApi* | [**get_secret_store**](docs/SecretStoreApi.md#get_secret_store) | Get secret store by ID
*SecretStoreApi* | [**get_secret_stores**](docs/SecretStoreApi.md#get_secret_stores) | Get all secret stores
*SecretStoreApi* | [**signing_key**](docs/SecretStoreApi.md#signing_key) | Get public key
*SecretStoreItemApi* | [**create_secret**](docs/SecretStoreItemApi.md#create_secret) | Create a new secret in a store.
*SecretStoreItemApi* | [**delete_secret**](docs/SecretStoreItemApi.md#delete_secret) | Delete a secret from a store.
*SecretStoreItemApi* | [**get_secret**](docs/SecretStoreItemApi.md#get_secret) | Get secret metadata.
*SecretStoreItemApi* | [**get_secrets**](docs/SecretStoreItemApi.md#get_secrets) | List secrets within a store.
*SecretStoreItemApi* | [**must_recreate_secret**](docs/SecretStoreItemApi.md#must_recreate_secret) | Recreate a secret in a store.
*SecretStoreItemApi* | [**recreate_secret**](docs/SecretStoreItemApi.md#recreate_secret) | Create or recreate a secret in a store.
*ServerApi* | [**create_pool_server**](docs/ServerApi.md#create_pool_server) | Add a server to a pool
*ServerApi* | [**delete_pool_server**](docs/ServerApi.md#delete_pool_server) | Delete a server from a pool
*ServerApi* | [**get_pool_server**](docs/ServerApi.md#get_pool_server) | Get a pool server
*ServerApi* | [**list_pool_servers**](docs/ServerApi.md#list_pool_servers) | List servers in a pool
*ServerApi* | [**update_pool_server**](docs/ServerApi.md#update_pool_server) | Update a server
*ServiceApi* | [**create_service**](docs/ServiceApi.md#create_service) | Create a service
*ServiceApi* | [**delete_service**](docs/ServiceApi.md#delete_service) | Delete a service
*ServiceApi* | [**get_service**](docs/ServiceApi.md#get_service) | Get a service
*ServiceApi* | [**get_service_detail**](docs/ServiceApi.md#get_service_detail) | Get service details
*ServiceApi* | [**list_service_domains**](docs/ServiceApi.md#list_service_domains) | List the domains within a service
*ServiceApi* | [**list_services**](docs/ServiceApi.md#list_services) | List services
*ServiceApi* | [**search_service**](docs/ServiceApi.md#search_service) | Search for a service by name
*ServiceApi* | [**update_service**](docs/ServiceApi.md#update_service) | Update a service
*ServiceAuthorizationsApi* | [**create_service_authorization**](docs/ServiceAuthorizationsApi.md#create_service_authorization) | Create service authorization
*ServiceAuthorizationsApi* | [**delete_service_authorization**](docs/ServiceAuthorizationsApi.md#delete_service_authorization) | Delete service authorization
*ServiceAuthorizationsApi* | [**delete_service_authorization2**](docs/ServiceAuthorizationsApi.md#delete_service_authorization2) | Delete service authorizations
*ServiceAuthorizationsApi* | [**list_service_authorization**](docs/ServiceAuthorizationsApi.md#list_service_authorization) | List service authorizations
*ServiceAuthorizationsApi* | [**show_service_authorization**](docs/ServiceAuthorizationsApi.md#show_service_authorization) | Show service authorization
*ServiceAuthorizationsApi* | [**update_service_authorization**](docs/ServiceAuthorizationsApi.md#update_service_authorization) | Update service authorization
*ServiceAuthorizationsApi* | [**update_service_authorization2**](docs/ServiceAuthorizationsApi.md#update_service_authorization2) | Update service authorizations
*SettingsApi* | [**get_service_settings**](docs/SettingsApi.md#get_service_settings) | Get service settings
*SettingsApi* | [**update_service_settings**](docs/SettingsApi.md#update_service_settings) | Update service settings
*SnippetApi* | [**create_snippet**](docs/SnippetApi.md#create_snippet) | Create a snippet
*SnippetApi* | [**delete_snippet**](docs/SnippetApi.md#delete_snippet) | Delete a snippet
*SnippetApi* | [**get_snippet**](docs/SnippetApi.md#get_snippet) | Get a versioned snippet
*SnippetApi* | [**get_snippet_dynamic**](docs/SnippetApi.md#get_snippet_dynamic) | Get a dynamic snippet
*SnippetApi* | [**list_snippets**](docs/SnippetApi.md#list_snippets) | List snippets
*SnippetApi* | [**update_snippet**](docs/SnippetApi.md#update_snippet) | Update a versioned snippet
*SnippetApi* | [**update_snippet_dynamic**](docs/SnippetApi.md#update_snippet_dynamic) | Update a dynamic snippet
*StarApi* | [**create_service_star**](docs/StarApi.md#create_service_star) | Create a star
*StarApi* | [**delete_service_star**](docs/StarApi.md#delete_service_star) | Delete a star
*StarApi* | [**get_service_star**](docs/StarApi.md#get_service_star) | Get a star
*StarApi* | [**list_service_stars**](docs/StarApi.md#list_service_stars) | List stars
*StatsApi* | [**get_service_stats**](docs/StatsApi.md#get_service_stats) | Get stats for a service
*SudoApi* | [**request_sudo_access**](docs/SudoApi.md#request_sudo_access) | Request Sudo access
*TlsActivationsApi* | [**create_tls_activation**](docs/TlsActivationsApi.md#create_tls_activation) | Enable TLS for a domain using a custom certificate
*TlsActivationsApi* | [**delete_tls_activation**](docs/TlsActivationsApi.md#delete_tls_activation) | Disable TLS on a domain
*TlsActivationsApi* | [**get_tls_activation**](docs/TlsActivationsApi.md#get_tls_activation) | Get a TLS activation
*TlsActivationsApi* | [**list_tls_activations**](docs/TlsActivationsApi.md#list_tls_activations) | List TLS activations
*TlsActivationsApi* | [**update_tls_activation**](docs/TlsActivationsApi.md#update_tls_activation) | Update a certificate
*TlsBulkCertificatesApi* | [**delete_bulk_tls_cert**](docs/TlsBulkCertificatesApi.md#delete_bulk_tls_cert) | Delete a certificate
*TlsBulkCertificatesApi* | [**get_tls_bulk_cert**](docs/TlsBulkCertificatesApi.md#get_tls_bulk_cert) | Get a certificate
*TlsBulkCertificatesApi* | [**list_tls_bulk_certs**](docs/TlsBulkCertificatesApi.md#list_tls_bulk_certs) | List certificates
*TlsBulkCertificatesApi* | [**update_bulk_tls_cert**](docs/TlsBulkCertificatesApi.md#update_bulk_tls_cert) | Update a certificate
*TlsBulkCertificatesApi* | [**upload_tls_bulk_cert**](docs/TlsBulkCertificatesApi.md#upload_tls_bulk_cert) | Upload a certificate
*TlsCertificatesApi* | [**create_tls_cert**](docs/TlsCertificatesApi.md#create_tls_cert) | Create a TLS certificate
*TlsCertificatesApi* | [**delete_tls_cert**](docs/TlsCertificatesApi.md#delete_tls_cert) | Delete a TLS certificate
*TlsCertificatesApi* | [**get_tls_cert**](docs/TlsCertificatesApi.md#get_tls_cert) | Get a TLS certificate
*TlsCertificatesApi* | [**get_tls_cert_blob**](docs/TlsCertificatesApi.md#get_tls_cert_blob) | Get a TLS certificate blob (Limited Availability)
*TlsCertificatesApi* | [**list_tls_certs**](docs/TlsCertificatesApi.md#list_tls_certs) | List TLS certificates
*TlsCertificatesApi* | [**update_tls_cert**](docs/TlsCertificatesApi.md#update_tls_cert) | Update a TLS certificate
*TlsConfigurationsApi* | [**get_tls_config**](docs/TlsConfigurationsApi.md#get_tls_config) | Get a TLS configuration
*TlsConfigurationsApi* | [**list_tls_configs**](docs/TlsConfigurationsApi.md#list_tls_configs) | List TLS configurations
*TlsConfigurationsApi* | [**update_tls_config**](docs/TlsConfigurationsApi.md#update_tls_config) | Update a TLS configuration
*TlsCsrsApi* | [**create_csr**](docs/TlsCsrsApi.md#create_csr) | Create CSR
*TlsDomainsApi* | [**list_tls_domains**](docs/TlsDomainsApi.md#list_tls_domains) | List TLS domains
*TlsPrivateKeysApi* | [**create_tls_key**](docs/TlsPrivateKeysApi.md#create_tls_key) | Create a TLS private key
*TlsPrivateKeysApi* | [**delete_tls_key**](docs/TlsPrivateKeysApi.md#delete_tls_key) | Delete a TLS private key
*TlsPrivateKeysApi* | [**get_tls_key**](docs/TlsPrivateKeysApi.md#get_tls_key) | Get a TLS private key
*TlsPrivateKeysApi* | [**list_tls_keys**](docs/TlsPrivateKeysApi.md#list_tls_keys) | List TLS private keys
*TlsSubscriptionsApi* | [**create_globalsign_email_challenge**](docs/TlsSubscriptionsApi.md#create_globalsign_email_challenge) | Creates a GlobalSign email challenge.
*TlsSubscriptionsApi* | [**create_tls_sub**](docs/TlsSubscriptionsApi.md#create_tls_sub) | Create a TLS subscription
*TlsSubscriptionsApi* | [**delete_globalsign_email_challenge**](docs/TlsSubscriptionsApi.md#delete_globalsign_email_challenge) | Delete a GlobalSign email challenge
*TlsSubscriptionsApi* | [**delete_tls_sub**](docs/TlsSubscriptionsApi.md#delete_tls_sub) | Delete a TLS subscription
*TlsSubscriptionsApi* | [**get_tls_sub**](docs/TlsSubscriptionsApi.md#get_tls_sub) | Get a TLS subscription
*TlsSubscriptionsApi* | [**list_tls_subs**](docs/TlsSubscriptionsApi.md#list_tls_subs) | List TLS subscriptions
*TlsSubscriptionsApi* | [**patch_tls_sub**](docs/TlsSubscriptionsApi.md#patch_tls_sub) | Update a TLS subscription
*TokensApi* | [**bulk_revoke_tokens**](docs/TokensApi.md#bulk_revoke_tokens) | Revoke multiple tokens
*TokensApi* | [**create_token**](docs/TokensApi.md#create_token) | Create a token
*TokensApi* | [**get_token**](docs/TokensApi.md#get_token) | Get a token
*TokensApi* | [**get_token_current**](docs/TokensApi.md#get_token_current) | Get the current token
*TokensApi* | [**list_tokens_customer**](docs/TokensApi.md#list_tokens_customer) | List tokens for a customer
*TokensApi* | [**list_tokens_user**](docs/TokensApi.md#list_tokens_user) | List tokens for the authenticated user
*TokensApi* | [**revoke_token**](docs/TokensApi.md#revoke_token) | Revoke a token
*TokensApi* | [**revoke_token_current**](docs/TokensApi.md#revoke_token_current) | Revoke the current token
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | Create a user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | Delete a user
*UserApi* | [**get_current_user**](docs/UserApi.md#get_current_user) | Get the current user
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | Get a user
*UserApi* | [**request_password_reset**](docs/UserApi.md#request_password_reset) | Request a password reset
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | Update a user
*UserApi* | [**update_user_password**](docs/UserApi.md#update_user_password) | Update the user&#39;s password
*VclApi* | [**create_custom_vcl**](docs/VclApi.md#create_custom_vcl) | Create a custom VCL file
*VclApi* | [**delete_custom_vcl**](docs/VclApi.md#delete_custom_vcl) | Delete a custom VCL file
*VclApi* | [**get_custom_vcl**](docs/VclApi.md#get_custom_vcl) | Get a custom VCL file
*VclApi* | [**get_custom_vcl_boilerplate**](docs/VclApi.md#get_custom_vcl_boilerplate) | Get boilerplate VCL
*VclApi* | [**get_custom_vcl_generated**](docs/VclApi.md#get_custom_vcl_generated) | Get the generated VCL for a service
*VclApi* | [**get_custom_vcl_generated_highlighted**](docs/VclApi.md#get_custom_vcl_generated_highlighted) | Get the generated VCL with syntax highlighting
*VclApi* | [**get_custom_vcl_highlighted**](docs/VclApi.md#get_custom_vcl_highlighted) | Get a custom VCL file with syntax highlighting
*VclApi* | [**get_custom_vcl_raw**](docs/VclApi.md#get_custom_vcl_raw) | Download a custom VCL file
*VclApi* | [**lint_vcl_default**](docs/VclApi.md#lint_vcl_default) | Lint (validate) VCL using a default set of flags.
*VclApi* | [**lint_vcl_for_service**](docs/VclApi.md#lint_vcl_for_service) | Lint (validate) VCL using flags set for the service.
*VclApi* | [**list_custom_vcl**](docs/VclApi.md#list_custom_vcl) | List custom VCL files
*VclApi* | [**set_custom_vcl_main**](docs/VclApi.md#set_custom_vcl_main) | Set a custom VCL file as main
*VclApi* | [**update_custom_vcl**](docs/VclApi.md#update_custom_vcl) | Update a custom VCL file
*VclDiffApi* | [**vcl_diff_service_versions**](docs/VclDiffApi.md#vcl_diff_service_versions) | Get a comparison of the VCL changes between two service versions
*VersionApi* | [**activate_service_version**](docs/VersionApi.md#activate_service_version) | Activate a service version
*VersionApi* | [**activate_service_version_environment**](docs/VersionApi.md#activate_service_version_environment) | Activate a service version on the specified environment
*VersionApi* | [**clone_service_version**](docs/VersionApi.md#clone_service_version) | Clone a service version
*VersionApi* | [**create_service_version**](docs/VersionApi.md#create_service_version) | Create a service version
*VersionApi* | [**deactivate_service_version**](docs/VersionApi.md#deactivate_service_version) | Deactivate a service version
*VersionApi* | [**deactivate_service_version_environment**](docs/VersionApi.md#deactivate_service_version_environment) | Deactivate a service version on an environment
*VersionApi* | [**get_service_version**](docs/VersionApi.md#get_service_version) | Get a version of a service
*VersionApi* | [**list_service_versions**](docs/VersionApi.md#list_service_versions) | List versions of a service
*VersionApi* | [**lock_service_version**](docs/VersionApi.md#lock_service_version) | Lock a service version
*VersionApi* | [**update_service_version**](docs/VersionApi.md#update_service_version) | Update a service version
*VersionApi* | [**validate_service_version**](docs/VersionApi.md#validate_service_version) | Validate a service version
*WafActiveRulesApi* | [**bulk_delete_waf_active_rules**](docs/WafActiveRulesApi.md#bulk_delete_waf_active_rules) | Delete multiple active rules from a WAF
*WafActiveRulesApi* | [**bulk_update_waf_active_rules**](docs/WafActiveRulesApi.md#bulk_update_waf_active_rules) | Update multiple active rules
*WafActiveRulesApi* | [**create_waf_active_rule**](docs/WafActiveRulesApi.md#create_waf_active_rule) | Add a rule to a WAF as an active rule
*WafActiveRulesApi* | [**create_waf_active_rules_tag**](docs/WafActiveRulesApi.md#create_waf_active_rules_tag) | Create active rules by tag
*WafActiveRulesApi* | [**delete_waf_active_rule**](docs/WafActiveRulesApi.md#delete_waf_active_rule) | Delete an active rule
*WafActiveRulesApi* | [**get_waf_active_rule**](docs/WafActiveRulesApi.md#get_waf_active_rule) | Get an active WAF rule object
*WafActiveRulesApi* | [**list_waf_active_rules**](docs/WafActiveRulesApi.md#list_waf_active_rules) | List active rules on a WAF
*WafActiveRulesApi* | [**update_waf_active_rule**](docs/WafActiveRulesApi.md#update_waf_active_rule) | Update an active rule
*WafExclusionsApi* | [**create_waf_rule_exclusion**](docs/WafExclusionsApi.md#create_waf_rule_exclusion) | Create a WAF rule exclusion
*WafExclusionsApi* | [**delete_waf_rule_exclusion**](docs/WafExclusionsApi.md#delete_waf_rule_exclusion) | Delete a WAF rule exclusion
*WafExclusionsApi* | [**get_waf_rule_exclusion**](docs/WafExclusionsApi.md#get_waf_rule_exclusion) | Get a WAF rule exclusion
*WafExclusionsApi* | [**list_waf_rule_exclusions**](docs/WafExclusionsApi.md#list_waf_rule_exclusions) | List WAF rule exclusions
*WafExclusionsApi* | [**update_waf_rule_exclusion**](docs/WafExclusionsApi.md#update_waf_rule_exclusion) | Update a WAF rule exclusion
*WafFirewallVersionsApi* | [**clone_waf_firewall_version**](docs/WafFirewallVersionsApi.md#clone_waf_firewall_version) | Clone a firewall version
*WafFirewallVersionsApi* | [**create_waf_firewall_version**](docs/WafFirewallVersionsApi.md#create_waf_firewall_version) | Create a firewall version
*WafFirewallVersionsApi* | [**deploy_activate_waf_firewall_version**](docs/WafFirewallVersionsApi.md#deploy_activate_waf_firewall_version) | Deploy or activate a firewall version
*WafFirewallVersionsApi* | [**get_waf_firewall_version**](docs/WafFirewallVersionsApi.md#get_waf_firewall_version) | Get a firewall version
*WafFirewallVersionsApi* | [**list_waf_firewall_versions**](docs/WafFirewallVersionsApi.md#list_waf_firewall_versions) | List firewall versions
*WafFirewallVersionsApi* | [**update_waf_firewall_version**](docs/WafFirewallVersionsApi.md#update_waf_firewall_version) | Update a firewall version
*WafFirewallsApi* | [**create_waf_firewall**](docs/WafFirewallsApi.md#create_waf_firewall) | Create a firewall
*WafFirewallsApi* | [**delete_waf_firewall**](docs/WafFirewallsApi.md#delete_waf_firewall) | Delete a firewall
*WafFirewallsApi* | [**get_waf_firewall**](docs/WafFirewallsApi.md#get_waf_firewall) | Get a firewall
*WafFirewallsApi* | [**list_waf_firewalls**](docs/WafFirewallsApi.md#list_waf_firewalls) | List firewalls
*WafFirewallsApi* | [**update_waf_firewall**](docs/WafFirewallsApi.md#update_waf_firewall) | Update a firewall
*WafRuleRevisionsApi* | [**get_waf_rule_revision**](docs/WafRuleRevisionsApi.md#get_waf_rule_revision) | Get a revision of a rule
*WafRuleRevisionsApi* | [**list_waf_rule_revisions**](docs/WafRuleRevisionsApi.md#list_waf_rule_revisions) | List revisions for a rule
*WafRulesApi* | [**get_waf_rule**](docs/WafRulesApi.md#get_waf_rule) | Get a rule
*WafRulesApi* | [**list_waf_rules**](docs/WafRulesApi.md#list_waf_rules) | List available WAF rules
*WafTagsApi* | [**list_waf_tags**](docs/WafTagsApi.md#list_waf_tags) | List tags
*WholePlatformDdosHistoricalApi* | [**get_platform_ddos_historical**](docs/WholePlatformDdosHistoricalApi.md#get_platform_ddos_historical) | Get historical DDoS metrics for the entire Fastly platform


</details>

## Issues

The fastly-py API client currently does not support the following endpoints:

- [`/alerts/definitions/{definition_id}`](https://www.fastly.com/documentation/reference/api/observability/alerts/definitions) (DELETE, GET, PUT)
- [`/alerts/definitions`](https://www.fastly.com/documentation/reference/api/observability/alerts/definitions) (GET, POST)
- [`/alerts/history`](https://www.fastly.com/documentation/reference/api/observability/alerts/history) (GET)
- [`/dns/configurations/{dns_configuration_id}`](https://www.fastly.com/documentation/reference/api/) (DELETE, GET, PATCH)
- [`/dns/configurations`](https://www.fastly.com/documentation/reference/api/) (GET, POST)
- [`/domains/v1/{domain_id}`](https://www.fastly.com/documentation/reference/api/) (DELETE, GET, PATCH)
- [`/domains/v1`](https://www.fastly.com/documentation/reference/api/) (GET, POST)
- [`/notifications/integration-types`](https://developer.fastly.com/reference/api/observability/notification) (GET)
- [`/notifications/integrations/{integration_id}/rotateSigningKey`](https://developer.fastly.com/reference/api/observability/notification) (POST)
- [`/notifications/integrations/{integration_id}/signingKey`](https://developer.fastly.com/reference/api/observability/notification) (GET)
- [`/notifications/integrations/{integration_id}`](https://developer.fastly.com/reference/api/observability/notification) (DELETE, GET, PATCH)
- [`/notifications/integrations`](https://developer.fastly.com/reference/api/observability/notification) (GET, POST)
- [`/notifications/mailinglist-confirmations`](https://developer.fastly.com/reference/api/observability/notification) (POST)
- [`/resources/stores/kv/{store_id}/batch`](https://www.fastly.com/documentation/reference/api/services/resources/kv-store-item) (PUT)
- [`/security/workspaces/{workspace_id}/events/{event_id}`](https://docs.fastly.com/en/ngwaf/) (GET, PATCH)
- [`/security/workspaces/{workspace_id}/events`](https://docs.fastly.com/en/ngwaf/) (GET)
- [`/security/workspaces/{workspace_id}/redactions/{redaction_id}`](https://docs.fastly.com/en/ngwaf/) (DELETE, GET, PATCH)
- [`/security/workspaces/{workspace_id}/redactions`](https://docs.fastly.com/en/ngwaf/) (GET, POST)
- [`/security/workspaces/{workspace_id}/requests/{request_id}`](https://docs.fastly.com/en/ngwaf/) (GET)
- [`/security/workspaces/{workspace_id}/requests`](https://docs.fastly.com/en/ngwaf/) (GET)
- [`/security/workspaces/{workspace_id}/rules/{rule_id}`](https://docs.fastly.com/en/ngwaf/) (DELETE, GET, PATCH)
- [`/security/workspaces/{workspace_id}/rules`](https://docs.fastly.com/en/ngwaf/) (GET, POST)
- [`/security/workspaces/{workspace_id}/timeseries`](https://docs.fastly.com/en/ngwaf/) (GET)
- [`/security/workspaces/{workspace_id}/virtual-patches/{virtual_patch_id}`](https://docs.fastly.com/en/ngwaf/) (GET, PATCH)
- [`/security/workspaces/{workspace_id}/virtual-patches`](https://docs.fastly.com/en/ngwaf/) (GET)
- [`/security/workspaces/{workspace_id}`](https://docs.fastly.com/en/ngwaf/) (DELETE, GET, PATCH)
- [`/security/workspaces`](https://docs.fastly.com/en/ngwaf/) (GET, POST)
- [`/tls/activations/{tls_activation_id}`](https://www.fastly.com/documentation/reference/api/tls/mutual-tls/activations) (GET, PATCH)
- [`/tls/activations`](https://www.fastly.com/documentation/reference/api/tls/mutual-tls/activations) (GET)
- [`/tls/configurations/{tls_configuration_id}`](https://www.fastly.com/documentation/reference/api/) (DELETE, GET, PATCH)
- [`/tls/configurations`](https://www.fastly.com/documentation/reference/api/) (GET, POST)
- [`/v1/channel/{service_id}/ts/h/limit/{max_entries}`](https://www.fastly.com/documentation/reference/api/metrics-stats/origin-insights) (GET)
- [`/v1/channel/{service_id}/ts/h`](https://www.fastly.com/documentation/reference/api/metrics-stats/origin-insights) (GET)
- [`/v1/channel/{service_id}/ts/{start_timestamp}`](https://www.fastly.com/documentation/reference/api/metrics-stats/origin-insights) (GET)


If you encounter any non-security-related bug or unexpected behavior, please [file an issue][bug]
using the bug report template.

[bug]: https://github.com/fastly/fastly-py/issues/new?labels=bug

### Security issues

Please see our [SECURITY.md](./SECURITY.md) for guidance on reporting security-related issues.

## License

[MIT](./LICENSE).

