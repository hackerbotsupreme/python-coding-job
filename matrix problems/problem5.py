#Find unique elements in a matrix

#Difficulty Level : Basic
#Given a matrix mat[][] having n rows and m columns. We need to find unique elements in matrix i.e, those elements which are not repeated in the matrix or those elements whose frequency is 1. 

#Examples: 

#Input :  20  15  30  2
#         2   3   5   30
#         6   7   6   8
#Output : 3  20  5  7  8  15 

#Input :  1  2  3  
#         5  6  2
#         1  3  5
#         6  2  2
#Output : No unique element in the matrix
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Follow these steps to find a unique element: 

#Create an empty hash table or dictionary. 
#Traverse through all the elements of the matrix 
#If element is present in the dictionary, then increment its count 
#Otherwise insert element with value = 1. 
#Implementation:

C++
Java
Python3
# Python 3 program to find unique
# element in matrix
def unique(mat, n, m):
 
    maximum = 0; flag = 0
     
    for i in range(0, n):
        for j in range(0, m):
             
            # Find maximum element in
            # a matrix
            if(maximum < mat[i][j]):
                maximum = mat[i][j];
 
    uniqueElementDict = [0] * (maximum + 1)
 
    # loops to traverse through the matrix
    for i in range(0, n):
        for j in range(0, m):
                uniqueElementDict[mat[i][j]] += 1
 
    # Print all those keys whose count is 1
    for key in range(maximum + 1):
        if uniqueElementDict[key] == 1:
            print (key, end = " ")
            flag = 1
     
    if(flag == 0):
        print("No unique element in the matrix")
 
# Driver Code
mat = [[1, 2, 3, 20],
       [5, 6, 20, 25],
       [1, 3, 5, 6],
       [6, 7, 8, 15]]
n = 4
m = 4
unique(mat, n, m)
#C#
#PHP
#Javascript
#Output
#2 7 8 15 25 
#Complexity Analysis:

#Time Complexity: O(m*n) where m is the number of rows & n is the number of columns.
#Auxiliary Space: O(max(matrix)). 
#Method – 2: Using HashMap



This approach uses a hashmap instead of creating a hashtable of size max element + 1.

Implementation

C++
Java
Python3
# Python program to find unique element in matrix
 
# function that calculate unique element
def unique(mat, r, c) -> int:
   
    # declare map for hashing
    mp = {}
    for i in range(r):
        for j in range(c):
           
            # increase freq of mat[i][j] in map
            if mat[i][j] not in mp:
                mp[mat[i][j]] = 1
            else:
                mp[mat[i][j]] += 1
    flag = False
     
    # print unique element
    for p in mp:
        if mp[p] == 1:
            print(p, end=" ")
            flag = True
    if flag == False:
        print("No unique element in the matrix")
 
 
# Driver program
if __name__ == "__main__":
    mat = [[1, 2, 3, 20], [5, 6, 20, 25], [1, 3, 5, 6], [6, 7, 8, 15]]
     
    # function that calculate unique element
    unique(mat, 4, 4)
 
    # This code is contributed by ajaymakvana
C#
Javascript
Output
2 7 8 15 25 
Time Complexity: O(R*C)
Auxiliary Space: O(R*C)