# remove word from string and strip at same time

# .strip()
# strip means remove the spaces from the string

name = "    Shaikh Mohd Arif    "                 ## .strip() function will remove the space from the string
print(name.strip())


def remove_strip(string, word):
    str = string.replace(word,"")
    return str.strip()

name = "     Shaikh Mohd Arif     "
rs = remove_strip(name,"Shaikh")
print(rs)
