# Changelog

## [v5.0.1](https://github.com/fastly/fastly-py/releases/tag/release/v5.0.1) (2024-02-16)

**Bug fixes:**

- fix(response_object): strongly type response_object create_update requests
- fix(tls_configurations): fix `tls_protocols` field to be a string array type
- fix(generator): fix `str, none_type` in generated code

## [v5.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v5.0.0) (2023-11-29)

**Breaking:**

- breaking(historical): restructure OpenAPI schema to avoid duplicated data rendering.

**Bug fixes:**

- fix: no longer display Markdown syntax in code comments.

**Enhancements:**

- feat(stats): expose new `service_id` and `start_time` fields.

## [v4.2.2](https://github.com/fastly/fastly-py/releases/tag/release/v4.2.2) (2023-11-07)

**Enhancements:**

- feat(config_store): add `name` query param to list endpoint.

## [v4.2.1](https://github.com/fastly/fastly-py/releases/tag/release/v4.2.1) (2023-10-27)

**Documentation:**

- docs: rename Compute@Edge to Compute.

## [v4.2.0](https://github.com/fastly/fastly-py/releases/tag/release/v4.2.0) (2023-10-24)

**Enhancements:**

- feat(stats): add historical DDoS metrics.
- feat(stats): add bot challenges.

**Bug fixes:**

- fix(snippets): ensure POST response's dynamic field is numerical.

## [v4.1.1](https://github.com/fastly/fastly-py/releases/tag/release/v4.1.1) (2023-09-01)

**Enhancements:**

- feat(events): support extra created_at filters.

## [v4.1.0](https://github.com/fastly/fastly-py/releases/tag/release/v4.1.0) (2023-09-01)

**Enhancements:**

- feat(backend): support share_key field.
- feat(events): support extra created_at filters.
- feat(logging/newrelic): add OTLP endpoints.
- feat(tls/subscriptions): support self_managed_http_challenge field.

**Documentation:**

- doc(secretstore): correct description for GET endpoint.

## [v4.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v4.0.0) (2023-07-31)

**Breaking:**

The following restructures have helped resolve some issues with our OpenAPI schemas but as a side-effect this has resulted in a break to our API client interface as different types are now being generated.

- refactor: general restructure OpenAPI schemas.
- refactor(domain): remove explicit schema type for 'any'.

**Bug fixes:**

- fix: change response `version` type to string.
- fix(cache_settings): change response `stale_ttl` and `ttl` types to strings.
- fix(header): change response `ignore_if_set` and `priority` types to strings.
- fix(logging): change response `period` and `gzip_level` types to strings.
- fix(pool): change response `use_tls`, `max_conn_default`, `first_byte_timeout`, `quorum` and `tls_check_cert` types to strings.
- fix(request_settings): change response `bypass_busy_wait`, `force_miss`, `force_ssl`, `geo_headers`, `max_stale_age` and `timer_support` types to strings.
- fix(response_object): change response `status` type to string.

## [v3.0.2](https://github.com/fastly/fastly-py/releases/tag/release/v3.0.2) (2023-07-13)

**Bug fixes:**

- fix(logging_gcs): set expected default value for 'path'.
- fix(origin_inspector_historical): use correct type for 'values'.
- fix(tls_subscriptions): fix argument order for deleting globalsign email challenge.

## [v3.0.1](https://github.com/fastly/fastly-py/releases/tag/release/v3.0.1) (2023-07-12)

**Bug fixes:**

- fix(billing): rename response field 'lines' to 'line_items'.
- fix(billing): restructure response models like 'aria_invoice_id'.
- fix(billing): make 'sent_at', 'locked', 'require_new_password', 'two_factor_auth_enabled' nullable.

## [v3.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v3.0.0) (2023-07-06)

Substantial changes were made to the underlying OpenAPI specification that produces this API client. These changes have resulted in multiple new endpoints being supported as well as multiple breaking type changes and so we're publishing these changes as a new major release.

**Enhancements:**

- feat(apex_redirect): support all endpoints.
- feat(contact): support 'create' endpoint.
- feat(director): support 'update' endpoint.
- feat(domain_inspector): support all endpoints.
- feat(iam_roles): support 'add permissions' endpoint.
- feat(iam_roles): support 'create role' endpoint.
- feat(iam_roles): support 'delete permissions' endpoint.
- feat(iam_roles): support 'update role' endpoint.
- feat(iam_services): support 'add services' endpoint.
- feat(iam_services): support 'create service group' endpoint.
- feat(iam_services): support 'remove services' endpoint.
- feat(iam_services): support 'update service group' endpoint.
- feat(iam_users): support 'add members' endpoint.
- feat(iam_users): support 'add roles' endpoint.
- feat(iam_users): support 'add service groups' endpoint.
- feat(iam_users): support 'create user group' endpoint.
- feat(iam_users): support 'remove members' endpoint.
- feat(iam_users): support 'remove roles' endpoint.
- feat(iam_users): support 'remove service groups' endpoint.
- feat(iam_users): support 'update user group' endpoint.
- feat(legacy_waf): support all endpoints.
- feat(logging_kafka): support 'update' endpoint.
- feat(logging_kinesis): support 'update' endpoint.
- feat(origin_inspector): support all endpoints.
- feat(request_settings): support 'create' endpoint.
- feat(response_object): support 'create' endpoint.
- feat(response_object): support 'update' endpoint.
- feat(secret_store): support all endpoints.
- feat(service_authorizations): support 'delete' endpoint.
- feat(service_authorizations): support 'update' endpoint.
- feat(snippet): support 'update versioned snippet' endpoint.
- feat(sudo): support 'request sudo access' endpoint.
- feat(tokens): support 'revoke multiple tokens' endpoint.
- feat(tokens): support 'create token' endpoint.
- feat(waf_active_rules): support 'delete' endpoint.

**Bug fixes:**

- fix(content): update request/response types.
- fix(events): update metadata type.
- fix(realtime_entry): update recorded/aggregated type.
- fix(realtime_measurements): update miss_histogram type.

## [v2.4.0](https://github.com/fastly/fastly-py/releases/tag/release/v2.4.0) (2023-07-05)

**Enhancements:**

- feat(purge): support purge of multiple surrogate keys.
- feat(vcl): support vcl content endpoints.

**Bug fixes:**

- fix(snippet): dynamic field switched from int to string.
- fix(vcl): implement correct response models.

**Documentation:**

- docs: remove deprecated docs endpoints from README 'issues' list.

## [v2.3.0](https://github.com/fastly/fastly-py/releases/tag/release/v2.3.0) (2023-06-27)

**Enhancements:**

- feat(rate_limiter): implement POST/PUT endpoints.

**Bug fixes:**

- fix(historical_stats): extract primitive into custom type.

## [v2.2.2](https://github.com/fastly/fastly-py/releases/tag/release/v2.2.2) (2023-06-23)

**Bug fixes:**

- fix(historical_stats): generate missing models.
- fix(historical_stats): apply upstream fix to partial models.

## [v2.2.1](https://github.com/fastly/fastly-py/releases/tag/release/v2.2.1) (2023-06-21)

**Bug fixes:**

- fix(tls_activation): add tls_configuration and tls_domains.
- fix(tls_subscription): add tls_configuration and common name.

## [v2.2.0](https://github.com/fastly/fastly-py/releases/tag/release/v2.2.0) (2023-06-20)

**Enhancements:**

- feat(realtime_measurements): add billable request processing time.
- feat(tokens): add support for the 'get token' endpoint.

**Bug fixes:**

- fix(config): add realtime hostname.
- fix(historical_stats): generate field results model.
- fix(kv_store): remove the 'force' property from the 'delete store' endpoint.
- feat(realtime_measurements): rename object store to kv store.

## [v2.1.1](https://github.com/fastly/fastly-py/releases/tag/release/v2.1.1) (2023-05-22)

**Bug fixes:**

- fix(acl): change `version` from int to string.
- fix(acl): add missing methods for `service_id` and `service_version` properties.
- fix(backend): make `ssl_check_cert` nullable.
- fix(purge): skip URL escape for `surrogate_key` param.
- fix(snippets): change `priority` and `version` from int to string.
- fix(snippets): add missing methods for `service_id` and `service_version` properties.

## [v2.1.0](https://github.com/fastly/fastly-py/releases/tag/release/v2.1.0) (2023-05-17)

**Enhancements:**

- feat(config_store): add Config Store endpoints.

## [v2.0.0](https://github.com/fastly/fastly-py/releases/tag/release/v2.0.0) (2023-05-16)

**Breaking changes:**

- breaking(object_store): rename to kv_store

**Enhancements:**

- feat(dictionary_item): add 'bulk' PATCH endpoint.
- feat(package): add `files_hash` metadata property.
- feat(tls_certificates): add `filter[in_use]` parameter.

## [v1.3.1](https://github.com/fastly/fastly-py/releases/tag/release/v1.3.1) (2023-04-26)

**Bug fixes:**

- fix(object-store-item): use correct type for key value
- fix(tls-csrs): remove internal endpoint

## [v1.3.0](https://github.com/fastly/fastly-py/releases/tag/release/v1.3.0) (2023-04-03)

**Bug fixes:**

- fix(purge): avoid escaping URL parameter

**Enhancements:**

- feat(domain-ownership): list API endpoint
- feat(object-store): items API endpoints
- feat(object-store): add 'location' property to 'create_store'
- feat(object-store): add 'force' property to 'delete_store'
- feat(realtime): additional DDoS properties

**Documentation:**

- docs(acl-entries): document batch updating
- docs(resource): terminology + 'config_store' support.

## [v1.2.0](https://github.com/fastly/fastly-py/releases/tag/release/v1.2.0) (2023-03-20)

[Full Changelog](https://github.com/fastly/fastly-py/compare/v1.1.0...v1.2.0)

**Bug fixes:**

- fix(purge): switch authentication type to 'token'

**Enhancements:**

- feat(events): implement 'filter_created_at' property
- feat(mutual-authentication): implement 'include' property
- feat(object-store): implement new Object Store API endpoints
- feat(settings): implement Service Settings 'update' endpoint

**Documentation:**

- docs(backend): keepalive_time
- docs(pop): region, shield, latitude, longitude
- docs(product-enablement): brotli_compression
- docs(resource): terminology
- docs(results): fanout properties
- docs(tls/subscriptions): new 'failed' state
- docs(user): 'login' modification note removed

## [v1.0.0](https://github.com/fastly/fastly-py/releases/tag/v1.0.0) (2022-12-15)

[Full Changelog](https://github.com/fastly/fastly-py/compare/v0.5.1...v1.0.0)

**Enhancements:**

* New interface from code-generated API client [#82](https://github.com/fastly/fastly-py/pull/82) 
  * [Blog post: Better Fastly API clients with OpenAPI Generator](https://dev.to/fastly/better-fastly-api-clients-with-openapi-generator-3lno)
  * [Documentation](https://github.com/fastly/fastly-py#documentation-for-api-endpoints)
  * [Unsupported API endpoints](https://github.com/fastly/fastly-py#issues)

## [0.5.1] - March 26, 2021

### Fixed

- Boolean values in attributes now properly lower-cased during save

## [0.5.0] - September 30, 2020

### Breaking

- Removed support for password authentication because the API no longer supports it.
- Fixed how the `FASTLY_SECURE` environment variable is processed so as to convert it to a boolean

## [0.4.0] - January 6, 2020

### Added

- new command-line interface: `fastly` using argparse, thanks to the work of @dcmoore-gd

## [0.3.1] - January 6, 2020: 

### Fixed

- Fixed [unused imports](https://github.com/fastly/fastly-py/pull/47)
- Fixed [compatibility with python < 3.6](https://github.com/fastly/fastly-py/pull/46)

## [0.3.0] - July 10, 2019: 
### Added

- This `CHANGELOG.md` file
- `create` and `delete` methods to Model base
- Convenience methods to Service for fetching details and active version number

### Fixed

- Updated Service.version and Version.vcl to use new Model.create
- Compare `attrs` and `_original_attrs` before saving. (Without this check, calling .save() on an instance without changed attributes makes a PUT call with no data. Then instance.attrs is set to the error response for an incomplete API call, e.g. {"msg": "Missing parameter", "detail": "param is missing or the value is empty: item_value"})
Added missing VCL import to fastly.py

## [0.2.3] - August 2019
## Added
- Custom errors
- Backwards compatibility with Python 3.4

## Fixed
- Updates API models
