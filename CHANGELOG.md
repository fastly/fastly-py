# Changelog

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
