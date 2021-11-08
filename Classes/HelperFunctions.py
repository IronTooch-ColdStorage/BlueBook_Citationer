import time
import datetime


def getDate(strDate: str) -> time.struct_time:
    for fmt in ('%B %d, %Y', '%b %d, %Y'):
        try:
            return time.strptime(strDate, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')