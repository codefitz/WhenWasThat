import datetime as dt
import pytest

from WhenWasThat import when


def test_days_between_known_dates():
    first_date = dt.datetime(2006, 10, 27, 11, 59, 32, 343001)
    last_date = dt.datetime(2016, 9, 30, 20, 21, 43, 561783)
    expected_days = (last_date - first_date).total_seconds() / 86400
    assert when(first_date, last_date).days == pytest.approx(expected_days)


def test_natural_known_dates():
    first_date = dt.datetime(2006, 10, 27, 11, 59, 32, 343001)
    last_date = dt.datetime(2016, 9, 30, 20, 21, 43, 561783)
    assert when(first_date, last_date).natural == "Approximately 9.9 years ago"

