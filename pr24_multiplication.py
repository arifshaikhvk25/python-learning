## multiplication table using for loop

num = int(input("Enter number:\n"))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

num = int(input("Enter number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

num = int(input("Enter number: "))
i = 1
while i<=10:
    print(f"{num} X {i} = {num*i}")
    i += 1

num = int(input("Enter number:\n"))
i = 1
while i < 11:
    print(f"{num} X {i} {num*i}")
#     i += 1


## mnultiplication table using def function

nm = int(input("Enter number:  "))
def multiplication(num):
    for i in range(1,11):
        print(num * i)
    
    ##return num

n =  multiplication(nm)
# print(n)

user = int(input("Enter Number:  "))
def table(number):
    for i in range(1,11):
        print(f"{number} X {i} = {number*i}")

num = table(user)

###################################################################################################################################

## muliplication in reverse

num = int(input("Enter number:  "))
for i in range(10,0,-1):
    print(f"{num} X {i} = {num*i}")

num = int(input("Enter number:  "))
for i in list(range(11-1,-1,-1)):
    print(num*i)






