# greet person name stored in list start with M
# using .startswith method 

list1 = ["Mohan Das","Apple","Google","Mohd Arif","Amazon","Microsoft"]
## for i in list1:
for name in list1:
    if name.startswith("M"):
        print(f"Hello {name}, Have A Good Day")

brand = ["Apple","Microsoft","Amazon","Google","Tata","Github"]
for i in brand:
    if i.startswith("A"):
        print(f"Hola {i}")

## brand = ["Apple","Microsoft","Amazon","Google","Tata","Github"]
## for i in brand:
##     if i.startswith("A") and i.startswith("G"):
##         print(f"Hola {i}")


brand = ["Apple","Microsoft","Amazon","Google","Tata","Github"]
for i in brand:
    if i.startswith("A"):
        print(f"Hola {i}")
    elif i.startswith("G"):
        print(f"one day i will be the best coder of {i}")
    else:
        print(f"The best {i}")





