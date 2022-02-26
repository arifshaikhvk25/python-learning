# marks enter by the user
#  check or fail

marks1 = int(input("Enter your marks1 :\n"))
marks2 = int(input("Enter your marks2 :\n"))
marks3 = int(input("Enter your marks3 :\n"))

if (marks1<33 or marks2<33 or marks3<33):
    print("Fail! you have less than 33% in one subject")

elif (marks1+marks2+marks3)/3< 40:
    print("Your fail to total percentage less than 40%")

else:
    print("Your pass")


sub1 = int(input("Enter you marks :\n "))
sub2 = int(input("Enter you marks :\n "))
sub3 = int(input("Enter you marks :\n "))
sub4 = int(input("Enter you marks :\n "))

if (sub1+sub2+sub3+sub4)/4 < 37:
    print("Fail! you have less than 37 ")

elif (sub1<35 or sub2<35 or sub3<35 or sub4<35):
    print("Fail! you have less than 35 in one subject")

else:
    print("congratulation your PASS")

# Day 11
