item1='phone'
item1_price=100
item1_quantity=5
item1_price_total=item1_price*item1_quantity 


print(type(item1))#<class 'str'>
print(type(item1_price))#<class 'int'>
print(type(item1_quantity))#<class 'int'>
print(type(item1_price_total))#<class 'int'>
# what is happening is whenever we write something and run it python first identify what we have written then mathch and instantitate the assigned object 
# so actuallay python treats everything as an object and instantiate and process that whenever it needs.
# so here we can think rathere then making a varible for certain type we can tell python to make our own classes and objects so that that we could also add, edit within our comfort .
# so to instantiate an object we need to  tell python that we want to make a  class for an object  . 
# so the process consists of /made up of two parts 1.creating class for the object  then 2. instantiating the object 

#if we were to print data types of each variables then wewill receive their types  as above and  i want  you to notice here that we can see the word  'class' eing constantly used in the output
#so thats mean , first python treats everything as a object second , this means that those data types are instaces of strings and ints 
#so in python each datatypes is an object that has been instantiated by some class earlier and for the item 1  variable  that has beeen instantiated  from a string  typr of class ans for the price and price total .abs(

#what is oop?

#so the conclusion is   for each of the we also see the keyword class now  this means that those data types are actually instances of strings and integers 
#so in python programming language each data types is an object that has been instantiated earlier by some class and  for the above item 1 variable 
#that has been instantiated from a string type of class and for the price quantity and price total those have been instantiated from a class that is named int 
#so it could have been nicer if we tell the python that  we want to create a datattype of our own it will allow us to write a code that we can reuse in future easily if we needed 
#each instance could have attributes to  describe related information about it . and we can think about some good can didates for attributes we could have 
#for our item data type .  

#so now we will rewrite the above code with oop.
class Item :# creating class for an object
    #here --item -- is the name of the class 
    pass#here , ehatever we write here will implemented to this class 
# by creating a class you will not need to repeat similar actions repeatedly 
# by elsewhere if you continue with creating variables (will also contain loops etc.etc. )
# you have to repeat same steps again and again to get the job done 
# with that you will be exhausted also eventually the code
# will become so long that after one point of time you 
# will start to forget what this piece of do and what the
# others ones . the same facts are applicable to every other real world application like. games, applications, apps , websites etc
# so it is very very important to master opps right after you are familiar with basics .
# practice old concepts and learn the oops along side 
# so basics , oops  ,  modules and lastly how objects are working in the python itself mastering these will make 
# you absolute master .

# and yah one more important thing is that we need to know hoe objects are working in the python itself 


#now that we have created class we have permission to create instances .
# and after that we can give attributes to our object . 



# so we need to say 
# name of the object =name of the class # it will instantiate an object of our created class 
item1=Item()#creating instance for the above class 
item1.name='phone'#creating attribtes to the instances  of a class and that is achievable by using the dot sign 
item1.price=100
item1.quantity=5

#now in this stage you might ask yourself what is the difference between random variables that we created to those four lines ?

#well, here we can see we have a relationship we actually have a relationship between those four lines because each one of the attributes are assigned to one instance of the class . so now if we do this,
print(type(item1))#<class '__main__.item'>
print(type(item1.name))#<class 'str'>
print(type(item1.price))#<class 'int'>
print(type(item1.quantity))#<class 'int'>
#also you can see that by yourself , going ahead and tey to print the types of item1and as well as the types of the attributes of the 
#name , price and quantity , now if we were to print that check out the result if i was to  run this program so we can see that we have a data type of item here and
#that, data type of Item  is the big difference between what we have seen previously to this thing that wwe have juxt created . now we understtod how we can create our own datat types .
#let's go ahead and see what are the resst of the benefits using oop .
#<class '__main__.item'># data type of Item 
#<class 'str'>
#<class 'int'>
#<class 'int'>
 



#untill now we undesttod how to add attributes  to the  instances ,we should also understand that how we create  some methods and execute them on our 
#instances  now if  we will take as an example  , the building class of string  then you know that  we  have some methods that we can go ahead and 
#execute for each of our string and for this example we can see that i grabbed an instance  of a string  that i named random str , then i go ahead in 
#that  i named  random str  and then i go  ahead in the next line and execute  the opera method which if you remembes is it's  possible to grab all
#letters and turn them in to upper case now the biggest question here is how we can go ahead and design som emethods that are going tobe  allowed to execute 
#and the answer is inside our class so we could go inside our class and write some methods that will be accesible from our instances so we could go ahead and say .
name='aloke'
print(name.upper())# string method
# ALOKE # so we can see python itself has its method for its instances so how do we add methods or rules or functions to our instances ? 
# so now we will see how we can create some methods and excute them on our attributes . 
# we can  do that by defining the the function under our class . 
#like this------------>
class item :#here --item -- is the name of the class 
# now a good candidate for the method we would like to create now is calculate_price#now just aquick sidenote when you will hear me say methods then i basically mean two functions inside classes because  in terms of python or in any programming language when you have isolated definations with this kayword , then those are considered tobe called functions but when you goahead and create those functions inside classes then those are called methods . 
#and as we understand it could have been noice to have a method that will go ahead and calculate the total price 
    def calculate_total_price(self,x,y):# creating a method 
     return x*y
item2=item()
item2.name='laptop'
item2.price=1000
item2.quantity=3
print(item2.calculate_total_price(item2.price,item2.quantity))# creating a method # the action we doing now is we are calling this method for item1 .
##when you go ahead and call any  method from an instance python itself  passes the object as the first argument everytime and that is why we are not allowed to create such 
# methods that never receive parameters in oops in any programming language .
# you can also check that by --


#output is 3000
#now by opening up closing those parenthesis  then you are going to see  one parameter that is auto generated that python eants us to receive 
#intentionally now python passes the object itself as a forst argument when you go ahead and call those methods .
#now if  i was go here and say item one dot calculate total price ,
item1=item()#creating instance for the above class 
item1.name='phone'#creating attribtes to the instances  of a class and that is achievable by using the dot sign 
item1.price=100
item1.quantity=5
print(item1.calculate_total_price(item1.price,item1.quantity) )#output is 500 

# one more thing that we can go ahead and use method from any on any of our instances 
# and at the same time we can tell that if there was going to be any variable then for every operation we have been needed to create that again and again .


#so untill now we understood that  we can assign attributes and as well as  creating some methods that we can go ahead and use them to our instances directily ,



