# age = int(input("age : "))

# methot 1)
""" 
if(18 <= age <= 28):
    print("Valid Age")
elif(age < 18):
    print("Abhi omer nahi hui nahi ")
else:
    print("aap ke age ho chuke hai apply kar ne ke liya")
"""


# methot 2)
"""
if 18 <= age <= 28 :
    print("Valid Age")
elif age < 18 :
    print("Abhi omer nahi hui nahi ")
else:
    print("aap ke age ho chuke hai apply kar ne ke liya")
"""

# Both method is vaild


light = input("light :")

if(light == "red"):
    print("stop") 
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")


marks = int(input("marks :"))

if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks < 80):
    print("C")
else:
    print("D")


A= int(input("A:")) 
G = input("M/F :") 

if((A == 1 or A == 2) and G == "M"): 
    print("fee is 100")
elif(A == 3 or A == 4 or G == "F"): 
    print("fee is 200")
elif(A == 5 and G == "M"): 
    print("fee is 300") 
else: 
    print("no fee")


# ternary operator
a = 2
eat = "yes" if  a == 4 else "no" 
print(eat)


food = input("Food : ")
print("Nice") if food == "cake" or food == 'jalebi' else print("not nice")


# Clever IF ternary operator
age = int(input("Age : "))
vote = ("yes","no") [age >= 18]

sal = float(input("Salary :"))
tax = sal*(0.1,0.2) [sal>=50000]

print(tax)




