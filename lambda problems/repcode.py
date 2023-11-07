square = lambda x : x*x if(x > 0) else None

print(square(4))
square = lambda x : x*x if(x > 0)
 
print(square(6))
#Output:

#File "/home/2c8c59351e1635b6b026fb3c7fc17c8f.py", line 2
#    square = lambda x : x*x if(x > 0)
#                                   ^
#SyntaxError: invalid syntax

#The above code on execution shows SyntaxError, as we know that a lambda function must return a value and this function returns x*x if x > 0 and it does not specify what will be returned if the value of x is less than or equal to 0.

#To correct it, we need to specify what will be returned if the if-condition will be false i.e. we must have to specify its else part.

#Let’s see the above code with its else part.
#finding the square of a number using lambda function 

square=lambda x:x*x#syntax :lambda arguments : expression
print(square(3))#squre(functon name) then (brackets) means --stquare of 

#finding the sum of a number using lambda function 
add=lambda x,y:(x+y)#syntax :lambda arguments : expression
print(add(3,6))

#writing a program to add two given numbers
def addtwonumber(x,y):
    return (x+y)
print(addtwonumber(25364,4796874))


#The Fibonacci numbers are the numbers in the following integer sequence.
#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
#In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation 

#    Fn = Fn-1 + Fn-2
#with seed values  

#   F0 = 0 and F1 = 1.


# Function for nth Fibonacci number
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Driver Program
print(Fibonacci(9))
#write a python program to find maximum number between two numbes

maximumbetweentwonumbers=lambda x,y:print(x) if(x>y) else print(y) 
maximumbetweentwonumbers(2,3)

#output--- memorize it 
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe "c:/Users/rekha/OneDrive/Desktop/lambda problems/random.py"
#3
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> 

#give your attention on this 
maximumbetweentwonumbers=lambda x,y:print(x) if(x>y) else print(y) 
print(maximumbetweentwonumbers(2,3))

#output---note that whenwe add print to the previos code it is giving none ----implying no value to print 
# as whatever value was there already printed by function inside this 
#3
#None
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> 

#some old but precious tricks=============================================================================================================
str='alokepramanik'
print(str)
str=''.join(reversed(str))
print(str)


string='alokepramanik'
string=sorted(string)
print(string)
string=''.join(sorted(string))
print(string)




list=[1,2,4,5,7,8,9,0]
print(sorted(list))
#================================================================================================================================================
