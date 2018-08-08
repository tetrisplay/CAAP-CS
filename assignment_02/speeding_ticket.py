def speeding():
    limit = int(input("Please enter the speed limit: "))
    speed = int(input("Please enter your speed"))

    if speed <= limit:
        print(" You were driving legally")
    if speed > limit and speed < 90:
        fine = 50 + (speed - limit)*5
        print( "Your speeding ticket will cost", fine)
    elif speed > limit and speed > 90:
        badfine = 250 + (speed - limit)*5
        print( "Your speeding ticket will cost", badfine)
    else:
        superbadfine = 250 + (speed - limit)*5
        print( "Your speeding ticket will cost", superbadfine)

speeding()
