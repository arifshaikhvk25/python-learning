##create class programmer for storing information of few programmer working at microsoft

class Programmer():
    company = "Microsoft"

    def __init__(self,name,language):
        self.name = name
        self.language = language

    def inFormation(self):
        print(f"Programmer works in {self.company}")
        print(f"The name of the programmer is {self.name}")
        print(f"The language programmer knows {self.language}")

coderArif = Programmer("Arif","python")
coderArif.inFormation()

coderMohan = Programmer("Mohan","python, css, java, html, javascript, c, c++.......")
coderMohan.inFormation()

## class calculator capable of finding square, squareroot, cube

class calculator():
    def __init__(self,num):
        self.num = num

    def square(self):
        print(f"The value of the {self.num} square is {self.num **2}")

    def squareroot(self):
        print(f"The value of the {self.num} squareroot is {self.num **0.5}")

    def cube(self):
        print(f"The value of {self.num} cube is {self.num **3}")

calculate = calculator(5)
calculate.square()
calculate.squareroot()
calculate.cube()


class calculate():
    def __init__(self,number):
        self.number = number

    def square(self):
        print(f"The value of {self.number} square is {self.number **2}")

    def squareroot(self):
        print(f"The value of {self.number} squareroot is {self.number **0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number **3}")

calculating = calculate(3)
calculating.square()
calculating.squareroot()
calculating.cube()

## create a class attribute a, create object from it and set a directly using object.a = Does this change the class attribute ?

class sample ():
    a = "Arif"

object = sample()
object.a = "Mohan"           # ## this will set an instance attribute
print(sample.a)
print(object.a)
# ##print(object)

class smaple2():
    m ="Mohan"

obj = sample()
sample.m = "Das"             # ## this will change class atribute
print(sample.m)

class calculator():
    def __init__(self,num):
        self.num = num 

    def square (self):
        print(f"The vlaue of {self.num} square is {self.num**2} ")

    def squareroot (self):
        print(f"The value of {self.num} squareroot is {self.num**0.5}")

    def cube (self):
        print(f"The value of cube {self.num} cube is {self.num**3}")
    @staticmethod
    def greet():
        print("Hie There")


calculate = calculator(3)
calculate.greet()
calculate.square()
calculate.squareroot()
calculate.cube()
