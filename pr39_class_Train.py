## class train 

class Train():
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats 
        self.fare = fare
    
    def fareInfo (self):
        print(f"The fare of the train is Rs. {self.fare}")

    def trainINfo (self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f"The name of the Train is {self.name}")
        print(f"The seats available are {self.seats}")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    def bookTicket(self):
        if self.seats>0:
            print(f"Your ticket has been booked! your seat number is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry this Train is FULL!! try in tatkal")

cr = Train("Mumbai Train 400017", 3, 100)
# cr.fareInfo()
cr.trainINfo()
cr.fareInfo()
cr.bookTicket()
cr.bookTicket()
cr.trainINfo()
cr.bookTicket()
cr.trainINfo()
cr.bookTicket()

#######################################################################################################################################

class Train():
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats 
        self.fare = fare
    
    def trainStatus (self):
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(f"The name of the Train is {self.name}")
        print(f"The seats are available in this train {self.seats}")
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    def fareInfo (self):
        print(f"The fare of the Train is {self.fare}")

    def bookTickets(self):
        if self.seats > 0:
            print(f"Your tickte as been booked! Your seat number is {self.seats} ")
            self.seats = self.seats - 1
        else :
            print("SOORY Train is full! kindly try in  Tatkal")


ir = Train("Train Mumbai",3,1999)
ir.trainStatus()
ir.fareInfo()
ir.bookTickets()
ir.trainStatus()
ir.bookTickets()
ir.trainStatus()
ir.bookTickets()
ir.trainStatus()
ir.bookTickets()
