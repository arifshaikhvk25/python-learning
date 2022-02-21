# replace 

mail = '''Dear name
Your are selected in Apple, Google, Microsoft. 
Your Date of joining
Date : date
'''

name = input("Enter your name:\n")
date = input("Enter your date:\n")

mail = mail.replace("name",name)
mail = mail.replace("date",date)

print(mail)

# # Day 6

# # Day 7

important = '''Hie name
you need to learn short cut keys and Github.
Solve the problems in Hacker rank 
learn language
'''

name = input("Enter your name:\n")
language = input("language name:\n")
important = important.replace("name",name)
important = important.replace("language",language)
print(important)

letter = "Hello Github help me to add, status, commit, push "
# print(letter = "Hello Github help me to add, status, commit, push  "

formatted_letter = "Hello Github,\n\t help me!\n to add, status, commit, push "
print(formatted_letter)

