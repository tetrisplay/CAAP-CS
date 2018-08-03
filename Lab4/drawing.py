# Christina Tetrick
# Lab 4
# 8/5/18

# Imports the turtle graphics module
import turtle
 
# creates a turtle (pen) an sets the speed (where 0 is fastest and 10 is slowest)
# The colors can be set through their names or through hexadecimal codes, use hex for accuracy
myPen = turtle.Turtle()
myPen.speed(0)
myPen.color("#000000")
turtle.delay(0)

# setting out box sizes to the n sq pixels per box
boxSize = 10
 

# myPen.setheading(n) points pen to given angle direction.
# where n queals the angle.
# 0 points to the right, 90 to go up, 180 to go to the left 270 to go down

# Positions myPen in top left area of the screen
# This should change according to the image size you want to make and the size of your boxes ("pixels")
# This canvas is currently set to 200*200 pixels or a 20x20 box of 10 sq pixels each
myPen.penup()
myPen.forward(-100)
myPen.setheading(90)
myPen.forward(100)
myPen.setheading(0) 

# This function draws a box by drawing each side of the square and using the fill function
def box(intDim):
    myPen.begin_fill()
    # 0 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 90 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 180 deg.
    myPen.forward(intDim)
    myPen.left(90)
    # 270 deg.
    myPen.forward(intDim)
    myPen.end_fill()
    myPen.setheading(0)       

# Here is an example of how to draw a box using the box function      
# Comment this out when you draw your own images
box(boxSize)
 

# Challenge functions (2 bonus pts each) 
# You need to make shapes with each
#def circle(intRadius):
#def triangle(intLength): #This can be an equilateral triangle
#def save_image(): # saves the screen to an image/vector file

# These are the instructions on how to move "myPen" around after drawing a box.
# penup() lifts the pen so it doesn't draw anything and can be moved freely
# pendown() puts the oen down and it draws as it moves
# myPen.penup()
# myPen.forward(boxSize)
# myPen.pendown()
 
# You will save your drawings as lists.
# This first list stores the color values
pallet_1 = ["#FFFFFF" , "#FFFF00" , "#000000" , "#61380B" , "#F4FA58"]
# Your drawings are stored using a "list of lists" where each value within every list
# element is the index of the color in the pallet list
# Banana
pixels_1 = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,2,2,3,3,2,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,4,1,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,4,1,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,4,1,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,1,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,2,4,4,1,2,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,2,4,1,1,2,2,2,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,2,4,1,3,2,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_1.append([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

# Mario
pallet_2 = ["#4B610B" , "#FAFAFA" , "#DF0101" , "#FE9A2E"]
pixels_2 = [[1,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1]]
pixels_2.append([1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,1])
pixels_2.append([1,1,1,0,0,0,3,3,3,3,3,0,3,1,1,1])
pixels_2.append([1,1,0,3,0,3,3,3,3,3,3,0,3,3,3,1])
pixels_2.append([1,1,0,3,0,0,3,3,3,3,3,3,0,3,3,3])
pixels_2.append([1,1,0,0,3,3,3,3,3,3,3,0,0,0,0,1])
pixels_2.append([1,1,1,1,3,3,3,3,3,3,3,3,3,3,1,1])
pixels_2.append([1,1,1,0,0,2,0,0,0,0,2,0,1,1,1,1])
pixels_2.append([1,1,0,0,0,2,0,0,0,0,2,0,0,0,1,1])
pixels_2.append([0,0,0,0,0,2,2,2,2,2,2,0,0,0,0,0])
pixels_2.append([3,3,3,0,2,3,2,2,2,2,3,2,0,3,3,3])
pixels_2.append([3,3,3,3,2,2,2,2,2,2,2,2,3,3,3,3])
pixels_2.append([3,3,3,2,2,2,2,1,1,2,2,2,2,3,3,3])
pixels_2.append([1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1])
pixels_2.append([1,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1])
pixels_2.append([0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,10])

# Ghost
pallet_3 = ["red","white","blue"]
pixels_3 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
pixels_3.append([1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1])
pixels_3.append([1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1])
pixels_3.append([1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1])
pixels_3.append([1,1,0,0,1,1,1,1,0,0,1,1,1,1,1,1,1])
pixels_3.append([1,1,0,0,1,1,2,2,0,0,1,1,2,2,1,1,1])
pixels_3.append([1,0,0,0,1,1,2,2,0,0,1,1,2,2,0,1,1])
pixels_3.append([1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,1,1])
pixels_3.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])
pixels_3.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])
pixels_3.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])
pixels_3.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])
pixels_3.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1])
pixels_3.append([1,0,0,1,0,0,0,1,1,0,0,0,1,0,0,1,1])
pixels_3.append([1,0,1,1,1,0,0,1,1,0,0,1,1,1,0,1,1])

#Shroom
pallet_4 = ["black","red","white"]
pixels_4 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
pixels_4.append([2,2,2,2,2,0,0,0,0,0,0,2,2,2,2,2,2,2])
pixels_4.append([2,2,2,0,0,1,1,1,1,2,2,0,0,2,2,2,2,2])
pixels_4.append([2,2,0,2,2,1,1,1,1,2,2,2,2,0,2,2,2,2])
pixels_4.append([2,0,2,2,1,1,1,1,1,1,2,2,2,2,0,2,2,2])
pixels_4.append([2,0,2,1,1,2,2,2,2,1,1,2,2,2,0,2,2,2])
pixels_4.append([0,1,1,1,2,2,2,2,2,2,1,1,1,1,1,0,2,2])
pixels_4.append([0,1,1,1,2,2,2,2,2,2,1,1,2,2,1,0,2,2])
pixels_4.append([0,2,1,1,2,2,2,2,2,2,1,2,2,2,2,0,2,2])
pixels_4.append([0,2,2,1,1,2,2,2,2,1,1,2,2,2,2,0,2,2])
pixels_4.append([0,2,2,1,1,1,1,1,1,1,1,1,2,2,1,0,2,2])
pixels_4.append([0,2,1,1,0,0,0,0,0,0,0,0,1,1,1,0,2,2])
pixels_4.append([2,0,0,0,2,2,0,2,2,0,2,2,0,0,0,2,2,2])
pixels_4.append([2,2,0,2,2,2,0,2,2,0,2,2,2,0,2,2,2,2])
pixels_4.append([2,2,0,2,2,2,2,2,2,2,2,2,2,0,2,2,2,2])
pixels_4.append([2,2,2,0,2,2,2,2,2,2,2,2,0,2,2,2,2,2])
pixels_4.append([2,2,2,2,0,0,0,0,0,0,0,0,2,2,2,2,2,2])

#Alien

pallet_5 = ["pink","white","light grey"]
pixels_5 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
pixels_5.append([1,1,1,1,2,2,1,1,1,1,1,1,1,1,1,1,2,2,1,1,1,1,1])
pixels_5.append([1,1,1,1,2,0,0,1,1,1,1,1,1,1,1,1,2,0,0,1,1,1,1])
pixels_5.append([1,1,1,1,1,0,0,2,1,1,1,1,1,1,2,2,1,0,0,1,1,1,1])
pixels_5.append([1,1,1,1,1,1,2,0,0,1,1,1,1,1,2,0,0,1,1,1,1,1,1])
pixels_5.append([1,1,1,1,2,2,2,0,0,2,2,2,2,2,2,0,0,2,1,1,1,1,1])
pixels_5.append([1,1,1,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1])
pixels_5.append([1,1,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,1,1,1])
pixels_5.append([1,1,2,0,0,0,0,1,2,0,0,0,0,0,0,1,2,0,0,0,0,1,1])
pixels_5.append([2,2,2,0,0,0,0,2,2,0,0,0,0,0,0,2,2,0,0,0,0,2,1])
pixels_5.append([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_5.append([2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
pixels_5.append([2,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0])
pixels_5.append([2,0,0,1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,0,0])
pixels_5.append([2,0,0,1,2,0,0,1,1,1,1,1,1,1,1,1,2,0,0,1,2,0,0])
pixels_5.append([1,0,0,1,1,0,0,2,2,2,1,1,2,2,2,2,1,0,0,1,1,0,0])
pixels_5.append([1,1,1,1,1,1,2,0,0,0,0,1,2,0,0,0,0,1,1,1,1,1,1])
pixels_5.append([1,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1,1,1,1])

#Smiley

pallet_6 = ["yellow","black","white","brown","pink"]
pixels_6 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
pixels_6.append([2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2])
pixels_6.append([2,2,2,2,2,2,2,2,2,2,1,1,1,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2,2,2])
pixels_6.append([2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2,2,2])
pixels_6.append([2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2])
pixels_6.append([2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2])
pixels_6.append([2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2])
pixels_6.append([2,2,2,1,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,2,2,2])
pixels_6.append([2,2,2,1,0,0,1,1,1,1,2,1,0,0,0,0,0,0,0,1,1,1,2,2,1,0,0,1,2,2,2])
pixels_6.append([2,2,1,0,0,1,1,1,1,1,2,2,1,0,0,0,0,0,1,1,1,1,2,2,2,1,0,0,1,2,2])
pixels_6.append([2,2,1,0,0,1,1,1,1,1,2,2,1,0,0,0,0,0,1,1,1,1,2,2,2,1,0,0,1,2,2])
pixels_6.append([2,1,0,0,0,1,1,1,1,2,2,2,1,0,0,0,0,0,1,1,1,2,2,2,2,1,0,0,0,1,2])
pixels_6.append([2,1,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,1,2])
pixels_6.append([2,1,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,1,2])
pixels_6.append([1,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,1,2,2,2,2,2,2,2,2,1,0,0,0,1])
pixels_6.append([1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1])
pixels_6.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
pixels_6.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
pixels_6.append([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
pixels_6.append([2,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,1,2])
pixels_6.append([2,1,0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,1,2])
pixels_6.append([2,1,0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,1,2])
pixels_6.append([2,2,1,0,0,1,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,1,0,0,1,2,2])
pixels_6.append([2,2,1,0,0,1,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,3,3,3,3,1,0,0,1,2,2])
pixels_6.append([2,2,2,1,0,0,1,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,3,3,1,0,0,1,2,2,2])
pixels_6.append([2,2,2,1,0,0,0,1,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,1,0,0,0,1,2,2,2])
pixels_6.append([2,2,2,2,1,0,0,0,1,1,3,3,3,3,3,4,4,4,4,4,4,1,1,0,0,0,1,2,2,2,2])
pixels_6.append([2,2,2,2,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,2,2,2,2])
pixels_6.append([2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,2,2,2,2,2,2])
pixels_6.append([2,2,2,2,2,2,2,2,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,2,2,2,2,2,2,2,2])
pixels_6.append([2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2])

#Deadpool Head
pallet_7 = ["red","black","white","Light grey","grey"]
pixels_7 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
pixels_7.append([2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,1,1,2,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2])
pixels_7.append([2,2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,2])
pixels_7.append([2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2])
pixels_7.append([2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2])
pixels_7.append([2,2,2,2,2,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2])
pixels_7.append([2,2,2,2,2,1,0,0,0,0,0,4,3,3,0,0,0,0,0,3,1,2,2])
pixels_7.append([2,2,2,2,2,1,0,0,0,0,4,4,4,3,3,3,0,0,3,3,1,2,2])
pixels_7.append([2,2,2,2,2,2,1,0,0,0,4,4,2,2,3,3,0,0,3,3,1,2,2])
pixels_7.append([2,2,2,2,2,2,1,0,0,0,4,4,2,2,2,3,0,0,3,1,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,1,0,0,0,4,4,4,3,3,0,0,3,1,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,2,1,0,0,0,4,4,3,0,0,0,1,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,2,2,1,0,0,0,0,0,0,0,1,2,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,2,2,2,1,1,0,0,0,1,1,2,2,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,2,2,2,2,2,2,2,2])
pixels_7.append([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])

#Spiderman
pallet_8 = ["red","blue","white","black"]
pixels_8 = [[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]]
pixels_8.append([2,2,2,2,2,2,2,2,2,2,2,2,3,2,3,2,2,2,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,2,2,3,0,2,0,3,2,2,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,2,3,0,0,2,0,0,3,2,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,3,0,0,0,2,0,0,0,3,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,3,0,0,0,0,2,0,0,0,0,3,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,3,1,0,0,0,3,3,2,3,3,0,0,0,1,3,2,2,2,2])
pixels_8.append([2,2,2,2,2,3,1,1,1,0,3,1,1,2,1,1,3,0,1,1,1,3,2,2,2])
pixels_8.append([2,2,2,2,3,1,1,1,1,3,3,3,2,2,2,3,3,3,1,1,1,1,3,2,2])
pixels_8.append([2,2,2,2,3,1,1,1,3,0,0,0,3,2,3,0,0,0,3,1,1,1,3,2,2])
pixels_8.append([2,2,2,2,2,3,3,3,0,0,0,0,3,0,3,0,0,0,0,3,3,3,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,0,1,3,0,0,0,3,1,0,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,3,0,0,1,3,1,0,0,0,1,3,1,0,0,3,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,3,0,0,3,1,0,0,3,0,0,1,3,0,0,3,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,3,3,0,0,3,3,3,0,0,3,3,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,2,3,3,0,0,0,3,3,2,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,3,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,0,3,3,0,0,0,3,3,0,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,3,2,2,3,0,3,2,2,3,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,3,2,3,0,0,0,3,2,3,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,3,3,0,0,0,0,0,3,3,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,3,0,0,0,0,0,0,0,3,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,0,0,3,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,3,3,0,0,0,0,0,3,3,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,2,2,2,2,2,2,2,2,2])
pixels_8.append([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2])


# This function takes a pallet and pixel list (matrix) to draw the picture
# You are to write this function
#Help from Jesus
def draw(pallet, pixels):
    myPen.setheading(0)
    for i in range(len(pixels)):
        for k in range(len(pixels[i])):
            myPen.penup()
            myPen.forward(boxSize)
            myPen.pendown()
            if pallet[pixels[i][k]] != "#FFFFFF":
                myPen.color(pallet[pixels[i][k]])
                box(boxSize)
        myPen.penup()
        myPen.forward(-1*len(pixels[0])*boxSize)
        myPen.setheading(270)
        myPen.forward(boxSize)
        myPen.setheading(0)
        

#prompts user for drawing choice then generates it
def main():
    
    print("What drawing do you want? Bannana: a, Mario: b, Ghost: c, Mushroom: d, Space Invader: e, Smiley: f, Deadpool: g, Spiderman: h.")
    print("Please switch to the graphics screen after you have made your choice.")
    ask = input("Please enter a letter: ")
    if ask == "a":
        draw(pallet_1, pixels_1)
    elif ask == "b":
        draw(pallet_2, pixels_2)
    elif ask == "c":
        draw(pallet_3, pixels_3)
    elif ask == "d":
        draw(pallet_4, pixels_4)
    elif ask == "e":
        draw(pallet_5, pixels_5)
    elif ask == "f":
        draw(pallet_6, pixels_6)
    elif ask == "g":
        draw(pallet_7, pixels_7)
    elif ask == "h":
        draw(pallet_8, pixels_8)
    else:
        return      
	# You need this to prevent the window from closing after drawing
    turtle.done()

main()
