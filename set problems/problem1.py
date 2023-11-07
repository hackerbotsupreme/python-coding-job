# write a program to find the size if the set 


#using"getsizeof() function:
#well what is getsizeof() function ?In python, the usage of sys.getsizeof() can be done to find the storage size
# of a particular object that occupies some space in the memory. This function returns the size of the object
# in bytes. It takes at most two arguments i.e Object itself.
#imp-- interview  asked questions
#Difference between __sizeof__() and getsizeof() method – Python
#Memory management is of utmost priority when we write large chunks of code. So in addition to good coding knowledge, it is important to be able to write programs, so as to handle memory efficiently. 

#So let us look at the two ways of getting the size of a particular object in Python. These are getsizeof() method and __sizeof() method. 
#The getsizeof() is a system-specific method and hence we have to import the sys module to use it. A sample code is as shown below for calculating the size of a list.

#para above continues at the end....

#attemppt 1 
#using ----getsizeof()-----  function :

import sys
Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}
print("Size of Set1: " + str(sys.getsizeof(Set1)) + "bytes")
print("Size of Set2: " + str(sys.getsizeof(Set2)) + "bytes")
print("Size of Set3: " + str(sys.getsizeof(Set3)) + "bytes")



#USING---sizeof()------- function :

Set1 = {"A", 1, "B", 2, "C", 3}
Set2 = {"Geek1", "Raju", "Geek2", "Nikhil", "Geek3", "Deepanshu"}
Set3 = {(1, "Lion"), ( 2, "Tiger"), (3, "Fox")}

print("Size of Set1: " + str(Set1.__sizeof__()) + "bytes")
print("Size of Set2: " + str(Set2.__sizeof__()) + "bytes")
print("Size of Set3: " + str(Set3.__sezeof__()) + "bytes")

#__sizeof__()--syntax
#Set1.__sizeof__())--set.__size of__()
#getsizeof()---syntax
#sys.getsizeof(Set1)---getsizeif(set)