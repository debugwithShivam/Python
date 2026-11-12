# Loops in python
# Loops are user to repeat instructions until a certain condition is met. There are two types of loops in python:
# 1. While loop
# how While loop works:  repeatedly executes a block of code as long as a specified condition remains true
# Syntex
count = 1
while count <= 10:
    print("hello")
    count += 1 # increment the count by 1

# example of while loop with break statement
count = 1
while count <= 10:
    print(f"hello {count}")
    count += 1
    if count == 5:
        break

print(f"Final count: {count}") # 5

# example of while loop with continue statement
count = 1
while count <= 10:
    count += 1
    if count == 5:
        continue
    print(f"hello {count}")

# reverse Loop
i = 5
while i >= 1:
    print(i)
    i -= 1

# let's see an example of while loop with else statement
count = 1
while count <= 5:
    print(f"hello {count}")
    count += 1
else:
    print("Loop finished without encountering a break statement.")

# let's Practice
# 1 to 100 print the numbers using while loop
count = 1
while count <= 100:
    print(count)
    count += 1

# 100 to 1
count = 100

while count >= 1:
    print(count)
    count-=1

table = int(input("Enter a number : "))
count = 1
while count <= 10:
    print(f"tabel of {table} : {table*count}")
    count+=1

# loop with List travers
print("\n----- List -----")

nums = [1,2,5,3,4,6,7,8,9,4]
heros = ["superman","thor","hulk","batman"] 
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx+=1

# loop with DICTIONARY travers
print("\n----- DICTIONARY -----")

student = {
    "name": "Shivam",
    "age": 21,
    "language": "Python"
}

keys = list(student.keys())
i = 0

while i < len(keys):
    key = keys[i]
    print(key, ":", student[key])
    i += 1

# loop with SET travers
print("\n----- SET -----")

numbers = {10, 20, 30, 40, 50}

numbers_list = list(numbers)

i = 0

while i < len(numbers_list):
    print(numbers_list[i])
    i += 1

# loop with TUPLE travers
print("----- TUPLE -----")

fruits = ("Apple", "Banana", "Mango", "Orange")

i = 0

while i < len(fruits):
    print(fruits[i])
    i += 1


numbers = (1,4,9,16,25,36,49,64,81,100)

i = 0 # initialization
x = 36

while i < len(numbers):
    if(numbers[i] == x):
        print(f"Fount at index {i}")
        break
    else:
        print("Finding..")
    i+=1

i = 1
while i<= 10:
    if(i%2==0):
        i+=1
        continue
    print(f"odd numbers : {i}")
    i+=1
# what is the difference between break and continue statement?
# Break statement is used to exit the loop when a certain condition is met, while continue statement is used to skip the current iteration and move to the next iteration of the loop.


# 2. For loop
# how For loop works:  iterates over a sequence (like a list, tuple, dictionary, set, or string) and executes a block of code for each item in the sequence.
# Loops are used for sequential traversal. for traversing list, string, tuples etc.

# for loops 
# for el in list
  # some work 

list = [11,22,33,44,55]

for val in list:
    print("for in loop with List : ",val) # output is 11 , 22 ,33 44, 55

tup = (100,200,300,400,500)

for num in tup:
    print("for in loop with tuple : ",num)

str = "powershell"

for char in str:
    print("for in loop with string : ",char)

# for loops with else
# for el in list
  # some work
# else:
  #work when loop ends

print("\n------- loops with else --------")

for char in str:
    if(char == "o"):
     print("for in loop with else: ",char,)
     break
else:
    print("END")


nums = (1,2,3,4,5,6,7,8,9,10)
x = int(input("enter your number : "))
idx = 0
for num in nums:
    if(num == x):
        print("Number Fount at idx : ",idx)
        break
    idx += 1
else:
    print("Founding...")


# range()
# Range function returns a sequence of numbers, starting form 0 by default, and increments by 1 (by defult), and stops before a specified number.
# range(start?,stop,step?)

print("\n------ range(start?,stop,step?) --------")
print("\n------ range loop --------")
# Step by default is 1 
print("\n ---renge(5)--- ")
for el in range(5): # start by default from 0 and ENd on 5 
    print(el)

print("\n ---renge(3,15)--- ")
for el in range(3,15): # range(start,stop)
    print(el)

print("\n ---renge(1,10,2)--- ")
for el in range(1,10,2):  # range(start,stop,step)
    print(el)


seq = range(10)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])

for i in seq:
    print(f"range(10) : {i}")

# revers loop
for i in range(100, 0 , -1):
    print(i)

# even number
print("\n ---- even ----")
for i in range(2,101,2):
    print(f"even numbers {i}")

# odd number
print("\n ---- odd ----")
for i in range(1,100,2):
    print(f"odd numbers {i}")

# table 
print("\n ---- table ----")
table = 2
for i in range(1, 11):
    print(f"{table} * {i} = {table * i}")


# pass statement
# pass is a null statment that dose nothing. it is used as a placeholder for future code.

# ager loop empty hoga to error dega us ka bad wala koi code nahi run hoga es problem ko pass keyword solve karta hai 
# for el in range(10):
#     # empty

# print("some useful work")

for el in range(10):
    pass # loop ma pass likha na ka matlab hai skip kar dena loop ko ab loop ka bad wale code run hoga 

if i > 5:
    pass

print("some useful work")

# Let's Practice
# WAP to find the sum of first n number. (using while)
n = 5
sum = 0 

for i in range(1,n+1):
    sum += i

print("total sum is = ",sum)

n = 7
sum = 0
i = 1
while i <= n:
    sum+=i
    i+=1
print("total sum = ",sum)

# WAP to find the factorial of first n numbers. (using for)
n = 5
fact = 1
i = 1
while i <= n:
    fact*=i
    i+=1
print("find factorial with while loop = ",fact)



n = 5
fact = 1
for i in range(1,n+1):
    fact*=i
print("find factorial with for in loop = ",fact)