"""
content of file "file.txt"
Hey
My name is Aryan
I study in SFIT
"""
#Q1
f=open('file.txt','r')
print(f.read())
f.close()
#Q2
print("-------------------------------------------------------------------------")
n=int(input("Enter a number of lines:"))
f=open('file.txt','r')
lines=f.readlines()
for t in lines[:n]:
    print(t)
f.close()
#Q3
print("-------------------------------------------------------------------------")
f=open('file.txt','a')
l=["\n this is Mumbai"]
f.writelines(l)
f=open('file.txt','r')
print(f.read())
f.close()
#Q4
print("-------------------------------------------------------------------------")
f=open('file.txt','r')
list1=[]
list1=f.readlines()
print(list1)
f.close()
#Q5
print("-------------------------------------------------------------------------")
f=open('file.txt','r')
array1=[]
for line in f:
    array1.append(line)
print(array1)
f.close()
#Q6
print("-------------------------------------------------------------------------")
with open("file.txt",'r') as f:
    lines=len(f.readlines())
    print("Total number of lines",lines)
    f.close()
#Q7
print("-------------------------------------------------------------------------")
import os
f=os.stat("file.txt") 
print("Size of file",f.st_size,"bytes")
"""
----------------------------OUTPUT----------------------------------------
Hey
My name is Aryan
I study in SFIT
 this is Mumbai
-------------------------------------------------------------------------
Enter a number of lines:2
Hey

My name is Aryan

-------------------------------------------------------------------------
Hey
My name is Aryan
I study in SFIT
 this is Mumbai
 this is Mumbai
-------------------------------------------------------------------------
['Hey\n', 'My name is Aryan\n', 'I study in SFIT\n', ' this is Mumbai\n', ' this is Mumbai']
-------------------------------------------------------------------------
['Hey\n', 'My name is Aryan\n', 'I study in SFIT\n', ' this is Mumbai\n', ' this is Mumbai']
-------------------------------------------------------------------------
Total number of lines 5
-------------------------------------------------------------------------
Size of file 72 bytes
"""

