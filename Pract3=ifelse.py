
#Implimentation
#Q1
a=int(input("Enter a number:"))
if a%2==0:
        print("Number is even")
else:
    print("Number is odd")
print("----------------------------------------------")

#Q2      
if a>0:
    print("Number is positive")
    if a%2==0:
        print("Number is even")
    else:
        print("Number is odd")
elif a<0:
    print("Number is negative")
else:
    print("Number is zero")
print("----------------------------------------------")

#Q3
marks=int(input("Enter your marks:"))
if marks>89:
    print("grade A")
elif marks>79:
    print("Grade B")
elif marks>69:
    print("Grade C")
else:
    print("Fail")
print("----------------------------------------------")

#Q4
year=int(input('Enter a year:'))
if(year%4==0):
    print(f"{year} is a leep year")
else:
    print(f"{year}Not a leep year")
print("----------------------------------------------")

#Q5
age=int(input("Enter your age:"))
if age>=18:
    print("you can voat")
    if age<60:
        print('you are not eligible for senior citizen')
    else:
        print('you are eligible for senior citizen')
else:
    print("You are not eligible for voat")
    
print("----------------------------------------------")


#post experiment exerxise

#Q1
a=int(input("Enter a number:"))
if a%3==0 and a%5==0:
        print("Number is multiple of both 3 and 5 ")
else:
        print("Number is  Not multiple of both 3 and 5 ")
        
print("----------------------------------------------")

#Q2
temp=int(input("Enter temperature in celsius:"))
if temp<15:
        print("Cold")
elif temp>15 and temp<30:
        print("Moderate")
else:
        print("Hot")
print("----------------------------------------------")

#Q3 
char=input("Enter a charecter: ")
if 'a'==char or 'e'==char or 'i'==char or 'o'==char or 'u'==char :
        print("Entered charecter is a vowel")
elif 'A'==char or 'E'==char or 'I'==char or 'O'==char or 'U'==char :
        print("Entered charecter is a vowel")
else:
        print("Entered charecter is consonant")
print("----------------------------------------------")


"""
___________________OUTPUT_____________________
Enter a number:1
Number is odd
----------------------------------------------
Number is positive
Number is odd
----------------------------------------------
Enter your marks:95
grade A
----------------------------------------------
Enter a year:2024
2024 is a leep year
----------------------------------------------
Enter your age:65
you can voat
you are eligible for senior citizen
----------------------------------------------
Enter a number:15
Number is multiple of both 3 and 5 
----------------------------------------------
Enter temperature in celsius:18
Moderate
----------------------------------------------
Enter a charecter: a
Entered charecter is a vowel
----------------------------------------------
"""

        







    
