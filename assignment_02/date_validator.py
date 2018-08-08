def is_leap(year):
    leap = False
    if year %4 == 0:
        if year % 100 != 0 or year% 400 == 0:
            leap = true
    return leap

def date_checker():
    is_valid = True
    thirty_one_months = [1, 3, 5, 7, 8, 10, 12]
    date = input("Please enter a date in XX/XX/XXXX format: ")

    date_list = date.split('/')
    if len(date_list) != 3:
        is_valid = False
    else:
        month, day, year = date_list

        try:
            month = int(month)
            day = int(day)
            year = int(year)

            if month > 12 or month < 1 or day > 31 or day < 1 or year < 1:
                is_valid = False
            elif month not in thirty_one_months and day == 31:
                is_valid = False

            if is_leap(year) and month == 2 and day == 30:
                is_valid = False
            elif not is_leap(year) and month == 2 and day > 28:
                is_valid = False
        except:
            is_valid = False

    if is_valid:
        print("Valid Date")
    else:
        print("Not Valid Date")

date_checker()
