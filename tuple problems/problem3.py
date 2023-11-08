#write a  python program for adding
# tuple to list and vice-vesa




#Sometimes, while working with Python containers,
# we can have a problem in which we need to perform 
# addition of one container with another. This kind of problem can have occurrence in many data domains across Computer Science and Programming. Let’s discuss certain ways in which this task can be performed.
#Method 1 : Using += operator [list + tuple] 
#This operator can be used to join a list with a tuple. 
# Internally its working is similar to that of list.extend(), which can have any iterable as its argument, tuple in this case.

# Python3 code to demonstrate working of
# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
 
# initializing list
test_list = [5, 6, 7]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing tuple
test_tup = (9, 10)
 
# Adding Tuple to List and vice - versa
# Using += operator (list + tuple)
test_list += test_tup
 
# printing result
print("The container after addition : " + str(test_list))




#Method #2 : Using tuple(), data type conversion [tuple + list] 
#he following technique is used to add list to a tuple. The tuple 
#has to converted to list and list has to be added, at last resultant 
# is converted to tuple.

# Python3 code to demonstrate working of
# Adding Tuple to List and vice - versa
# Using tuple(), data type conversion [tuple + list]
 
# initializing list
test_list = [5, 6, 7]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing tuple
test_tup = (9, 10)
 
# Adding Tuple to List and vice - versa
# Using tuple(), data type conversion [tuple + list]
res = tuple(list(test_tup) + test_list)
 
# printing result
print("The container after addition : " + str(res))





#Method #3: Using tuple(),list() and extend() methods

# Python3 code to demonstrate working of
# Adding Tuple to List and vice - versa
 
# initializing list and tuple
test_list = [5, 6, 7]
test_tup = (9,10)
 
# printing original list
print("The original list is : " + str(test_list))
 
# Adding Tuple to List
test_list.extend(list(test_tup))
# printing result
print("The container after addition : " + str(test_list))
 
#*********************************************************
 
# initializing list and tuple
test_list = [1,2,3,4]
test_tup=(5,6)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
#Adding list to tuple
test_tup=list(test_tup)
test_tup.extend(test_list)
test_tup=tuple(test_tup)
# printing result
print("The container after addition : " + str(test_tup))



 




