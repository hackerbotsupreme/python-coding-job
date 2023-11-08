#Length of the longest substring without repeating characters
#Given a string str, find the length of the longest substring without repeating characters. 


#Example:

#For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.

#For “BBBB” the longest substring is “B”, with length 1.


#For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7
#------------------------------------------------------------------------------

#Method 1 (Simple : O(n3)): We can consider all substrings one by one and check for each substring whether it contains all unique characters or not. There will be n*(n+1)/2 substrings. Whether a substring contains all unique characters or not can be checked in linear time by scanning it from left to right and keeping a map of visited characters. 

# Python3 program to find the length
# of the longest substring without
# repeating characters

# This function returns true if all
# characters in str[i..j] are
# distinct, otherwise returns false
def areDistinct(str, i, j):

	# Note : Default values in visited are false
	visited = [0] * (26)

	for k in range(i, j + 1):
		if (visited[ord(str[k]) -
				ord('a')] == True):
			return False
			
		visited[ord(str[k]) -
				ord('a')] = True

	return True

# Returns length of the longest substring
# with all distinct characters.
def longestUniqueSubsttr(str):
	
	n = len(str)
	
	# Result
	res = 0
	
	for i in range(n):
		for j in range(i, n):
			if (areDistinct(str, i, j)):
				res = max(res, j - i + 1)
				
	return res

# Driver code
if __name__ == '__main__':
	
	str = "geeksforgeeks"
	print("The input is ", str)
	
	len = longestUniqueSubsttr(str)
	print("The length of the longest "
		"non-repeating character substring is ", len)

# This code is contributed by mohit kumar 29

#Output
#The input string is geeksforgeeks
#The length of the longest non-repeating character substring is 7
#Time Complexity: O(n^3) since we are processing n^2 substrings with maximum length n.
#Auxiliary Space: O(1)
#------------------------------------------------------------------------
#method 2 (Better : O(n2)) The idea is to use window sliding. Whenever we see repetition, we remove the previous occurrence and slide the window.

# Python3 program to find the
# length of the longest substring
# without repeating characters
def longestUniqueSubsttr(str):
	
	n = len(str)
	
	# Result
	res = 0

	for i in range(n):
		
		# Note : Default values in
		# visited are false
		visited = [0] * 256

		for j in range(i, n):

			# If current character is visited
			# Break the loop
			if (visited[ord(str[j])] == True):
				break

			# Else update the result if
			# this window is larger, and mark
			# current character as visited.
			else:
				res = max(res, j - i + 1)
				visited[ord(str[j])] = True
			
		# Remove the first character of previous
		# window
		visited[ord(str[i])] = False
	
	return res

# Driver code
str = "geeksforgeeks"
print("The input is ", str)

len = longestUniqueSubsttr(str)
print("The length of the longest "
	"non-repeating character substring is ", len)

# This code is contributed by sanjoy_62

# Python3 program to find the
# length of the longest substring
# without repeating characters
def longestUniqueSubsttr(str):
     
    n = len(str)
     
    # Result
    res = 0
  
    for i in range(n):
          
        # Note : Default values in
        # visited are false
        visited = [0] * 256  
  
        for j in range(i, n):
  
            # If current character is visited
            # Break the loop
            if (visited[ord(str[j])] == True):
                break
  
            # Else update the result if
            # this window is larger, and mark
            # current character as visited.
            else:
                res = max(res, j - i + 1)
                visited[ord(str[j])] = True
             
        # Remove the first character of previous
        # window
        visited[ord(str[i])] = False
     
    return res
 
# Driver code
str = "geeksforgeeks"
print("The input is ", str)
 
len = longestUniqueSubsttr(str)
print("The length of the longest "
      "non-repeating character substring is ", len)
 
# This code is contributed by sanjoy_62
#Output
#The input string is geeksforgeeks
#The length of the longest non-repeating character substring is 7
#Time Complexity: O(n^2) since we are traversing each window to remove all repetitions.
#Auxiliary Space: O(1)
#--------------------------------------------------------------------
#Method 3 ( Linear Time ): Using this solution the problem can be solved in linear time using the window sliding technique. Whenever we see repetition, we remove the window till the repeated string.

import math

def longestUniqueSubsttr(str):
	test = ""
	# Result
	maxLength = -1
	
	# Return zero if string is empty
	if (len(str) == 0):
		return 0
	elif(len(str) == 1):
		return 1
	for c in list(str):
		current = "".join(c)
		
		# If string already contains the character
		# Then substring after repeating character
		if (current in test):
			test = test[test.index(current) + 1:]
		test = test + "".join(c)
		maxLength = max(len(test), maxLength)
	return maxLength


# Driver Code
string = "geeksforgeeks"
print("The input string is", string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", length)

# This code is contributed by santeswar.
#Output
#7
#Time Complexity: O(n) since we slide the window whenever we see any repetitions.
#Auxiliary Space: O(1)
#-----------------------------------------------------------------
#Method 4 (Linear Time): Let us talk about the linear time solution now. This solution uses extra space to store the last indexes of already visited characters. The idea is to scan the string from left to right, keep track of the maximum length Non-Repeating Character Substring seen so far in res. When we traverse the string, to know the length of current window we need two indexes. 
#1) Ending index ( j ) : We consider current index as ending index. 
#2) Starting index ( i ) : It is same as previous window if current character was not present in the previous window. To check if the current character was present in the previous window or not, we store last index of every character in an array lasIndex[]. If lastIndex[str[j]] + 1 is more than previous start, then we updated the start index i. Else we keep same i.  

#Below is the implementation of the above approach :

# Python3 program to find the length
# of the longest substring
# without repeating characters
def longestUniqueSubsttr(string):

	# last index of every character
	last_idx = {}
	max_len = 0

	# starting index of current
	# window to calculate max_len
	start_idx = 0

	for i in range(0, len(string)):
	
		# Find the last index of str[i]
		# Update start_idx (starting index of current window)
		# as maximum of current value of start_idx and last
		# index plus 1
		if string[i] in last_idx:
			start_idx = max(start_idx, last_idx[string[i]] + 1)

		# Update result if we get a larger window
		max_len = max(max_len, i-start_idx + 1)

		# Update last index of current char.
		last_idx[string[i]] = i

	return max_len


# Driver program to test the above function
string = "geeksforgeeks"
print("The input string is " + string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character" +
	" substring is " + str(length))


#Output
#The input string is geeksforgeeks
#The length of the longest non-repeating character substring is 7
#Time Complexity: O(n + d) where n is length of the input string and d is number of characters in input string alphabet. For example, if string consists of lowercase English characters then value of d is 26. 
#Auxiliary Space: O(d) 

#-----------------------------------------------------------------------
#Alternate Implementation : 



# Here, we are planning to implement a simple sliding window methodology

def longestUniqueSubsttr(string):
	
	# Creating a set to store the last positions of occurrence
	seen = {}
	maximum_length = 0

	# starting the initial point of window to index 0
	start = 0
	
	for end in range(len(string)):

		# Checking if we have already seen the element or not
		if string[end] in seen:

			# If we have seen the number, move the start pointer
			# to position after the last occurrence
			start = max(start, seen[string[end]] + 1)

		# Updating the last seen value of the character
		seen[string[end]] = end
		maximum_length = max(maximum_length, end-start + 1)
	return maximum_length

# Driver Code
string = "geeksforgeeks"
print("The input string is", string)
length = longestUniqueSubsttr(string)
print("The length of the longest non-repeating character substring is", length)
#Output
#The input String is geeksforgeeks
#The length of the longest non-repeating character substring is 7
#Time Complexity: O(n + d) where n is length of the input string and d is number of characters in input string alphabet. For example, if string consists of lowercase English characters then value of d is 26. 
#Auxiliary Space: O(d) 

#As an exercise, try the modified version of the above problem where you need to print the maximum length NRCS also (the above program only prints the length of it).
#----------------------------------------------------------------------------------
#Method 5 (Linear time):   In this method we will apply  KMP Algorithm technique, to solve the problem. We maintain an Unordered Set to keep track of the maximum non repeating char sub string (Instead of standard LPS array of KMP). When ever we find a repeating char, then we clear the Set and reset len to zero. Rest everything is almost similar to KMP.
# Python3 implementation of the above approach
# instead of len variable we have used leng
# because len is a reserved keyword in python.
# same reason for using string instead of str
def longestSubstrDistinctChars(s):
	if len(s) == 0:
		return 0
	n = len(s)
	st = set()
	leng = 1
	st.add(s[0])
	i = 1
	maxLen = 0
	while i < n:
		# check if consiqutive chars are distinct and non repeating
		if s[i] != s[i - 1] and s[i] not in st:
			st.add(s[i])
			leng += 1
			i += 1
			# back up the max length
			if leng > maxLen:
				maxLen = leng
		else:
			# move forward for repeating chars
			if leng == 1:
				i += 1
			else:
				# reset the substring and set the pivot for next sub string
				st.clear()
				i = i - leng + 1
				leng = 0
	return max(maxLen, leng)

# Driver program to test above function
if __name__ == '__main__':
	string = "abcabcbb"
	print("The input string is " + string)
	leng = longestSubstrDistinctChars(string)
	print("The length of the longest non-repeating character substring " + str(leng))

# this code is contributed by akashish__
#Output#
#The input string is abcabcbb
#The length of the longest non-repeating character substring 3
#Time Complexity : O(n) where n is the input string length

#Auxiliary Space: O(m) where m is the length of the resultant sub string