#it is exactly how it sounds ,it is solving problems by creating objects 
#the concept focuses on using reusable code 


# fisrt read through the notes 

#lets imagine you need to add two nu bers then
a=12
b=34
print("the sum of a and b is ",a+b)
#but with object oriented programming you can do something like this,
class Number:
    def sum(self):
        return self.a+self.b
    
num=Number()
num.a=12
num.b=34
s=num.sum()
print(s)

#well, for this it looks quite big but it really makes long codes short
'''
we write the syntax of class in PascalCase
PascalCase
EmployeeName-->PascalCase

camelCase
isNumeric,isFloat-->camelCase
'''