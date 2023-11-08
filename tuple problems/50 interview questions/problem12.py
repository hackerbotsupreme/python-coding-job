#Python | Count occurrences of an element in a Tuple

#Difficulty Level : Medium

#In this program, we need to accept a tuple and then find the number of times an item is present in the tuple. This can be done in various ways, but in this article, we will see how this can be done using a simple approach and how inbuilt functions can be used to solve this problem. 

#Examples:

#Tuple: (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
#Input : 4
#Output : 0 times

#Input : 10
#Output : 3 times

Input : 8
#Output : 4 times
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Method 1(Simple Approach): 

#We keep a counter that keeps on increasing if the required element is found in the tuple. 

#Python3
# Program to count the number of times an element
# Present in the list
 
 
def countX(tup, x):
    count = 0
    for ele in tup:
        if (ele == x):
            count = count + 1
    return count
 
 
# Driver Code
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
 
print(countX(tup, enq))
print(countX(tup, enq1))
print(countX(tup, enq2))
#Output
0
3
4
#Method 2(Using count()): 

#The idea is to use method count() to count number of occurrences. 

#Python3
# Program to count the number of times an element
# Present in the list
# Count function is used
 
 
def Count(tup, en):
    return tup.count(en)
 
 
# Driver Code
tup = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
enq = 4
enq1 = 10
enq2 = 8
print(Count(tup, enq), "times")
print(Count(tup, enq1), "times")
print(Count(tup, enq2), "times")
#Output
#0 times
#3 times
#4 times
#Method 3: Using list comprehension

#Python3
tuple1 = (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
x = [i for i in tuple1 if i == 10]
print("the element 10 occurs", len(x), "times")
#Output
#the element 10 occurs 3 times
#Method #4: Using enumerate function

#Python3
#tuple1=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
#x=[i for a,i in enumerate(tuple1) if i==10]
print("the element 10 occurs",len(x),"times")
#Output
#the element 10 occurs 3 times
#Method #5: Using lambda function

#Python3
tuple1=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
x=list(filter(lambda i: (i==10),tuple1))
print("the element 10 occurs",len(x),"times")
#Output
#the element 10 occurs 3 times
#Method #6: Using counter function

#Python3
from collections import Counter
tuple1=("10", "8", "5", "2", "10", "15", "10", "8", "5", "8", "8", "2")
x=Counter(tuple1)
print("the element 10 occurs",x["10"],"times")
#Output
#the element 10 occurs 3 times
#Method#7: Using Countof function

#Python3
tuple1=("10", "8", "5", "2", "10", "15", "10", "8", "5", "8", "8", "2")
 
import operator as op
 
print(op.countOf(tuple1,"10"))
#Output
#3
