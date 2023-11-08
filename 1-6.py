#***write a program to find greatest of four numbers entered by the user**** 
num1=int(input('enter the num1:'))
num2=int(input('enter the num2:'))
num3=int(input('enter the num3:'))
num4=int(input('enter the num4:'))

if(num1>num4):
    f1=num1
else:
    f1=num4
if(num2>num4):
        f2=num2
else:
    f2=num4
if(f1>f2):
    print("the greatest of four number is:",f1)
else:
    print("the greatest of four numbers is:",f2)
 
