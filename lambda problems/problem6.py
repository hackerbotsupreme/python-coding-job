#how to use if ,else and elif in python lambda functions.



#Lambda function can have multiple parameters but have only one expression. This one expression is evaluated and returned. Thus, We can use lambda functions as a function object. In this article, we will learn how to use if, else & elif in Lambda Functions.

#Using if-else in lambda function
#The lambda function will return a value for every validated input. Here, if block will be returned when the condition is true, and else block will be returned when the condition is false. 

#Syntax:

#lambda <arguments> : <statement1> if <condition> else <statement2>

#Here, the lambda function will return statement1 when if the condition is true and return statement2 when if the condition is false.

#Example:

#Here, We are going to find whether a number is even or odd. when we pass number 12 to lambda function it will execute statement 1 and statement2 for 11. 

# Use if-else in Lambda Functions

# check if number is even or odd
result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"

# print for numbers
print(result(12))
print(result(11))


#Output
#12 is even
#11 is odd
#Using if else & elif in lambda function
#We can also use nested if, if-else in lambda function. Here we will create a lambda function to check if two number is equal or greater or lesser. We will implement this using the lambda function.

#Syntax:

#lambda <args> : <statement1> if <condition > ( <statement2> if <condition> else <statement3>)

#Here, statement1 will be returned when if the condition is true, statement2 will be returned when elif true, and statement3 will be returned when else is executed. 

#Example:

#Here, we passed 2 numbers to the lambda function. and check the relation between them. That is if one number is greater or equal or lesser than another number


# Use if-else in Lambda Functions
 
# check if two numbers is equal or greater or lesser
result = lambda x,y : f"{x} is smaller than {y}" \
if x < y else (f"{x} is greater than {y}" if x > y \
               else f"{x} is equal to {y}")
 
 
# print for numbers
print(result(12, 11))
print(result(12, 12))
print(result(12, 13))
 
 

#Output
#12 is greater than 11
#12 is equal to 12
#12 is smaller than 13