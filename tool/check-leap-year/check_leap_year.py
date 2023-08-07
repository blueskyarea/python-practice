def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

if __name__ == '__main__':
    try:
        year = int(input("Enter a year to check if it's a leap year: "))
        if is_leap_year(year):
            print("{} is a leap year.".format(year))
        else:
            print("{} is not a leap year.".format(year))
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
