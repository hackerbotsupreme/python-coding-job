#write a program to find the maximum of two numbers given by the user  in python 


#concept
#use of max function that returns the  greatest of two numbers 
#def stops at return 
#attempt  1
    
a=int(input("enter the first num :"))
b=int(input("enter the second num :"))
M=max(a,b)

print("the maximum of two numbers is",M)

# concept 
#lets try def function as this func gets used in almost every case
def Greatestnum(c,d) :
    c=int(input("enter the first num :"))
    d=int(input("enter the second num :"))
    w=max(c,d)
    return w
#lesson
#def does not takes command of taking inputs it takes command to  perform operations  


#attempt 3
# lets deep into max function 
def maximun(num1,num2):
    if num1<num2:
        return num2
    else:
        return num1

a=maximun(4,5)
print("maximum of two numbers are",a)
     





