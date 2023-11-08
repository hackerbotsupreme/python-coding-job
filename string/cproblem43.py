#Lexicographic rank of a String
#Difficulty Level : Hard

#Given a string str, find its rank among all its permutations when sorted lexicographically.

#Note: The characters a string are all unique.

#Examples:

#Input: str = “acb”
#Output: 2
#Explanation: If all the permutations of the string are arranged lexicographically they will be “abc”, “acb”, “bac”, “bca”, “cab”, “cba”. From here it can be clearly that the rank of str is 2.


#Input: str = “string”
#Output: 598

#Input: str[] = “cba”
#Output: Rank = 6

#------------------------------------------------------------------------------
#Naive Approach: One simple solution is to generate all the permutations in lexicographic order and store the rank of the current string. After generating a permutation, check if the generated permutation is the same as the given string and return the rank of str.

#Lexicographic rank of a String using the concept of permutation:
#The problem can be solved using the concept of permutation, based on the following idea:

#For characters in each index, find how many lexicographically smaller strings can be formed when all the characters till that index are fixed. This will give the strings smaller than that and we can get the rank.

#For a better understanding follow the below illustration.

#Illustration:

#Let the given string be “STRING”. In the input string, ‘S’ is the first character. There are total 6 characters and 4 of them are smaller than ‘S’. So there can be 4 * 5! smaller strings where first character is smaller than ‘S’, like following 

#G X X X X X
#R X X X X X
#I X X X X X
#N X X X X X
#Similarly we can use the same process for the other letters. Fix ‘S’ and find the smaller strings starting with ‘S’. 

#Repeat the same process for T, rank is 4*5! + 4*4! +. . . 
#Now fix T and repeat the same process for R, rank is 4*5! + 4*4! + 3*3! + . . .
#Now fix R and repeat the same process for I, rank is 4*5! + 4*4! + 3*3! + 1*2! + . . . 
#Now fix I and repeat the same process for N, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + . . .
#Now fic N and repeat the same process for G, rank is 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0!  
#If this process is continued the rank = 4*5! + 4*4! + 3*3! + 1*2! + 1*1! + 0*0! = 597. The above computations find count of smaller strings. Therefore rank of given string is count of smaller strings plus 1. The final rank = 1 + 597 = 598

#Follow the steps mentioned below to implement the idea:

#Iterate the string from i = 0 to length of string:
#Find the number of characters smaller than the current character.
#Calculate the number of lexicographically smaller that can be formed using them as shown above.
#Add that value to the rank.
#At the end, add 1 with rank and return it as the required answer. [the reason is mentioned above]
#Below is the implementation of the above approach.  


# Python program to find lexicographic
# rank of a string
 
# A utility function to find factorial
# of n
def fact(n):
    f = 1
    while n >= 1:
        f = f * n
        n = n - 1
    return f
 
# A utility function to count smaller
# characters on right of arr[low]
def findSmallerInRight(st, low, high):
    countRight = 0
    i = low + 1
    while i <= high:
        if st[i] < st[low]:
            countRight = countRight + 1
        i = i + 1
 
    return countRight
 
# A function to find rank of a string
# in all permutations of characters
def findRank(st):
    ln = len(st)
    mul = fact(ln)
    rank = 1
    i = 0
 
    while i < ln:
        mul = mul // (ln - i)
 
        # count number of chars smaller
        # than str[i] from str[i + 1] to
        # str[len-1]
        countRight = findSmallerInRight(st, i, ln-1)
 
        rank = rank + countRight * mul
        i = i + 1
 
    return rank
 
 
# Driver code
if __name__ == '__main__':
    st = "string"
     
    # Function call
    print(findRank(st))
 
# This code is contributed by Nikita Tiwari.
#Output
#598
#Time Complexity: O(N2)
#Auxiliary Space: O(1)
#------------------------------------------------------------------------------
#Lexicographic rank of a String in linear time:
#The idea of the solution is the same as the above approach. The time complexity can be reduced by creating an auxiliary array of size 256.

#Create an array to store the number of characters smaller than the ith character in the whole string and update it after each index of the given string during the iteration of the string.

#Below is the implementation of the above approach.


# A O(n) solution for finding rank of string
MAX_CHAR = 256
 
# All elements of count[] are initialized with 0
count = [0]*(MAX_CHAR + 1)
 
# A utility function to find factorial of n
def fact(n):
    return 1 if(n <= 1) else (n * fact(n - 1))
 
# Construct a count array where value at every index
# contains count of smaller characters in whole string
def populateAndIncreaseCount(str):
    for i in range(len(str)):
        count[ord(str[i])] += 1
 
    for i in range(1, MAX_CHAR):
        count[i] += count[i - 1]
 
# Removes a character ch from count[] array
# constructed by populateAndIncreaseCount()
def updatecount(ch):
 
    for i in range(ord(ch), MAX_CHAR):
        count[i] -= 1
 
# A function to find rank of a string in all permutations
# of characters
def findRank(str):
    len1 = len(str)
    mul = fact(len1)
    rank = 1
 
    # Populate the count array such that count[i]
    # contains count of characters which are present
    # in str and are smaller than i
    populateAndIncreaseCount(str)
 
    for i in range(len1):
        mul = mul//(len1 - i)
 
        # count number of chars smaller than str[i]
        # from str[i+1] to str[len-1]
        rank += count[ord(str[i]) - 1] * mul
 
        # Reduce count of characters greater than str[i]
        updatecount(str[i])
 
    return rank
 
 
# Driver code
if __name__ == '__main__':
    str = "string"
    print(findRank(str))
 
# This is code is contributed by chandan_jnu
#Output
#598
#Time Complexity: O(N)
#Auxiliary Space: O(1) as we are using an array of size 256