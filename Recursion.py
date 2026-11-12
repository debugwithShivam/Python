# Recursion
# When a function calls itself repeatedly

# print n to 1 backwords
def show(n):
    if n == 0:
        return
    print(n)
    show(n-1)
    print("end")

show(5) 


def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

print(fact(5))

def calc_Sum(n):
    sum = 0
    if(n==0):
        return 0
    return calc_Sum(n-1)+n

calc_Sum(5)
print(calc_Sum(5))

def print_list(list,idx):
    if(idx==len(list)):
        return 
    print(list[idx],end=" ")
    print_list(list,idx+1)

fruits = ["mango","litchi","apple","banana"]

print_list(fruits,0)