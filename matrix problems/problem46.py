#Program for Sudoku Generator

#Difficulty Level : Hard
#Last Updated : 11 Jan, 2023
#Read
#Discuss
#Courses
#Practice
#Video
#Background: 
#Following are the rules of Sudoku for a player. 

#In all 9 sub matrices 3×3 the elements should be 1-9, without repetition.
#In all rows there should be elements between 1-9 , without repetition.
#In all columns there should be elements between 1-9 , without repetition.
#The task is to generate a 9 x 9 Sudoku grid that is valid, i.e., a player can fill the grid following above set of rules.

#A simple naïve solution can be. 

#Randomly take any number 1-9.
#Check if it is safe to put in the cell.(row , column and box)
#If safe, place it and increment to next location and go to step 1.
#If not safe, then without incrementing go to step 1.
#Once matrix is fully filled, remove k no. of elements randomly to complete game.
#Improved Solution : We can improve the solution, if we understand a pattern in this game. We can observe that all 3 x 3 matrices, which are diagonally present are independent of other 3 x 3 adjacent matrices initially, as others are empty. 


#   3 8 5 0 0 0 0 0 0 
#   9 2 1 0 0 0 0 0 0 
#   6 4 7 0 0 0 0 0 0 
#   0 0 0 1 2 3 0 0 0 
#   0 0 0 7 8 4 0 0 0 
#   0 0 0 6 9 5 0 0 0 
#   0 0 0 0 0 0 8 7 3 
#   0 0 0 0 0 0 9 6 2 
#   0 0 0 0 0 0 1 4 5 
#(We can observe that in above matrix, the diagonal matrices are independent of other empty matrices initially). So if we fill them first, then we will only have to do box check and thus column/row check not required.

#Secondly, while we fill rest of the non-diagonal elements, we will not have to use random generator, but we can fill recursively by checking 1 to 9. 

#Following is the improved logic for the problem.
#1. Fill all the diagonal 3x3 matrices.
#2. Fill recursively rest of the non-diagonal matrices.
#   For every cell to be filled, we try all numbers until
#   we find a safe number to be placed.  
#3. Once matrix is fully filled, remove K elements
#   randomly to complete game.
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#C++
#Java
#Python3
import random
import math
 
class Sudoku:
    def __init__(self, N, K):
        self.N = N
        self.K = K
 
        # Compute square root of N
        SRNd = math.sqrt(N)
        self.SRN = int(SRNd)
        self.mat = [[0 for _ in range(N)] for _ in range(N)]
     
    def fillValues(self):
        # Fill the diagonal of SRN x SRN matrices
        self.fillDiagonal()
 
        # Fill remaining blocks
        self.fillRemaining(0, self.SRN)
 
        # Remove Randomly K digits to make game
        self.removeKDigits()
     
    def fillDiagonal(self):
        for i in range(0, self.N, self.SRN):
            self.fillBox(i, i)
     
    def unUsedInBox(self, rowStart, colStart, num):
        for i in range(self.SRN):
            for j in range(self.SRN):
                if self.mat[rowStart + i][colStart + j] == num:
                    return False
        return True
     
    def fillBox(self, row, col):
        num = 0
        for i in range(self.SRN):
            for j in range(self.SRN):
                while True:
                    num = self.randomGenerator(self.N)
                    if self.unUsedInBox(row, col, num):
                        break
                self.mat[row + i][col + j] = num
     
    def randomGenerator(self, num):
        return math.floor(random.random() * num + 1)
     
    def checkIfSafe(self, i, j, num):
        return (self.unUsedInRow(i, num) and self.unUsedInCol(j, num) and self.unUsedInBox(i - i % self.SRN, j - j % self.SRN, num))
     
    def unUsedInRow(self, i, num):
        for j in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    def unUsedInCol(self, j, num):
        for i in range(self.N):
            if self.mat[i][j] == num:
                return False
        return True
     
    
    def fillRemaining(self, i, j):
        # Check if we have reached the end of the matrix
        if i == self.N - 1 and j == self.N:
            return True
     
        # Move to the next row if we have reached the end of the current row
        if j == self.N:
            i += 1
            j = 0
     
        # Skip cells that are already filled
        if self.mat[i][j] != 0:
            return self.fillRemaining(i, j + 1)
     
        # Try filling the current cell with a valid value
        for num in range(1, self.N + 1):
            if self.checkIfSafe(i, j, num):
                self.mat[i][j] = num
                if self.fillRemaining(i, j + 1):
                    return True
                self.mat[i][j] = 0
         
        # No valid value was found, so backtrack
        return False
 
    def removeKDigits(self):
        count = self.K
 
        while (count != 0):
            i = self.randomGenerator(self.N) - 1
            j = self.randomGenerator(self.N) - 1
            if (self.mat[i][j] != 0):
                count -= 1
                self.mat[i][j] = 0
     
        return
 
    def printSudoku(self):
        for i in range(self.N):
            for j in range(self.N):
                print(self.mat[i][j], end=" ")
            print()
 
# Driver code
if __name__ == "__main__":
    N = 9
    K = 40
    sudoku = Sudoku(N, K)
    sudoku.fillValues()
    sudoku.printSudoku()
#C#
#Output: [0 means not filled] 



#2 3 0 4 1 5 0 6 8 
#0 8 0 2 3 6 5 1 9 
#1 6 0 9 8 7 2 3 4 
#3 1 7 0 9 4 0 2 5 
#4 5 8 1 2 0 6 9 7 
#9 2 6 0 5 8 3 0 1 
#0 0 0 5 0 0 1 0 2 
#0 0 0 8 4 2 9 0 3 
#5 9 2 3 7 1 4 8 6 
#Time Complexity: O(N2) 
#Auxiliary Space: O(N2), since N2 extra space has been taken.

#This article is contributed by Aarti_Rathi and Ankur Trisal (ankur.trisal@gmail.com). If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.
#Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above.
 





#Like
#15
#Previous
#Construct Ancestor Matrix from a Given Binary Tree
#Next
#Program for Conway's Game Of Life
#Related Articles
#1.
#Check if given Sudoku board configuration is valid or not
#2.
#Solve Sudoku on the basis of the given irregular regions
#3.
#Check if given Sudoku solution is valid or not
#4.
#Sudoku | Backtracking-7
#5.
#Random Acyclic Maze Generator with given Entry and Exit point
#6.
#C Program for Program to Interchange Diagonals of Matrix
#7.
#Program for Rank of Matrix
#8.
#Program to find Normal and Trace of a matrix
##9.
#C Program To Check whether Matrix is Skew Symmetric or not
#10.
#Program for Conway's Game Of Life
#Article Contributed By :
#https://media.geeksforgeeks.org/auth/avatar.png
#GeeksforGeeks
#Vote for difficulty
#Current difficulty : Hard
#Easy
#Normal
#Medium
#Hard
#Expert
#Improved By :
#menonkartikeya
#clintra
#rrrtnx
#codewithshinchan
#adi1212
#rishavnitro
#vikramshirsath177
#Article Tags :
#Matrix
#Practice Tags :
#Matrix