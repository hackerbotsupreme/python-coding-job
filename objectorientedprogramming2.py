class RailwayForm:
    formtype="railwayform"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")
        
    
harrysapplication=RailwayForm()
harrysapplication.name="harry"
harrysapplication.train="rajdhaniexpress"
harrysapplication.printdata()

#a simple awy toimagine this is 
#class-->noun/object before initiation) --> employee
#objective-->attribute-->                  name,age,salary-->attributes are of two types-- class (property of class) atteributes, instance attributes 
#verbs------->methods to  get data---------->get.salary(),salary.incrment()

#demonstratiion of attributes 
class employee:
    company="google"
    salary=500

harry=employee()
rajni=employee()
#creating instance attribute salary for the both objects 
harry.salary=300
rajni.salary=500
print(harry.company)
print(rajni.company)
employee.company="youtube"# adding instance attribute 
print(harry.company)#when we adds an instance attribute  the program access the given data from the instance attribute not from class 
print(harry.salary)
print(rajni.salary)#300
print(rajni.company)#500#instance attribute take preferece over class attribute during retrival of the data 





