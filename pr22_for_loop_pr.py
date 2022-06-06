
for i in range(1,5):
        for j in range(1,5):
                print("* ",end="")
        print("\n")

for i in range(1,5):
        for j in range(1,i+1):
                print("*",end="")
        print()

for i in range(5,0,-1):
        for j in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5+1):
        for j in range(1,i+1):
                print("*",end="")
        print()

for i in range(5,0,-1):
        for j in range(1,i):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5-1):        ## this will print the 3 space cuz the i is (5 will not include ,4) and in 2nd loop j (5,4) 5 - 1 this is 3 cuz the 5 will not include so that is 4 -1 is 3 it will print 3 spaces 
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end="")
        print()

for i in range(4,0,-1):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end="")
        print()

###################################################################################################
class Pattern():
        def __init__(self,num):
                self.num = num
                for i in range(1,num):
                        for j in range(1,i+1):
                                print("*",end="")
                        print()
        @staticmethod
        def greet():
                print("Very Nice")

star = Pattern(5)
star.greet()
#############################################################################################

for i in range(1,5):                                              ## ****
        for j in range(1,5):                                      ## ****
                print("*",end="")                                 ## ****
        print()                                                   ## ****
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                              ## *
        for j in range(1,i+1):                                    ##  **
                print(" ",end="")                                 ##   ***
        for k in range(1,i+1):                                    ##    ****
                print("*",end="")
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                           ##     *****
        for j in range(1,i+1):                                    ##    ****
                print(" ",end="")                                 ##   ***
        for k in range(1,i+1):                                    ##  **
                print("*",end="")                                 ## *
        print()
print("###############################")

for i in range(1,5):                                              ##    *
        for j in range(1,5-1):                                    ##    **
                print(" ",end="")                                 ##    ***
        for k in range(1,i+1):                                    ##    ****
                print("*",end="")                                 
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                            ##    *****
        for j in range(1,6-1):                                     ##    ****
                print(" ",end="")                                  ##    ***
        for k in range(1,i+1):                                     ##    **
                print("*",end="")                                  ##    *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                               ## *
        for j in range(1,i+1):                                     ## **
                print("*",end="")                                  ## ***
        print()                                                    ## ****
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                            ## *****
        for j in range(1,i+1):                                     ## ****
                print("*",end="")                                  ## ***
        print()                                                    ## **
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")                       ## *

for i in range(1,5):                                                 ##    *
        for j in range(1,5-1):                                       ##    ***
                print(" ",end="")                                    ##    *****
        for k in range(1,(2*i-1)+1):                                 ##    *******
                print("*",end="")
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                               ##    *********
        for j in range(1,5-1):                                        ##    *******
                print(" ",end="")                                     ##    *****
        for k in range(1,(2*i-1)+1):                                  ##    ***
                print("*",end="")                                     ##    *
        print()                                                       
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")

for i in range(1,5):                                                 ## *
        for j in range(1,(2*i-1)+1):                                 ## ***
                print("*",end="")                                    ## *****
        print()                                                      ## *******
print("#################################")

for i in range(5,0,-1):                                              ## *********
        for j in range(1,(2*i-1)+1):                                 ## ******* 
                print("*",end="")                                    ## *****
        print()                                                      ## ***
print("####################################")                        ## *

for i in range(1,5):                                                   ##    *
        for j in range(1,5-i):                                         ##   **
                print(" ",end="")                                      ##  ***
        for k in range(1,i+1):                                         ## ****  
                print("*",end="")
        print()
print("#################################")

for i in range(5,0,-1):                                                  ##  ***** 
        for j in range(1,6-i):                                           ##   **** 
                print(" ",end="")                                        ##    ***
        for k in range(1,i+1):                                           ##     **
                print("*",end="")                                        ##      *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                                   ##  *
        for j in range(1,i+1):                                         ##   ***
                print(" ",end="")                                      ##    *****
        for k in range(1,(2*i-1)+1):                                   ##     *******
                print("*",end="")
        print()
print("###################################")

for i in range(5,0,-1):                                                  ##      *********
        for j in range(1,i+1):                                           ##     *******
                print(" ",end="")                                        ##    *****
        for k in range(1,(2*i-1)+1):                                     ##   ***
                print("*",end="")                                        ##  *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                                  ##    *
        for j in range(1,5-i):                                        ##   ***
                print(" ",end="")                                     ##  ***** 
        for j in range(1,(2*i-1)+1):                                  ## *******
                print("*",end="")
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                                 ## *********
        for j in range(1,6-i):                                          ##  *******
                print(" ",end="")                                       ##   *****
        for k in range(1,(2*i-1)+1):                                    ##    ***
                print("*",end="")                                       ##     *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    

####################################################################################################################################################

# ##for loop practice

# print by for loop 

a = "Shaikh Mohd Arif"
for name in a:
    print(name)

# reversed the variable

a = "Shaikh Mohd Arif"
for i in range((len(a)-1),-1,-1):
    print(a[i])
    
a = "Shaikh Mohd Arif"
string = len(a)
for i in range(string-1,-1,-1):
    print(a[i])


# list printed by the for loop

companies = ["Apple","Google","Microsoft","Facebook","Twitter","Github"]
for company in companies:
    print(company)


# list printed reversed

companies = ["Apple","Google","Microsoft","Facebook","Twitter","Github"]
for company in range(len(companies )-1,-1,-1):
    print(companies[company])

companies = ["Apple","Google","Microsoft","Facebook","Twitter","Github"]
length = len(companies)
for i in range(length-1,-1,-1):
    print(companies[i])








# ##print 2nd element of list in python using for loop
# ##not done

 





brands = ["Apple","Google","Microsoft","Facebook","Twitter","Github"]
# elemnts = brands[2]
# print(elemnts)
# lenght = len(brands)

for brand in brands:
    # lenght = (len(brand))
    print(brand[2])
        

# ##find even odd numbers from list

total_even_numbers = 0
total_odd_numbers = 0
# count_all = 0

integers = [1,2,3,4,5,6,7,8,9,10]
for number in integers:
    if number % 2 == 0:
        total_even_numbers += 1
        
        print(number,"even numbers")
    elif number % 2 == 1:
        total_odd_numbers += 1
       
        print(number,"odd numbers")
print(f"total {total_even_numbers} even numbers\ntotal {total_odd_numbers} odd nmbers")
# print(f"total {total_even_numbers} even numbers\ntotal {total_odd_numbers} odd numbers\n {count_all}")


# ##find even numbers from list

integers = [1,2,3,4,5,6,7,8,9,10]

for number in integers:
    if number % 2 == 0:
        print(number)

# ##printing the star

for i in range(1,5):
    for j in range(1,i+1):
        print(i,j)


# factorial

a = 5
fact = 1
for i in range(1,a+1):
    fact = fact *i
    # fact *= i

print(fact)

# factorial 

number = int(input("Enter Number: ")) 
fact = 1
for i in range(1,number+1):
    fact = fact * i
    # print(fact)
print(fact)


# printing the patterns

star = 5
for i in range(1,star):
    for j in range(star):
            print("*" ,end=" ")
    print()


dates = []
start = 201001
for i in range (2):
        for j in range(12):
                dates.append(start + j)
        start = start + 100
print(dates)


add = 0
for i in list(range(1,5)):
        add += i
        print(i)
print(f"sum of the range is {add}")


add = 0
for i in range(1,5):
        add += i
        print([i])
print(f"sum of the range is {add}")

total = 0
print(list(range(1,10)))
for i in range(1,10):
        if i % 3 == 0 :
                total += i
                print(i)
print(total)

add = 0
print(list(range(1,10)))
for i in range(1,10):
        if i % 2 == 0:
                add += i
                print(i)
print(add)
            
# ##total = 0
a = ["Apple","Amazon", "Microsoft","Google" ]
for i in range(len(a)):
        for j in range(i+1):
                # ##total += a
                print(a[i])
##print(total)


a = "Shaikh Mohd Arif"
# print(range(len(a)))
for i in range(len(a)):
        print(i ,a[i])
        # ##print(a[A])

for i in range(len(a)-1,-1,-1):
        print(a[i])


for i in range(1,5):
        for j in range(1,i+1):
                print("*",end="")
        ##print()                         ## this will not leave a line
        print("\n")                     ## this will print in new line 



for i in range(5,0,-1):
        for j in range(1,i+1):
                print("*",end="")
        print("\n")


for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print("\n")

for i in range(5,0,-1):
        for j in range(1,6-i):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print("\n")


for i in range(1,5):
        for j in range(1,i+1):
                print("*",end=" ")
        print("\n")

for i in range(5,0,-1):
        for j in range(1,i+1):
                print("*",end=" ")
        print("\n")


for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print("\n")

for i in range(5,0,-1):
        for j in range(1,6-i):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print("\n")

for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end=" ")
        print("\n")

for i in range(5,0,-1):
        for j in range(1,6-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end=" ")
        print("\n")
        # print()

for i in range(1,10):
        for j in range(1,10-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end="")
        print()

for i in range(10,0,-1):
        for j in range(1,11-i):
                print(" ",end="")
        for k in range(1,2*i-1+1):
                print("*",end="")
        print()

# ########################################################################################################

for i in range(1,5):
        for j in range(1,5):
                print("* ",end="")
        print("\n")

for i in range(1,5):
        for j in range(1,i+1):
                print("*",end="")
        print()

for i in range(5,0,-1):
        for j in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5+1):
        for j in range(1,i+1):
                print("*",end="")
        print()

for i in range(5,0,-1):
        for j in range(1,i):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5):
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5-1):        ## this will print the 3 space cuz the i is (5 will not include ,4) and in 2nd loop j (5,4) 5 - 1 this is 3 cuz the 5 will not include so that is 4 -1 is 3 it will print 3 spaces 
                print(" ",end="")
        for k in range(1,i+1):
                print("*",end="")
        print()

for i in range(1,5):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end="")
        print()

for i in range(4,0,-1):
        for j in range(1,5-i):
                print(" ",end="")
        for k in range(1,(2*i-1)+1):
                print("*",end="")
        print()

###################################################################################################
class Pattern():
        def __init__(self,num):
                self.num = num
                for i in range(1,num):
                        for j in range(1,i+1):
                                print("*",end="")
                        print()
        @staticmethod
        def greet():
                print("Very Nice")

star = Pattern(5)
star.greet()
#############################################################################################

for i in range(1,5):                                              ## ****
        for j in range(1,5):                                      ## ****
                print("*",end="")                                 ## ****
        print()                                                   ## ****
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                              ## *
        for j in range(1,i+1):                                    ##  **
                print(" ",end="")                                 ##   ***
        for k in range(1,i+1):                                    ##    ****
                print("*",end="")
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                           ##     *****
        for j in range(1,i+1):                                    ##    ****
                print(" ",end="")                                 ##   ***
        for k in range(1,i+1):                                    ##  **
                print("*",end="")                                 ## *
        print()
print("###############################")

for i in range(1,5):                                              ##    *
        for j in range(1,5-1):                                    ##    **
                print(" ",end="")                                 ##    ***
        for k in range(1,i+1):                                    ##    ****
                print("*",end="")                                 
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                            ##    *****
        for j in range(1,6-1):                                     ##    ****
                print(" ",end="")                                  ##    ***
        for k in range(1,i+1):                                     ##    **
                print("*",end="")                                  ##    *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                               ## *
        for j in range(1,i+1):                                     ## **
                print("*",end="")                                  ## ***
        print()                                                    ## ****
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                            ## *****
        for j in range(1,i+1):                                     ## ****
                print("*",end="")                                  ## ***
        print()                                                    ## **
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")                       ## *

for i in range(1,5):                                                 ##    *
        for j in range(1,5-1):                                       ##    ***
                print(" ",end="")                                    ##    *****
        for k in range(1,(2*i-1)+1):                                 ##    *******
                print("*",end="")
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                               ##    *********
        for j in range(1,5-1):                                        ##    *******
                print(" ",end="")                                     ##    *****
        for k in range(1,(2*i-1)+1):                                  ##    ***
                print("*",end="")                                     ##    *
        print()                                                       
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4")

for i in range(1,5):                                                 ## *
        for j in range(1,(2*i-1)+1):                                 ## ***
                print("*",end="")                                    ## *****
        print()                                                      ## *******
print("#################################")

for i in range(5,0,-1):                                              ## *********
        for j in range(1,(2*i-1)+1):                                 ## ******* 
                print("*",end="")                                    ## *****
        print()                                                      ## ***
print("####################################")                        ## *

for i in range(1,5):                                                   ##    *
        for j in range(1,5-i):                                         ##   **
                print(" ",end="")                                      ##  ***
        for k in range(1,i+1):                                         ## ****  
                print("*",end="")
        print()
print("#################################")

for i in range(5,0,-1):                                                  ##  ***** 
        for j in range(1,6-i):                                           ##   **** 
                print(" ",end="")                                        ##    ***
        for k in range(1,i+1):                                           ##     **
                print("*",end="")                                        ##      *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                                   ##  *
        for j in range(1,i+1):                                         ##   ***
                print(" ",end="")                                      ##    *****
        for k in range(1,(2*i-1)+1):                                   ##     *******
                print("*",end="")
        print()
print("###################################")

for i in range(5,0,-1):                                                  ##      *********
        for j in range(1,i+1):                                           ##     *******
                print(" ",end="")                                        ##    *****
        for k in range(1,(2*i-1)+1):                                     ##   ***
                print("*",end="")                                        ##  *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(1,5):                                                  ##    *
        for j in range(1,5-i):                                        ##   ***
                print(" ",end="")                                     ##  ***** 
        for j in range(1,(2*i-1)+1):                                  ## *******
                print("*",end="")
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

for i in range(5,0,-1):                                                 ## *********
        for j in range(1,6-i):                                          ##  *******
                print(" ",end="")                                       ##   *****
        for k in range(1,(2*i-1)+1):                                    ##    ***
                print("*",end="")                                       ##     *
        print()
print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    