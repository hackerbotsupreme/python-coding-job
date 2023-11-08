#concept :parent 1+ parent 2= child

class Freelancer:
    company="Fiverr"
    level=0
    
    def  upgradelevel(self):
        self.level=self.level+1
class Employee:
    company="visa"
    ecode=120

class Programmer ( Freelancer,Employee):
    name="rohit"




p=Programmer()
p.upgradelevel()
print(p.company)