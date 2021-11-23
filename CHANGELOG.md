# Changelog
All notable changes to this project will be documented in this file.
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
