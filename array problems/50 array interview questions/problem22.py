#Find if there is a subarray with 0 sum

#Difficulty Level : Medium
#-----------------------------------------------------------------------

#Given an array of positive and negative numbers, find if there is a subarray (of size at least one) with 0 sum.

#Examples: 

#Input: {4, 2, -3, 1, 6}
#Output: true 
#Explanation:
#There is a subarray with zero sum from index 1 to 3.

#Input: {4, 2, 0, 1, 6}
#Output: true
#Explanation: The third element is zero. A single element is also a sub-array.

#Input: {-3, 2, 3, 1, 6}
#Output: false
#----------------------------------------------------------------------------------------------

#Naive approach:
#consider all subarrays one by one and check the sum of every subarray. Run two loops: the outer loop picks a starting point i and the inner loop tries all subarrays starting from i (See this for implementation).

#Time Complexity: O(N2)
#Auxiliary Space: O(1)



#Find if there is a subarray with 0 sum using hashing: 
#The idea is to iterate through the array and for every element arr[i], calculate the sum of elements from 0 to i (this can simply be done as sum += arr[i]). If the current sum has been seen before, then there is a zero-sum array. Hashing is used to store the sum values so that sum can be stored quickly and find out whether the current sum is seen before or not.

#Follow the given steps to solve the problem:

#Declare a variable sum, to store the sum of prefix elements
#Traverse the array and at each index, add the element into the sum and check if this sum exists earlier. If the sum exists, then return true
#Also, insert every prefix sum into a map, so that later on it can be found whether the current sum is seen before or not
#At the end return false, as no such subarray is found
#Illustration:

#arr[] = {1, 4, -2, -2, 5, -4, 3}

#Consider all prefix sums, one can notice that there is a subarray with 0 sum when :

#Either a prefix sum repeats or
#Or prefix sum becomes 0.
#Prefix sums for above array are: 1, 5, 3, 1, 6, 2, 5
#Since prefix sum 1 repeats, we have a subarray with 0 sum. 

#Below is the Implementation of the above approach:

# python3 program to find if
# there is a zero sum subarray
 
 
def subArrayExists(arr, N):
    # traverse through array
    # and store prefix sums
    n_sum = 0
    s = set()
 
    for i in range(N):
        n_sum += arr[i]
 
        # If prefix sum is 0 or
        # it is already present
        if n_sum == 0 or n_sum in s:
            return True
        s.add(n_sum)
 
    return False
 
 
# Driver's code
if __name__ == '__main__':
    arr = [-3, 2, 3, 1, 6]
    N = len(arr)
 
    # Function call
    if subArrayExists(arr, N) == True:
        print("Found a sunbarray with 0 sum")
    else:
        print("No Such sub array exits!")
 
# This code is contributed by Shrikant13
#Output
#No Such Sub Array Exists!
#Time Complexity: O(N) under the assumption that a good hashing function is used, that allows insertion and retrieval operations in O(1) time. 
#Auxiliary Space: O(N) Here extra space is required for hashing
#-------------------------------------------------------------------

 

 