# one of the main problems we have mentiones of if you remember that  we still are needing to hardcode the attributes that is making our process lenthy and time consuming 
# to avoid that isuue we can use __init __method . lets understand how?
# now we understand that for each instance that we create it will go ahead and call the method  that will result in implementing all the actions under that method . 
# now what that means  not only  we can allow ourselve to receive the self parameter (which is mandatory  bcz python in the background passes the instance itself as the very first argument )we
# could in addition take some more parameter and can perform any reqired operation with them .
# lets say that we would receive on more parameter that we could name it as name   . 
# and as you can see avtomatically python is going to complain about  how the name argument is not filled in here.so now i could go ahead and pass 
# argument of  phone for that one .
class item :
    def __init__(self,name,price, quantity):
        #print(f'an instance created :{name}')#we can call it --{}--- "refer to the "---in this case it is name of the assignes instance 
        self.name=name
        self.price=price
        self.quantity=quantity 
        
    def calculate_total_price(self,x,y): 
     return x*y
 
 

Item2=item('laptop',1000,3)#instance 



Item1=item('phone',100,5)#instance 



print(Item1.name,',',Item2.name)#phone , laptops
print(Item1.price)#phone , laptops
print(Item1.quantity )#phone , laptops
print(Item2.name)#phone , laptops
print(Item2.price)#phone , laptops
print(Item2.quantity)#phone , laptops


#and for the second one we go and pass the argument of laptop , now once we have created this if we were to run our program then were gonna see:
#an instance created :laptop
#an instance created :phone


#now even if we have done this there is certainly some thing is not perfect asthere still a hard coded name instances /passes the atrribute name for both items .
#now pay attention to how the init method has to receive the  self as a  parameter as well and we already know reasons for that . 
#and the fact that we have self as a parameter here could actually allow us to assign the attributes from the init method .
#so that we dont have to go ahead and assign the attribute for each of the name  for each of the instances we create.
#and what that means is we can dynamically assign an attribute to an instance fromthis method . 
#so if i was to  say--line 12 -- 
#so now i can allow myself to delete --line 26,20--Item1.name='phone' #attributes for item1-----Item2.name='laptop'#attributes for item2-----
#as you can see we have a dynamic attribute assigned --line--12
#to test that i will go down here and use two more lines that will look like the following  --line 29 
 
 
#and there is out output and this is perdect. so now , that we get the idea of the dynamic programming we should do the same to the others as well .
#so i  am going to go to my in it method and i am going to receive it again . 

# and i am going to do exact same  thing as we have done for the name of items 
# after writing that in under the method we can see that python is  again telling us that  ehere it is . so we will go to instance lines and add more values 
#corresponding to the added attributes under the method  and then we can finally allow us to delete previously written lines .abs(#then we will see for the output)
#in order to prove that it workd we are going tocopy the line 29 down then replace/add values  then run the file .

#output
#phone , laptop
#100
#5
#laptop
#1000
#3

#and as we can see we have got the correct output
#for each of our statement .
#that is thee way you shouls work with __init__mathod . 



# 1.now we have understood that each instance  that we create its going to  automatically called that many times the instance we create .
# and what does that mean ... that means not only we can allow ourselves to take more parameters and then do something with 
# them  and as you can see python is going to automatically complain why  the name argument is not filled in here 


#2.class item :
#    def __init__(self):
#        print('i am creative')
#    def calculate_total_price(self,x,y): 
#     return x*y
#item2=item()#instance 
#item2.name='laptop'#attributes for item2
#item2.price=1000#attributes for item2
#item2.quantity=3
# class item :
#    def __init__(self,name , )

# them  and as you can see python is going to automatically complain why  the name argument is not filled in here 
# so we can pass phone here and and if we change our print line to do something 


#3.class item :
#    def __init__(self,name):
#        print(f'An instance created:{ name }')
#    def calculate_total_price(self,x,y): 
#     return x*y
#item2=item('laptop')
#An instance created:laptop#instance 
#item2.name='laptop'#attributes for item2
#item2.price=1000#attributes for item2
#item2.quantity=3

# now we can also do this to other attribute like this 
# now that

#4. class item :
#    def __init__(self,name,price,quantity):
#        print(f'the name of instance:{ name }')
#        print(f'quantity of instance:{ price }')
#        print(f'the price of the instance :{ quantity }')
#    def calculate_total_price(self,x,y): 
#     return x*y
#item2=item('laptop',1000,4)
#item1=item('ipad',5000,10)



# the name of instance:laptop
#quantity of instance:1000
#the price of the instance :4
#the name of instance:ipad
#quantity of instance:5000
#the price of the instance :10



# now when we have done this but there is still something is not quite perfect 
# bcz we still pass the attribute of name here and here 
# now pay attention how the init method has to receive the self as a parameter as well 
# and we alread know reasons for that fact that we have self as a parameter could actually
# allow us to assign attributes from the onot method so that we not have to go ahead and 
# assign the attribute of name for each of the instances we create  
# so  it means that i can dynamically assign an atrtibute to an instance 
# from this method .
# so i can say --
# so i am assigning the attribute of name to each instance that is going 
# be created and i am making it equal to the name that is passed in from here .
# and that means now i can alllow myself to delete the hard coded line 
# also now i have the dynamic attribute addignment .
# bcz of the  this lines  -- self.name=name --
# and to check that attribute assignment worked 


# class item :
#    # dynamically assigning attributes 
#    def __init__(self,name,price,quantity):
#       self.name=name
#       self.price=price
#       self.quantity=quantity
       
       
#    def calculate_total_price(self,x,y): 
#     return x*y
#item2=item('laptop',1000,4)
#item1=item('ipad',5000,10)
#print(item1.name)
#print(item2.name)
#print(item1.price)
#print(item1.quantity)
#PS C:\Users\rekha\OneDrive\Desktop\oops> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/oops/ite.py
#ipad
#laptop
#5000
#10




# so that is the way you should work with  
# init method ,you should always take care of the 
# attributes that areassign to an object inside init method 
# couple of sidenotes that are important to remember 
# whaen we use init method 
# so say that you currently dont know much from a 
# specific item then you can go ahead and by default 
# receive the quantity parameter as 0 . and then this will mean 
# you will not have to pass in those quantity variables here 
# like this ==


# class item :
#    # dynamically assigning attributes 
#    def __init__(self,name,price,quantity=0):
#       self.name=name
#       self.price=price
#       self.quantity=quantity
       
       
#    def calculate_total_price(self,x,y): 
#     return x*y
#item2=item('laptop',1000,4)
#item1=item('ipad',5000)
#print(item1.name)
#print(item2.name)
#print(item1.price)
#print(item1.quantity)
#PS C:\Users\rekha\OneDrive\Desktop\oops> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/oops/ite.py
#ipad
#laptop
#5000
#10

# so this default value is something you want to remember 
# and another important thing is / one more quite important poiint is 
# you can assign attributes to specific instances individually 
# 
# so say that you want to know if the laptop has the numpad or not 
# and that is not an realestic attribute that you go ahead 
# and assign to a phone 
# then we can say that 
# and the fact that you want to use some attrinbute assignment 
# in the constructor doesnot mean that you can ot add some attributes that you like 
# after you instantiate the instances that you would like to 
# now that we understood this there is a one more problem we need to solve 

 

class item :
    # dynamically assigning attributes 
    def __init__(self,name,price,quantity=0):
       self.name=name
       self.price=price
       self.quantity=quantity
       
       
    def calculate_total_price(self,x,y): 
     return x*y
item2=item('laptop',1000,4)
item1=item('ipad',5000)

item2.has_numpad= False

# now notice that how in calculate total price it still t=receives x and y 
# the thing is why it still receives x , y we could for sure now  we could replace them in this method 
# as we know each method we designs in clsses then the object otself passed as the arguments 
# and for oops this is the most important behaiour that we need to understand 
# and the object itself passed as an argument that's why we receive self 
# this means  we can wite like this -- self.price*self.quantity--
# and we dont need to receive x,y --> this parameters anymore 
# we assign those attributes once the instancs has been created so this means that we have 
# access to those attributes throughout this method that we gonna add here .
 

class item :
    # dynamically assigning attributes 
    def __init__(self,name,price,quantity=0):
       self.name=name
       self.price=price
       self.quantity=quantity
       
       
    def calculate_total_price(self): 
       return self.price*self.quantity
item2=item('laptop',1000,4)
item1=item('ipad',5000)

item2.has_numpad= False 



