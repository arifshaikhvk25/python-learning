# making dictionary values enter by the user keys as there name
# keys must be different
# values can be same

fav_language = {}

a = input("Enter your favourite language Mohan : \n")
b = input("Enter your favourite language Das : \n")
c = input("Enter your favourite language Virat : \n")
d = input("Enter your favourite language Messi : \n")

fav_language["Mohan"] = a
fav_language["Das"]  = b
fav_language["Virat"] = c 
fav_language["Messi"] = d

print(fav_language)

fav_language = {}

a = input("Enter your favourite language Mohan : \n")
b = input("Enter your favourite language Das : \n")
c = input("Enter your favourite language Virat : \n")
d = input("Enter your favourite language Messi: \n")    # name not changed

fav_language["Mohan"] = a
fav_language["Das"]  = b
fav_language["Virat"] = c 
fav_language["Das"] = d     # keys should not be same 
                            # if the keys are same name has two friends in same qustion the latest value will be print

print(fav_language)


fav_language = {}

a = input("Enter your favourite language Mohan : \n")
b = input("Enter your favourite language Das : \n")
c = input("Enter your favourite language Virat : \n")
d = input("Enter your favourite language Das: \n")       # name changed

fav_language["Mohan"] = a
fav_language["Das"]  = b
fav_language["Virat"] = c 
fav_language["Das"] = d    #if the same name has two friends in same qustion the latest value will be print

print(fav_language)

# Day 9  
