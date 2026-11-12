# Function in python 
# Block of statements that perform a specific task 

# def func_name(param1,param2...): <--- function definition
    # some work
    # return val

# func_name(arg1,arg2..) function call


# example 
def sum(a,b):
    s = a+b
    return s

print(sum(2,3))

# function definition
def mul(a,b): #parameters
    return a*b

multiplay = mul(2,5) # function call; agguments
print(multiplay)

def print_hello():
    print("hello world")

print_hello() # output is hello world
hello = print_hello() 
print(hello) # output is None becasue function kuch bhi return nahi kar raha hai 


def calc_avg(a,b,c):
    sum = a + b + c
    avg = sum / 3
    print(int(avg))
    return avg 

calc_avg(1,2,3)
calc_avg(98,97,95)


# function types in python 

# 1) build-in functions 
    # print()
    # len()
    # type()
    # range()

# 2) user defined functions


# Default Parameters
# Assigning a default value to parameter, which is used no argument is passed

def cal_prod(a=3,b=3):
    print(a*b)
    return a * b

cal_prod()

# Let's Practice
num = ["delhi","gurgaon","noida","puna","munbai","chennai"]

# WAF to print the length of a list. ( list is the parameter)
def listLenght(lists):
    print(f"lenght of List {len(lists)}")
    return len(lists)

listLenght(num)

# WAF to print the elements of a list in a single line. ( list is the parameter)
def print_list(list):
    for item in list:
        print(item,end=" ") #In Python, end=" " is an optional keyword argument for the print() function that replaces the default newline (\n) at the end of the output with a single space

print_list(num)

# WAF to find the factorial of n. (n is the parameter)
def factorial(n):
    fact = 1
    for el in range(1,n+1):
        fact*=el
    print(f"factorial of {n} is : {fact}")

factorial(5)


# WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 83
    print(f"{usd_val} USD = {inr_val} INR")

converter(100)


# *args and **kwargs

# Jab tumhe pata nahi hota ki function mein kitne arguments pass honge, tab ye useful hote hain.
# *args allows a function to receive any number of positional
# Description: Used to collect multiple positional arguments into a single tuple inside a function. It allows a function to accept any number of positional arguments.
def add_numbers(*numbers):
    print(numbers)

add_numbers(10, 20, 30, 40)

# 1. What is **kwargs?
# **kwargs allows a function to receive any number of keyword
# arguments (arguments written as name=value).
# Description: Used to collect multiple keyword arguments into a single dictionary inside a function. It allows a function to accept any number of keyword arguments.

def student_details(**kwargs):
        print(kwargs)

student_details(name="Shivam", age=21, language="Python")

# Output:{'name': 'Shivam', 'age': 21, 'language': 'Python'}

def add(a, b):
    """This function adds two numbers."""
    return a + b

print(add.__doc__)

def multiply(a, b):
        """This function multiplies two numbers."""
        return a * b

print(multiply.__doc__) #This function multiplies two numbers.
print(multiply(5, 4)) # 20