# python program to  find element frequency in tuple.


#Input : test_tup = (4, 5, 4, 5, 6, 6, 5) 
#Output : {4: 2, 5: 3, 6: 2} 
#Explanation : Frequency of 4 is 2 and so on..
#Input : test_tup = (4, 5, 4, 5, 6, 6, 6) 
#Output : {4: 2, 5: 2, 6: 3} 
#Explanation : Frequency of 4 is 2 and so on.. 



#Method #1  Using defaultdict()

#In this, we perform task of getting all elements and 
# assigning frequency using defaultdict which maps each
# element with key and then frequency can be incremented.

# Python3 code to demonstrate working of
# Elements frequency in Tuple
# Using defaultdict()
from collections import defaultdict
 
# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
res = defaultdict(int)
for ele in test_tup:
     
    # incrementing frequency
    res[ele] += 1
 
# printing result
print("Tuple elements frequency is : " + str(dict(res)))



#Method #2 : Using Counter()

#This is straight forward way to solve this problem. In this, we just employ this function and it returns frequency of elements in container, in this case tuple.

# Python3 code to demonstrate working of
# Elements frequency in Tuple
# Using Counter()
from collections import Counter
 
# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# converting result back from defaultdict to dict
res = dict(Counter(test_tup))
 
# printing result
print("Tuple elements frequency is : " + str(res))


Method #3 : Using count() method.

# Python3 code to demonstrate working of
# Elements frequency in Tuple
 
# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
res = dict()
x=list(test_tup)
y=[]
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    res[i]=x.count(i)
# printing result
print("Tuple elements frequency is : " + str(res))



Method #4 : Using operator.countOf() method.

# Python3 code to demonstrate working of
# Elements frequency in Tuple
import operator as op
# initializing tuple
test_tup = (4, 5, 4, 5, 6, 6, 5, 5, 4)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
res = dict()
x=list(test_tup)
y=[]
for i in x:
    if i not in y:
        y.append(i)
for i in y:
    res[i]=op.countOf(x,i)
# printing result
print("Tuple elements frequency is : " + str(res))

 