# WhenWasThat

Python module for returning a human readable value for the time between two specified datetime objects. Inspired by whenWasThat() function from BMC Discovery.

## Properties

| Property     | Details                                                              |
| :----------: | -------------------------------------------------------------------- |
| microseconds | Output the total number of microseconds between two datetime objects |
| seconds      | Output the total number of seconds between two datetime objects      |
| minutes      | Output the total number of minutes between two datetime objects      |
| hours        | Output the total number of hours between two datetime objects        |
| days         | Output the total number of days between two datetime objects         |
| weeks        | Output the total number of weeks between two datetime objects        |
| months       | Output the total number of months between two datetime objects       |
| years        | Output the total number of years between two datetime objects        |
| natural      | Output an approximate number of seconds, minutes, hours, days, weeks, months or years between two datetime objects |

## Usage Examples

### Retrieve number of days between two dates

```python
>>> import import datetime as dt
>>> from WhenWasThat import when
>>> first_date = dt.datetime(2006, 10, 27, 11, 59, 32, 343001)
>>> last_date = dt.datetime(2016, 9, 30, 20, 21, 43, 561783)
>>> when(first_date,last_date).days
3626.348740958125
```

### Output a natural approximation of the time between two dates

```python
>>> first_date = dt.datetime(2006, 10, 27, 11, 59, 32, 343001)
>>> last_date = dt.datetime(2016, 9, 30, 20, 21, 43, 561783)
>>> when(first_date,last_date).natural
Approximately 9.9 years ago
```

### Last date is not required (module will calculate from `datetime.now()`)

```python
>>> time_then = dt.datetime(2020, 3, 23, 0, 1, 1, 1)
>>> when(time_then).weeks
75.20358385298611
>>> when(time_then).natural
Approximately 17.5 months ago
```

## How many days since the Titanic sunk?

```python
>>> dt.datetime.now()
datetime.datetime(2021, 8, 31, 10, 20, 59, 979468)
>>> titanic = dt.datetime(1912, 4, 15, 2, 20, 0, 0)
>>> print("The Titanic sunk %s days ago." % round(when(titanic).days))
The Titanic sunk 39950 days ago.
```

## Releases

| Version     | Summary                                                | Known Issues          | Fixed                          |
| :---------: | ------------------------------------------------------ | --------------------- | ------------------------------ |
| Alpha-0.0.1 | Alpha release.                                         |                       |                                |
| 0.1.0       | Released to PyPi                                       |                       |                                |
