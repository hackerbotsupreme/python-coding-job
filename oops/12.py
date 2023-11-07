# i will specify here that whenn to use static method wen to use class method 
# so we can completely understand the difference between those  bexause i remember  myself  i had a very tough time to 
# understand why i need this and why i need that 

# when you should use the static method ?
class Item:
    @staticmethod ()
    def is_integer():
        pass
class Item:
    @classmethod ()
    def is_integer():
        pass


# now when should you use the static method  , ehrn you want to do something that has a relationship 
# with class , but not something that mst be unique per instance !



# when should you use the @classmethod ?
# you want to create class methods for instantiating instances from some stuctured data that you own 
# this should also do ssomething that has a relations ship with the lcass , but usually , those are used 
# to manipulate different structures  of data to instantiate  objects , llike   we have done with csv . 


# now the only main difference between the class and ststic method that  staticmethod is not passing the object 
# reference as the first argument in the backgroud . 
# it is noticable from the fact that we dont have a special highlight purple was the first parameter 
# so if you remember if i was to go ahead use here a first parameter in the @staticmethod like num
# then you will see that this is the first parameter that is colourred with orange as that is regular parameter ,
# but num in the classmethod is a mandatory parameter as also its coloured in purple . 



# now if you remember that i intentionally said that @class,ethod and #sttaticmethod could only be called 
# from the class level but however .   
# those are also called from the instances .


# as you can see i can  actually instantiate an object . 

item1= Item()
item1.is_integer(5)
item1.instantiate_from_something()

