import os
# File I/O in python
# Python can be used to perform operations on a file. (read & write data)

# Type of all files
# 1. Text File : .txt, .docx, .log etc
# 2.Binary Files : .mp4, .mov, .png, .jpeg, etc.

# Open, read & close File
# we have to open a file before reading or writing.

# f = open("file_name","mode")
            #  |          |
            #  |          |------> r:read mode <--- default parameter
            #  |          |------> w:write mode
            #  |          
            #  |----->saample.txt,domo.docx

# data = f.read()
# f.close()
 
 
file = open("demo.txt","r") # r mean read mode on file
data = file.read() # ek bar ager mana data ko read kar liya to uska bad ab next line ma uska pas kuch read karne ka liya kuch hoga he nahi ager phale he hum file ka data read kar le to readline ka pas kuch hoga he nahi read karne ke liya
fiveLatters = file.read(5) # 5 likh ne sa ap ma file ka starting ka 5 latters ko read kar pauga (file ka starting ka 5 latters ko access kar paguga)
line1 = file.readline() # abma file ka first line ko access kar pauga
line2 = file.readline() # abma file ka second line ko access kar pauga

print(data)
print(fiveLatters)
print(type(data))
print(file)
print(type(file))


file.close()



# overwak

# Character    Meaning
# 'r'          open for reading (default)
# 'w'          open for writing, truncating the file first (puri file ka data overwrite kar deta hai)
# 'x'          create a new file and open it for writing
# 'a'          open for writing, appending to the end of the file if it exists (data overwrite nahi karta hai existsing data ma new data add kar deta hai file ke end ma)
# 'b'          binary mode
# 't'          text mode (default)
# '+'          open a disk file for updating (readina and writing)
# rt or r+     text file ma read or write ke liya
# rd           binary file me read or write ke liya
# w+           read or file dono ke liya 
# a+           data add (append) or read ke liya 


# Reading a file
# data = f.read() reads entire file
# data = f.readline() reads one line at a time

#  Writing to a file
writeFile = open("demo.txt","w")

writeFile.write("\nthen I'll move to react.js")

writeFile.close()


# ager hum kesi bhi file ko "w" ya "r" mode me open karte hai par wo exists nahi karte to file automatic create hogate hai 
f = open("sample.txt","w+")
# After writing  characters, the file cursor moves forward by 3 (ABC) positions.
f.write("ABC")
f.seek(0)  # Move cursor to the beginning
print("reading",f.read())

f.close()



# with Stntax
# with open("demo.txt","a") as f:
        #   data = f.read()
    
# example
with open("sample.txt","w+") as f:
    f.write("then I'll move to react.js")
    f.seek(0)
    data = f.read()
    print(data)


# Deleting a file using os module
# Module (like a code library) is a file written by another programmer that generally has a functions we can use

# import os
# os.remove(filename)

os.remove("sample.txt") # after execute this line sample.txt is deleting


with open("practice.txt","w") as f:
    f.write("Hi everyone \nwe are learing File I/O\n")
    f.write("using java \nI like programming in Java.")



def replace_text(file, old_text, new_text):
    with open(file,"r") as f:
        data = f.read()
    data = data.replace(old_text,new_text)

    with open(file,"w") as f:
        f.write(data)


replace_text("practice.txt", "Java", "JavaScript")


with open("demo.txt","r") as f:
    data = f.read()
new_data = data.replace("react.js","node")

print(new_data)

with open("demo.txt","w") as f:
    f.write(new_data)



def checkWord(file,word):
    with open(file,"r") as f:
      data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not Found")  

checkWord("demo.txt","node")

def check_for_line(file,word):
    data = True
    line_no = 1
    with open(file,"r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print(line_no)
                return
            line_no+=1

check_for_line("practice.txt","learing")


with open("practice2.txt","r") as f:
    data = f.read()
    print(data)
    num = ""
    for i in range(len(data)):
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]


count = 0
with open("practice2.txt","r") as f:
    data = f.read()
    print(data)
    nums = data.split(",")
    for val in nums:
        if(int(val) % 2 == 0):
            count+=1

print(count)
