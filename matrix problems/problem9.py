#Squares of Matrix Diagonal Elements

#Difficulty Level : Basic

#You have given an integer matrix with odd dimensions. Find the square of the diagonal elements on both sides.

#Examples:

#Input  :  1 2 3
#         4 5 6
#         7 8 9
#Output :  Diagonal one: 1 25 81
#         Diagonal two: 9 25 49
#Input  :  2 5 7  
#         3 7 2
#         5 6 9
#Output :  Diagonal one : 4 49 81
#         Diagonal two : 49 49 25
#Method 1: Firstly we find the diagonal element of the matrix and then we print the square of that element.

#C++
#Java
#Python3
# Simple Python program
# to print squares
# of diagonal elements.
 
# function of diagonal square
def diagonalsquare(mat, row, column) :
 
    # This loop is for finding square
    # of first diagonal elements
    print ("Diagonal one : ", end = "")
    for i in range(0, row) :
        for j in range(0, column) :
 
            # if this condition will
            # become true then we will
            # get diagonal element
            if (i == j) :
                # printing square of
                # diagonal element
                print ("{} ".format(mat[i][j] *
                                    mat[i][j]), end = "")
 
    # This loop is for finding
    # square of second side
    # of diagonal elements
    print (" \nDiagonal two : ", end = "")
    for i in range(0, row) :
        for j in range(0, column) :
 
            # if this condition will become
            # true then we will get second
            # side diagonal element
            if (i + j == column - 1) :
 
                # printing square of diagonal
                # element
                print ("{} ".format(mat[i][j] *
                                    mat[i][j]), end = "")
 
 
# Driver code
mat = [[ 2, 5, 7 ],
        [ 3, 7, 2 ],
        [ 5, 6, 9 ]]
diagonalsquare(mat, 3, 3)
 
# This code is contributed by
# Manish Shaw(manishshaw1)
#C#
##PHP
##Javascript
#Output
#Diagonal one : 4 49 81  
#Diagonal two : 49 49 25 
#Time Complexity : O(n*n)
#Auxiliary Space: O(1)

#Method 2:
#An efficient solution is also the same as in the naive approach but in this, we are taking only one loop to find the diagonal element and then we print the square of that element.

#C++
#Java
#Python3
# Efficient Python program
# to print squares of
# diagonal elements.
 
# function of diagonal square
def diagonalsquare(mat, row,
                column) :
     
    # This loop is for finding
    # of square of the first
    # side of diagonal elements
    print ("Diagonal one : ",
                    end = "")
    for i in range(0, row) :
 
        # printing direct square
        # of diagonal element
        # there is no need to
        # check condition
        print (mat[i][i] *
            mat[i][i], end = " ")
     
 
    # This loop is for finding
    # square of the second side
    # of diagonal elements
    print ("\nDiagonal two : ",
                        end = "")
     
    for i in range(0, row) :   
         
        # printing direct square
        # of diagonal element in
        # the second side
        print (mat[i][row - i - 1] *
            mat[i][row - i - 1] ,
                        end = " ")
 
# Driver code
mat = [[2, 5, 7 ],
    [3, 7, 2 ],
    [5, 6, 9 ]]
diagonalsquare(mat, 3, 3)
     
# This code is contributed by
# Manish Shaw(manishshaw1)
#C#
#PHP
#Javascript
#Output


 
#Diagonal one : 4 49 81  
#Diagonal two : 49 49 25 
#Time Complexity: O(n)
#Auxiliary Space:  O(1)