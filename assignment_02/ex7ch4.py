from graphics import *
from math import sqrt

def previous():
    win = GraphWin('Circle Intersection Calulator', 300, 330)
    win.setCoords(-10, -12, 10 10)

    descr = Text(Point(0,0), 'This program calulates the x values of the intersection of a horizontal line and a circle.')

    click = Text(Point(0,-11), 'Click anywere to continue')
    descr.setSize(8)
    click.setSize(8)
    descr.draw(win)
    click.draw(win)

    win.getMouse()
    descr.undraw()

    rad_text = Text(Point(-5,5), 'Radius: ')
    int_text = Text(Point(-5,0), 'Y Intercept: ')
    rad_text.setSize(8)
    int_text.setSize(8)
    rad_text.draw(win)
    int_text.draw(win)
    rad_input = Entry(Point(0,5), 3)
    int_input = Entry(Point(0,0), 3)
    rad_input.setSize(8)
    int_input.setSize(8)
    rad_input.draw(win)
    int_input.draw(win)

    win.getMouse()
    radius = eval(rad_input.getText())
    intercept = eval(int_input.getText())
    rad_text.undraw()
    int_text.undraw()
    rad_input.undraw()
    int_input.undraw()
    click.undraw()

    if abs(intercept) <= radius:
        x_int1 = -sqrt(radius**2-intercept**2)
        x_int2 = sqrt(radius**2-intercept**2)

    x_axis = Line(Point(-10,0), Point(10,0))
    x_axis.setArrow('last')
    y_axis= Line(Point(0, -10), Point(0,10))
    y_axis.setArrow('last')
    circ = Circle(Point(0,0), radius)
    circ.setOutline('blue')
    line = Line(Point(-10, intercept), Point(10, intercept))
    line.setOutline('blue')
    x_axis.draw(win)
    y_axis.draw(win)
    circ.draw(win)
    line.draw(win)
    if abs(intercept) <= radius:
        int1 = Circle(Point(x_int1, intercept), 0.2)
        int1.setFill('red')
        int1.setOutline('red')
        int2 = Circle(Point(x_int2, intercept), 0.2)
        int2.setFill('red')
        int2.setOutline('red')
        int1.draw(win)
        int2.draw(win)

    if abs(intercept) <= radius:
        int_info = Text(Point(0, -11), 'x values of points of intersection:', x_int1 x_int2)

    elif abs(intercept) == radius:
        int_info = Text(Point(0, -11), 'x values of points of intersection: 0.0')

    else:
        int_info = Text(Point(0, -11), 'There are no points of intersection')

    int_info.setSize(8)
    int_info.draw(win)

    win.getMouse()
    win.close()

previous()
