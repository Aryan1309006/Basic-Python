<<<<<<< HEAD

#               Object oriented programing
#Q1:
class Student:  
    Branch = "Computer Science"   
    Sem = 5   
    def __init__(self, name, age, marks):   
        self.Name = name  
        self.Age = age  
        self.Marks = marks  
student1 = Student("John", 20, 85)   
print("Accessing class variables through the class:")  
print(f"Branch: {Student.Branch}")  
print(f"Sem: {Student.Sem}")   
print("\nAccessing class variables via the object:")  
print(f"Branch: {student1.Branch}")  
print(f"Sem: {student1.Sem}")   
print("\nAccessing instance variables directly from the object:")  
print(f"Name: {student1.Name}")  
print(f"Age: {student1.Age}")  
print(f"Marks: {student1.Marks}")
print("----------------------------------------------------------------------")

#Q2
class Student:    
    Branch = "Computer Science"  
    Sem = 5    
    def __init__(self, name, age, marks):  
        self.Name = name  
        self.Age = age  
        self.Marks = marks    
    def display_details(self):    
        print(f"Branch: {Student.Branch}, Sem: {Student.Sem}")    
        print(f"Name: {self.Name}, Age: {self.Age}, Marks: {self.Marks}")    
student1 = Student("John", 20, 85)   
student1.display_details()
print("----------------------------------------------------------------------")



#Q3
class Fruit:  
    def __init__(self, name="", color="", price=0.0):  
        self.__name = name 
        self.__color = color 
        self.__price = price  
    def set_name(self, name):  
        self.__name = name  
    def set_color(self, color):  
        self.__color = color  
    def set_price(self, price):  
        self.__price = price   
    def get_name(self):  
        return self.__name  
    def get_color(self):  
        return self.__color  
    def get_price(self):  
        return self.__price   
fruit1 = Fruit()  
fruit1.set_name("Apple")  
fruit1.set_color("Red")  
fruit1.set_price(250)  
print("Fruit Details:")  
print(f"Name: {fruit1.get_name()}")  
print(f"Color: {fruit1.get_color()}")  
print(f"Price: Rs{fruit1.get_price()}")  
print("----------------------------------------------------------------------")

'''
----------------------------OUTPUT-------------------------------------
Accessing class variables through the class:
Branch: Computer Science
Sem: 5

Accessing class variables via the object:
Branch: Computer Science
Sem: 5

Accessing instance variables directly from the object:
Name: John
Age: 20
Marks: 85
----------------------------------------------------------------------
Branch: Computer Science, Sem: 5
Name: John, Age: 20, Marks: 85
----------------------------------------------------------------------
Fruit Details:
Name: Apple
Color: Red
Price: Rs250
'''
