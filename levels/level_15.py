from datetime import datetime, timedelta
import calendar


# Level url: http://www.pythonchallenge.com/pc/return/uzi.html
# Level title: "whom?"
# Image is a calendar
# January 1*6 (a whole torn out covering digist betwee 1 and 6)
# Circle around Monday 26th January
# What year is this from? 1**6? 1066?
# Image url: screen15.jpg

# Comments from html:
# <!-- he ain't the youngest, he is the second -->
# <!-- todo: buy flowers for tomorrow -->

# Reference to a King, second of his name?
# Buy flowers for 27th Jan - what is this?

# To determine the year, we need to find all dates where 26th Jan 
# Is a Monday, when the year starts with 1 and ends with 6

# Who was a king, 2nd of their name at this time? OR second youngest sibling at the time?

# February 29th is on the calendar - leap year.

def is_monday(date):
    return date.weekday() == 0


def is_january(date):
    return date.month == 1


def is_26th_of_month(date):
    return date.day == 26


def year_match(date):
    year_str = date.strftime("%Y")
    return (year_str.startswith("1") or year_str.startswith("01") or year_str.startswith("001")) and year_str.endswith("6")


def is_leap_year(year):
    return calendar.isleap(year)


def loop_over_dates(start_date, end_date):
    # Convert strings to datetime objects
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")

    # Loop through all dates in the range
    current_date = start_date

    while current_date <= end_date:
        year = current_date.year
        if is_leap_year(year):
            if year_match(current_date):
                if is_monday(current_date):
                    if is_january(current_date):
                        if is_26th_of_month(current_date):
                            print(current_date.strftime("%Y-%m-%d"))
        current_date += timedelta(days=1)


def main():
    loop_over_dates("0001-01-01", "2024-10-24")


if __name__ == "__main__":
    main()
