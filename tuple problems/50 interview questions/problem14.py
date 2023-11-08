#Python | Sort Tuples in Increasing Order by any key

#Difficulty Level : Hard

#Given a tuple, sort the list of tuples in increasing order by any key in tuple. Examples:#

#Input : tuple = [(2, 5), (1, 2), (4, 4), (2, 3)] 
#            m = 0
#Output : [(1, 2), (2, 3), (2, 5), (4, 4)]
#Explanation: Sorted using the 0th index key.

#Input :  [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
#         m = 2
#Output : Sorted: [(23, 45, 20), (89, 40, 23), (25, 44, 39)] 
#Explanation: Sorted using the 2nd index key
#Given tuples, we need to sort them according to any given key. This can be done using sorted() function where we sort them using key=last and store last as the key index according to which we have to sort the given tuples. Below is the Python implementation of the above approach: 

#Python
# Python code to sort a list of tuples
# according to given key.
 
# get the last key.
def last(n):
    return n[m] 
  
# function to sort the tuple  
def sort(tuples):
 
    # We pass used defined function last
    # as a parameter.
    return sorted(tuples, key = last)
  
# driver code 
a = [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
m = 2
print("Sorted:"),
print(sort(a))
#Output:

#Sorted: [(23, 45, 20), (89, 40, 23), (25, 44, 39)] 
#Another  approach  is  using the operator.itemgetter() function from the operator module. The itemgetter() function returns a callable object that can be used to retrieve an item from an object, such as a tuple.

#Here is an example of how to use itemgetter() to sort a list of tuples by any key:

#Python3
import operator
 
def sort_tuples(tuples, key):
    return sorted(tuples, key=operator.itemgetter(key))
 
tuples = [(2, 5), (1, 2), (4, 4), (2, 3)]
key = 0
print(sort_tuples(tuples, key))  # Output: [(1, 2), (2, 3), (2, 5), (4, 4)]
#Output
#[(1, 2), (2, 5), (2, 3), (4, 4)]
#This approach has the advantage of being concise and efficient, as it uses the built-in sorted() function and the itemgetter() function from the operator module. It is also easy to understand and implement.



#Note that the itemgetter() function returns a callable object that can be used to retrieve an item from an object, such as a tuple. To sort the tuples, we pass this callable object to the key argument of the `sorted

