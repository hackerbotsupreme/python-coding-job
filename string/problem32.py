#Smallest window in a String containing all characters of other String



#Given two strings, string and pattern, the task is to find the smallest substring in string containing all characters of pattern. 

#Examples: 

#Input: string = “this is a test string”, pattern = “tist” 
#Output: “t stri” 
#Explanation: “t stri” contains all the characters of pattern.

#Input: string = “geeksforgeeks”, pattern = “ork” 
#Output: “ksfor”


#--------------------------------------------------------------------------------------
#Naive Approach:

#Generate all substrings of string.
#For each substring, check whether the substring contains all characters of pattern (“tist”) 
#Finally, print the smallest substring containing all characters of pattern.
#Time Complexity: O(N3)
#Auxiliary Space: O(N) to create substrings.

#Smallest window in a String containing all characters of other String using Hashing:
#The idea is to use the two pointer approach on the hash array of pattern string and then find the minimum window by eliminating characters from the start of the window.



#Follow the steps below to solve the problem:

#First check if the length of the string is less than the length of the given pattern, if yes then “no such window can exist “.
#Store the occurrence of characters of the given pattern in a hash array (say, hash_pat[]).
#We will be using two pointer technique basically
#Start matching the characters of the pattern with the characters of the string i.e. increment count if a character matches.
#Check if (count == length of pattern ) this means a window is found.
#If such a window is found, try to minimize it by removing extra characters from the beginning of the current window.
#Delete one character from the first and again find this deleted key at right.
#If found, then again check if count and pattern length are same and repeat the process.
#Update min_length.
#Print the minimum length window.
#See the image below for a better understanding:

#Illustration:

#smallest-window
#after the second image(array) our left pointer should be at s and then find I at right and then apply step5 (basically one step has not been shown)

#Below is the implementation of the above aapproach.


# Python3 program to find the smallest window
# containing all characters of a pattern.
no_of_chars = 256
 
# Function to find smallest window
# containing all characters of 'pat'
def findSubString(string, pat):
 
    len1 = len(string)
    len2 = len(pat)
 
    # Check if string's length is
    # less than pattern's
    # length. If yes then no such
    # window can exist
    if len1 < len2:
 
        print("No such window exists")
        return ""
 
    hash_pat = [0] * no_of_chars
    hash_str = [0] * no_of_chars
 
    # Store occurrence ofs characters of pattern
    for i in range(0, len2):
        hash_pat[ord(pat[i])] += 1
 
    start, start_index, min_len = 0, -1, float('inf')
 
    # Start traversing the string
    count = 0  # count of characters
    for j in range(0, len1):
 
        # count occurrence of characters of string
        hash_str[ord(string[j])] += 1
 
        # If string's char matches with
        # pattern's char then increment count
        if (hash_str[ord(string[j])] <=
                hash_pat[ord(string[j])]):
            count += 1
 
        # if all the characters are matched
        if count == len2:
 
            # Try to minimize the window
            while (hash_str[ord(string[start])] >
                   hash_pat[ord(string[start])] or
                   hash_pat[ord(string[start])] == 0):
 
                if (hash_str[ord(string[start])] >
                        hash_pat[ord(string[start])]):
                    hash_str[ord(string[start])] -= 1
                start += 1
 
            # update window size
            len_window = j - start + 1
            if min_len > len_window:
 
                min_len = len_window
                start_index = start
 
    # If no window found
    if start_index == -1:
        print("No such window exists")
        return ""
 
    # Return substring starting from
    # start_index and length min_len
    return string[start_index: start_index + min_len]
 
 
# Driver code
if __name__ == "__main__":
 
    string = "this is a test string"
    pat = "tist"
 
    print(findSubString(string, pat))
 
# This code is contributed by Rituraj Jain
#Output
#t stri
#Time Complexity:  O(N), where N is the length of string. 
#Auxiliary Space: O(1)

#------------------------------------------------------------------------------
#Smallest window in a string containing all characters of other string using Sliding Window:
#The idea is to use the sliding window technique whenever any window contains all the characters of the pattern string then start minimizing it from the start of the window.

#Follow the steps below to solve the problem:

#Make a hash array of size 256.
#First store the frequency of every character of pattern string.
#Then loop over the string and decrement the frequency from the hash array.
#When count variable equals to zero then start minimizing the window.
#Below is the implementation of the above approach:


''' Python solution '''
 
 
def smallestWindow(s, p):
    n = len(s)
    if n < len(p):
        return -1
    mp = [0]*256
 
    # Starting index of ans
    start = 0
 
    # Answer
    # Length of ans
    ans = n + 1
    cnt = 0
 
    # creating map
    for i in p:
        mp[ord(i)] += 1
        if mp[ord(i)] == 1:
            cnt += 1
 
     # References of Window
    j = 0
    i = 0
 
    # Traversing the window
    while(j < n):
 
      # Calculating
        mp[ord(s[j])] -= 1
        if mp[ord(s[j])] == 0:
            cnt -= 1
 
            # Condition matching
            while cnt == 0:
                if ans > j - i + 1:
 
                  # calculating answer.
                    ans = j - i + 1
                    start = i
 
                 # Sliding I
                # Calculation for removing I
                mp[ord(s[i])] += 1
                if mp[ord(s[i])] > 0:
                    cnt += 1
                i += 1
        j += 1
    if ans > n:
        return "-1"
    return s[start:start+ans]
 
 
# Driver code
if __name__ == "__main__":
    s = "this is a test string"
    p = "tist"
    result = smallestWindow(s, p)
    print(result)
 
    # This code is contributed by cyclades.
#Output
#t stri
#Time Complexity:  O(N), where N is the length of string s. 
#Auxiliary Space: O(1)