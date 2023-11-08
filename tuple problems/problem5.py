# write python prom formodulo of tuple elements


#Sometimes, while working with records, we can have a problem in 
# which we may need to perform modulo of tuples. This 
# problem can occur in day-day programming. Let’s discuss 
# certain ways in which this task can be performed. 

#Method #1 : Using zip() + generator expression The combination 
# of above functions can be used to perform this task. In this,
# we perform the task of modulo using generator expression and 
# mapping index of each tuple is done by zip(). 

# Python3 code to demonstrate working of
# Tuple modulo
# using zip() + generator expression
 
# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)
 
# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
 
# Tuple modulo
# using zip() + generator expression
res = tuple(ele1 % ele2 for ele1, ele2 in zip(test_tup1, test_tup2))
 
# printing result
print("The modulus tuple : " + str(res))



#Method #2 : Using map() + mod The combination of above 
# functionalities can also perform this task. In this, we
# perform the task of extending logic of modulus using mod
# and mapping is done by map(). 

# Python3 code to demonstrate working of
# Tuple modulo
# using map() + mod
from operator import mod
 
# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)
 
# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
 
# Tuple modulo
# using map() + mod
res = tuple(map(mod, test_tup1, test_tup2))
 
# printing result
print("The modulus tuple : " + str(res))




#Method #3 : Using for loop 

# Python3 code to demonstrate working of
# Tuple modulo
 
# initialize tuples
test_tup1 = (10, 4, 5, 6)
test_tup2 = (5, 6, 7, 5)
 
# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))
 
# Tuple modulo
res=[]
for i in range(0,len(test_tup1)):
    res.append(test_tup1[i]%test_tup2[i])
res=tuple(res)
# printing result
print("The modulus tuple : " + str(res))



