#Count pairs with given sum

#Difficulty Level : Medium
#-----------------------------------------------------------------------
#Given an array of N integers, and a number sum, the task is to find the number of pairs of integers in the array whose sum is equal to sum.

#Examples:  

#Input:  arr[] = {1, 5, 7, -1}, sum = 6
#Output:  2
#Explanation: Pairs with sum 6 are (1, 5) and (7, -1).

#Input:  arr[] = {1, 5, 7, -1, 5}, sum = 6
#Output:  3
#Explanation: Pairs with sum 6 are (1, 5), (7, -1) & (1, 5).         

#Input:  arr[] = {1, 1, 1, 1}, sum = 2
#Output:  6
#Explanation: Pairs with sum 2 are (1, 1), (1, 1), (1, 1), (1, 1), (1, 1).

#Input:  arr[] = {10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1}, sum = 11
#Output:  9
#Explanation: Pairs with sum 11 are (10, 1), (10, 1), (10, 1), (12, -1), (10, 1), (10, 1), (10, 1), (7, 4), (6, 5).
#-------------------------------------------------------------------
#Naive Approach: 



#A simple solution is to traverse each element and check if there’s another number in the array which can be added to it to give sum.
#This can be achieved by nested loops.
#Illustration:

#Given arr[] = {1, 5, 7, -1}, sum = 6
#count = 0

#First Iteration : For index = 0
#{1, 5, 7, -1}, pair = (1, 5), count = 1
#Second Iteration : For index = 1
#{1, 5, 7, -1}, count = 1
#Third Iteration : For index = 2
#{1, 5, 7, -1}, count = 2
#Hence output is 2

#Follow the steps below to solve the given problem:

#Initialize the count variable with 0 which stores the result.
#Iterate arr and if the sum of ith and jth [i + 1…..n – 1] element is equal to sum i.e. arr[i] + arr[j] == sum, then increment the count variable.
#Return the count.
#Below is the implementation of the above approach.

# Python3 implementation of simple method
# to find count of pairs with given sum.
  
# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'
  
  
def getPairsCount(arr, n, sum):
  
    count = 0  # Initialize result
  
    # Consider all possible pairs
    # and check their sums
    for i in range(0, n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum:
                count += 1
  
    return count
  
  
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print("Count of pairs is",
      getPairsCount(arr, n, sum))
  
# This code is contributed by Smitha Dinesh Semwal
#Output
#Count of pairs is 3
#Time Complexity: O(n2), traversing the array for each element
#Auxiliary Space: O(1)
#-------------------------------------------------------------------
#Count pairs with given sum using Binary Search
#This approach is based on the following idea:

#If the array is sorted then for each array element arr[i], find the number of pairs by finding all the values (sum – arr[i]) which are situated after ith index.
#This can be achieved using Binary Search.
#Illustration:

#Given arr[] = {1, 5, 7, -1}, sum = 6

#Array after sorting: arr[] = {-1, 1, 5, 7}
#count = 0

#At index = 0: val = sum – arr[0] = 6 – (-1) = 7
#count = count + upperBound(1, 3, 7) – lowerBound(1, 3, 7)
#count = 1

#At index = 1: val = sum – arr[1] = 6 – 1 = 5
#count = count + upperBound(2, 3, 5) – lowerBound(2, 3, 5)
#count = 2

#At index = 2: val = sum – arr[2] = 6 – 5 = 1
#count = count + upperBound(3, 3, 1) – lowerBound(3, 3, 1)
#count = 2

#Number of pairs = 2

#Follow the steps below to solve the given problem:

#Sort the array arr[] in increasing order.
#Loop from i = 0 to N-1.
#Find the index of the first element having value same or just greater than (sum – arr[i]) using lower bound.
#Find the index of the first element having value just greater than (sum – arr[i]) using upper bound.
#The gap between these two indices is the number of elements with value same as (sum – arr[i]).
#Add this with the final count of pairs.
#Return the final count after the iteration is over.
#Below is the implementation of the above approach.

# Python code to implement the approach
import bisect
  
# Function to find the count of pairs
  
  
def getPairsCount(arr, n, k):
    arr.sort()
    x, c = 0, 0
    for i in range(n-1):
        x = k-arr[i]
  
        # Lower bound from i+1
        y = bisect.bisect_left(arr, x, i+1, n)
  
        # Upper bound from i+1
        z = bisect.bisect(arr, x, i+1, n)
        c = c+z-y
    return c
  
  
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
k = 6
  
# Function call
print("Count of pairs is", getPairsCount(arr, n, k))
  
# This code is contributed by Pushpesh Raj
#Output
#Count of pairs is 3
#Time Complexity: O(n * log(n) ), applying binary search on each element
#Auxiliary Space: O(1)
#-------------------------------------------------------
#Count pairs with given sum using Hashing
#This approach is based on the following idea:

#Check the frequency of sum – arr[i] in the arr
#This can be achieved using Hashing.
#Illustration:

#Given arr[] = {1, 5, 7, -1}, sum = 6

#Store the frequency of every element: 
#freq[arr[i]] = freq[arr[i]] + 1
#freq[1] : 1
#freq[5] : 1
#freq[7] : 1
#req[-1] : 1
 
#Initialise a variable count with 0 to find the required count of pairs
#At index = 0: freq[sum – arr[0]] = freq[6 – 1] = freq[5] = 1
#count = 1
#At index = 1: freq[sum – arr[1]] = freq[6 – 5] = freq[1] = 1
#count = 2
#At index = 2: freq[sum – arr[2]] = freq[6 – 7] = freq[-1] = 1
#count = 3
#At index = 3: freq[sum – arr[3]] = freq[6 – (-1)] = freq[7] = 1
#count = 4
#The above also contains repeated pairs from front and last, i.e. pair (a, b) and (b, a) are considered as different pairs till now.
#Therefore, we will reduce the count by half to determine the count of unique pairs.
#count = count / 2 = 2
#Therefore, required Number of pairs with given sum = 2
#Follow the steps below to solve the given problem: 

#Create a map to store the frequency of each number in the array. (Single traversal is required)
#In the next traversal, for every element check if it can be combined with any other element (other than itself!) to give the desired sum. Increment the counter accordingly.
#After completion of the second traversal, we’d have twice the required value stored in counter because every pair is counted two times. Hence divide the count by 2 and return.
#Below is the implementation of the above idea : 
 

# Python 3 implementation of simple method
# to find count of pairs with given sum.
import sys
  
# Returns number of pairs in arr[0..n-1]
# with sum equal to 'sum'
  
  
def getPairsCount(arr, n, sum):
  
    m = [0] * 1000
  
    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
  
    twice_count = 0
  
    # Iterate through each element and increment
    # the count (Notice that every pair is
    # counted twice)
    for i in range(0, n):
  
        twice_count += m[sum - arr[i]]
  
        # if (arr[i], arr[i]) pair satisfies the
        # condition, then we need to ensure that
        # the count is  decreased by one such
        # that the (arr[i], arr[i]) pair is not
        # considered
        if (sum - arr[i] == arr[i]):
            twice_count -= 1
  
    # return the half of twice_count
    return int(twice_count / 2)
  
  
# Driver function
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
  
print("Count of pairs is", getPairsCount(arr,
                                         n, sum))
  
# This code is contributed by
# Smitha Dinesh Semwal
#Output
#Count of pairs is 3
#Time Complexity: O(n), to iterate over the array
#Auxiliary Space: O(n), to make a map of size n
#--------------------------3----------------------------------------
#Count pairs with given sum using Hashing in Single loop
#This approach is based on the following idea:

#The idea is to solve in single loop.
#Check the frequency of sum – arr[i] in the arr
#This can be achieved using Hashing.
#Illustration:

#Given arr[] = {1, 5, 7, -1}, sum = 6

count = 0

#At index = 0: freq[sum – arr[0]] = freq[6 – 1] = freq[5] = 0
#count = 0
#freq[arr[0]] = freq[1] = 1

#At index = 1: freq[sum – arr[1]] = freq[6 – 5] = freq[1] = 1
#count = 1
#freq[arr[1]] = freq[5] = 1

#At index = 2: freq[sum – arr[2]] = freq[6 – 7] = freq[-1] = 0
#count = 1
#freq[arr[2]] = freq[7] = 1

#At index = 3: freq[sum – arr[3]] = freq[6 – (-1)] = freq[7] = 1
##count = 2
#freq[arr[3]] = freq[-1] = 1

count = 2

#Number of pairs  = 2

#Follow the steps below to solve the given problem: 

#Create a map to store the frequency of each number in the array.
#Check if (sum – arr[i]) is present in the map, if present then increment the count variable by its frequency.
#After traversal is over, return the count.
#Below is the implementation of the above idea : 

# Python implementation of simple method to find count of
# pairs with given sum.
  
# Returns number of pairs in arr[0..n-1] with sum equal to 'sum'
  
  
def getPairsCount(arr, n, sum):
    unordered_map = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in unordered_map:
            count += unordered_map[sum - arr[i]]
        if arr[i] in unordered_map:
            unordered_map[arr[i]] += 1
        else:
            unordered_map[arr[i]] = 1
    return count
  
  
# Driver code
arr = [1, 5, 7, -1, 5]
n = len(arr)
sum = 6
print('Count of pairs is', getPairsCount(arr, n, sum))
  
# This code is contributed by Manish Thapa
#Output
#Count of pairs is 3
#Time Complexity: O(n), to iterate over the array
#Auxiliary Space: O(n), to make a map of size n
#-------------------------------------------------------------------

