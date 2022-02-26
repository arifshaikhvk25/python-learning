# Detect spam :
# earn millions in one hour
# click to get rich
# download this for free
# link for movies


text = input("Enter the text:\n")

if("earn millions in one hour" in text) :
    spam = True
elif("click to get rich" in text):
    spam = True
elif("downlad this for free" in text):
    spam = True
elif("link for movies" in text):
    spam = True
else:
    spam = False

if(spam):
    print("this text is spam")
else :
    print("this is not a spam")


names = ["Muhammad", "Mohan", "Das", "Virat", "jeff",] # list names are in uppercase to check the present name in list
name = input("Enter name to check ")

if name in names:
    print("your name is in list")

else:
    print("your name is not present in list")


user = input("Enter the text:\n")

if("click button" in user):
    alert = True
elif("earn and fun" in user):
    alert = True
elif("music free"in user):
    alert = True
else:
    alert = False
if(alert):
    print("alert this might be spam")
else:
    print("see you again")


input = input("Enter your input:\n")

if input == "listen free music":
    print("warning")

elif input == "learn python in 2mins":
    print("be carefull")

elif input == "watch and earn":
    print("scam")
else:
    print("THANK YOU")

# finding the given user containe less than 10 character or not
user_name = input("Enter your name:\n")

if len(user_name) < 10:
    print("less")
else:
    print("not")

# Day 11
