#Find common elements in three sorted arrays

#Difficulty Level : Easy
#---------------------------------------------------------------
#Given three arrays sorted in non-decreasing order, print all common elements in these arrays.

#Examples: 

#Input: 
#ar1[] = {1, 5, 10, 20, 40, 80} 
#ar2[] = {6, 7, 20, 80, 100} 
#ar3[] = {3, 4, 15, 20, 30, 70, 80, 120} 
#Output: 20, 80

#Input: 
#ar1[] = {1, 5, 5} 
#ar2[] = {3, 4, 5, 5, 10} 
#ar3[] = {5, 5, 10, 20} 
#Output: 5, 5
#-----------------------------------------------------
#A simple solution is to first find intersection of two arrays and store the intersection in a temporary array, then find the intersection of third array and temporary array. 
#Time complexity of this solution is O(n1 + n2 + n3) where n1, n2 and n3 are sizes of ar1[], ar2[] and ar3[] respectively.
#The above solution requires extra space and two loops, we can find the common elements using a single loop and without extra space. The idea is similar to intersection of two arrays. Like two arrays loop, we run a loop and traverse three arrays. 
#Let the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z. We can have following cases inside the loop. 

#If x, y and z are same, we can simply print any of them as common element and move ahead in all three arrays.
#Else If x < y, we can move ahead in ar1[] as x cannot be a common element.
#Else If x > z and y > z), we can simply move ahead in ar3[] as z cannot be a common element.
#Below image is a dry run of the above approach: 

#common elements in three sorted arrays



#Below is the implementation of the above approach:

# Python function to print common elements in three sorted arrays
def findCommon(ar1, ar2, ar3, n1, n2, n3):
 
    # Initialize starting indexes for ar1[], ar2[] and ar3[]
    i, j, k = 0, 0, 0
 
    # Iterate through three arrays while all arrays have elements
    while (i < n1 and j < n2 and k < n3):
 
        # If x = y and y = z, print any of them and move ahead
        # in all arrays
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print ar1[i],
            i += 1
            j += 1
            k += 1
 
        # x < y
        elif ar1[i] < ar2[j]:
            i += 1
 
        # y < z
        elif ar2[j] < ar3[k]:
            j += 1
 
        # We reach here when x > y and z < y, i.e., z is smallest
        else:
            k += 1
 
 
# Driver program to check above function
ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
print "Common elements are",
findCommon(ar1, ar2, ar3, n1, n2, n3)
 
# This code is contributed by __Devesh Agrawal__
#Output
#Common Elements are 20 80 
#Time complexity of the above solution is O(n1 + n2 + n3). In the worst case, the largest sized array may have all small elements and middle-sized array has all middle elements.
#Auxiliary Space:   O(1)
#------------------------------------------------------------------------
#Method 2:
#The approach used above works well if the arrays does not contain duplicate values however it can fail in cases where the array elements are repeated. This can lead to a single common element to get printed multiple times.

#These duplicate entries can be handled without using any additional data structure by keeping the track of the previous element. Since the elements inside the array are arranged in sorted manner there is no possibility for the repeated elements to occur at random positions. 

#Let’s consider the current element traversed in ar1[] be x, in ar2[] be y and in ar3[] be z and let the variables prev1, prev2, prev3 for keeping the track of last encountered element in each array and initialize them with INT_MIN. Hence for every element we visit across each array, we check for the following. 

#If x = prev1, move ahead in ar1[] and repeat the procedure until x != prev1. Similarly, apply the same for the ar2[] and ar3[].
#If x, y, and z are same, we can simply print any of them as common element, update prev1, prev2, and prev3 and move ahead in all three arrays.
#Else If (x < y), we update prev1 and move ahead in ar1[] as x cannot be a common element.
#Else If (y < z), we update prev2 and move ahead in ar2[] as y cannot be a common element.
#Else If (x > z and y > z), we update prev3 and we move ahead in ar3[] as z cannot be a common element.
#Below is the implementation of the above approach:

# Python 3 program for above approach
import sys
 
# This function prints
# common elements in ar1
 
 
def findCommon(ar1, ar2, ar3, n1,
               n2, n3):
 
    # Initialize starting indexes
    # for ar1[], ar2and
    # ar3[]
    i = 0
    j = 0
    k = 0
 
    # Declare three variables prev1,
    # prev2, prev3 to track
    # previous element
    # Initialize prev1, prev2,
    # prev3 with INT_MIN
    prev1 = prev2 = prev3 = -sys.maxsize - 1
 
    # Iterate through three arrays
    # while all arrays have
    # elements
    while (i < n1 and j < n2 and k < n3):
 
        # If ar1[i] = prev1 and i < n1,
        # keep incrementing i
        while (ar1[i] == prev1 and i < n1-1):
            i += 1
 
        # If ar2[j] = prev2 and j < n2,
        # keep incrementing j
        while (ar2[j] == prev2 and j < n2):
            j += 1
 
        # If ar3[k] = prev3 and k < n3,
        # keep incrementing k
        while (ar3[k] == prev3 and k < n3):
            k += 1
 
        # If x = y and y = z, pr
        # any of them, update
        # prev1 prev2, prev3 and move
        # ahead in each array
        if (ar1[i] == ar2[j] and ar2[j] == ar3[k]):
            print(ar1[i], end=" ")
            prev1 = ar1[i]
            prev2 = ar2[j]
            prev3 = ar3[k]
            i += 1
            j += 1
            k += 1
 
        # If x < y, update prev1
        # and increment i
        elif (ar1[i] < ar2[j]):
            prev1 = ar1[i]
            i += 1
 
        # If y < z, update prev2
        # and increment j
        elif (ar2[j] < ar3[k]):
            prev2 = ar2[j]
            j += 1
 
        # We reach here when x > y
        # and z < y, i.e., z is
        # smallest update prev3
        # and increment k
        else:
            prev3 = ar3[k]
            k += 1
 
 
# Driver code
ar1 = [1, 5, 10, 20, 40, 80, 80]
ar2 = [6, 7, 20, 80, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 80, 120]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
 
print("Common Elements are ")
findCommon(ar1, ar2, ar3, n1, n2, n3)
 
# This code is contributed by splevel62.
#Output
#Common Elements are 20 80 
#Time Complexity: O(n1 + n2 + n3)
#Auxiliary Space: O(1)
#-----------------------------------------------------------------
#Method 3:

#In this approach, we will first delete the duplicate from each array, and after this, we will find the frequency of each element and the element whose frequency equals 3 will be printed. For finding the frequency we can use a map but in this, we will use an array instead of a map. But the problem with using an array is, we cannot find the frequency of negative numbers so in the code given below we will consider each and every element of array to be positive.

#Below is the implementation of the above approach:

# Python implementation of the above approach   
import sys
def commonElements(arr1,  arr2,  arr3 , n1 , n2 , n3):
 
    # creating a max variable
    # for storing the maximum
    # value present in the all
    # the three array
    # this will be the size of
    # array for calculating the
    # frequency of each element
    # present in all the array
    Max = -sys.maxsize -1
 
    # deleting duplicates in linear time
    # for arr1
    res1 = 1
    for i in range(1, n1):
        Max = max(arr1[i], Max)
        if arr1[i] != arr1[res1 - 1]:
            arr1[res1] = arr1[i]
            res1 += 1
 
    # deleting duplicates in linear time
    # for arr2
    res2 = 1
    for i in range(1, n2):
        Max = max(arr2[i], Max)
        if (arr2[i] != arr2[res2 - 1]):
            arr2[res2] = arr2[i]
            res2 += 1
 
    # deleting duplicates in linear time
    # for arr3
    res3 = 1
    for i in range(1, n3):
        Max = max(arr3[i], Max)
        if (arr3[i] != arr3[res3 - 1]):
            arr3[res3] = arr3[i]
            res3 += 1
 
    # creating an array for finding frequency
    freq = [0 for i in range(Max + 1)]
 
    # calculating the frequency of
    # all the elements present in
    # all the array
    for i in range(res1):
        freq[arr1[i]] += 1
    for i in range(res2):
        freq[arr2[i]] += 1
    for i in range(res3):
        freq[arr3[i]] += 1
 
    # iterating till max and
    # whenever the frequency of element
    # will be three we print that element
    for i in range(Max + 1):
        if freq[i] == 3:
            print(i,end = " ")
 
# Driver Code
arr1 = [ 1, 5, 10, 20, 40, 80 ]
arr2 = [ 6, 7, 20, 80, 100 ]
arr3 = [ 3, 4, 15, 20, 30, 70, 80, 120 ]
 
commonElements(arr1, arr2, arr3, 6, 5, 8)
 
# This code is contributed by shinjanpatra
#Output
#20 80 
 
#Time Complexity: O(n1 + n2) 
#Auxiliary Space: O(maximum element in array))
#--------------------------------------------------------------------

#Method 4: Using STL 

#The idea is to use hash set. Here we use 2 of the sets to store elements of the 1st and 2nd arrays. The elements of the 3rd array are then checked if they are present in the first 2 sets. Then, we use a 3rd set to prevent any duplicates from getting added to the required array.

#Below is the implementation of the above approach:

# Python implementation of the approach
def findCommon(a, b, c, n1, n2, n3):
 
    # three sets to maintain frequency of elements
    uset = set()
    uset2 = set()
    uset3 = set()
    for i in range(n1):
        uset.add(a[i])
 
    for i in range(n2):
        uset2.add(b[i])
 
    # checking if elements of 3rd array are present in first 2 sets
    for i in range(n3):
 
        if(c[i] in uset and c[i] in uset2):
 
            # using a 3rd set to prevent duplicates
            if c[i] not in uset3:
                print(c[i], end = " ")
            uset3.add(c[i])
 
# Driver code
ar1 = [ 1, 5, 10, 20, 40, 80 ]
ar2 = [ 6, 7, 20, 80, 100 ]
ar3 = [ 3, 4, 15, 20, 30, 70, 80, 120 ]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
 
print("Common Elements are ")
findCommon(ar1, ar2, ar3, n1, n2, n3)
 
# This code is contributed by shinjanpatra.
#Output#
#Common Elements are 
#20 80 
#Time Complexity: O(n1 + n2 + n3) 
#Auxiliary Space: O(n1 + n2 + n3) 
#-----------------------------------------------------------------
#Method 5: Using Binary Search

#This approach is a modification of previous approach. Here Instead of using unordered_set, we use binary search to find elements of 1st array that are present in 2nd and 3rd arrays.

#Below is the implementation of the above approach:

# Python program to Find all range
# Having set bit sum X in array
 
 
def binary_search(arr, n, element):
 
    l,h = 0,n - 1
    while (l <= h):
        mid = (l + h) // 2
        if (arr[mid] == element):
            return True
 
        elif (arr[mid] > element):
            h = mid - 1
 
        else:
            l = mid + 1
 
    return False
 
def findCommon(a, b, c, n1, n2, n3):
 
    # Iterate on first array
    for j in range(n1):
        if (j != 0 and a[j] == a[j - 1]):
            continue
     
        # check if the element is present in 2nd and 3rd
        # array.
        if (binary_search(b, n2, a[j]) and binary_search(c, n3, a[j])):
            print(a[j],end=" ")
 
 
# Driver code
 
ar1 = [ 1, 5, 10, 20, 40, 80 ]
ar2 = [ 6, 7, 20, 80, 100 ]
ar3 = [ 3, 4, 15, 20, 30, 70, 80, 120 ]
n1 = len(ar1)
n2 = len(ar2)
n3 = len(ar3)
 
print("Common Elements are ")
findCommon(ar1, ar2, ar3, n1, n2, n3)
 
 
# This code is contributed by shinjanpatra
#Output
#Common Elements are 
#20 80 
#Time complexity: O(n1(log(n2*n3))
#Auxiliary complexity: O(1)
#--------------------------------------------------------------------



