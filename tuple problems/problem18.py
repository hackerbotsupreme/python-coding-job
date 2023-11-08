#python  program removing duplicate tuples

#Many times, while working with Python tuples, we can have a problem removing duplicates. This is a very common problem and can occur in any form of programming setup, be it regular programming or web development. Let’s discuss certain ways in which this task can be performed. 

#Method #1 : Using set() + tuple() This is the most straight forward way to remove duplicates. In this, we convert the tuple to a set, removing duplicates and then converting it back again using tuple(). 


# Python3 code to demonstrate working of
# Removing duplicates from tuple
# using tuple() + set()
 
# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Removing duplicates from tuple
# using tuple() + set()
res = tuple(set(test_tup))
 
# printing result
print("The tuple after removing duplicates : " + str(res))


#Method #2 : Using OrderedDict() + fromkeys() 

#The combination of the above functions can also be used to perform this particular task. In this, we convert the tuples to dictionaries removing duplicates and then accessing its keys. 


# Python3 code to demonstrate working of
# Removing duplicates from tuple
# using OrderedDict() + fromkeys()
from collections import OrderedDict
 
# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Removing duplicates from tuple
# using OrderedDict() + fromkeys()
res = tuple(OrderedDict.fromkeys(test_tup).keys())
 
# printing result
print("The tuple after removing duplicates : " + str(res))



#Method #3: Using in, not in operators and tuple() 

# Python3 code to demonstrate working of
# Removing duplicates from tuple
 
# initialize tuple
test_tup = (1, 3, 5, 2, 3, 5, 1, 1, 3)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Removing duplicates from tuple
x=[]
for i in test_tup:
    if i not in x:
        x.append(i)
res=tuple(x)
 
# printing result
print("The tuple after removing duplicates : " + str(res))
