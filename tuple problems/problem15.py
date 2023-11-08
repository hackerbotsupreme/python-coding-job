#python program to assign frequency to tuples.

#Given tuple list, assign frequency to each tuple in list.

#Input : test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (9, ), (2, 7)] 
#Output : [(6, 5, 8, 2), (2, 7, 2), (9, 1)] 
#Explanation : (2, 7) occurs 2 times, hence 2 is append in tuple.
#Input : test_list = [(2, 7), (2, 7), (6, 5, 8), (9, ), (2, 7)] 
#Output : [(6, 5, 8, 1), (2, 7, 3), (9, 1)] 
#Explanation : (2, 7) occurs 3 times, hence 3 is append in tuple. 


 
#Method #1 : Using Counter() + items() + * operator + list comprehension

#In this, we extract the frequency using Counter(), fetch frequency numbers using items(), * operator is used to unpack elements and list comprehension is used to assign this to all elements in tuple list.



# Python3 code to demonstrate working of
# Assign Frequency to Tuples
# Using Counter() + items() + * operator + list comprehension
from collections import Counter
 
# initializing list
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# one-liner to solve problem
# assign Frequency as last element of tuple
res = [(*key, val) for key, val in Counter(test_list).items()]
 
# printing results
print("Frequency Tuple list : " + str(res))




#Method #2 : Using most_common() + Counter() + * operator + list comprehension

#This is similar to the above method, just most_common() performs sort operation on list, which is not necessary.
# Python3 code to demonstrate working of
# Assign Frequency to Tuples
# Using most_common() + Counter() + * operator + list comprehension
from collections import Counter
 
# initializing list
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# most_common performs sort on arg. list
# assign Frequency as last element of tuple
res = [(*key, val) for key, val in Counter(test_list).most_common()]
 
# printing results
print("Frequency Tuple list : " + str(res))



Method #3 : Using count(),list(),tuple() methods

# Python3 code to demonstrate working of
# Assign Frequency to Tuples
 
# initializing list
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# one-liner to solve problem
# assign Frequency as last element of tuple
res=[]
for i in test_list:
    if i not in res:
        res.append(i)
res1=[]
for i in res:
    x=list(i)
    x.append(test_list.count(i))
    p=tuple(x)
    res1.append(p)
 
# printing results
print("Frequency Tuple list : " + str(res1))




Method #4 : Using operator.countOf(),list(),tuple() methods

# Python3 code to demonstrate working of
# Assign Frequency to Tuples
import operator as op
# initializing list
test_list = [(6, 5, 8), (2, 7), (6, 5, 8), (6, 5, 8), (9, ), (2, 7)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# one-liner to solve problem
# assign Frequency as last element of tuple
res=[]
for i in test_list:
    if i not in res:
        res.append(i)
res1=[]
for i in res:
    x=list(i)
    x.append(op.countOf(test_list,i))
    p=tuple(x)
    res1.append(p)
 
# printing results
print("Frequency Tuple list : " + str(res1))



