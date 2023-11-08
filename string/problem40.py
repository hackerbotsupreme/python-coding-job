#Count number of substrings with exactly k distinct characters
#Given a string of lowercase alphabets, count all possible substrings (not necessarily distinct) that has exactly k distinct characters. 

#Examples: 

#Input: abc, k = 2
#Output: 2
#Possible substrings are {“ab”, “bc”}

#Input: aba, k = 2
#Output: 3
#Possible substrings are {“ab”, “ba”, “aba”}
#Input: aa, k = 1
#Output: 3
#Possible substrings are {“a”, “a”, “aa”}
#-----------------------------------------------------------------------
#Method 1 (Brute Force): If the length of string is n, then there can be n*(n+1)/2 possible substrings. A simple way is to generate all the substring and check each one whether it has exactly k unique characters or not. If we apply this brute force, it would take O(n*n) to generate all substrings and O(n) to do a check on each one. Thus overall it would go O(n*n*n) 

#Method 2: The problem can be solved in O(n*n). Idea is to maintain a hash table while generating substring and checking the number of unique characters using that hash table. 
#The implementation below assume that the input string contains only characters from ‘a’ to ‘z’. 

# Python3 program to count number of
# substrings with exactly k distinct
# characters in a given string

# Function to count number of substrings
# with exactly k unique characters
def countkDist(str1, k):
	n = len(str1)
	
	# Initialize result
	res = 0

	# To store count of characters from
	# 'a' to 'z'
	cnt = [0] * 27

	# Consider all substrings beginning
	# with str[i]
	for i in range(0, n):
		dist_count = 0

		# Initializing array with 0
		cnt = [0] * 27

		# Consider all substrings between str[i..j]
		for j in range(i, n):
			
			# If this is a new character for this
			# substring, increment dist_count.
			if(cnt[ord(str1[j]) - 97] == 0):
				dist_count += 1

			# Increment count of current character
			cnt[ord(str1[j]) - 97] += 1

			# If distinct character count becomes k,
			# then increment result.
			if(dist_count == k):
				res += 1
			if(dist_count > k):
				break

	return res	

# Driver Code
if __name__ == "__main__":
	str1 = "abcbaa"
	k = 3
	print("Total substrings with exactly", k,
		"distinct characters : ", end = "")
	print(countkDist(str1, k))

# This code is contributed by
# Sairahul Jella
#Output
#Total substrings with exactly 3 distinct characters :8
#Time Complexity: O(n*n)
#Auxiliary Space: O(1), Only 26 size array is used, which can be considered constant space.
#---------------------------------------------------------------------------------
#Efficient Approach: The idea is to count all the subarrays with at most K distinct characters and then subtract all the subarrays with atmost K – 1 characters. That leaves us with count of subarrays with exactly K distinct characters.

#Below is the implementation of the above approach:

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

// the number of subarrays with at most K distinct elements
int most_k_chars(string& s, int k)
{
	if (s.size() == 0) {
		return 0;
	}
	unordered_map<char, int> map;
	int num = 0, left = 0;

	for (int i = 0; i < s.size(); i++) {
		map[s[i]]++;
		while (map.size() > k) {
			map[s[left]]--;
			if (map[s[left]] == 0) {
				map.erase(s[left]);
			}
			left++;
		}
		num += i - left + 1;
	}
	return num;
}

int exact_k_chars(string& s, int k)
{
	return most_k_chars(s, k) - most_k_chars(s, k - 1);
}

// Driver Program
int main()
{
	string s1 = "pqpqs";
	int k = 2;
	cout << "Total substrings with exactly " << k
		<< " distinct characters : "
		<< exact_k_chars(s1, k) << endl;

	string s2 = "aabab";
	k = 2;
	cout << "Total substrings with exactly " << k
		<< " distinct characters : "
		<< exact_k_chars(s2, k) << endl;
}
#Output
T#otal substrings with exactly 2 distinct characters : 7
#Total substrings with exactly 2 distinct characters : 9
#Time Complexity: O(n)
#Auxiliary Space: O(1)

