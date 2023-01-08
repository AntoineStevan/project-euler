#! /usr/bin/env python3

def is_leap_year(year: int) -> bool:
    """ Tells if a given year is a leap one. """
    return True if year % 400 == 0 else (year % 4 == 0 and year % 100 != 0)


def other(year):
    if year % 4 != 0: return False
    if year % 100 != 0: return True
    if year % 400 != 0: return False
    return True


def next_day(date: [int, str, int]) -> [int, str, int]:
    """ Computes the next day. """
    day = date["day"]
    month = date["month"]
    year = date["year"]

    day += 1
    if day > months[month][is_leap_year(year)]:
        day = 1
        month = months[month][2]
        if month == "jan":
            year += 1

    return dict(day=day, month=month, year=year, day_of_the_week=(date["day_of_the_week"] + 1) % 7)


def same_date(d1, d2):
    return d1["day"] == d2["day"] and d1["month"] == d2["month"] and d1["year"] == d2["year"]


months = dict(
    jan=(31, 31, "feb"), feb=(28, 29, "mar"), mar=(31, 31, "apr"),
    apr=(30, 30, "mai"), mai=(31, 31, "jun"), jun=(30, 30, "jul"),
    jul=(31, 31, "aug"), aug=(31, 31, "sept"), sept=(30, 30, "oct"),
    oct=(31, 31, "nov"), nov=(30, 30, "dec"), dec=(31, 31, "jan")
)

date = dict(day=1, month="jan", year=1900, day_of_the_week=0)
end = dict(day=31, month="dec", year=2000)

count = 0
do_count = False

while not same_date(date, end):
    date = next_day(date)

    if same_date(date, dict(day=1, month="jan", year=1901)):
        do_count = True

    if do_count:
        if date["day"] == 1 and date["day_of_the_week"] == 6:
            count += 1

print(count)
