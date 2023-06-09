from django import template
from accounts.models import userTimeZone

import pytz

register = template.Library()

def translate_date(date, requestUser):
    user_timezone, __ = userTimeZone.objects.get_or_create(user = requestUser)
    user_timezone = user_timezone.timeZone

    localtz = pytz.timezone(user_timezone)   #Get real local TimeZone

    date = date.replace(tzinfo=pytz.utc).astimezone(localtz)
    date = localtz.normalize(date)

    return date.strftime('%Y-%m-%d %H:%M')

register.filter('translate_date', translate_date)