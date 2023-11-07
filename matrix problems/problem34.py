#Magic Square | ODD Order

#Difficulty Level : Hard
#A magic square of order n is an arrangement of n2 numbers, usually distinct integers, in a square, such that the n numbers in all rows, all columns, and both diagonals sum to the same constant. A magic square contains the integers from 1 to n2. 
#The constant sum in every row, column and diagonal are called the magic constant or magic sum, M. The magic constant of a normal magic square depends only on n and has the following value: 
#M = n(n2+1)/2

#For normal magic squares of order n = 3, 4, 5, ...,
#the magic constants are: 15, 34, 65, 111, 175, 260, ... 
#In this post, we will discuss how programmatically we can generate a magic square of size n. This approach only takes into account odd values of n and doesn’t work for even numbers. Before we go further, consider the below examples:
#
#Magic Square of size 3
#3-----------------------
#  2   7   6
#  9   5   1
#  4   3   8
#Sum in each row & each column = 3*(32+1)/2 = 15


#Magic Square of size 5
#----------------------
#  9   3  22  16  15
#  2  21  20  14   8
# 25  19  13   7   1
# 18  12   6   5  24
# 11  10   4  23  17
#Sum in each row & each column = 5*(52+1)/2 = 65


#Magic Square of size 7
#----------------------
# 20  12   4  45  37  29  28
# 11   3  44  36  35  27  19
#  2  43  42  34  26  18  10
# 49  41  33  25  17   9   1
# 40  32  24  16   8   7  48
# 31  23  15  14   6  47  39
# 22  21  13   5  46  38  30
#Sum in each row & each column = 7*(72+1)/2 = 175
#Did you find any pattern in which the numbers are stored? 

#In any magic square, the first number i.e. 1 is stored at position (n/2, n-1). Let this position be (i,j). The next number is stored at position (i-1, j+1) where we can consider each row & column as circular array i.e. they wrap around.

#Three conditions hold:

#The position of next number is calculated by decrementing row number of the previous number by 1, and incrementing the column number of the previous number by 1. At any time, if the calculated row position becomes -1, it will wrap around to n-1. Similarly, if the calculated column position becomes n, it will wrap around to 0.
#If the magic square already contains a number at the calculated position, calculated column position will be decremented by 2, and calculated row position will be incremented by 1.
#If the calculated row position is -1 & calculated column position is n, the new position would be: (0, n-2). 
#Example:
#Magic Square of size 3
#----------------------
# 2  7  6
# 9  5  1
# 4  3  8 

#Steps:
#1. position of number 1 = (3/2, 3-1) = (1, 2)
#2. position of number 2 = (1-1, 2+1) = (0, 0)
#3. position of number 3 = (0-1, 0+1) = (3-1, 1) = (2, 1)
#4. position of number 4 = (2-1, 1+1) = (1, 2)
#   Since, at this position, 1 is there. So, apply condition 2.
#   new position=(1+1,2-2)=(2,0)
#5. position of number 5=(2-1,0+1)=(1,1)
#6. position of number 6=(1-1,1+1)=(0,2)
#7. position of number 7 = (0-1, 2+1) = (-1,3) // this is tricky, see condition 3 
#   new position = (0, 3-2) = (0,1)
#8. position of number 8=(0-1,1+1)=(-1,2)=(2,2) //wrap around
#9. position of number 9=(2-1,2+1)=(1,3)=(1,0) //wrap around
#Based on the above approach, the following is the working code: 


# Python program to generate
# odd sized magic squares
# A function to generate odd
# sized magic squares
 
 
def generateSquare(n):
 
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]
 
    # initialize position of 1
    i = n // 2
    j = n - 1
 
    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:
 
            # next number goes out of
            # right side of square
            if j == n:
                j = 0
 
            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1
 
        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1
 
        j = j + 1
        i = i - 1  # 1st condition
 
    # Printing magic square
    print("Magic Square for n =", n)
    print("Sum of each row or column",
          n * (n * n + 1) // 2, "\n")
 
    for i in range(0, n):
        for j in range(0, n):
            print('%2d ' % (magicSquare[i][j]),
                  end='')
 
            # To display output
            # in matrix form
            if j == n - 1:
                print()
 
# Driver Code
 
 
# Works only when n is odd
n = 7
generateSquare(n)
 
# This code is contributed
# by Harshit Agrawal

#Output
#The Magic Square for n=7:
#Sum of each row or column 175:

#  20   12    4   45   37   29   28 
#  11    3   44   36   35   27   19 
#   2   43   42   34   26   18   10 
#  49   41   33   25   17    9    1 
#  40   32   24   16    8    7   48 
#  31   23   15   14    6   47   39 
#  22   21   13    5   46   38   30 
#Time Complexity: O(n2)
#Auxiliary Space: O(n2)

#NOTE: This approach works only for odd values of n.

#Recommended
#Solve DSA problems on GfG Practice.

#Solve Problems


#Like
#Previous
#Count numbers that don't contain 3
#Next
#Check given matrix is magic square or not
#Related Articles
#1.
#Magic Square | Even Order
#2.
#Minimum cost to convert 3 X 3 matrix into magic square
#3.
#Check given matrix is magic square or not
#4.
#Minimum changes needed to make a 3*3 matrix magic square
#5.
#Fill missing entries of a magic square
#6.
#Sum of both diagonals of a spiral odd-order square matrix
#7.
#Make all the elements of array odd by incrementing odd-indexed elements of odd-length subarrays
#8.
#Print odd positioned nodes of odd levels in level order of the given binary tree
#9.
#Find nth Magic Number
#10.
#The Magic of Fibonacci Numbers