#Count of substrings of length K with exactly K distinct characters
#Given string str of the lowercase alphabet and an integer K, the task is to count all substrings of length K which have exactly K distinct characters.

#Example:

#Input: str = “abcc”, K = 2 
#Output: 2 
#Explanation: 
#Possible substrings of length K = 2 are 
#ab : 2 distinct characters 
#bc : 2 distinct characters 
#cc : 1 distinct character 
#Only two valid substrings exist {“ab”, “bc”}.

#Input: str = “aabab”, K = 3 
#Output: 0 
#Explanation: 
#Possible substrings of length K = 3 are 
#aab : 2 distinct characters 
#aba : 2 distinct characters 
#bab : 2 distinct characters 
#No substrings of length 3 exist with exactly 3 distinct characters. 
#-----------------------------------------------------------------------------
#Naive approach: 
#The idea is to generate all substrings of length K and, for each substring count, a number of distinct characters. If the length of a string is N, then there can be N – K + 1 substring of length K. Generating these substrings will require O(N) complexity, and checking each substring requires O(K) complexity, hence making the overall complexity like O(N*K).

// C++ program to find the
// count of k length substrings
// with k distinct characters
// using sliding window
#include <bits/stdc++.h>
using namespace std;

// Function to return the
// required count of substrings
int countSubstrings(string s, int K)
{
	int n = s.size();
	int count = 0;
	
	// Generate all the subarray of size K
	for (int i = 0; i < n - K + 1; i++) {
		string s1 = s.substr(i, K);
		unordered_map<char, int> unmap;
		
		for (auto c : s1)
			unmap++;
		
		// Check for any duplicate
		if (unmap.size() == s1.size())
			count++;
	}

	return count;
}

// Driver code
int main()
{
	// string str
	string str = "aabcdabbcdc";

	// integer K
	int K = 3;

	// Print the count of K length
	// substrings with k distinct characters
	cout << countSubstrings(str, K) << endl;

	return 0;
}

#Output
#5
#Time Complexity: O(N*K)
#Auxiliary Space: O(K)
#----------------------------------------------------------------------------
#Efficient approach: 
#The idea is to use Window Sliding Technique. Maintain a window of size K and keep a count of all the characters in the window using a HashMap. Traverse through the string reduces the count of the first character of the previous window and adds the frequency of the last character of the current window in the HashMap. If the count of distinct characters in a window of length K is equal to K, increment the answer by 1.

#Below is the implementation of the above approach: 

# Python3 program to find the
# count of k length substrings
# with k distinct characters
# using sliding window

# Function to return the
# required count of substrings
def countSubstrings(str, K):

	N = len(str)

	# Store the count
	answer = 0

	# Store the count of
	# distinct characters
	# in every window
	map = {}

	# Store the frequency of
	# the first K length substring
	for i in range(K):

		# Increase frequency of
		# i-th character
		map[str[i]] = map.get(str[i], 0) + 1
		
	# If K distinct characters
	# exist
	if (len(map) == K):
		answer += 1

	# Traverse the rest of the
	# substring
	for i in range(K, N):

		# Increase the frequency
		# of the last character
		# of the current substring
		map[str[i]] = map.get(str[i], 0) + 1
		
		# Decrease the frequency
		# of the first character
		# of the previous substring
		map[str[i - K]] -= 1

		# If the character is not present
		# in the current substring
		if (map[str[i - K]] == 0):
			del map[str[i - K]]

		# If the count of distinct
		# characters is 0
		if (len(map) == K):
			answer += 1

	# Return the count
	return answer

# Driver code
if __name__ == '__main__':
	
	str = "aabcdabbcdc"

	# Integer K
	K = 3

	# Print the count of K length
	# substrings with k distinct characters
	print(countSubstrings(str, K))

# This code is contributed by mohit kumar 29

#Output: 
#5
 

#Time Complexity: O(N)
# Auxiliary Space: O(1)

