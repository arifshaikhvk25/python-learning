# escape sequence string

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


















# Day 6