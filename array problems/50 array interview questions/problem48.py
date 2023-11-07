#Chocolate Distribution Problem

#Difficulty Level : Easy
#--------------------------------------------------------------------
#Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

#Each student gets one packet.
#The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.
#Examples:

#Input : arr[] = {7, 3, 2, 4, 9, 12, 56} , m = 3 
##Output: Minimum Difference is 2 
#Explanation:
#We have seven packets of chocolates and we need to pick three packets for 3 students 
#If we pick 2, 3 and 4, we get the minimum difference between maximum and minimum packet sizes.

#Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5 
#Output: Minimum Difference is 6 

#Input : arr[] = {12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50} , m = 7 
#Output: Minimum Difference is 10 
#--------------------------------------------------------------
#Naive Approach for Chocolate Distribution Problem
#The idea is to generate all subsets of size m of arr[0..n-1]. For every subset, find the difference between the maximum and minimum elements in it. Finally, return the minimum difference.

#Efficient Approach for Chocolate Distribution Problem
#The idea is based on the observation that to minimize the difference, we must choose consecutive elements from a sorted packet. We first sort the array arr[0..n-1], then find the subarray of size m with the minimum difference between the last and first elements.



#Illustration:
#Below is the illustration of example arr[] = [ 7,3,2,4,9,12,56 ] , m = 3

#Chocolate Distribution Problem Solution

#Follow the steps mentioned below to implement the approach:

#Initially sort the given array. And declare a variable to store the minimum difference, and initialize it to INT_MAX. Let the variable be min_diff.
#Find the subarray of size m such that the difference between the last (maximum in case of sorted) and first (minimum in case of sorted) elements of the subarray is minimum.
#We will run a loop from 0 to (n-m), where n is the size of the given array and m is the size of the subarray.
#We will calculate the maximum difference with the subarray and store it in diff = arr[highest index] – arr[lowest index]
#Whenever we get a diff less than the min_diff, we will update the min_diff with diff.
#Below is the implementation of the above approach:


# Python3 program to solve
# chocolate distribution
# problem
 
 
# arr[0..n-1] represents sizes of packets
# m is number of students.
# Returns minimum difference between maximum
# and minimum values of distribution.
def findMinDiff(arr, n, m):
 
    # if there are no chocolates or number
    # of students is 0
    if (m == 0 or n == 0):
        return 0
 
    # Sort the given packets
    arr.sort()
 
    # Number of students cannot be more than
    # number of packets
    if (n < m):
        return -1
 
    # Largest number of chocolates
    min_diff = arr[n-1] - arr[0]
 
    # Find the subarray of size m such that
    # difference between last (maximum in case
    # of sorted) and first (minimum in case of
    # sorted) elements of subarray is minimum.
    for i in range(len(arr) - m + 1):
        min_diff = min(min_diff,  arr[i + m - 1] - arr[i])
 
    return min_diff
 
 
# Driver Code
if __name__ == "__main__":
    arr = [12, 4, 7, 9, 2, 23, 25, 41,
           30, 40, 28, 42, 30, 44, 48,
           43, 50]
    m = 7  # Number of students
    n = len(arr)
    print("Minimum difference is", findMinDiff(arr, n, m))
 
# This code is contributed by Smitha
#Output
#Minimum difference is 10
#Time Complexity: O(N*log(N))
#Auxiliary Space: O(1)
