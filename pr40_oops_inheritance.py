 ## vector

class C2dvev ():                                  
    def __init__(self,i,j):
        self.i = i
        self.j = j

        print(f"{self.i}i + {self.j}j")

class C3dvec (C2dvev):
    def __init__(self,i, j, k) :
        super().__init__(i,j)
        self.k = k

        print(f"{self.i}i + {self.j}j + {self.k}k")

# v2d = C2dvev(1,3)
v3d = C3dvec(1, 9, 7)


class C2dvec ():                           ## YouTube
    def __init__(self,i, j):
        self.icap = i
        self.jcap = j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class C3dvec (C2dvec):
    def __init__(self, i, j, k):
        super().__init__(i,j)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j + {self.kcap}k"

c2 = C2dvec(1, 3)
c3 = C3dvec(1, 9, 7)
print(c2)
print(c3)

#################################################################################################################

class Animal:
    animalType = "Mammal"

class Pets:
    color = "black and grey"

class Dog:
    
    @staticmethod
    def bark():
        print("bow bow!")
d = Dog()
d.bark()


class domesticAnimal:
    typeofAnimal = "Mammal"

    def __init__(self, name):
        self.name = name
        print(f"The name of the cat is {self.name}")

    
    ## ##def __init__(self):
    ## ##     print(f"The name of the cat is {self.name}")


class Pet (domesticAnimal):
    color = "White and Brown"
    
    def __init__(self, name):                              ## both use for same 
        super().__init__(name)
        
    # def __init__(self, name):                            ## both use for same 
    #     self.name = name
    #     print(f"The name of the cat is {self.name}")


    def agePet (self):
        print(f"age of cat is {self.age}")
        print(f"The color of the cat is {self.color}")

class Cat:
    @staticmethod
    def gender ():
        print("Gender of the cat is female")

d = domesticAnimal("Alice")

p = Pet("Olive")
p.age = "3 year"
p.agePet()

c = Cat()
c.gender()

##########################################################################################################################

## getter setter

class Employee :
    salary = 1000
    increment = 1.5

    @property 
    def salary_After_Increment (self):
        return self.salary * self.increment

    
    @salary_After_Increment.setter
    def salary_After_Increment (self,salary_increment):
        self.increment = salary_increment / self.salary 

e = Employee()
print(e.salary)
print(e.increment)
print(e.salary_After_Increment)
e.salary_After_Increment = 2000
print(e.increment)
print(e.salary)
