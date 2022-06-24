# ## display a/b where a and b are integers . If b = 0, dispaly infinite by handling ZeroDIvisionError

a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

try :
    print(a/b)
except:
    print("infinite")
    