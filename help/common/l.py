from help.common.m import M
from datetime import datetime, date, timedelta

class L(M):
    def n_days_back_date(self, n_days=10):
        return self.get_today_date() - timedelta(days=n_days)
    
    def n_days_back_datetime(self, n_days=10, zone='utc'):
        today_datetime = self.get_today_datetime(zone=zone)
        print('today_datetime ', today_datetime)
        return today_datetime - timedelta(days=n_days)