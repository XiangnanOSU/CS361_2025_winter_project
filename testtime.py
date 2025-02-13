import datetime

e_date = input("Event dates (yyyy-mm-dd): ")
print(e_date)
e_date = e_date.split('-')
e_year = int(e_date[0])
e_month = int(e_date[1])
e_day = int(e_date[2])
print(e_year)
t3 = datetime.date(e_year,e_month,e_day)
print(t3)