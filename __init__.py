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
    
    def __init__(self,name ,salary,subunit) :
        self.name=name
        self.salary=100
        self.subunit=subunit
        print("Employee is created")#__init__ is a special method which runs as fast as soon as the object is created .
                                    #it takes self argument and can also take further arguments.
        
    def getdetails(self):
        print(f'the name of the employee  is {self.name}')    
        print(f'the name of the employee  is {self.salary}')    
        print(f'the name of the employee  is {self.subunit}')    

    def getsalary(self,signature):
        print(f"salary for this emplloyee working in {self.company} is {self.salary}")
    def getsalary(self):
        print(f"salary for the employee working in {self.company} is {self.salary}")
        
        
    #@staticmethod#A static method does not receive an implicit(means inherent, ontornihit) first argument. 
    def greet(self):
        print("good Morning,master aloke ")
        
harry=Employee("harry",100,"youtube")
#TypeError: Employee.__init__() missing 3 required positional arguments: 'name', 'salary', and 'subunit'       
harry=Employee()
harry.salary=100000
harry.getsalary()#Employee.getsalary(harry)
harry.greet()#Employee.greet() missing 1 required positional argument: 'self'