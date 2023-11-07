#Validity of a given Tic-Tac-Toe board configuration

#Difficulty Level : Hard
#A Tic-Tac-Toe board is given after some moves are played. Find out if the given board is valid, i.e., is it possible to reach this board position after some moves or not.
#Note that every arbitrary filled grid of 9 spaces isn’t valid e.g. a grid filled with 3 X and 6 O isn’t valid situation because each player needs to take alternate turns.


#tictactoe
#Input is given as a 1D array of size 9. 

#Examples:

#Input: board[] =  {'X', 'X', 'O', 
#                   'O', 'O', 'X',
#                   'X', 'O', 'X'};
#Output: Valid

#Input: board[] =  {'O', 'X', 'X', 
#                   'O', 'X', 'X',
#                   'O', 'O', 'X'};
#Output: Invalid
#(Both X and O cannot win)

#Input: board[] =  {'O', 'X', ' ', 
#                   ' ', ' ', ' ',
#                   ' ', ' ', ' '};
#Output: Valid
#(Valid board with only two moves played)
#Recommended Problem
#Tic Tac Toe
#Arrays
#Data Structures
#Flipkart
#Accolite
#+2 more
#Solve Problem
#Submission count: 17.1K
#Basically, to find the validity of an input grid, we can think of the conditions when an input grid is invalid. Let no. of “X”s be countX and no. of “O”s be countO. Since we know that the game starts with X, a given grid of Tic-Tac-Toe game would be definitely invalid if following two conditions meet 

#countX != countO AND 
#countX != countO + 1
#Since “X” is always the first move, second condition is also required.
#Now does it mean that all the remaining board positions are valid one? The answer is NO. Think of the cases when input grid is such that both X and O are making straight lines. This is also not
#valid position because the game ends when one player wins. So we need to check the following condition as well 
#If input grid shows that both the players are in winning situation, it’s an invalid position. 
#If input grid shows that the player with O has put a straight-line (i.e. is in win condition) and countX != countO, it’s an invalid position. The reason is that O plays his move only after X plays his
#move. Since X has started the game, O would win when both X and O has played equal no. of moves. 
#If input grid shows that X is in winning condition than xCount must be one greater that oCount.
#Armed with above conditions i.e. a), b), c) and d), we can now easily formulate an algorithm/program to check the validity of a given Tic-Tac-Toe board position. 
#1)  countX == countO or countX == countO + 1
#2)  If O is in win condition then check 
#     a)     If X also wins, not valid
#     b)     If xbox != obox , not valid
#3)  If X is in win condition then check if xCount is
#     one more than oCount or not  
#Another way to find the validity of a given board is using ‘inverse method’ i.e. rule out all the possibilities when a given board is invalid.

#C++
#Java
#Python3
# Python3 program to check whether a given tic tac toe
# board is valid or not
 
# Returns true if char wins. Char can be either
# 'X' or 'O'
def win_check(arr, char):
    # Check all possible winning combinations
    matches = [[0, 1, 2], [3, 4, 5],
               [6, 7, 8], [0, 3, 6],
               [1, 4, 7], [2, 5, 8],
               [0, 4, 8], [2, 4, 6]]
 
    for i in range(8):
        if(arr[matches[i][0]] == char and
            arr[matches[i][1]] == char and
            arr[matches[i][2]] == char):
            return True
    return False
 
def is_valid(arr):
    # Count number of 'X' and 'O' in the given board
    xcount = arr.count('X')
    ocount = arr.count('O')
     
    # Board can be valid only if either xcount and ocount
    # is same or count is one more than oCount
    if(xcount == ocount+1 or xcount == ocount):
        # Check if O wins
        if win_check(arr, 'O'):
            # Check if X wins, At a given point only one can win,
            # if X also wins then return Invalid
            if win_check(arr, 'X'):
                return "Invalid"
 
            # O can only win if xcount == ocount in case where whole
            # board has values in each position.
            if xcount == ocount:
                return "Valid"
 
        # If X wins then it should be xc == oc + 1,
        # If not return Invalid    
        if win_check(arr, 'X') and xcount != ocount+1:
            return "Invalid"
         
        # if O is not the winner return Valid
        if not win_check(arr, 'O'):
            return "valid"
         
    # If nothing above matches return invalid
    return "Invalid"
 
 
# Driver Code
arr = ['X', 'X', 'O',
       'O', 'O', 'X',
       'X', 'O', 'X']
print("Given board is " + is_valid(arr))
#C#
#PHP
#Javascript
#Output


#Given board is valid
#Time complexity: O(1)
#Auxiliary Space: O(1), since no extra space has been taken.

#Thanks to Utkarsh for suggesting this solution. This article is contributed by Aarti_Rathi and Utkarsh. Please write comments if you find anything incorrect, or you want to share more information about the topic discussed above





#Like
#20
#Previous
#Submatrix Sum Queries
#Next
#Find perimeter of shapes formed with 1s in binary matrix
#Related Articles
#1.
#Check if given Sudoku board configuration is valid or not
#2.
#Count Knights that can attack a given pawn in an N * N board
#3.
#Minimum queens required to cover all the squares of a chess board
#4.
#Expected number of moves to reach the end of a board | Dynamic programming
#5.
#Expected number of moves to reach the end of a board | Matrix Exponentiation
#6.
#Boggle (Find all possible words in a board of characters) | Set 1
#7.
#Count of moves to escape given Matrix from given position based on given conditions
#8.
#Queries to increment array elements in a given range by a given value for a given number of times
#9.
#Sum of elements in given range from Array formed by infinitely concatenating given array
#10.
#Find element at given index after given range reversals