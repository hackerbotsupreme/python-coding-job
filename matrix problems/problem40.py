#Print K’th element in spiral form of matrix

#Difficulty Level : Hard
#Given a 2D Matrix of order n X m, print K’th element in the spiral form of the matrix. See the following examples. 

#Examples: 

#Input: mat[][] = 
#          {{1, 2, 3, 4}
#           {5, 6, 7, 8}
#           {9, 10, 11, 12}
#           {13, 14, 15, 16}}
#       k = 6
#Output: 12
#Explanation: The elements in spiral order is 
#1, 2, 3, 4, 8, 12, 16, 15...
#so the 6th element is 12

#Input: mat[][] =
#       {{1, 2, 3, 4, 5, 6}
#        {7, 8, 9, 10, 11, 12}
#        {13, 14, 15, 16, 17, 18}}
#       k = 17
#Output: 10
#Explanation: The elements in spiral order is 
#1, 2, 3, 4, 5, 6, 12, 18, 17,
#16, 15, 14, 13, 7, 8, 9, 10, 11 
#so the 17 th element is 10.  
#Recommended Problem
#Find nth element of spiral matrix
#Matrix
#Data Structures
#Amazon
#Solve Problem
#Submission count: 8.2K
#Simple Approach: One simple solution is to start traversing matrix in spiral form Print Spiral Matrix and start a counter i.e; count = 0. Whenever count gets equal to K, print that element.
#
#Algorithm: 
#Keep a variable count = 0 to store the count.
#Traverse the matrix in spiral from start to end.
#Increase the count by 1 for every iteration.
#If the count is equal to the given value of k print the element and break.
#Implementation:

#C++
#Java
#Python3
#R = 3
#C = 6
 
def spiralPrint(m, n, a, c):
    k = 0
    l = 0
    count = 0
    """ k - starting row index
    m - ending row index
    l - starting column index
    n - ending column index
    i - iterator
    """
    while (k < m and l < n):
        for i in range(l,n):
            count+=1
             
            if (count == c):
                print(a[k][i] , end=" ")
         
        k+=1
        """ check the last column
        from the remaining columns """
        for i in range(k,m):
            count+=1
            if (count == c):
                print(a[i][n - 1],end=" ")
        n-=1
        """ check the last row from
        the remaining rows """
        if (k < m):
            for i in range(n - 1,l-1,-1):
                count+=1
                if (count == c):
                    print(a[m - 1][i],end=" ")
            m-=1
        """ check the first column from
        the remaining columns """
        if (l < n):
            for i in range(m - 1,k-1,-1):
                count+=1
                if (count == c):
                    print(a[i][l],end=" ")
            l+=1
 
""" Driver program to test above functions """
 
a = [[1, 2, 3, 4, 5, 6 ],[ 7, 8, 9, 10, 11, 12 ],[ 13, 14, 15, 16, 17, 18]]
k = 17
spiralPrint(R, C, a, k)
 
# This code is contributed by shivanisingh
#C#
#Javascript
##Output
#10 
#Complexity Analysis: 

#Time Complexity: O(R*C), A single traversal of matrix is needed so the Time Complexity is O(R*C).
#Space Complexity: O(1), constant space is required.
#Efficient Approach: While traversing the array in spiral order, a loop is used to traverse the sides. So if it can be found out that the kth element is in the given side then the kth element can be found out in constant time. This can be done recursively as well as iteratively.



#Algorithm : 
#Traverse the matrix in form of spiral or cycles.
#So a cycle can be divided into 4 parts, so if the cycle is of size m X n.
#Element is in first row, i.e k <= m
#Element is in last column, i.e k <= (m+n-1)
#Element is in last row, i.e. k <= (m+n-1+m-1)
#Element is in first column, i.e k <= (m+n-1+m-1+n-2)
#If any of the above conditions meet then the kth element can be found is constant time.
#Else remove the cycle from the array and recursively call the function.
#Implementation:

#C++
#Java
#Python3
# Python3 program for Kth element in spiral
# form of matrix
MAX = 100
 
''' function for Kth element '''
def findK(A, n, m, k):
     
    if (n < 1 or m < 1):
        return -1
         
    '''....If element is in outermost ring ....'''
    ''' Element is in first row '''
    if (k <= m):
        return A[0][k - 1]
         
    ''' Element is in last column '''
    if (k <= (m + n - 1)):
        return A[(k - m)][m - 1]
         
    ''' Element is in last row '''
    if (k <= (m + n - 1 + m - 1)):
        return A[n - 1][m - 1 - (k - (m + n - 1))]
     
    ''' Element is in first column '''
    if (k <= (m + n - 1 + m - 1 + n - 2)):
        return A[n - 1 - (k - (m + n - 1 + m - 1))][0]
         
         
    '''....If element is NOT in outermost ring ....'''
    ''' Recursion for sub-matrix. &A[1][1] is
    address to next inside sub matrix.'''
    A.pop(0)
    [j.pop(0) for j in A]
    return findK(A, n - 2, m - 2, k - (2 * n + 2 * m - 4))
 
''' Driver code '''
 
a = [[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11, 12 ],
    [ 13, 14, 15, 16, 17, 18 ]]
k = 17
print(findK(a, 3, 6, k))
 
# This code is contributed by shivanisinghss2110
#C#
#Javascript
#Output
#10
#Complexity Analysis: 

#Time Complexity: O(c), where c is number of outer circular rings with respect to k’th element.
#Space Complexity: O(1). 
#As constant space is required.
#This article is contributed by Shashank Mishra (Gullu). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.





#Like
#9
#Next
#Print a given matrix in spiral form
#Related Articles
##1.
#Print a given matrix in reverse spiral form
#2.
#Print a matrix in a spiral form starting from a point
#3.
#Print a given matrix in counter-clock wise spiral form
#4.
#Print a given matrix in spiral form using direction tracking method
#5.
#Print matrix elements diagonally in spiral form
#.
#C++ Program to Print a given matrix in reverse spiral form
#7.
#Java Program to Print a given matrix in reverse spiral form
#8.
#Python Program to Print a given matrix in reverse spiral form
#9.
#Php Program to Print a given matrix in reverse spiral form
#10.
#Javascript Program to Print a given matrix in reverse spiral form