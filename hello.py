"""Beginner-friendly examples of Python variables, data types, and arithmetic."""

# A number and a string containing the same digits are different values.
number = 5
number_as_text = "5"
print("Is the number equal to the text?", number == number_as_text)

# Variables can store text, whole numbers, and decimal numbers.
name = "Shivam"
age = 23
chips_price = 25.99

print("Name:", name)
print("Age:", age)
print("Chips price:", chips_price)

# Assigning a variable's value to another variable copies the current value.
age_copy = age
age_copy = 4
print("Age:", age)
print("Age copy after changing it:", age_copy)

# Use type() to find out what kind of value a variable contains.
is_learning_python = False
favorite_color = None

print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of chips_price:", type(chips_price))
print("Type of is_learning_python:", type(is_learning_python))
print("Type of favorite_color:", type(favorite_color))
print("Does favorite_color have no value?", favorite_color is None)

# Add two numbers and store the result in a clearly named variable.
first_number = 2
second_number = 5
total = first_number + second_number
print("Sum:", total)