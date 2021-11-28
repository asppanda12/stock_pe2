
from datetime import date
def numOfDays(date1, date2):
    return (date2-date1).days



date1 = date(2018, 12, 13)
date2 = date(2020, 2, 25)


print(numOfDays(date1,date2))