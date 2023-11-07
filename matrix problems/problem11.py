#Program to check idempotent matrix

#Difficulty Level : Easy

#Given a N * N matrix and the task is to check matrix is idempotent matrix or not.

#Idempotent matrix: A matrix is said to be idempotent matrix if matrix multiplied by itself return the same matrix. The matrix M is said to be idempotent matrix if and only if M * M = M. In idempotent matrix M is a square matrix.


#Examples: 

#Input : mat[][] = {{3, -6},
#                   {1, -2}};
#Output : Idempotent Matrix

#Input : mat[N][N] = {{2, -2, -4},
#                     {-1, 3, 4},
#                     {1, -2, -3}}
#Output : Idempotent Matrix.
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Implementation:

#C++
#Java
#Python 3
# Python Program to check given matrix
# is idempotent matrix or not.
import math
 
# Function for matrix multiplication.
def multiply(mat, res):
 
    N= len(mat)
    for i in range(0,N):
     
        for j in range(0,N):
         
            res[i][j] = 0
            for k in range(0,N):
                res[i][j] += mat[i][k] * mat[k][j]
 
# Function to check idempotent
# property of matrix.
def checkIdempotent(mat):
 
    N= len(mat)
    # Calculate multiplication of matrix
    # with itself and store it into res.
    res =[[0]*N for i in range(0,N)]
    multiply(mat, res)
 
    for i in range(0,N):
        for j in range(0,N):    
            if (mat[i][j] != res[i][j]):
                return False
    return True
 
# driver Function
mat = [ [2, -2, -4],
        [-1, 3, 4],
        [1, -2, -3] ]
     
# checkIdempotent function call.
if (checkIdempotent(mat)):
    print("Idempotent Matrix")
else:
    print("Not Idempotent Matrix.")
 
# This code is contributed by Gitanjali.
#C#
#Javascript
#Output
#Idempotent Matrix
#Time Complexity: O(n3)
#Auxiliary Space: O(n2), since n2 extra space has been taken.

