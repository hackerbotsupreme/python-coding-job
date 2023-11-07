#Find the Missing Number

#Difficulty Level : Easy
#----------------------------------------------------------------------
#Given an array arr[] of size N-1 with integers in the range of [1, N], the task is to find the missing number from the first N integers.

#Note: There are no duplicates in the list.

#Examples: 

#Input: arr[] = {1, 2, 4, 6, 3, 7, 8}, N = 8
#Output: 5
#Explanation: The missing number between 1 to 8 is 5


#Input: arr[] = {1, 2, 3, 5}, N = 5
#Output: 4
#Explanation: The missing number between 1 to 5 is 4
#----------------------------------------------------------------------
#Complete Interview Preparation - GFG
#Approach 1 (Using Hashing): The idea behind the following approach is



#The numbers will be in the range (1, N), an array of size N can be maintained to keep record of the elements present in the given array

#Create a temp array temp[] of size n + 1 with all initial values as 0.
#Traverse the input array arr[], and do following for each arr[i] 
#if(temp[arr[i]] == 0) temp[arr[i]] = 1 
#Traverse temp[] and output the array element having value as 0 (This is the missing element).
#Below is the implementation of the above approach:

# Find Missing Element
def findMissing(arr, N):
   
    # create a list of zeroes
    temp = [0] * (N+1)
 
    for i in range(0, N):
        temp[arr[i] - 1] = 1
 
    for i in range(0, N+1):
        if(temp[i] == 0):
            ans = i + 1
 
    print(ans)
 
# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)
 
    # Function call
    findMissing(arr, N)
 
    # This code is contributed by nikhilm2302
#Output
#4
#Time Complexity: O(N)
#Auxiliary Space: O(N)
#---------------------------------------------------------------------
#Approach 2 (Using summation of first N natural numbers): The idea behind the approach is to use the summation of the first N numbers.

#Find the sum of the numbers in the range [1, N] using the formula N * (N+1)/2. Now find the sum of all the elements in the array and subtract it from the sum of the first N natural numbers. This will give the value of the missing element.


#Follow the steps mentioned below to implement the idea:

#Calculate the sum of the first N natural numbers as sumtotal= N*(N+1)/2.
#Traverse the array from start to end.
#Find the sum of all the array elements.
#Print the missing number as SumTotal – sum of array
#Below is the implementation of the above approach:

# Function to find the missing element
def getMissingNo(arr, n):
    total = (n + 1)*(n + 2)/2
    sum_of_A = sum(arr)
    return total - sum_of_A
 
# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)
     
    # Function call
    miss = getMissingNo(arr, N)
    print(miss)
     
# This code is contributed by Pratik Chhajer
#Output
#4
#Time Complexity: O(N)
#Auxiliary Space: O(1)
#----------------------------------------------------------------------
#Modification for Overflow: The approach remains the same but there can be an overflow if N is large. 

#In order to avoid integer overflow, pick one number from the range [1, N] and subtract a number from the given array (don’t subtract the same number twice). This way there won’t be any integer overflow.

#Algorithm: 

#Create a variable sum = 1 which will store the missing number and a counter variable c = 2.
#Traverse the array from start to end.
#Update the value of sum as sum = sum – array[i] + c and increment c by 1. This performs the task mentioned in the above idea]
#Print the missing number as a sum.
#Below is the implementation of the above approach:

# Function to get the missing number
def getMissingNo(a, n):
    i, total = 0, 1
 
    for i in range(2, n + 2):
        total += i
        total -= a[i - 2]
    return total
 
 
# Driver Code
if __name__ == '__main__':
    arr = [1, 2, 3, 5]
    N = len(arr)
 
    # Function call
    print(getMissingNo(arr, N))
 
# This code is contributed by Mohit kumar
#Output
#4
#Time Complexity: O(N).  Only one traversal of the array is needed.
#Auxiliary Space: O(1). No extra space is needed
#-----------------------------------------------------------------

#Approach 3 (Using binary operations): This method uses the technique of XOR to solve the problem.  

#XOR has certain properties 

#Assume a1 ⊕ a2 ⊕ a3 ⊕ . . . ⊕ an = a and a1 ⊕ a2 ⊕ a3 ⊕ . . . ⊕ an-1 = b
#Then a ⊕ b = an
#Follow the steps mentioned below to implement the idea:

#Create two variables a = 0 and b = 0
#Run a loop from i = 1 to N:
#For every index, update a as a = a ^ i
#Now traverse the array from i = start to end.
#For every index, update b as b = b ^ arr[i].
#The missing number is a ^ b.
#Below is the implementation of the above approach:

# Python3 program to find
# the missing Number
# getMissingNo takes list as argument
 
 
def getMissingNo(a, n):
    x1 = a[0]
    x2 = 1
 
    for i in range(1, n):
        x1 = x1 ^ a[i]
 
    for i in range(2, n + 2):
        x2 = x2 ^ i
 
    return x1 ^ x2
 
 
# Driver program to test above function
if __name__ == '__main__':
 
    arr = [1, 2, 3, 5]
    N = len(arr)
 
    # Driver code
    miss = getMissingNo(arr, N)
    print(miss)
 
# This code is contributed by Yatin Gupta
#Output
#4
#Time Complexity: O(N) 
#Auxiliary Space: O(1) 
#-------------------------------------------------------------
#Approach 4 (Using Cyclic Sort): The idea behind it is as follows:

#All the given array numbers are sorted and in the range of 1 to n-1. If the range is 1 to N  then the index of every array element will be the same as (value – 1).

#Follow the below steps to implement the idea:

#Use cyclic sort to sort the elements in linear time.
#Now traverse from i = 0 to the end of the array:
#If arr[i] is not the same as i+1 then the missing element is (i+1).
#If all elements are present then N is the missing element in the range [1, N].
#Below is the implementation of the above approach.

# Python3 program to check missingNo
 
# Function to find the missing number
def getMissingNo(arr, n) :
    i = 0;
     
    while (i < n) :
        # as array is of 1 based indexing so the
        # correct position or index number of each
        # element is element-1 i.e. 1 will be at 0th
        # index similarly 2 correct index will 1 so
        # on...
        correctpos = arr[i] - 1;
        if (arr[i] < n and arr[i] != arr[correctpos]) :
            # if array element should be lesser than
            # size and array element should not be at
            # its correct position then only swap with
            # its correct position or index value
            arr[i],arr[correctpos] = arr[correctpos], arr[i]
 
        else :
            # if element is at its correct position
            # just increment i and check for remaining
            # array elements
            i += 1;
             
    # check for missing element by comparing elements with their index values
    for index in range(n) :
        if (arr[index] != index + 1) :
            return index + 1;
             
    return n;
 
# Driver code
if __name__ == "__main__" :
    arr = [ 1, 2, 3, 5 ];
    N = len(arr);
    print(getMissingNo(arr, N));
 
 
    # This Code is Contributed by AnkThon
#Output
#4
#Time Complexity: O(N), requires (N-1) comparisons
#Auxiliary Complexity: O(1) 
#------------------------------------------------------------------
#Approach 5 (Use elements as Index and mark the visited places as negative): Use the below idea to get the approach

#Traverse the array. While traversing, use the absolute value of every element as an index and make the value at this index as negative to mark it visited. To find missing, traverse the array again and look for a positive value.

#Follow the steps to solve the problem:

#Traverse the given array
#If the absolute value of current element is greater than size of the array, then continue.
#else multiply the (absolute value of (current element) – 1)th index with -1.
#Initialize a variable ans = size + 1.
#Traverse the array and follow the steps:
#if the value is positive assign ans = index + 1
#Print ans as the missing value.
#Below is the implementation of the above approach:

# Function to get the missing number
def findMissing(a, size):
 
    for i in range(0, n):
        if (abs(arr[i]) - 1 == size):
            continue
 
        ind = abs(arr[i]) - 1
        arr[ind] *= -1
 
    ans = size + 1
    for i in range(0, n):
        if (arr[i] > 0):
            ans = i + 1
 
    print(ans)
 
# Driver Code
if __name__ == '__main__':
    arr = [1, 3, 7, 5, 6, 2]
    n = len(arr)
 
    # Function call
    findMissing(arr, n)
 
    # This code is contributed by aarohirai2616.
#Output
#4
#Time Complexity: O(N) 
#Auxiliary Space: O(1) 
#------------------------------------------------------------------
