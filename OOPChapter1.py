# OOP in pythin
# To map with real world scenario, we started using object in code
# this is called object oriented programming

# Class & Object in Python
# class is a blueprint for createing object

# createing class
class Student:
    name ="Karan kumar"

# create Object (instance)
s1 = Student()
print(s1) # output is : <__main__.Student object at 0x0000022B50448AD0>
print(type(s1)) # output is : <class '__main__.Student'>
print(s1.name) # output is : Karan kumar

class Car:
    color = "blue"
    brand = "Mercedes"

car1 = Car()

print(car1.color)
print(car1.brand)

# __init__ function
# Constructro
"""
 All classes have a function calles __init__(), which is
 always executed when the Object is being initiated
"""

# createing class 
class Student:
    # default Constructro
    def __init__(self):
        pass
        
    # parameterized Constructro
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        print("adding new student in database..")

"""
Self :- 1) self is a reference to the current object of a class.
           It is used to access the variables and methods belonging
           to that particular object.
        2) In simple words, self tells Python which object's data
           we are working with.
"""

# creating Object
S1 = Student("Karan",34)
print(S1.name,S1.marks)

"""
The self parameter is a reference to the current
instance of the class, and is used to access variables 
that belongs to the class
"""


# Class & Instance Attributes
# 1) Class.attr <-- comman for all class
"""
 A class attribute is a variable that is defined inside a
 class but outside all methods. It is shared by all objects (instances) of that class.
"""
# Example
class Student:
    college = "ABC College"  # Class Attribute

s1 = Student()
s2 = Student()

print(s1.college)
print(s2.college)
# 2) obj.attr
# An instance attribute is a variable that belongs to a particular object (instance) of a class. Each object can have its own separate value.
# Example
class Student:
    def __init__(self, name):
        self.name = name  # Instance Attribute

s1 = Student("Shivam")
s2 = Student("Rahul")

print(s1.name)
print(s2.name)



class Student:
    college = "ABC College"  # Class Attribute

    def __init__(self, name, age):
        self.name = name     # Instance Attribute
        self.age = age       # Instance Attribute


s1 = Student("Shivam", 21)
s2 = Student("Rahul", 22)

print(s1.college)
print(s2.college)

print(s1.name)
print(s2.name)


# Methods
# Methods are functions that belong to object

# Create Class
class Student:
    name  = "shivam"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks

    def hello(self):
        print(f"hello {self.name}")

    def get_marks(self):
        print(f"hello {self.marks}")

# create Object
obj1 = Student("karan",56)
obj1.hello()
obj1.get_marks()


class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def get_Avg(self):
        sum = 0
        for val in self.marks:
            sum+= val
        print(f"hii {self.name} your avg score is {sum/3}")

obj2 = students("tony stark",[99,98,97])
obj2.get_Avg()
obj2.name = "harsh"
obj2.get_Avg()

# Static Method
# Methods that don't use the self parameter (work at class level)

class CollagStudent:
    @staticmethod #decorator
    def college():
        print("ABC College")

"""
*Decorators allow us to wrap another function in order to
extend the behaviour of the wrapped function, without
permanently modifying it
"""

# 1. Abstraction in Python
"""
-----What is Abstraction?--------
1)Abstraction is an Object-Oriented Programming concept
that hides unnecessary implementation details and shows
only the essential features of an object to the user.
It means hiding the complex implementation inside something
and showing the user only the necessary functionality.

----Why do we need Abstraction?------
When we build large software, it involves many complex operations.
If a user had to understand the internal workings of every operation,
using the software would become difficult.

Therefore, we hide the internal implementation and provide only
the necessary functionality. This makes the code easier to understand
and use.

-----How does Abstraction work in Python?------
3)In Python, we can implement abstraction using the `abc` 
(Abstract Base Classes) module.
This primarily involves the use of the `ABC` class and the`@abstractmethod`
decorator.

In Python, an abstract method only affects classes that inherit
from the parent class. This means that if a class is defined—for
instance, on line 234—and no other class inherits from it, then
that class remains unaffected. Only those classes that inherit
from the abstract parent are strictly required to implement the 
method; otherwise, Python will not allow an object of that class
to be created.
"""


from abc import ABC, abstractmethod

class Car(ABC):

    @abstractmethod
    def starts(self):
        print("Car starting...")


class Tesla(Car):

    def starts(self):
        print("Car started using a button")

class BMW(Car):

    def starts(self):
        print("Car started using a key")


car1 = Tesla()
car2 = BMW()

car1.starts()
car2.starts()


# 2. Encapsulation in Python

"""
-----What is Encapsulation?-------
Encapsulation is an Object-Oriented Programming concept
that combines data (attributes) and methods into a single
unit (class) and restricts direct access to some of the 
object's internal data. Encapsulation means keeping data and
the methods that operate on that data within a single class,
and protecting the data from unnecessary direct access.

------Why do we need Encapsulation?----
When working on a large application, we often need to prevent
an object's data from being modified in an incorrect or unintended
way. For example, if a bank account has a balance of ₹10,000, we
must ensure that no one can accidentally change it to -5,000.
To address this, we create methods to control the data.
This ensures the validity of the data and allows us to regulate
the changes made within an object.

----How does Encapsulation work in Python?----
In Python, naming conventions are used for encapsulation.
For example, prefixing an attribute name with a double
underscore (__) triggers name mangling in Python.
"""

class bank():
    def __init__(self,user,balance,account_number=None):
        self.balance = balance 
        self.user = user 
        self.account_number = account_number 

    def debit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    def credit(self,amount):
        if self.balance <= 0:
            print("Withdrawal amount must be greater than zero.")
        elif  amount > self.balance:
            print("Insufficient balance for this withdrawal.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
    

    def printingBalance(self):
        print(f"your Bank balance is {self.balance}")

rohan = bank("Rohan",1000,"12sb45T")
print(rohan.debit(5000))
print(rohan.credit(5000))
print(rohan.printingBalance())