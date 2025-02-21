#Q1. WAP to to find factors of a given number
a=int(input("Enter a number: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(f"Factorial of the number {a} is ",fact)
print("-----------------------------------------------------------------")
#Q2. WAP to print first n prime numbers where n is given by user.
n=int(input("enter no of prime number to be displayed:"))
count=1
j=2
while(count<=n):
    for i in range(2,n):
        if(j%i==0):
            break
    else:
        print(j)
        count=count+1
    j=j+1
print("-----------------------------------------------------------------")   
#Q3. WAP to check the given number is perfect number or not
n=int(input("Enter a number: ")) 
sum=0 
for i in range(1,n,1): 
    if(n%i==0): 
        sum=sum+i 
if(sum==n): 
    print("the number is perfect number") 
else: 
    print("the number is not perfect number") 
print("-----------------------------------------------------------------")
#Q4WAP to print prime numbers in the range given by user
lower=eval(input("Enter a lower range: ")) 
upper=eval(input("Enter a upper range: ")) 
for n in range(lower,upper + 1): 
   if n > 1: 
       for i in range(2,n): 
           if (n % i) == 0: 
               break 
       else: 
           print(n)
print("-----------------------------------------------------------------")
#Post experiment exercise
#Write down the accurate output for following code:
adj = ["red","big", "shiny"]
fruits = ["car", "wall","rose"]
for x in adj:
    for y in fruits:
        print(x, y)
print("-----------------------------------------------------------------")

"""
_______________________________OUTPUT____________________________
Enter a number: 5
Factorial of the number 5 is  120
-----------------------------------------------------------------
enter no of prime number to be displayed:5
5
7
11
13
17
-----------------------------------------------------------------
Enter a number: 6
the number is perfect number
-----------------------------------------------------------------
Enter a lower range: 10
Enter a upper range: 20
11
13
17
19
-----------------------------------------------------------------
red car
red wall
red rose
big car
big wall
big rose
shiny car
shiny wall
shiny rose
-----------------------------------------------------------------
"""

