#Minimum insertions to form a palindrome | DP-28
#Given string str, the task is to find the minimum number of characters to be inserted to convert it to a palindrome.

#Before we go further, let us understand with a few examples: 

#ab: Number of insertions required is 1 i.e. bab
#aa: Number of insertions required is 0 i.e. aa
#abcd: Number of insertions required is 3 i.e. dcbabcd
#abcda: Number of insertions required is 2 i.e. adcbcda which is the same as the number of insertions in the substring bcd(Why?).
#abcde: Number of insertions required is 4 i.e. edcbabcde
#--------------------------------------------------------------

#Let the input string be str[l……h]. The problem can be broken down into three parts:  

#Find the minimum number of insertions in the substring str[l+1,…….h].
#Find the minimum number of insertions in the substring str[l…….h-1].
#Find the minimum number of insertions in the substring str[l+1……h-1].
#Recursive Approach: The minimum number of insertions in the string str[l…..h] can be given as:  

#minInsertions(str[l+1…..h-1]) if str[l] is equal to str[h]
#min(minInsertions(str[l…..h-1]), minInsertions(str[l+1…..h])) + 1 otherwise
# A Naive recursive program to find minimum
# number insertions needed to make a string
# palindrome
import sys

# Recursive function to find minimum
# number of insertions
def findMinInsertions(str, l, h):

	# Base Cases
	if (l > h):
		return sys.maxsize
	if (l == h):
		return 0
	if (l == h - 1):
		return 0 if(str[l] == str[h]) else 1

	# Check if the first and last characters are
	# same. On the basis of the comparison result,
	# decide which subproblem(s) to call
	
	if(str[l] == str[h]):
		return findMinInsertions(str, l + 1, h - 1)
	else:
		return (min(findMinInsertions(str, l, h - 1),
					findMinInsertions(str, l + 1, h)) + 1)

# Driver Code
if __name__ == "__main__":
	
	str = "geeks"
	print(findMinInsertions(str, 0, len(str) - 1))

# This code is contributed by ita_c
#Output
#3
#Time Complexity: O(2n)
#Auxiliary Space: O(n)
#------------------------------------------------------------
#Dynamic Programming based Solution 
#If we observe the above approach carefully, we can find that it exhibits overlapping subproblems. 
#Suppose we want to find the minimum number of insertions in string “abcde”:  
#                      abcde
#            /       |      \
#           /        |        \
#           bcde         abcd       bcd  <- case 3 is discarded as str[l] != str[h]
#       /   |   \       /   |   \
#      /    |    \     /    |    \
#     cde   bcd  cd   bcd abc bc
#   / | \  / | \ /|\ / | \
#de cd d cd bc c………………….


#The substrings in bold show that the recursion is to be terminated and the recursion tree cannot originate from there. Substring in the same color indicates overlapping subproblems.

#How to re-use solutions of subproblems? The memorization technique is used to avoid similar subproblem recalls. We can create a table to store the results of subproblems so that they can be used directly if the same subproblem is encountered again.
#The below table represents the stored values for the string abcde. 

#a b c d e
#---------
#0 1 2 3 4
#0 0 1 2 3 
#0 0 0 1 2 
#0 0 0 0 1 
#0 0 0 0 0


#How to fill the table? 
#The table should be filled in a diagonal fashion. For the string abcde, 0….4, the following should be ordered in which the table is filled:

#Gap = 1: (0, 1) (1, 2) (2, 3) (3, 4)

#Gap = 2: (0, 2) (1, 3) (2, 4)

#Gap = 3: (0, 3) (1, 4)

#Gap = 4: (0, 4)
#Below is the implementation of the above approach: 

# A Dynamic Programming based program to
# find minimum number insertions needed
# to make a string palindrome

# A utility function to find minimum
# of two integers
def Min(a, b):
	return min(a, b)

# A DP function to find minimum number
# of insertions
def findMinInsertionsDP(str1, n):

	# Create a table of size n*n. table[i][j]
	# will store minimum number of insertions
	# needed to convert str1[i..j] to a palindrome.
	table = [[0 for i in range(n)]
				for i in range(n)]
	l, h, gap = 0, 0, 0

	# Fill the table
	for gap in range(1, n):
		l = 0
		for h in range(gap, n):
			if str1[l] == str1[h]:
				table[l][h] = table[l + 1][h - 1]
			else:
				table[l][h] = (Min(table[l][h - 1],
								table[l + 1][h]) + 1)
			l += 1

	# Return minimum number of insertions
	# for str1[0..n-1]
	return table[0][n - 1];

# Driver Code
str1 = "geeks"
print(findMinInsertionsDP(str1, len(str1)))

# This code is contributed by
# Mohit kumar 29
#---------------------------------------------------------------------
#Output
#3
#Time complexity: O(N2) 
#Auxiliary Space: O(N2)

#Another Dynamic Programming Solution (Variation of Longest Common Subsequence Problem) 
#The problem of finding minimum insertions can also be solved using Longest Common Subsequence (LCS) Problem. If we find out the LCS of string and its reverse, we know how many maximum characters can form a palindrome. We need to insert the remaining characters. Following are the steps. 

#Find the length of LCS of the input string and its reverse. Let the length be ‘l’.
#The minimum number of insertions needed is the length of the input string minus ‘l’.
#Below is the implementation of the above approach:  
# An LCS based Python3 program to find minimum
# number insertions needed to make a string
# palindrome

""" Returns length of LCS for X[0..m-1],
Y[0..n-1]. See http://goo.gl/bHQVP for
details of this function """
def lcs(X, Y, m, n) :

	L = [[0 for i in range(n + 1)] for j in range(m + 1)]

	""" Following steps build L[m + 1, n + 1] in
	bottom up fashion. Note that L[i, j]
	contains length of LCS of X[0..i - 1]
	and Y[0..j - 1] """
	for i in range(m + 1) :	
		for j in range(n + 1) :	
			if (i == 0 or j == 0) :
				L[i][j] = 0

			elif (X[i - 1] == Y[j - 1]) :
				L[i][j] = L[i - 1][j - 1] + 1
			else :
				L[i][j] = max(L[i - 1][j], L[i][j - 1])

	""" L[m,n] contains length of LCS for
	X[0..n-1] and Y[0..m-1] """
	return L[m][n]
	
# LCS based function to find minimum number
# of insertions
def findMinInsertionsLCS(Str, n) :

	# Using charArray to reverse a String
	charArray = list(Str)
	charArray.reverse()
	revString = "".join(charArray)
	
	# The output is length of string minus
	# length of lcs of str and it reverse
	return (n - lcs(Str, revString , n, n))

# Driver code
Str = "geeks"
print(findMinInsertionsLCS(Str,len(Str)))

# This code is contributed by divyehrabadiya07

#Output
#3
#Time complexity: O(N2) 
#Auxiliary Space: O(N2) 
#-------------------------------------------------------------------------
#Space Optimization Method: The above code can be space optimized by using only 1d array instead of 2d array. In the dp table we only need previous row and current row elements.
# An LCS based program to find minimum number
# insertions needed to make a string palindrome

# Returns length of LCS for X[0..m-1], Y[0..n-1].
def lcs(X, Y, m, n):
	prev = [0 for i in range(n+1)]
	curr = [0 for i in range(n+1)]
	for i in range(m+1):
		for j in range(n+1):
			if i == 0 or j == 0:
				prev[j] = 0
			elif X[i-1] == Y[j-1]:
				curr[j] = prev[j-1]+1
			else:
				curr[j] = max(prev[j], curr[j-1])
		prev = curr

	# L[m][n] contains length of LCS for X[0..n-1]
	# and Y[0..m-1]
	return prev[n]

def reverseStr(str):
	return str[::-1]

# LCS based function to find minimum number of
# insertions
def findMinInsertionsLCS(str, n):

	# Creata another string to store reverse of 'str'
	rev = reverseStr(str)

	# The output is length of string minus length of lcs of
	# str and it reverse
	return (n - lcs(str, rev, n, n))

# Driver code
if __name__ == "__main__":
	str = "geeks"
	print(findMinInsertionsLCS(str, len(str)))

# This Code is Contributed By Vivek Maddeshiya
#Output
#3
#Time complexity: O(N2) 
#Auxiliary Space: O(N) 
#--------------------------------------------------------------