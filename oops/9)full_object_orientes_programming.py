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
     
     
    def __repr__(self):
        return  f'item("{self.name}",{self.price},{self.quantity})'

Item1=item('phone',100,5)
Item2=item('laptop',1000,3)
Item3=item('cable',10,5)#all of the five are instances 
Item4=item('mouse',58,5)
Item5=item('keyboard ',75,5)

print(item.all)
for instance in item.all:
    print(instance.name )

Item2.pay_rate=0.7
Item2.apply_discount()
print(Item2.price)
Item1.apply_discount()
print(Item1.price)



#=================================explanation=========================================
# considering that your shop is going to be larger in the future an dyou are going to have more items 
# then  the more items you are going to have the more filtration like things you want todo in the future 
# and what is currntly problematic with our class is that we dont have any resourse where we can just
#access all the items we have in our shop right now . 

#it could have been nicer if we could somehow have a list all the item instances that we have created untill this point .
# but currently there is not an approach that give us a list with five elements where each 
# each element will represent an instance of a class .

# so in order to come up with such design then here is wonderful candidate for creating a class attribute --
# Item5=item('keyboard ',75,5)
#that we could name all and once we do this then we are gonna see how we are going to  add our 
# instances to that list. so i will go ahead and start with like--
#    all= [] # all sets to empty list 
#now we need to figure out how we are going to add our instances for each time that we are going 
# go ahead and create an instance  and if you remember __init__ method  is being called 
# immediately once the instance has been created . so i might be a good idea going down below --
# inside the __init__ method use a code that will responsible to append to the list , every time we create 
# an instance and that  will be as easy as saying something like -- line 
#        Item.all.append(self)
# now once we know that self is actually the instance itself every time that it is being created.so once we 
#so once we go ahead and launch such comment  in side of init method then for each instance that 
# is going to be created this whole list is going to be filled with our instances . now
#to show you that i can jump a line  after we create the intances ,and we can say print item that all.
#and now if i was to run our program--


#[<__main__.item object at 0x000001778CE6BFD0>, <__main__.item object at 0x000001778CE6BDF0>, <__main__.item object at 0x000001778CE6BD90>, <__main__.item object at 0x000001778CE6BD30>, <__main__.item object at 0x000001778CE6BCD0>]
#700.0
#80.0
#PS C:\Users\rekha\OneDrive\Desktop\oops>

# then you are going to see we're going to have a list with five instances and when we scroll right a bit 
# we can see that i have exactily five elements and that is perfect . now i have exactly five elements .


# now thats going to be extremely useful when we want to do domething with only one of the attribute . 
# so say  that you like to print all the names for all of your instances then you can easily 
# use a for loop to achieve such a task . so we can go ahead and say -- line  40 -- 


#for instance in item.all:
#    print(instance.name )


# and once we have come up with this we can see---
#  phone
#  laptop
#  cable
#  mouse

# we can see that we have all the names 
# and that going to be useful here and there esprcially if you know the filter function 
# for example to apply some special things on some of the instances that are matching your criteria .



#now that we have understood this we can also solve one problem here  we saw previously.
# for this we have to focus on  output of -- print(Item.all ) --
#[<__main__.item object at 0x000001778CE6BFD0>, <__main__.item object at 0x000001778CE6BDF0>, <__main__.item object at 0x000001778CE6BD90>, <__main__.item object at 0x000001778CE6BD30>, <__main__.item object at 0x000001778CE6BCD0>]
#700.0
#80.0
#PS C:\Users\rekha\OneDrive\Desktop\oops>
# and you could see the way that the object is being represented is not too friendly .
# now , could have been nicer if we could have been some how change the way the object is being represented in the list here .
# now , the way to achieve this using a certain method inside our class that is __repr__ method .
# and repr stands for represenying your object .
# and that is why you can actually go ahead and use this method an then...........
# you will have to control your display your objects when you are printing  them in the console ,now , i 
# recommend watching a video that comapares the method similar to it which is __str___
# and you can take a look in the desciption of thsi video of this entire series  . 
#



# so i am going to say --  


#now what we can do now is returning  a string that will be responsible to represent a string .
#that will be responsible  to represent  this object .
# now, obviously we dont want to use something that is not unique for each of the instances . 
#because that i was to use now return items , something  like that , and run  our program , then you can 


#  see that  i am going to  receive a list which is going to this string -'item' - five times .
#def __repr__(self):
#       return  'item'

#[item, item, item, item, item]- output
#but it is still hard to identify which onstance represents which string here it could be helpful if we were to
#return a string that could be unique .
#so now we will use a formatted string and in order to make this unique it is a best practice that we represent it 
# exactly how we have created and then  i am going to make the string here as much to the way that we created those instances 
#   so we will start by typing ---
#        return  f'item("{self.name}",{self.price},{self.quantity})'

# first we 're going to type doble quotes to escape from the singke quotes then i am going to refer to the value of name by using 
# self.name and then i will leave my quotes and comma then i am going to refer to the value of our price 
# then  comma then similarly  i am going to refer to the value of our quantity .
# [item("phone",100,5), item("laptop",1000,3), item("cable",10,5), item("mouse",58,5), item("keyboard ",75,5)]

#and now we can see that we receive a list that is way mre friendly  than what we have seen  previously . 
# and we can also see that this first element for example is quite equivalent to line -- 36 to 40 --
# and there is also a reson behind  why we have worked this hard just to represent the output similar to our lines 
# because it is just a best practice means  the more friendly we make the code to understand for python 
# to the same extent python will understand us . also by phthon.org .





#49.52




