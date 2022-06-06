# printing the star patern

n = 4
for i in range(1,n+1):
    print("*" * i)

a = 4
for i in range(a):
    print("*" * (i+1))

for i in range(4):
    print("*" * (i+1))


## star = 4
## for i in range(1,star+1):
##    print(" " * (star-i-1), end = " ")
##     print("*" * (3*i+1), end = " ")
##     print(" " * (star-i-1))


star = 3
for i in range(3):
    print(" " * (star-i-1), end = " ")
    print("*" * (2*i+1), end = " ")
    print(" " * (star-i-1))

n  = 5
for i in range(n):
    print("*" * (n-i))



