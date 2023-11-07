#Find distinct elements common to all rows of a matrix

#Difficulty Level : Medium
#Given a n x n matrix. The problem is to find all the distinct elements common to all rows of the matrix. The elements can be printed in any order.

#Examples: 

#Input : mat[][] = {  {2, 1, 4, 3},
#                     {1, 2, 3, 2},  
#                     {3, 6, 2, 3},  
#                     {5, 2, 5, 3}  }
#Output : 2 3

#Input : mat[][] = {  {12, 1, 14, 3, 16},
#                     {14, 2, 1, 3, 35},  
#                     {14, 1, 14, 3, 11},  
#                     {14, 25, 3, 2, 1},
#                     {1, 18, 3, 21, 14}  }
#Output : 1 3 14
#Recommended Problem
#Find distinct elements
#Arrays
#Hash
#+1 more
#Solve Problem
#Submission count: 14.2K
#Method 1: Using three nested loops. Check if an element of 1st row is present in all the subsequent rows. Time Complexity of O(n3). Extra space could be required to handle the duplicate elements.
 
#Method 2: Sort all the rows of the matrix individually in increasing order. Then apply a modified approach to the problem of finding common elements in 3 sorted arrays. Below an implementation for the same is given. 

# Python3 implementation to find distinct
# elements common to all rows of a matrix
MAX = 100
 
# function to individually sort
# each row in increasing order
def sortRows(mat, n):
 
    for i in range(0, n):
        mat[i].sort();
 
# function to find all the common elements
def findAndPrintCommonElements(mat, n):
 
    # sort rows individually
    sortRows(mat, n)
 
    # current column index of each row is
    # stored from where the element is being
    # searched in that row
     
    curr_index = [0] * n
    for i in range (0, n):
        curr_index[i] = 0
         
    f = 0
 
    while(curr_index[0] < n):
     
        # value present at the current
        # column index of 1st row
        value = mat[0][curr_index[0]]
 
        present = True
 
        # 'value' is being searched in
        # all the subsequent rows
        for i in range (1, n):
         
            # iterate through all the elements
            # of the row from its current column
            # index till an element greater than
            # the 'value' is found or the end of
            # the row is encountered
            while (curr_index[i] < n and
                   mat[i][curr_index[i]] <= value):
                curr_index[i] = curr_index[i] + 1
                 
            # if the element was not present at
            # the column before to the 'curr_index'
            # of the row
            if (mat[i][curr_index[i] - 1] != value):
                present = False
 
            # if all elements of the row have
            # been traversed)
            if (curr_index[i] == n):
             
                f = 1
                break
             
        # if the 'value' is common to all the rows
        if (present):
            print(value, end = " ")
 
        # if any row have been completely traversed
        # then no more common elements can be found
        if (f == 1):
            break
     
        curr_index[0] = curr_index[0] + 1
 
# Driver Code
mat = [[12, 1, 14, 3, 16],
       [14, 2, 1, 3, 35],
       [14, 1, 14, 3, 11],
       [14, 25, 3, 2, 1],
       [1, 18, 3, 21, 14]]
 
n = 5
findAndPrintCommonElements(mat, n)
 
# This code is contributed by iAyushRaj

#Output:  

#1 3 14
#Time Complexity: O(n2log n), each row of size n requires O(nlogn) for sorting and there are total n rows. 
#Auxiliary Space: O(n) to store current column indexes for each row.
 
#Method 3: It uses the concept of hashing. The following steps are:  

#Map the element of the 1st row in a hash table. Let it be hash.
#Fow row = 2 to n
#Map each element of the current row into a temporary hash table. Let it be temp.
#Iterate through the elements of hash and check that the elements in hash are present in temp. If not present then delete those elements from hash.
#When all the rows are being processed in this manner, then the elements left in hash are the required common elements.
#C++
#Java
#Python3
# Python3 program to find distinct elements
# common to all rows of a matrix
MAX = 100
 
# function to individually sort
# each row in increasing order
def findAndPrintCommonElements(mat, n):
    us = dict()
 
    # map elements of first row
    # into 'us'
    for i in range(n):
        us[mat[0][i]] = 1
 
    for i in range(1, n):
        temp = dict()
         
        # mapping elements of current row
        # in 'temp'
        for j in range(n):
            temp[mat[i][j]] = 1
 
        # iterate through all the elements
        # of 'us'
        for itr in list(us):
 
            # if an element of 'us' is not present
            # into 'temp', then erase that element
            # from 'us'
            if itr not in temp:
                del us[itr]
 
        # if size of 'us' becomes 0,
        # then there are no common elements
        if (len(us) == 0):
            break
 
    # print common elements
    for itr in list(us)[::-1]:
        print(itr, end = " ")
 
# Driver Code
mat = [[2, 1, 4, 3],
       [1, 2, 3, 2],
       [3, 6, 2, 3],
       [5, 2, 5, 3]]
n = 4
findAndPrintCommonElements(mat, n)
 
# This code is contributed by Mohit Kumar
C#
Javascript
# Output: 

#3 2
#Time Complexity: O(n2) 
#Space Complexity: O(n), since n extra space has been taken.

#Method 4: Using Map

#Insert all the elements of the 1st row in the map.
#Now we check that the elements present in the map are present in each row or not.
#If the element is present in the map and is not duplicated in the current row, then we increment the count of the element in the map by 1.
#If we reach the last row while traversing and if the element appears (N-1) times before then we print the element.
#C++
#Java
#Python3
# Python code to find distinct elements
# common to all rows of a matrix
def distinct(matrix, N):
     
    # Make a empty map
    ans = {}
 
    # Insert the elements of
    # first row in the map and
    # initialize with 1
    for j in range(N):
        ans[matrix[0][j]] = 1
 
    # Traverse the matrix from 2nd row
    for i in range(N):
        for j in range(N):
             
            # If the element is present in the map
            # and is not duplicated in the current row
            if matrix[i][j] in ans and ans[matrix[i][j]] == i:
                 
                # Increment count of the element in
                # map by 1
                ans[matrix[i][j]] = i + 1
 
                # If we have reached the last row
                if (i == N - 1):
                     
                    # Print the element
                    print(matrix[i][j],end=" ")
 
# Driver code
matrix = [ [ 2, 1, 4, 3 ],
                  [ 1, 2, 3, 2 ],
                  [ 3, 6, 2, 3 ],
                  [ 5, 2, 5, 3 ] ]
n = 4
 
distinct(matrix, n)
 
# This code is contributed by shinjanpatra
#C#
#Javascript
#Output:

#2 3
#Time Complexity: O(n2) 

#Space Complexity: O(n)

#This article is contributed by Ayush Jauhari. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to contribute@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
#Please write comments if you find anything incorrect, or you want to