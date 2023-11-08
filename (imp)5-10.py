#write a class Train which has methods to book a ticket,get status(no of seats)
# and get fare information of trains  running under Indian Railway. 
class Train:
    def __init__(self,name, fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
        
    def getStatus(self):
        print("*******************")
        print(f"The name of the train is {self.name}")
        print(f"The fare of the train is {self.fare}")
        print(f"The seats in  the train is {self.seats}")
        print("*******************")


    def fareInfo(self):
        print(f"the price of the ticket is :rs.{self.fare}")
        print("************************")
        
    def bookticket(self):
        if(self.seats>0):
            print(f"your ticket has been booked ! your seat number is{self.seats}")
            self.seats=self.seats-1
        else:
            print("sorry!the train is full!kindly try again later")
            '''1 2 3 4 5 6 7 8 9 10
            if  somebody books a seat  i am giving him 10 nth seat then the program 
            will show that 9 seats are avilable and if that seat gets cancelled then that seat will be avilable again
            '''
            
        def cancelTicket( self,seatno.):
            pass#do it by yourself 

intercity=Train("Intercity Express :14015",90 ,300)
intercity.getStatus()
intercity.fareInfo()
