#Program for Identity Matrix

#Difficulty Level : Easy

#Introduction to Identity Matrix :

# The dictionary definition of an Identity Matrix is a square matrix in which all the elements of the principal or main diagonal are 1’s and all other elements are zeros. In the below image, every matrix is an Identity Matrix. 
 



#In linear algebra, this is sometimes called as a Unit Matrix, of a square matrix (size = n x n) with ones on the main diagonal and zeros elsewhere. The identity matrix is denoted by “ I “. Sometimes U or E is also used to denote an Identity Matrix. 


#A property of the identity matrix is that it leaves a matrix unchanged if it is multiplied by an Identity Matrix.

#Examples:  

#Input  : 2
#Output : 1 0
#         0 1

#Input :  4
#Output : 1 0 0 0
#         0 1 0 0
#         0 0 1 0
#         0 0 0 1
#The explanation is simple. We need to make all
#the elements of principal or main diagonal as 
#1 and everything else as 0.
#Program to print Identity Matrix: The logic is simple. You need to print 1 in those positions where row is equal to the column of a matrix and make all other positions as 0. 



#Implementation

#C++
#C
#Java
#Python3
# Python code to print identity matrix
 
# Function to print identity matrix
def Identity(size):
    for row in range(0, size):
        for col in range(0, size):
 
            # Here end is used to stay in same line
            if (row == col):
                print("1 ", end=" ")
            else:
                print("0 ", end=" ")
        print()
 
# Driver Code       
size = 5
Identity(size)
#C#
#PHP
#Javascript
#Output
#1 0 0 0 0 
#0 1 0 0 0 
#0 0 1 0 0 
#0 0 0 1 0 
#0 0 0 0 1 
#Time Complexity: O(row x col)
#Auxiliary Space: O(1), as no extra space is used
 
#Program to check if a given square matrix is Identity Matrix : 

#C++
#C
#Java
#Python3
# Python3 program to check
# if a given matrix is identity
#MAX = 100;
def isIdentity(mat, N):
    for row in range(N):
        for col in range(N):
            if (row == col and
                mat[row][col] != 1):
                return False;
            elif (row != col and
                  mat[row][col] != 0):
                return False;
    return True;
 
# Driver Code
#N = 4;
mat = [[1, 0, 0, 0],
       [0, 1, 0, 0],
       [0, 0, 1, 0],
       [0, 0, 0, 1]];
if (isIdentity(mat, N)):
    print("Yes ");
else:
    print("No ");
 
# This code is contributed
# by mits
#C#
#PHP
#Javascript
#Output
#Yes 
#Time Complexity: O(row x col)
#Auxiliary Space: O(1), as no extra space is used

#This article is contributed by Aarti_Rathi. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above. 

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems


#Previous
#Program to check if matrix is lower triangular
#Next
#C Program To Check whether Matrix is Skew Symmetric or not
#Related Articles
#1.
#C++ Program for Identity Matrix
#2.
#C Program for Identity Matrix
#3.
#Java Program for Identity Matrix
#4.
#Php Program for Identity Matrix
#5.
#Python Program for Identity Matrix
#6.
#Significance of Pascal’s Identity
#7.
#Cassini’s Identity
#8.
#Euler's Four Square Identity
#9.
#Brahmagupta Fibonacci Identity
#10.
#Proizvolov's Identity
