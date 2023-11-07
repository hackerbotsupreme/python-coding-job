#Find whether an array is subset of another array

#Difficulty Level : Easy
#-----------------------------------------------------------------
#Given two arrays: arr1[0..m-1] and arr2[0..n-1]. Find whether arr2[] is a subset of arr1[] or not. Both arrays are not in sorted order. It may be assumed that elements in both arrays are distinct.

#Examples: 

#Input: arr1[] = {11, 1, 13, 21, 3, 7}, arr2[] = {11, 3, 7, 1} 
#Output: arr2[] is a subset of arr1[]

#Input: arr1[] = {1, 2, 3, 4, 5, 6}, arr2[] = {1, 2, 4} 
#Output: arr2[] is a subset of arr1[]

#Input: arr1[] = {10, 5, 2, 23, 19}, arr2[] = {19, 5, 3} 
#Output: arr2[] is not a subset of arr1[] 
#----------------------------------------------------------------------

#Naive Approach to Find whether an array is subset of another array
#Use two loops: The outer loop picks all the elements of arr2[] one by one. The inner loop linearly searches for the element picked by the outer loop. If all elements are found then return 1, else return 0.

#Below is the implementation of the above approach:



# Python 3 program to find whether an array
# is subset of another array
 
# Return 1 if arr2[] is a subset of
# arr1[]
 
 
def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0
    for i in range(n):
        for j in range(m):
            if(arr2[i] == arr1[j]):
                break
 
        # If the above inner loop was
        # not broken at all then arr2[i]
        # is not present in arr1[]
        if (j == m):
            return 0
 
    # If we reach here then all
    # elements of arr2[] are present
    # in arr1[]
    return 1
 
 
# Driver code
if __name__ == "__main__":
 
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
 
    m = len(arr1)
    n = len(arr2)
 
    if(isSubset(arr1, arr2, m, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")
 
# This code is contributed by ita_c
#Output
#arr2[] is subset of arr1[] 
#Time Complexity: O(m*n)
#Auxiliary Space: O(1)
#-------------------------------------------------------------------
#Find whether an array is subset of another array using Sorting and Binary Search
#The idea is to sort the given array arr1[], and then for each element in arr2[] do a binary search for it in sorted arr1[]. If the element is not found then return 0. If all elements are present then return 1.

#Illustration:

#Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

#Step 1: We will sort the array arr1[], and have arr1[] = { 1, 3, 7, 11, 13, 21}.

#Step 2: We will look for each element in arr2[] in arr1[] using binary search.

#arr2[] = { 11, 3, 7, 1 }, 11 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
#arr2[] = { 11, 3, 7, 1 }, 3 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
#arr2[] = { 11, 3, 7, 1 }, 7 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
#arr2[] = { 11, 3, 7, 1 }, 1 is present in arr1[] = { 1, 3, 7, 11, 13, 21}
#As all the elements are found we can conclude arr2[] is the subset of arr1[].

#Algorithm:

#The algorithm is pretty straightforward. 

#Sort the first array arr1[].
#Look for the elements of arr2[] in sorted arr1[].
#If we encounter a particular value that is present in arr2[] but not in arr1[], the code will terminate, arr2[] can never be the subset of arr1[].
#Else arr2[] is the subset of arr1[].
#Below is the code implementation of the above approach :

# Python3 program to find whether an array
# is subset of another array
 
# Return 1 if arr2[] is a subset of arr1[]
 
 
def isSubset(arr1, arr2, m, n):
    i = 0
 
    quickSort(arr1, 0, m-1)
    for i in range(n):
        if (binarySearch(arr1, 0, m - 1, arr2[i]) == -1):
            return 0
 
    # If we reach here then all elements
    # of arr2[] are present in arr1[]
    return 1
 
# FOLLOWING FUNCTIONS ARE ONLY FOR
# SEARCHING AND SORTING PURPOSE
# Standard Binary Search function
 
 
def binarySearch(arr, low, high, x):
    if(high >= low):
        mid = (low + high)//2
 
        # Check if arr[mid] is the first
        # occurrence of x.
        # arr[mid] is first occurrence if x is
        # one of the following
        # is true:
        # (i) mid == 0 and arr[mid] == x
        # (ii) arr[mid-1] < x and arr[mid] == x
        if((mid == 0 or x > arr[mid-1]) and (arr[mid] == x)):
            return mid
        elif(x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid - 1), x)
 
    return -1
 
 
def partition(A, si, ei):
    x = A[ei]
    i = (si - 1)
 
    for j in range(si, ei):
        if(A[j] <= x):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[ei] = A[ei], A[i + 1]
    return (i + 1)
 
# Implementation of Quick Sort
# A[] --> Array to be sorted
# si --> Starting index
# ei --> Ending index
 
 
def quickSort(A, si, ei):
    # Partitioning index
    if(si < ei):
        pi = partition(A, si, ei)
        quickSort(A, si, pi - 1)
        quickSort(A, pi + 1, ei)
 
 
# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
 
m = len(arr1)
n = len(arr2)
 
if(isSubset(arr1, arr2, m, n)):
    print("arr2[] is subset of arr1[] ")
else:
    print("arr2[] is not a subset of arr1[] ")
 
 
# This code is contributed by chandan_jnu
#Output
#arr2[] is subset of arr1[] 
#Time Complexity: O(mLog(m) + nlog(m)). O(mLog(m)) for sorting and O(nlog(m)) for binary searching each element of one array in another. In the above code, Quick Sort is used and the worst-case time complexity of Quick Sort is O(m2).
#----------------------------------------------------------------------------------------------
#Find whether an array is subset of another array using Sorting and Merging
#The idea is to sort the two arrays and then iterate on the second array looking for the same values on the first array using two pointers. Whenever we encounter the same values we will increment both the pointer and if we encounter any values less than that of the second array, we will increment the value of the pointer pointing to the first array. If the value is greater than that of the second array, we know the second array is not the subset of the first array.

#Illustration:

#Find whether an array is subset of another array using sorting and merging

#Algorithm:

#The initial step will be to sort the two arrays.

#Set two pointers j and i or arr1[] and arr2[] respectively.
#If arr1[j] < arr2[i], we will increase j by 1.
#If arr1[j] = arr2[i], we will increase j and i by 1.
#If arr1[j] > arr2[i], we will terminate as arr2[] is not the subset of arr1[].
#Below is the implementation of the above approach: 

# Python3 program to find whether an array
# is subset of another array
 
# Return 1 if arr2[] is a subset of arr1[] */
 
 
def isSubset(arr1, arr2, m, n):
    i = 0
    j = 0
    if m < n:
        return 0
 
    arr1.sort()
    arr2.sort()
 
    while i < n and j < m:
        if arr1[j] < arr2[i]:
            j += 1
        elif arr1[j] == arr2[i]:
            j += 1
            i += 1
        elif arr1[j] > arr2[i]:
            return 0
    return False if i < n else True
 
 
# Driver code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
 
m = len(arr1)
n = len(arr2)
if isSubset(arr1, arr2, m, n) == True:
    print("arr2[] is subset of arr1[] ")
else:
    printf("arr2[] is not a subset of arr1[] ")
 
# This code is contributed by Shrikant13
#Output
#arr2[] is subset of arr1[] 
#Time Complexity: O(mLog(m) + nLog(n)) which is better than approach 2.
#Auxiliary Space: O(1)

#Thanks to Parthsarthi for suggesting this method.

#Find whether an array is a subset of another array using Hashing
#The idea is to insert all the elements of the first array in a HashSet, and then iterate on the second array and find if the element exists in the HashSet, if the HashSet doesn’t contain any particular value then the second array is not the subset of the first array.

#Illustration:

#Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

#Step 1: We will store the array arr1[] elements in HashSet

#Step 2: We will look for each element in arr2[] in arr1[] using binary search.

#arr2[] = { 11, 3, 7, 1 }, 11 is present in the HashSet = { 1, 3, 7, 11, 13, 21}
#arr2[] = { 11, 3, 7, 1 }, 3 is present in the HashSet = { 1, 3, 7, 11, 13, 21}
#arr2[] = { 11, 3, 7, 1 }, 7 is present in the HashSet = { 1, 3, 7, 11, 13, 21}
#arr2[] = { 11, 3, 7, 1 }, 1 is present in the HashSet = { 1, 3, 7, 11, 13, 21}
#As all the elements are found we can conclude arr2[] is the subset of arr1[].

#Algorithm:

#The algorithm is pretty straightforward. 

#Store the first array arr1[] in a HashSet.
#Look for the elements of arr2[] in the HashSet.
#If we encounter a particular value that is present in arr2[] but not in the HashSet, the code will terminate, arr2[] can never be the subset of arr1[].
#Else arr2[] is the subset of arr1[].
#Below is the implementation of the above approach:  

# Python3 program to find whether an array
# is subset of another array
 
# Return true if arr2[] is a subset
# of arr1[]
 
 
def isSubset(arr1, m, arr2, n):
 
    # Using STL set for hashing
    hashset = set()
 
    # hset stores all the values of arr1
    for i in range(0, m):
        hashset.add(arr1[i])
 
    # Loop to check if all elements
    # of arr2 also lies in arr1
    for i in range(0, n):
        if arr2[i] in hashset:
            continue
        else:
            return False
 
    return True
 
 
# Driver Code
if __name__ == '__main__':
 
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
 
    m = len(arr1)
    n = len(arr2)
 
    if (isSubset(arr1, m, arr2, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[] ")
 
# This code is contributed by akhilsaini
#Output
#arr2[] is subset of arr1[] 
#Time Complexity: O(m+n*logm)
#Auxiliary Space: O(m)

#Find whether an array is a subset of another array using Set
#The idea is to insert all the elements of the first array and second array in the set, if the size of the set is equal to the size of arr1[] then the arr2[] is the subset of arr1[]. As no new elements are found in arr2[] hence is the subset.

#Illustration:

#Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

#Step 1: We will store the array arr1[] and arr2[] elements in Set

#The final Set = { 1, 3, 7, 11, 13, 21}
#Step 2: Size of arr1[] = 6 and size of the Set = 6

#Hence no new elements are found in arr2[]
#As all the elements are found we can conclude arr2[] is the subset of arr1[].

#Algorithm:

#The algorithm is pretty straightforward. 

#Store the first array arr1[] in a Set.
#Store the first array arr1[] in the same Set.
#If the size of arr1[] = size of the Set, arr2[] is the subset of arr1[].
#Else arr2[] is not the subset of arr1[].
# Python3 code
arr1 = [11, 1, 13, 21, 3, 7]
arr2 = [11, 3, 7, 1]
m = len(arr1)
n = len(arr2)
s = set()
for i in range(m):
    s.add(arr1[i])
 
p = len(s)
for i in range(n):
    s.add(arr2[i])
 
if (len(s) == p):
    print("arr2[] is subset of arr1[] ")
 
else:
    print("arr2[] is not subset of arr1[] ")
 
    # This code is contributed by divyeshrabadiya07.
#Output
#arr2[] is subset of arr1[] 
#Time Complexity: O(m+n) because we are using unordered_set and inserting in it, If we would be using an ordered set inserting would have taken log n increasing the TC to O(mlogm+nlogn), but order does not matter in this approach.
#Auxiliary Space: O(n+m)

#Find whether an array is a subset of another array using the Frequency Table
#The idea is to store the frequency of the elements present in the first array, then look for the elements present in arr2[] in the frequency array. As no new elements are found in arr2[] hence is the subset.

#Illustration:

#Given array arr1[] = { 11, 1, 13, 21, 3, 7 } and arr2[] = { 11, 3, 7, 1 }.

#Step 1: We will store the array arr1[] elements frequency in the frequency array

#The frequency array will look like this

#frequency array

#Step 2: We will look for arr2[] elements in the frequency array.

#arr2[] = { 11, 3, 7, 1 }, 11 is present in the frequency array
#arr2[] = { 11, 3, 7, 1 }, 3 is present in the frequency array
#arr2[] = { 11, 3, 7, 1 }, 7 is present in the frequency array
#arr2[] = { 11, 3, 7, 1 }, 1 is present in the frequency array
#As all the elements are found we can conclude arr2[] is the subset of arr1[].

Algorithm:

#The algorithm is pretty straightforward. 

#Store the frequency of the first array elements of arr1[] in the frequency array.
#Iterate on the arr2[] and look for its elements in the frequency array.
#If the value is found in the frequency array reduce the frequency value by one.
#3If for any elements in arr2[] frequency is less than 1, we will conclude arr2[] is not the subset of arr1[],
#Below is the implementation of the above approach:   

# Python3 program to find whether an array
# is subset of another array
 
# Return true if arr2[] is a subset of arr1[]
 
 
def isSubset(arr1, m, arr2, n):
 
    # Create a Frequency Table using STL
    frequency = {}
 
    # Increase the frequency of each element
    # in the frequency table.
    for i in range(0, m):
        if arr1[i] in frequency:
            frequency[arr1[i]] = frequency[arr1[i]] + 1
        else:
            frequency[arr1[i]] = 1
 
    # Decrease the frequency if the
    # element was found in the frequency
    # table with the frequency more than 0.
    # else return 0 and if loop is
    # completed return 1.
    for i in range(0, n):
        if (frequency[arr2[i]] > 0):
            frequency[arr2[i]] -= 1
        else:
            return False
 
    return True
 
 
# Driver Code
if __name__ == '__main__':
 
    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]
 
    m = len(arr1)
    n = len(arr2)
 
    if (isSubset(arr1, m, arr2, n)):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[] ")
 
# This code is contributed by akhilsaini
#Output
#arr2[] is subset of arr1[] 
#Time Complexity: O(m+n) which is better than methods 1,2,3
#Auxiliary Space: O(n)

#Note that method 1, method 2, method 4, and method 5 don’t handle the cases when we have duplicates in arr2[]. For example, {1, 4, 4, 2} is not a subset of {1, 4, 2}, but these methods will print it as a subset.  

#Please write comments if you find the above codes/algorithms incorrect, or find other ways to solve the same problem. 