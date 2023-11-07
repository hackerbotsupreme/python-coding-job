#Program to check diagonal matrix and scalar matrix

#Difficulty Level : Easy
Diagonal matrix
A square matrix is said to be a diagonal matrix if the elements of the matrix except the main diagonal are zero. A square null matrix is also a diagonal matrix whose main diagonal elements are zero. 

Examples: 

Input: 
Mat[4][4] = {{4, 0, 0, 0},
             {0, 5, 0, 0},
             {0, 0, 2, 0},
             {0, 0, 0, 1}}
Output: Yes

Input:
Mat[4][4] = {{6, 10, 12, 0},
             {0, 5, 0, 0},
             {0, 0, 9, 0},
             {0, 0, 0, 1}}
Output: No
Below is the implementation:

CPP
Java
Python3
# Python3 Program to check if matrix
# is diagonal matrix or not.
 
N = 4
 
# Function to check matrix
# is diagonal matrix
# or not.  
def isDiagonalMatrix(mat) :
    for i in range(0, N):
        for j in range(0, N) :
             
            # condition to check
            # other elements
            # except main diagonal
            # are zero or not.
            if ((i != j) and
             (mat[i][j] != 0)) :
                return False
 
    return True
 
 
# Driver function
mat = [[ 4, 0, 0, 0 ],
       [ 0, 7, 0, 0 ],
       [ 0, 0, 5, 0 ],
       [ 0, 0, 0, 1 ]]
 
if (isDiagonalMatrix(mat)) :
    print("Yes")
else :
    print("No")
     
     
# This code is contributed by Nikita Tiwari.
C#
PHP
Javascript
Output
Yes
Time Complexity: O(N2), where N represents the number of rows and columns of the given matrix.
Auxiliary Space: O(1), no extra space is required, so it is a constant.

Scalar matrix
A square matrix is said to be a scalar matrix if all the main diagonal elements are equal and other elements except main diagonal are zero. The scalar matrix can also be written in form of n * I, where n is any real number and I is the identity matrix. 

Examples: 



Input:
Mat[4][4] = {{4, 0, 0, 0},
             {0, 4, 0, 0},
             {0, 0, 4, 0},
             {0, 0, 0, 4}} 
Output: Yes

Input:
Mat[4][4] = {{4, 0, 0, 0},
             {0, 4, 0, 0},
             {0, 0, 1, 0},
             {0, 0, 0, 4}} 
Output: No
Below is the implementation:

CPP
Java
Python3
# Program to check matrix
# is scalar matrix or not.
 
 
N = 4
 
# Function to check matrix is
# scalar matrix or not.
def isScalarMatrix(mat) :
     
    # Check all elements
    # except main diagonal are
    # zero or not.
    for i in range(0,N) :
        for j in range(0,N) :
            if ((i != j)
               and (mat[i][j] != 0)) :
                return False
  
    # Check all diagonal
    # elements are same or not.
    for i in range(0,N-1) :
        if (mat[i][i] !=
           mat[i + 1][i + 1]) :
            return False
 
    return True
 
 
# Driver function
mat = [[ 2, 0, 0, 0 ],
       [ 0, 2, 0, 0 ],
       [ 0, 0, 2, 0 ],
       [ 0, 0, 0, 2 ]]
 
# Function call
if (isScalarMatrix(mat)):
    print("Yes")
else :
    print("No")
     
     
# This code is contributed by
# Nikita tiwari.
#C#
#PHP
#Javascript
#Output
#Yes
#Time Complexity: O(N2), where N represents the number of rows and columns of the given matrix.
#Auxiliary Space: O(1), no extra space is required, so it is a constant.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems
