#Minimum number of jumps to reach end

#Difficulty Level : Medium
#-------------------------------------------------------------------------------
#Given an array arr[] where each element represents the max number of steps that can be made forward from that index. The task is to find the minimum number of jumps to reach the end of the array starting from index 0. If the end isn’t reachable, return -1.

#Examples: 

#Input: arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9}
#Output: 3 (1-> 3 -> 9 -> 9)
#Explanation: Jump from 1st element to 2nd element as there is only 1 step.
#Now there are three options 5, 8 or 9. I
#f 8 or 9 is chosen then the end node 9 can be reached. So 3 jumps are made.

#Input:  arr[] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
#Output: 10
#Explanation: In every step a jump is needed so the count of jumps is 10.

#-----------------------------------------------------------------
#Minimum number of jumps to reach the end using Recursion: 
#Start from the first element and recursively call for all the elements reachable from the first element. The minimum number of jumps to reach end from first can be calculated using the minimum value from the recursive calls. 

#minJumps(start, end) = Min ( minJumps(k, end) ) for all k reachable from start.

#Follow the steps mentioned below to implement the idea:



#Create a recursive function.
#In each recursive call get all the reachable nodes from that index.
#For each of the index call the recursive function.
#Find the minimum number of jumps to reach the end from current index.
#Return the minimum number of jumps from the recursive call.
#Below is the Implementation of the above approach:

# Python3 program to find Minimum
# number of jumps to reach end
 
# Returns minimum number of jumps
# to reach arr[h] from arr[l]
 
 
def minJumps(arr, l, h):
 
    # Base case: when source and
    # destination are same
    if (h == l):
        return 0
 
    # when nothing is reachable
    # from the given source
    if (arr[l] == 0):
        return float('inf')
 
    # Traverse through all the points
    # reachable from arr[l]. Recursively
    # get the minimum number of jumps
    # needed to reach arr[h] from
    # these reachable points.
    min = float('inf')
    for i in range(l + 1, h + 1):
        if (i < l + arr[l] + 1):
            jumps = minJumps(arr, i, h)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1
 
    return min
 
 
# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, 0, n-1))
 
# This code is contributed by Soumen Ghosh
#Output
#Minimum number of jumps to reach the end is 3
#Time complexity: O(nNn). 

#There are maximum n possible ways to move from an element. 
#So the maximum number of steps can be nn, Thus O(nn)
#Auxiliary Space: O(n). For recursion call stack. 
#------------------------------------------------------------------------

#Minimum number of jumps to reach end using Dynamic Programming from left to right:
#It can be observed that there will be overlapping subproblems. 

#For example in array, arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} minJumps(3, 9) will be called two times as arr[3] is reachable from arr[1] and arr[2]. So this problem has both properties (optimal substructure and overlapping subproblems) of Dynamic Programming

#Follow the below steps to implement the idea:

#Create jumps[] array from left to right such that jumps[i] indicate the minimum number of jumps needed to reach arr[i] from arr[0].
#To fill the jumps array run a nested loop inner loop counter is j and the outer loop count is i.
#Outer loop from 1 to n-1 and inner loop from 0 to i.
#If i is less than j + arr[j] then set jumps[i] to minimum of jumps[i] and jumps[j] + 1. initially set jump[i] to INT MAX
#Return jumps[n-1].
#Below is the implementation of the above approach:

# Python3 program to find Minimum
# number of jumps to reach end
 
# Returns minimum number of jumps
# to reach arr[n-1] from arr[0]
 
 
def minJumps(arr, n):
    jumps = [0 for i in range(n)]
 
    if (n == 0) or (arr[0] == 0):
        return float('inf')
 
    jumps[0] = 0
 
    # Find the minimum number of
    # jumps to reach arr[i] from
    # arr[0] and assign this
    # value to jumps[i]
    for i in range(1, n):
        jumps[i] = float('inf')
        for j in range(i):
            if (i <= j + arr[j]) and (jumps[j] != float('inf')):
                jumps[i] = min(jumps[i], jumps[j] + 1)
                break
    return jumps[n-1]
 
 
# Driver Program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
size = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, size))
 
# This code is contributed by Soumen Ghosh
#Output
#Minimum number of jumps to reach end is 3
#Thanks to paras for suggesting this method. 

#Time Complexity: O(n2) 
#Auxiliary Space: O(n), since n extra space has been taken.
#------------------------------------------------------------------
#Another implementation using Dynamic programming:

#Build jumps[] array from right to left such that jumps[i] indicate the minimum number of jumps needed to reach arr[n-1] from arr[i]. Finally, we return jumps[0]. Use Dynamic programming in a similar way of the above method.

#Below is the Implementation of the above approach:

# Python3 program to find Minimum
# number of jumps to reach end
 
# Returns Minimum number of
# jumps to reach end
 
 
def minJumps(arr, n):
 
    # jumps[0] will hold the result
    jumps = [0 for i in range(n)]
 
    # Minimum number of jumps needed
    # to reach last element from
    # last elements itself is always 0
    # jumps[n-1] is also initialized to 0
 
    # Start from the second element,
    # move from right to left and
    # construct the jumps[] array where
    # jumps[i] represents minimum number
    # of jumps needed to reach arr[m-1]
    # form arr[i]
    for i in range(n-2, -1, -1):
 
        # If arr[i] is 0 then arr[n-1]
        # can't be reached from here
        if (arr[i] == 0):
            jumps[i] = float('inf')
 
        # If we can directly reach to
        # the end point from here then
        # jumps[i] is 1
        elif (arr[i] >= n - i - 1):
            jumps[i] = 1
 
        # Otherwise, to find out the
        # minimum number of jumps
        # needed to reach arr[n-1],
        # check all the points
        # reachable from here and
        # jumps[] value for those points
        else:
            # initialize min value
            min = float('inf')
 
            # following loop checks with
            # all reachable points and
            # takes the minimum
            for j in range(i + 1, n):
                if (j <= arr[i] + i):
                    if (min > jumps[j]):
                        min = jumps[j]
 
            # Handle overflow
            if (min != float('inf')):
                jumps[i] = min + 1
            else:
                # or INT_MAX
                jumps[i] = min
 
    return jumps[0]
 
 
# Driver program to test above function
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, n-1))
 
# This code is contributed by Soumen Ghosh
#Output
#Minimum number of jumps to reach end is 3
#Time complexity: O(n2). Nested traversal of the array is needed.
#Auxiliary Space: O(n). To store the DP array linear space is needed.

#Minimum number of jumps to reach end | Set 2 (O(n) solution)
#Thanks to Ashish for suggesting this solution.
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.