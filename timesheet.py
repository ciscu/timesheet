from datetime import datetime
import calendar
import math

timesheet = {datetime(2021, 10, 1): 8, datetime(2021, 10, 7): 8, datetime(2021, 10, 8): 8, datetime(2021, 10, 9): 8}

def print_calendar(timesheet, year=datetime.now().year, month=datetime.now().month,):
    days_in_month = calendar.monthrange(year, month)[1]
    starting_day =  datetime(year, month, 1).strftime("%a")
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    offset = {days_of_week[i]: i for i in range(7)}
    weeks = math.ceil((days_in_month + offset[starting_day]) / 7)

    counter = 0
    present_day = 1
    for week in range(weeks):
        for day in days_of_week:
            if present_day <= days_in_month:
                if counter == offset[starting_day] or present_day >1:
                    today = datetime(year, month, present_day)
                    if today in timesheet:
                        print("|{}-{}/{}: {}\t".format(day, present_day, month, timesheet[today]), end="")
                    else:
                        print("|{}-{}/{} \t".format(day, present_day, month), end="")
                    present_day += 1
                else:
                    print("|{} \t\t".format(day), end="")
                counter += 1
            else:
                print("|{} \t\t".format(day), end="")
        print()


print_calendar(timesheet, 2021, 10)
