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
     return f'Item("{self.name},{self.price},{self.quantity}")'

class phone(Item):
    all=[]
    def __init__(self, name: str , price: float , quantity=0, broken_phones=0 ):
        
        #call to super  function to access  all the attributes/ methods 
        super().__init__(
            name,price,quantity 
        ) 
        

phone1= phone("jscPhonev10",500,5,1)
print(phone1.calculate_total_price())
phone2= phone("jscPhonev20",700,5,1)
print(phone2.calculate_total_price())




#thee next  step that we might think about could be creating a method that will go ahead and calculate 
# the total number of phones that are actually not broken meaning subtracting the quantity by 
# that i can use the inherited Item class now thats where the polymorphism is also in action .

# now we have lot of the peoblems to create such a thing because we can not we'll go ahead inside 
# our item . and do this smooth enogh . because we dont really have the broken phones attribute 
# assignned to itself . and we can not just go ahead and create this class inside this Item class 
#because this method is not going to be useful for hundreds of items that you will go ahead and create .
# this jjust represent a phone kind of item . so  in order to solve this problem in the best practices 
#  we could go and create a seperated class that will inherit the functionalities that the item class 
#  brings with it and that is exactly where we could benefit from inheritence . 
# we will go ahead create a class named phone and this phone class will inherit all the methods and attributes 
# that item class has .
# now i will go ahead and create a class that i will name it home 
# now pay attention   that i will not use a  .

# class phone(Item):
# this says  i have created a class of phone and it will inherit all the functionalities of the 
# Item . 
# ok now that we have created this class then lets go ahead and execute our program where 
# the instances would be item instances , this should not have any problems because 
# we know that we could create those item instances and we will not receive any error 
# but if we were to change those to  a phone

#phone1= phone("jscPhonev10",500,5)
#phone1.broken_phones =1
#phone2= phone("jscPhonev20",700,5)
#phone2.broken_phones =1 

#like that then we should not receive any error and that's just a basic way that youu could inheritence 
# in order to represent different kind s of object when you want to do that . 
# now this could aalso be applied to other realistic programs that you want to comeup with them by on your own.
# but in my case it also make sense to create some classes where each class will represent a kind of an item.
# and then i could go ahead and inherit from the otem class in each of the child classes that i will go ahead and create in . 
# the future  could also use another class for an item like laptop then i could go ahead use something like seperate functionality from that . 
# now talked about the classes that w inherit fom then those are considered to be called parent classes .
# and when we create multiple class that inherit from that class then those are considered to be child classes . 
# 



# now throughout the series we learnd that it is not a good idea to assign attributes manually . once we crete 
# create those instances and a better way to do that is actually going ahead and creating our constructor and pass the value that we would like to 
# immediately in the instance creation exactly like here  . so in order to solve this we gonna need to figure out 
# how we are going to do that becausse creating the constructor inside this class is going to br really tricky .
# because we dont really want to break the logic .

# now we are gonna copy the the code from above and paste it on the phone class
# it solves the problem temporarily  because we received the exact same parameters that we receive 
# when we instantiate an instance when and wew also have control to receive some more parameters like 
# we want to do with broken phones . lets go and say --
# broken_phones=0 and type ina a validation for that -- line 58,66, 70--
# now it could have been nicer to create a class attribute for the phone class and that will 
# mean that we could go ahead and say all is equal to an empty list .  
# 



# to check that it works i am going to pass the values in line  73-- 
#and we are adding lines -- 74,76 --
# then we can see that we have received a result --
#2500
#3500



# now one thing for the __init__ method is this says to us 
#call to  __init__ of super class is missed -- and what that means it means 
# when we initialixze __init__ method inside the child class  then python expects for some function to be 
# called intentionally now that function is named super .
# and what super allows us to do it allows us to have full access to all the attribute of the 
# parent class and by using super function .
#  we dont really need to hard code in the attribute assignment . like we have done with the name .
# like price, quantity , name and as well as for other  that we have executed every time  we want to come up with a child class .
# imagine how hard it would be if w have to copy-paste  every time we create a class . 

# and to us time that is exactly why we needed to use the super function .
# te super functio will allow us to access the attributes from the parent class .
# so with this best practice in inheritence  when it comes to object oriented programs  .

#thought experiment 
# if i was to remove those three lines and two lines--57-66-- those are happen to be the lines i have copied and pasted .
# and we runs our program then we will get an error because saying that phone object has no attribute and where does it comes from it comes from the lines 
# we have just created because it thinks that it has the attribute of price but we never have the price attribute in 
# the phone level because we jusst have deleted self.price=price . and we are going to replace the lines 
# we have deleted with the following thing i am going to write---


#super().__init__{
#           name,price,quantity 
#        }
# you could also ask yourself that is not it the duplication of the code that we the fact that we also copied and pasted the 
# the parameters that we receive in the child class and yeah that is a perfect question that is something that could be solved by 
# somrthing more advanced if you heard about keyword arguments ..
# now  calling the super function  and adding the __init__after that  will be responsible for thhe same 
# behaviour like we had previously. so that means we still  should see the same result as before and no errors .

#  2500
#  3500

# we received the expected result  so that way we implemment the best practices of object 
# oriented programming 

# for each child class we used seperate constructur we also gonna need to call to the super 
# function in order to have aceess to all the methods that are coming from the class we inherit from .


