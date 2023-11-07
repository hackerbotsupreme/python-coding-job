#lambda with if but without else in python
#Lambda with if but without else in Python


#In Python, Lambda function is an anonymous function, which means that it is a function without a name. It can have any number of arguments but only one expression, which is evaluated and returned. It must have a return value.

#Since a lambda function must have a return value for every valid input, we cannot define it with if but without else as we are not specifying what will we return if the if-condition will be false i.e. its else part.

#Let’s understand this with a simple example of lambda function to square a number only if it is greater than 0 using if but without else.
# Lambda function with if but without else.

# Lambda function with if but without else.
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


# Lambda function with if-else
square = lambda x : x*x if(x > 0) else None

print(square(4))
#16

# Example of lambda function using if without else
mod = lambda x : x if(x >= 0)

print(mod(-1))

# Example of lambda function using if-else
mod = lambda x : x if(x >= 0) else -x

print(mod(-1))


#1
#Example #3: The first code is with if but without else then second is with if-else.
# Example of lambda function using if without else
max = lambda a, b : x if(a > b)

print(max(1, 2))
Output:

#File "/home/8cf3856fc13d0ce75edfdd76793bdde4.py", line 2
 #   max = lambda a, b : x if(a > b)
 #                                 ^
#SyntaxError: invalid syntax
#Now, let’s see it using if-else.


# Example of lambda functi
# Example of lambda function using if-else
max = lambda a, b : a if(a > b) else b

print(max(1, 2))
print(max(10, 2))


#ouyput 
#2
#10



