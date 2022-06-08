# converting celcius to farenheit  to celcius
# converting inches to centimeters to inches

# celcius to farenheit

def farenheit(c):
   celcius = (c * 1.8) + 32          # this is the formula of celcius to farenheit
   return celcius

f = farenheit(37)
print(f"{f} is the Farenheit Temprature")


def far(cel):
   return cel * (9/5) + 32 

fa = far(0)
print(fa)

##############################################################################

## farenheit to celcius

def celcius (f):
    farenheit = f -32 * 1.8             # formula 
    return farenheit

c = celcius(88)
print(f"{c} is the Celcius Temperature")

def celcius(far):
    return (far - 32) * (5/9) 

cel = celcius(55)
print(cel)

############################################################################

# inches to cms

def cms(inches):                         #formula
    return inches * 2.54

c = cms(4)
print(c)


def centimeters(inches):
    inch  = inches * 2.54
    return inch

cms = centimeters(5)
print(f"5 inches is {cms} centimeters")

###########################################################################

# centimeters to inches

def inches(cms):
    return cms / 2.54

inch = inches(10.16)
print(inch)

def inche(centimeters):
    inc = centimeters / 2.54
    return inc

i = inche(12.7)
print(f"12.7 centimeters is {i} inches")

###############################################################################

# end=""
# to prevent new line at the end

print("Bismillah", end=" ")
print("Assalamualikum", end=" ")
print("warahamtullahi", end=" ")
print("wabarkhatuh", end=" ")

print("hey", end=" ")
print("wsup", end=" ")

