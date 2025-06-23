from django.core.mail import EmailMessage
from datetime import datetime, date, timedelta
from help.common.o import O
import pytz

class N(O):
    def get_timezone(self, zone='utc'):
        time_zone = None
        if zone == 'utc': time_zone = pytz.UTC
        else:
            try: time_zone = pytz.timezone(zone)
            except: pass
        return time_zone
    
    def list_to_tuple(self, demo_list):
        return tuple(map(lambda a: (a, a), demo_list))
    
    def get_unique_code(self):
      return f"{datetime.now().strftime('%Y%m%d%H%M%S%f')}"[:18]
  
    def get_settings(self, Settings):
        settings = Settings.objects.all()
        if settings.exists(): return settings.first()
        else: return None
    
    def send_mail_including_attatchment(self, subject, message, recipient_list, attachments=[], email_from = None):
        flag = False
        try:
            email = EmailMessage(subject, message, email_from, recipient_list)
            for attachment in attachments:
                email.attach_file(attachment)
            flag = bool(email.send())
        except: flag = False
        return flag
    
    