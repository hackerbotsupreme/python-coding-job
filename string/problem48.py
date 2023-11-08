#Shortest Common Supersequence
#Difficulty Level : Medium
#Given two strings str1 and str2, the task is to find the length of the shortest string that has both str1 and str2 as subsequences.

#Examples : 

#Input:   str1 = "geek",  str2 = "eke"
#Output: 5
#Explanation: 
#String "geeke" has both string "geek" 
#and "eke" as subsequences.

##Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
#Output:  9
#Explanation: 
#String "AGXGTXAYB" has both string 
#"AGGTAB" and "GXTXAYB" as subsequences.

#--------------------------------------------------------
#Method 1: This problem is closely related to longest common subsequence problem.
#Below are steps.

#Find Longest Common Subsequence (lcs) of two given strings. For example, lcs of “geek” and “eke” is “ek”. 
#Insert non-lcs characters (in their original order in strings) to the lcs found above, and return the result. So “ek” becomes “geeke” which is shortest common supersequence.
##Let us consider another example, str1 = “AGGTAB” and str2 = “GXTXAYB”. LCS of str1 and str2 is “GTAB”. Once we find LCS, we insert characters of both strings in order and we get “AGXGTXAYB”
#How does this work? 

#We need to find a string that has both strings as subsequences and is the shortest such string. If both strings have all characters different, then result is sum of lengths of two given strings. If there are common characters, then we don’t want them multiple times as the task is to minimize length. Therefore, we first find the longest common subsequence, take one occurrence of this subsequence and add extra characters. 

#Length of the shortest supersequence  
#= (Sum of lengths of given two strings) 
#- (Length of LCS of two given strings) 
#Below is the implementation of above idea. The below implementation only finds length of the shortest super sequence. 


# Python program to find length
# of the shortest supersequence
 
# Function to find length of the
# shortest supersequence of X and Y.
 
 
def shortestSuperSequence(X, Y):
    m = len(X)
    n = len(Y)
    l = lcs(X, Y, m, n)
 
    # Result is sum of input string
    # lengths - length of lcs
    return (m + n - l)
 
# Returns length of LCS for
# X[0..m - 1], Y[0..n - 1]
 
 
def lcs(X, Y, m, n):
    L = [[0] * (n + 2) for i in
         range(m + 2)]
 
    # Following steps build L[m + 1][n + 1]
    # in bottom up fashion. Note that L[i][j]
    # contains length of LCS of X[0..i - 1]
    # and Y[0..j - 1]
    for i in range(m + 1):
 
        for j in range(n + 1):
 
            if (i == 0 or j == 0):
                L[i][j] = 0
 
            elif (X[i - 1] == Y[j - 1]):
                L[i][j] = L[i - 1][j - 1] + 1
 
            else:
                L[i][j] = max(L[i - 1][j],
                              L[i][j - 1])
 
    # L[m][n] contains length of
    # LCS for X[0..n - 1] and Y[0..m - 1]
    return L[m][n]
 
 
# Driver code
X = "AGGTAB"
Y = "GXTXAYB"
 
print("Length of the shortest supersequence is %d"
      % shortestSuperSequence(X, Y))
 
# This code is contributed by Ansu Kumari
#Output


#Length of the shortest supersequence is 9
#Time Complexity: O(m*n).
#Auxiliary Space: O(m*n)
#------------------------------------------------------------------
#Method 2: A simple analysis yields below simple recursive solution.

#Let X[0..m - 1] and Y[0..n - 1] be two 
##strings and m and n be respective
#lengths.

#  if (m == 0) return n;
#  if (n == 0) return m;

#  // If last characters are same, then 
#  // add 1 to result and
#  // recur for X[]
#  if (X[m - 1] == Y[n - 1])
#     return 1 + SCS(X, Y, m - 1, n - 1);

#  // Else find shortest of following two
#  //  a) Remove last character from X and recur
#  //  b) Remove last character from Y and recur
#  else 
#    return 1 + min( SCS(X, Y, m - 1, n), SCS(X, Y, m, n - 1) );
#Below is simple naive recursive solution based on above recursive formula. 


# A Naive recursive python program to find
# length of the shortest supersequence
 
 
def superSeq(X, Y, m, n):
    if (not m):
        return n
    if (not n):
        return m
 
    if (X[m - 1] == Y[n - 1]):
        return 1 + superSeq(X, Y, m - 1, n - 1)
 
    return 1 + min(superSeq(X, Y, m - 1, n),
                   superSeq(X, Y, m, n - 1))
 
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of the shortest supersequence is %d"
      % superSeq(X, Y, len(X), len(Y)))
 
# This code is contributed by Ansu Kumari
#Output
#Length of the shortest supersequence is 9
#Time Complexity: O(2min(m, n)). Since there are overlapping subproblems, 
#Auxiliary Space: O(min(m, n)), due to recursive call stack



#-----------------------------------------------------------
#Method 3: We can efficiently solve this recursive problem using Dynamic Programming.
#Below is the Dynamic Programming-based implementation. 
# A dynamic programming based python program
# to find length of the shortest supersequence

# Returns length of the shortest supersequence of X and Y


def superSeq(X, Y, m, n):
	dp = [[0] * (n + 2) for i in range(m + 2)]

	# Fill table in bottom up manner
	for i in range(m + 1):
		for j in range(n + 1):

			# Below steps follow above recurrence
			if (not i):
				dp[i][j] = j
			elif (not j):
				dp[i][j] = i

			elif (X[i - 1] == Y[j - 1]):
				dp[i][j] = 1 + dp[i - 1][j - 1]

			else:
				dp[i][j] = 1 + min(dp[i - 1][j],
								dp[i][j - 1])

	return dp[m][n]


# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of the shortest supersequence is %d"
	% superSeq(X, Y, len(X), len(Y)))

# This code is contributed by Ansu Kumari
#Output
#Length of the shortest supersequence is 9
#Time Complexity: O(m*n). 
#Auxiliary Space: O(m*n)
#Thanks to Gaurav Ahirwar for suggesting this solution. 
#-------------------------------------------------------------------------
#Method 4 (Top Down Memoization Approach):
#The idea is to follow the simple recursive solution, and use a lookup table to avoid re-computations. Before computing the result for input, we check if the result is already computed or not. If already computed, we return that result.


# A dynamic programming based python program
# to find length of the shortest supersequence
 
# Returns length of the
# shortest supersequence of X and Y
 
def superSeq(X,Y,n,m,lookup):
     
    if m==0 or n==0:
        lookup[n][m] = n+m
 
    if (lookup[n][m] == 0):    
        if X[n-1]==Y[m-1]:
            lookup[n][m] = superSeq(X,Y,n-1,m-1,lookup)+1
     
        else:
            lookup[n][m] = min(superSeq(X,Y,n-1,m,lookup)+1,
                               superSeq(X,Y,n,m-1,lookup)+1)
     
    return lookup[n][m]
     
 
 
# Driver Code
X = "AGGTAB"
Y = "GXTXAYB"
 
lookup = [[0 for j in range(len(Y)+1)]for i in range(len(X)+1)]
print("Length of the shortest supersequence is {}"
      .format(superSeq(X,Y,len(X),len(Y),lookup)))
 
# This code is contributed by Tanmay Ambadkar
#Output
#Length of the shortest supersequence is 9
#Time Complexity: O(n2)
#Auxiliary Space: O(n2)

#Exercise: 
#Extend the above program to print shortest super sequence also using function to print LCS. 