""" content of sample.py
sample_variable="This is the string variable in the sample.py"
def say_hello():
    name=input("Enter your name:")
    print(f"Welcome {name}")
def add():
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print(f"addition:{a+b}")
"""

import sample as sp
print(sp.sample_variable) #Q1
sp.say_hello()  #Q2
sp.add()    #Q3
#---------------------------------------------------------------------
import math
import random
a=float(input("Enter a number: "))  #Q1
print(math.sqrt(a)) 
print(f"factorial of 5 is :{math.factorial(5)}")   #Q2
print(math.pi)  #Q3
print(f"randome int is: {random.randint(1,100)}")   #Q4
print(f"randome no between 0 and1 is {random.random()}")    #Q5
#---------------------------------------------------------------------

"""Content of math_opration.py
def add(a,b):
    print(f"addition : {a+b}")

def multiply(a,b):
    print(f"multiplication: {a*b}")
-----------------------------------------------------
string_operation.py :
def uppercase(text):
    print(f"upper case of string {text} is {text.upper()}")

def reverse_string(text):
    print(f"reverse of string is {text[::-1]}")
"""
import mypackage.math_opration as mo
import mypackage.string_operation as so

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

mo.add(a,b)
mo.multiply(a,b)

str=input("Enter a string: ")
so.uppercase(str)
so.reverse_string(str)
"""  output
This is the string variable in the sample.py
Enter your name:Aryan
Welcome Aryan
Enter first number:10
Enter second number:20
addition:30

Enter a number: 10
3.1622776601683795
factorial of 5 is :120
3.141592653589793
randome int is: 38
randome no between 0 and1 is 0.7814152393921633


Enter first number: 10
Enter second number: 20
addition : 30
multiplication: 200
Enter a string: Aryan
upper case of string Aryan is ARYAN
reverse of string is nayrA

"""