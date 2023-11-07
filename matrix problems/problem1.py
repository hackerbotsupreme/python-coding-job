#Print matrix in zig-zag fashion

#Difficulty Level : Hard
#Given a matrix of 2D array of n rows and m columns. Print this matrix in ZIG-ZAG fashion as shown in figure. 
 

#matrix_zag-zag

#Example: 

#Input: 
#1 2 3
#4 5 6
#7 8 9
#Output: 
#1 2 4 7 5 3 6 8 9
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Approach of C++ code
#The approach is simple. Just simply iterate over every diagonal elements one at a time and change the direction according to the previous match. 


#
#Approach of Python3 code 
#This approach is simple. While travelling the matrix in the usual fashion, on basis of parity of the sum of the indices of the element, add that particular element to the list either at the beginning or at the end if sum of i and j is either even or odd respectively. Print the solution list as it is.

#Implementation:
# Program to print matrix in Zig-zag pattern
 
#matrix =[
#            [ 1, 2, 3,],
#            [ 4, 5, 6 ],
#            [ 7, 8, 9 ],
#        ]
#rows=3
#columns=3
   
#solution=[[] for i in range(rows+columns-1)]
 
for i in range(rows):
    for j in range(columns):
        sum=i+j
        if(sum%2 ==0):
 
            #add at beginning
            solution[sum].insert(0,matrix[i][j])
        else:
 
            #add at end of the list
            solution[sum].append(matrix[i][j])
         
             
# print the solution as it as
for i in solution:
    for j in i:
        print(j,end=" ")
         
 

#Output


#1 2 4 7 5 3 6 8 9 
#Time complexity: O(n*m)
#Auxiliary space: O(1), since no extra space has been taken.

