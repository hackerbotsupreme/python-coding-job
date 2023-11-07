import csv # that will take the full responsibility to read the csv file 
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
#    def instantiate_from_csv(self):
    def instantiate_from_csv(cls):
        with open('iall_tems.csv','r') as f :
               reader=csv.DictReader(f)# now this method should go ahead and read our content as a list of dictionaries . # but at the end we should go and convert this into a list . 
               items= list(reader)# with that we have completed reading our csv file 
        for item in items:
            item(
                name = item.get('name'),
                price = item.get('price '),
                quantity = item.get('quantity '),
            )

#Item1=item('phone',100,5)
#Item2=item('laptop',1000,3)
#Item3=item('cable',10,5)#all of the five are instances 
#Item4=item('mouse',58,5)
#Item5=item('keyboard ',75,5)
     
    def __repr__(self):
        return  f'item("{self.name}",{self.price},{self.quantity})'

#Item1=item('phone',100,5)
#Item2=item('laptop',1000,3)
#Item3=item('cable',10,5)#all of the five are instances 
#Item4=item('mouse',58,5)
#Item5=item('keyboard ',75,5)


item.instantiate_from_csv()
print(item.all)    # this piece of code will show us the  behaviour  .
    


#print(item.all)
for instance in item.all:
    print(instance.name )




#=============================================explanation----------------------------------------------
#untill this point we understood how we can change that we represent our object anad we also understood 
#how we can access to all of our  instances by this class attribute that we intentionally named all . 

# and now lets takea a look and try to solve onne more problem that  we ahve in terms of best practices 
# when we are going to extend this application and  add more features now you can see that untill this point we maaintained all of 
#our information is as code in a file by only instantiatting . now whenn we will look to extend the application 
#and add more features then we might have a harder life to add those features because the aactual data in the code are maintained 
# location. intead of creating databases to handle the data we will iae somethimg called 
# csv-- csv stands for comma seperated values . 
# that mean you could go and make a csv file and you could store yoyur values as comma seperated wehere each line will represent a single structured  .
# data and csv is a great option here because it allows the data to be saved in a table  structured format 
# lets go and make  csv file 
#  we have made an csv file named - iall_items.csv 
# and lets go ahead and read our csv files and instantiate our instances  in a generic way . 
# and now it makes sense to hash thode five lines  and use them under the apply_disciunt line


#now the problem is we aer not going tpo have any instances on our hand to call this method  from the instance 
#because this method is actually desinged for intantantiating the object itself 
# so this means that this method  will not be called from an instance so the way that it is going tobe solved 
# is by converting this method  into a class method ,, now now a class method is a method that could be accessed in the 
#  --print(item.all)-- 
# follwing way 
# so now we will hash following line and write --
#item.insatantiate_from_csv()

# now this line will take ful responsibility to instantiate our object .
# and in order to convert this to a class method we need to a class method we need  to a decorator that will be responsible to 
#  to convert  this method into a class  method , now  decorators in python is just a quick way to change 
#  the behaviour of the function that we eill create by basically calling  them just before the line 
# that we create our  functio  so we could use the  add sign and use the class method in here and then 

# now if i was to write -- def instantiate_from_csv(cls):
#                              written this        (received parameter)
# pay attention here that we the received parameter is cls , so what is going on here . the thing is 
# whn we call ouur class methods then the class object itself is passed itself as the first argument in the background 
# so it is a bit alike the instance where it is also  passed as a first argument but this time when we called 
# a class method  in this approach , then the class reference must be passed  as a first argument so that is why
# you should still receive at least one parameter but we probanly  understand that we could not name this self 
# bcz that is just going to be too much confusing .. 
# ok so  
# lets write some code to read the csv file and instantiate some object .
# first we are giving it the with_open with permission to read  then under that we will
# use some metadata  to directly  reead the csv which at  the end of the day will be responsible to  conver t
#this to a python dictionary . 
# line --34--37 
# shift + tab = indent out 

# lets go over and see the results of iterating over the items list .
# def instantiate_from_csv(cls):
#       with open('iall_tems.csv','r') as f :
#               reader=csv.DictReader(f)# now this method should go ahead and read our content as a list of dictionaries . # but at the end we should go and convert this into a list . 
#               items= list(reader)# with that we have completed reading our csv file 
#        for item in items:
#            print(item) # # this piece of code will show us the  behaviour  .

# and lets run the code  and then .
# {'name': "'phone'", 'price': '100', 'quantity': '5'}
# {'name': "'laptop'", 'price': '1000', 'quantity': '3'}
# {'name': "'cable'", 'price': '10', 'quantity': '5'}
# {'name': "'mouse'", 'price': '58', 'quantity': '5'}
# {'name': "'keyboard '", 'price': '75', 'quantity': '5'}


# here you can see that i receive some dictionary in seperated lines . and that is because i iterate over a list of dictionaries .
# 
# the only thing we miss here is creating the instances , besides printing those  , we could now say something like 
# 





#  for item in items:
#            item(
#                name = item.get('name'),
#                pricr = item.get('price '),
#                quantity = item.get('quantity '),
#            )
#item.instance_from_csv()
# print(item.all)
# now this should be enogh to instantiate our  instances now i can go ahead and pass my arguments here by basically reading the keys from a dictionary 
# so ,i can say the following on above
# and lets see what would happen if i call this method and as well as calling the attribute of item.all because this one [item.all] stores all the instances 
# inside the list . Now  if i was to go ahead and run it .
# 



# name = item.get('name'),
#                price = int(item.get('price ')),
#                quantity = int(item.get('quantity ')),
# now these three lines are working with  this structure of a data  in 'iall_tems' .

# now let if we change the data of ---'keyboard ',75,5 ---- 'keyboard ',74.90,5 --
# to this then we can see that we receive some problems but we need to convert the price not to 
#  an integer but to a  float  like that . and that is the only way to get over this . 
# name = item.get('name'),
#                price = float (item.get('price ')),
#                quantity = int(item.get('quantity ')),

# because we  dont want to convert the price to an industial directly  because it could be 
# float . so , now we could go ahead and see that it works perfectly .
# although we see the price as 100.0 and like that 
#
