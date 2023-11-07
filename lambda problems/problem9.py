#sorting string using order defined by another string.


#Given two strings (of lowercase letters), a pattern, and a string. The task is to sort strings according to the order defined by the pattern. It may be assumed that the pattern has all characters of the string and all characters in the pattern appear only once.
#Examples: 

#Input  : pat = "bca", str = "abc"
#Output : str = "bca"

#Input  : pat = "bxyzca", str = "abcabcabc"
#Output : str = "bbbcccaaa"

#Input  : pat = "wcyuogmlrdfphitxjakqvzbnes", str = "jcdokai"
#Output : str = "codijak"

#Approach 1: The idea is to first count occurrences of all characters in str and store these counts in a count array. Then traverse pattern from left to right, and for each character pat[i], see how many times it appears in count array and copy this character these many times to str.
#Below is the implementation of the above idea. 


# Python3 program to sort a string according to
# the order defined by a pattern string
MAX_CHAR = 26

# Sort str according to the order defined by pattern.
def sortByPattern(str, pat):
	
	global MAX_CHAR
	
	# Create a count array store count
	# of characters in str.
	count = [0] * MAX_CHAR
	
	# Count number of occurrences of
	# each character in str.
	for i in range (0, len(str)):
		count[ord(str[i]) - 97] += 1
	
	# Traverse the pattern and print every characters
	# same number of times as it appears in str. This
	# loop takes O(m + n) time where m is length of
	# pattern and n is length of str.
	index = 0;
	str = ""
	
	for i in range (0, len(pat)):
		j = 0
		while(j < count[ord(pat[i]) - ord('a')]):
			str += pat[i]
			j = j + 1
			index += 1
	
	return str

# Driver code
pat = "bca"
str = "abc"
print(sortByPattern(str, pat))

# This code is contributed by ihritik
