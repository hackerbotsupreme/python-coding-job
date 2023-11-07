#Find first non-repeating element in a given Array of integers

#Difficulty Level : Easy
#-------------------------------------------------------------------------------------

#Given an array of integers of size N, the task is to find the first non-repeating element in this array. 

#Examples:

#Input: {-1, 2, -1, 3, 0}
##Output: 2
#Explanation: The first number that does not repeat is : 2

#Input: {9, 4, 9, 6, 7, 4}
#Output: 6
#-------------------------------------------------------------------------

#Find first non-repeating element in a given Array of integers using Nested Loops:
#This approach is based on the following idea:

#Simple Solution is to use two loops. The outer loop picks elements one by one and the inner loop checks if the element is present more than once or not..

#Illustration:



#Given arr[] = {-1, 2, -1, 3, 0}

#For element at i = 0: 

#The value of element at index 2 is same, then this can’t be first non-repeating element
#For element at i = 1:

#After traversing the array arr[1] is not present is not present in the array except at 1.
#Hence, element is index 1 is the first non-repeating element which is 2

#Follow the steps below to solve the given problem: 

#Loop over the array from the left.
#Check for each element if its presence is present in the array for more than 1 time.
#Use a nested loop to check the presence.
#Below is the implementation of the above idea:

# Python3 program to find first
# non-repeating element.
 
 
def firstNonRepeating(arr, n):
 
    # Loop for checking each element
    for i in range(n):
        j = 0
        # Checking if ith element is present in array
        while(j < n):
            if (i != j and arr[i] == arr[j]):
                break
            j += 1
        # if ith element is not present in array
        # except at ith index then return element
        if (j == n):
            return arr[i]
 
    return -1
 
 
# Driver code
arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))
 
# This code is contributed by Anant Agarwal.
#Output
#6
#Time Complexity: O(n*n), Checking for each element n times
#Auxiliary Space: O(1)
#--------------------------------------------------
#Find first non-repeating element in a given Array of integers using Hashing:
#This approach is based on the following idea:

#The idea is to store the frequency of every element in the hashmap.
#Then check the first element whose frequency is 1 in the hashmap.
#This can be achieved using hashing
#Illustration:

#arr[] = {-1, 2, -1, 3, 0}

#Frequency map for arr:

#-1 -> 2
#2 -> 1
#3 -> 1
#0 -> 1
#Traverse arr[] from left:

#At i = 0:

#Frequency of arr[0] is 2, therefore it can’t be first non-repeating element
#At i = 1:

#Frequency of arr[1] is 1, therefore it will be the first non-repeating element.
#Hence, 2 is the first non-repeating element.

#Follow the steps below to solve the given problem: 

##Traverse array and insert elements and their counts in the hash table.
#Traverse array again and print the first element with a count equal to 1.
#Below is the implementation of the above idea:

# Efficient Python3 program to find first
# non-repeating element.
from collections import defaultdict
 
 
def firstNonRepeating(arr, n):
    mp = defaultdict(lambda: 0)
 
    # Insert all array elements in hash table
    for i in range(n):
        mp[arr[i]] += 1
 
    # Traverse array again and return
    # first element with count 1.
    for i in range(n):
        if mp[arr[i]] == 1:
            return arr[i]
    return -1
 
 
# Driver Code
arr = [9, 4, 9, 6, 7, 4]
n = len(arr)
print(firstNonRepeating(arr, n))
 
# This code is contributed by Shrikant13
#Output
#6
#Time Complexity: O(2n), Traverse over the array to map the frequency and again traverse over the array to check for frequency.
#Auxiliary Space: O(n), Create a hash table for storing frequency
#------------------------------------------------------------------------
