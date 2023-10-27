# fastly-py

A Python client library for interacting with most facets of the [Fastly API](https://developer.fastly.com/reference/api).


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

The Fastly API requires an [API token](https://developer.fastly.com/reference/api/#authentication) for most operations.  Set it by assigning `api_token` to a configuration as shown:

```python
# Authorize the client with a Fastly API token.
configuration = fastly.Configuration()
configuration.api_token = 'YOUR_API_KEY'
```

Alternatively, set the `FASTLY_API_TOKEN` environment variable.

## Documentation for API Endpoints

All URIs are relative to *https://api.fastly.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AclApi* | [**create_acl**](docs/AclApi.md#create_acl) | **POST** /service/{service_id}/version/{version_id}/acl | Create a new ACL
*AclApi* | [**delete_acl**](docs/AclApi.md#delete_acl) | **DELETE** /service/{service_id}/version/{version_id}/acl/{acl_name} | Delete an ACL
*AclApi* | [**get_acl**](docs/AclApi.md#get_acl) | **GET** /service/{service_id}/version/{version_id}/acl/{acl_name} | Describe an ACL
*AclApi* | [**list_acls**](docs/AclApi.md#list_acls) | **GET** /service/{service_id}/version/{version_id}/acl | List ACLs
*AclApi* | [**update_acl**](docs/AclApi.md#update_acl) | **PUT** /service/{service_id}/version/{version_id}/acl/{acl_name} | Update an ACL
*AclEntryApi* | [**bulk_update_acl_entries**](docs/AclEntryApi.md#bulk_update_acl_entries) | **PATCH** /service/{service_id}/acl/{acl_id}/entries | Update multiple ACL entries
*AclEntryApi* | [**create_acl_entry**](docs/AclEntryApi.md#create_acl_entry) | **POST** /service/{service_id}/acl/{acl_id}/entry | Create an ACL entry
*AclEntryApi* | [**delete_acl_entry**](docs/AclEntryApi.md#delete_acl_entry) | **DELETE** /service/{service_id}/acl/{acl_id}/entry/{acl_entry_id} | Delete an ACL entry
*AclEntryApi* | [**get_acl_entry**](docs/AclEntryApi.md#get_acl_entry) | **GET** /service/{service_id}/acl/{acl_id}/entry/{acl_entry_id} | Describe an ACL entry
*AclEntryApi* | [**list_acl_entries**](docs/AclEntryApi.md#list_acl_entries) | **GET** /service/{service_id}/acl/{acl_id}/entries | List ACL entries
*AclEntryApi* | [**update_acl_entry**](docs/AclEntryApi.md#update_acl_entry) | **PATCH** /service/{service_id}/acl/{acl_id}/entry/{acl_entry_id} | Update an ACL entry
*ApexRedirectApi* | [**create_apex_redirect**](docs/ApexRedirectApi.md#create_apex_redirect) | **POST** /service/{service_id}/version/{version_id}/apex-redirects | Create an apex redirect
*ApexRedirectApi* | [**delete_apex_redirect**](docs/ApexRedirectApi.md#delete_apex_redirect) | **DELETE** /apex-redirects/{apex_redirect_id} | Delete an apex redirect
*ApexRedirectApi* | [**get_apex_redirect**](docs/ApexRedirectApi.md#get_apex_redirect) | **GET** /apex-redirects/{apex_redirect_id} | Get an apex redirect
*ApexRedirectApi* | [**list_apex_redirects**](docs/ApexRedirectApi.md#list_apex_redirects) | **GET** /service/{service_id}/version/{version_id}/apex-redirects | List apex redirects
*ApexRedirectApi* | [**update_apex_redirect**](docs/ApexRedirectApi.md#update_apex_redirect) | **PUT** /apex-redirects/{apex_redirect_id} | Update an apex redirect
*AutomationTokensApi* | [**create_automation_token**](docs/AutomationTokensApi.md#create_automation_token) | **POST** /automation-tokens | Create Automation Token
*AutomationTokensApi* | [**get_automation_token_id**](docs/AutomationTokensApi.md#get_automation_token_id) | **GET** /automation-tokens/{id} | Retrieve an Automation Token by ID
*AutomationTokensApi* | [**get_automation_tokens_id_services**](docs/AutomationTokensApi.md#get_automation_tokens_id_services) | **GET** /automation-tokens/{id}/services | List Automation Token Services
*AutomationTokensApi* | [**list_automation_tokens**](docs/AutomationTokensApi.md#list_automation_tokens) | **GET** /automation-tokens | List Customer Automation Tokens
*AutomationTokensApi* | [**revoke_automation_token_id**](docs/AutomationTokensApi.md#revoke_automation_token_id) | **DELETE** /automation-tokens/{id} | Revoke an Automation Token by ID
*BackendApi* | [**create_backend**](docs/BackendApi.md#create_backend) | **POST** /service/{service_id}/version/{version_id}/backend | Create a backend
*BackendApi* | [**delete_backend**](docs/BackendApi.md#delete_backend) | **DELETE** /service/{service_id}/version/{version_id}/backend/{backend_name} | Delete a backend
*BackendApi* | [**get_backend**](docs/BackendApi.md#get_backend) | **GET** /service/{service_id}/version/{version_id}/backend/{backend_name} | Describe a backend
*BackendApi* | [**list_backends**](docs/BackendApi.md#list_backends) | **GET** /service/{service_id}/version/{version_id}/backend | List backends
*BackendApi* | [**update_backend**](docs/BackendApi.md#update_backend) | **PUT** /service/{service_id}/version/{version_id}/backend/{backend_name} | Update a backend
*BillingApi* | [**get_invoice**](docs/BillingApi.md#get_invoice) | **GET** /billing/v2/year/{year}/month/{month} | Get an invoice
*BillingApi* | [**get_invoice_by_id**](docs/BillingApi.md#get_invoice_by_id) | **GET** /billing/v2/account_customers/{customer_id}/invoices/{invoice_id} | Get an invoice
*BillingApi* | [**get_invoice_mtd**](docs/BillingApi.md#get_invoice_mtd) | **GET** /billing/v2/account_customers/{customer_id}/mtd_invoice | Get month-to-date billing estimate
*BillingAddressApi* | [**add_billing_addr**](docs/BillingAddressApi.md#add_billing_addr) | **POST** /customer/{customer_id}/billing_address | Add a billing address to a customer
*BillingAddressApi* | [**delete_billing_addr**](docs/BillingAddressApi.md#delete_billing_addr) | **DELETE** /customer/{customer_id}/billing_address | Delete a billing address
*BillingAddressApi* | [**get_billing_addr**](docs/BillingAddressApi.md#get_billing_addr) | **GET** /customer/{customer_id}/billing_address | Get a billing address
*BillingAddressApi* | [**update_billing_addr**](docs/BillingAddressApi.md#update_billing_addr) | **PATCH** /customer/{customer_id}/billing_address | Update a billing address
*CacheSettingsApi* | [**create_cache_settings**](docs/CacheSettingsApi.md#create_cache_settings) | **POST** /service/{service_id}/version/{version_id}/cache_settings | Create a cache settings object
*CacheSettingsApi* | [**delete_cache_settings**](docs/CacheSettingsApi.md#delete_cache_settings) | **DELETE** /service/{service_id}/version/{version_id}/cache_settings/{cache_settings_name} | Delete a cache settings object
*CacheSettingsApi* | [**get_cache_settings**](docs/CacheSettingsApi.md#get_cache_settings) | **GET** /service/{service_id}/version/{version_id}/cache_settings/{cache_settings_name} | Get a cache settings object
*CacheSettingsApi* | [**list_cache_settings**](docs/CacheSettingsApi.md#list_cache_settings) | **GET** /service/{service_id}/version/{version_id}/cache_settings | List cache settings objects
*CacheSettingsApi* | [**update_cache_settings**](docs/CacheSettingsApi.md#update_cache_settings) | **PUT** /service/{service_id}/version/{version_id}/cache_settings/{cache_settings_name} | Update a cache settings object
*ConditionApi* | [**create_condition**](docs/ConditionApi.md#create_condition) | **POST** /service/{service_id}/version/{version_id}/condition | Create a condition
*ConditionApi* | [**delete_condition**](docs/ConditionApi.md#delete_condition) | **DELETE** /service/{service_id}/version/{version_id}/condition/{condition_name} | Delete a condition
*ConditionApi* | [**get_condition**](docs/ConditionApi.md#get_condition) | **GET** /service/{service_id}/version/{version_id}/condition/{condition_name} | Describe a condition
*ConditionApi* | [**list_conditions**](docs/ConditionApi.md#list_conditions) | **GET** /service/{service_id}/version/{version_id}/condition | List conditions
*ConditionApi* | [**update_condition**](docs/ConditionApi.md#update_condition) | **PUT** /service/{service_id}/version/{version_id}/condition/{condition_name} | Update a condition
*ConfigStoreApi* | [**create_config_store**](docs/ConfigStoreApi.md#create_config_store) | **POST** /resources/stores/config | Create a config store
*ConfigStoreApi* | [**delete_config_store**](docs/ConfigStoreApi.md#delete_config_store) | **DELETE** /resources/stores/config/{config_store_id} | Delete a config store
*ConfigStoreApi* | [**get_config_store**](docs/ConfigStoreApi.md#get_config_store) | **GET** /resources/stores/config/{config_store_id} | Describe a config store
*ConfigStoreApi* | [**get_config_store_info**](docs/ConfigStoreApi.md#get_config_store_info) | **GET** /resources/stores/config/{config_store_id}/info | Get config store metadata
*ConfigStoreApi* | [**list_config_store_services**](docs/ConfigStoreApi.md#list_config_store_services) | **GET** /resources/stores/config/{config_store_id}/services | List linked services
*ConfigStoreApi* | [**list_config_stores**](docs/ConfigStoreApi.md#list_config_stores) | **GET** /resources/stores/config | List config stores
*ConfigStoreApi* | [**update_config_store**](docs/ConfigStoreApi.md#update_config_store) | **PUT** /resources/stores/config/{config_store_id} | Update a config store
*ConfigStoreItemApi* | [**bulk_update_config_store_item**](docs/ConfigStoreItemApi.md#bulk_update_config_store_item) | **PATCH** /resources/stores/config/{config_store_id}/items | Update multiple entries in a config store
*ConfigStoreItemApi* | [**create_config_store_item**](docs/ConfigStoreItemApi.md#create_config_store_item) | **POST** /resources/stores/config/{config_store_id}/item | Create an entry in a config store
*ConfigStoreItemApi* | [**delete_config_store_item**](docs/ConfigStoreItemApi.md#delete_config_store_item) | **DELETE** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Delete an item from a config store
*ConfigStoreItemApi* | [**get_config_store_item**](docs/ConfigStoreItemApi.md#get_config_store_item) | **GET** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Get an item from a config store
*ConfigStoreItemApi* | [**list_config_store_items**](docs/ConfigStoreItemApi.md#list_config_store_items) | **GET** /resources/stores/config/{config_store_id}/items | List items in a config store
*ConfigStoreItemApi* | [**update_config_store_item**](docs/ConfigStoreItemApi.md#update_config_store_item) | **PATCH** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Update an entry in a config store
*ConfigStoreItemApi* | [**upsert_config_store_item**](docs/ConfigStoreItemApi.md#upsert_config_store_item) | **PUT** /resources/stores/config/{config_store_id}/item/{config_store_item_key} | Insert or update an entry in a config store
*ContactApi* | [**create_contacts**](docs/ContactApi.md#create_contacts) | **POST** /customer/{customer_id}/contacts | Add a new customer contact
*ContactApi* | [**delete_contact**](docs/ContactApi.md#delete_contact) | **DELETE** /customer/{customer_id}/contact/{contact_id} | Delete a contact
*ContactApi* | [**list_contacts**](docs/ContactApi.md#list_contacts) | **GET** /customer/{customer_id}/contacts | List contacts
*ContentApi* | [**content_check**](docs/ContentApi.md#content_check) | **GET** /content/edge_check | Check status of content in each POP&#39;s cache
*CustomerApi* | [**delete_customer**](docs/CustomerApi.md#delete_customer) | **DELETE** /customer/{customer_id} | Delete a customer
*CustomerApi* | [**get_customer**](docs/CustomerApi.md#get_customer) | **GET** /customer/{customer_id} | Get a customer
*CustomerApi* | [**get_logged_in_customer**](docs/CustomerApi.md#get_logged_in_customer) | **GET** /current_customer | Get the logged in customer
*CustomerApi* | [**list_users**](docs/CustomerApi.md#list_users) | **GET** /customer/{customer_id}/users | List users
*CustomerApi* | [**update_customer**](docs/CustomerApi.md#update_customer) | **PUT** /customer/{customer_id} | Update a customer
*DictionaryApi* | [**create_dictionary**](docs/DictionaryApi.md#create_dictionary) | **POST** /service/{service_id}/version/{version_id}/dictionary | Create an edge dictionary
*DictionaryApi* | [**delete_dictionary**](docs/DictionaryApi.md#delete_dictionary) | **DELETE** /service/{service_id}/version/{version_id}/dictionary/{dictionary_name} | Delete an edge dictionary
*DictionaryApi* | [**get_dictionary**](docs/DictionaryApi.md#get_dictionary) | **GET** /service/{service_id}/version/{version_id}/dictionary/{dictionary_name} | Get an edge dictionary
*DictionaryApi* | [**list_dictionaries**](docs/DictionaryApi.md#list_dictionaries) | **GET** /service/{service_id}/version/{version_id}/dictionary | List edge dictionaries
*DictionaryApi* | [**update_dictionary**](docs/DictionaryApi.md#update_dictionary) | **PUT** /service/{service_id}/version/{version_id}/dictionary/{dictionary_name} | Update an edge dictionary
*DictionaryInfoApi* | [**get_dictionary_info**](docs/DictionaryInfoApi.md#get_dictionary_info) | **GET** /service/{service_id}/version/{version_id}/dictionary/{dictionary_id}/info | Get edge dictionary metadata
*DictionaryItemApi* | [**bulk_update_dictionary_item**](docs/DictionaryItemApi.md#bulk_update_dictionary_item) | **PATCH** /service/{service_id}/dictionary/{dictionary_id}/items | Update multiple entries in an edge dictionary
*DictionaryItemApi* | [**create_dictionary_item**](docs/DictionaryItemApi.md#create_dictionary_item) | **POST** /service/{service_id}/dictionary/{dictionary_id}/item | Create an entry in an edge dictionary
*DictionaryItemApi* | [**delete_dictionary_item**](docs/DictionaryItemApi.md#delete_dictionary_item) | **DELETE** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Delete an item from an edge dictionary
*DictionaryItemApi* | [**get_dictionary_item**](docs/DictionaryItemApi.md#get_dictionary_item) | **GET** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Get an item from an edge dictionary
*DictionaryItemApi* | [**list_dictionary_items**](docs/DictionaryItemApi.md#list_dictionary_items) | **GET** /service/{service_id}/dictionary/{dictionary_id}/items | List items in an edge dictionary
*DictionaryItemApi* | [**update_dictionary_item**](docs/DictionaryItemApi.md#update_dictionary_item) | **PATCH** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Update an entry in an edge dictionary
*DictionaryItemApi* | [**upsert_dictionary_item**](docs/DictionaryItemApi.md#upsert_dictionary_item) | **PUT** /service/{service_id}/dictionary/{dictionary_id}/item/{dictionary_item_key} | Insert or update an entry in an edge dictionary
*DiffApi* | [**diff_service_versions**](docs/DiffApi.md#diff_service_versions) | **GET** /service/{service_id}/diff/from/{from_version_id}/to/{to_version_id} | Diff two service versions
*DirectorApi* | [**create_director**](docs/DirectorApi.md#create_director) | **POST** /service/{service_id}/version/{version_id}/director | Create a director
*DirectorApi* | [**delete_director**](docs/DirectorApi.md#delete_director) | **DELETE** /service/{service_id}/version/{version_id}/director/{director_name} | Delete a director
*DirectorApi* | [**get_director**](docs/DirectorApi.md#get_director) | **GET** /service/{service_id}/version/{version_id}/director/{director_name} | Get a director
*DirectorApi* | [**list_directors**](docs/DirectorApi.md#list_directors) | **GET** /service/{service_id}/version/{version_id}/director | List directors
*DirectorApi* | [**update_director**](docs/DirectorApi.md#update_director) | **PUT** /service/{service_id}/version/{version_id}/director/{director_name} | Update a director
*DirectorBackendApi* | [**create_director_backend**](docs/DirectorBackendApi.md#create_director_backend) | **POST** /service/{service_id}/version/{version_id}/director/{director_name}/backend/{backend_name} | Create a director-backend relationship
*DirectorBackendApi* | [**delete_director_backend**](docs/DirectorBackendApi.md#delete_director_backend) | **DELETE** /service/{service_id}/version/{version_id}/director/{director_name}/backend/{backend_name} | Delete a director-backend relationship
*DirectorBackendApi* | [**get_director_backend**](docs/DirectorBackendApi.md#get_director_backend) | **GET** /service/{service_id}/version/{version_id}/director/{director_name}/backend/{backend_name} | Get a director-backend relationship
*DomainApi* | [**check_domain**](docs/DomainApi.md#check_domain) | **GET** /service/{service_id}/version/{version_id}/domain/{domain_name}/check | Validate DNS configuration for a single domain on a service
*DomainApi* | [**check_domains**](docs/DomainApi.md#check_domains) | **GET** /service/{service_id}/version/{version_id}/domain/check_all | Validate DNS configuration for all domains on a service
*DomainApi* | [**create_domain**](docs/DomainApi.md#create_domain) | **POST** /service/{service_id}/version/{version_id}/domain | Add a domain name to a service
*DomainApi* | [**delete_domain**](docs/DomainApi.md#delete_domain) | **DELETE** /service/{service_id}/version/{version_id}/domain/{domain_name} | Remove a domain from a service
*DomainApi* | [**get_domain**](docs/DomainApi.md#get_domain) | **GET** /service/{service_id}/version/{version_id}/domain/{domain_name} | Describe a domain
*DomainApi* | [**list_domains**](docs/DomainApi.md#list_domains) | **GET** /service/{service_id}/version/{version_id}/domain | List domains
*DomainApi* | [**update_domain**](docs/DomainApi.md#update_domain) | **PUT** /service/{service_id}/version/{version_id}/domain/{domain_name} | Update a domain
*DomainInspectorHistoricalApi* | [**get_domain_inspector_historical**](docs/DomainInspectorHistoricalApi.md#get_domain_inspector_historical) | **GET** /metrics/domains/services/{service_id} | Get historical domain data for a service
*DomainInspectorRealtimeApi* | [**get_domain_inspector_last120_seconds**](docs/DomainInspectorRealtimeApi.md#get_domain_inspector_last120_seconds) | **GET** /v1/domains/{service_id}/ts/h | Get real-time domain data for the last 120 seconds
*DomainInspectorRealtimeApi* | [**get_domain_inspector_last_max_entries**](docs/DomainInspectorRealtimeApi.md#get_domain_inspector_last_max_entries) | **GET** /v1/domains/{service_id}/ts/h/limit/{max_entries} | Get a limited number of real-time domain data entries
*DomainInspectorRealtimeApi* | [**get_domain_inspector_last_second**](docs/DomainInspectorRealtimeApi.md#get_domain_inspector_last_second) | **GET** /v1/domains/{service_id}/ts/{start_timestamp} | Get real-time domain data from a specified time
*DomainOwnershipsApi* | [**list_domain_ownerships**](docs/DomainOwnershipsApi.md#list_domain_ownerships) | **GET** /domain-ownerships | List domain-ownerships
*EnabledProductsApi* | [**disable_product**](docs/EnabledProductsApi.md#disable_product) | **DELETE** /enabled-products/{product_id}/services/{service_id} | Disable a product
*EnabledProductsApi* | [**enable_product**](docs/EnabledProductsApi.md#enable_product) | **PUT** /enabled-products/{product_id}/services/{service_id} | Enable a product
*EnabledProductsApi* | [**get_enabled_product**](docs/EnabledProductsApi.md#get_enabled_product) | **GET** /enabled-products/{product_id}/services/{service_id} | Get enabled product
*EventsApi* | [**get_event**](docs/EventsApi.md#get_event) | **GET** /events/{event_id} | Get an event
*EventsApi* | [**list_events**](docs/EventsApi.md#list_events) | **GET** /events | List events
*GzipApi* | [**create_gzip_config**](docs/GzipApi.md#create_gzip_config) | **POST** /service/{service_id}/version/{version_id}/gzip | Create a gzip configuration
*GzipApi* | [**delete_gzip_config**](docs/GzipApi.md#delete_gzip_config) | **DELETE** /service/{service_id}/version/{version_id}/gzip/{gzip_name} | Delete a gzip configuration
*GzipApi* | [**get_gzip_configs**](docs/GzipApi.md#get_gzip_configs) | **GET** /service/{service_id}/version/{version_id}/gzip/{gzip_name} | Get a gzip configuration
*GzipApi* | [**list_gzip_configs**](docs/GzipApi.md#list_gzip_configs) | **GET** /service/{service_id}/version/{version_id}/gzip | List gzip configurations
*GzipApi* | [**update_gzip_config**](docs/GzipApi.md#update_gzip_config) | **PUT** /service/{service_id}/version/{version_id}/gzip/{gzip_name} | Update a gzip configuration
*HeaderApi* | [**create_header_object**](docs/HeaderApi.md#create_header_object) | **POST** /service/{service_id}/version/{version_id}/header | Create a Header object
*HeaderApi* | [**delete_header_object**](docs/HeaderApi.md#delete_header_object) | **DELETE** /service/{service_id}/version/{version_id}/header/{header_name} | Delete a Header object
*HeaderApi* | [**get_header_object**](docs/HeaderApi.md#get_header_object) | **GET** /service/{service_id}/version/{version_id}/header/{header_name} | Get a Header object
*HeaderApi* | [**list_header_objects**](docs/HeaderApi.md#list_header_objects) | **GET** /service/{service_id}/version/{version_id}/header | List Header objects
*HeaderApi* | [**update_header_object**](docs/HeaderApi.md#update_header_object) | **PUT** /service/{service_id}/version/{version_id}/header/{header_name} | Update a Header object
*HealthcheckApi* | [**create_healthcheck**](docs/HealthcheckApi.md#create_healthcheck) | **POST** /service/{service_id}/version/{version_id}/healthcheck | Create a health check
*HealthcheckApi* | [**delete_healthcheck**](docs/HealthcheckApi.md#delete_healthcheck) | **DELETE** /service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name} | Delete a health check
*HealthcheckApi* | [**get_healthcheck**](docs/HealthcheckApi.md#get_healthcheck) | **GET** /service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name} | Get a health check
*HealthcheckApi* | [**list_healthchecks**](docs/HealthcheckApi.md#list_healthchecks) | **GET** /service/{service_id}/version/{version_id}/healthcheck | List health checks
*HealthcheckApi* | [**update_healthcheck**](docs/HealthcheckApi.md#update_healthcheck) | **PUT** /service/{service_id}/version/{version_id}/healthcheck/{healthcheck_name} | Update a health check
*HistoricalApi* | [**get_hist_stats**](docs/HistoricalApi.md#get_hist_stats) | **GET** /stats | Get historical stats
*HistoricalApi* | [**get_hist_stats_aggregated**](docs/HistoricalApi.md#get_hist_stats_aggregated) | **GET** /stats/aggregate | Get aggregated historical stats
*HistoricalApi* | [**get_hist_stats_field**](docs/HistoricalApi.md#get_hist_stats_field) | **GET** /stats/field/{field} | Get historical stats for a single field
*HistoricalApi* | [**get_hist_stats_service**](docs/HistoricalApi.md#get_hist_stats_service) | **GET** /stats/service/{service_id} | Get historical stats for a single service
*HistoricalApi* | [**get_hist_stats_service_field**](docs/HistoricalApi.md#get_hist_stats_service_field) | **GET** /stats/service/{service_id}/field/{field} | Get historical stats for a single service/field combination
*HistoricalApi* | [**get_regions**](docs/HistoricalApi.md#get_regions) | **GET** /stats/regions | Get region codes
*HistoricalApi* | [**get_usage**](docs/HistoricalApi.md#get_usage) | **GET** /stats/usage | Get usage statistics
*HistoricalApi* | [**get_usage_month**](docs/HistoricalApi.md#get_usage_month) | **GET** /stats/usage_by_month | Get month-to-date usage statistics
*HistoricalApi* | [**get_usage_service**](docs/HistoricalApi.md#get_usage_service) | **GET** /stats/usage_by_service | Get usage statistics per service
*Http3Api* | [**create_http3**](docs/Http3Api.md#create_http3) | **POST** /service/{service_id}/version/{version_id}/http3 | Enable support for HTTP/3
*Http3Api* | [**delete_http3**](docs/Http3Api.md#delete_http3) | **DELETE** /service/{service_id}/version/{version_id}/http3 | Disable support for HTTP/3
*Http3Api* | [**get_http3**](docs/Http3Api.md#get_http3) | **GET** /service/{service_id}/version/{version_id}/http3 | Get HTTP/3 status
*IamPermissionsApi* | [**list_permissions**](docs/IamPermissionsApi.md#list_permissions) | **GET** /permissions | List permissions
*IamRolesApi* | [**add_role_permissions**](docs/IamRolesApi.md#add_role_permissions) | **POST** /roles/{role_id}/permissions | Add permissions to a role
*IamRolesApi* | [**create_a_role**](docs/IamRolesApi.md#create_a_role) | **POST** /roles | Create a role
*IamRolesApi* | [**delete_a_role**](docs/IamRolesApi.md#delete_a_role) | **DELETE** /roles/{role_id} | Delete a role
*IamRolesApi* | [**get_a_role**](docs/IamRolesApi.md#get_a_role) | **GET** /roles/{role_id} | Get a role
*IamRolesApi* | [**list_role_permissions**](docs/IamRolesApi.md#list_role_permissions) | **GET** /roles/{role_id}/permissions | List permissions in a role
*IamRolesApi* | [**list_roles**](docs/IamRolesApi.md#list_roles) | **GET** /roles | List roles
*IamRolesApi* | [**remove_role_permissions**](docs/IamRolesApi.md#remove_role_permissions) | **DELETE** /roles/{role_id}/permissions | Remove permissions from a role
*IamRolesApi* | [**update_a_role**](docs/IamRolesApi.md#update_a_role) | **PATCH** /roles/{role_id} | Update a role
*IamServiceGroupsApi* | [**add_service_group_services**](docs/IamServiceGroupsApi.md#add_service_group_services) | **POST** /service-groups/{service_group_id}/services | Add services in a service group
*IamServiceGroupsApi* | [**create_a_service_group**](docs/IamServiceGroupsApi.md#create_a_service_group) | **POST** /service-groups | Create a service group
*IamServiceGroupsApi* | [**delete_a_service_group**](docs/IamServiceGroupsApi.md#delete_a_service_group) | **DELETE** /service-groups/{service_group_id} | Delete a service group
*IamServiceGroupsApi* | [**get_a_service_group**](docs/IamServiceGroupsApi.md#get_a_service_group) | **GET** /service-groups/{service_group_id} | Get a service group
*IamServiceGroupsApi* | [**list_service_group_services**](docs/IamServiceGroupsApi.md#list_service_group_services) | **GET** /service-groups/{service_group_id}/services | List services to a service group
*IamServiceGroupsApi* | [**list_service_groups**](docs/IamServiceGroupsApi.md#list_service_groups) | **GET** /service-groups | List service groups
*IamServiceGroupsApi* | [**remove_service_group_services**](docs/IamServiceGroupsApi.md#remove_service_group_services) | **DELETE** /service-groups/{service_group_id}/services | Remove services from a service group
*IamServiceGroupsApi* | [**update_a_service_group**](docs/IamServiceGroupsApi.md#update_a_service_group) | **PATCH** /service-groups/{service_group_id} | Update a service group
*IamUserGroupsApi* | [**add_user_group_members**](docs/IamUserGroupsApi.md#add_user_group_members) | **POST** /user-groups/{user_group_id}/members | Add members to a user group
*IamUserGroupsApi* | [**add_user_group_roles**](docs/IamUserGroupsApi.md#add_user_group_roles) | **POST** /user-groups/{user_group_id}/roles | Add roles to a user group
*IamUserGroupsApi* | [**add_user_group_service_groups**](docs/IamUserGroupsApi.md#add_user_group_service_groups) | **POST** /user-groups/{user_group_id}/service-groups | Add service groups to a user group
*IamUserGroupsApi* | [**create_a_user_group**](docs/IamUserGroupsApi.md#create_a_user_group) | **POST** /user-groups | Create a user group
*IamUserGroupsApi* | [**delete_a_user_group**](docs/IamUserGroupsApi.md#delete_a_user_group) | **DELETE** /user-groups/{user_group_id} | Delete a user group
*IamUserGroupsApi* | [**get_a_user_group**](docs/IamUserGroupsApi.md#get_a_user_group) | **GET** /user-groups/{user_group_id} | Get a user group
*IamUserGroupsApi* | [**list_user_group_members**](docs/IamUserGroupsApi.md#list_user_group_members) | **GET** /user-groups/{user_group_id}/members | List members of a user group
*IamUserGroupsApi* | [**list_user_group_roles**](docs/IamUserGroupsApi.md#list_user_group_roles) | **GET** /user-groups/{user_group_id}/roles | List roles in a user group
*IamUserGroupsApi* | [**list_user_group_service_groups**](docs/IamUserGroupsApi.md#list_user_group_service_groups) | **GET** /user-groups/{user_group_id}/service-groups | List service groups in a user group
*IamUserGroupsApi* | [**list_user_groups**](docs/IamUserGroupsApi.md#list_user_groups) | **GET** /user-groups | List user groups
*IamUserGroupsApi* | [**remove_user_group_members**](docs/IamUserGroupsApi.md#remove_user_group_members) | **DELETE** /user-groups/{user_group_id}/members | Remove members of a user group
*IamUserGroupsApi* | [**remove_user_group_roles**](docs/IamUserGroupsApi.md#remove_user_group_roles) | **DELETE** /user-groups/{user_group_id}/roles | Remove roles from a user group
*IamUserGroupsApi* | [**remove_user_group_service_groups**](docs/IamUserGroupsApi.md#remove_user_group_service_groups) | **DELETE** /user-groups/{user_group_id}/service-groups | Remove service groups from a user group
*IamUserGroupsApi* | [**update_a_user_group**](docs/IamUserGroupsApi.md#update_a_user_group) | **PATCH** /user-groups/{user_group_id} | Update a user group
*InvitationsApi* | [**create_invitation**](docs/InvitationsApi.md#create_invitation) | **POST** /invitations | Create an invitation
*InvitationsApi* | [**delete_invitation**](docs/InvitationsApi.md#delete_invitation) | **DELETE** /invitations/{invitation_id} | Delete an invitation
*InvitationsApi* | [**list_invitations**](docs/InvitationsApi.md#list_invitations) | **GET** /invitations | List invitations
*KvStoreApi* | [**create_store**](docs/KvStoreApi.md#create_store) | **POST** /resources/stores/kv | Create a KV store.
*KvStoreApi* | [**delete_store**](docs/KvStoreApi.md#delete_store) | **DELETE** /resources/stores/kv/{store_id} | Delete a KV store.
*KvStoreApi* | [**get_store**](docs/KvStoreApi.md#get_store) | **GET** /resources/stores/kv/{store_id} | Describe a KV store.
*KvStoreApi* | [**get_stores**](docs/KvStoreApi.md#get_stores) | **GET** /resources/stores/kv | List KV stores.
*KvStoreItemApi* | [**delete_key_from_store**](docs/KvStoreItemApi.md#delete_key_from_store) | **DELETE** /resources/stores/kv/{store_id}/keys/{key_name} | Delete kv store item.
*KvStoreItemApi* | [**get_keys**](docs/KvStoreItemApi.md#get_keys) | **GET** /resources/stores/kv/{store_id}/keys | List kv store keys.
*KvStoreItemApi* | [**get_value_for_key**](docs/KvStoreItemApi.md#get_value_for_key) | **GET** /resources/stores/kv/{store_id}/keys/{key_name} | Get the value of an kv store item
*KvStoreItemApi* | [**set_value_for_key**](docs/KvStoreItemApi.md#set_value_for_key) | **PUT** /resources/stores/kv/{store_id}/keys/{key_name} | Insert an item into an kv store
*LegacyWafConfigurationSetsApi* | [**list_waf_config_sets**](docs/LegacyWafConfigurationSetsApi.md#list_waf_config_sets) | **GET** /wafs/configuration_sets | List configuration sets
*LegacyWafConfigurationSetsApi* | [**list_wafs_config_set**](docs/LegacyWafConfigurationSetsApi.md#list_wafs_config_set) | **GET** /wafs/configuration_sets/{configuration_set_id}/relationships/wafs | List WAFs currently using a configuration set
*LegacyWafConfigurationSetsApi* | [**use_waf_config_set**](docs/LegacyWafConfigurationSetsApi.md#use_waf_config_set) | **PATCH** /wafs/configuration_sets/{configuration_set_id}/relationships/wafs | Apply a configuration set to a WAF
*LegacyWafFirewallApi* | [**create_legacy_waf_firewall_service**](docs/LegacyWafFirewallApi.md#create_legacy_waf_firewall_service) | **POST** /service/{service_id}/version/{version_id}/wafs | Create a firewall
*LegacyWafFirewallApi* | [**disable_legacy_waf_firewall**](docs/LegacyWafFirewallApi.md#disable_legacy_waf_firewall) | **PATCH** /wafs/{firewall_id}/disable | Disable a firewall
*LegacyWafFirewallApi* | [**enable_legacy_waf_firewall**](docs/LegacyWafFirewallApi.md#enable_legacy_waf_firewall) | **PATCH** /wafs/{firewall_id}/enable | Enable a firewall
*LegacyWafFirewallApi* | [**get_legacy_waf_firewall**](docs/LegacyWafFirewallApi.md#get_legacy_waf_firewall) | **GET** /wafs/{firewall_id} | Get a firewall object
*LegacyWafFirewallApi* | [**get_legacy_waf_firewall_service**](docs/LegacyWafFirewallApi.md#get_legacy_waf_firewall_service) | **GET** /service/{service_id}/version/{version_id}/wafs/{firewall_id} | Get a firewall
*LegacyWafFirewallApi* | [**list_legacy_waf_firewalls**](docs/LegacyWafFirewallApi.md#list_legacy_waf_firewalls) | **GET** /wafs | List active firewalls
*LegacyWafFirewallApi* | [**list_legacy_waf_firewalls_service**](docs/LegacyWafFirewallApi.md#list_legacy_waf_firewalls_service) | **GET** /service/{service_id}/version/{version_id}/wafs | List firewalls
*LegacyWafFirewallApi* | [**update_legacy_waf_firewall_service**](docs/LegacyWafFirewallApi.md#update_legacy_waf_firewall_service) | **PATCH** /service/{service_id}/version/{version_id}/wafs/{firewall_id} | Update a firewall
*LegacyWafOwaspApi* | [**create_owasp_settings**](docs/LegacyWafOwaspApi.md#create_owasp_settings) | **POST** /service/{service_id}/wafs/{firewall_id}/owasp | Create an OWASP settings object
*LegacyWafOwaspApi* | [**get_owasp_settings**](docs/LegacyWafOwaspApi.md#get_owasp_settings) | **GET** /service/{service_id}/wafs/{firewall_id}/owasp | Get the OWASP settings object
*LegacyWafOwaspApi* | [**update_owasp_settings**](docs/LegacyWafOwaspApi.md#update_owasp_settings) | **PATCH** /service/{service_id}/wafs/{firewall_id}/owasp | Update the OWASP settings object
*LegacyWafRuleApi* | [**get_legacy_waf_firewall_rule_vcl**](docs/LegacyWafRuleApi.md#get_legacy_waf_firewall_rule_vcl) | **GET** /wafs/{firewall_id}/rules/{waf_rule_id}/vcl | Get VCL for a rule associated with a firewall
*LegacyWafRuleApi* | [**get_legacy_waf_rule**](docs/LegacyWafRuleApi.md#get_legacy_waf_rule) | **GET** /wafs/rules/{waf_rule_id} | Get a rule
*LegacyWafRuleApi* | [**get_legacy_waf_rule_vcl**](docs/LegacyWafRuleApi.md#get_legacy_waf_rule_vcl) | **GET** /wafs/rules/{waf_rule_id}/vcl | Get VCL for a rule
*LegacyWafRuleApi* | [**list_legacy_waf_rules**](docs/LegacyWafRuleApi.md#list_legacy_waf_rules) | **GET** /wafs/rules | List rules in the latest configuration set
*LegacyWafRuleStatusApi* | [**get_waf_firewall_rule_status**](docs/LegacyWafRuleStatusApi.md#get_waf_firewall_rule_status) | **GET** /service/{service_id}/wafs/{firewall_id}/rules/{waf_rule_id}/rule_status | Get the status of a rule on a firewall
*LegacyWafRuleStatusApi* | [**list_waf_firewall_rule_statuses**](docs/LegacyWafRuleStatusApi.md#list_waf_firewall_rule_statuses) | **GET** /service/{service_id}/wafs/{firewall_id}/rule_statuses | List rule statuses
*LegacyWafRuleStatusApi* | [**update_waf_firewall_rule_status**](docs/LegacyWafRuleStatusApi.md#update_waf_firewall_rule_status) | **PATCH** /service/{service_id}/wafs/{firewall_id}/rules/{waf_rule_id}/rule_status | Update the status of a rule
*LegacyWafRuleStatusApi* | [**update_waf_firewall_rule_statuses_tag**](docs/LegacyWafRuleStatusApi.md#update_waf_firewall_rule_statuses_tag) | **POST** /service/{service_id}/wafs/{firewall_id}/rule_statuses | Create or update status of a tagged group of rules
*LegacyWafRulesetApi* | [**get_waf_ruleset**](docs/LegacyWafRulesetApi.md#get_waf_ruleset) | **GET** /service/{service_id}/wafs/{firewall_id}/ruleset | Get a WAF ruleset
*LegacyWafRulesetApi* | [**get_waf_ruleset_vcl**](docs/LegacyWafRulesetApi.md#get_waf_ruleset_vcl) | **GET** /service/{service_id}/wafs/{firewall_id}/ruleset/preview | Generate WAF ruleset VCL
*LegacyWafRulesetApi* | [**update_waf_ruleset**](docs/LegacyWafRulesetApi.md#update_waf_ruleset) | **PATCH** /service/{service_id}/wafs/{firewall_id}/ruleset | Update a WAF ruleset
*LegacyWafTagApi* | [**list_legacy_waf_tags**](docs/LegacyWafTagApi.md#list_legacy_waf_tags) | **GET** /wafs/tags | List WAF tags
*LegacyWafUpdateStatusApi* | [**get_waf_update_status**](docs/LegacyWafUpdateStatusApi.md#get_waf_update_status) | **GET** /service/{service_id}/wafs/{firewall_id}/update_statuses/{update_status_id} | Get the status of a WAF update
*LegacyWafUpdateStatusApi* | [**list_waf_update_statuses**](docs/LegacyWafUpdateStatusApi.md#list_waf_update_statuses) | **GET** /service/{service_id}/wafs/{firewall_id}/update_statuses | List update statuses
*LoggingAzureblobApi* | [**create_log_azure**](docs/LoggingAzureblobApi.md#create_log_azure) | **POST** /service/{service_id}/version/{version_id}/logging/azureblob | Create an Azure Blob Storage log endpoint
*LoggingAzureblobApi* | [**delete_log_azure**](docs/LoggingAzureblobApi.md#delete_log_azure) | **DELETE** /service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name} | Delete the Azure Blob Storage log endpoint
*LoggingAzureblobApi* | [**get_log_azure**](docs/LoggingAzureblobApi.md#get_log_azure) | **GET** /service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name} | Get an Azure Blob Storage log endpoint
*LoggingAzureblobApi* | [**list_log_azure**](docs/LoggingAzureblobApi.md#list_log_azure) | **GET** /service/{service_id}/version/{version_id}/logging/azureblob | List Azure Blob Storage log endpoints
*LoggingAzureblobApi* | [**update_log_azure**](docs/LoggingAzureblobApi.md#update_log_azure) | **PUT** /service/{service_id}/version/{version_id}/logging/azureblob/{logging_azureblob_name} | Update an Azure Blob Storage log endpoint
*LoggingBigqueryApi* | [**create_log_bigquery**](docs/LoggingBigqueryApi.md#create_log_bigquery) | **POST** /service/{service_id}/version/{version_id}/logging/bigquery | Create a BigQuery log endpoint
*LoggingBigqueryApi* | [**delete_log_bigquery**](docs/LoggingBigqueryApi.md#delete_log_bigquery) | **DELETE** /service/{service_id}/version/{version_id}/logging/bigquery/{logging_bigquery_name} | Delete a BigQuery log endpoint
*LoggingBigqueryApi* | [**get_log_bigquery**](docs/LoggingBigqueryApi.md#get_log_bigquery) | **GET** /service/{service_id}/version/{version_id}/logging/bigquery/{logging_bigquery_name} | Get a BigQuery log endpoint
*LoggingBigqueryApi* | [**list_log_bigquery**](docs/LoggingBigqueryApi.md#list_log_bigquery) | **GET** /service/{service_id}/version/{version_id}/logging/bigquery | List BigQuery log endpoints
*LoggingBigqueryApi* | [**update_log_bigquery**](docs/LoggingBigqueryApi.md#update_log_bigquery) | **PUT** /service/{service_id}/version/{version_id}/logging/bigquery/{logging_bigquery_name} | Update a BigQuery log endpoint
*LoggingCloudfilesApi* | [**create_log_cloudfiles**](docs/LoggingCloudfilesApi.md#create_log_cloudfiles) | **POST** /service/{service_id}/version/{version_id}/logging/cloudfiles | Create a Cloud Files log endpoint
*LoggingCloudfilesApi* | [**delete_log_cloudfiles**](docs/LoggingCloudfilesApi.md#delete_log_cloudfiles) | **DELETE** /service/{service_id}/version/{version_id}/logging/cloudfiles/{logging_cloudfiles_name} | Delete the Cloud Files log endpoint
*LoggingCloudfilesApi* | [**get_log_cloudfiles**](docs/LoggingCloudfilesApi.md#get_log_cloudfiles) | **GET** /service/{service_id}/version/{version_id}/logging/cloudfiles/{logging_cloudfiles_name} | Get a Cloud Files log endpoint
*LoggingCloudfilesApi* | [**list_log_cloudfiles**](docs/LoggingCloudfilesApi.md#list_log_cloudfiles) | **GET** /service/{service_id}/version/{version_id}/logging/cloudfiles | List Cloud Files log endpoints
*LoggingCloudfilesApi* | [**update_log_cloudfiles**](docs/LoggingCloudfilesApi.md#update_log_cloudfiles) | **PUT** /service/{service_id}/version/{version_id}/logging/cloudfiles/{logging_cloudfiles_name} | Update the Cloud Files log endpoint
*LoggingDatadogApi* | [**create_log_datadog**](docs/LoggingDatadogApi.md#create_log_datadog) | **POST** /service/{service_id}/version/{version_id}/logging/datadog | Create a Datadog log endpoint
*LoggingDatadogApi* | [**delete_log_datadog**](docs/LoggingDatadogApi.md#delete_log_datadog) | **DELETE** /service/{service_id}/version/{version_id}/logging/datadog/{logging_datadog_name} | Delete a Datadog log endpoint
*LoggingDatadogApi* | [**get_log_datadog**](docs/LoggingDatadogApi.md#get_log_datadog) | **GET** /service/{service_id}/version/{version_id}/logging/datadog/{logging_datadog_name} | Get a Datadog log endpoint
*LoggingDatadogApi* | [**list_log_datadog**](docs/LoggingDatadogApi.md#list_log_datadog) | **GET** /service/{service_id}/version/{version_id}/logging/datadog | List Datadog log endpoints
*LoggingDatadogApi* | [**update_log_datadog**](docs/LoggingDatadogApi.md#update_log_datadog) | **PUT** /service/{service_id}/version/{version_id}/logging/datadog/{logging_datadog_name} | Update a Datadog log endpoint
*LoggingDigitaloceanApi* | [**create_log_digocean**](docs/LoggingDigitaloceanApi.md#create_log_digocean) | **POST** /service/{service_id}/version/{version_id}/logging/digitalocean | Create a DigitalOcean Spaces log endpoint
*LoggingDigitaloceanApi* | [**delete_log_digocean**](docs/LoggingDigitaloceanApi.md#delete_log_digocean) | **DELETE** /service/{service_id}/version/{version_id}/logging/digitalocean/{logging_digitalocean_name} | Delete a DigitalOcean Spaces log endpoint
*LoggingDigitaloceanApi* | [**get_log_digocean**](docs/LoggingDigitaloceanApi.md#get_log_digocean) | **GET** /service/{service_id}/version/{version_id}/logging/digitalocean/{logging_digitalocean_name} | Get a DigitalOcean Spaces log endpoint
*LoggingDigitaloceanApi* | [**list_log_digocean**](docs/LoggingDigitaloceanApi.md#list_log_digocean) | **GET** /service/{service_id}/version/{version_id}/logging/digitalocean | List DigitalOcean Spaces log endpoints
*LoggingDigitaloceanApi* | [**update_log_digocean**](docs/LoggingDigitaloceanApi.md#update_log_digocean) | **PUT** /service/{service_id}/version/{version_id}/logging/digitalocean/{logging_digitalocean_name} | Update a DigitalOcean Spaces log endpoint
*LoggingElasticsearchApi* | [**create_log_elasticsearch**](docs/LoggingElasticsearchApi.md#create_log_elasticsearch) | **POST** /service/{service_id}/version/{version_id}/logging/elasticsearch | Create an Elasticsearch log endpoint
*LoggingElasticsearchApi* | [**delete_log_elasticsearch**](docs/LoggingElasticsearchApi.md#delete_log_elasticsearch) | **DELETE** /service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name} | Delete an Elasticsearch log endpoint
*LoggingElasticsearchApi* | [**get_log_elasticsearch**](docs/LoggingElasticsearchApi.md#get_log_elasticsearch) | **GET** /service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name} | Get an Elasticsearch log endpoint
*LoggingElasticsearchApi* | [**list_log_elasticsearch**](docs/LoggingElasticsearchApi.md#list_log_elasticsearch) | **GET** /service/{service_id}/version/{version_id}/logging/elasticsearch | List Elasticsearch log endpoints
*LoggingElasticsearchApi* | [**update_log_elasticsearch**](docs/LoggingElasticsearchApi.md#update_log_elasticsearch) | **PUT** /service/{service_id}/version/{version_id}/logging/elasticsearch/{logging_elasticsearch_name} | Update an Elasticsearch log endpoint
*LoggingFtpApi* | [**create_log_ftp**](docs/LoggingFtpApi.md#create_log_ftp) | **POST** /service/{service_id}/version/{version_id}/logging/ftp | Create an FTP log endpoint
*LoggingFtpApi* | [**delete_log_ftp**](docs/LoggingFtpApi.md#delete_log_ftp) | **DELETE** /service/{service_id}/version/{version_id}/logging/ftp/{logging_ftp_name} | Delete an FTP log endpoint
*LoggingFtpApi* | [**get_log_ftp**](docs/LoggingFtpApi.md#get_log_ftp) | **GET** /service/{service_id}/version/{version_id}/logging/ftp/{logging_ftp_name} | Get an FTP log endpoint
*LoggingFtpApi* | [**list_log_ftp**](docs/LoggingFtpApi.md#list_log_ftp) | **GET** /service/{service_id}/version/{version_id}/logging/ftp | List FTP log endpoints
*LoggingFtpApi* | [**update_log_ftp**](docs/LoggingFtpApi.md#update_log_ftp) | **PUT** /service/{service_id}/version/{version_id}/logging/ftp/{logging_ftp_name} | Update an FTP log endpoint
*LoggingGcsApi* | [**create_log_gcs**](docs/LoggingGcsApi.md#create_log_gcs) | **POST** /service/{service_id}/version/{version_id}/logging/gcs | Create a GCS log endpoint
*LoggingGcsApi* | [**delete_log_gcs**](docs/LoggingGcsApi.md#delete_log_gcs) | **DELETE** /service/{service_id}/version/{version_id}/logging/gcs/{logging_gcs_name} | Delete a GCS log endpoint
*LoggingGcsApi* | [**get_log_gcs**](docs/LoggingGcsApi.md#get_log_gcs) | **GET** /service/{service_id}/version/{version_id}/logging/gcs/{logging_gcs_name} | Get a GCS log endpoint
*LoggingGcsApi* | [**list_log_gcs**](docs/LoggingGcsApi.md#list_log_gcs) | **GET** /service/{service_id}/version/{version_id}/logging/gcs | List GCS log endpoints
*LoggingGcsApi* | [**update_log_gcs**](docs/LoggingGcsApi.md#update_log_gcs) | **PUT** /service/{service_id}/version/{version_id}/logging/gcs/{logging_gcs_name} | Update a GCS log endpoint
*LoggingHerokuApi* | [**create_log_heroku**](docs/LoggingHerokuApi.md#create_log_heroku) | **POST** /service/{service_id}/version/{version_id}/logging/heroku | Create a Heroku log endpoint
*LoggingHerokuApi* | [**delete_log_heroku**](docs/LoggingHerokuApi.md#delete_log_heroku) | **DELETE** /service/{service_id}/version/{version_id}/logging/heroku/{logging_heroku_name} | Delete the Heroku log endpoint
*LoggingHerokuApi* | [**get_log_heroku**](docs/LoggingHerokuApi.md#get_log_heroku) | **GET** /service/{service_id}/version/{version_id}/logging/heroku/{logging_heroku_name} | Get a Heroku log endpoint
*LoggingHerokuApi* | [**list_log_heroku**](docs/LoggingHerokuApi.md#list_log_heroku) | **GET** /service/{service_id}/version/{version_id}/logging/heroku | List Heroku log endpoints
*LoggingHerokuApi* | [**update_log_heroku**](docs/LoggingHerokuApi.md#update_log_heroku) | **PUT** /service/{service_id}/version/{version_id}/logging/heroku/{logging_heroku_name} | Update the Heroku log endpoint
*LoggingHoneycombApi* | [**create_log_honeycomb**](docs/LoggingHoneycombApi.md#create_log_honeycomb) | **POST** /service/{service_id}/version/{version_id}/logging/honeycomb | Create a Honeycomb log endpoint
*LoggingHoneycombApi* | [**delete_log_honeycomb**](docs/LoggingHoneycombApi.md#delete_log_honeycomb) | **DELETE** /service/{service_id}/version/{version_id}/logging/honeycomb/{logging_honeycomb_name} | Delete the Honeycomb log endpoint
*LoggingHoneycombApi* | [**get_log_honeycomb**](docs/LoggingHoneycombApi.md#get_log_honeycomb) | **GET** /service/{service_id}/version/{version_id}/logging/honeycomb/{logging_honeycomb_name} | Get a Honeycomb log endpoint
*LoggingHoneycombApi* | [**list_log_honeycomb**](docs/LoggingHoneycombApi.md#list_log_honeycomb) | **GET** /service/{service_id}/version/{version_id}/logging/honeycomb | List Honeycomb log endpoints
*LoggingHoneycombApi* | [**update_log_honeycomb**](docs/LoggingHoneycombApi.md#update_log_honeycomb) | **PUT** /service/{service_id}/version/{version_id}/logging/honeycomb/{logging_honeycomb_name} | Update a Honeycomb log endpoint
*LoggingHttpsApi* | [**create_log_https**](docs/LoggingHttpsApi.md#create_log_https) | **POST** /service/{service_id}/version/{version_id}/logging/https | Create an HTTPS log endpoint
*LoggingHttpsApi* | [**delete_log_https**](docs/LoggingHttpsApi.md#delete_log_https) | **DELETE** /service/{service_id}/version/{version_id}/logging/https/{logging_https_name} | Delete an HTTPS log endpoint
*LoggingHttpsApi* | [**get_log_https**](docs/LoggingHttpsApi.md#get_log_https) | **GET** /service/{service_id}/version/{version_id}/logging/https/{logging_https_name} | Get an HTTPS log endpoint
*LoggingHttpsApi* | [**list_log_https**](docs/LoggingHttpsApi.md#list_log_https) | **GET** /service/{service_id}/version/{version_id}/logging/https | List HTTPS log endpoints
*LoggingHttpsApi* | [**update_log_https**](docs/LoggingHttpsApi.md#update_log_https) | **PUT** /service/{service_id}/version/{version_id}/logging/https/{logging_https_name} | Update an HTTPS log endpoint
*LoggingKafkaApi* | [**create_log_kafka**](docs/LoggingKafkaApi.md#create_log_kafka) | **POST** /service/{service_id}/version/{version_id}/logging/kafka | Create a Kafka log endpoint
*LoggingKafkaApi* | [**delete_log_kafka**](docs/LoggingKafkaApi.md#delete_log_kafka) | **DELETE** /service/{service_id}/version/{version_id}/logging/kafka/{logging_kafka_name} | Delete the Kafka log endpoint
*LoggingKafkaApi* | [**get_log_kafka**](docs/LoggingKafkaApi.md#get_log_kafka) | **GET** /service/{service_id}/version/{version_id}/logging/kafka/{logging_kafka_name} | Get a Kafka log endpoint
*LoggingKafkaApi* | [**list_log_kafka**](docs/LoggingKafkaApi.md#list_log_kafka) | **GET** /service/{service_id}/version/{version_id}/logging/kafka | List Kafka log endpoints
*LoggingKafkaApi* | [**update_log_kafka**](docs/LoggingKafkaApi.md#update_log_kafka) | **PUT** /service/{service_id}/version/{version_id}/logging/kafka/{logging_kafka_name} | Update the Kafka log endpoint
*LoggingKinesisApi* | [**create_log_kinesis**](docs/LoggingKinesisApi.md#create_log_kinesis) | **POST** /service/{service_id}/version/{version_id}/logging/kinesis | Create  an Amazon Kinesis log endpoint
*LoggingKinesisApi* | [**delete_log_kinesis**](docs/LoggingKinesisApi.md#delete_log_kinesis) | **DELETE** /service/{service_id}/version/{version_id}/logging/kinesis/{logging_kinesis_name} | Delete the Amazon Kinesis log endpoint
*LoggingKinesisApi* | [**get_log_kinesis**](docs/LoggingKinesisApi.md#get_log_kinesis) | **GET** /service/{service_id}/version/{version_id}/logging/kinesis/{logging_kinesis_name} | Get an Amazon Kinesis log endpoint
*LoggingKinesisApi* | [**list_log_kinesis**](docs/LoggingKinesisApi.md#list_log_kinesis) | **GET** /service/{service_id}/version/{version_id}/logging/kinesis | List Amazon Kinesis log endpoints
*LoggingKinesisApi* | [**update_log_kinesis**](docs/LoggingKinesisApi.md#update_log_kinesis) | **PUT** /service/{service_id}/version/{version_id}/logging/kinesis/{logging_kinesis_name} | Update the Amazon Kinesis log endpoint
*LoggingLogentriesApi* | [**create_log_logentries**](docs/LoggingLogentriesApi.md#create_log_logentries) | **POST** /service/{service_id}/version/{version_id}/logging/logentries | Create a Logentries log endpoint
*LoggingLogentriesApi* | [**delete_log_logentries**](docs/LoggingLogentriesApi.md#delete_log_logentries) | **DELETE** /service/{service_id}/version/{version_id}/logging/logentries/{logging_logentries_name} | Delete a Logentries log endpoint
*LoggingLogentriesApi* | [**get_log_logentries**](docs/LoggingLogentriesApi.md#get_log_logentries) | **GET** /service/{service_id}/version/{version_id}/logging/logentries/{logging_logentries_name} | Get a Logentries log endpoint
*LoggingLogentriesApi* | [**list_log_logentries**](docs/LoggingLogentriesApi.md#list_log_logentries) | **GET** /service/{service_id}/version/{version_id}/logging/logentries | List Logentries log endpoints
*LoggingLogentriesApi* | [**update_log_logentries**](docs/LoggingLogentriesApi.md#update_log_logentries) | **PUT** /service/{service_id}/version/{version_id}/logging/logentries/{logging_logentries_name} | Update a Logentries log endpoint
*LoggingLogglyApi* | [**create_log_loggly**](docs/LoggingLogglyApi.md#create_log_loggly) | **POST** /service/{service_id}/version/{version_id}/logging/loggly | Create a Loggly log endpoint
*LoggingLogglyApi* | [**delete_log_loggly**](docs/LoggingLogglyApi.md#delete_log_loggly) | **DELETE** /service/{service_id}/version/{version_id}/logging/loggly/{logging_loggly_name} | Delete a Loggly log endpoint
*LoggingLogglyApi* | [**get_log_loggly**](docs/LoggingLogglyApi.md#get_log_loggly) | **GET** /service/{service_id}/version/{version_id}/logging/loggly/{logging_loggly_name} | Get a Loggly log endpoint
*LoggingLogglyApi* | [**list_log_loggly**](docs/LoggingLogglyApi.md#list_log_loggly) | **GET** /service/{service_id}/version/{version_id}/logging/loggly | List Loggly log endpoints
*LoggingLogglyApi* | [**update_log_loggly**](docs/LoggingLogglyApi.md#update_log_loggly) | **PUT** /service/{service_id}/version/{version_id}/logging/loggly/{logging_loggly_name} | Update a Loggly log endpoint
*LoggingLogshuttleApi* | [**create_log_logshuttle**](docs/LoggingLogshuttleApi.md#create_log_logshuttle) | **POST** /service/{service_id}/version/{version_id}/logging/logshuttle | Create a Log Shuttle log endpoint
*LoggingLogshuttleApi* | [**delete_log_logshuttle**](docs/LoggingLogshuttleApi.md#delete_log_logshuttle) | **DELETE** /service/{service_id}/version/{version_id}/logging/logshuttle/{logging_logshuttle_name} | Delete a Log Shuttle log endpoint
*LoggingLogshuttleApi* | [**get_log_logshuttle**](docs/LoggingLogshuttleApi.md#get_log_logshuttle) | **GET** /service/{service_id}/version/{version_id}/logging/logshuttle/{logging_logshuttle_name} | Get a Log Shuttle log endpoint
*LoggingLogshuttleApi* | [**list_log_logshuttle**](docs/LoggingLogshuttleApi.md#list_log_logshuttle) | **GET** /service/{service_id}/version/{version_id}/logging/logshuttle | List Log Shuttle log endpoints
*LoggingLogshuttleApi* | [**update_log_logshuttle**](docs/LoggingLogshuttleApi.md#update_log_logshuttle) | **PUT** /service/{service_id}/version/{version_id}/logging/logshuttle/{logging_logshuttle_name} | Update a Log Shuttle log endpoint
*LoggingNewrelicApi* | [**create_log_newrelic**](docs/LoggingNewrelicApi.md#create_log_newrelic) | **POST** /service/{service_id}/version/{version_id}/logging/newrelic | Create a New Relic log endpoint
*LoggingNewrelicApi* | [**delete_log_newrelic**](docs/LoggingNewrelicApi.md#delete_log_newrelic) | **DELETE** /service/{service_id}/version/{version_id}/logging/newrelic/{logging_newrelic_name} | Delete a New Relic log endpoint
*LoggingNewrelicApi* | [**get_log_newrelic**](docs/LoggingNewrelicApi.md#get_log_newrelic) | **GET** /service/{service_id}/version/{version_id}/logging/newrelic/{logging_newrelic_name} | Get a New Relic log endpoint
*LoggingNewrelicApi* | [**list_log_newrelic**](docs/LoggingNewrelicApi.md#list_log_newrelic) | **GET** /service/{service_id}/version/{version_id}/logging/newrelic | List New Relic log endpoints
*LoggingNewrelicApi* | [**update_log_newrelic**](docs/LoggingNewrelicApi.md#update_log_newrelic) | **PUT** /service/{service_id}/version/{version_id}/logging/newrelic/{logging_newrelic_name} | Update a New Relic log endpoint
*LoggingNewrelicotlpApi* | [**create_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#create_log_newrelicotlp) | **POST** /service/{service_id}/version/{version_id}/logging/newrelicotlp | Create a New Relic OTLP endpoint
*LoggingNewrelicotlpApi* | [**delete_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#delete_log_newrelicotlp) | **DELETE** /service/{service_id}/version/{version_id}/logging/newrelicotlp/{logging_newrelicotlp_name} | Delete a New Relic OTLP endpoint
*LoggingNewrelicotlpApi* | [**get_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#get_log_newrelicotlp) | **GET** /service/{service_id}/version/{version_id}/logging/newrelicotlp/{logging_newrelicotlp_name} | Get a New Relic OTLP endpoint
*LoggingNewrelicotlpApi* | [**list_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#list_log_newrelicotlp) | **GET** /service/{service_id}/version/{version_id}/logging/newrelicotlp | List New Relic OTLP endpoints
*LoggingNewrelicotlpApi* | [**update_log_newrelicotlp**](docs/LoggingNewrelicotlpApi.md#update_log_newrelicotlp) | **PUT** /service/{service_id}/version/{version_id}/logging/newrelicotlp/{logging_newrelicotlp_name} | Update a New Relic log endpoint
*LoggingOpenstackApi* | [**create_log_openstack**](docs/LoggingOpenstackApi.md#create_log_openstack) | **POST** /service/{service_id}/version/{version_id}/logging/openstack | Create an OpenStack log endpoint
*LoggingOpenstackApi* | [**delete_log_openstack**](docs/LoggingOpenstackApi.md#delete_log_openstack) | **DELETE** /service/{service_id}/version/{version_id}/logging/openstack/{logging_openstack_name} | Delete an OpenStack log endpoint
*LoggingOpenstackApi* | [**get_log_openstack**](docs/LoggingOpenstackApi.md#get_log_openstack) | **GET** /service/{service_id}/version/{version_id}/logging/openstack/{logging_openstack_name} | Get an OpenStack log endpoint
*LoggingOpenstackApi* | [**list_log_openstack**](docs/LoggingOpenstackApi.md#list_log_openstack) | **GET** /service/{service_id}/version/{version_id}/logging/openstack | List OpenStack log endpoints
*LoggingOpenstackApi* | [**update_log_openstack**](docs/LoggingOpenstackApi.md#update_log_openstack) | **PUT** /service/{service_id}/version/{version_id}/logging/openstack/{logging_openstack_name} | Update an OpenStack log endpoint
*LoggingPapertrailApi* | [**create_log_papertrail**](docs/LoggingPapertrailApi.md#create_log_papertrail) | **POST** /service/{service_id}/version/{version_id}/logging/papertrail | Create a Papertrail log endpoint
*LoggingPapertrailApi* | [**delete_log_papertrail**](docs/LoggingPapertrailApi.md#delete_log_papertrail) | **DELETE** /service/{service_id}/version/{version_id}/logging/papertrail/{logging_papertrail_name} | Delete a Papertrail log endpoint
*LoggingPapertrailApi* | [**get_log_papertrail**](docs/LoggingPapertrailApi.md#get_log_papertrail) | **GET** /service/{service_id}/version/{version_id}/logging/papertrail/{logging_papertrail_name} | Get a Papertrail log endpoint
*LoggingPapertrailApi* | [**list_log_papertrail**](docs/LoggingPapertrailApi.md#list_log_papertrail) | **GET** /service/{service_id}/version/{version_id}/logging/papertrail | List Papertrail log endpoints
*LoggingPapertrailApi* | [**update_log_papertrail**](docs/LoggingPapertrailApi.md#update_log_papertrail) | **PUT** /service/{service_id}/version/{version_id}/logging/papertrail/{logging_papertrail_name} | Update a Papertrail log endpoint
*LoggingPubsubApi* | [**create_log_gcp_pubsub**](docs/LoggingPubsubApi.md#create_log_gcp_pubsub) | **POST** /service/{service_id}/version/{version_id}/logging/pubsub | Create a GCP Cloud Pub/Sub log endpoint
*LoggingPubsubApi* | [**delete_log_gcp_pubsub**](docs/LoggingPubsubApi.md#delete_log_gcp_pubsub) | **DELETE** /service/{service_id}/version/{version_id}/logging/pubsub/{logging_google_pubsub_name} | Delete a GCP Cloud Pub/Sub log endpoint
*LoggingPubsubApi* | [**get_log_gcp_pubsub**](docs/LoggingPubsubApi.md#get_log_gcp_pubsub) | **GET** /service/{service_id}/version/{version_id}/logging/pubsub/{logging_google_pubsub_name} | Get a GCP Cloud Pub/Sub log endpoint
*LoggingPubsubApi* | [**list_log_gcp_pubsub**](docs/LoggingPubsubApi.md#list_log_gcp_pubsub) | **GET** /service/{service_id}/version/{version_id}/logging/pubsub | List GCP Cloud Pub/Sub log endpoints
*LoggingPubsubApi* | [**update_log_gcp_pubsub**](docs/LoggingPubsubApi.md#update_log_gcp_pubsub) | **PUT** /service/{service_id}/version/{version_id}/logging/pubsub/{logging_google_pubsub_name} | Update a GCP Cloud Pub/Sub log endpoint
*LoggingS3Api* | [**create_log_aws_s3**](docs/LoggingS3Api.md#create_log_aws_s3) | **POST** /service/{service_id}/version/{version_id}/logging/s3 | Create an AWS S3 log endpoint
*LoggingS3Api* | [**delete_log_aws_s3**](docs/LoggingS3Api.md#delete_log_aws_s3) | **DELETE** /service/{service_id}/version/{version_id}/logging/s3/{logging_s3_name} | Delete an AWS S3 log endpoint
*LoggingS3Api* | [**get_log_aws_s3**](docs/LoggingS3Api.md#get_log_aws_s3) | **GET** /service/{service_id}/version/{version_id}/logging/s3/{logging_s3_name} | Get an AWS S3 log endpoint
*LoggingS3Api* | [**list_log_aws_s3**](docs/LoggingS3Api.md#list_log_aws_s3) | **GET** /service/{service_id}/version/{version_id}/logging/s3 | List AWS S3 log endpoints
*LoggingS3Api* | [**update_log_aws_s3**](docs/LoggingS3Api.md#update_log_aws_s3) | **PUT** /service/{service_id}/version/{version_id}/logging/s3/{logging_s3_name} | Update an AWS S3 log endpoint
*LoggingScalyrApi* | [**create_log_scalyr**](docs/LoggingScalyrApi.md#create_log_scalyr) | **POST** /service/{service_id}/version/{version_id}/logging/scalyr | Create a Scalyr log endpoint
*LoggingScalyrApi* | [**delete_log_scalyr**](docs/LoggingScalyrApi.md#delete_log_scalyr) | **DELETE** /service/{service_id}/version/{version_id}/logging/scalyr/{logging_scalyr_name} | Delete the Scalyr log endpoint
*LoggingScalyrApi* | [**get_log_scalyr**](docs/LoggingScalyrApi.md#get_log_scalyr) | **GET** /service/{service_id}/version/{version_id}/logging/scalyr/{logging_scalyr_name} | Get a Scalyr log endpoint
*LoggingScalyrApi* | [**list_log_scalyr**](docs/LoggingScalyrApi.md#list_log_scalyr) | **GET** /service/{service_id}/version/{version_id}/logging/scalyr | List Scalyr log endpoints
*LoggingScalyrApi* | [**update_log_scalyr**](docs/LoggingScalyrApi.md#update_log_scalyr) | **PUT** /service/{service_id}/version/{version_id}/logging/scalyr/{logging_scalyr_name} | Update the Scalyr log endpoint
*LoggingSftpApi* | [**create_log_sftp**](docs/LoggingSftpApi.md#create_log_sftp) | **POST** /service/{service_id}/version/{version_id}/logging/sftp | Create an SFTP log endpoint
*LoggingSftpApi* | [**delete_log_sftp**](docs/LoggingSftpApi.md#delete_log_sftp) | **DELETE** /service/{service_id}/version/{version_id}/logging/sftp/{logging_sftp_name} | Delete an SFTP log endpoint
*LoggingSftpApi* | [**get_log_sftp**](docs/LoggingSftpApi.md#get_log_sftp) | **GET** /service/{service_id}/version/{version_id}/logging/sftp/{logging_sftp_name} | Get an SFTP log endpoint
*LoggingSftpApi* | [**list_log_sftp**](docs/LoggingSftpApi.md#list_log_sftp) | **GET** /service/{service_id}/version/{version_id}/logging/sftp | List SFTP log endpoints
*LoggingSftpApi* | [**update_log_sftp**](docs/LoggingSftpApi.md#update_log_sftp) | **PUT** /service/{service_id}/version/{version_id}/logging/sftp/{logging_sftp_name} | Update an SFTP log endpoint
*LoggingSplunkApi* | [**create_log_splunk**](docs/LoggingSplunkApi.md#create_log_splunk) | **POST** /service/{service_id}/version/{version_id}/logging/splunk | Create a Splunk log endpoint
*LoggingSplunkApi* | [**delete_log_splunk**](docs/LoggingSplunkApi.md#delete_log_splunk) | **DELETE** /service/{service_id}/version/{version_id}/logging/splunk/{logging_splunk_name} | Delete a Splunk log endpoint
*LoggingSplunkApi* | [**get_log_splunk**](docs/LoggingSplunkApi.md#get_log_splunk) | **GET** /service/{service_id}/version/{version_id}/logging/splunk/{logging_splunk_name} | Get a Splunk log endpoint
*LoggingSplunkApi* | [**list_log_splunk**](docs/LoggingSplunkApi.md#list_log_splunk) | **GET** /service/{service_id}/version/{version_id}/logging/splunk | List Splunk log endpoints
*LoggingSplunkApi* | [**update_log_splunk**](docs/LoggingSplunkApi.md#update_log_splunk) | **PUT** /service/{service_id}/version/{version_id}/logging/splunk/{logging_splunk_name} | Update a Splunk log endpoint
*LoggingSumologicApi* | [**create_log_sumologic**](docs/LoggingSumologicApi.md#create_log_sumologic) | **POST** /service/{service_id}/version/{version_id}/logging/sumologic | Create a Sumologic log endpoint
*LoggingSumologicApi* | [**delete_log_sumologic**](docs/LoggingSumologicApi.md#delete_log_sumologic) | **DELETE** /service/{service_id}/version/{version_id}/logging/sumologic/{logging_sumologic_name} | Delete a Sumologic log endpoint
*LoggingSumologicApi* | [**get_log_sumologic**](docs/LoggingSumologicApi.md#get_log_sumologic) | **GET** /service/{service_id}/version/{version_id}/logging/sumologic/{logging_sumologic_name} | Get a Sumologic log endpoint
*LoggingSumologicApi* | [**list_log_sumologic**](docs/LoggingSumologicApi.md#list_log_sumologic) | **GET** /service/{service_id}/version/{version_id}/logging/sumologic | List Sumologic log endpoints
*LoggingSumologicApi* | [**update_log_sumologic**](docs/LoggingSumologicApi.md#update_log_sumologic) | **PUT** /service/{service_id}/version/{version_id}/logging/sumologic/{logging_sumologic_name} | Update a Sumologic log endpoint
*LoggingSyslogApi* | [**create_log_syslog**](docs/LoggingSyslogApi.md#create_log_syslog) | **POST** /service/{service_id}/version/{version_id}/logging/syslog | Create a syslog log endpoint
*LoggingSyslogApi* | [**delete_log_syslog**](docs/LoggingSyslogApi.md#delete_log_syslog) | **DELETE** /service/{service_id}/version/{version_id}/logging/syslog/{logging_syslog_name} | Delete a syslog log endpoint
*LoggingSyslogApi* | [**get_log_syslog**](docs/LoggingSyslogApi.md#get_log_syslog) | **GET** /service/{service_id}/version/{version_id}/logging/syslog/{logging_syslog_name} | Get a syslog log endpoint
*LoggingSyslogApi* | [**list_log_syslog**](docs/LoggingSyslogApi.md#list_log_syslog) | **GET** /service/{service_id}/version/{version_id}/logging/syslog | List Syslog log endpoints
*LoggingSyslogApi* | [**update_log_syslog**](docs/LoggingSyslogApi.md#update_log_syslog) | **PUT** /service/{service_id}/version/{version_id}/logging/syslog/{logging_syslog_name} | Update a syslog log endpoint
*MutualAuthenticationApi* | [**create_mutual_tls_authentication**](docs/MutualAuthenticationApi.md#create_mutual_tls_authentication) | **POST** /tls/mutual_authentications | Create a Mutual Authentication
*MutualAuthenticationApi* | [**delete_mutual_tls**](docs/MutualAuthenticationApi.md#delete_mutual_tls) | **DELETE** /tls/mutual_authentications/{mutual_authentication_id} | Delete a Mutual TLS
*MutualAuthenticationApi* | [**get_mutual_authentication**](docs/MutualAuthenticationApi.md#get_mutual_authentication) | **GET** /tls/mutual_authentications/{mutual_authentication_id} | Get a Mutual Authentication
*MutualAuthenticationApi* | [**list_mutual_authentications**](docs/MutualAuthenticationApi.md#list_mutual_authentications) | **GET** /tls/mutual_authentications | List Mutual Authentications
*MutualAuthenticationApi* | [**patch_mutual_authentication**](docs/MutualAuthenticationApi.md#patch_mutual_authentication) | **PATCH** /tls/mutual_authentications/{mutual_authentication_id} | Update a Mutual Authentication
*OriginInspectorHistoricalApi* | [**get_origin_inspector_historical**](docs/OriginInspectorHistoricalApi.md#get_origin_inspector_historical) | **GET** /metrics/origins/services/{service_id} | Get historical origin data for a service
*OriginInspectorRealtimeApi* | [**get_origin_inspector_last120_seconds**](docs/OriginInspectorRealtimeApi.md#get_origin_inspector_last120_seconds) | **GET** /v1/origins/{service_id}/ts/h | Get real-time origin data for the last 120 seconds
*OriginInspectorRealtimeApi* | [**get_origin_inspector_last_max_entries**](docs/OriginInspectorRealtimeApi.md#get_origin_inspector_last_max_entries) | **GET** /v1/origins/{service_id}/ts/h/limit/{max_entries} | Get a limited number of real-time origin data entries
*OriginInspectorRealtimeApi* | [**get_origin_inspector_last_second**](docs/OriginInspectorRealtimeApi.md#get_origin_inspector_last_second) | **GET** /v1/origins/{service_id}/ts/{start_timestamp} | Get real-time origin data from specific time.
*PackageApi* | [**get_package**](docs/PackageApi.md#get_package) | **GET** /service/{service_id}/version/{version_id}/package | Get details of the service&#39;s Compute package.
*PackageApi* | [**put_package**](docs/PackageApi.md#put_package) | **PUT** /service/{service_id}/version/{version_id}/package | Upload a Compute package.
*PoolApi* | [**create_server_pool**](docs/PoolApi.md#create_server_pool) | **POST** /service/{service_id}/version/{version_id}/pool | Create a server pool
*PoolApi* | [**delete_server_pool**](docs/PoolApi.md#delete_server_pool) | **DELETE** /service/{service_id}/version/{version_id}/pool/{pool_name} | Delete a server pool
*PoolApi* | [**get_server_pool**](docs/PoolApi.md#get_server_pool) | **GET** /service/{service_id}/version/{version_id}/pool/{pool_name} | Get a server pool
*PoolApi* | [**list_server_pools**](docs/PoolApi.md#list_server_pools) | **GET** /service/{service_id}/version/{version_id}/pool | List server pools
*PoolApi* | [**update_server_pool**](docs/PoolApi.md#update_server_pool) | **PUT** /service/{service_id}/version/{version_id}/pool/{pool_name} | Update a server pool
*PopApi* | [**list_pops**](docs/PopApi.md#list_pops) | **GET** /datacenters | List Fastly POPs
*PublicIpListApi* | [**list_fastly_ips**](docs/PublicIpListApi.md#list_fastly_ips) | **GET** /public-ip-list | List Fastly&#39;s public IPs
*PublishApi* | [**publish**](docs/PublishApi.md#publish) | **POST** /service/{service_id}/publish/ | Send messages to Fanout subscribers
*PurgeApi* | [**bulk_purge_tag**](docs/PurgeApi.md#bulk_purge_tag) | **POST** /service/{service_id}/purge | Purge multiple surrogate key tags
*PurgeApi* | [**purge_all**](docs/PurgeApi.md#purge_all) | **POST** /service/{service_id}/purge_all | Purge everything from a service
*PurgeApi* | [**purge_single_url**](docs/PurgeApi.md#purge_single_url) | **POST** /purge/{cached_url} | Purge a URL
*PurgeApi* | [**purge_tag**](docs/PurgeApi.md#purge_tag) | **POST** /service/{service_id}/purge/{surrogate_key} | Purge by surrogate key tag
*RateLimiterApi* | [**create_rate_limiter**](docs/RateLimiterApi.md#create_rate_limiter) | **POST** /service/{service_id}/version/{version_id}/rate-limiters | Create a rate limiter
*RateLimiterApi* | [**delete_rate_limiter**](docs/RateLimiterApi.md#delete_rate_limiter) | **DELETE** /rate-limiters/{rate_limiter_id} | Delete a rate limiter
*RateLimiterApi* | [**get_rate_limiter**](docs/RateLimiterApi.md#get_rate_limiter) | **GET** /rate-limiters/{rate_limiter_id} | Get a rate limiter
*RateLimiterApi* | [**list_rate_limiters**](docs/RateLimiterApi.md#list_rate_limiters) | **GET** /service/{service_id}/version/{version_id}/rate-limiters | List rate limiters
*RateLimiterApi* | [**update_rate_limiter**](docs/RateLimiterApi.md#update_rate_limiter) | **PUT** /rate-limiters/{rate_limiter_id} | Update a rate limiter
*RealtimeApi* | [**get_stats_last120_seconds**](docs/RealtimeApi.md#get_stats_last120_seconds) | **GET** /v1/channel/{service_id}/ts/h | Get real-time data for the last 120 seconds
*RealtimeApi* | [**get_stats_last120_seconds_limit_entries**](docs/RealtimeApi.md#get_stats_last120_seconds_limit_entries) | **GET** /v1/channel/{service_id}/ts/h/limit/{max_entries} | Get a limited number of real-time data entries
*RealtimeApi* | [**get_stats_last_second**](docs/RealtimeApi.md#get_stats_last_second) | **GET** /v1/channel/{service_id}/ts/{timestamp_in_seconds} | Get real-time data from specified time
*RequestSettingsApi* | [**create_request_settings**](docs/RequestSettingsApi.md#create_request_settings) | **POST** /service/{service_id}/version/{version_id}/request_settings | Create a Request Settings object
*RequestSettingsApi* | [**delete_request_settings**](docs/RequestSettingsApi.md#delete_request_settings) | **DELETE** /service/{service_id}/version/{version_id}/request_settings/{request_settings_name} | Delete a Request Settings object
*RequestSettingsApi* | [**get_request_settings**](docs/RequestSettingsApi.md#get_request_settings) | **GET** /service/{service_id}/version/{version_id}/request_settings/{request_settings_name} | Get a Request Settings object
*RequestSettingsApi* | [**list_request_settings**](docs/RequestSettingsApi.md#list_request_settings) | **GET** /service/{service_id}/version/{version_id}/request_settings | List Request Settings objects
*RequestSettingsApi* | [**update_request_settings**](docs/RequestSettingsApi.md#update_request_settings) | **PUT** /service/{service_id}/version/{version_id}/request_settings/{request_settings_name} | Update a Request Settings object
*ResourceApi* | [**create_resource**](docs/ResourceApi.md#create_resource) | **POST** /service/{service_id}/version/{version_id}/resource | Create a resource link
*ResourceApi* | [**delete_resource**](docs/ResourceApi.md#delete_resource) | **DELETE** /service/{service_id}/version/{version_id}/resource/{id} | Delete a resource link
*ResourceApi* | [**get_resource**](docs/ResourceApi.md#get_resource) | **GET** /service/{service_id}/version/{version_id}/resource/{id} | Display a resource link
*ResourceApi* | [**list_resources**](docs/ResourceApi.md#list_resources) | **GET** /service/{service_id}/version/{version_id}/resource | List resource links
*ResourceApi* | [**update_resource**](docs/ResourceApi.md#update_resource) | **PUT** /service/{service_id}/version/{version_id}/resource/{id} | Update a resource link
*ResponseObjectApi* | [**create_response_object**](docs/ResponseObjectApi.md#create_response_object) | **POST** /service/{service_id}/version/{version_id}/response_object | Create a Response object
*ResponseObjectApi* | [**delete_response_object**](docs/ResponseObjectApi.md#delete_response_object) | **DELETE** /service/{service_id}/version/{version_id}/response_object/{response_object_name} | Delete a Response Object
*ResponseObjectApi* | [**get_response_object**](docs/ResponseObjectApi.md#get_response_object) | **GET** /service/{service_id}/version/{version_id}/response_object/{response_object_name} | Get a Response object
*ResponseObjectApi* | [**list_response_objects**](docs/ResponseObjectApi.md#list_response_objects) | **GET** /service/{service_id}/version/{version_id}/response_object | List Response objects
*ResponseObjectApi* | [**update_response_object**](docs/ResponseObjectApi.md#update_response_object) | **PUT** /service/{service_id}/version/{version_id}/response_object/{response_object_name} | Update a Response object
*SecretStoreApi* | [**client_key**](docs/SecretStoreApi.md#client_key) | **POST** /resources/stores/secret/client-key | Create new client key
*SecretStoreApi* | [**create_secret_store**](docs/SecretStoreApi.md#create_secret_store) | **POST** /resources/stores/secret | Create new secret store
*SecretStoreApi* | [**delete_secret_store**](docs/SecretStoreApi.md#delete_secret_store) | **DELETE** /resources/stores/secret/{store_id} | Delete secret store
*SecretStoreApi* | [**get_secret_store**](docs/SecretStoreApi.md#get_secret_store) | **GET** /resources/stores/secret/{store_id} | Get secret store by ID
*SecretStoreApi* | [**get_secret_stores**](docs/SecretStoreApi.md#get_secret_stores) | **GET** /resources/stores/secret | Get all secret stores
*SecretStoreApi* | [**signing_key**](docs/SecretStoreApi.md#signing_key) | **GET** /resources/stores/secret/signing-key | Get public key
*SecretStoreItemApi* | [**create_secret**](docs/SecretStoreItemApi.md#create_secret) | **POST** /resources/stores/secret/{store_id}/secrets | Create a new secret in a store.
*SecretStoreItemApi* | [**delete_secret**](docs/SecretStoreItemApi.md#delete_secret) | **DELETE** /resources/stores/secret/{store_id}/secrets/{secret_name} | Delete a secret from a store.
*SecretStoreItemApi* | [**get_secret**](docs/SecretStoreItemApi.md#get_secret) | **GET** /resources/stores/secret/{store_id}/secrets/{secret_name} | Get secret metadata.
*SecretStoreItemApi* | [**get_secrets**](docs/SecretStoreItemApi.md#get_secrets) | **GET** /resources/stores/secret/{store_id}/secrets | List secrets within a store.
*SecretStoreItemApi* | [**must_recreate_secret**](docs/SecretStoreItemApi.md#must_recreate_secret) | **PATCH** /resources/stores/secret/{store_id}/secrets | Recreate a secret in a store.
*SecretStoreItemApi* | [**recreate_secret**](docs/SecretStoreItemApi.md#recreate_secret) | **PUT** /resources/stores/secret/{store_id}/secrets | Create or recreate a secret in a store.
*ServerApi* | [**create_pool_server**](docs/ServerApi.md#create_pool_server) | **POST** /service/{service_id}/pool/{pool_id}/server | Add a server to a pool
*ServerApi* | [**delete_pool_server**](docs/ServerApi.md#delete_pool_server) | **DELETE** /service/{service_id}/pool/{pool_id}/server/{server_id} | Delete a server from a pool
*ServerApi* | [**get_pool_server**](docs/ServerApi.md#get_pool_server) | **GET** /service/{service_id}/pool/{pool_id}/server/{server_id} | Get a pool server
*ServerApi* | [**list_pool_servers**](docs/ServerApi.md#list_pool_servers) | **GET** /service/{service_id}/pool/{pool_id}/servers | List servers in a pool
*ServerApi* | [**update_pool_server**](docs/ServerApi.md#update_pool_server) | **PUT** /service/{service_id}/pool/{pool_id}/server/{server_id} | Update a server
*ServiceApi* | [**create_service**](docs/ServiceApi.md#create_service) | **POST** /service | Create a service
*ServiceApi* | [**delete_service**](docs/ServiceApi.md#delete_service) | **DELETE** /service/{service_id} | Delete a service
*ServiceApi* | [**get_service**](docs/ServiceApi.md#get_service) | **GET** /service/{service_id} | Get a service
*ServiceApi* | [**get_service_detail**](docs/ServiceApi.md#get_service_detail) | **GET** /service/{service_id}/details | Get service details
*ServiceApi* | [**list_service_domains**](docs/ServiceApi.md#list_service_domains) | **GET** /service/{service_id}/domain | List the domains within a service
*ServiceApi* | [**list_services**](docs/ServiceApi.md#list_services) | **GET** /service | List services
*ServiceApi* | [**search_service**](docs/ServiceApi.md#search_service) | **GET** /service/search | Search for a service by name
*ServiceApi* | [**update_service**](docs/ServiceApi.md#update_service) | **PUT** /service/{service_id} | Update a service
*ServiceAuthorizationsApi* | [**create_service_authorization**](docs/ServiceAuthorizationsApi.md#create_service_authorization) | **POST** /service-authorizations | Create service authorization
*ServiceAuthorizationsApi* | [**delete_service_authorization**](docs/ServiceAuthorizationsApi.md#delete_service_authorization) | **DELETE** /service-authorizations/{service_authorization_id} | Delete service authorization
*ServiceAuthorizationsApi* | [**delete_service_authorization2**](docs/ServiceAuthorizationsApi.md#delete_service_authorization2) | **DELETE** /service-authorizations | Delete service authorizations
*ServiceAuthorizationsApi* | [**list_service_authorization**](docs/ServiceAuthorizationsApi.md#list_service_authorization) | **GET** /service-authorizations | List service authorizations
*ServiceAuthorizationsApi* | [**show_service_authorization**](docs/ServiceAuthorizationsApi.md#show_service_authorization) | **GET** /service-authorizations/{service_authorization_id} | Show service authorization
*ServiceAuthorizationsApi* | [**update_service_authorization**](docs/ServiceAuthorizationsApi.md#update_service_authorization) | **PATCH** /service-authorizations/{service_authorization_id} | Update service authorization
*ServiceAuthorizationsApi* | [**update_service_authorization2**](docs/ServiceAuthorizationsApi.md#update_service_authorization2) | **PATCH** /service-authorizations | Update service authorizations
*SettingsApi* | [**get_service_settings**](docs/SettingsApi.md#get_service_settings) | **GET** /service/{service_id}/version/{version_id}/settings | Get service settings
*SettingsApi* | [**update_service_settings**](docs/SettingsApi.md#update_service_settings) | **PUT** /service/{service_id}/version/{version_id}/settings | Update service settings
*SnippetApi* | [**create_snippet**](docs/SnippetApi.md#create_snippet) | **POST** /service/{service_id}/version/{version_id}/snippet | Create a snippet
*SnippetApi* | [**delete_snippet**](docs/SnippetApi.md#delete_snippet) | **DELETE** /service/{service_id}/version/{version_id}/snippet/{snippet_name} | Delete a snippet
*SnippetApi* | [**get_snippet**](docs/SnippetApi.md#get_snippet) | **GET** /service/{service_id}/version/{version_id}/snippet/{snippet_name} | Get a versioned snippet
*SnippetApi* | [**get_snippet_dynamic**](docs/SnippetApi.md#get_snippet_dynamic) | **GET** /service/{service_id}/snippet/{snippet_id} | Get a dynamic snippet
*SnippetApi* | [**list_snippets**](docs/SnippetApi.md#list_snippets) | **GET** /service/{service_id}/version/{version_id}/snippet | List snippets
*SnippetApi* | [**update_snippet**](docs/SnippetApi.md#update_snippet) | **PUT** /service/{service_id}/version/{version_id}/snippet/{snippet_name} | Update a versioned snippet
*SnippetApi* | [**update_snippet_dynamic**](docs/SnippetApi.md#update_snippet_dynamic) | **PUT** /service/{service_id}/snippet/{snippet_id} | Update a dynamic snippet
*StarApi* | [**create_service_star**](docs/StarApi.md#create_service_star) | **POST** /stars | Create a star
*StarApi* | [**delete_service_star**](docs/StarApi.md#delete_service_star) | **DELETE** /stars/{star_id} | Delete a star
*StarApi* | [**get_service_star**](docs/StarApi.md#get_service_star) | **GET** /stars/{star_id} | Get a star
*StarApi* | [**list_service_stars**](docs/StarApi.md#list_service_stars) | **GET** /stars | List stars
*StatsApi* | [**get_service_stats**](docs/StatsApi.md#get_service_stats) | **GET** /service/{service_id}/stats/summary | Get stats for a service
*SudoApi* | [**request_sudo_access**](docs/SudoApi.md#request_sudo_access) | **POST** /sudo | Request Sudo access
*TlsActivationsApi* | [**create_tls_activation**](docs/TlsActivationsApi.md#create_tls_activation) | **POST** /tls/activations | Enable TLS for a domain using a custom certificate
*TlsActivationsApi* | [**delete_tls_activation**](docs/TlsActivationsApi.md#delete_tls_activation) | **DELETE** /tls/activations/{tls_activation_id} | Disable TLS on a domain
*TlsActivationsApi* | [**get_tls_activation**](docs/TlsActivationsApi.md#get_tls_activation) | **GET** /tls/activations/{tls_activation_id} | Get a TLS activation
*TlsActivationsApi* | [**list_tls_activations**](docs/TlsActivationsApi.md#list_tls_activations) | **GET** /tls/activations | List TLS activations
*TlsActivationsApi* | [**update_tls_activation**](docs/TlsActivationsApi.md#update_tls_activation) | **PATCH** /tls/activations/{tls_activation_id} | Update a certificate
*TlsBulkCertificatesApi* | [**delete_bulk_tls_cert**](docs/TlsBulkCertificatesApi.md#delete_bulk_tls_cert) | **DELETE** /tls/bulk/certificates/{certificate_id} | Delete a certificate
*TlsBulkCertificatesApi* | [**get_tls_bulk_cert**](docs/TlsBulkCertificatesApi.md#get_tls_bulk_cert) | **GET** /tls/bulk/certificates/{certificate_id} | Get a certificate
*TlsBulkCertificatesApi* | [**list_tls_bulk_certs**](docs/TlsBulkCertificatesApi.md#list_tls_bulk_certs) | **GET** /tls/bulk/certificates | List certificates
*TlsBulkCertificatesApi* | [**update_bulk_tls_cert**](docs/TlsBulkCertificatesApi.md#update_bulk_tls_cert) | **PATCH** /tls/bulk/certificates/{certificate_id} | Update a certificate
*TlsBulkCertificatesApi* | [**upload_tls_bulk_cert**](docs/TlsBulkCertificatesApi.md#upload_tls_bulk_cert) | **POST** /tls/bulk/certificates | Upload a certificate
*TlsCertificatesApi* | [**create_tls_cert**](docs/TlsCertificatesApi.md#create_tls_cert) | **POST** /tls/certificates | Create a TLS certificate
*TlsCertificatesApi* | [**delete_tls_cert**](docs/TlsCertificatesApi.md#delete_tls_cert) | **DELETE** /tls/certificates/{tls_certificate_id} | Delete a TLS certificate
*TlsCertificatesApi* | [**get_tls_cert**](docs/TlsCertificatesApi.md#get_tls_cert) | **GET** /tls/certificates/{tls_certificate_id} | Get a TLS certificate
*TlsCertificatesApi* | [**list_tls_certs**](docs/TlsCertificatesApi.md#list_tls_certs) | **GET** /tls/certificates | List TLS certificates
*TlsCertificatesApi* | [**update_tls_cert**](docs/TlsCertificatesApi.md#update_tls_cert) | **PATCH** /tls/certificates/{tls_certificate_id} | Update a TLS certificate
*TlsConfigurationsApi* | [**get_tls_config**](docs/TlsConfigurationsApi.md#get_tls_config) | **GET** /tls/configurations/{tls_configuration_id} | Get a TLS configuration
*TlsConfigurationsApi* | [**list_tls_configs**](docs/TlsConfigurationsApi.md#list_tls_configs) | **GET** /tls/configurations | List TLS configurations
*TlsConfigurationsApi* | [**update_tls_config**](docs/TlsConfigurationsApi.md#update_tls_config) | **PATCH** /tls/configurations/{tls_configuration_id} | Update a TLS configuration
*TlsDomainsApi* | [**list_tls_domains**](docs/TlsDomainsApi.md#list_tls_domains) | **GET** /tls/domains | List TLS domains
*TlsPrivateKeysApi* | [**create_tls_key**](docs/TlsPrivateKeysApi.md#create_tls_key) | **POST** /tls/private_keys | Create a TLS private key
*TlsPrivateKeysApi* | [**delete_tls_key**](docs/TlsPrivateKeysApi.md#delete_tls_key) | **DELETE** /tls/private_keys/{tls_private_key_id} | Delete a TLS private key
*TlsPrivateKeysApi* | [**get_tls_key**](docs/TlsPrivateKeysApi.md#get_tls_key) | **GET** /tls/private_keys/{tls_private_key_id} | Get a TLS private key
*TlsPrivateKeysApi* | [**list_tls_keys**](docs/TlsPrivateKeysApi.md#list_tls_keys) | **GET** /tls/private_keys | List TLS private keys
*TlsSubscriptionsApi* | [**create_globalsign_email_challenge**](docs/TlsSubscriptionsApi.md#create_globalsign_email_challenge) | **POST** /tls/subscriptions/{tls_subscription_id}/authorizations/{tls_authorization_id}/globalsign_email_challenges | Creates a GlobalSign email challenge.
*TlsSubscriptionsApi* | [**create_tls_sub**](docs/TlsSubscriptionsApi.md#create_tls_sub) | **POST** /tls/subscriptions | Create a TLS subscription
*TlsSubscriptionsApi* | [**delete_globalsign_email_challenge**](docs/TlsSubscriptionsApi.md#delete_globalsign_email_challenge) | **DELETE** /tls/subscriptions/{tls_subscription_id}/authorizations/{tls_authorization_id}/globalsign_email_challenges/{globalsign_email_challenge_id} | Delete a GlobalSign email challenge
*TlsSubscriptionsApi* | [**delete_tls_sub**](docs/TlsSubscriptionsApi.md#delete_tls_sub) | **DELETE** /tls/subscriptions/{tls_subscription_id} | Delete a TLS subscription
*TlsSubscriptionsApi* | [**get_tls_sub**](docs/TlsSubscriptionsApi.md#get_tls_sub) | **GET** /tls/subscriptions/{tls_subscription_id} | Get a TLS subscription
*TlsSubscriptionsApi* | [**list_tls_subs**](docs/TlsSubscriptionsApi.md#list_tls_subs) | **GET** /tls/subscriptions | List TLS subscriptions
*TlsSubscriptionsApi* | [**patch_tls_sub**](docs/TlsSubscriptionsApi.md#patch_tls_sub) | **PATCH** /tls/subscriptions/{tls_subscription_id} | Update a TLS subscription
*TokensApi* | [**bulk_revoke_tokens**](docs/TokensApi.md#bulk_revoke_tokens) | **DELETE** /tokens | Revoke multiple tokens
*TokensApi* | [**create_token**](docs/TokensApi.md#create_token) | **POST** /tokens | Create a token
*TokensApi* | [**get_token**](docs/TokensApi.md#get_token) | **GET** /tokens/{token_id} | Get a token
*TokensApi* | [**get_token_current**](docs/TokensApi.md#get_token_current) | **GET** /tokens/self | Get the current token
*TokensApi* | [**list_tokens_customer**](docs/TokensApi.md#list_tokens_customer) | **GET** /customer/{customer_id}/tokens | List tokens for a customer
*TokensApi* | [**list_tokens_user**](docs/TokensApi.md#list_tokens_user) | **GET** /tokens | List tokens for the authenticated user
*TokensApi* | [**revoke_token**](docs/TokensApi.md#revoke_token) | **DELETE** /tokens/{token_id} | Revoke a token
*TokensApi* | [**revoke_token_current**](docs/TokensApi.md#revoke_token_current) | **DELETE** /tokens/self | Revoke the current token
*UserApi* | [**create_user**](docs/UserApi.md#create_user) | **POST** /user | Create a user
*UserApi* | [**delete_user**](docs/UserApi.md#delete_user) | **DELETE** /user/{user_id} | Delete a user
*UserApi* | [**get_current_user**](docs/UserApi.md#get_current_user) | **GET** /current_user | Get the current user
*UserApi* | [**get_user**](docs/UserApi.md#get_user) | **GET** /user/{user_id} | Get a user
*UserApi* | [**request_password_reset**](docs/UserApi.md#request_password_reset) | **POST** /user/{user_login}/password/request_reset | Request a password reset
*UserApi* | [**update_user**](docs/UserApi.md#update_user) | **PUT** /user/{user_id} | Update a user
*UserApi* | [**update_user_password**](docs/UserApi.md#update_user_password) | **POST** /current_user/password | Update the user&#39;s password
*VclApi* | [**create_custom_vcl**](docs/VclApi.md#create_custom_vcl) | **POST** /service/{service_id}/version/{version_id}/vcl | Create a custom VCL file
*VclApi* | [**delete_custom_vcl**](docs/VclApi.md#delete_custom_vcl) | **DELETE** /service/{service_id}/version/{version_id}/vcl/{vcl_name} | Delete a custom VCL file
*VclApi* | [**get_custom_vcl**](docs/VclApi.md#get_custom_vcl) | **GET** /service/{service_id}/version/{version_id}/vcl/{vcl_name} | Get a custom VCL file
*VclApi* | [**get_custom_vcl_boilerplate**](docs/VclApi.md#get_custom_vcl_boilerplate) | **GET** /service/{service_id}/version/{version_id}/boilerplate | Get boilerplate VCL
*VclApi* | [**get_custom_vcl_generated**](docs/VclApi.md#get_custom_vcl_generated) | **GET** /service/{service_id}/version/{version_id}/generated_vcl | Get the generated VCL for a service
*VclApi* | [**get_custom_vcl_generated_highlighted**](docs/VclApi.md#get_custom_vcl_generated_highlighted) | **GET** /service/{service_id}/version/{version_id}/generated_vcl/content | Get the generated VCL with syntax highlighting
*VclApi* | [**get_custom_vcl_highlighted**](docs/VclApi.md#get_custom_vcl_highlighted) | **GET** /service/{service_id}/version/{version_id}/vcl/{vcl_name}/content | Get a custom VCL file with syntax highlighting
*VclApi* | [**get_custom_vcl_raw**](docs/VclApi.md#get_custom_vcl_raw) | **GET** /service/{service_id}/version/{version_id}/vcl/{vcl_name}/download | Download a custom VCL file
*VclApi* | [**lint_vcl_default**](docs/VclApi.md#lint_vcl_default) | **POST** /vcl_lint | Lint (validate) VCL using a default set of flags.
*VclApi* | [**lint_vcl_for_service**](docs/VclApi.md#lint_vcl_for_service) | **POST** /service/{service_id}/lint | Lint (validate) VCL using flags set for the service.
*VclApi* | [**list_custom_vcl**](docs/VclApi.md#list_custom_vcl) | **GET** /service/{service_id}/version/{version_id}/vcl | List custom VCL files
*VclApi* | [**set_custom_vcl_main**](docs/VclApi.md#set_custom_vcl_main) | **PUT** /service/{service_id}/version/{version_id}/vcl/{vcl_name}/main | Set a custom VCL file as main
*VclApi* | [**update_custom_vcl**](docs/VclApi.md#update_custom_vcl) | **PUT** /service/{service_id}/version/{version_id}/vcl/{vcl_name} | Update a custom VCL file
*VclDiffApi* | [**vcl_diff_service_versions**](docs/VclDiffApi.md#vcl_diff_service_versions) | **GET** /service/{service_id}/vcl/diff/from/{from_version_id}/to/{to_version_id} | Get a comparison of the VCL changes between two service versions
*VersionApi* | [**activate_service_version**](docs/VersionApi.md#activate_service_version) | **PUT** /service/{service_id}/version/{version_id}/activate | Activate a service version
*VersionApi* | [**clone_service_version**](docs/VersionApi.md#clone_service_version) | **PUT** /service/{service_id}/version/{version_id}/clone | Clone a service version
*VersionApi* | [**create_service_version**](docs/VersionApi.md#create_service_version) | **POST** /service/{service_id}/version | Create a service version
*VersionApi* | [**deactivate_service_version**](docs/VersionApi.md#deactivate_service_version) | **PUT** /service/{service_id}/version/{version_id}/deactivate | Deactivate a service version
*VersionApi* | [**get_service_version**](docs/VersionApi.md#get_service_version) | **GET** /service/{service_id}/version/{version_id} | Get a version of a service
*VersionApi* | [**list_service_versions**](docs/VersionApi.md#list_service_versions) | **GET** /service/{service_id}/version | List versions of a service
*VersionApi* | [**lock_service_version**](docs/VersionApi.md#lock_service_version) | **PUT** /service/{service_id}/version/{version_id}/lock | Lock a service version
*VersionApi* | [**update_service_version**](docs/VersionApi.md#update_service_version) | **PUT** /service/{service_id}/version/{version_id} | Update a service version
*VersionApi* | [**validate_service_version**](docs/VersionApi.md#validate_service_version) | **GET** /service/{service_id}/version/{version_id}/validate | Validate a service version
*WafActiveRulesApi* | [**bulk_delete_waf_active_rules**](docs/WafActiveRulesApi.md#bulk_delete_waf_active_rules) | **DELETE** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules | Delete multiple active rules from a WAF
*WafActiveRulesApi* | [**bulk_update_waf_active_rules**](docs/WafActiveRulesApi.md#bulk_update_waf_active_rules) | **PATCH** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/bulk | Update multiple active rules
*WafActiveRulesApi* | [**create_waf_active_rule**](docs/WafActiveRulesApi.md#create_waf_active_rule) | **POST** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules | Add a rule to a WAF as an active rule
*WafActiveRulesApi* | [**create_waf_active_rules_tag**](docs/WafActiveRulesApi.md#create_waf_active_rules_tag) | **POST** /waf/firewalls/{firewall_id}/versions/{version_id}/tags/{waf_tag_name}/active-rules | Create active rules by tag
*WafActiveRulesApi* | [**delete_waf_active_rule**](docs/WafActiveRulesApi.md#delete_waf_active_rule) | **DELETE** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id} | Delete an active rule
*WafActiveRulesApi* | [**get_waf_active_rule**](docs/WafActiveRulesApi.md#get_waf_active_rule) | **GET** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id} | Get an active WAF rule object
*WafActiveRulesApi* | [**list_waf_active_rules**](docs/WafActiveRulesApi.md#list_waf_active_rules) | **GET** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules | List active rules on a WAF
*WafActiveRulesApi* | [**update_waf_active_rule**](docs/WafActiveRulesApi.md#update_waf_active_rule) | **PATCH** /waf/firewalls/{firewall_id}/versions/{version_id}/active-rules/{waf_rule_id} | Update an active rule
*WafExclusionsApi* | [**create_waf_rule_exclusion**](docs/WafExclusionsApi.md#create_waf_rule_exclusion) | **POST** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions | Create a WAF rule exclusion
*WafExclusionsApi* | [**delete_waf_rule_exclusion**](docs/WafExclusionsApi.md#delete_waf_rule_exclusion) | **DELETE** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number} | Delete a WAF rule exclusion
*WafExclusionsApi* | [**get_waf_rule_exclusion**](docs/WafExclusionsApi.md#get_waf_rule_exclusion) | **GET** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number} | Get a WAF rule exclusion
*WafExclusionsApi* | [**list_waf_rule_exclusions**](docs/WafExclusionsApi.md#list_waf_rule_exclusions) | **GET** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions | List WAF rule exclusions
*WafExclusionsApi* | [**update_waf_rule_exclusion**](docs/WafExclusionsApi.md#update_waf_rule_exclusion) | **PATCH** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/exclusions/{exclusion_number} | Update a WAF rule exclusion
*WafFirewallVersionsApi* | [**clone_waf_firewall_version**](docs/WafFirewallVersionsApi.md#clone_waf_firewall_version) | **PUT** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/clone | Clone a firewall version
*WafFirewallVersionsApi* | [**create_waf_firewall_version**](docs/WafFirewallVersionsApi.md#create_waf_firewall_version) | **POST** /waf/firewalls/{firewall_id}/versions | Create a firewall version
*WafFirewallVersionsApi* | [**deploy_activate_waf_firewall_version**](docs/WafFirewallVersionsApi.md#deploy_activate_waf_firewall_version) | **PUT** /waf/firewalls/{firewall_id}/versions/{firewall_version_number}/activate | Deploy or activate a firewall version
*WafFirewallVersionsApi* | [**get_waf_firewall_version**](docs/WafFirewallVersionsApi.md#get_waf_firewall_version) | **GET** /waf/firewalls/{firewall_id}/versions/{firewall_version_number} | Get a firewall version
*WafFirewallVersionsApi* | [**list_waf_firewall_versions**](docs/WafFirewallVersionsApi.md#list_waf_firewall_versions) | **GET** /waf/firewalls/{firewall_id}/versions | List firewall versions
*WafFirewallVersionsApi* | [**update_waf_firewall_version**](docs/WafFirewallVersionsApi.md#update_waf_firewall_version) | **PATCH** /waf/firewalls/{firewall_id}/versions/{firewall_version_number} | Update a firewall version
*WafFirewallsApi* | [**create_waf_firewall**](docs/WafFirewallsApi.md#create_waf_firewall) | **POST** /waf/firewalls | Create a firewall
*WafFirewallsApi* | [**delete_waf_firewall**](docs/WafFirewallsApi.md#delete_waf_firewall) | **DELETE** /waf/firewalls/{firewall_id} | Delete a firewall
*WafFirewallsApi* | [**get_waf_firewall**](docs/WafFirewallsApi.md#get_waf_firewall) | **GET** /waf/firewalls/{firewall_id} | Get a firewall
*WafFirewallsApi* | [**list_waf_firewalls**](docs/WafFirewallsApi.md#list_waf_firewalls) | **GET** /waf/firewalls | List firewalls
*WafFirewallsApi* | [**update_waf_firewall**](docs/WafFirewallsApi.md#update_waf_firewall) | **PATCH** /waf/firewalls/{firewall_id} | Update a firewall
*WafRuleRevisionsApi* | [**get_waf_rule_revision**](docs/WafRuleRevisionsApi.md#get_waf_rule_revision) | **GET** /waf/rules/{waf_rule_id}/revisions/{waf_rule_revision_number} | Get a revision of a rule
*WafRuleRevisionsApi* | [**list_waf_rule_revisions**](docs/WafRuleRevisionsApi.md#list_waf_rule_revisions) | **GET** /waf/rules/{waf_rule_id}/revisions | List revisions for a rule
*WafRulesApi* | [**get_waf_rule**](docs/WafRulesApi.md#get_waf_rule) | **GET** /waf/rules/{waf_rule_id} | Get a rule
*WafRulesApi* | [**list_waf_rules**](docs/WafRulesApi.md#list_waf_rules) | **GET** /waf/rules | List available WAF rules
*WafTagsApi* | [**list_waf_tags**](docs/WafTagsApi.md#list_waf_tags) | **GET** /waf/tags | List tags
*WholePlatformDdosHistoricalApi* | [**get_platform_ddos_historical**](docs/WholePlatformDdosHistoricalApi.md#get_platform_ddos_historical) | **GET** /metrics/platform/ddos | Get historical DDoS metrics for the entire Fastly platform


## Issues

The fastly-py API client currently does not support the following endpoints:

- [`/resources/stores/kv/{store_id}/batch`](https://developer.fastly.com/reference/api/services/resources/kv-store-item) (PUT)
- [`/tls/activations/{tls_activation_id}`](https://developer.fastly.com/reference/api/tls/mutual-tls/activations) (GET, PATCH)
- [`/tls/activations`](https://developer.fastly.com/reference/api/tls/mutual-tls/activations) (GET)
- [`/v1/channel/{service_id}/ts/h/limit/{max_entries}`](https://developer.fastly.com/reference/api/metrics-stats/origin-insights) (GET)
- [`/v1/channel/{service_id}/ts/h`](https://developer.fastly.com/reference/api/metrics-stats/origin-insights) (GET)
- [`/v1/channel/{service_id}/ts/{start_timestamp}`](https://developer.fastly.com/reference/api/metrics-stats/origin-insights) (GET)


If you encounter any non-security-related bug or unexpected behavior, please [file an issue][bug]
using the bug report template.

[bug]: https://github.com/fastly/fastly-py/issues/new?labels=bug

### Security issues

Please see our [SECURITY.md](./SECURITY.md) for guidance on reporting security-related issues.

## License

[MIT](./LICENSE).

