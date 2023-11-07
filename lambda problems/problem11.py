#using lambda function()  with reduce()  function in the python.

#Python Lambda Functions are anonymous function means that the function is without a name. As we already know that the def keyword is used to define a normal function in Python. Similarly, the lambda keyword is used to define an anonymous function in Python. 


#Python Lambda Function Syntax
#Syntax: lambda arguments: expression

#This function can have any number of arguments but only one expression, which is evaluated and returned.
#One is free to use lambda functions wherever function objects are required.
#You need to keep in your knowledge that lambda functions are syntactically restricted to a single expression.
#It has various uses in particular fields of programming, besides other types of expressions in functions.

#Python Lambda Function Example

str1 = 'GeeksforGeeks'
 
# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))

#Output:

#SKEEGROFSKEEG
#Explanation: In the above example, we defined a lambda function(rev_upper) to convert a string to it’s upper-case and reverse it.

#Use of Lambda Function in Python
#Example 1: Condition Checking Using Python lambda function

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:,.2f}"
 
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
#Output:

#Int formatting: 1.000000e+06
#float formatting: 999,999.79
#Example 2: Difference Between Lam

#Example 2: Difference Between Lambda functions and def defined function
def cube(y):
	return y*y*y


lambda_cube = lambda y: y*y*y


# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))

# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))


def cube(y):
    return y*y*y
 
 
lambda_cube = lambda y: y*y*y
 
 
# using function defined
# using def keyword
print("Using function defined with `def` keyword, cube:", cube(5))
 
# using the lambda function
print("Using lambda function, cube:", lambda_cube(5))
#Output:

#Using function defined with `def` keyword, cube: 125
#Using lambda function, cube: 125
#As we can see in the above example, both the cube() function and lambda_cube() function behave the same and as intended. Let’s analyze the above example a bit more:

#With lambda function	Without lambda function
#Supports single line statements that returns some value.	Supports any number of lines inside a function block
#Good for performing short operations/data manipulations.	Good for any cases that require multiple lines of code.
#Using lambda function can sometime reduce the readability of code.	We can use comments and function descriptions for easy readability.
#Practical Uses of Python lambda function
#Example 1: Python Lambda Function with List Comprehension
#In this example, we will use the lambda function with list comprehension.


is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
 
# iterate on each lambda function
# and invoke the function to get the calculated value
for item in is_even_list:
    print(item())
#Output:

10
20
30
40
#Explanation: On each iteration inside the list comprehension, we are creating a new lambda function with default argument of x (where x is the current item in the iteration). Later, inside the for loop, we are calling the same function object having the default argument using item() and getting the desired value. Thus, is_even_list stores the list of lambda function objects.

#Example 2: Python Lambda Function with if-else
#Here we are using Max lambda function to find the maximum of two integers.


# Example of lambda function using if-else
Max = lambda a, b : a if(a > b) else b
 
print(Max(1, 2))
#Output:

2
#Example 3: Python Lambda with Multiple statements
#Lambda functions does not allow multiple statements, however, we can create two lambda functions and then call the other lambda function as a parameter to the first function. Let’s try to find the second maximum element using lambda.


List = [[2,3,4],[1, 4, 16, 64],[3, 6, 9, 12]]
 
# Sort each sublist
sortList = lambda x: (sorted(i) for i in x)
 
# Get the second largest element
secondLargest = lambda x, f : [y[len(y)-2] for y in f(x)]
res = secondLargest(List, sortList)
 
print(res)
#Output:

[3, 16, 9]
#Explanation: In the above example, we have created a lambda function that sorts each sublist of the given list. Then this list is passed as the parameter to the second lambda function, which returns the n-2 element from the sorted list, where n is the length of the sublist.

#Lambda functions can be used along with built-in functions like filter(), map() and reduce().

#Using lambda() Function with filter()
#The filter() function in Python takes in a function and a list as arguments. This offers an elegant way to filter out all the elements of a sequence “sequence”, for which the function returns True. Here is a small program that returns the odd numbers from an input list: 

#Example 1: Filter out all odd numbers using filter() and lambda function
#Here, lambda x: (x % 2 != 0) returns True or False if x is not even. Since filter() only keeps elements where it produces True, thus it removes all odd numbers that generated False.


li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
#Output:

[5, 7, 97, 77, 23, 73, 61]
#Example 2: Filter all people having age more than 18, using lambda and filter() function

# Python 3 code to people above 18 yrs
ages = [13, 90, 17, 59, 21, 60, 5]
 
adults = list(filter(lambda age: age > 18, ages))
 
print(adults)
#Output:

[90, 59, 21, 60]
#Using lambda() Function with map()
#The map() function in Python takes in a function and a list as an argument. The function is called with a lambda function and a list and a new list is returned which contains all the lambda modified items returned by that function for each item. Example: 

#Example 1: Multiply all elements of a list by 2 using lambda and map() function

# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
 
final_list = list(map(lambda x: x*2, li))
print(final_list)
#Output:

[10, 14, 44, 194, 108, 124, 154, 46, 146, 122]
#Example 2: Transform all elements of a list to upper case using lambda and map() function

# Python program to demonstrate
# use of lambda() function
# with map() function
animals = ['dog', 'cat', 'parrot', 'rabbit']
 
# here we intend to change all animal names
# to upper case and return the same
uppered_animals = list(map(lambda animal: animal.upper(), animals))
 
print(uppered_animals)
#Output:

['DOG', 'CAT', 'PARROT', 'RABBIT']
#Using lambda() Function with reduce()
#The reduce() function in Python takes in a function and a list as an argument. The function is called with a lambda function and an iterable and a new reduced result is returned. This performs a repetitive operation over the pairs of the iterable. The reduce() function belongs to the  functools module. 

#Example 1: Sum of all elements in a list using lambda and reduce() function

# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
 
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print(sum)
#Output:

193
#Here the results of the previous two elements are added to the next element and this goes on till the end of the list like (((((5+8)+10)+20)+50)+100).

#Example 2: Find the maximum element in a list using lambda and reduce() function

# python code to demonstrate working of reduce()
# with a lambda function
 
# importing functools for reduce()
import functools
 
# initializing list
lis = [1, 3, 5, 6, 2, ]
 
# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))
#Output:

#The maximum element of the list is : 6