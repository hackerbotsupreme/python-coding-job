#python program to remove tuples of length k.


#Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 2
#Output : [(4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
#Explanation : (4, 5) of len = 2 is removed.

#Input : test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)], K = 3
#Output : [(4, 5), (4, ), (1, ), (3, 4, 6, 7)]
#Explanation : 3 length tuple is removed.


#Method #1 : Using list comprehension
#This is one of the ways in which this task can be 
# performed. In this, we iterate for all elements in loop 
# and perform the required task of removal of K length elements 
# using conditions.

 #Python3 code to demonstrate working of 
# Remove Tuples of Length K
# Using list comprehension
  
# initializing list
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
  
# printing original list
print("The original list : " + str(test_list))
  
# initializing K 
K = 1
  
# 1 liner to perform task
# filter just lengths other than K 
# len() used to compute length
res = [ele for ele in test_list if len(ele) != K]
  
# printing result 
print("Filtered list : " + str(res))


#Method #2 : Using filter() + lambda + len() 

#Yet another way to solve this problem. In this, we perform filtering
# using filter() and lambda function to extract just non K
# length elements using len().
# Python3 code to demonstrate working of 
# Remove Tuples of Length K
# Using filter() + lambda + len() 
  
# initializing list
test_list = [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
  
# printing original list
print("The original list : " + str(test_list))
  
# initializing K 
K = 1
  
# filter() filters non K length values and returns result
res = list(filter(lambda x : len(x) != K, test_list))
  
# printing result 
print("Filtered list : " + str(res))


