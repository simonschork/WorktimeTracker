import datetime
from string import Template


# Returns currend datetime
def current():
    return datetime.datetime.now()


# Returns string "h:m.s" for log
def formatTime(datetime):
    return datetime.strftime("%H:%M:%S")


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    d["H"], rem = divmod(tdelta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)
