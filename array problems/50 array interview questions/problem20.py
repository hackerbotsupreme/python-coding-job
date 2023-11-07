#Count subarrays with equal number of 1’s and 0’s

#
# Difficulty Level : Hard
#----------------------------------------------------------------------
#Given an array arr[] of size n containing 0 and 1 only. The problem is to count the subarrays having an equal number of 0’s and 1’s.

#Examples:  

#Input: arr[] = {1, 0, 0, 1, 0, 1, 1}
#Output: 8
#Explanation: The index range for the 8 sub-arrays are: (0, 1), (2, 3), (0, 3), (3, 4), (4, 5)(2, 5), (0, 5), (1, 6)

#Input: arr = { 1, 0, 0, 1, 1, 0, 0, 1}
#Output: 12
#--------------------------------------------------------------------
#Count subarrays with equal number of 1’s and 0’s using Frequency Counting:
#The problem is closely related to the Largest subarray with an equal number of 0’s and 1’s

#Follow the steps below to implement the above idea:

#Consider all 0’s in arr[] as -1.
#Create a hash table that holds the count of each sum[i] value, where sum[i] = sum(arr[0]+..+arr[i]), for i = 0 to n-1.
#Now start calculating the cumulative sum and then we get an incremental count of 1 for that sum represented as an index in the hash table. Arrays of each pair of positions with the same value in the cumulative sum constitute a continuous range with an equal number of 1’s and 0’s.
#Now traverse the hash table and get the frequency of each element in the hash table. Let frequency be denoted as freq. For each freq > 1 we can choose any two pairs of indices of a sub-array by (freq * (freq – 1)) / 2 number of ways. Do the same for all freq and sum up the result will be the number of all possible sub-arrays containing the equal number of 1’s and 0’s.
#Also, add freq of the sum of 0 to the hash table for the final result.
#Explanation: 
#Considering all 0’s as -1. if sum[i] == sum[j], where sum[i] = sum(arr[0]+..+arr[i]) and sum[j] = sum(arr[0]+..+arr[j]) and ‘i’ is less than ‘j’, then sum(arr[i+1]+..+arr[j]) must be 0. It can only be 0 if arr(i+1, .., j) contains an equal number of 1’s and 0’s. 



#Follow the steps below to implement the above approach:

# Python3 implementation to count
# subarrays with equal number
# of 1's and 0's
 
# function to count subarrays with
# equal number of 1's and 0's
 
 
def countSubarrWithEqualZeroAndOne(arr, n):
 
    # 'um' implemented as hash table
    # to store frequency of values
    # obtained through cumulative sum
    um = dict()
    curr_sum = 0
 
    # Traverse original array and compute
    # cumulative sum and increase count
    # by 1 for this sum in 'um'.
    # Adds '-1' when arr[i] == 0
    for i in range(n):
        curr_sum += (-1 if (arr[i] == 0) else arr[i])
        if um.get(curr_sum):
            um[curr_sum] += 1
        else:
            um[curr_sum] = 1
 
    count = 0
 
    # traverse the hash table 'um'
    for itr in um:
 
        # If there are more than one
        # prefix subarrays with a
        # particular sum
        if um[itr] > 1:
            count += ((um[itr] * int(um[itr] - 1)) / 2)
 
    # add the subarrays starting from
    # 1st element and have equal
    # number of 1's and 0's
    if um.get(0):
        count += um[0]
 
    # required count of subarrays
    return int(count)
 
 
# Driver code to test above
arr = [1, 0, 0, 1, 0, 1, 1]
n = len(arr)
print("Count =",
      countSubarrWithEqualZeroAndOne(arr, n))
 
# This code is contributed by "Sharad_Bhardwaj".
#Output
#Count = 8
#Time Complexity: O(N), where N is the length of the given array
#Auxiliary Space: O(N). 
#-------------------------------------------------------------------


#Count subarrays with equal number of 1’s and 0’s using Map:
#Follow the steps below for implementation:

#Create a map say mp.
#Iterate over the length of the given array
#Check if arr[i] == 0, then replace it with -1.
#Keep calculating the number into sum till ith index.
#If sum = 0, it implies the number of 0’s and 1’s are equal from arr[0]..arr[i]
#if mp[sum] exists then add “frequency-1” to count
#if the frequency of “sum” is zero then we initialize that frequency to 1, f it’s not 0, we increment it
#Finally, return the count.
#Follow the steps below to implement the above approach:

# Python3 implementation to count subarrays
# with equal number of 1's and 0's
 
 
def countSubarrWithEqualZeroAndOne(arr, n):
    mp = dict()
    Sum = 0
    count = 0
 
    for i in range(n):
 
        # Replacing 0's in array with -1
        if (arr[i] == 0):
            arr[i] = -1
 
        Sum += arr[i]
 
        # If Sum = 0, it implies number of
        # 0's and 1's are equal from arr[0]..arr[i]
        if (Sum == 0):
            count += 1
 
        if (Sum in mp.keys()):
            count += mp[Sum]
 
        mp[Sum] = mp.get(Sum, 0) + 1
 
    return count
 
 
# Driver Code
arr = [1, 0, 0, 1, 0, 1, 1]
 
n = len(arr)
 
print("count =",
      countSubarrWithEqualZeroAndOne(arr, n))
 
# This code is contributed by mohit kumar
#Output
#count=8
#Time Complexity: O(N), where N is the length of the given array
#Auxiliary Space: O(N).
#------------------------------------------------------
