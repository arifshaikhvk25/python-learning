## class complex to represent complex numbers, along with overloaded operators + and * which added multiplies them

##  multiplication complex (a+bi)(c+di) = (ac−bd) + (ad+bc)i   ## formula 

## (3 + 2i)(1 + 7i) =	(3×1 − 2×7) + (3×7 + 2×1)i  ## example
## =	−11 + 23i

## adding complex (a+bi) + (c+di) = (a+c) + (b+d)i

############################################################################################################

## adding complex (a+bi) + (c+di) = (a+c) + (b+d)i

class Complex:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def __add__(self, c):
        return Complex(self.a + c.a, self.b + c.b)
    
    def __str__(self):
        return f"{self.a} + {self.b}i"

c1 = Complex(1,4)
c2 = Complex(8,5)
print(c1 + c2)

class Complex:
    def __init__(self,a,b):
        self.real = a
        self.imaginary = b

    def __add__(self,c):
        return Complex(self.real + c.real, self.imaginary + c.imaginary)

    def __str__ (self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(8,1)
c2 = Complex(1,8)
print(c1 + c2)

################################################################################################################################################

# #3 multiplication complex (a+bi)(c+di) = (ac−bd) + (ad+bc)i

class Complex:
    def __init__(self,a,b):
        self.real = a
        self.imaginary = b

    def __mul__ (self,c):
        mulreal = self.real * c.real - self.imaginary * c.imaginary
        mulimg = self.real * c.imaginary + self.imaginary * c.real
        return Complex (mulreal , mulimg)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1 = Complex(3,2)
c2 = Complex(1,7)
print(c1 * c2)
