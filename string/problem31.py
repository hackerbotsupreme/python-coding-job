#Find the longest substring with k unique characters in a given string
#Given a string you need to print longest possible substring that has exactly M unique characters. If there is more than one substring of longest possible length, then print any one of them.

#Examples: 

#Input: Str = “aabbcc”, k = 1
#Output: 2
#Explanation: Max substring can be any one from {“aa” , “bb” , “cc”}.

#Input: Str = “aabbcc”, k = 2
#Output: 4
#Explanation: Max substring can be any one from {“aabb” , “bbcc”}.

#Input: Str = “aabbcc”, k = 3
#Output: 6
#Explanation: 
#There are substrings with exactly 3 unique characters
#{“aabbcc” , “abbcc” , “aabbc” , “abbc” }
#Max is “aabbcc” with length 6.

#Input: Str = “aaabbb”, k = 3
#Output: Not enough unique characters
#Explanation: There are only two unique characters, thus show error message. 

#Source: Google Interview Question.


#--------------------------------------------------------------------------------

#Method 1 (Brute Force) 
#If the length of string is n, then there can be n*(n+1)/2 possible substrings. A simple way is to generate all the substring and check each one whether it has exactly k unique characters or not. If we apply this brute force, it would take O(n2) to generate all substrings and O(n) to do a check on each one. Thus overall it would go O(n3).

#We can further improve this solution by creating a hash table and while generating the substrings, check the number of unique characters using that hash table. Thus it would improve up to O(n2).



// C++ program to find the longest substring
// with k unique characters in a given string

#include <bits/stdc++.h>
using namespace std;

// Function to calculate length of
// longest substring with k characters
void longestKSubstr(string s, int k)
{

	int n = s.length();
	int answer = -1;
	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j <= n; j++) {
			unordered_set<char> distinct(s.begin() + i,
										s.begin() + j);
			if (distinct.size() == k) {
				answer = max(answer, j - i);
			}
		}
	}

	cout << answer;
}

// Driver function
int main()
{
	string s = "aabacbebebe";
	int k = 3;

	// Function Call
	longestKSubstr(s, k);
	return 0;
}

#Output
#7
#Time Complexity: O(n^2) 
#Auxiliary Space: O(n)
#-----------------------------------------------------------------

#Method 2 (Linear Time) 
#The problem can be solved in O(n). Idea is to maintain a window and add elements to the window till it contains less or equal k, update our result if required while doing so. If unique elements exceeds than required in window, start removing the elements from left side. 
#   Below are the implementations of above. The implementations assume that the input string alphabet contains only 26 characters (from ‘a’ to ‘z’). The code can be easily extended to 256 characters. 

# Python program to find the longest substring with k unique
# characters in a given string
MAX_CHARS = 26

# This function calculates number of unique characters
# using a associative array count[]. Returns true if
# no. of characters are less than required else returns
# false.
def isValid(count, k):
	val = 0
	for i in range(MAX_CHARS):
		if count[i] > 0:
			val += 1

	# Return true if k is greater than or equal to val
	return (k >= val)

# Finds the maximum substring with exactly k unique characters
def kUniques(s, k):
	u = 0 # number of unique characters
	n = len(s)

	# Associative array to store the count
	count = [0] * MAX_CHARS

	# Traverse the string, fills the associative array
	# count[] and count number of unique characters
	for i in range(n):
		if count[ord(s[i])-ord('a')] == 0:
			u += 1
		count[ord(s[i])-ord('a')] += 1

	# If there are not enough unique characters, show
	# an error message.
	if u < k:
		print ("Not enough unique characters")
		return

	# Otherwise take a window with first element in it.
	# start and end variables.
	curr_start = 0
	curr_end = 0

	# Also initialize values for result longest window
	max_window_size = 1
	max_window_start = 0

	# Initialize associative array count[] with zero
	count = [0] * len(count)

	count[ord(s[0])-ord('a')] += 1 # put the first character

	# Start from the second character and add
	# characters in window according to above
	# explanation
	for i in range(1,n):

		# Add the character 's[i]' to current window
		count[ord(s[i])-ord('a')] += 1
		curr_end+=1

		# If there are more than k unique characters in
		# current window, remove from left side
		while not isValid(count, k):
			count[ord(s[curr_start])-ord('a')] -= 1
			curr_start += 1

		# Update the max window size if required
		if curr_end-curr_start+1 > max_window_size:
			max_window_size = curr_end-curr_start+1
			max_window_start = curr_start

	print ("Max substring is : " + s[max_window_start:max_window_start + max_window_size]
	+ " with length " + str(max_window_size))

# Driver function
s = "aabacbebebe"
k = 3
kUniques(s, k)

# This code is contributed by BHAVYA JAIN
#Output
#Max substring is : cbebebe with length 7
#Time Complexity: Considering function “isValid()” takes constant time, time complexity of above solution is O(n).
