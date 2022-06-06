
a = 10
for a in range(1, a):
    str = ""
    for b in range(a):
        str = str + "* "
    print(str)
for a in range(a, 0, -1):
    str = ""
    for c in range(a):
        str = str + "* "
    print(str)

i = 5
for i in range(1,5):
    str = " *" 
    print(str)
    for j in range(i):
        print(str)
        str = str + "*"
    print(i,str)

for i in range(1,4):
    for j in range(i):
        print(i)


str = "mohan"
i = len(str) - 1
while True:
    if i == -1:
        break
    print(str[i])
    i = i - 1

for i in range(5,1,-1):
    print(i)

a = "arif"
b = len(a)
# for i in range(b):
for i in range(b-1,-1,-1):
    if a == "r" in b:
        print("R")
    print(i,a[i])
print(i,a[i])
    

a = "arif"
b = len(a)
# end = ""
for i in range(b-1,-1,-1):
    # end = ""
    print(a[i])

a = "arif"
for i in range((len (a)-1),-1,-1):
    print(a[i])

i = 5
for i in range (1,i):
    str = ""
    for j in range (i):
        str = str + " *"
    print(str)

for i in range(i,0,-1):
    str = ""
    for k in range(i):
        str = str + " *"
    print(str)


for i in range (3):
    print("Arif")

lists = ["shiakh", "mohd", "arif",]
for list in lists:
    print(list)

lists = ["shiakh", "mohd", "arif",]
for lists in lists:
    print(lists)

for i in range (1,4):
    print( "python",i, i * "*")


lists = (12)
for list in range(1,lists):   # prints 11***********
    str = "*"
    print(list, list * str)

for i in range (1,5):
    print("python",i,i * "*")

a = 10
for i in range(1,a,2):
    print(i,i * "*")

successful = False
# successful = True
for i in range(1,3):
    print("Attempt",i)
    if successful:
        print("successful")
        break
else:
    print("Attempted 2 times and FAILED")


# message = True
message = False

for i in range (1,4):
    print("message",i)
    if message :
        print("message sent")
        break
else :
    print("3 messages ")

for x in range (5):
    for y in range(3):
        print(x,y)

numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    if number%2==0:
        print(f"{number} is even number")
    elif number in numbers:
        if number%2==1:
            print(f"{number} is odd number")
    
for i in range (1,20):
    if i % 5 == 0:
        print(f"{i} is even number")
    else:
        print(f"{i} is odd number")

count = 0
for i in range(1,10):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"we have {count} even number")       # Doubt


a = ["Apple","Google","Microsoft"]
for i in a:
    print(i)

b = [5,10,5]
total = 0
for i in b:
    total += i
print(total)

count = 0
for i in range(1,10):
    if i % 2 == 0:
        count += 1
        print(i)
print(f"we have {count} even number")

total = 0
a = list(range(1,20))
for i in range(1,20):
    if i % 2 == 0:                          # how to add remainder in list
        total +=1
        print(i,a)
    # else:
    #     print("odd numbers")
print(f"we have {total} even numbers")

sum = 0
for i in range(1,5):
    sum += i
print(sum)
    # sum += i

total1 = 0
print(list(range(1,20)))
for i in range(1,20):
    if i % 3 == 0:
        total1 += i
        print(i)
total2 = 0
for i in list(range(1,20)):
    if i % 5 == 0:
        total2 +=1
        print(i)
print(f"total {total1} numbers are multiple of 3 and\ntotal {total2} numbers are multiple of 5")

for i in list(range(1,20)):
    if i % 5 == 0:
        print(i)


total = 0
print(list(range(1,20)))
for i in range(1,20):
    if i % 3 == 0:
        total += i

       # # print(i)
    elif i % 5 == 0 :

        total += i
       # print(i)
print(total)


total = 0
print(list(range(1,20)))
for i in range(1,20):
    if i % 3 == 0 or i % 5 == 0:
        total += i
        # print(i)
print(total)

total = 0
print(list(range(1,20)))
for i in range(1,20):
    if i % 3 == 0 and i % 5 == 0:
        total += i
print(total)
        

lists = [["Apple",5], ["Google",4], ["Microsoft",3], ["Tata",2]]
for list, numbers in  lists :
    print(list,numbers)

lists = [["Apple","a"], ["Google","g"], ["Microsoft","m"], ["Tata","t"]]
dict = dict(lists)
print(dict)
# for list, numbers in dict.items() :  # to  print the items (values) of the dictionary dict.items()
for list, numbers in lists :
    # len(lists) ==-1
    print(list,numbers)

print(len(lists))


lists = [["Apple","a"], ["Google","g"], ["Microsoft","m"], ["Tata","t"]]
dict = dict(lists)
print(dict)
for list,numbers in dict.items():
    print(list)

lists = [["Apple","a"], ["Google","g"], ["Microsoft","m"], ["Tata","t"]]
for list,numbers, in lists:
    print(list)


a = ["apple","microsoft","google",345,56,765,8,345,68,3656,5873,24,6669,543,6,3245]
for i in a:
    if str(i).isnumeric() and i >=569:
        print(i)
    if i == "apple"in a:#and i == "google":
        print(i)

list = ["Apple", "Microsoft","Google","Facebook"]
for list in "Apple" " Google":
    print(list)

lists = ["Apple", "Microsoft","Google","Facebook"]
for list in lists :
    print(list)

    if list == "Microsoft":
        break
print(list)

lists = ["Apple", "Microsoft","Google","Facebook"]
for list in lists:
    print(list)
    if list == "Microsoft":
        continue
