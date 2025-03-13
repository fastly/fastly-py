# Changelog

## [v8.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v8.0.0) (2025-03-13)

**Breaking Changes:**

- fix(automation_tokens): Response content types corrected.
- fix(automation_tokens): Removed timestamp fields.
- removed(billing): Billing v2 API has been removed.

- fix(acls_in_compute): Corrected `meta.limit` field type from string to integer.

- fix(condition): Condition responses now always have a string value for the priority field.
- fix(header): Header responses now always have a string value for the priority field.
- fix(snippet): Snippet responses now always have string values for the priority and dynamic fields.

- fix(kv_store_item): `kv-store-get-item` returns an inline object instead of a File object.


**Enhancements:**

- fix(automation_tokens): Added tls_access, creator_id fields to responses.
- feat(billing_usage_metrics): Added filter by service identifier for service-usage-metrics endpoint.
- feat(historical): Added new metrics: `ngwaf_requests_total_count`, `ngwaf_requests_unknown_count`,
                    `ngwaf_requests_allowed_count`, `ngwaf_requests_logged_count`, `ngwaf_requests_blocked_count`,
                    `ngwaf_requests_timeout_count`, and `ngwaf_requests_challenged_count`.
- feat(tls_bulk_certificates): Added `not_before` and `not_after` filter parameters to allow for filtering of bulk TLS
                               certificates by expiry.


**Documentation:**

- doc(billing_usage_metrics): Correct documentation of pagination limits.
- doc(billing_usage_metrics): Correct documentation of api conditions for product_id and usage_type_name filters.
- doc(logging_azureblob): Mention Azure Block size limits.


## [v7.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v7.0.0) (2025-02-26)

**Breaking Changes:**

- fix(snippet): Renamed `snippet_id` and `snippet_name` properties to `id` and `name` respectively.
- feat(kv_store, kv_store_item): KV store endpoints have new operation names, and the associated data models also have
                                 new names.
- feat(product): Product enablement and configuration endpoints have been renamed into per-product operations.
- fix(historical): Widened integer stats fields to 64 bits.
- fix(realtime, domain_inspector): Widened integer stats fields to 64 bits.
- fix(historical): Corrected field names of `ddos_protection_requests_detect_count`,
                   `ddos_protection_requests_mitigate_count`, and `ddos_protection_requests_allow_count`.
- fix(realtime): Corrected field names of `ddos_protection_requests_detect_count`,
                 `ddos_protection_requests_mitigate_count`, and `ddos_protection_requests_allow_count`.
- fix(billing_usage_metrics): added parameters `req_start_month` and `req_end_month`.
- deprecated(billing): Billing v2 API has been deprecated.
- removed(legacy_waf): Legacy WAF API has been removed.

**Bug fixes:**

- fix(snippet): Marked `content` as nullable to support dynamic snippets.
- fix(billing_usage_metrics): `product_id` and `usage_type_name` parameters are no longer required.

**Enhancements:**

- feat(products): Added `object_storage` and `ai_accelerator` products.
- feat(historical): Added new metrics: `object_storage_class_a_operations_count`,
                    `object_storage_class_b_operations_count`, `aia_requests`, `aia_status_1xx`,
                    `aia_status_2xx`, `aia_status_3xx`, `aia_status_5xx`, `aia_response_usage_tokens`,
                    `aia_origin_usage_tokens`, `aia_estimated_time_saved_ms`, `request_collapse_usable_count`,
                    `request_collapse_unusable_count`, `status_530`, and `compute_cache_operations_count`.
- feat(realtime): Added new metrics: `object_storage_class_a_operations_count`,
                  `object_storage_class_b_operations_count`, `aia_requests`, `aia_status_1xx`,
                  `aia_status_2xx`, `aia_status_3xx`, `aia_status_5xx`, `aia_response_usage_tokens`,
                  `aia_origin_usage_tokens`, `aia_estimated_time_saved_ms`, `request_collapse_usable_count`,
                  `request_collapse_unusable_count`, `status_530`, and `compute_cache_operations_count`.
- feat(object_storage_access_keys): Added Object Storage Access Keys API.
- feat(domain_inspector_historical, domain_inspector_realtime): Added new metrics: `status_530` and `origin_status_530`.
- feat(origin_inspector_historical, origin_inspector_realtime): Added new metrics: `status_530`, `waf_status_530`,
                                                                `compute_status_530`, and `all_status_530`.
- feat(kv_store_item): Added support for `if-generation-match`.
- feat(acls_in_compute): Added ACLs in Compute API.

**Documentation:**

- doc(billing_usage_metrics): Documented that `start_month` and `end_month` are required.
- doc(historical): Correct default start time in description of Historical Stats API.
- doc(domain_inspector_historical): Removed duplicate description.
- doc(domain_inspector_realtime): Removed duplicate description.
- doc(origin_inspector_historical): Removed duplicate description.
- doc(origin_inspector_realtime): Removed duplicate description.
- doc(backend): Updated description of Backend API.
- doc(backend): Clarified default behavior of keepalive_time.
- doc(waf): Updated EOL notice of legacy-waf.

## [v6.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v6.0.0) (2024-12-05)

**Breaking Changes:**

- fix(udm-domains): Use v1 versioned HTTP endpoints for UDM domains
- fix(historical): Remove references to VCL on Compute metrics
- fix(realtime): Remove references to VCL on Compute metrics
- feat(billing-usage-metrics): Updated to v3 of the API

**Bug fixes:**

- fix(acls-in-compute): Corrected shape of `compute-acl-update` model.

**Enhancements:**

- feat(object-storage-access-keys): Added Object Storage Access Keys API
- feat(logging-grafanacloudlogs): Added Grafana Cloud Logs Loggin API
- feat(log-explorer): Added Log Explorer API
- feat(insights): Added Insights API
- feat(kv-store-item): Added `consistency` parameter to `get-keys` operation.
- feat(enabled-products): Added `mode` property to `set-configuration`.

**Documentation:**

- doc(observability-custom-dashboards): Fix bad link in custom dashboard documentation
- doc(observability-custom-dashboards): Reformat some enums to fix docs rendering
- doc(acls-in-compute): Corrections to descriptions of `compute-acl-lookup`, `compute-acl-list-entries`,
                        `compute-acl-update-entry`, and `compute-acl-update` structures
- doc(enabled-products): Added support for product ID `log_explorer_insights`.
- doc(enabled-products): Added support for product ID `ddos_protection`.

## [v5.10.0](https://github.com/fastly/fastly-py/releases/tag/release/v5.10.0) (2024-10-23)

**Bug fixes:**

- bugfix(rust): Implement std::fmt::Display instead of std::string::ToString for enum models.
- bugfix(py): Add dependencies to pyproject.toml.
- fix(contact): Corrected endpoint called by `delete-contact` operation
- fix(origin-inspector, domain-inspector): Use integer type for Timestamp.
- fix(billing): Make all fields on billing list item data nullable
- fix(billing): make rate-per-unit nullable
- fix(billing): Adjust type of regional data to help the generator
- fix(billing): Correct type of invoice_id field
- fix(logging): For several endpoints, correct use_tls to be string
- fix(backend): Correct tcp_keepalive_enable to be nullable
- bugfix(billing_address, invitations): Correct customer relationship schema to be single entry rather than array
- bugfix(request_settings): Mark request_settings fields as nullable: bypass_busy_wait, force_miss, geo_headers,
  max_stale_age, timer_support, and xff
- bugfix(resource): Correct `type_resource` accepted values
- bugfix(sudo): Mark API to require authentication token
- bugfix(alerts-definitions): For Origin derived metrics, correct `all_bandwidth` type to `integer`

**Enhancements:**

- feat(generator): The API Client Generator now uses a new automatic changelog generation process.
- feat(acls-in-compute): Add ACLs in Compute API
- feat(enabled-products): Updated to use `v1` versioned endpoints.
- feat(enabled-products): Added `get-product-configuration`, `set-product-configuration` operations.
- feat(realtime, historical): Added `request_denied_get_head_body` metric.
- feat(tls): Add definitions for values of sort parameter
- feat(staging): Add activate/deactivate endpoints for staging
- feat(customer-addresses): Add Customer Addresses API
- feat(observability): Adds new Observability Custom Dashboards API
- feat(billing-invoices): Adds month-to-date invoice information
- feat(billing-usage-metrics): Adds information on service-level usage.
- feat(tls): Adds an endpoint to get a TLS certificate blob (Limited Availability)
- feat(stats): Add `origin_offload` metric
- feat(content): `/content/edge_check` endpoint now returns informational values in `hash` when a timeout occurs or when
  an object is too large.
- feat(logging-datalog): Added additional regions
- feat(historical, realtime): Add the following new metrics: `ddos_action_downgrade`,
  `ddos_action_downgraded_connections`, `vcl_on_compute_hit_requests`, `vcl_on_compute_miss_requests`,
  `vcl_on_compute_pass_requests`, `vcl_on_compute_error_requests`, `vcl_on_compute_synth_requests`,
  `vcl_on_compute_edge_hit_requests`, `vcl_on_compute_edge_miss_requests`, `all_hit_requests`,
  `all_miss_requests`, `all_pass_requests`, `all_error_requests`, `all_synth_requests`, `all_edge_hit_requests`,
  `all_edge_miss_requests`, `all_status_1xx`, `all_status_2xx`, `all_status_3xx`, `all_status_4xx`, and
  `all_status_5xx`.
- feat(backend): Add `tcp_keepalive_*` properties to the Backend API, which allow configuring TCP keepalives for
  backend connections.
- feat(image-optimizer-default-settings): Add Image Optimizer Default Settings APIs
- feat(tls-subscriptions): Add `certificate_authority` filter parameter
- feat(logging-s3): Add `file_max_bytes` configuration field
- feat(alerts-definitions): Add `integration_id` parameter to the List Alert Definitions endpoint
- feat(alerts-definitions): For Origin derived metrics, add `all_status_4xx_excl_404_rate` and `all_status_404_rate` properties
- feat(alerts-definitions): For Domain derived metrics, add `status_4xx_excl_404_rate` and `status_404_rate` properties
- feat(alerts-definitions): For Stats derived metrics, add `status_4xx_excl_404_rate`, `status_404_rate`, `all_status_5xx_rate`,
                            `all_status_4xx_rate`, `all_status_gte_400_rate`, and `all_status_lt_500_rate` properties
- feat(billing-invoices): For invoice line items, added `ProductLine` property

**Documentation:**

- docs(generator): Update links in docs and comments with unified docs site URL structure
- docs(generator): Clean up README by using GitHub alert icons and collapsible sections
- doc(backend): Correct spelling in `connect_timeout` and `first_byte_timeout` field descriptions.
- doc(enabled-products): Added support for product IDs `bot_management` and `ngwaf`.
- doc(realtime): Correct description of miss_histogram structure in real-time stats.
- doc(logging-kinesis): Update description of `format` field.
- doc(tls-subscriptions): Update descriptions of `certificate_authority` and `tls_subscription_include` fields.
- doc(billing-invoices): "Billing Invoices API" relabeled to "Invoices API"
- doc(billing-invoices): Updated documentation of `billing_start_date` and `billing_end_date` query parameters of
                         List of invoices endpoint
- doc(alerts-definitions): Updated documentation of several fields
- doc(notification-service): Updated documentation examples for several fields
