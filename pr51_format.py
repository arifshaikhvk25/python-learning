# ## format

name = input("Enter your name: \n")
marks = int(input("Enter your marks: \n"))
phone = int(input("Enter phone number: \n"))

detail = "The name of the user is {} his marks are {} and phone number is {}".format(name, marks, phone)
# print(detail)

name1 = input("Enter your name :  ")
age = int(input("Enter your age :  ")) 
system = input("Enter your system name :  ")

info = "The name of the user is {} he is {} years old and name of his laptop is {}"
output = info.format(name1, age, system)
print(output)
