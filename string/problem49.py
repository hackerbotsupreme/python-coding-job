#Number of distinct words of size N with at most K contiguous vowels
#Difficulty Level : Hard


#Given two integers N and K, the task is to find the number of distinct strings consisting of lowercase alphabets of length N that can be formed with at-most K contiguous vowels. As the answer may be too large, print answer%1000000007.

#Input: N = 1, K = 0
#Output: 21
#Explanation: All the 21 consonants are there which has 0 contiguous vowels and are of length 1.

#Input: N = 1, K = 1
#Output: 26

#Recommended Problem
#Number of distinct words with K maximum contiguous vowels
#Strings
#Dynamic Programming
#+2 more
#Adobe
#Solve Problem
#Submission count: 6.1K
#Approach: The idea to solve this problem is based on dynamic programming. Follow the steps below to solve the problem: 


#Let dp[i][j] be the number of ways to make distinct strings of length i where the last j characters of the string are vowels.
#So the states of dynamic programming are:
#If j = 0, then dp[i][j] = (dp[i-1][0] + dp[i-1][1] +……+ dp[i-1][K])*21(represented by the integer variable sum) because the last added character should be a consonant than only the value of j will become 0 irrespective of its value on previous states.
#If i<j then dp[i][j] = 0. Since it is not possible to create a string containing j vowels and has a length less than j.
#If i == j, then dp[i][j] = 5i because the number of characters in the string is equal to the number of vowels, therefore all the characters should be vowels.
#If j<i then dp[i][j] = dp[i-1][j-1]*5 because a string of length i with last j characters vowel can be made only if the last character is the vowel and the string of length i-1 has last j – 1 character as vowels.
#Print the sum of dp[n][0] + dp[n][1] + …… + dp[n][K] as the answer.
#Below is the implementation of the above Approach


# Python3 program for the above approach
# Python3 program for the above approach

# Power function to calculate
# long powers with mod
def power(x, y, p):
	
	res = 1
	x = x % p

	if (x == 0):
		return 0

	while (y > 0):
		if (y & 1):
			res = (res * x) % p
			
		y = y >> 1
		x = (x * x) % p
		
	return res

# Function for finding number of ways to
# create string with length N and atmost
# K contiguous vowels
def kvowelwords(N, K):

	i, j = 0, 0
	MOD = 1000000007

	# Array dp to store number of ways
	dp = [[0 for i in range(K + 1)]
			for i in range(N + 1)]

	sum = 1
	for i in range(1, N + 1):
		
		#dp[i][0] = (dp[i-1][0]+dp[i-1][1]..dp[i-1][k])*21
		dp[i][0] = sum * 21
		dp[i][0] %= MOD

		# Now setting sum to be dp[i][0]
		sum = dp[i][0]

		for j in range(1, K + 1):
			
			# If j>i, no ways are possible to create
			# a string with length i and vowel j
			if (j > i):
				dp[i][j] = 0
			elif (j == i):
				
				# If j = i all the character should
				# be vowel
				dp[i][j] = power(5, i, MOD)
			else:
				
				# dp[i][j] relation with dp[i-1][j-1]
				dp[i][j] = dp[i - 1][j - 1] * 5

			dp[i][j] %= MOD

			# Adding dp[i][j] in the sum
			sum += dp[i][j]
			sum %= MOD

	return sum
	
# Driver Code
if __name__ == '__main__':
	
	# Input
	N = 3
	K = 3

	# Function Call
	print (kvowelwords(N, K))

# This code is contributed by mohit kumar 29

#Output: 
#17576
 

#Time Complexity: O(N×K)
#Auxiliary Space: O(N×K)


































