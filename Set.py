# Set in python
# Set is the collection of the unorderd items.
# Each element in the set must be unique & immutable

nums = {1,2,3,4}
set2 = {1,2,2,2} # repeated elements stored only once, so it resolved to {1,2}

null_set = {} # but this is not a empty set, this is a empty dictionary syntax
# if you want to create a empty set then you have to use set() function
null_set = set() # this is a empty set Syntax  

print("set : ",nums) # {1, 2, 3, 4}
print("type of set : ",type(nums)) # <class 'set'>

# sets ma hum boolean, integer, string, float, tuple ko save kar sakta hai kyu ke ya values immutable
# par hum list or dictionary ko hum Sets ma save nahi kara sakta hai kyu ke ya value mutables hote hai 


collection = {1,2,2,"hello","world","world"}
print("collection : ",collection) # {1, 2, 'hello', 'world'}
print(len(collection)) # 4 also len() remove the duplicate values and return the length of the set

# Set Methods
# 1. add() : add the element in the set
nums.add(5)
nums.add((1,2)) # adding tuple in the set unhashable and immutable so it is allowed

# 2. remove() : remove the element from the set, if the element is not present then it will raise an error
nums.remove(3) # removes 3 from the set output : {1, 2, 4, 5}

# 3. discard() : remove the element from the set, if the element is not present then it will not raise an error
nums.discard(10) # no error raised 

# 4. pop() : remove the random element from the set and return the removed element
removed_element = nums.pop()
print("removed element : ",removed_element) # 1

# 5. clear() : remove all the elements from the set
nums.clear() 

# 6. union() : return the union of two sets
set1 = {1,2,3}
set2 = {3,4,5}
union_set = set1.union(set2) # {1, 2, 3, 4, 5}

# 7. intersection() : return the intersection of two sets
intersection_set = set1.intersection(set2) # {3} combines common values & return new

# 8. difference() : return the difference of two sets
difference_set = set1.difference(set2) # {1, 2}

# set is mutable but the elements of the set must be immutable, so we can not add list or dictionary in the set but we can add tuple in the set because tuple is immutable
# Example of adding tuple in the set
set3 = {(1,2), (3,4)} # {(1, 2), (3, 4)}


# what is hashable in python?
# Hashable means that an object has a hash value which remains the same during its lifetime.
# example of hashable objects are int, float, string, tuple, frozenset etc.

# unhashable means that an object does not have a hash value or its hash value can change during its lifetime.
# example of unhashable objects are list, set, dictionary etc.


# frozenset in python
# frozenset is an immutable version of set, it means that we can not add or remove elements from the frozenset once it is created. It is hashable and can be used as a key in a dictionary or as an element of another set.


# Let's see an example of frozenset in python
fset = frozenset([1,2,3,4])
print("frozenset : ",fset) # frozenset({1, 2, 3, 4})
print("type of frozenset : ",type(fset)) # <class 'frozenset'>

# Let's Practice some frozenset methods
# 1. union() : return the union of two frozensets
fset1 = frozenset([1,2,3])
fset2 = frozenset([3,4,5])
union_fset = fset1.union(fset2)
print("Union of frozensets : ",union_fset) # frozenset({1, 2, 3, 4, 5})

# 2. intersection() : return the intersection of two frozensets
intersection_fset = fset1.intersection(fset2)
print("Intersection of frozensets : ",intersection_fset) # frozenset({3})

# 3. difference() : return the difference of two frozensets
difference_fset = fset1.difference(fset2)
print("Difference of frozensets : ",difference_fset) # frozenset({1, 2})

# 4. isdisjoint() : return True if two frozensets have no elements in common, otherwise return False
is_disjoint = fset1.isdisjoint(fset2)
print("Are frozensets disjoint? : ",is_disjoint) # False

# Let's Practice 
# Store following word meanings in a python dictionary :
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

meanings = {
    "table" : ["a piece of furniture", "list of facts & figures"],
    "cat" : ["a small animal"]
}


# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"

subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# we can use set to find the unique subjects and then we can find the length of the set to find the number of classrooms needed
unique_subjects = set(subjects)
print("Unique subjects : ",unique_subjects) # {'python', 'java', 'C++', 'javascript', 'C'}
print("Number of classrooms needed : ",len(unique_subjects)) # 5


# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.
marks = {}

x = int(input("Enter marks of subject 1 : "))
marks.update({"subject 1" : x})

y = int(input("Enter marks of subject 2 : "))
marks.update({"subject 2" : y})

z = int(input("Enter marks of subject 3 : "))
marks.update({"subject 3" : z})

print("Marks of all subjects : ",marks)


# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
values = {9, 9.25}
print("Values in the set : ",values) # {9}

# if we write 9 or 9.0 in the set then it will be considered as same value because both are equal in python, so it will store only one value in the set.

# if we want to store 9 and 9.0 as separate values in the set then we can use tuple or string to store them as separate values
values = {9, 9.0, (9,), "9"}
print("Values in the set : ",values) # {9, 9.0, (9,)}