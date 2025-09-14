# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Removed
- Remove legacy module `danish_banking_holidays.bankdag`. The package now exposes
  `DanishBankingCalendar` in `danish_banking_holidays.calendar`.

### Added
- `DanishBankingCalendar` class (`danish_banking_holidays/calendar.py`) — new
  class-based API for computing Danish banking holidays and business-day
  arithmetic.
- Tests for the new calendar class (`tests/test_calendar.py`).
- `CHANGELOG.md` (this file).

### Changed
- `README.md` updated to document the new API and remove legacy usage example.
- `setup.py` version bumped to `0.2.0`.
- `tests/test_bankdag.py` converted to use the new API.

## 0.1.0 - Initial work
- Initial project structure and original procedural functions (historical).


### Notes
- The project is not yet published to PyPI. If publishing, consider a
  semantic version tag (e.g., `v0.2.0`) and include a release note referencing
  this changelog entry.
