#Maximum Product Subarray

#Difficulty Level : Hard


#Given an array that contains both positive and negative integers, find the product of the maximum product subarray. 

#Examples:

#Input: arr[] = {6, -3, -10, 0, 2}
#Output:   180  // The subarray is {6, -3, -10}

#Input: arr[] = {-1, -3, -10, 0, 60}
#Output:   60  // The subarray is {60}
#----------------------------------------------------------------------
#Naive Approach: To solve the problem follow the below idea:

#The idea is to traverse over every contiguous subarray, find the product of each of these subarrays and return the maximum product from these results.



#Follow the below steps to solve the problem:

#Run a nested for loop to generate every subarray
#Calculate the product of elements in the current subarray
#Return the maximum of these products calculated from the subarrays
#Below is the implementation of the above approach:

# Python3 program to find Maximum Product Subarray
 
# Returns the product of max product subarray.
 
 
def maxSubarrayProduct(arr, n):
 
    # Initializing result
    result = arr[0]
 
    for i in range(n):
 
        mul = arr[i]
 
        # traversing in current subarray
        for j in range(i + 1, n):
 
            # updating result every time
            # to keep an eye over the maximum product
            result = max(result, mul)
            mul *= arr[j]
 
        # updating the result for (n-1)th index.
        result = max(result, mul)
 
    return result
 
 
# Driver code
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print("Maximum Sub array product is", maxSubarrayProduct(arr, n))
 
# This code is contributed by divyeshrabadiya07
#Output
#Maximum Sub array product is 112
#Time Complexity: O(N2)
#Auxiliary Space: O(1)
#-------------------------------------------------------------

#Efficient Approach: To solve the problem follow the below idea:

#The following solution assumes that the given input array always has a positive output. The solution works for all cases mentioned above. It doesn’t work for arrays like {0, 0, -20, 0}, {0, 0, 0}.. etc. The solution can be easily modified to handle this case. It is similar to the Largest Sum Contiguous Subarray problem. 


#The only thing to note here is, the maximum product can also be obtained by the minimum (negative) product ending with the previous element multiplied by this element. For example, in array {12, 2, -3, -5, -6, -2}, when we are at element -2, the maximum product is the multiplication of, the minimum product ending with -6 and -2

#Note: if all elements of the array are negative then the maximum product with the above algorithm is 1. so, if the maximum product is 1, then we have to return the maximum element of an array

#Follow the below steps to solve the problem:

#Declare two integers max_ending _here and min_ending_here equal to one and max_so_far equal to zero
#Run a for loop for i [0, N]
#If the current element is greater than zero
#Set max_ending_here equal to max_ending_here * arr[i]
#Set min_ending_here equal to the minimum of min_ending_here * arr[i] and 1
#Set a boolean flag equal to one
#Else if the current element is equal to zero
#Set both max_ending_here and min_ending_here equal to one
#Else
#Set max_ending here equal to the maximum of min_ending_here * arr[i] and 1
#Set min_ending_here equal to max_ending_here * arr[i]
#If max_ending_here is greater than max_so_far then update max_so_far
#If the flag is equal to zero then return zero
#If the max_so_far is equal to one i.e all array elements are negative the return maximum element in the input array
#Return max_so_far
#Below is the implementation of the above approach:

# Python program to find maximum product subarray
 
# Returns the product of max product subarray.
# Assumes that the given array always has a subarray
# with product more than 1
 
 
def maxsubarrayproduct(arr):
 
    n = len(arr)
 
    # max positive product ending at the current position
    max_ending_here = 1
 
    # min positive product ending at the current position
    min_ending_here = 1
 
    # Initialize maximum so far
    max_so_far = 0
    flag = 0
 
    # Traverse throughout the array. Following values
    # are maintained after the ith iteration:
    # max_ending_here is always 1 or some positive product
    # ending with arr[i]
    # min_ending_here is always 1 or some negative product
    # ending with arr[i]
    for i in range(0, n):
 
        # If this element is positive, update max_ending_here.
        # Update min_ending_here only if min_ending_here is
        # negative
        if arr[i] > 0:
            max_ending_here = max_ending_here * arr[i]
            min_ending_here = min(min_ending_here * arr[i], 1)
            flag = 1
 
        # If this element is 0, then the maximum product cannot
        # end here, make both max_ending_here and min_ending_here 0
        # Assumption: Output is alway greater than or equal to 1.
        elif arr[i] == 0:
            max_ending_here = 1
            min_ending_here = 1
 
        # If element is negative. This is tricky
        # max_ending_here can either be 1 or positive.
        # min_ending_here can either be 1 or negative.
        # next min_ending_here will always be prev.
        # max_ending_here * arr[i]
        # next max_ending_here will be 1 if prev
        # min_ending_here is 1, otherwise
        # next max_ending_here will be prev min_ending_here * arr[i]
        else:
            temp = max_ending_here
            max_ending_here = max(min_ending_here * arr[i], 1)
            min_ending_here = temp * arr[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
    if flag == 0 and max_so_far == 0:
        return 0
    return max_so_far
 
 
# Driver function to test above function
arr = [1, -2, -3, 0, 7, -8, -2]
print("Maximum product subarray is", maxsubarrayproduct(arr))
 
# This code is contributed by Devesh Agrawal
#Output
#Maximum Sub array product is 112
#Time Complexity: O(N) 
#Auxiliary Space: O(1)

#Efficient Approach: To solve the problem follow the below idea:

#The above solution assumes there is always a positive outcome for the given array which does not work for cases where the array contains only non-positive elements like {0, 0, -20, 0}, {0, 0, 0}.. etc. The modified solution is also similar to the Largest Sum Contiguous Subarray problem which uses Kadane’s algorithm. 

#Follow the below steps to solve the problem:

#Here we use 3 variables called max_so_far, max_ending_here & min_ending_here
#For every index, the maximum number ending at that index will be the maximum(arr[i], max_ending_here * arr[i], min_ending_here[i]*arr[i])
#Similarly, the minimum number ending here will be the minimum of these 3
#Thus we get the final value for the maximum product subarray
#Below is the implementation of the above approach:

# Python3 program to find Maximum Product Subarray
 
#  Returns the product
# of max product subarray.
 
 
def maxSubarrayProduct(arr, n):
 
    # max positive product
    # ending at the current position
    max_ending_here = arr[0]
 
    # min negative product ending
    # at the current position
    min_ending_here = arr[0]
 
    # Initialize overall max product
    max_so_far = arr[0]
 
    # /* Traverse through the array.
    # the maximum product subarray ending at an index
    # will be the maximum of the element itself,
    # the product of element and max product ending previously
    # and the min product ending previously. */
    for i in range(1, n):
        temp = max(max(arr[i], arr[i] * max_ending_here),
                   arr[i] * min_ending_here)
        min_ending_here = min(
            min(arr[i], arr[i] * max_ending_here), arr[i] * min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)
 
    return max_so_far
 
 
# Driver code
arr = [1, -2, -3, 0, 7, -8, -2]
n = len(arr)
print(f"Maximum Sub array product is {maxSubarrayProduct(arr, n)}")
 
# This code is contributed by shinjanpatra
#Output
#Maximum Sub array product is 112
#Time Complexity: O(N)
#Auxiliary Space: O(1)


