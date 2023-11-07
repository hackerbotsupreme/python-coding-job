# distinction between  class attributes and instance attributes 
# 1.Overall, the key difference between class attributes and instance attributes is 
# that class attributes are shared among all instances of a class, while instance attributes
# are unique to each instance. Class attributes are typically used to store information that is common
# to all instances of a class, while instance attributes are used to store information that is specific to 
# each individual instance. Understanding the difference between these two types of attributes is crucial 
# for writing effective and maintainable object-oriented code in Python.the key point to remember is that 
# class attributes are shared among all instances of a class, while instance attributes are unique to each
# instance. Class attributes are typically used to store information that is common to all instances of a class, 
# while instance attributes are used to store information that is specific to each individual instance.



# __init__ method :
#are the attributes in the __init__ are class attributes ?

#No, attributes defined in the __init__ method are instance attributes, not class attributes. The __init__ method is called when an instance of the class is created, and it is used to initialize the instance attributes with specific values.

#Class attributes, on the other hand, are defined directly in the class body, outside of any methods, and are shared by all instances of the class. They are typically used to store information that is common to all instances of the class.

#Here is an example to illustrate the difference:

#ruby
#Copy code
class MyClass:
    email='alokepramanik@gmail.com '# now i can call this a class attribute  bcz whnever i print/ask for the email from any of our class it's gonna return this not an error 
    
    
    
    class_attribute = "I am a class attribute"

    def __init__(self, instance_attribute):
        self.instance_attribute = instance_attribute
#In the above example, class_attribute is a class attribute that is defined outside of the __init__ method and is shared by all instances of the MyClass class. instance_attribute, on the other hand, is an instance attribute that is defined inside the __init__ method and is specific to each instance of the MyClass class.

#To access the class attribute, you can use the class name, like this:

#scss
#Copy code
print(MyClass.class_attribute)
# Output: "I am a class attribute"
#To access the instance attribute, you need to create an instance of the class first, like this:

#scss
#Copy code
my_instance = MyClass("I am an instance attribute")
print(my_instance.instance_attribute)
# Output: "I am an instance attribute"
#So, instance_attribute is not a class attribute because it is defined inside the __init__ method and is specific to each instance of the class.


# you can say the oopposite too like 'aloke'and '20' below are only and only  unique to the p1  
# and similarly 'milan' and '21'  are only and only unique to the  p2 
# and that's why they are instance attribute as i said earlier that class attributes will be common to each of instances 

# 3.via example :
class perseon :
    email='alokepramanik@gmail.com '# now i can call this a class attribute  bcz whnever i print/ask for the email from any of our class it's gonna return this not an error 

    def __init__(self, name, age ):# class attribute 
        self.name= name
        self.age= age
p1=perseon('aloke', '20')# not  common to each class so instance attribute 
print(p1.name, ': name is our class attribute as not  common to each class so instance attribute ')
print(p1.age,': age is our class attribute as not  common to each class so instance attribute ')
p2=perseon('milan', '21')# not  common to each class so instance attribute 
print(p1.email,': this is class attribute as common to each of our instance so ')
print(p2.email,': this is class attribute as common to each of our instance so ')
# a class attribute  bcz whnever i print/ask for the email from any of our class it's gonna return this not an error  and common to every instance 



