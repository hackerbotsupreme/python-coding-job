#inheritence is the way of creating a new class from an existing class
class Employee:
    company ="Google"

    def showDetails(self):
        print("thhis is an employee")

class Programmer(Employee):                       #quick knowledge:inheritence have three types.
    language="python"                             # 1.single inheritence
    company="youtube"                             #2.multiple inheritnce
                                                  #3.multilevel inheritence
    
    def getName(self):
        print(f"the language is{self.language}")  
        
    def showDetails(self):
        print("this is an programmer")  



e=Employee()
e.showDetails()
p=Programmer()
p.showDetails()
print(p.company)


    