#Longest prefix which is also suffix

#Given a string s, find the length of the longest prefix, which is also a suffix. The prefix and suffix should not overlap.

#Examples: 

#Input : aabcdaabc
#Output : 4
#The string "aabc" is the longest
#prefix which is also suffix.

#Input : abcab
#Output : 2

#Input : aaaa
#Output : 2
#----------------------------------------------------------------------------
#Simple Solution: Since overlapping prefixes and suffixes is not allowed, we break the string from the middle and start matching left and right strings. If they are equal return size of one string, else they try for shorter lengths on both sides.
#Below is a solution to the above approach!

# Python3 program to find length
# of the longest prefix which
# is also suffix
def longestPrefixSuffix(s) :
	n = len(s)
	
	for res in range(n // 2, 0, -1) :
		
		# Check for shorter lengths
		# of first half.
		prefix = s[0: res]
		suffix = s[n - res: n]
		
		if (prefix == suffix) :
			return res
			

	# if no prefix and suffix match
	# occurs
	return 0
	
# Driver Code
if __name__ == "__main__":
	s = "blablabla"
	print(longestPrefixSuffix(s))

# This code is contributed by Nikita Tiwari.

#Output: 
#3
 

#Time Complexity: O(n)
#Auxiliary Space: O(1)
#--------------------------------------------------------------------------
#Efficient Solution: The idea is to use the preprocessing algorithm KMP search. In the preprocessing algorithm, we build lps array which stores the following values.

#lps[i] = the longest proper prefix of pat[0..i] 
#which is also a suffix of pat[0..i].
# Efficient Python 3 program
# to find length of
# the longest prefix
# which is also suffix

# Returns length of the longest prefix
# which is also suffix and the two do
# not overlap. This function mainly is
# copy computeLPSArray() of in below post
# https://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
def longestPrefixSuffix(s) :
	n = len(s)
	lps = [0] * n # lps[0] is always 0

	# length of the previous
	# longest prefix suffix
	l = 0
	
	# the loop calculates lps[i]
	# for i = 1 to n-1
	i = 1
	while (i < n) :
		if (s[i] == s[l]) :
			l = l + 1
			lps[i] = l
			i = i + 1
		
		else :

			# (pat[i] != pat[len])
			# This is tricky. Consider
			# the example. AAACAAAA
			# and i = 7. The idea is
			# similar to search step.
			if (l != 0) :
				l = lps[l-1]

				# Also, note that we do
				# not increment i here
			
			else :

				# if (len == 0)
				lps[i] = 0
				i = i + 1

	res = lps[n-1]

	# Since we are looking for
	# non overlapping parts.
	if(res > n/2) :
		return n//2
	else :
		return res
		

# Driver program to test above function
s = "abcab"
print(longestPrefixSuffix(s))


# This code is contributed
# by Nikita Tiwari.
#---------------------------------------------------------------------------------
#Output: 
#2
 

#Time Complexity: O(n) 
#Auxiliary Space: O(n)
#-----------------------------------------------------------------------------
#Solution using RegEx: 
# Python code to find length of the longest
# prefix which is also suffix
import re

s = "ABCABCABCABCABC" # Example input

print(len(re.findall(r'^(\w*).*\1$',s)[0]))
#Output: 
#6
#-----------------------------------------------------------------------------
 

#Efficient Solution: The idea is to traverse the suffix in reverse order and try to find a match in first half of the string (possible prefix). Here we take advantage of the property of a prefix substring – when traversed in reverse order, the prefix substring’s last character will always terminate at the string’s beginning.

#Please note that we search for the prefix in the first half of the string alone because of the constraint given in the problem that the prefix and suffix are non-overlapping.

#Algorithm :

#        1. Maintain two pointers –  one which starts at the end of string(for suffix) and one which starts at the middle of string(for prefix)

#        2. Keep on decrementing both the pointers provided they match and the prefix pointer is not exhausted( >0) .

#        3. When a mismatch occurs, reset the suffix pointer back to end of string and repeat step 2.
#
#        4. When prefix pointer reaches ‘-1’ (i.e. string is exhausted) the longest common suffix/prefix will be the substring from suffix pointer
#
#            to end of the string.  Return the length of this substring. 

#Implementation:


# Python3 program to find length
# Python3 program to find length
# of the longest prefix which
# is also suffix

# Returns length of the longest prefix
# which is also suffix and the two do
# not overlap.
def longestPrefixSuffix(s):

	n = len(s)

	if n == 0:
		return 0

	# end_suffix and end_prefix are used to keep track of the common suffix and prefix respectively.
	# For the prefix we search only in first half of string (0-->n//2-1) since
	# suffix and prefix do not overlap.
	end_suffix = n-1
	end_prefix = n // 2 - 1

	# Traverse each character of suffix from end to start and check for a match of prefix
	# in first half of array.
	while end_prefix >= 0:
		if s[end_prefix] != s[end_suffix]:
			if end_suffix != n-1:
				end_suffix = n-1 # reset end_suffix
			else:
				end_prefix -= 1
		else:
			end_suffix -= 1
			end_prefix -= 1

	# The longest common suffix and prefix is s[end+1:]
	return n-end_suffix-1


# Driver Code
if __name__ == "__main__":
	s = "ABCABCABCABCABC"
	print(longestPrefixSuffix(s))

# This code is contributed by Reshma Koshy.
#Output
#6
#Time Complexity: O(n)
#sAuxiliary Space: O(1)