def congress():
    age = int(input("Enter your age: ")
    citizen_years = int(input("Enter your years as a US citizen: ")

    if age >= 30 and citizen_years >= 9:
        print("You can run for the House and Senate")
    elif age >=25 and citizen_years >= 7:
        print("You can only run for the House")
    else:
        print("You can run for neither chamber")

congress()
