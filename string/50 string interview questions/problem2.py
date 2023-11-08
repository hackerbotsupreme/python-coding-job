#Longest Common Prefix using Sorting


#Problem Statement: Given a set of strings, find the longest common prefix.
#Examples: 
 

#Input: {"geeksforgeeks", "geeks", "geek", "geezer"}
#Output: "gee"

#Input: {"apple", "ape", "april"}
#Output: "ap"


#The longest common prefix for an array of strings is the common prefix between 2 most dissimilar strings. For example, in the given array {“apple”, “ape”, “zebra”}, there is no common prefix because the 2 most dissimilar strings of the array “ape” and “zebra” do not share any starting characters. 
#We have discussed five different approaches in below posts. 
 

#Word by Word Matching
#Character by Character Matching
#Divide and Conquer
#Binary Search.
#Using Trie)


# Python 3 program to find longest
# common prefix of given array of words.
def longestCommonPrefix( a):
	
	size = len(a)

	# if size is 0, return empty string
	if (size == 0):
		return ""

	if (size == 1):
		return a[0]

	# sort the array of strings
	a.sort()
	
	# find the minimum length from
	# first and last string
	end = min(len(a[0]), len(a[size - 1]))

	# find the common prefix between
	# the first and last string
	i = 0
	while (i < end and
		a[0][i] == a[size - 1][i]):
		i += 1

	pre = a[0][0: i]
	return pre

# Driver Code
if __name__ == "__main__":

	input = ["geeksforgeeks", "geeks",
					"geek", "geezer"]
	print("The longest Common Prefix is :" ,
				longestCommonPrefix(input))

# This code is contributed by ita_c



#Output: 
 

#The longest common prefix is : gee
#Time Complexity: O(MAX * n * log n ) where n is the number of strings in the array and MAX is maximum number of characters in any string. Please note that comparison of two strings would take at most O(MAX) time and for sorting n strings, we would need O(MAX * n * log n ) time.


































