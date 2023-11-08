#Check if two given Strings are Isomorphic to each other

#Two strings str1 and str2 are called isomorphic if there is a one-to-one mapping possible for every character of str1 to every character of str2. And all occurrences of every character in ‘str1’ map to the same character in ‘str2’.

#Examples: 

#Input:  str1 = “aab”, str2 = “xxy”
#Output: True
#Explanation: ‘a’ is mapped to ‘x’ and ‘b’ is mapped to ‘y’.

#Input:  str1 = “aab”, str2 = “xyz”
#Output: False
#Explanation: One occurrence of ‘a’ in str1 has ‘x’ in str2 and other occurrence of ‘a’ has ‘y’.

----------------------------------------------------
#Naive Approach:

#A Simple Solution is to consider every character of ‘str1’ and check if all occurrences of it map to the same character in ‘str2’. 

#Time Complexity: O(N * N)
#Auxiliary Space: O(1)



#Check if two given strings are isomorphic to each other using Mapping:
#The idea is to create an array to store mappings of processed characters. 

#Follow the steps below to solve the problem:

#If the lengths of str1 and str2 are not same, return false.
#Do the following for every character in str1 and str2.
#If this character is seen first time in str1, then-current of str2 must have not appeared before.
#If the current character of str2 is seen, return false. Mark the current character of str2 as visited.
#Store mapping of current characters.
#Else check if the previous occurrence of str1[i] mapped to the same character.
#Below is the implementation of the above idea :  
# Python program to check if two strings are isomorphic
MAX_CHARS = 256

# This function returns true if str1 and str2 are isomorphic


def areIsomorphic(string1, string2):
	m = len(string1)
	n = len(string2)

	# Length of both strings must be same for one to one
	# correspondence
	if m != n:
		return False

	# To mark visited characters in str2
	marked = [False] * MAX_CHARS

	# To store mapping of every character from str1 to
	# that of str2. Initialize all entries of map as -1
	map = [-1] * MAX_CHARS

	# Process all characters one by one
	for i in xrange(n):

		# if current character of str1 is seen first
		# time in it.
		if map[ord(string1[i])] == -1:

			# if current character of st2 is already
			# seen, one to one mapping not possible
			if marked[ord(string2[i])] == True:
				return False

			# Mark current character of str2 as visited
			marked[ord(string2[i])] = True

			# Store mapping of current characters
			map[ord(string1[i])] = string2[i]

		# If this is not first appearance of current
		# character in str1, then check if previous
		# appearance mapped to same character of str2
		elif map[ord(string1[i])] != string2[i]:
			return False

	return True


# Driver program
print areIsomorphic("aab", "xxy")
# This code is contributed by Bhavya Jain
#Output
True
---------------------------------------------
#Check if two given strings are isomorphic to each other using Hashing:
#The idea is to store the frequency of both strings in the separate array and then check if the frequency of the mapped characters are same or not.

#Follow the steps below to solve the problem:

#First, create two arrays of size 26 to store the frequency of the characters of the strings.
#Now traverse the string and store the count of the characters.
#After storing the count, check whether the count of every ith character of both the strings are same or not.
#Below is the implementation of the above approach.

# Python3 program for the above approach
CHAR = 26

# This function returns true if
# str1 and str2 are isomorphic


def isoMorphic(str1, str2):
	n = len(str1)
	m = len(str2)

	# Length of both strings must be
	# same for one to one correspondence
	if n != m:
		return "False"

	# for counting the previous appearances of character
	# in both the strings
	countChars1 = [0] * CHAR
	countChars2 = [0] * CHAR

	# Process all characters one by one
	for i in range(n):
		countChars1[ord(str1[i]) - ord('a')] += 1
		countChars2[ord(str2[i]) - ord('a')] += 1

	# For string to be isomorphice the
	# previous counts of appearances of
	# current character in both string
	# must be same if it is not same
	# we return false
	for i in range(n):
		if countChars1[ord(str1[i]) - ord('a')] != countChars2[ord(str2[i]) - ord('a')]:
			return "False"

	return "True"


# Driver Code
print(isoMorphic("aab", "xxy"))

# This code is contributed by phasing17
#Output
True
----------------------------------------------
#Check if two given strings are isomorphic to each other using Single Hashmap:
#The idea is to store map the character and check whether the mapping is correct or not

#Follow the steps to solve the problem:

#Create a hashmap of (char, char) to store the mapping of str1 and str2.
#Now traverse on the string and check whether the current character is present in the Hashmap.
#If it is present then the character that is mapped is there at the ith index or not.
#Else check if str2[i] is not present in the key then add the new mapping.
#Else return false.
#Below is the implementation of the above approach
# Python3 program to check if two strings are IsIsomorphic

# this function returns true if str1
# and str2 are isomorphic


def areIsomorphic(str1, str2):
	# initializing a dictionary
	# to store letters from str1 and str2
	# as key value pairs
	charCount = dict()
	# initially setting c to "a"
	c = "a"
	# iterating over str1 and str2
	for i in range(len(str1)):
		# if str1[i] is a key in charCount
		if str1[i] in charCount:
			c = charCount[str1[i]]
			if c != str2[i]:
				return False
		# if str2[i] is not a value in charCount
		elif str2[i] not in charCount.values():
			charCount[str1[i]] = str2[i]
		else:
			return False
	return True


# Driver Code
str1 = "aac"
str2 = "xxy"

# Function Call
if (len(str1) == len(str2) and areIsomorphic(str1, str2)):
	print("True")
else:
	print("False")


# this code is contributed by phasing17


#Output
True




