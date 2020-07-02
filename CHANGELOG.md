# Changelog
All notable changes to this project will be documented in this file.
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.5.0-ilon1] - October 14, 2020

### Fixed

<<<<<<< HEAD
- No longer raises KeyError exception when trying to save a model object with an attribute set not found in original attributes

## [0.5.0] - September 30, 2020

### Breaking

- Removed support for password authentication because the API no longer supports it.
- Fixed how the `FASTLY_SECURE` environment variable is processed so as to convert it to a boolean
=======
- Executing query on a model where attributes containing non-safe characters used in the URL no longer raises exception
- No longer raises KeyError exception when trying to save a model object with an attribute set not found in original attributes 
>>>>>>> 99d2225... Should not raise exceptions when running query with unsafe chars in kw

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
