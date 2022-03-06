import datetime as dt
import pandas as pd

class whenWasThat:
    '''When was that?'''

    def __init__(self, time_then, time_now = dt.datetime.now()):
        self.time_then = time_then
        self.time_now = time_now
        self.new_delta = abs(time_now - time_then)
        
        # Days Calculations
        self.d_days = self.new_delta.days
        self.d_hours = self.d_days * 24
        self.d_mins = self.d_days * 1440
        self.d_seconds = self.d_days * 86400
        self.d_micros = self.d_seconds * 1000000
        self.d_weeks = self.d_days / 7
        self.d_months = self.d_days / 30
        self.d_years = self.d_days / 365

        # Day Bits
        self.d_secs = self.new_delta.seconds
        self.d_mics = self.new_delta.microseconds
        self.m_seconds = self.d_mics / 1000000
        self.s_micros = self.d_secs * 1000000

        # Total Day Bits
        self.s_seconds = self.d_secs + self.m_seconds
        self.m_micros = self.d_mics + self.s_micros
        self.s_mins = self.s_seconds / 60
        self.s_hours = self.s_mins / 60
        self.s_days = self.s_hours / 24
        self.s_weeks = self.s_days / 7
        self.s_months = self.s_days / 30
        self.s_years = self.s_days / 365

    @property
    def microseconds(self):
        total = self.d_micros + self.m_micros
        return total

    @property
    def seconds(self):
        total = self.d_seconds + self.s_seconds
        return total
    
    @property
    def minutes(self):
        total = self.d_mins + self.s_mins
        return total

    @property
    def hours(self):
        total = self.d_hours + self.s_hours
        return total

    @property
    def days(self):
        total = self.d_days + self.s_days
        return total

    @property
    def weeks(self):
        total = self.d_weeks + self.s_weeks
        return total

    @property
    def months(self):
        total = self.d_months + self.s_months
        return total

    @property
    def years(self):
        total = self.d_years + self.s_years
        return total

    @property
    def natural(self):
        overall_mins = whenWasThat(self.time_then,self.time_now).minutes
        whenData = pd.DataFrame({'in_minutes':[overall_mins]})
        # 0, 1 min, 2 hours, 2 days, 2 weeks, 2 months, 2 years
        bins = [0,1,120,2880,20160,87660,1051920,float("inf")]
        secs = "%s seconds ago" % self.new_delta.seconds # 0-2
        mins = "Approximately %s minutes ago" % round(self.s_mins) # overall_mins # 2-59
        hours = "Approximately %s hours ago" % round(self.s_hours) # 59-1440
        days = "Approximately %s days ago" % self.d_days # 1440-10080
        weeks = "Approximately %s weeks ago" % round(self.d_weeks,1) # 10080-43830
        months = "Approximately %s months ago" % round(self.d_months,1) # 43830-525949
        years = "Approximately %s years ago" % round(self.d_years,1) # 525949-inf
        labels = [secs,mins,hours,days,weeks,months,years]
        whenData['when'] = pd.cut(whenData['in_minutes'], bins=bins, labels=labels, include_lowest=True)
        whenDict = whenData.to_dict()
        when = whenDict.get('when')
        return when.get(0)