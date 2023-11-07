#python program to sort objects of user defined class in python



#The following article discusses how objects of a user-defined class can be arranged based on any of the variables of the class, which obviously will hold some value for every object. So far, we are aware of how we can sort elements of a list, the concept here is more or less the same as, except it is a step forward or we can say it is an advanced version of sorting elements but instead of a list we are dealing with objects of a class. 

#Here sorted() method will be used. 

#Syntax:

#sorted (iterable, key(optional), reverse(optional) )

print(sorted([1,26,3,9]))

print(sorted("Geeks foR gEEks".split(), key=str.lower))

#[1, 3, 9, 26]
#['foR', 'Geeks', 'gEEks']
#Sorting objects of User Defined Class
#Method 1:

#In order to sort objects of a user-defined class, a key needs to be set for the sorted method, such that the key will be an indicator of how the objects should be sorted. With reference to the examples given below, here a function has been provided to the key which one by one compares the specified variable value for each object and returns a sorted list of objects for a class.

#Example 1: Sorting elements in ascending order of the integer value given to them

class GFG:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return str((self.a, self.b))


# list of objects
gfg = [GFG("geeks", 1),
	GFG("computer", 3),
	GFG("for", 2),
	GFG("geeks", 4),
	GFG("science", 3)]

# sorting objects on the basis of value
# stored at variable b
print(sorted(gfg, key=lambda x: x.b))



#Output:

#[(‘geeks’, 1), (‘for’, 2), (‘computer’, 3), (‘science’, 3), (‘geeks’, 4)]

#Example 2: Sorting objects on the basis of the string value a variable holds

class GFG:
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __repr__(self):
		return str((self.a, self.b))


# list of objects
gfg = [GFG("geeks", 1),
	GFG("computer", 3),
	GFG("for", 2),
	GFG("geeks", 4),
	GFG("science", 3)]

# sorting objects on the basis of value
# stored at variable a
print(sorted(gfg, key=lambda x: x.a.lower()))




#Output:

#[(‘computer’, 3), (‘for’, 2), (‘geeks’, 1), (‘geeks’, 4), (‘science’, 3)]

#Method 2:

#This method depicts how objects of a user-defined class can be sorted using functools inbuilt method total_ordering as a decorator to the class. Here, the class is defined normally as done in the above examples, only difference being during sorting, total_ordering() decorator is used. Two requirements for using total_ordering() are-

#Out of less than(__lt__), greater than(__gt__), less than equal to(__le__) and greater than equal to(__ge__), atleast one should be defined in the class being decorated using this method.
#Equal to (__eq__) should be defined.
#In the example given below less than and greater than, both are defined even though during processing only one is called(in this less than) since one is enough to decide the order of the elements but it is good programming practice to define all in case one thing fails. During sorting one of the comparison methods are called to compare objects on the basis of some element and the sorted result is returned.

#Example:
import functools
from functools import total_ordering


@total_ordering
class GFG:
	print("inside class")

	def __init__(self, a, b):
		self.a = a
		self.b = b

	def __lt__(self, obj):
		return ((self.b) < (obj.b))

	def __gt__(self, obj):
		return ((self.b) > (obj.b))

	def __le__(self, obj):
		return ((self.b) <= (obj.b))

	def __ge__(self, obj):
		return ((self.b) >= (obj.b))

	def __eq__(self, obj):
		return (self.b == obj.b)

	def __repr__(self):
		return str((self.a, self.b))


# list of objects
gfg = [GFG("geeks", 1),
	GFG("computer", 3),
	GFG("for", 2),
	GFG("geeks", 4),
	GFG("science", 3)]

# before sorting
print(gfg)

# sorting objects on the basis of value
# stored at variable b
# after sorting
print(sorted(gfg))




