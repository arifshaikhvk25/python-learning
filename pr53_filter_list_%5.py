# ## filter a list of numbers which divisible by 5

l1 = [2,3,4,45,678,98,45,78,69,879,4,8,78,43,5]

def mod (num):
    if num % 5 == 0:
        return num

print(list(filter(mod, l1)))

l2 = [23,43,5,6,7,8,45,67,89,0,87,776,55,7,4,6]

a = filter(lambda mod1 : mod1 % 5 == 0,l2)
print(list(a))

l3 = [2,3,4,5,7,68,5,78,56,5,3,5,65,]
lam = lambda mod2 : mod2 % 2 == 0
print(list(filter(lam,l3)))
