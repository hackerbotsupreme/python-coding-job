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
     return self.price*self.quantity
 
 

#Item2=item('laptop','1000',3)#instance 
#Item1=item('phone','100',5)#instance 
#Item2=item('laptop',1000,-1)#instance 
Item2=item('laptop',1000,3)#instance 
Item1=item('phone',100,5)#instance 

#Item2._has_numpad=False
#print(Item1.calculate_total_price())
#print(Item2.calculate_total_price())
print(item.__dict__)# all the attributes for the instance  level . 
print(Item1.__dict__)# all the attributes for the instance  level . 
#print(Item.pay_rate)# this line says that we are accessing the class from the class level 
#print(Item1.pay_rate)# this line says that we are accessing the class from the attribute level 
#print(Item2.pay_rate)# this line says that we are accessing the class from the attribute level 





# now consider  a situation   that  you will  want to make use of an attribute that is going to be global 
# global or across all the instances . now a good candidate for this  could be a situation that you will want 
# to apply a sale on your shop  so this  means that you want to apply a sale on your shop  so this means that you 
# want to go ahead and having the control of applying some discount for each one of the items . and that is 
# and that means its going to be shared across all the instances . 


# now we call those kind of attributes -- a class attributes --  and the attributes we have learned to this point is instance attribute 
# about instance attributes we learned eeverthing but we didnot  worked it with other type of attributes .
# class attributes belongs to the class itself . however you can also access this attribute from the instance level as well.
# let go and see / lets look for the good candidate for the  class attribute  . 


# now we are making a  pay_rate variable  on the line 2  and the reason that i am doing this because  i said 
#that  there is going to  be   20%  discount .So  I probaly  want to store an attribute that will  dexcribe how much i still
#neeed to pay  on line 2 . For avoiding confusion i will hash the  printlines if --27,28--
#and say something instead of this print lines that will look like the following --in line 29 --
# so i will try to access to the reference to the class itself  so i am not going to create  an instance like before .
# i am jus tgoing to bring the reference to the class level itself . 
#and i am going to access this attribute by saying -- line 29 ----
#when we run that i willl see that 

#0.8


# as expected . 

#now also remember that we can also access the class_attributes instance level .
#so now lets see if that is true . -- line 30,31 --
#in order to prove it we gonna run it . and the output is --

# 0.8
# 0.8
# 0.8


#as expected 
# in python when we have instance in our hand , then at  first this instance tries to bring the attribute 
# from the instance level and at his  first stage , but if it does not find it there , then it is going to
# try to bring that attribute from the class level . 
# so it means that item one did something in here and say to itsself okay  so i dont have this attribute
# right in here because  that is just not an attribute assigned to me so i am going to try to search  that from  
# the instance level and then i am going to find it and if  sprinted back so that is  exactly what is happening here .
#Item 1 and Item 2 are instances that could not find  the pay rate attribute  on the instance level . 
# so both of them went ahead and try to bring  this attribute  from the class level  . and since it really 
#exist in class level then we  were able to access those . 




#Now to even give  you a better idea what is going on here  i am going to do one more additional thing 
#  let's delete this forst print line -- 31--- and hash the attribute as well write something like.
# line 29,30
# __dict__ will go ahead bring you all the attribute that are belonging to the object that apply this attribute 
#and want to see its content .and now,the output of this code is.. 
#print(item1.__dict__)-- is --
# {'__module__': '__main__', 'pay_rate': 0.8, '__init__': <function item.__init__ at 0x000001D97138AF80>, 'calculate_total_price': <function item.calculate_total_price at 0x000001D97138B010>, '__dict__': <attribute '__dict__' of 'item' objects>, '__weakref__': <attribute '__weakref__' of 'item' objects>, '__doc__': None}
# {'name': 'phone', 'price': 100, 'quantity': 5}

#now you can see that at the first line we see the pay_rate attribute  but in  the second line we never see it 
#we see  name , price  , quantity  and you can also pay attention that this magic(init)  attribute is  actually responsible to take all the 
#attributes and convert it to a dictionary  and that is from where the dict keyword is coming from 
# which is just a shorten version of dictionary  
# an that is a magic attribute that you can use to see  all the attributes that are used 
# simply lets say for the debugging reason .
#  