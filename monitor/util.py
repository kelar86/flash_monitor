import pytz
from datetime import *


def date_expiered(date):
    utc = pytz.utc
    _date = date.replace(tzinfo=utc)
    now = datetime.utcnow().replace(tzinfo=utc)
    return now > _date
