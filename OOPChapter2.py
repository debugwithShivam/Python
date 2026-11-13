# del Keyword
# Used to delete object properties or Object itself

# del obj.name  <-- for attribute
# del obj <-- for whole object

class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Shivam")

del s1.name 


# Private(like) attributes & methods
"""
Conceptual Implementations in Python
Private attributes & methods are meant to be 
used only within the class and are not
accessible from outside the class.
"""


"""
undersocre lagane sa attribute private hojayga after add
underscore starting of the attribute (__attribute_name)
the attribute well be private then no one access this
attribute also not accessable from print() method 
"""

""" method ka aga underscore lagana sa method private hojata
    hai koi bhi underscore wale method ko access nahi kar pata hai """

""" Private methods or attributes ko dusre  dusre methods ke andar
    hi access Kiya Ja sakta hai """

class Account:
    __name = "anonymose"
    def __init__(self,acc_no,acc_pass):
        self.__acc_no = acc_no 
        
        self.__acc_pass = acc_pass 
    def reset_pass(self,password):
        if self.__acc_pass == password:
            # how to access private attribute
            print(f"your password is right and your password is :{self.__acc_pass} and account no is : {self.__acc_no}")
        else:
            print("Password is wrong")


    def __hello(self):
        print("hello person")

    # how to access private function
    def welcome(self):
        self.__hello()
        

account1 = Account("12345","abcde")
# print(account1.__acc_no)
# print(account1.__acc_pass)
# print(account1.reset_pass("abcde"))
print(account1.welcome())

# Inheritance
# When one class(child/derived) derives the properties & methods of another class(parent/base).
class Car:
    color = "back"
    @staticmethod
    def start():
        print("car Started..")

    @staticmethod
    def stop():
        print("car stopped..")


class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name


car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car2.stop())
print(car2.color)


# type of Inheritance
# 1) Single Inheritance 
"""
 When one child class inherits from only one parent class, it is
 called Single Inheritance.
"""
# example 
class Father:
    def skills(self):
        print("Father knows Driving")


class Son(Father):
    def coding(self):
        print("Son knows Coding")


s1 = Son()
s1.skills()  # Inherited method
s1.coding()  # Own method

# 2) multi-level Inheritance
"""
 When a class inherits from another child class, forming a chain
 of inheritance, it is called Multilevel Inheritance.
"""
# example

class Grandfather:
    def house(self):
        print("Grandfather has a House")


class Father(Grandfather):
    def car(self):
        print("Father has a Car")


class Son(Father):
    def bike(self):
        print("Son has a Bike")


s1 = Son()

s1.house()
s1.car()
s1.bike()

# 3) multiple Inheritance
"""
When one child class inherits from two or more parent classes,
it is called Multiple Inheritance.
"""
# example

class Father:
    def skills1(self):
        print("Father knows Driving")


class Mother:
    def skills2(self):
        print("Mother knows Cooking")


class Son(Father, Mother):
    def skills3(self):
        print("Son knows Coding")


s1 = Son()

s1.skills1()
s1.skills2()
s1.skills3()

# Super Method
"""
The super() function is used to access methods of a parent class
from a child class without directly mentioning the parent class name.
"""
# example 1 :-
class Parent:
    def Older(self):
        print("This is Parent class")


class Child(Parent):
    def show(self):
        super().Older()
        print("This is Child class")


obj = Child()
obj.show()

# example 2 :-
class Car:
  def __init__(self, type):
   self.type = type


class ToyotaCar(Car):
  def __init__(self, name, type):
   super().__init__(type)
   self. name = name



car1 = ToyotaCar("prius", "electric")
print(car1.type)


# Class method
# A class method is bound to the class & receives the class as an implicit first argument
# Note - static method can't access or modify class state & generally for utility
"""
@classmethod is a decorator in Python that is used to create a
method that works with the class itself rather than a particular
object (instance).

In simple words:
- Normal method works with an object using self.
- Class method works with a class using cls.
"""
class Student:
    @classmethod #decorator
    def college(cls):
        pass

"""
Here:
- @classmethod tells Python that this method is a class method.
- cls represents the current class.
- cls is similar to self, but self refers to an object and cls refers to a class.
"""