## find greatest number using function

def greatest (num1, num2 ,num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3

g = greatest(5,25,19)
print(f"The Greatest value is {g}")

###############################################################################

# # def greatest (num1, num2 ,num3):
# #     if num1 > num2:
# #         return num1
# #     elif num2 > num1:
# #         return num2
# #     elif num2 > num3:
# #         return num2
# #     elif num3 > num2:
# #         return num3
# #     elif num3 > num1:
# #         return num3
# #     elif num1 > num3:
# #         return num1

# # great = greatest(5,25,1999)
# # print(great)

###############################################################################








