import datetime

#event = {}
#event["date"] = str(datetime.date(e_year,e_month,e_day))
#event["created"] = str(datetime.date.today())


dx = datetime.timedelta(5)
print(dx)
dx = str(dx)
print(dx)

# convert dx back to timedlta type
print(dx.split()[0])
days = int(dx.split()[0].replace('days', ''))
timedelta_back = datetime.timedelta(days=days)
print(timedelta_back)

