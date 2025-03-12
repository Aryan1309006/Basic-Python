#Q1 inheritance
# Parent Class  
class Animal:  
    def __init__(self, name):
        self.name = name  
    def speak(self):  
        print(f"{self.name} makes a sound")  
# Single Inheritance: Dog inherits from Animal  
class Dog(Animal):  
    def bark(self):  
        print(f"{self.name} barks")  
# Multilevel Inheritance: Cat -> Dog -> Animal  
class Cat(Dog): # Dog is inherited here, creating a chain  
    def meow(self):  
        print(f"{self.name} meows")  
# Hierarchical Inheritance: Both Dog and Tiger inherit from Animal  
class Tiger(Animal): # Inheriting from Animal  
    def roar(self):  
        print(f"{self.name} roars")  
#Multiple Inheritance: HybridDog inherits from both Tiger & cat 
# Hybrid Inheritance: Combination of multiple inheritance types  
class HybridDog(Tiger, Cat): # Inheriting from both Tiger and Cat  
    pass      
print("Single Inheritance:")  
dog = Dog("Buddy")  
dog.speak() # Inherited method  
dog.bark() # Method from Dog  
print("\nMultilevel Inheritance:") 
cat = Cat("Kitty")  
cat.speak() # Inherited from Animal  
cat.bark() # Method from Dog  
cat.meow() # Method from Cat  
print("\nHierarchical Inheritance:")  
tiger = Tiger("Sheru")  
tiger.speak() # Inherited from Animal  
tiger.roar() # Method from Tiger  
print("\nHybrid Inheritance:")  
hybrid_dog = HybridDog("Hybrid")  
hybrid_dog.speak() # Inherited from Animal  
hybrid_dog.bark() # Inherited from Dog  
hybrid_dog.roar() # Inherited from Tiger
print("-------------------------------------------------------------------")
#Q2 polymorphism
# Compile Time Polymorphism (Method Overloading)  
# In Python, we simulate method overloading using default arguments  
class CompileTimeExample:  
    def add(self, a, b, c=0): # Default value of c allows overloading  
        return a + b + c  
# Creating an object of CompileTimeExample  
obj = CompileTimeExample()  
# Calling the method with 2 arguments  
print("Add 2 numbers:", obj.add(5, 10))  
# Calling the method with 3 arguments 
print("Add 3 numbers:", obj.add(5, 10, 15))  
# Runtime Polymorphism (Method Overriding)  
class Animal:  
    def sound(self):  
        print("Animal makes a sound")  
class Dog(Animal):  
    def sound(self):  
        print("Dog barks")  
class Cat(Animal):  
    def sound(self):  
        print("Cat meows")  
# Creating objects of Dog and Cat  
animal=Animal() 
dog = Dog()  
cat = Cat()  
# Demonstrating runtime polymorphism  
animal.sound() 
dog.sound() # Runtime Polymorphism - Dog's sound method is called 
cat.sound() # Runtime Polymorphism - Cat's sound method is called
print("-------------------------------------------------------------------")
"""
----------------------------------OUTPUT-----------------------------
Single Inheritance:
Buddy makes a sound
Buddy barks

Multilevel Inheritance:
Kitty makes a sound
Kitty barks
Kitty meows

Hierarchical Inheritance:
Sheru makes a sound
Sheru roars

Hybrid Inheritance:
Hybrid makes a sound
Hybrid barks
Hybrid roars
-------------------------------------------------------------------
Add 2 numbers: 15
Add 3 numbers: 30
Animal makes a sound
Dog barks
Cat meows
-------------------------------------------------------------------
"""
