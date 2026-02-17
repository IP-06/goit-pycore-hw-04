# Task 1
from datetime import datetime

date = input("Enter Year-month-day: ")
date_object = datetime.strptime(date, "%Y-%m-%d")


def get_days_from_today(date_object):
    real_date = datetime.today()
    result = real_date - date_object
    return(result.days)
    
print(get_days_from_today(date_object))