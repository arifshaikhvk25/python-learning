# Dictionary
'''
months = {
    "jan" : "january",
    "feb" : "february",
    "mar" : "march",
    "apr" : "april",
    "may" : "may"
}
print("options are ", months.keys())
a = input("Enter Month:\n")
print("name of Month ",months[a])

dictionary = {
    "s" : "shaikh",
    "m" : "muhaamad",
    "a" : "arif",
    "l" : "learning",
    "p" : "python"
}

print("options are ",dictionary.keys())
b = input("Enter Alphabet:\n")
print("The name is ", dictionary[b])'''

meaning = {
    "kitab" : "book",
    "khana" : "food",
    "paisa" : "money",
    "zindagi" : "life",
    "prayer" : "namaz"
}

print("options are ",meaning.keys())
c = input("Enter word:\n")
# print("The meaning of your word is", meaning[c])   # this throws an error if key is not present in the dictionary
print("The meaning of your word is", meaning.get(c)) # this will return None if key is not present in the dictionary

meaning = {
    "ghadi" : "watch",
    "paisa" : "money",
    "dhup" : "sun",
    "chand" : "moon"
}
print("options are ", meaning.keys())
d = input("Enter Hindi Word:\n")
print("The meaning of your Word is",meaning.get(d))

#  Day 9
