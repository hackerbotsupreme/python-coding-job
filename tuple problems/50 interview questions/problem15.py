#Namedtuple in Python

#ifficulty Level : Easy
#Python supports a type of container dictionaries called “namedtuple()” present in the module, “collections“. Like dictionaries, they contain keys that are hashed to a particular value. But on contrary, it supports both access from key-value and iteration, the functionality that dictionaries lack.

#Example: 

#Python3
# Python code to demonstrate namedtuple()
 
from collections import namedtuple
 
# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(S[1])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
#Output:

#The Student age using index is : 19
#The Student name using keyname is : Nandini
#Let’s see various Operations on namedtuple() 
#Access Operations
#Access by index: The attribute values of namedtuple() are ordered and can be accessed using the index number unlike dictionaries which are not accessible by index.
#Access by keyname: Access by keyname is also allowed as in dictionaries.
#using getattr(): This is yet another way to access the value by giving namedtuple and key value as its argument.
#Python3
# Python code to demonstrate namedtuple() and
# Access by name, index and getattr()
 
# importing "collections" for namedtuple()
import collections
 
# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# Access using index
print("The Student age using index is : ", end="")
print(S[1])
 
# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)
 
# Access using getattr()
print("The Student DOB using getattr() is : ", end="")
print(getattr(S, 'DOB'))
#Output : 


#The Student age using index is : 19
#The Student name using keyname is : Nandini
#The Student DOB using getattr() is : 2541997
#Conversion Operations
#_make() :- This function is used to return a namedtuple() from the iterable passed as argument.
#_asdict() :- This function returns the OrderedDict() as constructed from the mapped values of namedtuple().
#using “**” (double star) operator :- This function is used to convert a dictionary into the namedtuple().
#Python3
# Python code to demonstrate namedtuple() and
# _make(), _asdict() and "**" operator
 
# importing "collections" for namedtuple()
import collections
 
# Declaring namedtuple()
Student = collections.namedtuple('Student',
                                 ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# initializing iterable
li = ['Manjeet', '19', '411997']
 
# initializing dict
di = {'name': "Nikhil", 'age': 19, 'DOB': '1391997'}
 
# using _make() to return namedtuple()
print("The namedtuple instance using iterable is  : ")
print(Student._make(li))
 
# using _asdict() to return an OrderedDict()
print("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())
 
# using ** operator to return namedtuple from dictionary
print("The namedtuple instance from dict is  : ")
print(Student(**di))
#Output : 

#The namedtuple instance using iterable is  : 
#Student(name='Manjeet', age='19', DOB='411997')
#The OrderedDict instance using namedtuple is  : 
#OrderedDict([('name', 'Nandini'), ('age', '19'), ('DOB', '2541997')])
#The namedtuple instance from dict is  : 
#Student(name='Nikhil', age=19, DOB='1391997')
#Additional Operation 
#_fields: This function is used to return all the keynames of the namespace declared.
#_replace(): _replace() is like str.replace() but targets named fields( does not modify the original values)
#Python3
# Python code to demonstrate namedtuple() and
# _fields and _replace()
 
# importing "collections" for namedtuple()
import collections
 
# Declaring namedtuple()
Student = collections.namedtuple('Student', ['name', 'age', 'DOB'])
 
# Adding values
S = Student('Nandini', '19', '2541997')
 
# using _fields to display all the keynames of namedtuple()
print("All the fields of students are : ")
print(S._fields)
 
# ._replace returns a new namedtuple, it does not modify the original
print("returns a new namedtuple : ")
print(S._replace(name='Manjeet'))
# original namedtuple
print(S)
#Output
#All the fields of students are : 
#('name', 'age', 'DOB')
#returns a new namedtuple : 
#Student(name='Manjeet', age='19', DOB='2541997')
#Student(name='Nandini', age='19', DOB='2541997')
#This article is contributed by Manjeet Singh. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.



#Please write comments if you find anything incorrect, or if you want to share more information about the topic discussed above. 


