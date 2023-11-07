#Find Subarray with given sum | Set 1 (Non-negative Numbers)

#Difficulty Level : Medium
#Given an array arr[] of non-negative integers and an integer sum, find a subarray that adds to a given sum.

#Note: There may be more than one subarray with sum as the given sum, print first such subarray. 

#Examples: 

#Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
#Output: Sum found between indexes 2 and 4
#Explanation: Sum of elements between indices 2 and 4 is 20 + 3 + 10 = 33


#Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
#Output: Sum found between indexes 1 and 4
#Explanation: Sum of elements between indices 1 and 4 is 4 + 0 + 0 + 3 = 7

#Input: arr[] = {1, 4}, sum = 0
#Output: No subarray found
#Explanation: There is no subarray with 0 sum
#----------------------------------------------------------
#Find subarray with given sum using Nested loop
#The idea is to consider all subarrays one by one and check the sum of every subarray. Following program implements the given idea. 
#Run two loops: the outer loop picks a starting point i and the inner loop tries all subarrays starting from i.



#Follow the steps given below to implement the approach:

#Traverse the array from start to end.
#From every index start another loop from i to the end of the array to get all subarrays starting from i, and keep a variable currentSum to calculate the sum of every subarray.
#For every index in inner loop update currentSum = currentSum + arr[j]
#If the currentSum is equal to the given sum then print the subarray.
# Below is the implementation of the above approach.

# A simple program to print subarray with sum as given sum
 
# Returns true if the there is a subarray of arr[] with sum equal to 'sum' otherwise returns false. Also, prints the result
def subArraySum(arr, n, sum):
 
    # Pick a starting point
    for i in range(0,n):
        currentSum = arr[i]
        if(currentSum == sum):
            print("Sum found at indexes",i)
            return
        else:
            # Try all subarrays starting with 'i'
            for j in range(i+1,n):
                currentSum += arr[i]
                if(currentSum == sum):
                    print("Sum found between indexes",i,"and",j)
                    return
    print("No Subarray Found")
 
# Driver Code
if __name__ == "__main__":
    arr = [15,2,4,8,9,5,10,23]
    n = len(arr)
    sum = 23
    subArraySum(arr, n, sum)
     
    # This code is contributed by ajaymakvana
#Output
#Sum found between indexes 1 and 4
#Time Complexity: O(N2), Trying all subarrays from every index, used nested loop for the same
#Auxiliary Space: O(1). 
#---------------------------------------------------------------
#Find subarray with given sum using Sliding Window
#The idea is simple as we know that all the elements in subarray are positive so, If a subarray has sum greater than the given sum then there is no possibility that adding elements to the current subarray will be equal to the given sum. So the Idea is to use a similar approach to a sliding window. 

#Start with an empty subarray 
#add elements to the subarray until the sum is less than x( given sum ). 
#3If the sum is greater than x, remove elements from the start of the current subarray.
#Follow the steps given below to implement the approach:


#Create two variables, start=0, currentSum = arr[0]
#Traverse the array from index 1 to end.
#Update the variable currentSum by adding current element, currentSum = currentSum + arr[i]
#If the currentSum is greater than the given sum, update the variable currentSum as currentSum = currentSum – arr[start],
#and update start as, start++.
#If the currentSum is equal to given sum, print the subarray and break the loop.
# Below is the implementation of the above approach.

# An efficient program
# to print subarray
# with sum as given sum
 
# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.
 
 
def subArraySum(arr, n, sum_):
 
    # Initialize currentSum as
    # value of first element
    # and starting point as 0
    currentSum = arr[0]
    start = 0
 
    # Add elements one by
    # one to currentSum and
    # if the currentSum exceeds
    # the sum, then remove
    # starting element
    i = 1
    while i <= n:
 
        # If currentSum exceeds
        # the sum, then remove
        # the starting elements
        while currentSum > sum_ and start < i-1:
 
            currentSum = currentSum - arr[start]
            start += 1
 
        # If currentSum becomes
        # equal to sum, then
        # return true
        if currentSum == sum_:
            print("Sum found between indexes % d and % d" % (start, i-1))
 
            return 1
 
        # Add this element
        # to currentSum
        if i < n:
            currentSum = currentSum + arr[i]
        i += 1
 
    # If we reach here,
    # then no subarray
    print("No subarray found")
    return 0
 
 
# Driver program
if __name__ == '__main__':
    arr = [15, 2, 4, 8, 9, 5, 10, 23]
    n = len(arr)
    sum_ = 23
 
subArraySum(arr, n, sum_)
 
# This code is Contributed by shreyanshi_arun.
#Output
#Sum found between indexes 1 and 4
#Time Complexity: O(N)
#Auxiliary Space: O(1). Since no extra space has been taken.
#-----------------------------------------------------------------
#Find subarray with given sum using DP:
# We can use dynamic programming to find the subarray with the given sum. The basic idea is to iterate through the array, keeping track of the current sum and storing the difference between the current sum and the given sum in a hash table. If the difference is seen again later in the array, then we know that the subarray with the given sum exists and we can return it. This approach is efficient in terms of time and space, but it may not be suitable if the array is very large and the hash table becomes too large to fit in memory.

#Algorithm:

#Initialize an empty hash table and a variable curr_sum to 0.
#Iterate through the array, keeping track of the current element in a variable i.
#Add i to curr_sum and check if curr_sum – sum is in the hash table. If it is, then return the subarray from the index stored in the hash table to i.
#If curr_sum – sum is not in the hash table, add an entry to the hash table with the key curr_sum and the value i.
#If you reach the end of the array and no subarray with the given sum is found, return an empty array.
#Below in the implementation of the above approach:

#include <iostream>
#include <unordered_map>
#include <vector>
 
std::vector<int>
find_subarray_with_given_sum(const std::vector<int>& arr,
 #                            int sum)
{
    std::unordered_map<int, int> map;
    int curr_sum = 0;
    for (int i = 0; i < arr.size(); i++) {
        curr_sum += arr[i];
        if (map.count(curr_sum - sum)) {
            return std::vector<int>(
                arr.begin() + map[curr_sum - sum] + 1,
                arr.begin() + i + 1);
        }
        map[curr_sum] = i;
    }
    return {};
}
 
int main()
{
    std::vector<int> arr = { 15, 2, 4, 8, 9, 5, 10, 23 };
    std::vector<int> subarray
        = find_subarray_with_given_sum(arr, 23);
    if (subarray.empty()) {
        std::cout << "No subarray with given sum found"
                  << std::endl;
    }
    else {
        std::cout << "Subarray: [";
        for (int i : subarray) {
            std::cout << i << " ";
        }
        std::cout << "]" << std::endl;
    }
    return 0;
}
 
// This code is contributed by Susobhan Akhuli
Output
Subarray: [2 4 8 9 ]
Time Complexity: O(N)
Auxiliary Space: O(N) 

 
Complete Interview Preparation - GFG

The above solution doesn’t handle negative numbers. We can use hashing to handle negative numbers. See below set 2.

Find subarray with given sum | Set 2 (Handles Negative Numbers)
Find subarray with given sum with negatives allowed in constant space
