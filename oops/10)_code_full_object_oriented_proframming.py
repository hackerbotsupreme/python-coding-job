
import csv
class item :
    pay_rate=0.8# so i will say here the pay rate after 20% discount 
    all= []
    def __init__(self, name: str , price: float , quantity=0):
        #run validations to  the received arguments 
        assert price >= 0 , f'Price {price} is not greater than zero! '   #  i want it not to be a negative number 
        assert quantity  >= 0 , f'quantity {quantity} is not greater than zero! ' # same  as above 
        
        
        #assign  to self object 
        self.name=name
        self.price=price
        self.quantity=quantity 
        
        #actions to execute 
        item.all.append(self)
        
        
        
    def calculate_total_price(self): 
     return self.price*self.quantity # correct one that works 
    #       self.price=self.price * pay_rate # incorrect this will not work 

    def apply_discount(self):
        self.price=self.price * self.pay_rate
#       new value     =old value    *item.pay_rate(discount)
#      of self.price  | of self.price
#pay attention here==================>
#       self.price=self.price * pay_rate                  # incorrect this will not work 
#       self.price=self.price * item.pay_rate                 #correct one that works 
    @classmethod
    def instantiate_from_csv(cls):
        with open('iall_tems.csv','r')as f:
             reader = csv.DictReader(f)
             items = list(reader)
        for item in items:
            item(
               name=item.get ('name'),
               price=int(item.get ('price')),
               quantity=int(item.get ('quantity')),
            )

               
            
            
         
     
    
     
    def __repr__(self):
        return  f'item("{self.name}",{self.price},{self.quantity})'



item.instantiate_from_csv()# method
print(item.all)# stores all the instances 


#{'name': "'phone'", 'price': '100', 'quantity': '5'}
#{'name': "'laptop'", 'price': '1000', 'quantity': '3'}
#{'name': "'cable'", 'price': '10', 'quantity': '5'}
#{'name': "'mouse'", 'price': '58', 'quantity': '5'}
#{'name': "'keyboard '", 'price': '75', 'quantity': '5'}