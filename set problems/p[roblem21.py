#python program intersection of a two sets 
 
 
 
 
 
# Python set intersection() method returns a new set with an element that is common to all set

#The intersection of two given sets is the largest set, which contains all the elements that are common to both sets. The intersection of two given sets A and B is a set which consists of all the elements which are common to both A and B.



#Python Set intersection() Method Syntax:
#Syntax: set1.intersection(set2, set3, set4….) 
#Parameters:

#any number of sets can  be passed
#Return: Returns a set which has the intersection of all sets(set1, set2, set3…) with set1. It returns a copy of set1 only if no parameter is passed. 



#Python Set intersection() Method Example:
s1 = {1, 2, 3}
s2 = {2, 3}
print(s1.intersection(s2))




#Example 1: Working of set intersection()
# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}
 
# intersection of two sets
print("set1 intersection set2 : ",
      set1.intersection(set2))
 
# intersection of three sets
print("set1 intersection set2 intersection set3 :",
      set1.intersection(set2, set3))



#Example 2: Python set intersection operator(&)
#We can also get intersections using ‘&’ operator.

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {1, 0, 12}
 
print(set1 & set2)
print(set1 & set3)
 
print(set1 & set2 & set3)


#Example 3: Python set intersection opposite
#symmetric_difference() is an opposite to the Python Set intersection() method.

# Python3 program for intersection() function
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {1, 0, 12}
 
print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set3))
print(set2.symmetric_difference(set3))





#Example 4: Python set intersection empty
#Intersection of empty sets returns an empty set.

set1 = {}
set2 = {}
 
# union of two sets
print("set1 intersection set2 : ",
      set(set1).intersection(set(set2)))




