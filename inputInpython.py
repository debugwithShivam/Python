print("example of input")
example = input("Enter your age : ") # default input value is string
print(type(example)) # <class 'str'>

# integer = int(input("this input value type is integer"))
# floating = float(input("this input value type is floating"))
# boolean = bool(input("this input value type is boolean"))
# string = str(input("this input value type is string"))


print("print name age marks from user input")

name = input("Enter your name : ")
age = input("Enter your age : ")
marks = input("Enter your marks : ")

print("Welcome ", name)
print("age = ", age)
print("marks", marks)

# task 1
print("print two input number sum")

num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))

sum = num1 + num2

print("sum of first and second number is :- ",sum)

# task 2
print("print Area of square from two input number")

side1 = float(input("enter square side 1 : "))
side2 = float(input("enter square side 2: "))

squareArea = side1 * side2

print("area :- ",squareArea)

# task 3
print("find average of two number")

avg1 = float(input("enter first number : "))
avg2 = float(input("enter second number : "))

average = (avg1 + avg2) / 2

print("area :- ",average)


# task 4
print("Print true if a is greater than or equal to b. if not print False")

a = int(input("enter first number :"))
b = int(input("enter second number :"))

print("with If-else")
if a >= b :
    print(True)
else:
    print(False)

print("without If-else")
print("a >= b :", a >= b)