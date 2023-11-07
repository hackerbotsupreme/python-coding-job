#Maximum size square sub-matrix with all 1s

#Difficulty Level : Medium
#Given a binary matrix, find out the maximum size square sub-matrix with all 1s. 
#For example, consider the below binary matrix. 

#maximum-size-square-sub-matrix-with-all-1s

#Recommended Problem
#Largest square formed in a matrix
#Dynamic Programming
#Algorithms
#Amazon
#Samsung
#Solve Problem
#Submission count: 59.4K
#Algorithm: 
#Let the given binary matrix be M[R][C]. The idea of the algorithm is to construct an auxiliary size matrix S[][] in which each entry S[i][j] represents the size of the square sub-matrix with all 1s including M[i][j] where M[i][j] is the rightmost and bottom-most entry in sub-matrix. 

#1) Construct a sum matrix S[R][C] for the given M[R][C].
#     a)    Copy first row and first columns as it is from M[][] to S[][]
#     b)    For other entries, use following expressions to construct S[][]
#         If M[i][j] is 1 then
#            S[i][j] = min(S[i][j-1], S[i-1][j], S[i-1][j-1]) + 1
#         Else /*If M[i][j] is 0*/
#            S[i][j] = 0
#2) Find the maximum entry in S[R][C]
#3) Using the value and coordinates of maximum entry in S[i], print 
#   sub-matrix of M[][]
#For the given M[R][C] in the above example, constructed S[R][C] would be:


#   0  1  1  0  1
#   1  1  0  1  0
#   0  1  1  1  0
#   1  1  2  2  0
#   1  2  2  3  1
#   0  0  0  0  0
#The value of the maximum entry in the above matrix is 3 and the coordinates of the entry are (4, 3). Using the maximum value and its coordinates, we can find out the required sub-matrix. 

#C++
#C
#Java
#Python3
# Python3 code for Maximum size
# square sub-matrix with all 1s
 
#def printMaxSubSquare(M):
#    R = len(M)  # no. of rows in M[][]
#    C = len(M[0])  # no. of columns in M[][]
 
#    S = []
#    for i in range(R):
#        temp = []
#        for j in range(C):
#            if i == 0 or j == 0:
#                temp += M[i][j],
#            else:
#                temp += 0,
#        S += temp,
#    # here we have set the first row and first column of S same as input matrix, other entries are set to 0
 
    # Update other entries
    for i in range(1, R):
        for j in range(1, C):
            if (M[i][j] == 1):
                S[i][j] = min(S[i][j-1], S[i-1][j],
                              S[i-1][j-1]) + 1
            else:
                S[i][j] = 0
 
    # Find the maximum entry and
    # indices of maximum entry in S[][]
    max_of_s = S[0][0]
    max_i = 0
    max_j = 0
    for i in range(R):
        for j in range(C):
            if (max_of_s < S[i][j]):
                max_of_s = S[i][j]
                max_i = i
                max_j = j
 
    print("Maximum size sub-matrix is: ")
    for i in range(max_i, max_i - max_of_s, -1):
        for j in range(max_j, max_j - max_of_s, -1):
            print(M[i][j], end=" ")
        print("")
 
 
# Driver Program
M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
 
printMaxSubSquare(M)
 
# This code is contributed by Soumen Ghosh

#Output
#Maximum size sub-matrix is: 
#1 1 1 
#1 1 1 
#1 1 1 
#Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the given matrix. 
#Auxiliary Space: O(m*n) where m is the number of rows and n is the number of columns in the given matrix. 
#Algorithmic Paradigm: Dynamic Programming



#Space Optimized Solution: In order to compute an entry at any position in the matrix we only need the current row and the previous row.

#C++
#Java
#Python3
# Python code for Maximum size square
# sub-matrix with all 1s
# (space optimized solution)
 
R = 6
C = 5
 
 
def printMaxSubSquare(M):
 
    global R, C
    Max = 0
 
    # set all elements of S to 0 first
    S = [[0 for col in range(C)]for row in range(2)]
 
    # Construct the entries
    for i in range(R):
        for j in range(C):
 
            # Compute the entrie at the current position
            Entrie = M[i][j]
            if(Entrie):
                if(j):
                    Entrie = 1 + min(S[1][j - 1], min(S[0][j - 1], S[1][j]))
 
            # Save the last entrie and add the new one
            S[0][j] = S[1][j]
            S[1][j] = Entrie
 
            # Keep track of the max square length
            Max = max(Max, Entrie)
 
    # Print the square
    print("Maximum size sub-matrix is: ")
    for i in range(Max):
        for j in range(Max):
            print("1", end=" ")
        print()
 
 
# Driver code
M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]
 
printMaxSubSquare(M)
 
# This code is contributed by shinjanpatra

#Maximum size sub-matrix is: 
#1 1 1 
#1 1 1 
#1 1 1 
#Time Complexity: O(m*n) where m is the number of rows and n is the number of columns in the given matrix. 
#Auxiliary space: O(n) where n is the number of columns in the given matrix. 

#Please write comments if you find any bug in the above code/algorithm, or find other ways to solve the same problem





#Like
#164
#Previous
#Maximum size rectangle binary sub-matrix with all 1s
#Next
#Submatrix Sum Queries
#Related Articles
#1.
#Minimum area such that all submatrix of the size have same maximum value
#2.
#Find Maximum Length Of A Square Submatrix Having Sum Of Elements At-Most K
#3.
#Largest possible square submatrix with maximum AND value
#4.
#Submatrix of given size with maximum 1's
#35.
#Check if a matrix contains a square submatrix with 0 as boundary element
#6.
#Maximum size of square such that all submatrices of that size have sum less than K
#7.
#Minimum operations to convert Binary Matrix A to B by flipping submatrix of size K
#8.
#Smallest submatrix with Kth maximum XOR
#9.
#Maximum value in a matrix which contain intersecting concentric submatrix
#10.
#Maximum sum of any submatrix of a Matrix which is sorted row-wise and column-wise
