# ## find the maximum of the numbers in a list using the reduce functions

from functools import reduce

l1 = [23,34,2,354,56,68,79,809,7,45,354,534,345,335,325435,4534,345345,3453,45453465,345,324535,345]

a = reduce(max,l1)
print(a)

l2 = [23,34,5,2]

def sum (a, b):
    return a + b

print(reduce(sum,l2))

l3 = [23,4,5]
lam1 = lambda a, b: a + b
print(reduce(lam1,l3))

l4 = [2,4,5]
def mul1 (a, b):
    return a * b

print(reduce(mul1,l4))
