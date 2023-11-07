#lambda function to find the smaller element between two elements.



#The lambda function is an anonymous function. It can have any number of arguments but it can only have one expression.

#Syntax lambda arguments : expression

#In this article, we will learn how to find the smaller value between two elements using the Lambda function.


#Method 1: Using lambda and min() method

# lambda function to return minimum of
# two elements a, b are the arguments and
# min() method is the expression here.
get_min = lambda a, b : min(a,b)
  
print(get_min(5, 8))
#Output:

5
#Explanation: The a,b are passed to the lambda function and min() method is used as an expression to return the minimum element.

#Method 2: Using lambda and ternary operator

# lambda function to return minimum of two elements
# a, b are the arguments and ternary
# operator is used to compare two elements
get_min = lambda a, b : a if a < b else b
  
print(get_min(5, 8))
#Output:



5

#Explanation: a, b are the arguments and ternary operator is used for comparing two elements

#Method 3 :Using Tuple and lambda 

# Two lambda functions will be stored
# in tuple such that 1st element is b
# and 2nd element will be b.
# if [a<b] is true it return 1 and
# element with index 1 will print
# else if [a<b] is false it return 0,
# so element with index 0 will print
a = 5
b = 8
print((lambda: b, lambda: a)[a < b]())
#Output:

5
#Explanation: 

#Two lambda functions will be stored in a tuple such that 1st element is b and 2nd element will be b. if [a<b] is true it return 1 and element with index 1 will print else if [a<b] is false it return 0, so element with index 0 will print.