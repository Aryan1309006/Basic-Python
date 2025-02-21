#Display the different type of data used in Python
print("______________________list______________________")
list_1=[37,'aryan','INFT']
list_2=[55,'SFIT','a']
    #acess element
print("2nd element of list is: ",list_1[1])
    #item assignment
print("list[0] before assignment:",list_1)
list_1[0]="B"
print("list[0] after assignment:",list_1)

    #slicing
print(list_1[1:2])
    #using +
a=list_1+list_1
print(a)
    #Assign empty list
my_list=list()
print("Empty list:",my_list)
    #squeez
li=[1,2,2,3,4,4]
li=list(set(li))
print(li)
a="Aryan"
    #del
list_1.remove("INFT")
print(list_1)

list_1.clear()
print(list_1)
    #membership
print(55 in list_2)
print(34 in  list_2)
 #list
a="Aryan"
b=list(a)
print(b)
 #sort
b.sort()
print(b)
    #length
print("length of list_2 is:",len(list_2))
    #append
list_2.append("aryan")
print(list_2)

    #index
print("Index of SFIT is:",list_2.index("SFIT"))
    #copy
print("list befor pop:",list_2)
list_2.pop()
print("List after pop",list_2)
    #extend
list_2.extend("IT")
print(list_2)
#tupasls operation
tup=("aryan",2,45,"game")
print("first element of tup:",tup[1])

#string optration
a="Hello world"
b=" hi "
#length
print(len(a))
#lower upper
print("lower:",a.lower())
print("Upper",a.upper())
#slicing
print(a[3:9])
print(a[3:])
print(a[:9])

#starth with
print(a.startswith("H"))

#dictionary
print("______________________________dictionary _____________________________")
dict1={"name":'Aryan',"roll no":'1034','class':'INFT','lecture':'PYP'}
print("dict1['Name']:",dict1['name'])
del dict1['lecture']
print("After using del",dict1)
print("length of dict 1:",len(dict1))
dict2=dict1.copy()
print('dict2 after copy ',dict2)
print("value:", dict1.get('roll no'))
print("value:", dict1.get('age','NA'))
print("item method",dict1.items())
dict2={'age':18}
dict1.update(dict2)
print("updated dict:",dict1)
print("value:",dict1.keys())
print("value:",dict1.values())

#set
print("_________________________________set________________________________")
set1={'a','b','c','b','l'}
print(set1)
for x in set1:
    print(x)

print(len(set1))
print(type(set1))
print('z' in set1)
print('a' in set1)
print(set1.add('x'))
set1.add("m")
print(set1)
set1.remove("b")
print(set1)
set1.pop()
print(set1)
set1.clear()
print(set1)
set2={1,2,3,4}
set3={7,3}
set4=set2|set3 #union
set5=set4&set2 #intersection
print(set4)
print(set3)
a=set2-set3 #diffreence
print(a)
set7=set2^set3
print(set7)
a="aryan"
x=set(a)
print(x)











