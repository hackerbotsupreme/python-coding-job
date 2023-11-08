#Python | Convert a list of characters into a string

#Difficulty Level : Easy

#Given a list of characters, merge all of them into a string. Examples:

#Input : ['g', 'e', 'e', 'k', 's', 'f', 'o', 
#             'r', 'g', 'e', 'e', 'k', 's']
#Output : geeksforgeeks 

#Input : ['p', 'r', 'o', 'g', 'r', 'a', 'm', 
#                        'm', 'i', 'n', 'g']
#Output : programming 
#Recommended Practice
Initialize an empty string at the beginning. Traverse in the list of characters, for every index add character to the initial string. After complete traversal, print the string which has been added with every character. 

Implementation:

Python
# Python program to convert a list
# of character
 
def convert(s):
 
    # initialization of string to ""
    new = ""
 
    # traverse in the string
    for x in s:
        new += x
 
    # return string
    return new
     
     
# driver code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
#print(convert(s))
#Output

#geeksforgeeks
#Time Complexity: O(n)
#Auxiliary Space: O(n)

#Method 2 : Using join() function

#By using join() function in python, all characters in the list can be joined. The syntax is:



#str = ""
#str1 = ( "geeks", "for", "geeks" )
#str.join(str1) 
#The list of characters can be joined easily by initializing str=”” so that there are no spaces in between. 

#Implementation:

#Python
# Python program to convert a list
# of character
 
def convert(s):
 
    # initialization of string to ""
    str1 = ""
 
    # using join function join the list s by
    # separating words by str1
    return(str1.join(s))
     
# driver code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))
#Output
#geeksforgeeks
#Time Complexity: O(n)
#Auxiliary Space: O(n)

#Method#3: Using reduce() function

#Reduce function is used to convert the iterables to reduce in a single cumulative value. 

#Implementation:

#Python3
# Python program to convert a list
# of character
import functools
 
def convert(s):
 
    # Using reduce to join the list s to string
    str1 = functools.reduce(lambda x,y : x+y, s)
 
    # Return string 1
    return str1
     
# driver code
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))
#Output
#geeksforgeeks
#Method: Using list comprehension 
#Python3
s=['g','e','e','k','s','f','o','r','g','e','e','k']
x="".join([str(i) for i in s])
print(x)
#Output
#geeksforgeek
#Method: Using enumerate function 

#Python3
s=['g','e','e','k','s','f','o','r','g','e','e','k']
x="".join([str(i) for a,i in enumerate(s)])
print(x)
#Output
#geeksforgeek
