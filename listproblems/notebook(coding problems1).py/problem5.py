#write a program to find minimum of two num  
#attempt 1 
a=(int(input('enter the first number :')))
b=(int(input('enter the second number :')))
M=min(a,b)
print('th eminimum of two number is :',M)
#attempt2
def minimumnumber(a,b):
    return min(a,b)
m=minimumnumber(5,6)
print('the minimum of two number is ',m)
#attempt 3
#lets dive deep into minimum
def min(c,d):
    if c>d:
        return d
    else:
        return c
r=min(7,2)
print('the minimum of two numbers are',r)
