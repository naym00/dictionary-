from help.common.n import N
from datetime import datetime, date, timedelta

class M(N):
    def get_today_date(self):
        return date.today()
    
    def get_today_datetime(self, zone='utc'):
        return datetime.now(tz=self.get_timezone(zone=zone))