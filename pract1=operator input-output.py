#Display the different type of data types used in Python.
data1 = ["hello"," user"," no."," 1026"]
data2 = (1026,)
data3 = "Hello world"
data4 = {'Name':"Unmesh",'Roll no.':1026}
data5={"hello","33",33}
print(type(data1))
print(type(data2))
print(type(data3))
print(type(data4))
print(type(data5))

#Display different types of operators used in python.
a=12
b=10
print("\nArithmetic operations:\n")
print("Addition is       :",a+b)
print("Substraction is   :",a-b)
print("Multiplication is :",a*b)
print("Division is       :",a/b)
print("Remainder is      :",a%b)
print("cube of a is      :",a**3)
print("floor division is :",a//b)
print("--------------------------------------------------------------------------")
print("Assignment operations:\n")
b+=5
print("Addition is         :",b)
a-=4
print("Substraction is     :",a)
a*=4
print("Multiplication is   :",a)
b/=5
print("Division is         :",b)
b%=9
print("Remainder is        :",b)
a**=2
print("Square of a is      :",a)
b//=2
print("floor division is   :",b)
print("--------------------------------------------------------------------------")
print("comparison operations:\n")
a=4
b=2
print("a is greater than b:",a>b)
print("b is greater than a:",b>a)
print("a is equal to b    :",a==b)
print("a is not equal to b:",a!=b)
print("--------------------------------------------------------------------------")
print("Logical Operations:\n")
c=8
d=5
print((c<10)and(d>0))
print((c<10)or(d>0))
print(not(c<10 and d>0))
print("--------------------------------------------------------------------------")
print("Bitwise Operations:\n")
a=10
b=2
c=0
print("A=",a,"B=",b,"C",c)
print("a&c ",a&c)
print("a|b",a|b)
print("a^b",a^b)
print("~c",~c)
print("a<<2",a<<2)
print("a>>2",a>>2)
print("--------------------------------------------------------------------------")
print("Membership Operations:\n")
a="hello this is a wonderful place"
print("hello"in a)
print("."not in a)
print("--------------------------------------------------------------------------")
print("Identity Operations:\n")
a="hello this is a wonderful place"
b="hello that is a wonderful place"
print(b is a)
print(b is not a)
print("--------------------------------------------------------------------------")
#String operations:

str1="Python Program"
str2="string Operations"
print(f"Length of the str1 1 is:{len(str1)} and that of str2 is:{len(str2)}")
print(f"string concatenation{str1+str2}")
print(f"string repeatation:{str2*3}")
print("First element of string 2 is:",str2[0])
print("\nPerforming String slicing:\n")
print(str1[2:9])
print(str1[2:9:2])
print(str2[6:])
print(str2[:9:1])
print(str2[::-1])
print(f"Str1 in lower case is:{str2.lower()} and str2 in lower case is:{str2.lower()}")
print(f"Str1 in upper case is:{str2.upper()} and str2 in upper case is:{str2.upper()}")
print("str1 starts with Python:",str1.startswith("Python"))
print("str2 ends with Python:",str1.endswith("operations"))
print(str1.isalpha())
print(str1.isalnum())
print(str2.isspace())
print(str2.capitalize())
print("\nSplit operations:\n")
print(str1.split())
print(str2.split(" "))
print(str1.find('Pro'))
print(str1.index("Pro"))
print(str1.find('o',4,14))
print(str2.count('i'))
print("--------------------------------------------------------------------------")
#list operations

list1=[34,'aryan','INFT']
list2=[55,'SFIT','a']
print("2nd element of list is   : ",list1[1])
print("list[0] before assignment:",list1)
list1[0]="B"
print("list[0] after assignment :",list1)
print("Slicing                  :",list1[1:2])
a=list1+list1
print(a)
print("Assigning empty list:")
my_list=list()
print("Empty list:",my_list)
print("squeez")
li=[1,2,2,3,4,4]
li=list(set(li))
print(li)
a="Aryan"
print("Deleting List:",list1.remove("INFT"))
print(list1)
list1.clear()
print(list1)
print("Use of membership operators in list:")
print(55 in list2)
print(34 in  list2)
a="Aryan"
b=list(a)
print(b)
print("Sorting:",b.sort())
print(b)
print("length of list2 is:",len(list2))
list2.append("aryan")
print(list2)
print("Index of SFIT is:",list2.index("SFIT"))
print("list befor pop:",list2)
list2.pop()
print("List after pop",list2)
list2.extend("IT")
print(list2)
print("--------------------------------------------------------------------------")
#tuple operations
tup=("aryan",2,45,"game")
print("first element of tup:",tup[0])
print("Number of game elements are:",tup.count('game'))
print("First occurence of 2 is at index:",tup.index(2))
a="Aryan"
b=tuple(a)
print(b)

'''OUTPUT:

<class 'list'>
<class 'tuple'>
<class 'str'>
<class 'dict'>
<class 'set'>

Arithmetic operations:

Addition is       : 22
Substraction is   : 2
Multiplication is : 120
Division is       : 1.2
Remainder is      : 2
cube of a is      : 1728
floor division is : 1
--------------------------------------------------------------------------
Assignment operations:

Addition is         : 15
Substraction is     : 8
Multiplication is   : 32
Division is         : 3.0
Remainder is        : 3.0
Square of a is      : 1024
floor division is   : 1.0
--------------------------------------------------------------------------
comparison operations:

a is greater than b: True
b is greater than a: False
a is equal to b    : False
a is not equal to b: True
--------------------------------------------------------------------------
Logical Operations:

True
True
False
--------------------------------------------------------------------------
Bitwise Operations:

A= 10 B= 2 C 0
a&c  0
a|b 10
a^b 8
~c -1
a<<2 40
a>>2 2
--------------------------------------------------------------------------
Membership Operations:

True
True
--------------------------------------------------------------------------
Identity Operations:

False
True
--------------------------------------------------------------------------
Length of the str1 1 is:14 and that of str2 is:17
string concatenationPython Programstring Operations
string repeatation:string Operationsstring Operationsstring Operations
First element of string 2 is: s

Performing String slicing:

thon Pr
to r
 Operations
string Op
snoitarepO gnirts
Str1 in lower case is:string operations and str2 in lower case is:string operations
Str1 in upper case is:STRING OPERATIONS and str2 in upper case is:STRING OPERATIONS
str1 starts with Python: True
str2 ends with Python: False
False
False
False
String operations

Split operations:

['Python', 'Program']
['string', 'Operations']
7
7
4
2
--------------------------------------------------------------------------
2nd element of list is   :  aryan
list[0] before assignment: [34, 'aryan', 'INFT']
list[0] after assignment : ['B', 'aryan', 'INFT']
Slicing                  : ['aryan']
['B', 'aryan', 'INFT', 'B', 'aryan', 'INFT']
Assigning empty list:
Empty list: []
squeez
[1, 2, 3, 4]
Deleting List: None
['B', 'aryan']
[]
Use of membership operators in list:
True
False
['A', 'r', 'y', 'a', 'n']
Sorting: None
['A', 'a', 'n', 'r', 'y']
length of list2 is: 3
[55, 'SFIT', 'a', 'aryan']
Index of SFIT is: 1
list befor pop: [55, 'SFIT', 'a', 'aryan']
List after pop [55, 'SFIT', 'a']
[55, 'SFIT', 'a', 'I', 'T']
--------------------------------------------------------------------------
first element of tup: aryan
Number of game elements are: 1
First occurence of 2 is at index: 1
('A', 'r', 'y', 'a', 'n')

====== RESTART: C:/Users/Admin/OneDrive/Documents/Desktop/N Python/exp2.py =====
<class 'list'>
<class 'tuple'>
<class 'str'>
<class 'dict'>
<class 'set'>

Arithmetic operations:

Addition is       : 22
Substraction is   : 2
Multiplication is : 120
Division is       : 1.2
Remainder is      : 2
cube of a is      : 1728
floor division is : 1
--------------------------------------------------------------------------
Assignment operations:

Addition is         : 15
Substraction is     : 8
Multiplication is   : 32
Division is         : 3.0
Remainder is        : 3.0
Square of a is      : 1024
floor division is   : 1.0
--------------------------------------------------------------------------
comparison operations:

a is greater than b: True
b is greater than a: False
a is equal to b    : False
a is not equal to b: True
--------------------------------------------------------------------------
Logical Operations:

True
True
False
--------------------------------------------------------------------------
Bitwise Operations:

A= 10 B= 2 C 0
a&c  0
a|b 10
a^b 8
~c -1
a<<2 40
a>>2 2
--------------------------------------------------------------------------
Membership Operations:

True
True
--------------------------------------------------------------------------
Identity Operations:

False
True
--------------------------------------------------------------------------
Length of the str1 1 is:14 and that of str2 is:17
string concatenationPython Programstring Operations
string repeatation:string Operationsstring Operationsstring Operations
First element of string 2 is: s

Performing String slicing:

thon Pr
to r
 Operations
string Op
snoitarepO gnirts
Str1 in lower case is:string operations and str2 in lower case is:string operations
Str1 in upper case is:STRING OPERATIONS and str2 in upper case is:STRING OPERATIONS
str1 starts with Python: True
str2 ends with Python: False
False
False
False
String operations

Split operations:

['Python', 'Program']
['string', 'Operations']
7
7
4
2
--------------------------------------------------------------------------
2nd element of list is   :  aryan
list[0] before assignment: [34, 'aryan', 'INFT']
list[0] after assignment : ['B', 'aryan', 'INFT']
Slicing                  : ['aryan']
['B', 'aryan', 'INFT', 'B', 'aryan', 'INFT']
Assigning empty list:
Empty list: []
squeez
[1, 2, 3, 4]
Deleting List: None
['B', 'aryan']
[]
Use of membership operators in list:
True
False
['A', 'r', 'y', 'a', 'n']
Sorting: None
['A', 'a', 'n', 'r', 'y']
length of list2 is: 3
[55, 'SFIT', 'a', 'aryan']
Index of SFIT is: 1
list befor pop: [55, 'SFIT', 'a', 'aryan']
List after pop [55, 'SFIT', 'a']
[55, 'SFIT', 'a', 'I', 'T']
--------------------------------------------------------------------------
first element of tup: aryan
Number of game elements are: 1
First occurence of 2 is at index: 1
('A', 'r', 'y', 'a', 'n')

======= RESTART: C:/Users/Admin/OneDrive/Documents/Desktop/N Python/exp2.py =======
<class 'list'>
<class 'tuple'>
<class 'str'>
<class 'dict'>
<class 'set'>

Arithmetic operations:

Addition is       : 22
Substraction is   : 2
Multiplication is : 120
Division is       : 1.2
Remainder is      : 2
cube of a is      : 1728
floor division is : 1
--------------------------------------------------------------------------
Assignment operations:

Addition is         : 15
Substraction is     : 8
Multiplication is   : 32
Division is         : 3.0
Remainder is        : 3.0
Square of a is      : 1024
floor division is   : 1.0
--------------------------------------------------------------------------
comparison operations:

a is greater than b: True
b is greater than a: False
a is equal to b    : False
a is not equal to b: True
--------------------------------------------------------------------------
Logical Operations:

True
True
False
--------------------------------------------------------------------------
Bitwise Operations:

A= 10 B= 2 C 0
a&c  0
a|b 10
a^b 8
~c -1
a<<2 40
a>>2 2
--------------------------------------------------------------------------
Membership Operations:

True
True
--------------------------------------------------------------------------
Identity Operations:

False
True
--------------------------------------------------------------------------
Length of the str1 1 is:14 and that of str2 is:17
string concatenationPython Programstring Operations
string repeatation:string Operationsstring Operationsstring Operations
First element of string 2 is: s

Performing String slicing:

thon Pr
to r
 Operations
string Op
snoitarepO gnirts
Str1 in lower case is:string operations and str2 in lower case is:string operations
Str1 in upper case is:STRING OPERATIONS and str2 in upper case is:STRING OPERATIONS
str1 starts with Python: True
str2 ends with Python: False
False
False
False
String operations

Split operations:

['Python', 'Program']
['string', 'Operations']
7
7
4
2
--------------------------------------------------------------------------
2nd element of list is   :  aryan
list[0] before assignment: [34, 'aryan', 'INFT']
list[0] after assignment : ['B', 'aryan', 'INFT']
Slicing                  : ['aryan']
['B', 'aryan', 'INFT', 'B', 'aryan', 'INFT']
Assigning empty list:
Empty list: []
squeez
[1, 2, 3, 4]
Deleting List: None
['B', 'aryan']
[]
Use of membership operators in list:
True
False
['A', 'r', 'y', 'a', 'n']
Sorting: None
['A', 'a', 'n', 'r', 'y']
length of list2 is: 3
[55, 'SFIT', 'a', 'aryan']
Index of SFIT is: 1
list befor pop: [55, 'SFIT', 'a', 'aryan']
List after pop [55, 'SFIT', 'a']
[55, 'SFIT', 'a', 'I', 'T']
--------------------------------------------------------------------------
first element of tup: aryan
Number of game elements are: 1
First occurence of 2 is at index: 1
('A', 'r', 'y', 'a', 'n')

======= RESTART: C:/Users/Admin/OneDrive/Documents/Desktop/N Python/exp2.py =======
<class 'list'>
<class 'tuple'>
<class 'str'>
<class 'dict'>
<class 'set'>

Arithmetic operations:

Addition is       : 22
Substraction is   : 2
Multiplication is : 120
Division is       : 1.2
Remainder is      : 2
cube of a is      : 1728
floor division is : 1
--------------------------------------------------------------------------
Assignment operations:

Addition is         : 15
Substraction is     : 8
Multiplication is   : 32
Division is         : 3.0
Remainder is        : 3.0
Square of a is      : 1024
floor division is   : 1.0
--------------------------------------------------------------------------
comparison operations:

a is greater than b: True
b is greater than a: False
a is equal to b    : False
a is not equal to b: True
--------------------------------------------------------------------------
Logical Operations:

True
True
False
--------------------------------------------------------------------------
Bitwise Operations:

A= 10 B= 2 C 0
a&c  0
a|b 10
a^b 8
~c -1
a<<2 40
a>>2 2
--------------------------------------------------------------------------
Membership Operations:

True
True
--------------------------------------------------------------------------
Identity Operations:

False
True
--------------------------------------------------------------------------
Length of the str1 1 is:14 and that of str2 is:17
string concatenationPython Programstring Operations
string repeatation:string Operationsstring Operationsstring Operations
First element of string 2 is: s

Performing String slicing:

thon Pr
to r
 Operations
string Op
snoitarepO gnirts
Str1 in lower case is:string operations and str2 in lower case is:string operations
Str1 in upper case is:STRING OPERATIONS and str2 in upper case is:STRING OPERATIONS
str1 starts with Python: True
str2 ends with Python: False
False
False
False
String operations

Split operations:

['Python', 'Program']
['string', 'Operations']
7
7
4
2
--------------------------------------------------------------------------
2nd element of list is   :  aryan
list[0] before assignment: [34, 'aryan', 'INFT']
list[0] after assignment : ['B', 'aryan', 'INFT']
Slicing                  : ['aryan']
['B', 'aryan', 'INFT', 'B', 'aryan', 'INFT']
Assigning empty list:
Empty list: []
squeez
[1, 2, 3, 4]
Deleting List: None
['B', 'aryan']
[]
Use of membership operators in list:
True
False
['A', 'r', 'y', 'a', 'n']
Sorting: None
['A', 'a', 'n', 'r', 'y']
length of list2 is: 3
[55, 'SFIT', 'a', 'aryan']
Index of SFIT is: 1
list befor pop: [55, 'SFIT', 'a', 'aryan']
List after pop [55, 'SFIT', 'a']
[55, 'SFIT', 'a', 'I', 'T']
--------------------------------------------------------------------------
first element of tup: aryan
Number of game elements are: 1
First occurence of 2 is at index: 1
('A', 'r', 'y', 'a', 'n')
'''
