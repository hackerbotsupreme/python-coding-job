#Python | Reversing a Tuple

#Difficulty Level : Easy
#As we know that in Python, tuples are immutable, thus it cannot be changed or altered. This provides us with limited ways of reversing a tuple, unlike a list. We will go through few techniques on how a tuple in python can be reversed. Examples:

#Input : tuples = ('z','a','d','f','g','e','e','k')
#Output : ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')

#Input : tuples = (10, 11, 12, 13, 14, 15)
#Output : (15, 14, 13, 12, 11, 10)

#Method 1: Using the slicing technique. In this technique, a copy of the tuple is made and the tuple is not sorted in-place. Since tuples are immutable, there is no way to reverse a tuple in-place. Creating a copy requires more space to hold all of the existing elements. Therefore, this exhausts memory. 

#Python3
# Reversing a tuple using slicing technique
# New tuple is created
def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
     
# Driver Code
tuples = ('z','a','d','f','g','e','e','k')
print(Reverse(tuples))
#Output:

#('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
#Method 2: Using the reversed() built-in function. In this method, we do not make any copy of the tuple. Instead, we get a reverse iterator which we use to cycle through the tuple, similar to the list. 


#Python
# Reversing a list using reversed()
def Reverse(tuples):
    new_tup = ()
    for k in reversed(tuples):
        new_tup = new_tup + (k,)
    print new_tup
 
# Driver Code
tuples = (10, 11, 12, 13, 14, 15)
Reverse(tuples)
Output:

(15, 14, 13, 12, 11, 10)
Method3: Iteration

#One alternative approach you could use is to create a new empty tuple and then iterate through the original tuple in reverse order, adding each element to the new tuple. This approach requires creating a new tuple and adding each element one by one, so it may be less efficient than the other methods.

#Here is an example of how you could use this approach to reverse a tuple:

#Python3
def reverse_tuple(t):
    new_tuple = ()
    for i in range(len(t)-1, -1, -1):
        new_tuple += (t[i],)
    return new_tuple
 
tuples = ('z','a','d','f','g','e','e','k')
print(reverse_tuple(tuples))
# Output: ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
Output
('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
#Method4: Using Recursion

#Python3
# recursive function
def reverse_tuple(t):
  #condition checking
    if len(t) == 0:
        return t
    else:
        return(t[-1],)+reverse_tuple(t[:-1])
original_tuple = ('z','a','d','f','g','e','e','k')
# function call
reversed_tuple = reverse_tuple(original_tuple)
print("Original Tuple: ", original_tuple)
print("Reversed Tuple: ", reversed_tuple)
Output
#Original Tuple:  ('z', 'a', 'd', 'f', 'g', 'e', 'e', 'k')
#Reversed Tuple:  ('k', 'e', 'e', 'g', 'f', 'd', 'a', 'z')
#Time complexity : O(n)

#Auxiliary space : O(n)