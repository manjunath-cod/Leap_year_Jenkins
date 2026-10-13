import sys

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
if __name__ == "__main__":
    y = 2024
    print(f"{y} is leap year? {is_leap_year(y)}")
    print(sys.argv[1])
    print(sys.argv[0])