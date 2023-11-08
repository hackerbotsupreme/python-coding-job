#Longest substring whose characters can be rearranged to form a Palindrome
#Difficulty Level : Hard

#Given a string S of length N which only contains lowercase alphabets. Find the length of the longest substring of S such that the characters in it can be rearranged to form a palindrome. 

#Examples:

#Input: S = “aabe”
#Output: 3
##Explanation:
#The substring “aab” can be rearranged to form “aba”, which is a palindromic substring.
#Since the length of “aab” is 3 so output is 3.
#Notice that “a”, “aa”, “b” and “e” can be arranged to form palindromic strings, but they are not longer than “aab”.

#Input: S = “adbabd”
#Output: 6
#Explanation:
#The whole string “adbabd” can be rearranged to form a palindromic substring. One possible arrangement is “abddba”.
#Therefore, output length of the string i.e., 6.


#Recommended Problem
#Longest substring to form a Palindrome
#Strings
#Dynamic Programming
#+3 more
#Amazon
#Samsung
#Solve Problem
#Submission count: 5.6K
#Naive Approach: The idea is to generate all possible substring and keep count of each character in it. Initialize answer with the value 0. If the count of each character is even with at most one character with the odd occurrence, the substring can be re-arranged to form a palindromic string. If a substring satisfies this property then update the answer. Print the maximum length after the above steps. 

#Below is the implementation of the above approach:


# Python code for the above approach
# Python code for the above approach

# function to check if the string can be
# rearranged to a palindromic string or not
def ispalindromic(s):
	n = len(s)
	
	# hashmap to count the frequency of
	# every character in given substring
	hashmap={}
	for ch in s:
		if(ch in hashmap):
			hashmap[ch] = hashmap[ch] + 1
		else:
			hashmap[ch] = 1
	
	count = 0
	
	# Count of characters having odd frequency
	for key in hashmap:
		if(hashmap[key]%2 == 1):
			count += 1
	
	# if count is greater than 1
	if(count > 1):
		return False
	
	return True
	
# Function to get the length of longest
# substring whose characters can be
# arranged to form a palindromic string
def longestSubstring(S, n):
	ans = 0
	
	for i in range(len(S)):
		curstr = ""
		for j in range(i,len(S)):
			# Storing the substring
			curstr += S[j]
			
			# Checking if it is possible to
			# make it a palindrome
			if(ispalindromic(curstr) == True):
				# Storing the maximum answer
				ans = max(ans, j - i + 1)
	
	return ans
	
# Driver code

# Given String
s = "adbabd"

# Length of given string
n = len(s)

# Function call
print(longestSubstring(s,n))

# This code is contributed by Pushpesh Raj.
#Output


#6
#Time Complexity: O(N3 * 26)
#Auxiliary Space: O(N2 * 26)
#----------------------------------------------------------
Efficient Approach: The idea is to observe that the string is a palindrome if at most one character occurs an odd number of times. So there is no need to keep the total count of each character. Just knowing that it is occurring even or an odd number of times is enough. To do this, use bit masking since the count of lowercase alphabets is only 26.

Define a bitmask variable mask which tracks if the occurrence of each character is even or odd.
Create a dictionary index that keeps track of the index of each bitmask.
Traverse the given string S. First, convert the characters from ‘a’ – ‘z’ to 0 – 25 and store this value in a variable temp. For each occurrence of the character, take Bitwise XOR of 2temp with the mask.
If the character occurs even number of times, its bit in the mask will be off else it will be on. If the mask is currently not in the index, simply assign present index i to bitmask mask in the index.
If the mask is present in the index it means that from the index[mask] to i, the occurrence of all characters is even which is suitable for a palindromic substring. Therefore, update the answer if the length of this segment from the index[mask] to i is greater than the answer.
To check for the substring with one character occurring an odd number of times, iterate a variable j over [0, 25]. Store Bitwise XOR of x with 2j in mask2. 
If mask2 is present in the index, this means that this character is occurring an odd number of times and all characters occur even a number of times in the segment index[mask2] to i, which is also a suitable condition for a palindromic string. Therefore, update our answer with the length of this substring if it is greater than the answer.
Print the maximum length of substring after the above steps.
Below is the implementation of the above approach:


# Python3 program for the above approach
 
# Function to get the length of longest
# substring whose characters can be
# arranged to form a palindromic string
def longestSubstring(s: str, n: int):
 
    # To keep track of the last
    # index of each xor
    index = dict()
 
    # Initialize answer with 0
    answer = 0
 
    mask = 0
    index[mask] = -1
 
    # Now iterate through each character
    # of the string
    for i in range(n):
 
        # Convert the character from
        # [a, z] to [0, 25]
        temp = ord(s[i]) - 97
 
        # Turn the temp-th bit on if
        # character occurs odd number
        # of times and turn off the temp-th
        # bit off if the character occurs
        # ever number of times
        mask ^= (1 << temp)
 
        # If a mask is present in the index
        # Therefore a palindrome is
        # found from index[mask] to i
        if mask in index.keys():
            answer = max(answer,
                         i - index[mask])
 
        # If x is not found then add its
        # position in the index dict.
        else:
            index[mask] = i
 
        # Check for the palindrome of
        # odd length
        for j in range(26):
 
            # We cancel the occurrence
            # of a character if it occurs
            # odd number times
            mask2 = mask ^ (1 << j)
            if mask2 in index.keys():
 
                answer = max(answer,
                             i - index[mask2])
 
    return answer
 
 
# Driver Code
 
# Given String
s = "adbabd"
 
# Length of given string
n = len(s)
 
# Function call
#print(longestSubstring(s, n))
#Output
#6
#Time Complexity: O(N * 26)
#Auxiliary Space: O(N * 26)