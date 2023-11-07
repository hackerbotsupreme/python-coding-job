class item :
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
print(Item1.calculate_total_price())
print(Item2.calculate_total_price())





#print(f'an instance created :{name}')#we can call it --{}--- "refer to the "---in this case it is name of the assignes instance 
# in --line 4 -- f is called as formatted string 

#  but  we might   still  want  to validate the received values in the following  ways    say that  we never want to receive a (-ve) tive  value   and you never want to receive a (-ve)  number for  pricr 
#that is something we can not achieve by typing in -- line2-- but there is actually  a great way to work this around.  
#and that will be by using assert statements .
# assert statements is a statement keyword that is used to check if there is a match . between what is happening 
# to your expectation . so lets see how we can get work with assert . so i  am going to delete--line-- and organize out --
#or in it method a little method --line-- 3 to 6-- 
#  now when we run the program we will not receive any program 
#  but the moment we change the quantity to (-1) -- line  20 -- we are gonna see an assertion error / we will have some errors 

#PS C:\Users\rekha\OneDrive\Desktop\oops> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe "c:/Users/rekha/OneDrive/Desktop/oops/6)
# fill_object_orienAssertionError
#PS C:\Users\rekha\OneDrive\Desktop\oops> 

#the fact that we see here an assertion error is quite a generel exception  that does  not mean anything 
# but what is so beautiful with assert is you can add your own exception message  right near of it as a second argument , so let's go
# on top here to that two lines  ---4 and 5 with line 20  --- and as a result we also got the statement  with the error this  time .



#  File "c:\Users\rekha\OneDrive\Desktop\oops\6)fill_object_oriented_programming.py", line 5, in __init__
#    assert quantity  >= 0 , f'quantity {quantity} is not greater than zero! ' # same  as above
#AssertionError:  quantity -1 is not greater than zero!
#PS C:\Users\rekha\OneDrive\Desktop\oops> 


# so now we understand that   the assert statement  allows us to validate the arguments  that we receive . 
 
#so upto this point we learned about the constructor(__init__) and assert statement 


