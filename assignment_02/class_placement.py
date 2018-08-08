def class_placement():
    credit = int(input("Please enter total number of credits: ")

    if credit < 7:
        year = 'Freshman'
    elif credit < 16:
        year = 'Sophomore'
    elif credit < 26:
        year = 'Junior'
    else:
        year = 'Senior'
    print( "Your class is", year)

class_placement()
