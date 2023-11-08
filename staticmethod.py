class Employee:
    company="google"
    def getsalary(self):
        print("salary is 100k")

harry=Employee()# salary is 100k is printed twice you need to understand computer is so simple as if you 
# see something printed twice then that means command should have been passed twice
harry.getsalary()
Employee.getsalary(harry)

#lets talk about 'self'
# parameter --- self refers to the instance of the class it is an automatically passed with a function call from an object
class Employee:
    company="google"
    def getsalary(self):
        print(f"salary for the employee working in {self.company} is {self.salary}")
    @staticmethod#A static method does not receive an implicit(means inherent, ontornihit) first argument. 
    def greet(self):
        print("good Morning,master aloke ")
harry=Employee()
harry.salary=100000
harry.getsalary()#Employee.getsalary(harry)
harry.greet()#Employee.greet() missing 1 required positional argument: 'self'
# so one thing is whenever i am enabling "@static method"  the return for 
# harry.greet()[empliyee.greet] is TypeError: Employee.greet() missing 1 required positional argument: 'self'
#but when i am disabling the @staticmethod  the return is--
#salary is 100k
#salary is 100k
#salary for the employee working in google is 100000
#good Morning,master aloke
# so how does the @staticmethod is working 
#sometimes we need a function that doesnot use the self parameter we cwn  define a ststic method ,
# the fuction or item we write under it that become static
#@staticmethod Characteristics
#Declares a static method in the class.
#It cannot have cls or self parameter.
#The static method cannot access the class attributes or the instance attributes.
#The static method can be called using ClassName. MethodName() and also using object. ...
#It can return an object of the class
# Why should I use @staticmethod in Python?
#staticmethods can be used when the code that belongs to a class doesn't use the object
# itself at all. Python doesn't have to instantiate a bound method 
# for each object we instantiate. Bound methods are objects too, and creating them has a
# cost. Having a static method avoids that
