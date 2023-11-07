Queries in a Matrix

#Difficulty Level : Medium
#Given a matrix M of size m x n ( 1 <= m,n <= 1000 ). It is initially filled with integers from 1 to m x n sequentially in a row major order. The task is to process a list of queries manipulating M such that every query is one of the following three. 

#R(x, y): swaps the x-th and y-th rows of M where x and y vary from 1 to m.
#C(x, y): swaps the x-th and y-th columns of M where x and y vary from 1 to n.
#P(x, y): prints the element at x-th row and y-th column where x varies from 1 to m and y varies from 1 to n.
#Note that the given matrix is stored as a typical 2D array with indexes start from 0, but values of x and y start from 1.

#Examples: 

#Input : m = 3, n = 3
#                    R(1, 2)
#                    P(1, 1)
#                    P(2, 1)
#                    C(1, 2)
#                    P(1, 1)
#                    P(2, 1)
#Output: value at (1, 1) = 4
#        value at (2, 1) = 1
#        value at (1, 1) = 5
#        value at (2, 1) = 2
#Explanation:
#The matrix is {{1, 2, 3}, 
#               {4, 5, 6},
#               {7, 8, 9}}
#After first R(1, 2) matrix becomes, 
#              {{4, 5, 6}, 
#              {1, 2, 3}, 
#               {7, 8, 9}}
#After first C(1, 2) matrix becomes, 
#              {{5, 4, 6}, 
#               {2, 1, 3}, 
#               {8, 7, 9}}


#Input : m = 1234, n = 5678
#                R(1, 2)
#                P(1, 1)
#                P(2, 1)
#                C(1, 2)
#                P(1, 1)
#                P(2, 1)
#Output: value at (1, 1) = 5679
#        value at (2, 1) = 1
#        value at (1, 1) = 5680
#        value at (2, 1) = 2
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#A simple solution for this problem is to finish all the queries manually, that means when we have to swap the rows just swap the elements of x’th row and y’th row and similarly for column swapping. But this approach may have time complexity of q*O(m) or q*O(n) where ‘q’ is number of queries and auxiliary space required O(m*n).
#An efficient approach for this problem requires little bit mathematical observation. Here we are given that elements in matrix are filled from 1 to mxn sequentially in row major order, so we will take advantage of this given scenario and can solve this problem. 

#Create an auxiliary array rows[m] and fill it with values 0 to m-1 sequentially.
#Create another auxiliary array cols[n] and fill it with values 0 to n-1 sequentially.
#Now for query ‘R(x, y)’ just swap the value of rows[x-1] with rows[y-1].
#Now for query ‘C(x, y)’ just swap the value of cols[x-1] with cols[y-1].
#Now for query ‘P(x, y)’ just skip the number of columns you have seen and calculate the value at (x, y) by rows[x-1]*n + cols[y-1] + 1.
#Below is implementation of above idea. 


# Python3 implementation of program
 
# Fills initial values in rows[] and cols[]
def preprocessMatrix(rows, cols, m, n):
 
    # Fill rows with 1 to m-1
    for i in range(m):
        rows[i] = i;
 
    # Fill columns with 1 to n-1
    for i in range(n):
        cols[i] = i;
 
# Function to perform queries on matrix
# m --> number of rows
# n --> number of columns
# ch --> type of query
# x --> number of row for query
# y --> number of column for query
def queryMatrix(rows, cols, m, n, ch, x, y):
 
    # perform queries
    tmp = 0;
     
    if ch == 'R':
 
        # swap row x with y
        rows[x-1], rows[y-1] = rows[y-1], rows[x-1];
 
    elif ch == 'C':
 
        # swap column x with y
        cols[x-1], cols[y-1] = cols[y-1],cols[x-1];
 
    elif ch == 'P':
 
        # Print value at (x, y)
        print('value at (',x,',',y,') = ',rows[x-1]*n + cols[y-1]+1, sep='');
         
    return ;
 
# Driver program to run the case
m = 1234
n = 5678;
 
# row[] is array for rows and cols[]
# is array for columns
rows = [0 for i in range(m)]
cols = [0 for i in range(n)];
 
# Fill initial values in rows[] and cols[]
preprocessMatrix(rows, cols, m, n);
 
queryMatrix(rows, cols, m, n, 'R', 1, 2);
queryMatrix(rows, cols, m, n, 'P', 1, 1);
queryMatrix(rows, cols, m, n, 'P', 2, 1);
queryMatrix(rows, cols, m, n, 'C', 1, 2);
queryMatrix(rows, cols, m, n, 'P', 1, 1);
queryMatrix(rows, cols, m, n, 'P', 2, 1);
 
# This code is contributed by rutvik_56.

#value at (1, 1) = 5679
#value at (2, 1) = 1
#value at (1, 1) = 5680
#value at (2, 1) = 2
#Time Complexity : O(q) , q = number of queries 
#Axillary Space : O(m+n)



#This article is contributed by Shashank Mishra ( Gullu ). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. 





#Like#
#3
#Next
#Submatrix Sum Queries
#Related Articles
#1.
#Generate a Matrix such that given Matrix elements are equal to Bitwise OR of all corresponding row and column elements of generated Matrix
#2.
#Generate matrix from given Sparse Matrix using Linked List and reconstruct the Sparse Matrix
#3.
#Queries for bitwise AND in the given matrix
#4.
#Queries for bitwise OR in the given matrix
#5.
#Find Number of Even cells in a Zero Matrix after Q queries
#6.
#Largest Square in a Binary Matrix with at most K 1s for multiple Queries
#7.
#Queries to find the count of connected Non-Empty Cells in a Matrix with updates
#8.
#Final Matrix after incrementing submatrices by K in range given by Q queries
#9.
#Queries to check if a path made up of even numbers from source to destination exists in a Matrix
#10.
#Queries to count sum of rows and columns of a Matrix present in given ranges