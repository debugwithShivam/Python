# List in Python
# A build-in data type that store aet of values it can store elements of different types (interer float,string,etc.)

marks = [87,64,33,95,76]
student = ["Karan",85,"delhi"]
student[0] = "Arjun"
lenghtofArray = len(student)

print(lenghtofArray)

print(type(marks))
print(marks[0])
print(marks[1])

# List Slicing
# Similap to String Slicing

# list_name[start_idx:end_idx] #ending idx in not included
marks = [34,67,23,56,78]
marks[1:4] # is 67,23,56 
print(marks[1:4]) # output is [67,23,56 ]

# Negitivie Slicing
print(marks[-3:-1]) # output is [23,56]


# List method

list = [2,1,3,1]

print(list.count(1)) #Return number of occurrences of value.


list.remove(1) #remove first occurrence of element [2,3,1] from starting
print(list)

list.pop(2) #remove element at index []
print(list)

list.append(4) # Adds one element at the end
print(list)

list.sort() # sorts in ascending order
print(list)

list.sort(reverse=True) #sorts in decending order
print(list)

list.reverse() # reverses list [5,4,6,3,1,2]
print(list)


list.insert(1,10) #insert element at index list.index(indexElement,element)
print(list)


