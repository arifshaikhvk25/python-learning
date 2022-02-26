# find the greatest number enter by the user

num1  = int(input("Enter the number 1:\n"))
num2  = int(input("Enter the number 2:\n"))
num3  = int(input("Enter the number 3:\n"))
num4  = int(input("Enter the number 4:\n"))

if num1>num4:
    a1 = num1
else:
    a1 = num4

if num2>num3:
    a2 = num2
else:
    a2 = num3

if a1>a2:
    print(f"{a1} is greatest")
else:
    print(f"{a2} is greatest")


num1  = int(input("Enter the number 1:\n"))
num2  = int(input("Enter the number 2:\n"))
num3  = int(input("Enter the number 3:\n"))
num4  = int(input("Enter the number 4:\n"))
# num5  = int(input("Enter the number 5:\n"))

if num1>num4:
    b1 = num1
else:
    b1 = num4

if num2>num3:
    b2 = num2
else:
    b2 = num3

if b1>b2:
    print(f"{b1} is greatest")
else:
    print(f"{b2} is greatest")
    

# find out wheather the post is talkng about "Google " or not

post = '''
"I just hope my 
Death
makes more cents..
than my life." 
'''

if post == post.find("death") in post:              # finding with find function
    print("The post is talking about the death")
else :
    print("this post is not talking about the death")


if "Death"  in post:
    print("This post is talking about the Death")
elif "DEATH" in post:
    print("This post is talking about the Death")
elif "death" in post:
    print("This post is talking about the Death")
elif "DeAth" in post:
    print("This post is talking about the Death")
else:
    print("This post is not talking about the death")


# find out wheather the post is talkng about "Google " or not

post = '''
"I just hope my 
DeAth
makes more cents..
than my life." 
'''
print(post.find("Death"))
print(post.find("death"))
print(post.find("DeAth"))


# not done 
# find the greatest number enter by the user

# num1  = int(input("Enter the number 1:\n"))
# num2  = int(input("Enter the number 2:\n"))
# num3  = int(input("Enter the number 3:\n"))
# num4  = int(input("Enter the number 4:\n"))
# num5  = int(input("Enter the number 5:\n"))

# if num1>num2:
#     a1 = num1
# elif num5>num1:
#     a1 = num5
# elif num2>num3:
#     a2 = num2
# elif num3>num2:
#     a2 = num3
# else:
    
# Day 11
