#Python | Count the elements in a list until an element is a Tuple

#Difficulty Level : Medium

#In this problem, we need to accept a list. The list can have nested tuples. We need to count the elements in a list until a tuple has been encountered. Examples:

#Input : [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
#Output : 4

#Input : [4, (5, 6), 10, (1, 2, 3), 11, 2, 4]
#Output : 1
#Method #1:

#In this program we will use the concept of isinstance() to verify whether we are encountering a tuple or not in our path of count. For detailed guide on isinstance() visit isinstance in Python. 

#Python3
# Python program to count the items
# until a list is encountered
def Count(li):
    counter = 0
    for num in li:
        if isinstance(num, tuple):
            break
        counter = counter + 1
    return counter
 
# Driver Code
li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print(Count(li))
#Output:

4
#Method #2: Using type() method

#Python3
# Python program to count the items
# until a list is encountered
def Count(li):
    counter = 0
    for num in li:
        if type(num) is tuple:
            break
        counter = counter + 1
    return counter
 
# Driver Code
li = [4, 5, 6, 10, (1, 2, 3), 11, 2, 4]
print(Count(li))
#Output
4


