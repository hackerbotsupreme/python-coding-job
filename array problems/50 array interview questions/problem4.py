#K’th Smallest/Largest Element in Unsorted Array

#Difficulty Level : Medium

#-----------------------------------------------------------------
#Given an array and a number K where K is smaller than the size of the array. Find the K’th smallest element in the given array. Given that all array elements are distinct.

#Examples:  

#Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 3 
#Output: 7

#Input: arr[] = {7, 10, 4, 3, 20, 15}, K = 4 
#Output: 10 


#We have discussed a similar problem to print k largest elements. 
#-------------------------------------------------------------------
#K’th smallest element in an unsorted array using sorting:
#Sort the given array and return the element at index K-1 in the sorted array. 

#Follow the given steps to solve the problem:



#Sort the input array in the increasing order
#3Return the element at the K-1 index (0 – Based indexing) in the sorted array
#Below is the Implementation of the above approach:


# Python3 program to find K'th smallest
# element
 
# Function to return K'th smallest
# element in a given array
 
 
def kthSmallest(arr, N, K):
 
    # Sort the given array
    arr.sort()
 
    # Return k'th element in the
    # sorted array
    return arr[K-1]
 
 
# Driver code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2
 
    # Function call
    print("K'th smallest element is",
          kthSmallest(arr, N, K))
 
# This code is contributed by
# Shrikant13
#Output
#K'th smallest element is 5
#Time Complexity: O(N log N)
#Auxiliary Space: O(1) 

#-----------------------------------------------------------------
#K’th smallest element in an unsorted array using set data structure:
# Set data structure can be used to find the kth smallest element as it stores the distinct elements in sorted order. Set can be used because it is mentioned in the question that all the elements in the array are distinct.

#Follow the given steps to solve the problem:

#Insert all array elements into the set
#Advance the iterator to the Kth element in the set
#Return the value of the element at which the iterator is pointing
#Below is the Implementation of the above approach:

# Python3 code for the above approach
 
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 4
 
    s = set(arr)
 
    for itr in s:
        if K == 1:
            print(itr)  # itr is the Kth element in the set
            break
        K -= 1
 
# This code is contributed by Abhijeet Kumar(abhijeet19403)
#Output
#12
#Time Complexity:  O(N*log N)
#Auxiliary Space: O(N)

#---------------------------------------------------------
#K’th smallest element in an unsorted array using heap data structure:
#K’th smallest element in an unsorted array using Min-Heap
#Min-Heap can be used to find the kth smallest element, by inserting all the elements into Min-Heap and then and call extractMin() function K times. 

#Follow the given steps to solve the problem:

#Insert all the array elements into the Min-Heap
#Call extractMin() function K times
#Return the value obtained at the last call of extractMin() function 
#Below is the Implementation of the above approach:

# Python3 program to find K'th smallest element
# using min heap
 
# Class for Min Heap
 
 
class MinHeap:
 
    # Constructor
    def __init__(self, a, size):
 
        # list of elements in the heap
        self.harr = a
 
        # maximum possible size of min heap
        self.capacity = None
 
        # current number of elements in min heap
        self.heap_size = size
 
        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.minHeapify(i)
            i -= 1
 
    def parent(self, i):
        return (i - 1) / 2
 
    def left(self, i):
        return 2 * i + 1
 
    def right(self, i):
        return 2 * i + 2
 
    # Returns minimum
    def getMin(self):
        return self.harr[0]
 
    # Method to remove minimum element (or root)
    # from min heap
    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")
 
        # Store the minimum value
        root = self.harr[0]
 
        # If there are more than 1 items, move the last item
        # to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.minHeapify(0)
        self.heap_size -= 1
        return root
 
    # A recursive method to heapify a subtree with root at
    # given index. This method assumes that the subtrees
    # are already heapified
    def minHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if ((l < self.heap_size) and
                (self.harr[l] < self.harr[i])):
            smallest = l
        if ((r < self.heap_size) and
                (self.harr[r] < self.harr[smallest])):
            smallest = r
        if smallest != i:
            self.harr[i], self.harr[smallest] = (
                self.harr[smallest], self.harr[i])
            self.minHeapify(smallest)
 
# Function to return k'th smallest element in a given array
 
 
def kthSmallest(arr, N, K):
 
    # Build a heap of n elements in O(n) time
    mh = MinHeap(arr, N)
 
    # Do extract min (k-1) times
    for i in range(K - 1):
        mh.extractMin()
 
    # Return root
    return mh.getMin()
 
 
# Driver's code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 2
 
    # Function call
    print("K'th smallest element is", kthSmallest(arr, N, K))
 
# This Code is contributed by Kevin Joshi
#Output
#K'th smallest element is 5
#Time complexity: O(N + K Log N).
#Auxiliary Space: O(N)
#-------------------------------------------------------------------
#K’th smallest element in an unsorted array using Max-Heap
#Max-Heap can be used to find the kth smallest element, by inserting first K elements into Max-Heap and then compare remaining elements with the root of the Max-Heap and if the element is less than the root then remove the root and insert this element into the heap and finally return root of the Max-Heap 

#Follow the given steps to solve the problem:

#Build a Max-Heap MH of the first K elements (arr[0] to arr[K-1]) of the given array. 
#For each element, after the Kth element (arr[K] to arr[n-1]), compare it with the root of MH. 
#If the element is less than the root then make it the root and call heapify for Max-Heap MH
#b) Else ignore it. 
#Finally, the root of the MH is the Kth smallest element.
#Below is the Implementation of the above approach:

# Python3 program to find K'th smallest element
# using max heap
 
# Class for Max Heap
 
 
class MaxHeap:
    # Constructor
    def __init__(self, a, size):
        # list of elements in the heap
        self.harr = a
        # maximum possible size of max heap
        self.capacity = None
        # current number of elements in max heap
        self.heap_size = size
 
        i = int((self.heap_size - 1) / 2)
        while i >= 0:
            self.maxHeapify(i)
            i -= 1
 
    def parent(self, i):
        return (i - 1) / 2
 
    def left(self, i):
        return 2 * i + 1
 
    def right(self, i):
        return 2 * i + 2
 
    # Returns maximum
    def getMax(self):
        return self.harr[0]
 
    # to replace root with new node x and heapify() new root
    def replaceMax(self, x):
        self.harr[0] = x
        self.maxHeapify(0)
 
    # Method to remove maximum element (or root)
    # from max heap
    def extractMin(self):
        if self.heap_size == 0:
            return float("inf")
 
        # Store the maximum value.
        root = self.harr[0]
 
        # If there are more than 1 items, move the
        # last item to root and call heapify
        if self.heap_size > 1:
            self.harr[0] = self.harr[self.heap_size - 1]
            self.maxHeapify(0)
        self.heap_size -= 1
        return root
 
    # A recursive method to heapify a subtree with root at
    # given index. This method assumes that the subtrees
    # are already heapified
    def maxHeapify(self, i):
        l = self.left(i)
        r = self.right(i)
        largest = i
 
        if ((l < self.heap_size) and
                (self.harr[l] > self.harr[i])):
            largest = l
 
        if ((r < self.heap_size) and
                (self.harr[r] > self.harr[largest])):
            largest = r
 
        if largest != i:
            self.harr[i], self.harr[largest] = (
                self.harr[largest], self.harr[i])
            self.maxHeapify(largest)
 
 
# Function to return k'th smallest element in a given array
def kthSmallest(arr, N, K):
    # Build a heap of first k elements in O(k) time
    mh = MaxHeap(arr, K)
 
    # Process remaining n-k elements. If current element is
    # smaller than root, replace root with current element
    for i in range(K, N):
        if arr[i] < mh.getMax():
            mh.replaceMax(arr[i])
 
    # Return root
    return mh.getMax()
 
 
# Driver's code
if __name__ == '__main__':
    arr = [12, 3, 5, 7, 19]
    N = len(arr)
    K = 4
 
    # Function call
    print("K'th smallest element is", kthSmallest(arr, N, K))
 
# Code contributed by Kevin Joshi
#Output
#K'th smallest element is 12
#Time Complexity: O(K + (N-K) * Log K) 
#Auxiliary Space: O(K)
#-----------------------------------------------------------------------
#K’th smallest element in an unsorted array using QuickSelect:
#This is an optimization over method 1, if QuickSort is used as a sorting algorithm in first step. In QuickSort, pick a pivot element, then move the pivot element to its correct position and partition the surrounding array. The idea is, not to do complete quicksort, but stop at the point where pivot itself is k’th smallest element. Also, not to recur for both left and right sides of pivot, but recur for one of them according to the position of pivot. 

#Follow the given steps to solve the problem:

#Run quick sort algorithm on the input array
#In this algorithm pick a pivot element and move it to it’s correct position
#Now, if index of pivot is equal to K then return the value, else if the index of pivot is greater than K, then recur for the left subarray, else recur for the right subarray 
#Repeat this process until the element at index K is not found


# Python3 code for the above approach
 
# This function returns k'th smallest element
# in arr[l..r] using QuickSort based method.
# ASSUMPTION: ALL ELEMENTS IN ARR[] ARE DISTINCT
import sys
 
 
def kthSmallest(arr, l, r, K):
 
    # If k is smaller than number of
    # elements in array
    if (K > 0 and K <= r - l + 1):
 
        # Partition the array around last
        # element and get position of pivot
        # element in sorted array
        pos = partition(arr, l, r)
 
        # If position is same as k
        if (pos - l == K - 1):
            return arr[pos]
        if (pos - l > K - 1):  # If position is more,
                              # recur for left subarray
            return kthSmallest(arr, l, pos - 1, K)
 
        # Else recur for right subarray
        return kthSmallest(arr, pos + 1, r,
                           K - pos + l - 1)
 
    # If k is more than number of
    # elements in array
    return sys.maxsize
 
# Standard partition process of QuickSort().
# It considers the last element as pivot and
# moves all smaller element to left of it
# and greater elements to right
 
 
def partition(arr, l, r):
 
    x = arr[r]
    i = l
    for j in range(l, r):
        if (arr[j] <= x):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i
 
 
# Driver's Code
if __name__ == "__main__":
 
    arr = [12, 3, 5, 7, 4, 19, 26]
    N = len(arr)
    K = 3
    print("K'th smallest element is",
          kthSmallest(arr, 0, N - 1, K))
 
# This code is contributed by ita_c
#Output
#K'th smallest element is 5
#Time Complexity: O(N2) in worst case and O(N) on average 
#Auxiliary Space: O(1)
#--------------------------------------------------------------------

Auxiliary Space: O(1)

K’th smallest element in an unsorted array using Map:
This approach is very much similar to the QuickSelect and counting sort algorithm but much easier to implement. Use a map and then map each element with its frequency. And as an ordered map would store the data in a sorted manner, so keep on adding the frequency of each element till it does not become greater than or equal to k so that the k’th element from the start can be reached i.e. the k’th smallest element.

Example: A[] = {7, 0, 25, 6, 16, 17, 0}, K = 3

K’th Smallest/Largest Element in Unsorted Array

Follow the given steps to solve the problem:

Store frequency of every element in a Map mp
Now traverse over sorted elements in the Map mp and add their frequencies in a variable freq
If at any point the value of freq is greater than or equal to K, then return the value of iterator of Map mp
Below is the Implementation of the above approach:

# Python3 program for the above approach
 
 
def Kth_smallest(mp, K):
 
    freq = 0
    for it in sorted(mp.keys()):
        freq += mp[it]  # adding the frequencies of
        # each element
        if freq >= K:  # if at any point frequency becomes
            return it   # greater than or equal to k then
            # return that element
    return -1  # returning -1 if k>size of the array which
    # is an impossible scenario
 
 
# driver's code
if __name__ == "__main__":
    N = 5
    K = 2
    arr = [12, 3, 5, 7, 19]
    mp = {}
    for i in range(N):
        if arr[i] in mp:    # mapping every element with it's
            mp[arr[i]] = mp[arr[i]] + 1  # frequency
        else:
            mp[arr[i]] = 1
 
    # Function call
    ans = Kth_smallest(mp, K)
    print("The ", K, "th smallest element is ", ans)
 
# This code is contributed by Abhijeet Kumar(abhijeet19403)
Output
The 2th smallest element is 5
Time Complexity: O(N log N)
Auxiliary Space: O(N)

K’th smallest element in an unsorted array using Priority Queue:
To find the Kth minimum element in an array, insert the elements into the priority queue until the size of it is less than K, and then compare remaining elements with the root of the priority queue and if the element is less than the root then remove the root and insert this element into the priority queue and finally return root of the priority queue

Follow the given steps to solve the problem:

Build a priority queue of the first K elements (arr[0] to arr[K-1]) of the given array. 
For each element, after the Kth element (arr[K] to arr[n-1]), compare it with the root of priority queue. 
If the element is less than the root then remove the root and insert this element into the priority queue
b) Else ignore it. 
Finally, the root of the priority queue is the Kth smallest element.
Below is the Implementation of the above approach:

# Python3 code to implement the approach
import heapq
 
# Function to find the kth smallest array element
 
 
def kthSmallest(arr, N, K):
 
    # For finding min element we need (Max heap)priority queue
    pq = []
    for i in range(K):
 
        # First push first K elements into heap
        heapq.heappush(pq, arr[i])
        heapq._heapify_max(pq)
 
    # Now check from k to last element
    for i in range(K, N):
 
        # If current element is < first that means
        # there are  other k-1 lesser elements
        # are present at bottom thus, pop that element
        # and add kth largest element into the heap till curr
        # at last all the greater element than kth element will get pop off
        # and at the top of heap there will be kth smallest element
        if arr[i] < pq[0]:
            heapq.heappop(pq)
 
            # Push curr element
            heapq.heappush(pq, arr[i])
            heapq._heapify_max(pq)
    # Return first of element
    return pq[0]
 
 
# Driver's code:
if __name__ == "__main__":
    N = 10
    arr = [10, 5, 4, 3, 48, 6, 2, 33, 53, 10]
    K = 4
 
    # Function call
    print("Kth Smallest Element is:", kthSmallest(arr, N, K))
 
 
# This code is contributed by Tapesh(tapeshdua420)
#Output
#Kth Smallest Element is: 5
#Time complexity: O(K log K +  (N – K) log K)
#Auxiliary Space: O(K)

#K’th smallest element in an unsorted array using Binary Search:
#The idea to solve this problem is that the Kth smallest element would be the element at the kth position if the array was sorted in increasing order. Using this logic, binary search can be used to predict the index of an element as if the array was sorted but without actually sorting the array. 
 

#Follow the given steps to solve the problem:

#Find low and high that is the range where our answer can lie. 
#Apply Binary Search on this range. 
#If the selected element which would be mid has less than K elements lesser to it then increase the number that is low = mid + 1.
#Otherwise, Decrement the high pointer, i.e high = mid
#The Binary Search will end when only one element remains in the answer space which would be the answer.

























