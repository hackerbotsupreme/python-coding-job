#Rotate a matrix by 90 degree without using any extra space | Set 2

#Difficulty Level : Medium

#Given a square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.
#
#Examples: 
#
#Input:
# 1  2  3
# 4  5  6
# 7  8  9
#Output:
# 3  6  9 
# 2  5  8 
# 1  4  7 
#Rotated the input matrix by
#90 degrees in anti-clockwise direction.#

##Input:
## 1  2  3  4 
## 5  6  7  8 
# 9 10 11 12 
##13 14 15 16 
#Output:
## 4  8 12 16 
## 3  7 11 15 
## 2  6 10 14 
 1  5  9 13
#Rotated the input matrix by
#90 degrees in anti-clockwise direction.
##Recommended Problem
#Rotate by 90 degree
#Matrix
#Data Structures
##Paytm
#Zoho
##+6 more
##Solve Problem
##Submission count: 28.8K
#An approach that requires extra space is already discussed in a different article: 
##Inplace rotate square matrix by 90 degrees | Set 1##

##This post discusses the same problem with a different approach which is space-optimized.
#Approach: The idea is to find the transpose of the matrix and then reverse the columns of the transposed matrix. 
#Here is an example to show how this works. ##

##

#Algorithm:  #
#
#To solve the given problem there are two tasks. 1st is finding the transpose and the second is reversing the columns without using extra space
#A transpose of a matrix is when the matrix is flipped over its diagonal, i.e the row index of an element becomes the column index and vice versa. So to find the transpose interchange of the elements at position (i, j) with (j, i). Run two loops, the outer loop from 0 to row count and the inner loop from 0 to the index of the outer loop.
#To reverse the column of the transposed matrix, run two nested loops, the outer loop from 0 to column count and the inner loop from 0 to row count/2, interchange elements at (i, j) with (i, row[count-1-j]), where i and j are indices of inner and outer loop respectively.
#Implementation#:#


#
#C++
#Java
#C#
#Python3
## Python 3 program for left rotation of matrix by 90
## degree without using extra space
# 
#R = 4
#C = 4
# 
### After transpose we swap elements of column
# one by one for finding left rotation of matrix
# by 90 degree
 
# 
#def reverseColumns(arr):
#    for i in range(C):
#        j = 0
#        k = C-1
#        while j < k:
#            t = arr[j][i]
#            arr[j][i] = arr[k][i]
#            arr[k][i] = t
#            j += 1
##            k -= 1
 
# Function for do transpose of matrix
 
# 
#def transpose(arr):
#    for i in range(R):
#        for j in range(i, C):
#            t = arr[i][j]
#            arr[i][j] = arr[j][i]
#            arr[j][i] = t
# 
## Function for print matrix
# 
## 
#def printMatrix(arr):
#    for i in range(R):
#        for j in range(C):
##            print(str(arr[i][j]), end=" ")
#        print()
# 
# Function to anticlockwise rotate matrix
## by 90 degree
# 
# 
#def rotate90(arr):
#    transpose(arr)
#    reverseColumns(arr)
# 
# 
## Driven code
#arr = [[1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12],
##       [13, 14, 15, 16]
#       ]
#rotate90(arr)
#printMatrix(arr)
##PHP
#Javascript
#Output
#4 8 12 16 
#3 7 11 15 
#2 6 10 14 
##1 5 9 13 
#Complexity Analysis: 

#Time Complexity: O(R*#C). 
#The matrix is traversed twice, so the complexity is O(R*C).
#Auxiliary Space: O(1). 
#The space complexity is constant as no extra space is required.
#Another Approach usin#g a single traversal of the matrix :#

#The idea is to traver#se along the boundaries of the matri#x and shift the positions of the elements in 900 anticlockwise directions in each boundary. There are such (n/2-1) boundaries in the matrix.

#Algorithm:## 

#Iterate ov##er all the boundaries in the matrix. There are total (n/2-1) boundaries
#For each boundary take the 4 corner elements and swap them such that the 4 corner elements get rotated in anticlockwise directions. Then take the next 4 elements along the edges(left, right, top, bottom) and swap them in an anticlockwise direction. Continue as long as all the elements in that particular boundary get rotated in 900 anticlockwise directions.
#Then move ##on to the next inner boundary and continue the process as long the whole matrix is rotated in 900 anticlockwise direction.##

#Original a#rray
###

#to#tal n/2-1 boundaries


#fo#r outermost boundary


#fo#r next inner boundary

# Implementation:#
#
#C++14
#Java
#Python3
## Function to rotate matrix anticlockwise by 90 degrees.
#def rotateby90(arr):
# 
#    n = len(arr)
#    a,b,c,d = 0,0,0,0
# 
#    # iterate over all the boundaries of the matrix
#    for i in range(n // 2):
# 
#        # for each boundary, keep on taking 4 elements
#        # (one each along the 4 edges) and swap them in
#        # anticlockwise manner
#        for j in range(n - 2 * i - 1):
#            a = arr[i + j][i]
#            b = arr[n - 1 - i][i + j]
#            c = arr[n - 1 - i - j][n - 1 - i]
#            d = arr[i][n - 1 - i - j]
# 
#            arr[i + j][i] = d
#            arr[n - 1 - i][i + j] = a
#            arr[n - 1 - i - j][n - 1 - i] = b
#            arr[i][n - 1 - i - j] = c
             
 
# Function for print matrix
#def printMatrix(arr):
# 
#    for i in range(len(arr)):
#            for j in range(len(arr[0])):
#                print(arr[i][j] ,end = " ")
#            print()
#     
# 
## Driver program to test above function
#arr=[[ 1, 2, 3, 4 ],
#     [ 5, 6, 7, 8 ],
#     [ 9, 10, 11, 12 ],
#     [ 13, 14, 15, 16 ]]
#rotateby90(arr)
#printMatrix(arr)
# 
## this code is contributed by shinjanpatra
#C#
#Javascript
#Output
#4 8 12 16 
#3 7 11 15 
#2 6 10 14 
#1 5 9 13 
#Complexity Analysis: #

#Time Complexity: O(R*C). The matrix is traversed only once, so the time complexity is O(R*C).
#Auxiliary Space: O(1). The space complexity is O(1) as no extra space is required.#

#Implementation: Let’s see a method of Python numpy that can be used to arrive at the particular solution. #

#Python3
## Alternative implementation using numpy
#import numpy
 
## Driven code
#arr = [[1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12],
#       [13, 14, 15, 16]
#       ]
## 
### Define flip algorithm (Note numpy.flip is a builtin f
## function for versions > v.1.12.0)
# 
# 
#def flip(m, axis):
#    if not hasattr(m, 'ndim'):
#        m = asarray(m)
#    indexer = [slice(None)] * m.ndim
#    try:
##        indexer[axis] = slice(None, None, -1)
##    except IndexError:
#        raise ValueError("axis =% i is invalid for the % i-dimensional input array"
#                         % (axis, m.ndim))
#    return m[tuple(indexer)]
 
 
# Transpose the matrix
#trans = numpy.transpose(arr)
 
## Flip the matrix anti-clockwise (1 for clockwise)
#flipmat = flip(trans, 0)
# 
##print("\nnumpy implementation\n")
#print(flipmat)
#Output:  ##

#numpy implementation#

#[[ 4  8 12 16]
# [ 3  7 11 15]
# [ 2  6 10 14]
# [ 1  5  9 13]]
#Note: The above steps/programs do left (or anticlockwise) rotation. Let’s see how to do the right rotation or clockwise rotation. The approach would be similar. Find the transpose of the matrix and then reverse the rows of the transposed matrix. 
#This is how it is done. ##



#This article is contributed by DANISH_RAZA . If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.

#Rotating Along the Boundaries

#We can start at the first 4 corners of the given matrix and then keep incrementing the row and column indices to moves around.

#At any given moment we will have four corners lu (left-up),ld(left-down),ru(right-up),rd(right-down).

#To left rotate we will first swap the ru and ld,  then lu and ld and lastly ru and rd.

#ru	 	lu
# 	 	 
#rd	 	ld
#Implementation:#

#C++
#Java
#C#
#Javascrip#t
#Python#3
# Func#tion to rotate matrix anticlockwise by 90 degrees.
#def rotateby90(arr):
# 
#    n = len(arr)
#    if(n%2 == 0):
#      #  mid = n//2-1
#    el#se:
#      #  mid = n/2
#    # 
#    j=n-1
#    # iterate over all the boundaries of the matrix
#    for i in range(mid+1):
         
#        for k in range(j-i):
     #       arr[i][j-k],arr[j][i+k] = arr[j][i+k],arr[i][j-k]
#            arr[i+k][i],arr[j][i+k] = arr[j][i+k],arr[i+k][i]
#            arr[i][j-k],arr[j-k][j] = arr[j-k][j],arr[i][j-k]
#             
#        j=j-1
             
 
# Function for print matrix
#def printMatrix(arr):
# 
#    for i in range(len(arr)):
#            for j in range(len(arr[0])):
#                print(arr[i][j] ,end = " ")
#            print()
     
 
# Driver program to test above function
#arr=[[ 1, 2, 3, 4 ],
#    [ 5, 6, 7, 8 ],
#    [ 9, 10, 11, 12 ],
#    [ 13, 14, 15, 16 ]]
#rotateby90(arr)
#printMatrix(arr)
 
# this code is contributed by CodeWithMini
#Output
#4 8 12 16 
#3 7 11 15 
#2 6 10 14 
#1 5 9 13 
#Time Complexity: O(n2)
#Auxiliary Space: O(1), since no extra space has been taken.





#Like
#72
#Previous
#Inplace rotate square matrix by 90 degrees | Set 1
#Next
#Rotate each ring of matrix anticlockwise by K elements
#Related Articles
#1.
#Rotate a matrix clockwise by 90 degree without using any extra space | Set 3
#2.
#Rotate a matrix by 90 degree in clockwise direction without using any extra space
#3.
#Rotate a Matrix by 180 degree
#4.
#C++ Program to Rotate a Matrix by 180 degree
#5.
#Java Program for Rotate a Matrix by 180 degree
#6.
#Python Program for Rotate a Matrix by 180 degree
#7.
#Javascript Program for Rotate a Matrix by 180 degree
#8.
##Print n x n spiral matrix using O(1) extra space
##9.
#Python3 Program to Inplace rotate square matrix by 90 degrees | Set 1
#10.
#Php Program to Inplace rotate square matrix by 90 degrees | Set #1