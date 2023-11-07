#Maximum sum rectangle in a 2D matrix | DP-27

#Difficulty Level : Hard
#Last Updated : 12 Sep, 2022
#Read
#Discuss(30)
#ourses
#Practice
#Video
#Given a 2D array, find the maximum sum submatrix in it. For example, in the following 2D array, the maximum sum submatrix is highlighted with blue rectangle and sum of all elements in this submatrix is 29.



#This problem is mainly an extension of Largest Sum Contiguous Subarray for 1D array.  

#Recommended Problem
#Maximum sum Rectangle
#prefix-sum
##Matrix
#+3 more
#Flipkart
#Accolite
#+5 more
#Solve Problem
#Submission count: 29.5K
#The Naive Solution for this problem is to check every possible rectangle in the given 2D array. This solution requires 6 nested loops –  

#4 for start and end coordinate of the 2 axis O(n4)
#and 2 for the summation of the sub-matrix O(n2).
#The overall time complexity of this solution would be O(n6).

#Efficient Approach – 

#Kadane’s algorithm for 1D array can be used to reduce the time complexity to O(n^3). The idea is to fix the left and right columns one by one and find the maximum sum contiguous rows for every left and right column pair. We basically find top and bottom row numbers (which have maximum sum) for every fixed left and right column pair. To find the top and bottom row numbers, calculate the sum of elements in every row from left to right and store these sums in an array say temp[]. So temp[i] indicates sum of elements from left to right in row i. If we apply Kadane’s 1D algorithm on temp[], and get the maximum sum subarray of temp, this maximum sum would be the maximum possible sum with left and right as boundary columns. To get the overall maximum sum, we compare this sum with the maximum sum so far.



#Implementation:

#C++
#C
#Java
#Python3
# Python3 program to find maximum sum
# subarray in a given 2D array
 
# Implementation of Kadane's algorithm
# for 1D array. The function returns the
# maximum sum and stores starting and
# ending indexes of the maximum sum subarray
# at addresses pointed by start and finish
# pointers respectively.
 
 
def kadane(arr, start, finish, n):
 
    # initialize sum, maxSum and
    Sum = 0
    maxSum = -999999999999
    i = None
 
    # Just some initial value to check
    # for all negative values case
    finish[0] = -1
 
    # local variable
    local_start = 0
 
    for i in range(n):
        Sum += arr[i]
        if Sum < 0:
            Sum = 0
            local_start = i + 1
        elif Sum > maxSum:
            maxSum = Sum
            start[0] = local_start
            finish[0] = i
 
    # There is at-least one
    # non-negative number
    if finish[0] != -1:
        return maxSum
 
    # Special Case: When all numbers
    # in arr[] are negative
    maxSum = arr[0]
    start[0] = finish[0] = 0
 
    # Find the maximum element in array
    for i in range(1, n):
        if arr[i] > maxSum:
            maxSum = arr[i]
            start[0] = finish[0] = i
    return maxSum
 
# The main function that finds maximum
# sum rectangle in M[][]
 
 
def findMaxSum(M):
    global ROW, COL
 
    # Variables to store the final output
    maxSum, finalLeft = -999999999999, None
    finalRight, finalTop, finalBottom = None, None, None
    left, right, i = None, None, None
 
    temp = [None] * ROW
    Sum = 0
    start = [0]
    finish = [0]
 
    # Set the left column
    for left in range(COL):
 
        # Initialize all elements of temp as 0
        temp = [0] * ROW
 
        # Set the right column for the left
        # column set by outer loop
        for right in range(left, COL):
 
            # Calculate sum between current left
            # and right for every row 'i'
            for i in range(ROW):
                temp[i] += M[i][right]
 
            # Find the maximum sum subarray in
            # temp[]. The kadane() function also
            # sets values of start and finish.
            # So 'sum' is sum of rectangle between
            # (start, left) and (finish, right) which
            # is the maximum sum with boundary columns
            # strictly as left and right.
            Sum = kadane(temp, start, finish, ROW)
 
            # Compare sum with maximum sum so far.
            # If sum is more, then update maxSum
            # and other output values
            if Sum > maxSum:
                maxSum = Sum
                finalLeft = left
                finalRight = right
                finalTop = start[0]
                finalBottom = finish[0]
 
    # Prfinal values
    print("(Top, Left)", "(", finalTop,
          finalLeft, ")")
    print("(Bottom, Right)", "(", finalBottom,
          finalRight, ")")
    print("Max sum is:", maxSum)
 
 
# Driver Code
ROW = 4
COL = 5
M = [[1, 2, -1, -4, -20],
     [-8, -3, 4, 2, 1],
     [3, 8, 10, 1, 3],
     [-4, -1, 1, 7, -6]]
 
# Function call
findMaxSum(M)
 
# This code is contributed by PranchalK
#C#
#Javascript
#Output
#(Top, Left) (1, 1)
#(Bottom, Right) (3, 3)
#Max sum is: 29
#Time Complexity: O(c*c*r), where c represents the number of columns and r represents the number of rows in the given matrix.
#Auxiliary Space: O(r), where r represents the number of rows in the given matrix.

#Recommended Practice
#Maximum sum Rectangle
#Try It!




#Like
#115
#Previous
#Given an n x n square matrix, find sum of all sub-squares of size k x k
#Next
#Count pairs with given sum
#Related Articles
#1.
#Largest subset of rectangles such that no rectangle fit in any other rectangle
#2.
#Maximum sum not exceeding K possible for any rectangle of a Matrix
#3.
#Maximum size rectangle binary sub-matrix with all 1s
#4.
#Maximum size rectangle binary sub-matrix with all 1s | Set 2
#5.
#Find if there is a rectangle in binary matrix with corners as 1
#6.
#Form a Rectangle from boundary elements of Matrix using Linked List
#7.
#Maximum area rectangle by picking four sides from array
#8.
#Rectangle with Maximum Area using Java Pair
#9.
#Sum of Area of all possible square inside a rectangle
#10.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#Article Contributed By :
#https://media.geeksforgeeks.org/auth/avatar.png
#GeeksforGeeks
#Vote for difficulty
#Current difficulty : Hard
#Easy
#Normal
#Medium
#Hard
#Expert
#Improved By :
#Gaurav Kumar 33
#princiraj1992
#PranchalKatiyar
#rathbhupendra
#tonyshen
#kushagra98
#uchiha1101
#rutvik_56
#samim2000
#hardikkoriintern
#prashobh4657
#Article Tags :
#Accolite
#Amazon
#FactSet
#Samsung
#Arrays
#Dynamic Programming
#Matrix
##Misc
#Practice Tags :
#Accolite
##Amazon
#FactSet
#Misc
#Samsung
#Arrays
#Dynamic Programming
#Matrix
#Misc
##Improve Article
#Report Issue