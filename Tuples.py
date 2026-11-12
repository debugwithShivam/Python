# A build-in data type that lets us create immutable sequences of values.

tup = (87,64,33,95,76)

# tup[0] = 43 <-- NOT allowes in python

tup1 = (1) # <- Just an integer inside parentheses. Integer (int) type is  <class 'int'> same ager yaha par ager koi float , string ,boolean hota () bracket ke ander to python us ko data type ke hisab sa convert kar deda un ko tuple nahi samjha ta 
tup2 = (1,) # A tuple containing one element. type is <class 'tuple'>
tup3 = (1,2,3)

#tuples ma sigle value ka sath comma lagana jarure hai warna python us ko us ka data type ke hisab sa us ko change kar deta hai 

print(type(tup)) #<class 'tuple'>
print(tup[0]) # output is 87
print(tup[1]) # output is 64

#slicing in tuples
print(tup[1:3]) # 64,33

# tuple Methods
tup = (2,1,3,1,4,1)
tup.index(1) #returns index of first occurrence
print(tup.index(4))
tup.count(2) #count total occurrence
print(tup.count(1))

# Let's Practice
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
movie1 = str(input("enter your third fav move name : "))
movie2 = str(input("enter your second fav move name : "))
movie3 = str(input("enter your first fav move name : "))

tupleMovie = (movie1,movie2,movie3)
print(tupleMovie)

# with Array
movies = [] 
mov = str(input("enter your third fav move name : "))
movies.append(mov)
mov = str(input("enter your second fav move name : "))
movies.append(mov)
mov = str(input("enter your first fav move name : "))
movies.append(mov)

print(movies)

list1 = [1,2,1]
list2 = [1,2,3]

copy_list1 = list1.copy() #Return a shallow copy of the list.
copy_list1.reverse()

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("not Palindrome")