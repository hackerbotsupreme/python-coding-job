#Find the first repeating element in an array of integers

#Difficulty Level : Easy
#-----------------------------------------------------------------------
#Given an array of integers arr[], The task is to find the index of first repeating element in it i.e. the element that occurs more than once and whose index of the first occurrence is the smallest. 

#Examples: 

#Input: arr[] = {10, 5, 3, 4, 3, 5, 6}
#Output: 5 
#Explanation: 5 is the first element that repeats

#Input: arr[] = {6, 10, 5, 4, 9, 120, 4, 6, 10}
#Output: 6 
#Explanation: 6 is the first element that repeats


#Recommended Problem
#First Repeating Element
#Arrays
#Hash
#+1 more
#Amazon
#Oracle
#Solve Problem
#Submission count: 1.5L
#Naive Approach: Below is the idea to solve the problem

#Run two nested loops, the outer loop picks an element one by one, and the inner loop checks whether the element is repeated or not. Once a repeating element is found, break the loops and print the element.

#Time Complexity: O(N2)
#Auxiliary Space: O(1)
#--------------------------------------------------------------------
#Find the first repeating element in an array of integers using sorting:
#Below is the idea to solve the problem.

#Store the elements of arr[] in a duplicate array temp[], sort temp[] and traverse arr[] from 0 to N – 1, Simultaneously check the count of this element in temp[] and if the current element arr[i] has more than one occurrence then return arr[i].

#Follow the steps below to Implement the idea: 

#Copy the given array to an auxiliary array temp[] and sort temp array. 
##Traverse the input array arr[] from 0 to N – 1. 
#For every element, count its occurrences in temp[] using binary search.
#If the count of occurrence of current element is more than one, then return the current element.
#If no repeating element is found print “No Repeating Number Found”.
#Time complexity: O(NlogN).
#Auxiliary Space: O(N)

#Find the first repeating element in an array of integers using Hashset
#Below is the idea to solve the problem

#The idea is to traverse the given array arr[] from right to left and update the minimum index whenever, an already visited element has been found. To check if the element was already visited Hashset can be used. 

#Follow the steps below to implement the idea:

#Initialize an empty Hashset myset and a variable min with -1.  
#Run a for loop for each index of array arr[] from N – 1 to 0.
#If the current element is present in myset then update min with i.
#Else insert arr[i] in myset. 
#Return min.
#Below is the implementation of the above approach.

# Python3 program to find first repeating
# element in arr[]
  
# This function prints the first repeating
# element in arr[]
  
  
def printFirstRepeating(arr, n):
  
    # Initialize index of first repeating element
    Min = -1
  
    # Creates an empty hashset
    myset = dict()
  
    # Traverse the input array from right to left
    for i in range(n - 1, -1, -1):
  
        # If element is already in hash set,
        # update Min
        if arr[i] in myset.keys():
            Min = i
  
        else:  # Else add element to hash set
            myset[arr[i]] = 1
  
    # Print the result
    if (Min != -1):
        print("The first repeating element is",
              arr[Min])
    else:
        print("There are no repeating elements")
  
  
# Driver Code
arr = [10, 5, 3, 4, 3, 5, 6]
  
n = len(arr)
printFirstRepeating(arr, n)
  
# This code is contributed by Mohit kumar 29
#Output
#The first repeating element is 5
#Time Complexity: O(n).
#Auxiliary Space: O(n).
#-------------------------------------------------------------
#Find the first repeating element in an array of integers using Hashing 
#The idea is to use Hash array to store the occurrence of elements. Then traverse the array from left to right and return the first element with occurrence more than 1.

#Follow the below steps to implement the idea:

#Initialize variables k with 0, max with -1 and min with max + 1 and iterate over all values of arr[] to store the largest value in max.
#Initialize a Hash arrays a[] and b[] of size max + 1.
#Run a for loop from 0 to N – 1
#If a[arr[i]] is 0 put i+1 in place of a[arr[i]].
#Else assign 1 to b[arrr[i]] and k.
#If k is 0 print “No repeating element found”.
#Else iterate from 0 to max 
#If a[i] is not zero and b[i] is not zero and min is greater than a[i] then update min a[i].
#Print min.
#Below is the Implementation of above approach 

# Python3 program to find first
# repeating element in arr[]
  
# This function prints the
# first repeating element in arr[]
  
  
def printFirstRepeating(arr, n):
  
    # This will set k=1, if any
    # repeating element found
    k = 0
  
    # max = maximum from (all elements & n)
    max = n
  
    for i in range(n):
        if (max < arr[i]):
            max = arr[i]
  
    # Array a is for storing
    # 1st time occurrence of element
    # initialized by 0
    a = [0 for i in range(max + 1)]
  
    # Store 1 in array b
    # if element is duplicate
    # initialized by 0
    b = [0 for i in range(max + 1)]
  
    for i in range(n):
  
        # Duplicate element found
        if (a[arr[i]]):
            b[arr[i]] = 1
            k = 1
            continue
        else:
  
            # Storing 1st occurrence of arr[i]
            a[arr[i]] = i+1
  
    if (k == 0):
        print("No repeating element found")
    else:
        min = max + 1
  
        for i in range(max + 1):
  
            # Trace array a & find repeating
            # element with min index
            if (a[i] and (min > (a[i])) and b[i]):
                min = a[i]
  
        print(arr[min-1])
  
  
# Driver code
arr = [10, 5, 3, 4, 3, 5, 6]
N = len(arr)
  
printFirstRepeating(arr, N)
  
# This code is contributed by avanitrachhadiya2155
#Output
#5
#Time Complexity: O(N).
#Auxiliary Space: O(N).

