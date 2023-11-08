#python program to find the sum of the  tuple elements.


#Sometimes, while programming, we have a problem in which
# we might need to perform summation among tuple elements.
# This is an essential utility as we come across summation 
# operations many times and tuples are immutable and hence 
# required to be dealt with. Let’s discuss certain ways in 
# which this task can be performed. 



#Method #1 : Using list() + sum() The above functions 
# can be combined to perform this task. We can employ 
# sum() to accumulate the result of summation logic. The 
# list() function is used to perform interconversions. 

def summation(test_tup):
  # converting into list
    test = list(test_tup)
 
    # initializing count
    count = 0
 
    # for loop
    for i in test:
        count += i
    return count
 
 
# initializing test_tup
test_tup = (5, 20, 3, 7, 6, 8)
print(summation(test_tup))





#Method #2: Using map() + sum() + list() The combination
# of above functions can be used to perform this task. In
# this, we first convert the tuple to list, flatten it’s 
# each list element using map(), perform summation of each
# using sum() and again employ sum() for overall summation 
# of the resultant list. 


# Python 3 code to demonstrate working of
# Tuple elements inversions
# Using map() + list() + sum()
 
# initializing tup
test_tup = ([7, 8], [9, 1], [10, 7])
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Tuple elements inversions
# Using map() + list() + sum()
res = sum(list(map(sum, list(test_tup))))
 
# printing result
print("The summation of tuple elements are : " + str(res))




#Method #3: Using for loop

# Python3 code to demonstrate working of
# Tuple summation
 
# initializing tup
test_tup = (7, 8, 9, 1, 10, 7)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
res = 0
for i in test_tup:
    res += i
 
# printing result
print("The summation of tuple elements are : " + str(res))