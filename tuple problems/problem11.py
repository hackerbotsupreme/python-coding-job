#write python program to sort a list of tuples by second item.

#Given a list of tuples, write a Python program to sort the tuples by the second item of each tuple.

#Examples:

#Input : [('for', 24), ('Geeks', 8), ('Geeks', 30)] 
#Output : [('Geeks', 8), ('for', 24), ('Geeks', 30)]

#Input : [('452', 10), ('256', 5), ('100', 20), ('135', 15)]
#Output : [('256', 5), ('452', 10), ('135', 15), ('100', 20)]







#Method #1: Using the Bubble Sort Using the technique
# of Bubble Sort to we can perform the sorting. Note that 
# each tuple is an element in the given list. Access the 
# second element of each tuple using the nested loops. 
# This performs the in-place method of sorting. The time
# complexity is similar to the Bubble Sort i.e. O(n^2). 
# Python program to sort a list of tuples by the second Item
 
# Function to sort the list of tuples by its second item
 
 
def Sort_Tuple(tup):
 
    # getting length of list of tuples
    lst = len(tup)
    for i in range(0, lst):
 
        for j in range(0, lst-i-1):
            if (tup[j][1] > tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup
 
 
# Driver Code
tup = [('for', 24), ('is', 10), ('Geeks', 28),
       ('Geeksforgeeks', 5), ('portal', 20), ('a', 15)]
 
print(Sort_Tuple(tup))

#Method #2: Using sort() method While sorting via this method the actual content of the tuple is changed, and just like the previous method, the in-place method of the sort is performed. 

# Python program to sort a list of
# tuples by the second Item using sort()
 
# Function to sort the list by second item of tuple
def Sort_Tuple(tup):
 
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    tup.sort(key = lambda x: x[1])
    return tup
 
# Driver Code
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
 
# printing the sorted list of tuples
print(Sort_Tuple(tup))







#Method #3: Using sorted() method Sorted() method sorts a 
# list and always returns a list with the elements in a 
# sorted manner, without modifying the original sequence. 
# It takes three parameters from which two are optional, 
# here we tried to use all of the three: Iterable : 
# sequence (list, tuple, string) or collection (dictionary,
# set, frozenset) or any other iterator that needs to be 
# sorted. Key(optional) : A function that would serve as a key or a basis of sort comparison. Reverse(optional) : To sort this in ascending order we could have just ignored the third parameter, which we did in this program. If set true, then the iterable would be sorted in reverse (descending) order, by default it is set as false. 

# Python program to sort a list of
# tuples by the second Item using sorted()
 
# Function to sort the list by second item of tuple
def Sort_Tuple(tup):
 
    # reverse = None (Sorts in Ascending order)
    # key is set to sort using second element of
    # sublist lambda has been used
    return(sorted(tup, key = lambda x: x[1])) 
 
# Driver Code
tup = [('rishav', 10), ('akash', 5), ('ram', 20), ('gaurav', 15)]
 
# printing the sorted list of tuples
print(Sort_Tuple(tup))



#Method 4: Using the itemgetter function from the operator module

#The itemgetter function is a function from the operator 
# module that allows you to specify which element in a 
# tuple you want to sort by. In the example above, the
# itemgetter(1) function tells the sorted function to sort
# the tuples by the second element in each tuple (since indices start at 0, the second element has index 1).

#Here is an example of how you can use itemgetter to sort a list of tuples by the first element instead:


from operator import itemgetter
 
def sort_tuples(tuples):
    # Sort the tuples by the second item using the itemgetter function
    return sorted(tuples, key=itemgetter(1))
 
# Test the function
tuples = [('for', 24), ('Geeks', 8), ('Geeks', 30)]
print(sort_tuples(tuples))
#This code is contributed by Edula Vinay Kumar Reddy





