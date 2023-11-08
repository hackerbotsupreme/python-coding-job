#python program to create a list of tuple  from giveb list having number and its cube in each tuple


#Given a list of numbers of list, write a Python program to create a list of tuples having first element as the number and second element as the cube of the number. Example:

#Input: list = [1, 2, 3]
#Output: [(1, 1), (2, 8), (3, 27)]

#Input: list = [9, 5, 6]
#Output: [(9, 729), (5, 125), (6, 216)]


#Method #1 : Using pow() function.We can use list
# comprehension to create a list of tuples. The first 
# element will be simply an element and second element
# will be cube of that number. Below is the Python
# implementation: 



# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple
 
# creating a list
list1 = [1, 2, 5, 6]
 
# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]
 
# print the result
print(res)



#Method #2: Using ** operator 

# Python program to create a list of tuples
# from given list having number and
# its cube in each tuple
 
# creating a list
list1 = [1, 2, 5, 6]
 
# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, val**3) for val in list1]
 
# print the result
print(res)


#Method #3: Using map() and lambda function

#We can also use the map() function along with a lambda function to create a list of tuples. The lambda function will take an element from the list as input and return a tuple containing the element and its cube as output. The map() function will apply this lambda function to all elements in the list and return a list of tuples.

#Here is the Python implementation of this approach:

list1 = [1, 2, 5, 6]
res = list(map(lambda x: (x, x**3), list1))
print(res)
#This code is contributed by Edula Vinay Kumar Reddy











