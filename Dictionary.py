# Dictionaries are used to store data values in key:value paire
# They are unorderd, mutable(changeable) & don't allow dublicate keys

dict = {
    "name":"shradha",
    "cgpa":9.6,
    "marks":[98,97,95],
    "tup":(45,78,43,78),
    "bool":True,
    "int":5,
    "obj":{
        "pro1":"javascript",
        "pro2":"python"
    },
    12.99:94.4
}

print(dict["name"])
print(dict["cgpa"])
print(dict["marks"])


print(dict)
print(type(dict))

print(dict["obj"]["pro2"])

# how to overwrite a value
dict["name"] = "harsh" 

#how to add new key value
dict["key"] = "value"

#empty dictionary

null_dict = {}
null_dict["name"] = "zodX"

print(null_dict)


# Nested Dictionaries

student = {
    "name":"shivam",
    "age":21,
    "subject":{
        "phy":97,
        "Maths":98,
        "Chem":95,
    }
}

print(student)
print(student["subject"])
print(student["subject"]["phy"])

# Dictionary Methos
print("Dictionary Methos")

myDict = {
    "name":"harsh",
    "company":"Google",
    "salary":2500,
    "Role":"Frontend",
    "department":"IT"
}



# myDict.keys() returns all keys
print(myDict.keys()) # output is dict_keys(['name', 'company', 'salary', 'Role', 'department'])

# myDict.values() returns all values
print(myDict.values()) # output is dict_values(['harsh', 'Google', 2500, 'Frontend', 'IT'])

# myDict.items() returns all (key,val) prirs as tuples
print(myDict.items()) # output is dict_items([('name', 'harsh'), ('company', 'Google'), ('salary', 2500), ('Role', 'Frontend'), ('department', 'IT')])
pairs = list(myDict.items())
print("list(myDict.items()) = ",pairs[0]) # ('name', 'harsh')

# myDict.get("key") return the key accordind to value
# print(myDict["name2"])  if key is not exits then engine return Error 
print(myDict.get("name2")) # if key is not exits then engine return None 
print(myDict.get("name")) # output is harsh

# myDict.update(newDict) insert the specified items to the dictionary
myDict.update({"city":"delhi"})
new_Dict = {}
new_Dict.update(myDict)
print("update Dictionary : ",new_Dict)

# lenght of Dictionary
print(len(myDict))

# how to convert Dictionary into List or Tuple
# Dictionary into List
DictionaryIntoList = list(myDict)   # ['name', 'company', 'salary', 'Role', 'department']
DictionaryIntoListKey = list(myDict.keys())  #['name', 'company', 'salary', 'Role', 'department']
print(DictionaryIntoListKey)
# print(type(DictionaryIntoList)) <class 'list'>

# Dictionary into tuple
DictionaryIntoTuple = tuple(myDict) # ('name', 'company', 'salary', 'Role', 'department')
DictionaryIntoTupleValues = tuple(myDict.values())  # ('harsh', 'Google', 2500, 'Frontend', 'IT')
print(DictionaryIntoTupleValues) 
# print(type(DictionaryIntoTuple))<class 'tuple'>



