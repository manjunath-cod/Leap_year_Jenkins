import sys

def is_leap_year(year):
    if (year %4 == 0):
       return "Leap year"
    else:
        return "Not a leap year"
year = int(sys.argv[1])
is_leap_year(year)