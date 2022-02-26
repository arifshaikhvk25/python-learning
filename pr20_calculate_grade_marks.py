# calcultae the  grade of a student from his marks

marks = int(input("Enter your marks:\n"))

if marks > 100:
    print("invalid marks")

elif marks >= 90 and marks <= 100 :
    print("Grade Ex")

elif marks >= 80 and marks <= 90 :
    print("Grade A")

elif marks >=70 and marks <= 80 :
    print("Grade B")

elif marks >= 60 and marks <= 70 :
    print("Grade C")

elif marks >= 50 and marks <= 60 :
    print("Grade D")

else :
    print("Your FAIL!")


marks = int(input("Enter your marks:\n"))

if marks >= 90:
    grade  = "Ex"

elif marks >= 80 :
    grade = "A"

elif marks >= 70 :
    grade = "B"

elif marks >= 60 :
    grade = "C"

elif marks >= 50 :
    grade = "D"

else :
    grade = "F"

print("your grade is " + grade)

# Day 11
