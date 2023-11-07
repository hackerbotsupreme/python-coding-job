#Program to multiply two matrices

#Difficulty Level : Medium
#Last Updated : 12 Dec, 2022
#Read
#Discuss
#Courses
#Practice
#Video
#Given two matrices, the task is to multiply them. Matrices can either be square or rectangular:

#Examples: 

#(Square Matrix Multiplication)#

#Input: mat1[m][n] = { {1, 1}, {2, 2} }
#mat2[n][p] = { {1, 1}, {2, 2} }
#Output: result[m][p] = { {3, 3}, {6, 6} }#

#(Rectangular Matrix Multiplication)#

#Input: mat1[3][2] = { {1, 1}, {2, 2}, {3,# 3} }
#mat2[2][3] = { {1, 1, 1}, {2, 2, 2} }
#Output: result[3][3] = { {3, 3, 3}, {6, 6, 6}, {9, 9, 9} }
##
#



#Recommended Practice
#Multiply 2 matrices
#Try It!
##Multiplication of two Square or Rectangular Matrices:
#The number of columns in Matrix-1 must be equal to the number of rows in Matrix-2.
#Output of multiplication of Matrix-1 and Matrix-2, results with equal to the number of rows of Matrix-1 and  the number of columns of Matrix-2 i.e. rslt[R1][C2]
#Below is the implementation of the multiplication of two matrices:#

##C
#C++
#Java
#Pyt#hon3
# P#ython3 program to multiply two matrices
# 
# 
def mulMat(mat1, mat2, R1, R2, C1, C2):
    # List to store matrix multiplication result
    rslt = [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
 
    for i in range(0, R1):
        for j in range(0, C2):
            for k in range(0, R2):
                rslt[i][j] += mat1[i][k] * mat2[k][j]
 
    print("Multiplication of given two matrices is:")
    for i in range(0, R1):
        for j in range(0, C2):
            print(rslt[i][j], end=" ")
        print("\n", end="")
 
 
# Driver code
if __name__ == '__main__':
    R1 = 2
    R2 = 2
    C1 = 2
    C2 = 2
     
    # First matrix. M is a list
    mat1 = [[1, 1],
           [2, 2]]
     
   
    # Second matrix. N is a list
    mat2 = [[1, 1],
           [2, 2]]
 
    if C1 != R2:
        print("The number of columns in Matrix-1  must be equal to the number of rows in " + "Matrix-2", end='')
        print("\n", end='')
        print("Please update MACROs according to your array dimension in #define section", end='')
        print("\n", end='')
    else:
        # Call matrix_multiplication function
        mulMat(mat1, mat2, R1, R2, C1, C2)
 
# This code is contributed by Aarti_Rathi
#C#
#Jav#ascript
#Output
#Multiplication of given two matrices is:
#3    3    
#6    6    
#Time complexity: O(R1 * C2 * R2) for given matrices mat1[R1][C1] and mat2[R2][C2]
#Auxiliary space: O(R1 * C2)

#Multiplication of Rectangular Matrices using Pointers in C/C++: 
#To solve the problem follow the below idea:

#We use pointers in C/C++ to multiply matrices

#Prerequisite:  How to pass a 2D array as a parameter in C? 

#Below is the implementation of the above approach:

#C++
#C
#Java
#Python3
# Python program to multiply two
# rectangular matrices
 
# Multiplies two matrices mat1[][]
# and mat2[][] and prints result.
# (m1) x (m2) and (n1) x (n2) are
# dimensions of given matrices.
def multiply(m1, m2, mat1, n1, n2, mat2):
    res = [[0 for x in range(n2)] for y in range(m1)]
    for i in range(m1):
        for j in range(n2):
            res[i][j] = 0
            for x in range(m2):
                res[i][j] += mat1[i][x] * mat2[x][j]
    for i in range(m1):
        for j in range(n2):
            print(res[i][j], end=" ")
        print()
 
# Driver code
m1 = 2
m2 = 2
n1 = 2
n2 = 2
mat1 = [[1, 1], [2, 2]]
mat2 = [[1, 1], [2, 2]]
 
# Function call
multiply(m1, m2, mat1, n1, n2, mat2)
 
# This code is contributed by Tapesh(tapeshdua420)
#C#
#Javascript
#Output
#3 3 
#6 6 
#Time complexity: O(N3)
#Auxiliary Space: O(M1 * N2)

#Related Article: Strassen’s Matrix Multiplication

#This article is contributed by Aditya Ranjan. If you like GeeksforGeeks and would like to contribute, you can also write an article using contribute.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.





#Like
#45
#Previous
#Matrix Multiplication | Recursive
#Next
#Divide and Conquer | Set 5 (Strassen's Matrix Multiplication)
#Related Articles
#1.
#Python program to multiply two matrices
#2.
#Java Program to Multiply two Matrices of any size
#3.
#C Program to multiply two matrices
#4.
#Java Program to multiply two matrices
#5.
#Python Program to multiply two matrices
#6.
#Php Program to multiply two matrices
#7.
#Javascript Program to multiply two matrices
#8.
#C++ Program to Multiply Two Matrices
#9.
#C Program to Multiply two Floating Point Numbers
#10.
#Program to multiply two Matrix by taking data from user