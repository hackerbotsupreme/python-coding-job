#Tuple is a collection of Python objects much like a list. The sequence of values stored in a tuple can be of any type, and they are indexed by integers.
#Values of a tuple are syntactically separated by ‘commas’. Although it is not necessary, it is more common to define a tuple by closing the sequence of values in parentheses.
#The size of a Tuple means the amount of memory (in bytes) taken by a Tuple object. In this article, we will learn various ways to get the size of a python Tuple.





#Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a list in terms of indexing, nested objects, and repetition but a tuple is immutable, unlike lists which are mutable.

#Creating Python Tuples
#To create a tuple we will use () operators.

var = ("Geeks", "for", "Geeks")
print(var)
#Output:

#('Geeks', 'for', 'Geeks')
#A new way of creating Python Tuples in Python 3.11 –
values : tuple[int | str, ...] = (1,2,4,"Geek")
 
print(values)
#Output – 

(1, 2, 4, 'Geek')
#Here, in the above snipper we are considering a variable called values which holds a tuple which consists of either int or str , the ‘…’ means that the tuple will hold more than one int or str

#Note: In case your generating a tuple with a single element, make sure to add a comma after the element. 

#Accessing Values in Python Tuples
#Method 1: Using Positive Index
#Using square brackets we can get the values from tuples in Python.

var = ("Geeks", "for", "Geeks")
 
print("Value in Var[0] = ", var[0])
print("Value in Var[1] = ", var[1])
print("Value in Var[2] = ", var[2])
#Output:

#Value in Var[0] =  Geeks
#Value in Var[1] =  for
#Value in Var[2] =  Geeks
#Method 2: Using Negative Index.
#In the above methods, we use the positive index to access the value in Python, and here we will use -ve index within [].

var = ("Geeks", "for", "Geeks")
 
print("Value in Var[-3] = ", var[-3])
print("Value in Var[-2] = ", var[-2])
print("Value in Var[-1] = ", var[-1])
#Output:


#Value in Var[-3] =  Geeks
#Value in Var[-2] =  for
#Value in Var[-1] =  Geeks
#Concatenation of Python Tuples
#To concatenate the Python tuple we will use plus operators(+).

# Code for concatenating 2 tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
 
# Concatenating above two
print(tuple1 + tuple2)
#Output:

(0, 1, 2, 3, 'python', 'geek')
 #Nesting of Python Tuples
# Code for creating nested tuples
 
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'geek')
tuple3 = (tuple1, tuple2)
print(tuple3)
#Output :

((0, 1, 2, 3), ('python', 'geek'))
#Repetition Python Tuples
# Code to create a tuple with repetition
 
tuple3 = ('python',)*3
print(tuple3)
#Output:

 #('python', 'python', 'python')
#Try the above without a comma and check. You will get tuple3 as a string ‘pythonpythonpython’. 

#Immutable Python Tuples
# code to test that tuples are immutable
 
tuple1 = (0, 1, 2, 3)
tuple1[0] = 4
print(tuple1)
#Output:

#Traceback (most recent call last):
# File "e0eaddff843a8695575daec34506f126.py", line 3, in
 #   tuple1[0]=4
#TypeError: 'tuple' object does not support item assignment
 #Slicing Python Tuples
# code to test slicing
 
tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
#Output:

(1, 2, 3)
(3, 2, 1, 0)
(2, 3)
 #Deleting a Tuple
# Code for deleting a tuple
 
tuple3 = ( 0, 1)
del tuple3
print(tuple3)
#Error:

#Traceback (most recent call last):
# File "d92694727db1dc9118a5250bf04dafbd.py", line 6, in <module>
 #   print(tuple3)
#NameError: name 'tuple3' is not defined
#Output:

(0, 1)
 #Finding Length of a Tuple
# Code for printing the length of a tuple
 
tuple2 = ('python', 'geek')
print(len(tuple2))
#Output:

 #2
 #Converting list to a Tuple
# Code for converting a list and a string into a tuple
 
list1 = [0, 1, 2]
print(tuple(list1))
print(tuple('python')) # string 'python'
#Output:

(0, 1, 2)
('p', 'y', 't', 'h', 'o', 'n')
#Takes a single parameter which may be a list, string, set or even a dictionary( only keys are taken as elements) and converts them to a tuple.

 #Tuples in a loop
# python code for creating tuples in a loop
 
tup = ('geek',)
n = 5  # Number of time loop runs
for i in range(int(n)):
    tup = (tup,)
    print(tup)