# ## list comprehension contain multiplication table entered by the user

num1 = int(input("Enter a number: \n"))

a = [num1*i for i in range (1,11)]              ## list comprehension
print(a)


num2 = int(input("Enter a number: \n"))

b = []
for i in range (1,11):
    b.append(num2*i)
print(b)
