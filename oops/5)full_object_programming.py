class item :
    def __init__(self, name: str , price: float , quantity=0):
        #print(f'an instance created :{name}')#we can call it --{}--- "refer to the "---in this case it is name of the assignes instance 
        self.name=name
        self.price=price
        self.quantity=quantity 
        
    def calculate_total_price(self): 
     return self.price*self.quantity
 
 

#Item2=item('laptop','1000',3)#instance 
#Item1=item('phone','100',5)#instance 
Item2=item('laptop',1000,3)#instance 
Item1=item('phone',100,5)#instance 

#Item2._has_numpad=False
print(Item1.calculate_total_price())
print(Item2.calculate_total_price())


#3now i want to show you what happens when we multiply string with integer  
#100100100100100
#100010001000


#now when we ran our program then we can see that we are screwing things up here beceuse
#-- the function in line 17, 18 -- prints string three times becaus ewe see  we have 1000multiply by three that is being returned in here .
#now what that means that means we have to  validate data type of the values that we are passing  in .so there are a couple of ways to 
#achieve this and one way is by using typingss's in the parameter that you ar declaring in here . 
#so a great starter will be for example , to declare that a name  must be  a string now , let me first remove those quote sign from the lines --13,14--
#and change those to integers and then go here  and design  those parameters . 
#so in order to specify the type s you could go ahead and create a column sign followed by the type of the data type that you want/expect to receive 
#here so if i was to pass in here  , only the object reference to the class of str--line2---then it will mean that it will have to accept string 
#only and i can prove you that  by changing this to an integer .And you are going to see we have a complaint here--line15--
#now i have changed defined the typr of name ,we can also do this to the rest too........
# --line2-- so the type of price will be float and for for the quantity we dont need to specify a typing . because the fact that we passed a ddefault value 
# of cinteger already marked this parameter as to integer always and  that is why if i was to leave this as it is and change the quantity to a string 
# then you are gonna see that it is going to complain  that the default valueof quantity is an integer so it expects  the input to be an integer/  for an integer   -- line 15  and 16  -- 




#so that was a great setup  



#  but  we might   still  want  to validate the received values in the following  ways    say that  we never want to receive a (-ve) tive  value   and you never want to receive a (-ve)  number for  pricr 
#that is something we can not achieve by typing in -- line2-- but there is actually  a great way to work this around.  
#and that will be by using assert statements .
# assert statements is a statement keywird that is used to check if there is a match . between what is happening 
# to your expectation . so lets see how we can get work with assert . so i  am going to delete--line-- and organize out --line--
#or in it method a little method 

