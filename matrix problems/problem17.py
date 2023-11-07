#Program for subtraction of matrices

#Difficulty Level : Basic

#The below program subtracts of two square matrices of size 4*4, we can change N for a different dimension. 

#Implementation:

#C++
#C
#Java
#Python3
# Python 3 program for subtraction
# of matrices
 
N = 4
 
# This function returns 1
# if A[][] and B[][] are identical
# otherwise returns 0
def subtract(A, B, C):
     
    for i in range(N):
        for j in range(N):
            C[i][j] = A[i][j] - B[i][j]
 
# Driver Code
A = [ [1, 1, 1, 1],
      [2, 2, 2, 2],
      [3, 3, 3, 3],
      [4, 4, 4, 4]]
 
B = [ [1, 1, 1, 1],
      [2, 2, 2, 2],
      [3, 3, 3, 3],
      [4, 4, 4, 4]]
                     
C = A[:][:] # To store result
     
subtract(A, B, C)
 
print("Result matrix is")
for i in range(N):
    for j in range(N):
        print(C[i][j], " ", end = '')
    print()
     
# This code is contributed
# by Anant Agarwal.
C#
#PHP
#Javascript
#Output
#Result matrix is 
#0 0 0 0 
#0 0 0 0 
#0 0 0 0 
#0 0 0 0 
#Note – The number at 0th row and 0th column of first matrix gets subtracted with number at 0th row and 0th column of second matrix. And its subtraction result gets initialized as the value of 0th row and 0th column of resultant matrix. Same subtraction process applied for all the elements

#The program can be extended for rectangular matrices. The following post can be useful for extending this program. 
#How to pass a 2D array as a parameter in C?

#Time complexity: O(n2). 
#Auxiliary space:O(n2). since n2 extra space has been taken.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems




#Like
#6
#Previous
#Program for addition of two matrices
#Next
#Program to find transpose of a matrix
#Related Articles
#1.
#Addition and Subtraction of Matrix using pthreads
#2.
#Subtraction of two numbers using 2's Complement
#3.
#Subtraction of two large numbers using 9's complement
#4.
#Subtraction of two large numbers using 10's complement
#5.
#Program to multiply two matrices
#6.
#Program for addition of two matrices
#7.
#Program to check if two given matrices are identical
#8.
#Python program to add two Matrices
#9.
#Python program to multiply two matrices
#10.
#Java Program to Multiply two Matrices of any size