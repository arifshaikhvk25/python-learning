# ## print fifth, sixth and seventh element from the list using enumerate function 

list1 = [21,34,64,76,87,9,4,54,76,67,87945,346,65]

for index,item in enumerate (list1) :
    if index == 4 or index == 5 or index == 6:
        print(f"The {index +1}th element is {item}")      ## index+1 is written so that index should start with the 1

        # ##print(index,item)


list2 = [21,34,64,76,87,9,4,54,76,67,87945,346,65]

for index,item in enumerate (list2):
    if index == 2:
        print(f"The {index +1}rd element is {item} ")
    elif index == 4 or index == 6 :
        print(f"The {index +1}th element is {item}")
