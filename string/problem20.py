#How to replace a substring of a string
#Given three strings S, S1, and S2 consisting of N, M, and K characters respectively, the task is to modify the string S by replacing all the substrings S1 with the string S2 in the string S.

#Examples:

#Input: S = “abababa”, S1 = “aba”, S2 = “a”
#Output: aba
#Explanation:
#Change the substrings S[0, 2] and S[4, 6](= S1) to the string S2(= “a”) modifies the string S to “aba”. Therefore, print “aba”.

#Input: S = “geeksforgeeks”, S1 = “eek”, S2 = “ok”
#Output: goksforgoks
#---------------------------------------------------------------
#Naive Approach: The simplest approach to solve the given problem is to traverse the string S and when any string S1 is found as a substring in the string S then replace it by S2. Follow the steps below to solve this problem:

#Initialize a string ans to store the resultant string after replacing all the occurrences of the substring S1 to S2 in the string S.
#Iterate over the characters of the string S using variable i and perform the following steps:
#If the prefix substring of the string S is equal to S1 from the index i, then add the string S2 in the string ans.
#Otherwise, add the current character to the string ans.
#After completing the above steps, print the string ans as the result.
#Below is the implementation of the above approach:


#// C++ program for the above approach
// C++ program for the above approach

#include <bits/stdc++.h>
using namespace std;

// Function to calculate the LPS array
// for the given string S1
vector<int> computeLPS(string& s1)
{
	// Stores the longest proper prefix
	// and suffix for each character
	// in the string s1
	vector<int> lps(s1.length());
	int len = 0;

	// Set lps value 0 for the first
	// character of the string s1
	lps[0] = 0;

	int i = 1;

	// Iterate to fill the lps vector
	while (i < s1.length()) {
		if (s1[i] == s1[len]) {
			len = len + 1;
			lps[i] = len;
			i = i + 1;
		}
		else {

			// If there is no longest
			// proper prefix which is
			// suffix, then set lps[i] = 0
			if (len == 0) {
				lps[i] = 0;
				i = i + 1;
			}

			// Otherwise
			else
				len = lps[len - 1];
		}
	}

	return lps;
}

// Function to replace all the occurrences
// of the substring S1 to S2 in string S
void modifyString(string& s, string& s1,
				string& s2)
{
	vector<int> lps = computeLPS(s1);
	int i = 0;
	int j = 0;

	// Stores all the starting index
	// from character S1 occurs in S
	vector<int> found;

	// Iterate to find all starting
	// indexes and store all indices
	// in a vector found
	while (i < s.length()) {
		if (s[i] == s1[j]) {
			i = i + 1;
			j = j + 1;
		}

		// The string s1 occurrence is
		// found and store it in found[]
		if (j == s1.length()) {
			found.push_back(i - j);
			j = lps[j - 1];
		}
		else if (i < s.length()
				&& s1[j] != s[i]) {
			if (j == 0)
				i = i + 1;
			else
				j = lps[j - 1];
		}
	}

	// Stores the resultant string
	string ans = "";
	int prev = 0;

	// Traverse the vector found[]
	for (int k = 0; k < found.size(); k++) {
		if (found[k] < prev)
			continue;
		ans.append(s.substr(prev, found[k] - prev));
		ans.append(s2);
		prev = found[k] + s1.size();
	}

	ans.append(s.substr(prev,
						s.length() - prev));

	// Print the resultant string
	cout << ans << endl;
}

// Driver Code
int main()
{
	string S = "geeksforgeeks";
	string S1 = "eek";
	string S2 = "ok";
	modifyString(S, S1, S2);

	return 0;
}
#Output: 


#goksforgoks
 

#Time Complexity: O(N*M)
#Auxiliary Space: O(N)
#------------------------------------------------------------------
#Efficient Approach: The above approach can also be optimized by creating the longest proper prefix and suffix array for the string S1 and then perform the KMP Algorithm to find the occurrences of the string S1 in the string S. Follow the steps below to solve this problem:

#Create a vector, say lps[] that stores the longest proper prefix and suffix for each character and fill this vector using the KMP algorithm for the string S1.
Initialize two variables say, i and j as 0 to store the position of current character in s and s1 respectively.
#Initialize a vector found to store all the starting indexes from which string S1 occurs in S.
#Iterate over the characters of the string S using variable i and perform the following steps:
#If S[i] is equal to S1[j], then increment i and j by 1.
#If j is equal to the length of s1, then add the value (i – j) to the vector found and update j as lps[j – 1].
#Otherwise, if the value of S[i] is not equal to S1[j], then if j is equal to 0, then increment the value of i by 1. Otherwise, update j as lps[j – 1].
#Initialize a variable say, prev as 0 to store the last changed index and an empty string ans to store the resultant string after replacing all the initial appearances of s1 by s2 in s.
#Traverse the vector found[] and if the value of found[i] is greater than prev, then add the string S2 in place of S1 in ans.
#After completing the above steps, print the string ans as the result.
#Below is the implementation of the above approach:
#// C++ program for the above approach

#include <bits/stdc++.h>
#using namespace std;

// Function to calculate the LPS array
// for the given string S1
vector<int> computeLPS(string& s1)
{
	// Stores the longest proper prefix
	// and suffix for each character
	// in the string s1
	vector<int> lps(s1.length());
	int len = 0;

	// Set lps value 0 for the first
	// character of the string s1
	lps[0] = 0;

	int i = 1;

	// Iterate to fill the lps vector
	while (i < s1.length()) {
		if (s1[i] == s1[len]) {
			len = len + 1;
			lps[i] = len;
			i = i + 1;
		}
		else {

			// If there is no longest
			// proper prefix which is
			// suffix, then set lps[i] = 0
			if (len == 0) {
				lps[i] = 0;
				i = i + 1;
			}

			// Otherwise
			else
				len = lps[len - 1];
		}
	}

	return lps;
}

// Function to replace all the occurrences
// of the substring S1 to S2 in string S
void modifyString(string& s, string& s1,
				string& s2)
{
	vector<int> lps = computeLPS(s1);
	int i = 0;
	int j = 0;

	// Stores all the starting index
	// from character S1 occurs in S
	vector<int> found;

	// Iterate to find all starting
	// indexes and store all indices
	// in a vector found
	while (i < s.length()) {
		if (s[i] == s1[j]) {
			i = i + 1;
			j = j + 1;
		}

		// The string s1 occurrence is
		// found and store it in found[]
		if (j == s1.length()) {
			found.push_back(i - j);
			j = lps[j - 1];
		}
		else if (i < s.length()
				&& s1[j] != s[i]) {
			if (j == 0)
				i = i + 1;
			else
				j = lps[j - 1];
		}
	}

	// Stores the resultant string
	string ans = "";
	int prev = 0;

	// Traverse the vector found[]
	for (int k = 0; k < found.size(); k++) {
		if (found[k] < prev)
			continue;
		ans.append(s.substr(prev, found[k] - prev));
		ans.append(s2);
		prev = found[k] + s1.size();
	}

	ans.append(s.substr(prev,
						s.length() - prev));

	// Print the resultant string
	cout << ans << endl;
}

// Driver Code
int main()
{
	string S = "geeksforgeeks";
	string S1 = "eek";
	string S2 = "ok";
	modifyString(S, S1, S2);

	return 0;
}
##Output: 
#goksforgoks
 

#Time Complexity: O(N + M)
#Auxiliary Space: O(N)

