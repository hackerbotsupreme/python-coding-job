#Python groupby method to remove all consecutive duplicates

#Difficulty Level : Basic

#Given a string S, remove all the consecutive duplicates. Examples:

#Input  : aaaaabbbbbb
#Output : ab

#Input : geeksforgeeks
#Output : geksforgeks

#Input : aabccba
#Output : abcba
#We have existing solution for this problem please refer Remove all consecutive duplicates from the string link. We can solve this problem in python quickly using itertools.groupby() method.

#How itertools.groupby(iterable,key[optional]) works in Python?
#Group by method takes two input one is iterable (list,tuple,dictionary) and second is key function which calculates keys for each element present in iterable. It returns key and iterable of grouped items. If key function not specified or is None, key defaults to an identity function and returns the element unchanged. For example, 

#Python3
#numbers = [1, 1, 1, 3, 3, 2, 2, 2, 1, 1]
#import itertools
#for (key,group) in itertools.groupby(numbers):
#    print (key,list(group))
#Output

1 [1, 1, 1]
3 [3, 3]
2 [2, 2, 2]
1 [1, 1]
#Python3
# function to remove all consecutive duplicates
# from the string in Python
 
from itertools import groupby
def removeAllConsecutive(input):
     
    # group all consecutive characters based on their
    # order in string and we are only concerned
    # about first character of each consecutive substring
    # in given string, so key value will work for us
    # and we will join these keys without space to
    # generate resultant string
    result = []
    for (key,group) in groupby(input):
        result.append(key)
 
    print (''.join(result))
     
# Driver program
if __name__ == "__main__":
    input = 'aaaaabbbbbb'
    removeAllConsecutive(input)
#Output
#ab
#Time complexity : O(n) 
#Auxiliary Space : O(n)





