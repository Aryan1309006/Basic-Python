#Q1
def get_integer():
    try:
        user_input=input("Enter an integer: ")
        user_input=int(user_input)
        print(f"You entered the integer:{user_input}")
    except ValueError:
        print("This is a not a valid integer,Please try again !")

get_integer()

#Q2
try:
    num1=input("Enter the first nummber: ")
    num2=input("Enter the second nummber: ")
    num1=float(num1)
    num2=float(num2)
    print(f"You entered the integer are num1:{num1} and num2: {num2}")
except ValueError:
    raise TypeError("Both input must be numarical Please enter a valid numarical")
#Q3
def Text_index(data,index):
    try:
        result=data[index]
        print("result",result)
    except IndexError:
        print("Error:Index of range")
nums=[1,2,3,4,5,6,7]
index=int(input("Input index:"))
Text_index(nums,index)
#Q4
try:
    n=int(input("Input a number:"))
    print("You entered :",n)
except KeyboardInterrupt:
    print("Error: Input cancled by the user")
#Q5
def division(dividend, divisor):
    try:
        result=dividend/divisor
        print("Result",result)
    except ArithmeticError:
        print("Error: Arithmatic error occured!")
dividend=float(input("Input the dividend: "))
divisor=float(input("Input the divisor: "))
division(dividend,divisor)
#Q6
def simulate_attribute_error(list):
    my_string="Hello world"
    try:
        my_string.append("welocome")
    except AttributeError:
        print("Error: Invalid attribute")

simulate_attribute_error()