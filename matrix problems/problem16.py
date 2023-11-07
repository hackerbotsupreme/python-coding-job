#Program for addition of two matrices

#Difficulty Level : Basic


#Given two N x M matrices. Find a N x M matrix as the sum of given matrices each value at the sum of values of corresponding elements of the given two matrices. 



#Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.
#Approach: Below is the idea to solve the problem.

#Iterate over every cell of matrix (i, j), add the corresponding values of the two matrices and store in a single matrix i.e. the resultant matrix.

#Follow the below steps to Implement the idea:

#Initialize a resultant matrix res[N][M].
#Run a for loop for counter i as each row and in each iteration:
#Run a for loop for counter j as each column and in each iteration:
#Add values of the two matrices for index i, j and store in res[i][j].
#Return res.
#Below is the Implementation of above approach.

#C++
#C
#Java
#Python3
# Python3 program for addition
# of two matrices
 
N = 4
 
# This function adds A[][]
# and B[][], and stores
# the result in C[][]
 
 
def add(A, B, C):
 
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] + B[i][j]
 
 
# driver code
A = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
 
B = [[1, 1, 1, 1],
     [2, 2, 2, 2],
     [3, 3, 3, 3],
     [4, 4, 4, 4]]
 
C = A[:][:]  # To store result
 
add(A, B, C)
 
print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(C[i][j], " ", end='')
    print()
 
# This code is contributed
# by Anant Agarwal.
C#
#PHP
#Javascript
#Output


#Result matrix is 
#2 2 2 2 
#4 4 4 4 
#6 6 6 6 
#8 8 8 8 
#Time complexity: O(n2). 
#Auxiliary space: O(n2).  since n2 extra space has been taken for storing results
#The program can be extended for rectangular matrices. The following post can be useful for extending this program. 

#How to pass a 2D array as a parameter in C?





Like
12
Previous
Different Operations on Matrices
Next
Program for subtraction of matrices
Related Articles
1.
C++ Program For Addition of Two Matrices
2.
Program to multiply two matrices
3.
Program to check if two given matrices are identical
4.
Python program to add two Matrices
5.
Python program to multiply two matrices
6.
Java Program to Multiply two Matrices of any size
7.
Java Program to Add two Matrices
8.
Program to concatenate two given Matrices of same size
9.
C Program to multiply two matrices
10.
Java Program to multiply two matrices
