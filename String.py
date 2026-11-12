# three valid way to create String
str1 = "this is a string."
str2 = 'ZodX'
str3 = """this is a String"""

# how to break line in string (escape sequence charaters)
breakLine = "this is a string \n we are creating it in python with break line"
backSpace = "this is a string \t we are creating it in python with backspace"
# print(breakLine) 
# print(backSpace) 

# String indexing
str4 = "this is a string"
print(str4[0])  # Output: t
print(str4[5])  # Output: i

# String concatenation
str5 = "Hello"
str6 = "World"
str7 = str5 + " " + str6
print(str7)  # Output: Hello World

# length of string
print(len(str7))  # Output: 11

# String slicing
str8 = "Hello, World!"
# strint[start:end] - returns a substring from start index to end index (not including end index)
# String[1:4] is ello
# String[:4] is same as String[0:4]
# String[4:] is same as String[4:len(String)] python will automatically calculate the length of the string
print(str8[0:5])  # Output: Hello
print(str8[7:12])  # Output: World

# Negative indexing
# String[-1] is same as String[len(String)-1]
str9 = "Hello, World!"
print(str9[-1])  # Output: !
print(str9[-6:-1])  # Output: World


# String methods
str9 = "hello world"
# the following are some commonly used string methods in Python:

# upper() methos uses to convert all characters in a string to uppercase.
print(str9.upper())  # Output: HELLO WORLD
# lower() method uses to convert all characters in a string to lowercase.
print(str9.lower())  # Output: hello world
# capitalize() method uses to convert the first character of a string to uppercase.
print(str9.capitalize())  # Output: Hello world
# replace() method uses to replace a substring with another substring.
print(str9.replace("world", "Python"))  # Output: hello Python
# split() method uses to split a string into a list of substrings.
print(str9.split())  # Output: ['hello', 'world']
# strip() method uses to remove whitespace from the beginning and end of a string.  
print(str9.strip())  # Output: hello world
# startswith() method uses to check if a string starts with a specified substring.
print(str9.startswith("hello"))  # Output: True
# endswith() method uses to check if a string ends with a specified substring.
print(str9.endswith("world"))  # Output: True
# find() method uses to find the position of a substring in a string.
print(str9.find("world"))  # Output: 6
# count() method uses to count the number of occurrences of a substring in a string.
print(str9.count("o"))  # Output: 2


# isalpha() method uses to check if all characters in a string are alphabetic.
print(str9.isalpha())  # Output: False
# isdigit() method uses to check if all characters in a string are digits.
print(str9.isdigit())  # Output: False
# isalnum() method uses to check if all characters in a string are alphanumeric.
print(str9.isalnum())  # Output: False
# isspace() method uses to check if all characters in a string are whitespace.
print(str9.isspace())  # Output: False
# islower() method uses to check if all characters in a string are lowercase.
print(str9.islower())  # Output: True
# isupper() method uses to check if all characters in a string are uppercase.
print(str9.isupper())  # Output: False
# isprintable() method uses to check if all characters in a string are printable.
print(str9.isprintable())  # Output: True
# ljust() method uses to left-justify a string in a specified width.
print(str9.ljust(20, '-'))  # Output: hello world--------
# rjust() method uses to right-justify a string in a specified width.
print(str9.rjust(20, '-'))  # Output: --------hello world
# zfill() method uses to pad a string with zeros on the left.
print(str9.zfill(20))  # Output: 0000000000hello world
# isprintable() method uses to check if all characters in a string are printable.
print(str9.isprintable())  # Output: True
# isidentifier() method uses to check if a string is a valid identifier.
print(str9.isidentifier())  # Output: False
# isnumeric() method uses to check if all characters in a string are numeric.
print(str9.isnumeric())  # Output: False
# isdecimal() method uses to check if all characters in a string are decimal characters.
print(str9.isdecimal())  # Output: False
# isascii() method uses to check if all characters in a string are ASCII characters.
print(str9.isascii())  # Output: True


# String formatting
name = "John"
age = 30
price = 9.99
bool = True
# using f-string
print(f"My name is {name} and I am {age} years old.")  #Output: My name is John and I am 30 years old.
# using format() method
print("My name is {} and I am {} years old.".format(name, age))  #Output: My name is John and I am 30 years old.
# using % operator
print("My name is %s and I am %d years old." % (name, age))  #Output: My name is John and I am 30 years old.
print("The price is %.2f" % price)  #Output: The price is 9.99

# Let's Practice
nameLen = input("Enter your name: ")
print(f"Your name is {nameLen} and it has {len(nameLen)} characters.")


# even or Odd 
check = int(input("enter a number : "))
 
if check % 2 == 0:
    print(f"user input number {check} is even")
else:
    print(f"user input number {check} is odd")
