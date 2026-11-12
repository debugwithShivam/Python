"""
============================================================
PYTHON NOTES: DATA TYPES
File: dataType.py
Level: Beginner
============================================================

1. WHAT IS A DATA TYPE?
-----------------------
A data type tells Python what kind of value a variable refers to.

Examples:
    age = 21             # int (whole number)
    price = 99.50        # float (decimal number)
    name = "Shivam"      # str (text)
    is_learning = True   # bool (True or False)

Why do data types matter?
- They help Python understand what operations are valid.
- Different types support different methods and operations.
- They affect how values are stored and how they behave.

Python is dynamically typed:
You do not need to write the type when creating a variable.
Python determines the type at runtime.

    value = 10
    print(type(value))   # <class 'int'>

    value = "ten"        # The same variable can refer to a string now.
    print(type(value))   # <class 'str'>


2. MAIN BUILT-IN PYTHON DATA TYPES
----------------------------------

A) Numeric types
~~~~~~~~~~~~~~~~
int     : Whole numbers, positive or negative, without a decimal point.
          Example: 10, -5, 0

float   : Numbers with a decimal point.
          Example: 10.5, -3.14, 2.0

complex : Numbers with a real and imaginary part.
          Example: 2 + 3j

B) Text type
~~~~~~~~~~~~
str     : A sequence of characters (text).
          Example: "Python", 'Hello'

C) Boolean type
~~~~~~~~~~~~~~~
bool    : Represents a truth value: True or False.
          Example: is_valid = True

D) Sequence types
~~~~~~~~~~~~~~~~~
list    : Ordered collection; allows duplicate values; mutable.
          Example: [10, 20, 10]

tuple   : Ordered collection; allows duplicate values; immutable.
          Example: (10, 20, 10)

range   : Represents a sequence of integers, commonly used in loops.
          Example: range(5)  # 0, 1, 2, 3, 4

E) Mapping type
~~~~~~~~~~~~~~~
dict    : Stores key-value pairs. Mutable.
          Example: {"name": "Shivam", "age": 21}

F) Set types
~~~~~~~~~~~~
set       : Unordered collection of unique elements; mutable.
            Example: {10, 20, 30}

frozenset : Immutable version of a set.
            Example: frozenset({10, 20, 30})

G) Binary types
~~~~~~~~~~~~~~~
bytes      : Immutable sequence of bytes.
             Example: b"ABC"

bytearray  : Mutable sequence of bytes.
             Example: bytearray([65, 66, 67])

memoryview : A view of data in a bytes-like object, without copying it.
             Example: memoryview(b"ABC")

H) None type
~~~~~~~~~~~~
NoneType : The type of the special value None.
           None usually means "no value" or "nothing here".
           Example: result = None


3. HOW MANY DATA TYPES ARE THERE?
---------------------------------
Python has several built-in data types. The groups above cover the
main built-in types you will commonly meet as a beginner.

There is not just one fixed count that is useful in every situation:
Python also lets programmers create their own types using classes,
and libraries can provide additional types.

You can check the type of a value with type():

    print(type(100))          # int
    print(type(10.5))         # float
    print(type("Hello"))      # str
    print(type([1, 2, 3]))    # list


4. WHAT DOES MUTABLE MEAN?
--------------------------
Mutable means CHANGEABLE.

A mutable object can be changed after it has been created.
You can modify its contents without creating a completely new object.

Common mutable built-in types:
- list
- dict
- set
- bytearray

Example with a list:

    numbers = [10, 20, 30]
    print(numbers)

    numbers[0] = 100       # Change the first item.
    numbers.append(40)     # Add another item.

    print(numbers)         # [100, 20, 30, 40]

The list itself was modified.


5. WHAT DOES IMMUTABLE MEAN?
----------------------------
Immutable means NOT CHANGEABLE.

Once an immutable object has been created, its contents cannot be
changed. An operation that seems to modify it actually creates a
new object (or returns another object).

Common immutable built-in types:
- int
- float
- complex
- bool
- str
- tuple
- range
- frozenset
- bytes

Example with a string:

    text = "Python"
    text = text + " Language"

    print(text)  # Python Language

This does NOT change the original string object. The expression
creates a new string, and the variable `text` is assigned to it.

This is not allowed:

    word = "Python"
    word[0] = "J"   # TypeError: strings do not support item assignment


6. MUTABLE vs IMMUTABLE: THE DIFFERENCE
---------------------------------------

Mutable:
- Can be changed after creation.
- Changes can happen to the same object.
- Examples: list, dict, set, bytearray.

Immutable:
- Cannot be changed after creation.
- A change-like operation creates/returns a different object.
- Examples: int, float, bool, str, tuple, bytes.

Remember:
A variable is a name that refers to an object. Mutability is a
property of the object, not the variable.


7. IMPORTANT EXAMPLE: SAME OBJECT OR NEW OBJECT?
------------------------------------------------

# Mutable example
first_list = [1, 2, 3]
second_list = first_list

second_list.append(4)

print(first_list)   # [1, 2, 3, 4]
print(second_list)  # [1, 2, 3, 4]

Why?
Both variables refer to the SAME list object. Changing that object
through either variable is visible through the other variable.

# Immutable example
first_number = 10
second_number = first_number

second_number = second_number + 5

print(first_number)  # 10
print(second_number) # 15

Why?
Integers are immutable. The addition produces a new integer object,
and second_number is made to refer to that result. first_number
still refers to 10.


8. IMPORTANT WARNING: A TUPLE CAN CONTAIN A MUTABLE OBJECT
----------------------------------------------------------

A tuple itself is immutable, but it can contain a mutable object.

    data = ([1, 2], "Python")

    data[0].append(3)  # Allowed: the list inside the tuple changes.
    print(data)        # ([1, 2, 3], 'Python')

    # data[0] = [9, 9] # Not allowed: changing a tuple item.

The tuple's references/items cannot be reassigned, but the list
object stored inside it can still be changed.


9. QUICK REVISION TABLE
-----------------------

Type          Mutable or Immutable?     Example
---------------------------------------------------------
int           Immutable                 25
float         Immutable                 3.14
complex       Immutable                 2 + 3j
bool          Immutable                 True
str           Immutable                 "Hello"
list          Mutable                   [1, 2, 3]
tuple         Immutable                 (1, 2, 3)
range         Immutable                 range(5)
dict          Mutable                   {"a": 1}
set           Mutable                   {1, 2, 3}
frozenset     Immutable                 frozenset({1, 2})
bytes         Immutable                 b"ABC"
bytearray     Mutable                   bytearray(b"ABC")
memoryview    Depends on underlying     memoryview(b"ABC")
NoneType      Immutable                 None

Note: memoryview does not own the underlying data. Whether its data
can be changed depends on the object it views and how the view is used.


10. CHECK YOUR UNDERSTANDING
----------------------------

Try to predict the output before running each example.

Question 1:
    items = [1, 2]
    other = items
    other.append(3)
    print(items)

Question 2:
    name = "Sam"
    other_name = name
    other_name = other_name + "ir"
    print(name)
    print(other_name)

Question 3:
    values = (1, 2, 3)
    values[0] = 100

Think about:
- Which objects are mutable?
- Which variables refer to the same object?
- Does an operation modify an object or create a new one?

============================================================
END OF NOTES
============================================================
"""

# This file is intended to be read as notes.
# The examples are inside the documentation string, so they do not
# execute when you run this file.
