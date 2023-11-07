#Given an array arr[], find the maximum j – i such that arr[j] > arr[i]

#Difficulty Level : Hard
#-----------------------------------------------------------------------

#Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

#Examples : 

#  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
#  Output: 6  (j = 7, i = 1)

#  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
#  Output: 8 ( j = 8, i = 0)

#  Input:  {1, 2, 3, 4, 5, 6}
#  Output: 5  (j = 5, i = 0)

#  Input:  {6, 5, 4, 3, 2, 1}
#  Output: -1 
#--------------------------------------------------------------------
#Method 1 (Simple but Inefficient): Run two loops. In the outer loop, pick elements one by one from the left. In the inner loop, compare the picked element with the elements starting from the right side. Stop the inner loop when you see an element greater than the picked element and keep updating the maximum j-i so far. 

# Python3 program to find the maximum
# j – i such that arr[j] > arr[i]
 
# For a given array arr[], returns
# the maximum j – i such that
# arr[j] > arr[i]
 
 
def maxIndexDiff(arr, n):
    maxDiff = -1
    for i in range(0, n):
        j = n - 1
        while(j > i):
            if arr[j] > arr[i] and maxDiff < (j - i):
                maxDiff = j - i
            j -= 1
 
    return maxDiff
 
 
# driver code
arr = [9, 2, 3, 4, 5, 6, 7, 8, 18, 0]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)
 
# This article is contributed by Smitha Dinesh Semwal
#Output
#8
#Time Complexity: O(n2)
#Auxiliary Space: O(1)

#Method 2: Improvising the Brute Force Algorithm and looking for BUD, i.e Bottlenecks, unnecessary and duplicated works. A quick observation actually shows that we have been looking to find the first greatest element traversing from the end of the array to the current index. We can see that we are trying to find the first greatest element again and again for each element in the array. Let’s say we have an array with us for example [1, 5, 12, 4, 9] now we know that 9 is the element that is greater than 1, 5, and 4 but why do we need to find that again and again. We can actually keep a track of the maximum number moving from the end to the start of the array. The approach will help us understand better and also this improvisation is great to come up with in an interview. 



#Approach :  

#Traverse the array from the end and keep a track of the maximum number to the right of the current index including self
#Now we have a monotonous decreasing array, and we know we can use binary search to find the index of the rightmost greater element
#Now we will just use binary search for each of the elements in the array and store the maximum difference of the indices and that’s it we are done.
# Python3 program to implement
# the above approach
 
# For a given array arr,
# calculates the maximum j – i
# such that arr[j] > arr[i]
 
# Driver code
if __name__ == '__main__':
   
    v = [34, 8, 10, 3,
         2, 80, 30, 33, 1];
    n = len(v);
    maxFromEnd = [-38749432] * (n + 1);
 
    # Create an array maxfromEnd
    for i in range(n - 1, 0, -1):
        maxFromEnd[i] = max(maxFromEnd[i + 1],
                            v[i]);
 
    result = 0;
 
    for i in range(0, n):
        low = i + 1; high = n - 1; ans = i;
 
        while (low <= high):
            mid = int((low + high) / 2);
 
            if (v[i] <= maxFromEnd[mid]):
               
                # We store this as current
                # answer and look for further
                # larger number to the right side
                ans = max(ans, mid);
                low = mid + 1;
            else:
                high = mid - 1;       
 
        # Keeping a track of the
        # maximum difference in indices
        result = max(result, ans - i);
     
    print(result, end = "");
     
# This code is contributed by Rajput-Ji
#Output
#6
#Time complexity : O(N*log(N)) 
#Space complexity: O(N)

#Method 3 O(n * log n): Use hashing and sorting to solve this problem in less than quadratic complexity after taking special care of the duplicates. 
#Approach :  

#Traverse the array and store the index of each element in a list (to handle duplicates).
#Sort the array.
#Now traverse the array and keep track of the maximum difference of i and j.
#For j consider the last index from the list of possible indexes of the element and for i consider the first index from the list. (As the index was appended in ascending order).
#Keep updating the max difference till the end of the array.
#Below is the implementation of the above approach:

# Python3 implementation of the above approach
n = 9
a = [34, 8, 10, 3, 2, 80, 30, 33, 1]
 
# To store the index of an element.
index = dict()
for i in range(n):
    if a[i] in index:
 
        # append to list (for duplicates)
        index[a[i]].append(i) 
    else:
 
        # if first occurrence
        index[a[i]] = [i]  
 
# sort the input array
a.sort()    
maxDiff = 0
 
# Temporary variable to keep track of minimum i
temp = n    
for i in range(n):
    if temp > index[a[i]][0]:
        temp = index[a[i]][0]
    maxDiff = max(maxDiff, index[a[i]][-1]-temp)
 
#print(maxDiff)
#Output
#The maxIndexDiff is : 6
#Time complexity : O(N*log(N)) 
#Auxiliary Space: O(N)

#Method 4 (Efficient): To solve this problem, we need to get two optimum indexes of arr[]: left index i and right index j. For an element arr[i], we do not need to consider arr[i] for left index if there is an element smaller than arr[i] on left side of arr[i]. Similarly, if there is a greater element on right side of arr[j] then we do not need to consider this j for the right index. So we construct two auxiliary arrays LMin[] and RMax[] such that LMin[i] holds the smallest element on left side of arr[i] including arr[i], and RMax[j] holds the greatest element on right side of arr[j] including arr[j]. After constructing these two auxiliary arrays, we traverse both of these arrays from left to right. While traversing LMin[] and RMax[] if we see that LMin[i] is greater than RMax[j], then we must move ahead in LMin[] (or do i++) because all elements on left of LMin[i] are greater than or equal to LMin[i]. Otherwise, we must move ahead in RMax[j] to look for a greater j – i value.

#Thanks to celicom for suggesting the algorithm for this method. 

#Working Example:

#Lets consider any example [7 3 1 8 9 10 4 5 6]

#what is maxRight ?

#Filling from right side 6 is first element now 6 > 5 so again we fill 6 till we reach 10 > 6 :

#[10 10 10 10 10 10 6 6 6] this is maxR

#[7 3 1 1 1 1 1 1 1 ] this is minL

#now we see that how to reach answer from these to and its proof !!!

#lets compare first elements of the arrays now we see 10 > 7,

#now we increase maxR by 1 till it becomes lesser than 7 i.e at index 5

#hence answer till now is. 5-0 = 5

#now we will increase minL we get 3 which is lesser than 6 so we increase maxR till it reaches last index and the answer becomes 8-1= 7

#so we see how we are getting correct answer.

#As we need the max difference j – i such that A[i]<= A[j], hence we do not need to consider element after the index j and element before index i.

#in previous hint, make 2 arrays,

#First, will store smallest occurring element before the element

#Second, will store largest occurring element after the element

#Traverse the Second array, till the element in second array is larger than or equal to First array, and store the index difference. And if it becomes smaller, traverse the first array till it again becomes larger.

#And store the max difference of this index difference.

#Below is the implementation of the above approach:

# Utility Functions to get max
# and minimum of two integers
def max(a, b):
    if(a > b):
        return a
    else:
        return b
 
def min(a, b):
    if(a < b):
        return a
    else:
        return b
 
# For a given array arr[],
# returns the maximum j - i
# such that arr[j] > arr[i]
def maxIndexDiff(arr, n):
    maxDiff = 0;
    LMin = [0] * n
    RMax = [0] * n
 
    # Construct LMin[] such that
    # LMin[i] stores the minimum
    # value from (arr[0], arr[1],
    # ... arr[i])
    LMin[0] = arr[0]
    for i in range(1, n):
        LMin[i] = min(arr[i], LMin[i - 1])
 
    # Construct RMax[] such that
    # RMax[j] stores the maximum
    # value from (arr[j], arr[j + 1],
    # ..arr[n-1])
    RMax[n - 1] = arr[n - 1]
    for j in range(n - 2, -1, -1):
        RMax[j] = max(arr[j], RMax[j + 1]);
 
    # Traverse both arrays from left
    # to right to find optimum j - i
    # This process is similar to
    # merge() of MergeSort
    i, j = 0, 0
    maxDiff = -1
    while (j < n and i < n):
        if (LMin[i] <= RMax[j]):
            maxDiff = max(maxDiff, j - i)
            j = j + 1
        else:
            i = i + 1
 
    return maxDiff
 
# Driver Code
if(__name__ == '__main__'):
    arr = [9, 2, 3, 4, 5,
           6, 7, 8, 18, 0]
    n = len(arr)
    maxDiff = maxIndexDiff(arr, n)
    print (maxDiff)
 
# This code is contributed
# by gautam karakoti
#Output
#8
#Time Complexity: O(n) 
#Auxiliary Space: O(n) 

#Asked in: Amazon,  Google,  VMWare
#Please write comments if you find the above codes/algorithms incorrect, or find other ways to solve the same problem.

#Another Approach: ( only using one extra array ): We consider an auxiliary array : rightMax[] , such that, rightMax[i] = max element of the subarray arr[i…(n-1)], the largest or equal element after arr[i] element Suppose (arr[i], arr[jLast] ) is a pair, such that arr[jLast] is the last greater or equal element than arr[i]. For the pairs ending with arr[jLast] :  ( arr[k], arr[jLast] ) for all k = (i+1) to jLast we don’t need to consider (jLast – k) because (jLast – i ) > (jLast – k) for all such k’s. So we can skip those pairs. Traversing from left to right of both arrays : arr[] and rightMax[]  , when we first encounter rightMax[j] < arr[i[  , we know that jLast = j-1, and we can skip the pairs (arr[k], arr[jLast]) for all k = (i+1) to jLast. And also rightMax[] is non increasing sequence , so all elements at right side of rightMax[j] is smaller than or equal to rightMax[j]. But there may be arr[x]  after arr[i] (x > i) such that arr[x] < rightMax[j] for x > i, so increment i when rightMax[j] < arr[i] is encountered.

#Below is the implementation of the above approach:

# For a given array arr[], returns the
# maximum j – i such that arr[j] > arr[i]
def maxIndexDiff(arr, n):
     
    rightMax = [0] * n
    rightMax[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], arr[i])
         
    # rightMax[i] = max arr[i...(n-1]
    maxDist = -2**31
    i = 0
    j = 0
     
    while (i < n and j < n):
        if (rightMax[j] >= arr[i]):
            maxDist = max(maxDist, j - i)
            j += 1
             
        else:
             
            # if(rightMax[j] < leftMin[i])
            i += 1
     
    return maxDist
 
# Driver Code
arr = [ 34, 8, 10, 3, 2, 80, 30, 33, 1 ]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
 
print(maxDiff)
 
# This code is contributed by Shubham Singh
#Output
#6
#Time complexity: O(n), As i and j pointers are traversing at most n elements, time complexity  = O(n) + O(n) = O(n)
#Auxiliary Space: O(n)

#Using leftMin[]: We can also do this using leftMin[] array only , where leftMin[i] = min element of the subarray arr[0…i]

# For a given array arr[], 
#   returns the maximum j – i such that
#   arr[j] > arr[i] */
def maxIndexDiff(arr, n):
     
    leftMin = [0]*n
    leftMin[0] = arr[0]
    for i in range(1,n):
        leftMin[i] = min(leftMin[i-1], arr[i])
         
    # leftMin[i] = min arr[0...i] 
    maxDist = - 2**32
    i = n-1
    j = n-1
     
    while(i>=0  and  j>=0):
         
        if(arr[j] >= leftMin[i]):
            maxDist = max(maxDist, j-i)
            i-=1
        else:
            j-=1
             
    return maxDist
 
# Driver Code
arr = [34,8,10,3,2,80,30,33,1]
n = len(arr)
maxDiff = maxIndexDiff(arr, n)
print(maxDiff)
 
# This code is contributed by Shubham Singh
#Output
#6
#Time Complexity: O(n) 
#Auxiliary Space: O(n) 

#Please suggest if someone has a better solution that is more efficient in terms of space and time.

#Another approch : Using Stack
#Idea is :

#1) First we do one traversal from left to right of arrray and store only those indexes  in stack whose array values appears in decreasing order in stack.. This is because, say if any value at i and j is satisfying our condition A[ i ]<=A[ j ] and if any index k that appears before ith index  i.e.  k<i and if  A[ k ]<= A[ i ] then value at kth index will also satisfy the condition A[k]<=A[ j ] . so we can ignore ith value .

#2) Now we simpaly traverse from right of array with index i and comapre it with the top of stack . 

#if we find A[stack.peek()] <=A [i] we pop from stack and compare with next value else we decrement our i counter

#at any point in loop if  A[stack.peek()] <=A [i]. We compute tempMax = i – stack.peeak(). And keep updating maxSofar result.

#below is the code for this Approach:

#include<bits/stdc++.h>
#using namespace std;
 
int maxIndexDiff(int A[], int N) {
     
    stack<int> stkForIndex;
     
    //loop for storing index in stack whose value appears in decreasing order
    for(int i=0;i<N;i++){           
        if(stkForIndex.empty() || A[stkForIndex.top()]>A[i])
            stkForIndex.push(i);
    }
 
    int maxDiffSoFar = 0;
    int tempdiff;
     
    //Now we traverse from right to left.
    int i = N-1;
    while(i>=0){
         
        /*
        This will compare top value of array at index stack top.
        if it satisfy our condition we check the difference  and update out result.
        else we decrement our counter
        */
        if(!stkForIndex.empty() && A[stkForIndex.top()] <= A[i]){
            tempdiff = i - stkForIndex.top();
            stkForIndex.pop();
            if(tempdiff>maxDiffSoFar){
                maxDiffSoFar  = tempdiff;
            }
            continue;
        }           
        i--;
    }
 
    return maxDiffSoFar;
     
    //This Code is Contributed by Ashwini Chourasia
}
     
int main() {
     
    int A[] = {34,8,10,3,2,80,30,33,1};       
    int N = sizeof(A) / sizeof(int);
    cout<<"Max diff be : " << maxIndexDiff(A, N);
}
#Output
#Max diff be : 6
#Time complexity: O(n),  As it requires two traversal  so TC is O(n) + O(n) = O(n)
#Auxiliary Space: O(n)  O(n) is its worst case complexity in case whole array is already sorted in decreasing order.Other wise it stores only those values which appears in decreasing order.
 