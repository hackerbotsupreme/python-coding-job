#let's get started 
#now one of the main  problems  that we have here is the fact that we dont have a set of rules for the attributes that you would like to
#pass in order to instantiate an instance sucessfully, and what that means ,it means that for each item that 
#i want to go ahead and create i need to  hard code in the attribute name . 
#like --item2.name(),item2.price()-- and it could have been nicer if we somehow declaring the class that in order 
#to instantiate an instance sucessfully --name ,price,quantity -- must be passed other wise the instance could not have been created sucessfully 
#it means that it could have been a great option somehow execute something in the background the second that we instantiate  an instance and here is a way  thata
#you can reach such a behaviour . and  that is  possible by creating a special methods with a very unique name ,which is called 
#  __init__ operator .#its also called constructor .
#basically that is a method with a unique name that  you need to call it the way it is intentionally  in order to 
#use its special features. now , the way its going to work  is creating it the following way . 
class item :
    def __init__(self):
        print('i am creative')
    def calculate_total_price(self,x,y): 
     return x*y
item2=item()#instance 
item2.name='laptop'#attributes for item2
item2.price=1000#attributes for item2
item2.quantity=3#attributes for item2
item1=item()#instance 
item1.name='phone' #attributes for item1
item1.price=100#attributes for item1
item1.quantity=5#attributes for item1
#now that we have created this method then lets actually see what this method does in the background so when you go ahead and create instance of a aclass 
#-- like line 17 and  line 21 --then python executes this __init__() method automatically that means it means that now that we have declared our class 
#python is going to run through  the mentioned two lines (two instances )  then it is going to call the actions that is inside the __init__ method and to #prove that we have 
#run the program and  the output  is on the below  
#output
#i am creative
#i am creative

#so as we can see it has given us two outputs as we had one print under the init method and two instances 
#its also explained as we called init twicethanks to those instances that we have created .

#  the way that the __init__ is going to work is by creating it the following way .
# the methods that are used in the oops sis called magic methods . 
# __init__(self):
# 1.so when you go ahead and create an instance of a class python executes tis __init__ function 
# automatically and it means that now that we have declarec our class python isgoing to run through this line 
# and since an instance has been created and we have __init__designed then it is going to call the actions 
# that are inside of this method . in order to prove you that    erite this then 
# __init__(self):
# print('i am creative' )
# item1=Item()
# item2=Item()
# and based on how many obects we have instantiated our init method also will be called that many time .
# and in this case the init going tobe called 2 times i.e. the print going to be execute two times .




