#for this program I worked with Kevin Song to get the answer 
def change():
    change = float("What amount of money would you like change for? ")
     q = .25
     d = .10
     n = .05
     p = .01
     x = 0

     while change - q >= 0:
         change = change - q
         x += 1
     while change - d >= 0:
         change = change - d
         x += 1
     while change - n >= 0:
         change = change - n
         x += 1
     while change - p >= 0:
         change = change - p
         x += 1
     print("You will get", x "coins.")

change()
         
