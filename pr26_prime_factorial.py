# find given number is prime or not
# find factorial of given number
# find sum of first n natural number using while loop

num = int(input("Enter number: "))
prime = True
for i in range(2,num):
    if num % i == 0:
        prime = False
        break
if prime:
    print("This number is prime")
else:
    print("This is not a prime number")


number = int(input("Enter number to check its prime or not:\n"))
prime = True
for i in range(2,number):
    if number % i == 0:
        prime = False
if prime:
    print(f"{number} is prime number")
else:
    print(f"{number} is not a prime number")

######################################################################################################################################################
# factorial

num = int(input("Enter Number: \n"))
factorial = 1
for i in range(1,num+1):
    factorial *= i
    print(i)
print(factorial)

number = int(input("Enter Number to check the factorial: "))
fact= 1
for i in range(1,number+1):
    fact *= i
print(f"Factorial of {number} is {fact}")

n = 5
fact_num = 1
for i in range(n):
    fact_num *= i+1
print(f"The factorial of {n} is {fact_num}")

########################################################################################################################################################
# sum of natural number

n = int(input("Enter number: "))
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
    print(sum)

## n = int(input("Enter number: "))
## sum = 0 
## i =1
## while i<n+1:
##    sum+=1
##     i+=1
##      print(sum)
# # i+= 1
