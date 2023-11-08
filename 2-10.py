#write a class calculator capabble of finding square , cube, square root of a number
class Calculator:
    def __init__(self,num):
        self.number=num 
        
        
    def square(self):
        print(f"the value of{self.number}  square is {self.number**2}")
    
    def cube(self):
        print(f"the value of{self.number}  cube is {self.number**3}")
    # What does ** mean in Python?
    # In the case of numerical data values, ** works as an exponentiation operator.
    
    def squareRoot(self):
        print(f"the value of{self.number}  squareRoot is {self.number**0.5}")
    
a=Calculator(9)
a.square()
a.squareRoot()
a.cube()

