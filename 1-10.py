#create a class paraameter for storing information of few programmer working at microsoft
class Programmer:
    company="microsoft"
    def __init__(self, name,product):
        self.name=name
        self.product=product
        
    def getInfo(self):
        print(f"The name of the programmer is {self.name}and product is {self.product}")
        

harry=Programmer("harry","skype")
alka=Programmer("alka","Github")
harry.getInfo()#also remember the name in def is always written in camelcase and 
alka.getInfo()#similarly the name in class attribute alys written in pascalcase
#AttributeError: 'Programmer' object has no attribute 'getinfo'. Did you mean: 'getInfo'?
        