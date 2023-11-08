#Check if two strings are k-anagrams or not

#Given two strings of lowercase alphabets and a value k, the task is to find if two strings are K-anagrams of each other or not.
#Two strings are called k-anagrams if following two conditions are true. 

#Both have same number of characters.
#Two strings can become anagram by changing at most k characters in a string.

#Examples :  

#Input:  str1 = "anagram" , str2 = "grammar" , k = 3
#Output:  Yes
#Explanation: We can update maximum 3 values and 
#it can be done in changing only 'r' to 'n' 
#and 'm' to 'a' in str2.

#Input:  str1 = "geeks", str2 = "eggkf", k = 1
#Output:  No
#Explanation: We can update or modify only 1 
#value but there is a need of modifying 2 characters. 
#i.e. g and f in str 2.


---------------------------------------------------
#Method 1: 

#Below is a solution to check if two strings are k-anagrams of each other or not. 
#Stores occurrence of all characters of both strings in separate count arrays.
#Count number of different characters in both strings (in this if a string has 4 a and second has 3 ‘a’ then it will be also counted.
#If count of different characters is less than or equal to k, then return true else false.


# Python3 program to check if two
# strings are k anagram or not.
MAX_CHAR = 26

# Function to check that is
# k-anagram or not
def arekAnagrams(str1, str2, k) :

	# If both strings are not of equal
	# length then return false
	n = len(str1)
	if (len(str2)!= n) :
		return False

	count1 = [0] * MAX_CHAR
	count2 = [0] * MAX_CHAR

	# Store the occurrence of all
	# characters in a hash_array
	for i in range(n):
		count1[ord(str1[i]) -
			ord('a')] += 1
	for i in range(n):
		count2[ord(str2[i]) -
			ord('a')] += 1
		
	count = 0

	# Count number of characters that
	# are different in both strings
	for i in range(MAX_CHAR):
		if (count1[i] > count2[i]) :
			count = count + abs(count1[i] -
								count2[i])

	# Return true if count is less
	# than or equal to k
	return (count <= k)

# Driver Code
if __name__ == '__main__':
	str1 = "anagram"
	str2 = "grammar"
	k = 2
	if (arekAnagrams(str1, str2, k)):
		print("Yes")
	else:
		print("No")

# This code is contributed
# by SHUBHAMSINGH10
---------------------------------------------------------


#Method 2: We can optimize above solution. Here we use only one count array to store counts of characters in str1. We traverse str2 and decrement occurrence of every character in count array that is present in str2. If we find a character that is not there in str1, we increment count of different characters. If count of different character become more than k, we return false.

#Implementation:


# Optimized Pyt
# Optimized Python3 program
# to check if two strings
# are k anagram or not.
MAX_CHAR = 26;

# Function to check if str1
# and str2 are k-anagram or not
def areKAnagrams(str1, str2, k):
	# If both strings are
	# not of equal length
	# then return false

	n = len(str1);
	if (len(str2) != n):
		return False;

	hash_str1 = [0]*(MAX_CHAR);

	# Store the occurrence of
	# all characters in a hash_array
	for i in range(n):
		hash_str1[ord(str1[i]) - ord('a')]+=1;

	# Store the occurrence of all
	# characters in a hash_array
	count = 0;
	for i in range(n):
		if (hash_str1[ord(str2[i]) - ord('a')] > 0):
			hash_str1[ord(str2[i]) - ord('a')]-=1;
		else:
			count+=1;

		if (count > k):
			return False;

	# Return true if count is
	# less than or equal to k
	return True;

# Driver code
str1 = "fodr";
str2 = "gork";
k = 2;
if (areKAnagrams(str1, str2, k) == True):
	print("Yes");
else:
	print("No");
		
# This code is contributed by mits


























