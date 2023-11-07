class item :
    pay_rate=0.8# so i will say here the pay rate after 20% discount 
    
    def __init__(self, name: str , price: float , quantity=0):
        #run validations to  the received arguments 
        assert price >= 0 , f'Price {price} is not greater than zero! '   #  i want it not to be a negative number 
        assert quantity  >= 0 , f'quantity {quantity} is not greater than zero! ' # same  as above 
        
        
        #assign  to self object 
        self.name=name
        self.price=price
        self.quantity=quantity 
        
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


Item1=item('phone',100,5)#instance 
Item1.apply_discount()
print(Item1.price)


Item2=item('laptop',1000,3)#instance # here we will try to apply 30% discount on the item laptop 
Item2.pay_rate=0.7
Item2.apply_discount()
print(Item2.price)




#========================================explanation========================================
#print(item.__dict__)# all the attributes for the instance  level . 
#print(Item1.__dict__)

#alright then lets take it to a real life example  and come up with a  method that will go ahead and apply 
# a method that will put a discount to our price  of our items . so that will be by creating  a method that will 
#we  belong to each of our instances and that  means that we can go ahead and go ahead an come up with 
#   a method  that could name apply discount .


#so i am going to say -- line 18---
# at first we need to figure out that how we are going to override  an attribute that is belonging 
# to an instance  and we already know that we can do that by -- line 19 --
# and you might expect that we could just access the pay_rate directly like that  -- 
#        self.price=self.price * pay_rate
# this but if you could remember that pay_rate belongs to the item class itself . 
# now you think that it might going to work because  you can either  access it  from the class or 
# instance  level as we understood previously so we can go ahead and say 
#        self.price=self.price * item.pay_rate
#like this  and there you have a method that can go ahead and basically override the price 
#instance( attribte instance ) it self now to you that this works ---

#we will do --
#item1.apply_discount()
#print(item1.price)


#and we should receive correct answer --
# 80.0

# the output comes 80.0 because the item was phone and their price is 100 and applying 20 %discount on it makes it 80.0




# ok now think for the laptop you want to apply 30% dis count but it is a bad idea to change
# the pay_rate  because as it is going to effect all the instances and their attributes  . 


# so what you can do instead is that you can assign this attribute directly to one of the instances that you like to have a 
# different discount ammount for so lets go ahead and see an example for this ---
#so  we will do something like --Item2.pay_rate=0.7
# now what will happen hare is that for Item2 it will find the attribute of pay_rate at the instance level . 
# so Item2 does not really have to go ahead to the class level  and bring back the value of pay_rate. 
# but  note at the same time , pay_rate for Item1 is different  there it is stll going to look 
# from item level . which is going to be 0.8 . 

# so now when we will write like --
#Item2.apply_discount()
#print(Item2.price)
#then lets see what will happen . execute/run the code now,,,,,,,,,,,,,,,,
# 800.0
# now you can see that we still however receiving 800.0 that means  the pay_rate from the clas level 
# so what that means is   no matter what we try ro pull the pay_rate it still dont gives a fuck and gives the class level pay_rate .
# and then the best practice would be  change the line 20---
#def apply_discount(self):
#        self.price=self.price * item.pay_rate

#from this --- to 
#def apply_discount(self):
#        self.price=self.price * self.pay_rate
 
# and in this way if we override the psyrate from the insttance level then it is going to read from the instance level. that is for item 2 .
#but for  Item1 if we try to access the pay_rate from the instance level then this is still  great bcz we didnot assign the specific pay_rate for Item1
# so its going to pull that from class level .  so with that said 
#if we were to run that then ,,,,,,,,,,,,,,,,,,,,,,,,
#700.0
# now we have our expected result ,


# so the best practice  that we can conclude is  
# when it comes to accessing class attributes you must reconsider  how you want to access them
# when you want to access them when you will come up with some methods and specially for creating 
# a method like apply_discount  it is a great idea to access it from the instance level with also. 
#allowing the option to assign the pay_rate to the instance level. 












