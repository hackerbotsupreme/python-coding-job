import csv 
class Item:
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
     return f'{self.__class__.__name__}Item("{self.name},{self.price},{self.quantity}")'

class phone(Item):
    #all=[]
    def __init__(self, name: str , price: float , quantity=0, broken_phones=0 ):
        
        #call to super  function to access  all the attributes/ methods 
        super().__init__(
            name,price,quantity 
        ) 
        #actions to execute 
        #phone.all.append(self)
        

phone1= phone("jscPhonev10",500,5,1)
print(Item.all)
print(phone.all)# remember thst we also implemented the class attribute as well for the phone . 



# here i want to show you the result of the following thing so i will say and i will see what is the list of all
# in the item class is going to bring us back .  so i am going to say -----
#[Item("jscPhonev10,500,5")]
#[]
# something weird 
# we basically see the result of the repr method that comes from the item class 
# the reason that it happens is because we never implemented in our repr method so that's why we esee 
# this ungenericresult of item you can also pay attention that we only create the instance of the phone class ..
# so that's not so good that we see item in those outputs . so what we could use instead of hardcoding 
# in the name of the class in the repr method inside the item class .. then we could access to the name 
# of the class generically now if i was to replace this with some special magic attribute that will be responsible 
## to give me the name of the class then this will be perfect .

#      return f'{self.__class__.__name__}Item("{self.name},{self.price},{self.quantity}")'
# so that is the generic way to access the class from the instance . 
# and by doing this besides receiving item hardcoded string then i should receive the name of the class 
# that i initialize from the  begining so this should be phone bcz that is single instance that i have right now . 
# you can see that this  is what we receiving back . 

# i said this earlier that yby using the super function we basically have accessed to all the attributes and methods 
# that are coming from the class that we inherit from so what that means we also have the access to all the class attribute 
# of all that inside item class , i am talking about -- all[]-- attribute 
#  now to show you that i am going to remove the old attribute . 
# and i am also going to hash 
#  #actions to execute 
#  #phone.all.append(self)
# becasue we no;onger having the old attribute in the form classs and if i was to remove those  and execute our program now 
# [phoneItem("jscPhonev10,500,5")]
# [phoneItem("jscPhonev10,500,5")]
# then you can see that we still receive the  same result as before .
# so that proves that  it was a good idea (of making work and time  shorter) removing the old attributes 
# inthe child class level . it is a great idea to only use the old attribute in the parent class becaus e by using super function in the chld class 
# we will have access to all attribute so this means that if one day  we would like to have access to all the items 
# instancs that we have initialized . incliuding the chld class . 
# then accessing them from - item.all- should be enough .  
# yiiu might be cinfused how this line is responsible to add this instance inside all attribute .
# that is happen to be a list that is happening because by using the super function and as well as  the inti ,then we 
# basically call the init method inside the parent class now in the latest line in this method we also use item 
# item.all.append() which is also  going to be accessible to be phone class . thats whuy calling the all class 
# attribute from the item class is a better idea bcz it will give us the complete picture . okay , so before diving 
# into the topic of that episode . we gonna need to do some code organixation here as we can see for each for each of the child class that 
# we will go ahead and create in the future to extenf this project then we are gonna do this in the main file because that 
# was the only single file that we were working with  and now that our project groews we need to start working with the multiple files 
# so that is way working with a file that will represent a class of item  and working with a second file that will represent 
# phone child class will be a better idea . 
# so we ggot the main file dadicated to only create instances of those class so lets get started with this 
# 

