"""Package exports for danish_banking_holidays.

Exports the `DanishBankingCalendar` class. Legacy function wrappers were removed.
"""
from .calendar import DanishBankingCalendar  # noqa: F401

__all__ = ["DanishBankingCalendar"]
