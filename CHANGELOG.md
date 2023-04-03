# Changelog

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
