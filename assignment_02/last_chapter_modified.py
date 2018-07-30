#This was taken from assignment 1
def temp():
    celsius = float(input("What is your tempurature in celsius: ")
    fahrenheit = ((9/5)*celsius) + 32
    print("The tempurature is", farenheit, "degrees Fahrenheit.")

    if fahrenheit > 90:
        print("Heat advisory in effect")
    if fahrenheit < 30:
        print("Wind chill warning")

temp()
