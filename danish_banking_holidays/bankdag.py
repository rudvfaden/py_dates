"""
This module has been removed in favor of the `DanishBankingCalendar` class
implemented in `danish_banking_holidays.calendar`.

The package was not yet public, so the legacy function wrappers were removed.

If you imported functions from `danish_banking_holidays.bankdag`, update your
code to use the new API. Example:

    from danish_banking_holidays.calendar import DanishBankingCalendar
    calendar = DanishBankingCalendar()
    holidays = calendar.get_holidays(2023)

To intentionally fail fast if old imports remain, we raise an ImportError.
"""

raise ImportError(
    "danish_banking_holidays.bankdag has been removed. "
    "Use danish_banking_holidays.calendar.DanishBankingCalendar instead."
)
