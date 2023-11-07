#iterating with python lambda
#In Python, the lambda function is an anonymous function. This one expression is evaluated and returned. Thus, We can use lambda functions as a function object. In this article, we will learn how to iterate with lambda in python.

#Syntax:

lambda variable : expression
#Where,

#variable is used in the expression
#expression can be an mathematical expression
#Example 1:

# In the below code, We make for loop to iterate over a list of numbers and find the square of each number and save it in the list. And then, print a list of square numbers.


# Iterating With Python Lambdas
  
# list of numbers
l1 = [4, 2, 13, 21, 5]
  
l2 = []
  
# run for loop to iterate over list
for i in l1:
      
    # lambda function to make square 
    # of number
    temp=lambda i:i**2
  
    # save in list2
    l2.append(temp(i))
  
# print list
print(l2)
#Output:

[16, 4, 169, 441, 25]
#Example 2:



#We first iterate over the list using lambda and then find the square of each number. Here map function is used to iterate over list 1. And it passes each number in a single iterate. We then save it to a list using the list function. 


# Iterating With Python Lambdas
  
# list of numbers
l1 = [4, 2, 13, 21, 5]
  
# list of square of numbers
# lambda function is used to iterate 
# over list l1
l2 = list(map(lambda v: v ** 2, l1))
  
# print list
print(l2)
#Output:

[16, 4, 169, 441, 25]
#Example 3:

#In the below code, we use map, filter, and lambda functions. We first find odd numbers from the list using filter and lambda functions. Then, we do to the square of it using map and lambda functions as we did in example 2.


# Iterating With Python Lambdas
  
# list of numbers
l1 = [4, 2, 13, 21, 5]
  
# list of square of odd numbers
# lambda function is used to iterate over list l1
# filter is used to find odd numbers
l2 = list(map(lambda v: v ** 2, filter(lambda u: u % 2, l1)))
  
# print list
print(l2)
#Output:

[169, 441, 25]