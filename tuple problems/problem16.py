#python program to test if the tuple is distinct.


#Sometimes, while working with records, we have a problem in which we need to find if all elements of tuple are different. This can have applications in many domains including web development. Let’s discuss certain ways in which this task can be performed. 
#Method #1 : Using loop This is a brute force way in which this task can be performed. In this, we just iterate through all tuple elements and put it in set if it’s the first occurrence. During the subsequence occurrence we check in set, if it exists, we return False. 

# Python3 code to demonstrate working of
# Test if tuple is distinct
# Using loop
 
# initialize tuple
test_tup = (1, 4, 5, 6, 1, 4)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Test if tuple is distinct
# Using loop
res = True
temp = set()
for ele in test_tup:
    if ele in temp:
        res = False
        break
    temp.add(ele)
 
# printing result
print("Is tuple distinct ? : " + str(res))


 #Method #2 : Using set() + len() In this method, we convert the tuple into a set using set(), and then check it with original tuple length, if matches, means that it was a distinct tuple and returns True. 

# Python3 code to demonstrate working of
# Test if tuple is distinct
# Using set() + len()
 
# initialize tuple
test_tup = (1, 4, 5, 6)
 
# printing original tuple
print("The original tuple is : " + str(test_tup))
 
# Test if tuple is distinct
# Using set() + len()
res = len(set(test_tup)) == len(test_tup)
 
# printing result
print("Is tuple distinct ? : " + str(res))






#Method #3: Using collections.Counter()
#This method uses collections.Counter() to return a dictionary of elements and their respective counts. If the maximum count of any element is 1, the tuple is distinct.

# Python3 code to demonstrate working of
# Test if tuple is distinct
# Using collections.Counter()
 
# importing collections for Counter
import collections
   
# initialize tuple
test_tup = (1, 4, 5, 6, 1, 4)
   
# printing original tuple
print("The original tuple is : " + str(test_tup))
   
# Test if tuple is distinct
# Using collections.Counter()
res = max(collections.Counter(test_tup).values()) == 1
   
# printing result
print("Is tuple distinct ? : " + str(res))
#This code is contributed by Edula Vinay Kumar Reddy


