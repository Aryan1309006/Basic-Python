#WAP to find sum and average of a given list by creating a custom function.
list1=[1,2,3,4,5]
def sumavg(x):
    sum=0
    avg=0
    for i in range(0,5):
        sum=sum+list1[i]
        avg=sum/5
    print(f"Sum:{sum}")
    print(f"Avarage:{avg}")   
sumavg(list1)
print("----------------------------------------------------------------")
#WAP to find a^b for the given a and b using recursion.
base= int(input("Enter a Base: "))
power = int(input("Enter a Power: "))

def pow(x, y):
    if y == 0:
        return 1 
    else:
        return x * pow(x, y - 1)  

result = pow(base,power)
print(f"{base} to power {power} is {result}")
print("----------------------------------------------------------------")
#Write a python code to illustrate the cube of a number using lambda function
x=int(input("enter base:"))
a=lambda x:x**3
print("cube is ",a(x))
print("----------------------------------------------------------------")

#WAP to double each element of the given list using map().
def double(x):
    return x*2
num=[1,2,3,4,5]
double_number=list(map(double,num))
print("origmal list: ",num)
print("Double list: ",double_number)
print("----------------------------------------------------------------")

#Write a program to show use of a filter() in python
def is_even(number):
    return number%2==0
number=[1,2,3,4,5]
even_number=list(filter(is_even,number))
print("Orignal list: ",number)
print("Filtered even number:",even_number)
print("----------------------------------------------------------------")

'''
----------------------------OUTPUT------------------------------
Sum:15
Avarage:3.0
----------------------------------------------------------------
Enter a Base: 10
Enter a Power: 2
10 to power 2 is 100
----------------------------------------------------------------
enter base:3
cube is  27
----------------------------------------------------------------
origmal list:  [1, 2, 3, 4, 5]
Double list:  [2, 4, 6, 8, 10]
----------------------------------------------------------------
Orignal list:  [1, 2, 3, 4, 5]
Filtered even number: [2, 4]
----------------------------------------------------------------
'''