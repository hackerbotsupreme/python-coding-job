import csv
class Item :
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
        Item.all.append(self)
        
        
        
    def calculate_total_price(self): 
     return self.price*self.quantity # correct one that works 
    #       self.price=self.price * pay_rate # incorrect this will not work 

    def apply_discount(self):
        self.price=self.price * self.pay_rate
    @classmethod
    def instantiate_from_csv(cls):
      with open('iall_tems.csv','r')as f :
        reader=csv.DictReader(f)
        Items=list(reader)

      for Item in Items:
        Item(
            name=Item.get('name'),
            price=float(Item.get('price')),
            quantity=int(Item.get('quantity')),
        )
    @staticmethod        
    def is_integer(num):
    #we will count out the the floats that are point zero decimels 
    # for i.e: 5.0,10.0, so on .
       if isinstance(num, float):
        #count out the float that are decimel point zero . 
        return num.is_integer()
       elif isinstance(num,int):
        return True 
       else:
        return False 
    def __repr__(self):
     return f'Item("{self.name},{self.price},{self.quantity}")'
print(Item.is_integer(7))
print(Item.is_integer(7.5))
print(Item.is_integer(7.0))

#Item.instantiate_from_csv()
#print(Item.all)


#==============================explanation==========================================
#untill now we  understood @classmethod and 
# our next topic is #staticmethod 

# now a static method should do some work for you that has some logical connectio to the class so for example if you 
# if you want to check if a number is an integer or a float , then this is a good  candidate 
# for creating a static method , because this has some connetio to the class that we 
# work with , so it makes sense to vheck if a price of an item has a decimel point and by saying has 
# a decimel point , i obviously count out those that are point zero , now to be honest , static in class
# could look very alike to you . but we will explain the main difference very soon .

# pay attention ow the received parameter turned into the regular orange color  this means that @staticmethods are 
# never sending in the background the instannce as a first argument and that is unlike the class methods because the class 
# methods are sending the class reference as a first argument . and that is why we had to receive the cls 
# in fef instantiate_from_csv(cls)  and that is why it is intentionally colored with purple but in static method 
#we nwver send the object as a first argument so that is why we should relate to the static method like a 
#regular function jthat just receives parameter like w are familiar with isolated functions .  
# @staticmethod        
#def is_integer(num):
#    #we will count out the the floats that are point zero decimels 
#    # for i.e: 5.0,10.0, so on .
#    if isinstance(num, float):
#        #count out the float that are decimel point zero . 
#        return num.is_integer
#    elif isinstance(num,int):
#        return True 
#    else:
#        return False 
#def __repr__(self):
#    return f'Item("{self.name},{self.price},{self.quantity})'
#item.instantiate_from_csv()
#print(Item.all)
# so now we have designed this method , then lets take a look how  we can call it  so now i will just  remove this 
# and write  print(Item.is_integer(7))
# and lets see .............
# True
# and when we give a floating number / now if  i was to pass in a floating number 
# 
#False
# and what is happening in the backgrounf iit is the fact that is enters from a   -- if isinstance(num, float):
# but it sees that it is not an integer so it returns false but if was to enter something like 
#print(Item.is_integer(7.0))
# then 
#True
# this still returns true because what is happening here  it is entering inside this --if isinstance(num, float):--
# then it checks if it is an integer but we said that this method counts floats that are point zero 
# so it returns through still 
# 

#






#