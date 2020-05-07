import datetime
from string import Template

# Returns currend datetime
def current():
    return datetime.datetime.now()


# Returns string "h:m.s" for log
def formatTime(datetime):
    return datetime.strftime("%H:%M:%S")


# Returns string "d/m/y" for log
def formatDate(datetime):
    return datetime.strftime("%d/%m/%Y")


def getTime():
    return formatTime(current())


class DeltaTemplate(Template):
    delimiter = "%"


def strfdelta(tdelta, fmt):
    d = {"D": tdelta.days}
    d["H"], rem = divmod(tdelta.seconds, 3600)
    d["M"], d["S"] = divmod(rem, 60)
    t = DeltaTemplate(fmt)
    return t.substitute(**d)
