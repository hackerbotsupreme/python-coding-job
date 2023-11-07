#python progrAM TO FIND THe size of a dictionary

#Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key:value pair. Key value is provided in the dictionary to make it more optimized. The size of a Dictionary means the amount of memory (in bytes) occupied by a Dictionary object. In this article, we will learn various ways to get the size of a python Dictionary.

#1.Using getsizeof() function:

#The getsizeof() function belongs to the python’s sys module. It has been implemented in the below example.

#Example 1:
import sys

# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# print the sizes of sample Dictionaries
print("Size of dic1: " + str(sys.getsizeof(dic1)) + "bytes")
print("Size of dic2: " + str(sys.getsizeof(dic2)) + "bytes")
print("Size of dic3: " + str(sys.getsizeof(dic3)) + "bytes")

#Output:

#Size of dic1: 216bytes
#Size of dic2: 216bytes
#Size of dic3: 216bytes
#1.Using inbuilt __sizeof__() method:

#Python also has an inbuilt __sizeof__() method to determine the space allocation of an object without any additional garbage value. It has been implemented in the below example.


# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3}
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}

# print the sizes of sample Dictionaries
print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")
print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")



# sample Dictionaries
dic1 = {"A": 1, "B": 2, "C": 3} 
dic2 = {"Geek1": "Raju", "Geek2": "Nikhil", "Geek3": "Deepanshu"}
dic3 = {1: "Lion", 2: "Tiger", 3: "Fox", 4: "Wolf"}
  
# print the sizes of sample Dictionaries
print("Size of dic1: " + str(dic1.__sizeof__()) + "bytes")
print("Size of dic2: " + str(dic2.__sizeof__()) + "bytes")
print("Size of dic3: " + str(dic3.__sizeof__()) + "bytes")
#Output:

#Size of dic1: 216bytes
#Size of dic2: 216bytes
#Size of dic3: 216bytes






















