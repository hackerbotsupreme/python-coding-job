#Merge two sorted arrays with O(1) extra space

#Difficulty Level : Medium
#------------------------------------------------------------------
#We are given two sorted arrays. We need to merge these two arrays such that the initial numbers (after complete sorting) are in the first array and the remaining numbers are in the second array

#Examples: 

#Input: ar1[] = {10}, ar2[] = {2, 3}
#Output: ar1[] = {2}, ar2[] = {3, 10}  

#Input: ar1[] = {1, 5, 9, 10, 15, 20}, ar2[] = {2, 3, 8, 13}
#Output: ar1[] = {1, 2, 3, 5, 8, 9}, ar2[] = {10, 13, 15, 20}
#--------------------------------------------------------------------
#Note: This task is simple and O(m+n) if we are allowed to use extra space. But it becomes really complicated when extra space is not allowed and doesn’t look possible in less than O(m*n) worst-case time.  Though further optimizations are possible
#--------------------------------------------------------------------

#Efficient Approach: To solve the problem follow the below idea:



#The idea is to begin from the last element of ar2[] and search for it in ar1[]. If there is a greater element in ar1[], then we move the last element of ar1[] to ar2[]. To keep ar1[] and ar2[] sorted, we need to place the last element of ar2[] at the correct place in ar1[]. We can use the Insertion Sort for this

#Follow the below steps to solve the problem:

#Iterate through every element of ar2[] starting from the last element
#Do the following for every element ar2[i]
#Store last element of ar1[]: last = ar1[m-1]
#Loop from the second last element of ar1[] while element ar1[j] is greater than ar2[i].
#ar1[j+1] = ar1[j] Move element one position ahead, then j–
#If last element of ar1[] is greater than ar2[i], then ar1[j+1] = ar2[i] and ar2[i] = last
#Print the arrays
#Note: In the above loop, elements in ar1[] and ar2[] are always kept sorted.

#Below is the implementation of the above approach:

# Python program to merge
# two sorted arrays
# with O(1) extra space.
 
# Merge ar1[] and ar2[]
# with O(1) extra space
 
 
def merge(ar1, ar2, m, n):
 
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n-1, -1, -1):
 
        # Find the smallest element
        # greater than ar2[i]. Move all
        # elements one position ahead
        # till the smallest greater
        # element is not found
        last = ar1[m-1]
        j = m-2
        while(j >= 0 and ar1[j] > ar2[i]):
            ar1[j+1] = ar1[j]
            j -= 1
 
        # If there was a greater element
        if (last > ar2[i]):
 
            ar1[j+1] = ar2[i]
            ar2[i] = last
 
# Driver code
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)
 
merge(ar1, ar2, m, n)
 
print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(ar1[i], " ", end="")
 
print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i], " ", end="")
 
# This code is contributed
# by Anant Agarwal.
#Output
#After Merging 
#First Array: 1 2 3 5 8 9 
#Second Array: 10 13 15 20 
#Time Complexity: O(M * N)
#Auxiliary Space: O(1)

#Below is the illustration of the above approach: 

#merge-two-sorted-arrays:pic is avialable
#Initial Arrays: 
#ar1[] = {1, 5, 9, 10, 15, 20}; 
#ar2[] = {2, 3, 8, 13};

#=> After First Iteration: 
#ar1[] = {1, 5, 9, 10, 13, 15}; 
#ar2[] = {2, 3, 8, 20}; 

#20 is moved from ar1[] to ar2[] 
#13 from ar2[] is inserted in ar1[]

#=> After Second Iteration: 
#ar1[] = {1, 5, 8, 9, 10, 13}; 
#ar2[] = {2, 3, 15, 20};

#15 is moved from ar1[] to ar2[] 
#8 from ar2[] is inserted in ar1[]

#=> After Third Iteration: 
#ar1[] = {1, 3, 5, 8, 9, 10}; 
#ar2[] = {2, 13, 15, 20};

#13 is moved from ar1[] to ar2[] 
#3 from ar2[] is inserted in ar1[]

#=> After Fourth Iteration: 
#ar1[] = {1, 2, 3, 5, 8, 9}; 
#ar2[] = {10, 13, 15, 20}; 

#10 is moved from ar1[] to ar2[] 
#2 from ar2[] is inserted in ar1[] 
#-------------------------------------------------------------------------------------------
#Efficient Approach: To solve the problem follow the below idea:

#The solution can be further optimized by observing that while traversing the two sorted arrays parallelly, if we encounter the jth second array element being smaller than ith first array element, then the jth element is to be included and replace some kth element in the first array. This observation helps us with the following algorithm

#Follow the below steps to solve the problem:

#Initialize i,j,k as 0,0,n-1 where n is the size of arr1 
#Iterate through every element of arr1 and arr2 using two pointers i and j respectively
#if arr1[i] is less than arr2[j], then increment i
#else swap the arr2[j] and arr1[k]and increment j and decrement k
#Sort both arr1 and arr2
#Below is the implementation of the above approach:

# Python program for the above approach
arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
 
# Function to merge two arrays
 
 
def merge(n, m):
    i = 0
    j = 0
    k = n - 1
    while (i <= k and j < m):
        if (arr1[i] < arr2[j]):
            i += 1
        else:
            temp = arr2[j]
            arr2[j] = arr1[k]
            arr1[k] = temp
            j += 1
            k -= 1
 
    arr1.sort()
    arr2.sort()
 
 
# Driver code
if __name__ == '__main__':
    merge(len(arr1), len(arr2))
    print("After Merging \nFirst Array: ", ','.join(str(x) for x in arr1))
    print("Second Array: ", ','.join(str(x) for x in arr2))
 # This code is contributed by gauravrajput1
#Output
#After Merging 
#First Array: 1 2 3 5 8 9 
#Second Array: 10 13 15 20 
#Time Complexity: O((N+M) * log(N+M))
#Auxiliary Space: O(1)



#---------------------------------------------------------------------






#Efficient Approach: To solve the problem follow the below idea:

#We can compare the last element of array one with first element of array two and if the last element is greater than first element the swap the elements and sort the second array as the elements of first array should be less than or equal to elements in second array. Repeating this process while this condition holds true will give us two sorted arrays 

#Follow the below steps to solve the problem:

#Initialize i with 0
#Iterate while loop until the last element of array 1 is greater than the first element of array 2
#if arr1[i] greater than first element of arr2
#swap arr1[i] with arr2[0]
#sort arr2
#Incrementing i by 1
#Print the arrays
#Below is the implementation of the above approach:

# Python3 program for the above approach
 
arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]
 
 
def merge(n, m):
    i = 0
    temp = 0
 
    # While loop till last element
    # of array 1(sorted)
    # is greater than first element
    # of array 2(sorted)
    while (arr1[n - 1] > arr2[0]):
        if (arr1[i] > arr2[0]):
 
            # Swap arr1[i] with first element
            # of arr2 and sorting the updated
            # arr2(arr1 is already sorted)
            # swap(arr1[i],arr2[0]);
            temp = arr1[i]
            arr1[i] = arr2[0]
            arr2[0] = temp
            arr2.sort()
 
        i += 1
 
 
# Driver code
if __name__ == '__main__':
    merge(len(arr1), len(arr2))
 
    print("After Merging \nFirst Array: ", arr1)
 
    print("Second Array: ", arr2)
 
 
# This code contributed by gauravrajput1
#Output
#After Merging 
#First Array: 1 2 3 5 8 9 
#Second Array: 10 13 15 20 
#Time Complexity: O(M * (N * logN))
#Auxiliary Space: O(1)
#-------------------------------------------------------------------
#Approach: Follow the below steps to solve the problem

#Note: Let the length of the shorter array be ‘M’ and the larger array be ‘N’

#Select the shorter array and find the index at which the partition should be done. 
#Partition the shorter array at its median (l1)
#Select the first N-l1 elements from the second array


#Compare the border elements i.e.
#if l1 < r2 and l2 < r2 we have found the index
#else if l1 > r2 we have to search in the left subarray
#else we have to search in the right subarray
#Note: This step will store all the smallest elements in the shorter array

#Swap all the elements right to the index(i) of the shorter array with the first N-i elements of the larger array
#Sort both arrays
#Note: if length(arr1) > length(arr2) all the smallest elements are stored in arr2 so we have to move all the elements in arr1 since we have to print arr1 first.

#Rotate the larger array (arr1) M times counter-clockwise
#Swap the first M elements of both arrays
#Below is the implementation of the above approach:

# Python program to merge
# two sorted arrays
# with O(1) extra space.
 
# Merge ar1[] and ar2[]
# with O(1) extra space
 
 
def rotate(a, n, idx):
    for i in range((int)(idx/2)):
        a[i], a[idx-1-i] = a[idx-1-i], a[i]
    for i in range(idx, (int)((n+idx)/2)):
        a[i], a[n-1-(i-idx)] = a[n-1-(i-idx)], a[i]
    for i in range((int)(n/2)):
        a[i], a[n-1-i] = a[n-1-i], a[i]
 
 
def sol(a1, a2, n, m):
    l = 0
    h = n-1
    idx = 0
    while (l <= h):
        c1 = (int)((l+h)/2)
        c2 = n-c1-1
        l1 = a1[c1]
        l2 = a2[c2-1]
        r1 = sys.maxint if c1 == n-1 else a1[c1+1]
        r2 = sys.maxint if c2 == m else a2[c2]
        if l1 > r2:
            h = c1-1
            if h == -1:
                idx = 0
        elif l2 > r1:
            l = c1+1
            if l == n-1:
                idx = n
        else:
            idx = c1+1
            break
    for i in range(idx, n):
        a1[i], a2[i-idx] = a2[i-idx], a1[i]
 
    a1.sort()
    a2.sort()
 
 
def merge(a1, a2, n, m):
    if n > m:
        sol(a2, a1, m, n)
        rotate(a1, n, n-m)
        for i in range(m):
            a1[i], a2[i] = a2[i], a1[i]
    else:
        sol(a1, a2, n, m)
# Driver program
 
 
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)
 
merge(ar1, ar2, m, n)
 
print("After Merging \nFirst Array:", end="")
for i in range(m):
    print(ar1[i], " ", end="")
print("\nSecond Array: ", end="")
for i in range(n):
    print(ar2[i], " ", end="")
# This code is contributed
# by Aditya Anand.
#Output
#After Merging 
#First Array: 1 2 3 5 8 9 
#Second Array: 10 13 15 20 
#Time Complexity: O(max(N * logN, M * logM))
#Auxiliary Space: O(1)

#----------------------------------------------------------
#Merge two sorted arrays with O(1) extra space using Insertion Sort with Simultaneous Merge:
#To solve the problem follow the below idea:

#We can use the insertion sort in the third approach above to reduce the time complexity as the array is already sorted, so we can place swapped element in its correct position by just performing a single traversal on the second array

#Follow the below steps to solve the problem

#Sort list 1 by always comparing with the head/first of list 2 and swap if required
#After each head/first swap, perform insertion of the swapped element into the correct position in list 2 which will eventually sort list 2 at the end
#For every swapped item from list 1, perform insertion sort in list 2 to find its correct position so that when list 1 is sorted, list 2 is also sorted
#Below is the implementation of the above approach:

# code contributed by mahee96
 
# "Insertion sort of list 2 with swaps from list 1"
#
# swap elements to get list 1 correctly, meanwhile
# place the swapped item in correct position of list 2
# eventually list 2 is also sorted
# Time = O(m*n) or O(n*m)
# AUX = O(1)
 
 
def merge(arr1, arr2):
    x = arr1
    y = arr2
    end = len(arr1)
    i = 0
    while(i < end):                 # O(m) or O(n)
        if(x[i] > y[0]):
            swap(x, y, i, 0)
            insert(y, 0)             # O(n) or O(m) number of shifts
        i += 1
 
# O(n):
 
 
def insert(y, i):
    orig = y[i]
    i += 1
    while (i < len(y) and y[i] < orig):
        y[i-1] = y[i]
        i += 1
    y[i-1] = orig
 
 
def swap(x, y, i, j):
    temp = x[i]
    x[i] = y[j]
    y[j] = temp
 
 
def test():
    c1 = [2, 3, 8, 13]
    c2 = [1, 5, 9, 10, 15, 20]
    c1, c2 = c2, c1
    merge(c1, c2)
    print(c1, c2)
         
 
 
test()
#Output
#After Merging 
#First Array: 1 2 3 5 8 9 
#Second Array: 10 13 15 20 
#Time Complexity: O(M * N) 
#Auxiliary Space: O(1)
#-----------------------------------------------------------------
Merge two sorted arrays with O(1) extra space using Euclidean Division Lemma:
To solve the problem follow the below idea:

We can merge the two arrays as in merge sort and simultaneously use Euclidean Division Lemma i.e. (((Operation on array) % x) * x).

Follow the below steps to solve the problem:

Merge the two arrays as we do in merge sort, while simultaneously using Euclidean Division Lemma, i.e. (((Operation on the array) % x) * x)
After merging divide both arrays with x
Where x needs to be a number greater than all elements of the array
Here in this case x, (according to the constraints) can be 10e7 + 1
Below is the implementation of the above approach:

# Python3 program to merge two sorted arrays without using extra space
 
 
def merge(arr1, arr2, n, m):
    # three pointers to iterate
    i = 0
    j = 0
    k = 0
    # for euclid's division lemma
    x = 10e7 + 1
    # in this loop we are rearranging the elements of arr1
    while i < n and (j < n and k < m):
        # if both arr1 and arr2 elements are modified
        if arr1[j] >= x and arr2[k] >= x:
            if arr1[j] % x <= arr2[k] % x:
                arr1[i] += (arr1[j] % x) * x
                j += 1
            else:
                arr1[i] += (arr2[k] % x) * x
                k += 1
        # if only arr1 elements are modified
        elif arr1[j] >= x:
            if arr1[j] % x <= arr2[k]:
                arr1[i] += (arr1[j] % x) * x
                j += 1
            else:
                arr1[i] += (arr2[k] % x) * x
                k += 1
        # if only arr2 elements are modified
        elif arr2[k] >= x:
            if arr1[j] <= arr2[k] % x:
                arr1[i] += (arr1[j] % x) * x
                j += 1
            else:
                arr1[i] += (arr2[k] % x) * x
                k += 1
        # if none elements are modified
        else:
            if arr1[j] <= arr2[k]:
                arr1[i] += (arr1[j] % x) * x
                j += 1
            else:
                arr1[i] += (arr2[k] % x) * x
                k += 1
        i += 1
 
    #  we can copy the elements directly as the other array
    #  is exchausted
    while j < n and i < n:
        arr1[i] += (arr1[j] % x) * x
        i += 1
        j += 1
    while k < m and i < n:
        arr1[i] += (arr2[k] % x) * x
        i += 1
        k += 1
    #  we need to reset i
    i = 0
 
    # in this loop we are rearranging the elements of arr2
    while i < m and (j < n and k < m):
        # if both arr1 and arr2 elements are modified
        if arr1[j] >= x and arr2[k] >= x:
            if arr1[j] % x <= arr2[k] % x:
                arr2[i] += (arr1[j] % x) * x
                j += 1
 
            else:
                arr2[i] += (arr2[k] % x) * x
                k += 1
 
        # if only arr1 elements are modified
        elif arr1[j] >= x:
            if arr1[j] % x <= arr2[k]:
                arr2[i] += (arr1[j] % x) * x
                j += 1
 
            else:
                arr2[i] += (arr2[k] % x) * x
                k += 1
 
        # if only arr2 elements are modified
        elif arr2[k] >= x:
            if arr1[j] <= arr2[k] % x:
                arr2[i] += (arr1[j] % x) * x
                j += 1
 
            else:
                arr2[i] += (arr2[k] % x) * x
                k += 1
 
        else:
            # if none elements are modified
            if arr1[j] <= arr2[k]:
                arr2[i] += (arr1[j] % x) * x
                j += 1
 
            else:
                arr2[i] += (arr2[k] % x) * x
                k += 1
 
        i += 1
    # we can copy the elements directly as the other array
    # is exhausted
    while j < n and i < m:
        arr2[i] += (arr1[j] % x) * x
        i += 1
        j += 1
 
    while k < m and i < m:
        arr2[i] += (arr2[k] % x) * x
        i += 1
        k += 1
 
    # we need to reset i
    i = 0
    # we need to divide the whole arr1 by x
    while i < n:
        arr1[i] /= x
        i += 1
 
    # we need to reset i
    i = 0
    # we need to divide the whole arr2 by x
    while i < m:
        arr2[i] /= x
        i += 1
 
# Driver program
 
 
ar1 = [1, 5, 9, 10, 15, 20]
ar2 = [2, 3, 8, 13]
m = len(ar1)
n = len(ar2)
 
merge(ar1, ar2, m, n)
 
print("After Merging \nFirst Array:", end=" ")
for i in range(m):
    print(int(ar1[i]), end=" ")
print("\nSecond Array:", end=" ")
for i in range(n):
    print(int(ar2[i]), end=" ")
 
# This code is contributed by Tapesh(tapeshdua420)
#Output
#After Merging 
#First Array: 1 2 3 5 8 9 
#Second Array: 10 13 15 20 
#Time Complexity: O(M + N)
#Auxiliary Space: O(1), since no extra space has been taken

#Related Articles: 
#Merge two sorted arrays 
#Merge k sorted arrays | Set 1
#Efficiently merging two sorted arrays with O(1) extra space
#------------------------------------------------------------------------




