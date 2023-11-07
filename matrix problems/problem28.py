#Program for Conway’s Game Of Life

#Difficulty Level : Medium
#Initially, there is a grid with some cells which may be alive or dead. Our task is to generate the next generation of cells based on the following rules: 

#Any live cell with fewer than two live neighbors dies as if caused by underpopulation.
##Any live cell with two or three live neighbors lives on to the next generation.
#Any live cell with more than three live neighbors dies, as if by overpopulation.
#Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#Examples: 

#The ‘*’ represents an alive cell and the ‘.’ represents a dead cell. 

#Input : ..........
#        ...**.....
#        ....*.....
#        ..........
#        ..........
#Output: ..........
#        ...**.....
#        ...**.....
#        ..........
#        ..........
#        ..........

#Input : ..........
#        ...**.....
#        ....*.....
##        ..........
# #       ..........
###        ...**.....
##        ..**......
##        .....*....
##        ....*.....
##        ..........
#Output: ..........
##        ...**.....
#        ...**.....
##        ..........
##        ..........
# #       ..***.....
##        ..**......
 #       ...**.....
##        ..........
#        ..........
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Here is a simple Java implementation of the Game Of Life. Grid is initialized with 0’s representing the dead cells and 1’s representing alive cells. The generate() function loops through every cell and counts its neighbors. Based on that values, the aforementioned rules are implemented. The following implementation ignores the edge cells as it is supposed to be played on an infinite plane. #

#Implementation:#

#C++
##C
##Java
##Python3
## A simple Python program to implement Game of Life
## 
## driver program
 
## Function to print next generation
#def nextGeneration(grid, M, N):
#    future = [[0 for i in range(N)] for j in range(M)]
# 
#    # Loop through every cell
#    for l in range(M):
#        for m in range(N):
#             
#            # finding no Of Neighbours that are alive
#            aliveNeighbours = 0
#            for i in range(-1,2):
##                for j in range(-1,2):
#                    if ((l+i>=0 and l+i<M) and (m+j>=0 and m+j<N)):
#                        aliveNeighbours += grid[l + i][m + j]
# 
##            # The cell needs to be subtracted from
#            # its neighbours as it was counted before
#            aliveNeighbours -= grid[l][m]
## 
##            # Implementing the Rules of Life
# 
#            # Cell is lonely and dies
#            if ((grid[l][m] == 1) and (aliveNeighbours < 2)):
#                future[l][m] = 0
# 
#            # Cell dies due to over population
#            elif ((grid[l][m] == 1) and (aliveNeighbours > 3)):
#                future[l][m] = 0
 
##            # A new cell is born
#            elif ((grid[l][m] == 0) and (aliveNeighbours == 3)):
#                future[l][m] = 1
## 
#            # Remains the same
##            else:
#                future[l][m] = grid[l][m]
# 
## 
#    print("Next Generation")
#    for i in range(M):
#        for j in range(N):
#            if (future[i][j] == 0):
#                print(".",end="")
#            else:
#                print("*",end="")
#        print()
# 
M,N = 10,10
# 
## Initializing the grid.
#grid = [ [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
##    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
##    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
#    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
##    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ],
#    [ 0, 0, 0, 1, 1, 0, 0, 0, 0, 0 ],
#    [ 0, 0, 1, 1, 0, 0, 0, 0, 0, 0 ],
#    [ 0, 0, 0, 0, 0, 1, 0, 0, 0, 0 ],
#    [ 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 ],
#    [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ]
#]
# 
## Displaying the grid
#print("Original Generation")
#for i in range(M):
#    for j in range(N):
#        
#        if(grid[i][j] == 0):
##            print(".",end = "")
#        else:
#            print("*",end = "")
#    print()
##print()
#nextGeneration(grid, M, N)
# 
### This code is contributed by shinjanpatra
##C#
#Javascript
#Output
#Initial Stage:
# ----- ----- ----- -----
#:  1  :  0  :  1  :  1  :
# ----- ----- ----- -----
#:  1  :  1  :  0  :  0  :
# ----- ----- ----- -----
#:  1  :  1  :  0  :  1  :
## ----- ----- ----- -----
#:  0  :  1  :  1  :  0  :
# ----- ----- ----- -----
#:  0  :  0  :  0  :  0  :
## ----- ----- ----- -----#

#Next Generation:
## ----- ----- ----- -----
###:  1  :  0  :  1  :  0  :
# ----- ----- ----- -----
##:  0  :  0  :  0  :  1  :
## ----- ----- ----- -----
#:  0  :  0  :  0  :  0  :
# ----- ----- ----- -----
:  1  :  1  :  1  :  0  :
# ----- ----- ----- -----
##:  0  :  0  :  0  :  0  :
## ----- ----- ----- -----
#Time Complexity : O(r*c), where r is the number of rows and c is the number of columns.
##Auxiliary Space : O(r*c), since r*c extra space has been taken.#
####
#

##The above implementation is very basic. Try coming up with a more efficient implementation and be sure to comment below. Also for fun try creating your own rule for cellular Automata. 
###Conway’s Game Of Life is a Cellular Automation Method created by John Conway. This game was created with Biology in mind but has been applied in various fields such as Graphics, terrain generation, etc.
#This article is contributed by Vaibhav Mehta. If you like GeeksforGeeks and would like to contribute, you can also mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. #
##
#
##
##

#Like
#10
#Previous
#Program for Sudoku Generator
#Related Articles
#1.
#Program for Conway’s Game Of Life | Set 2
#2.
##Conway's Game Of Life (Python Implementation)
#3#.
#C Program for Program to Interchange Diagonals of Matrix
###4.
##Program for Rank of Matrix
#5.
##Program to find Normal and Trace of a matrix
##6.
#C Program To Check whether Matrix is Skew Symmetric or not
#7.
#Program to find largest element in an array
#8.
#Program to multiply two matrices
#9.
##Program to find transpose of a matrix
#10.
#Program for addition of two matrice##s