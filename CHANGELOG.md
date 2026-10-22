# Changelog

## [v15.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v15.0.0) (2026-10-21)

**Breaking Changes:**

- removed(metrics-platform): Removed the `get-platform-metrics-service-historical` operation (`GET /metrics/platform/services/{service_id}/{granularity}`). Use `get-platform-metrics-entity-historical` instead.
- removed(metrics-platform): Removed the `ttfb_*` fields (`ttfb_edge_p25_us` to `ttfb_edge_p99_us`, `ttfb_origin_*`, and `ttfb_shield_*`) from `platform_values`, and the `ttfb` value from the `metric_set` parameter.
- changed(automation-tokens): Removed the `attributes` wrapper object from `automation_token_create_request`. `name`, `role`, `services`, `scope`, `expires_at`, and `tls_access` are now top-level fields, and `role` is no longer required.
- changed(automation-tokens): Added `ngwaf_user_imported`, `ngwaf_admin_imported`, `ngwaf_owner_imported`, `ngwaf_observer_imported`, `tls_admin`, and `tls_viewer` to the `role` enum of token responses.
- changed(products[ddos_protection]): Added `client_challenge` to the allowed `mode` values for `enable-product-ddos-protection` and `set-product-ddos-protection-configuration`.


**Bug fixes:**

- fix(logging_datadog): Correct `request_time_ms` in the default Datadog log format to report elapsed time in milliseconds as a number, rather than microseconds as a string.


**Enhancements:**

- feat(metrics-platform): Add the `get-platform-metrics-entity-historical` (`/metrics/v2/platform/entities/{entity_id}/{granularity}`) and `get-platform-metrics-aggregate-historical` (`/metrics/v2/platform/aggregate/{granularity}`) operations, with pagination, metric sets, and flexible grouping.
- feat(metrics-platform): Add `metric_set` values `delivery_traffic_flow`, `delivery_cache_performance`, `delivery_errors`, `compute_traffic_flow`, `compute_performance`, `compute_errors`, `content_guard`, `content_security`, `ddos`, `domain_api`, `fanout`, `image_opto`, `ngwaf`, `object_storage`, and `websockets`, and add the corresponding metric fields to `platform_values`.
- feat(bot-requests-metrics): Add the bot request metrics API (`get-bot-request-metrics-service-historical`), which returns historical time series of ContentGuard bot-request metrics for a service, broken down by bot.
- feat(automation-tokens): Add support for multiple roles with the `roles`, `limit_services`, `limit_workspaces`, and `workspaces` fields on token create requests and token responses.
- feat(automation-tokens): Add the `get-automation-tokens-id-workspaces` operation to list the Next-Gen WAF workspaces that an automation token can access.
- feat(historical, realtime): Add new API Enforcement metrics: `api_enforcement_allowed_requests_count` and `api_enforcement_flagged_requests_count`.
- feat(historical, realtime): Add new Network Protect metrics: `netprotect_gre_sent_bytes`, `netprotect_gre_sent_packets`, `netprotect_received_bytes`, `netprotect_received_packets`, `netprotect_firewall_dropped_bytes`, and `netprotect_firewall_dropped_packets`.
- feat(historical, realtime): Add new ContentGuard challenge metrics: `bot_edge_challenge_complete_tokens_issued`, `bot_edge_challenges_issued`, `bot_edge_challenges_succeeded`, `bot_edge_challenges_failed`, `bot_edge_challenges_pats_issued`, and `bot_edge_challenges_pats_succeeded`.
- feat(historical, realtime): Add new AI Runtime Control AI Firewall metrics: `arc_ai_firewall_requests` and `arc_ai_firewall_blocked`.

- feat(purge): Add the optional `Fastly-Purge-Environment` header to `purge-all`, `purge-tag`, and `bulk-purge-tag`.
  Set it to `staging` to purge the cache of a service's staging environment.

- feat(network-protect): Add the Network Protect API for managing protected networks, GRE delivery endpoints, prefix lists, and traffic-filtering rule sets.

- feat(products): Add `ai_runtime_control` product to enablement API.
- feat(ai-runtime-control-virtual-keys): Add virtual keys API for AI Runtime Control, covering create/list/get/update/delete/rotate and per-key failover policies.
- feat(ai-runtime-control-provider-connections): Add provider connections API for AI Runtime Control, supporting API-key and AWS IAM (Bedrock) authentication.
- feat(ai-runtime-control-providers): Add providers API for AI Runtime Control, covering supported providers, provider models, and Bedrock setup information.
- feat(ai-runtime-control-usage-metrics): Add usage metrics API for AI Runtime Control, including a CSV export endpoint.
- feat(ai-runtime-control-sessions): Add session logs API for AI Runtime Control.

- feat(historical, realtime): Add new metric `bot_edge_requests_headless_count`, the number of edge requests where a headless bot was detected.
- feat(historical, realtime, domain_inspector_historical, domain_inspector_realtime): Add new metric `status_499`, the number of responses sent with status code 499 (Client Disconnected).
- feat(historical, realtime): Add new metrics `imgopto_input_image_bytes` and `imgopto_output_image_bytes`, describing the total image bytes before and after transformation by the Fastly Image Optimizer.
- feat(historical, realtime): Add new metric `arc_requests`, the number of requests received by AI Runtime Control.
- feat(historical, realtime): Add new DDoS protection challenge metrics: `ddos_challenge_complete_tokens_checked`, `ddos_challenge_complete_tokens_passed`, `ddos_challenge_complete_tokens_failed`, `ddos_challenge_starts`, `ddos_challenge_complete_tokens_issued`, `ddos_challenges_issued`, `ddos_challenges_succeeded`, `ddos_challenges_failed`, `ddos_challenges_pats_issued`, and `ddos_challenges_pats_succeeded`.

- feat(bot-management): Add the Bot Management API for configuring ContentGuard, covering workspace protection mode, category actions, per-bot action overrides, and a workspace-wide bot listing.

- feat(events): Add 37 `ngwaf.*` values to `event_type`, covering Next-Gen WAF workspaces, rules, lists, custom signals, redactions, virtual patches, thresholds, workspace alerts, header links, rate limited sources, custom dashboards, request reports, and agent keys.


**Documentation:**

- doc(dictionary-item): Correct the documented maximum length of `item_key` from 256 to 255 characters.

- doc(ddos-protection): Add `client_challenge` to the list of supported action values for DDoS protection rules.

- doc(events): Mark the `security.*` Next-Gen WAF `event_type` values as deprecated. They are no longer recorded, and are superseded by their `ngwaf.*` equivalents.


## [v14.1.0](https://github.com/fastly/fastly-py/releases/tag/release/v14.1.0) (2026-08-18)

**Enhancements:**

- feat(historical, realtime): Add new Private Access Token (PAT) challenge metrics: `bot_challenges_pats_issued` and `bot_challenges_pats_succeeded`.
- feat(domain_inspector_historical, domain_inspector_realtime): Add new metrics describing the distribution of HTTP and TLS versions used by incoming requests: `http2`, `http3`, `tls_v10`, `tls_v11`, `tls_v12`, and `tls_v13`.

- feat(ngwaf_rules): Add `created_by` to rule responses.
- feat(ngwaf_signals): Add `created_by` to signal responses.
- feat(ngwaf): Document missing error response codes across several Next-Gen WAF endpoints.

- feat(logging_endpoint_errors): Add new Logging Endpoint Errors API for creating error records and streaming recent errors from logging endpoints.


**Documentation:**

- doc(config_store, config_store_item, secret_store, secret_store_item): Update links to the config store and secret store documentation guides.


## [v14.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v14.0.0) (2026-07-17)

**Breaking Changes:**

- changed(properties): Changed the default value of `logging_message_type` from `classic` to `blank` for the Sumologic, HTTPS, and Syslog logging endpoints.

- changed(notifications): Added Datadog, Jira Issue, Jira Service Management, OpsGenie, and Splunk On-Call to the `integration_type` enum.
- changed(ngwaf_requests): Renamed the workspace-level search requests operation and response schema (`ngwafSearchRequests`/`searchRequests` -> `ngwafSearchWorkspaceRequests`/`searchWorkspaceRequests`) to disambiguate it from the new account-level search operation.

- removed(historical, realtime, observability_dashboard_metrics_edge): Removed metrics `waf_logged`, `waf_blocked`, and `waf_passed`.


**Bug fixes:**

- fix(realtime): Corrected the `realtime_entry_datacenter` schema to use `allOf` instead of `additionalProperties`, so generated models match the actual API response shape.


**Enhancements:**

- feat(ngwaf_simulate): Increased the WAF simulation request body size limit from 100 KB to 200 KB.
- feat(ngwaf_simulate): Add `detector_scope` field to WAF simulation signal responses.

- feat(historical, realtime): Add new Compute backend request error metrics: `compute_service_bereq_dns_error`, `compute_service_bereq_conn_timeout_error`, `compute_service_bereq_conn_refused_error`, `compute_service_bereq_conn_other_error`, `compute_service_bereq_tls_server_cert_error`, `compute_service_bereq_tls_other_error`, `compute_service_bereq_http_incomplete_error`, `compute_service_bereq_http_timeout_error`, `compute_service_bereq_http_other_error`, `compute_service_bereq_other_error`, `compute_service_bereq_conn_error`, `compute_service_bereq_tls_error`, and `compute_service_bereq_http_error`.

- feat(notification-service): Add Event Mappings API for creating and managing audit event notification mappings with support for `account`, `vcl`, `wasm`, and `ngwaf` scope types.
- feat(routing-configs): Add new Domain Management Routing Configs API for defining path-based routing rules, with support for paths, rules, versions, drafts, and activation.
- feat(domains): Add `routing_configuration_id` field and query filter for associating domains with a routing configuration.

- feat(ngwaf_requests): Add account-level `GET /ngwaf/v1/requests` endpoint for searching requests across all workspaces in an account.

- feat(ngwaf_workspaces): Add `workspace_uid` field to workspace responses.

- feat(ngwaf_thresholds): Add `block_immediately` action to the thresholds endpoints.

- feat(ngwaf_signals): Increased the maximum length of custom signal names from 25 to 128 characters.

- feat(backend): Add `max_lifetime` and `max_use` fields for controlling pooled HTTP keepalive connection reuse.

- feat(historical, realtime): Add new metric `compute_handoff`.

- feat(ngwaf): Add WAF simulate endpoint for testing WAF rule behavior against sample HTTP requests.

- feat(products): Add `kv_store` product to enablement API.

- feat(ngwaf_agents): Add new NGWAF Agents API for listing and retrieving agents.

- feat(enabled-products): Add ContentGuard support for `bot_management`
- feat(historical, realtime): Add new bot-classification metrics: `bot_requests_total_count`, `bot_edge_requests_analyzed_count`, `bot_edge_requests_detected_count`, `bot_edge_requests_verified_count`, `bot_edge_requests_ai_crawler_count`, `bot_edge_requests_ai_fetcher_count`, `bot_edge_requests_accessibility_count`, `bot_edge_requests_content_fetcher_count`, `bot_edge_requests_monitoring_count`, `bot_edge_requests_online_marketing_count`, `bot_edge_requests_page_preview_count`, `bot_edge_requests_platform_integrations_count`, `bot_edge_requests_research_count`, `bot_edge_requests_search_engine_crawler_count`, `bot_edge_requests_search_engine_optimization_count`, and `bot_edge_requests_security_tools_count`.

- feat(client_side_protection): Add new Client-Side Protection API for managing websites, pages, scripts, policies, and security headers.
- feat(historical, realtime): Add new metric `compute_sandboxes`.
- feat(ngwaf_agent_keys): Add new NGWAF Agent Keys API for listing agent keys within a workspace.

**Documentation:**

- doc(notifications): Document that deleting an integration removes it from all audit log event mappings. Any audit log event mappings whose `integration_ids` list becomes empty as a result are automatically set to `inactive`.


## [v13.1.0](https://github.com/fastly/fastly-py/releases/tag/release/v13.1.0) (2026-03-30)

**Enhancements:**

- feat(historical, realtime): Deprecated metrics `compute_bereq_errors`, `compute_resource_limit_exceeded`,
                              `compute_heap_limit_exceeded`, `compute_stack_limit_exceeded`, `compute_globals_limit_exceeded`,
                              `compute_guest_errors`, and `compute_runtime_errors`.
- feat(historical, realtime): Added metrics `compute_service_bereq_error`, `compute_service_memory_exceeded_error`.
                              `imgopto_avif_count`, `imgopto_jpeg_count`, `imgopto_png_count`, `imgopto_gif_count`,
                              `imgopto_webp_count`, `imgopto_jpegxl_count`, `imgopto_svg_count`, `imgopto_mp4_count`,
                              `compute_service_resource_limits_error`, `compute_service_runtime_error`, `compute_service_chain_error`
                              `compute_platform_internal_error`, `compute_service_timeout_error`, `compute_service_vcpu_exceeded_error`
                              `compute_service_limits_error`, and `compute_platform_invalid_request_error`.
- feat(domains): Add new Domain Management Domains API.
- feat(apisecurity-operations): Results include support for `rps` and `id`.
- feat(apisecurity-operations): List endpoints add support for new parameters `method`, `domain`, and `path`.
- feat(apisecurity-operations): Add new bulk operations endpoints.


## [v13.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v13.0.0) (2026-02-16)

**Breaking Changes:**

- deprecated(user): The Compute package metadata model `hashsum` and `size` fields have been deprecated.


**Enhancements:**

- feat(apisecurity-operations): Add new API Security Operations API.
- feat(domain-inspector-realtime, domain-inspector-historical): Add new metrics `compute_*`.
- feat(realtime, historical): Add new metrics `compute_resp_status_*`.
- feat(realtime, historical): Add new metric `ngwaf_bot_analysis_request_count`.
- feat(backend): Add support for `fetch_timeout` field.
- feat(historical): Add support for `datacenter` query.


## [v12.1.0](https://github.com/fastly/fastly-py/releases/tag/release/v12.1.0) (2025-12-09)

**Enhancements:**

- feat(py): Update to support urllib3 2.6.0 (fastly-py#112)
- feat(realtime, historical): Add new metrics `imgopto_compute_requests`, `dns_billable_responses_count`,
                              `dns_nonbillable_responses_count`, and `upgrade`.
- feat(products[ngwaf]): Add new parameter `traffic_ramp` to `enable-product-ngwaf`.
- feat(products[ddos_protection]): Add new parameter `mode` to `enable-product-ddos-protection`.
- feat(kv_store): Add `kv-store-put` operation.
- feat(iam_roles): Add `DisplayName` field to model.
- feat(domain_research): Add new Domain Research API.
- feat(ddos_protection): Add `requests_allowed` and `requests_detected` fields to DDoS Protection event API.

- feat(products): Add `domain_research` product to enablement API.



**Documentation:**

- doc(enabled-products): Add support for optional enablement parameters for some products.


## [v12.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v12.0.0) (2025-10-31)

**Bug fixes:**

- fix(dictionary): Correct example dictionary name to use valid characters

**Enhancements:**

- feat(iam_roles): Add new IAM Roles API.
- feat(api_discovery): Add new API Discovery API.
- feat(realtime, historical): Add new metric `api_discovery_requests_count`.
- feat(user): Add the ability to assign multiple roles to users.
- feat(healthcheck): Clarify the valid range for the `check_interval` parameter.
- feat(ddos_protection): Add `traffic_percentage` field to DDoS Protection traffic statistics responses.
- feat(ddos_protection): Update `ddos-protection-event-rule-list` with `include=traffic_stats` parameter for embedded traffic statistics.
- feat(logging_https): Add `period` parameter to the logging HTTPS endpoint.

**Documentation:**

- doc(sudo): Spelling fixes.
- doc(enabled-products): Add support for product ID `api_discovery`.


## [v11.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v11.0.0) (2025-08-28)

**Breaking Changes:**

- removed(ddos_protection): Remove enum configs `ddos_protection_action` and ``ddos_protection_traffic_attribute`.
- changed(backend): Added default values to `tcp_keepalive_interval`, `tcp_keepalive_probes`, and `tcp_keepalive_time` properties.
- removed(tls_subscriptions): Remove `force` parameter from TLS subscriptions.


**Enhancements:**

- feat(ngwaf_reports): Add Get attacks report endpoint.
- feat(kv_store): Add `name` parameter to the List KV stores endpoint.
- feat(historical): Add `services` parameter to the Historical Stats API endpoint.
- feat(ddos_protection): Add PATCH endpoint in the Fastly DDoS Protection Events API allowing customers to update the DDoS rules action to `log`, `block`, `default`, or `off`.
- feat(observability_timeseries): Add Observability Timeseries API for data visualized in the Sustainability dashboard.


**Documentation:**

- doc(backend, pool): Describe difference in behavior of `between_bytes_timeout` between
                      Deliver and Compute services.
- doc(ddos_protection): Update GET API docs describing that they can be accessed by any user role as long as the service belongs to the customer.


## [v10.1.0](https://github.com/fastly/fastly-py/releases/tag/release/v10.1.0) (2025-07-07)

**Bug fixes:**

- fix(backend): Marked `prefer_ipv6` as not nullable, and documented that the default value differs for Delivery and Compute services.
- fix(invitations): Marked `service_invitations.data` under relationships as nullable, and corrected model composition.


**Enhancements:**

- feat(tls_certificates): Add `allow_untrusted_root` attribute for TLS certificate creation and update endpoints


**Documentation:**

- doc: Update redirect URLs


## [v10.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v10.0.0) (2025-06-11)

**Breaking Changes:**

- removed(properties): Remove logging placement value `waf_debug`.


**Bug fixes:**

- fix(backend): Marked `prefer_ipv6` as nullable.


**Enhancements:**

- feat(historical): The following Next-Gen WAF metrics have been updated to include both Edge WAF and
-                   Core WAF counts:`ngwaf_requests_total_count`, `ngwaf_requests_blocked_count`,


**Documentation:**

- doc(domain-discovery): Correct documentation of valid values of `scope` query parameter.
- doc(observability-aggregations-for-logs): Correct documentation of valid values of `log-aggregations-filter` query
                                            parameter.
- doc(backend): Tweak language of `prefer_ipv6` description.
- doc(service): Add documentation for `filter[versions.active]` query parameter when getting detailed information on
                a specified service.


## [v9.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v9.0.0) (2025-05-12)

**Breaking Changes:**

- deprecated(user): The POST /user endpoint has been deprecated.

- fix(acls_in_compute): Corrected the successful `PATCH` response code from the `/resources/acls/${acl_id}/entries` endpoint.


**Enhancements:**

- feat(products): Add endpoint to each service-level product to list services that enable that product.
- feat(observability-aggregations-for-logs): Add new Observability Aggregations API for Logs.
- feat(observability-timeseries-for-logs): Add new Observability Timeseries API for Logs.
- feat(pops): Add new Mexico regions.
- feat(historical): Add new Mexico regions.
- feat(ddos-protection): Add `ddos-protection` product.
- feat(backend): Add the `prefer_ipv6` option to prefer IPv6 during a backend DNS hostname lookup.
- feat(products): Added new GET endpoint for all services with product enabled on a customer.

**Documentation:**

- doc(kv-store): Add clarification on valid KV Store names.
- doc(kv-store-item): Add clarification on valid KV Store keys.
- doc(dictionary): Usages of `edge dictionary` standardized to `dictionary`.
- doc(acls-in-compute): Add documentation on how to remove a single ACL entry using the existing
                        `compute-acl-update-acls` operation.
- doc(acls-in-compute): Correct documentation on `action` field of `compute-acl-update-acls` endpoint.

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