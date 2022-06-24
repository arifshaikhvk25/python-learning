# ## list contains multiple table write a program to convert it to a vertical string of same number (5)
# ##                                                                                             ##  (10)

user = int(input("Enter a Number :  "))
a = []
for i in range(1,11):
    a.append(i*user)
print(a)

l1 = [i * 5 for i in range(1,11)]          ## list comprehension
print(l1)

vertical_table = "\n".join(l1)           ## to join we have to typecaste in string str() .join() joins the string 
print(vertical_table)                    ## this will throw error -> TypeError: sequence item 0: expected str instance, int found

l1 = [str(i*5) for i in range (1,11)]
print(l1)                                 ## this will print the table in strings because its typecaste in str() and in horizontal list

vertical_table = "\n".join(l1)
print(vertical_table)                    ## this will print the list in vertical

l2 = ["Apple", "Amazon", "Google", "Microsoft"]
vt1 = "\n".join(l2)
print(vt1)
