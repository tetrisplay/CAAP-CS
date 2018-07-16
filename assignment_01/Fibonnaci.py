#The purpose of this function is to calculate the nth term of the Fibonnaci sequence.The function for fib was found onhttps://stackoverflow.com/questions/494594/how-to-write-the-fibonacci-sequence#  
from math import sqrt
def Fibonnaci():
    n = int(input("What is the nth term that you are looking for? The nth term must be greater than 2 "))
    fib = int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))
    print("Your nth term is",fib)

Fibonnaci()


