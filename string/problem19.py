#Count Substrings with equal number of 0s, 1s and 2s

#Given a string that consists of only 0s, 1s and 2s, count the number of substrings that have an equal number of 0s, 1s, and 2s.

#Examples: 

#Input: str = “0102010”
#Output:  2
#Explanation: Substring str[2, 4] = “102” and substring str[4, 6] = “201” has equal number of 0, 1 and 2

#Input: str = “102100211”
#Output: 5

#-----------------------------------------------------
#Recommended Problem
#Equal 0, 1 and 2
#Hash
#Strings
#+1 more
##Solve Problem
#ubmission count: 7.9K
##Brute Force: To solve the problem using this approach follow the below idea:

#Iterate through all substrings of str using nested loops and check whether they contain equal 0,1 and 2 or not.


# Python3 program to find subString with equal
# number of 0's, 1's and 2's

# Method to count number of subString which
# has equal 0, 1 and 2
def getSubStringWithEqual012(s) :
	
	arr = [];
	n = len(s);
		
	# generating subarrays
	for i in range(n):
		for j in range(i, n):
			
			s1 = ""
			for k in range(i, 1 + j):
				s1+=s[k];
				
			arr.append(s1);
				
	count = 0;
	
	# iterating over array of all subStrings
	for i in range(len(arr)):

		countZero=0;
		countOnes=0;
		countTwo=0;
		curs = arr[i];
		
		for j in range(len(curs)):

			if(curs[j] == '0'):
				countZero+=1;
			if(curs[j] == '1'):
				countOnes+=1;
			if(curs[j] == '2'):
				countTwo+=1;
			
		# if number of ones,two and zero are equal in a subString
		if(countZero == countOnes and countOnes == countTwo):
			count += 1;
					
	return count;
	
# Driver's code
Str = "0102010";

# Function call
print(getSubStringWithEqual012(Str));

# This code is contributed by phasing17
#Output


#2
#Time Complexity: O(N3) 
#Auxiliary Space: O(1)
#
# -----------------------------------------------------------------------

#Count Substrings with equal number of 0s, 1s and 2s using Hashing:
#Traverse through the string and keep track of counts of 0, 1, and 2 and make a difference pair of (zeroes – ones, zeroes – twos) and increase the answer count if this difference pair is seen before and at every index increase the count of this difference pair in the map

# Follow the given steps to solve the problem:

#Declare a map to store the difference pair and three variables to store the count of 0’s, 1’s and 2’s 
#Traverse the string and keep track of the count of 0’s, 1’s, and 2’s
#At each index make a difference pair of (zeroes – ones, zeroes – twos)
#Using the map check if this pair is seen before, if it is so then increase the result count
#Then, increase the count of this pair in the map
#Return the result
#Below is the implementation of the above approach:


# Python3 program to find substring with equal
# number of 0's, 1's and 2's
 
# Method to count number of substring which
# has equal 0, 1 and 2
def getSubstringWithEqual012(string):
    N = len(string)
 
    # map to store, how many times a difference
    # pair has occurred previously
    mp = dict()
    mp[(0, 0)] = 1
 
    # zc (Count of zeroes), oc(Count of 1s)
    # and tc(count of twos)
    # In starting all counts are zero
    zc, oc, tc = 0, 0, 0
 
    # looping into string
    res = 0 # Initialize result
    for i in range(N):
 
        # increasing the count of current character
        if string[i] == '0':
            zc += 1
        elif string[i] == '1':
            oc += 1
        else:
            tc += 1 # Assuming that string doesn't contain
                    # other characters
 
        # making pair of differences (z[i] - o[i],
        # z[i] - t[i])
        tmp = (zc - oc, zc - tc)
 
        # Count of previous occurrences of above pair
        # indicates that the subarrays forming from
        # every previous occurrence to this occurrence
        # is a subarray with equal number of 0's, 1's
        # and 2's
        if tmp not in mp:
            res += 0
        else:
            res += mp[tmp]
 
        # increasing the count of current difference
        # pair by 1
        if tmp in mp:
            mp[tmp] += 1
        else:
            mp[tmp] = 1
 
    return res
 
# Driver's Code
if __name__ == "__main__":
    string = "0102010"
    print(getSubstringWithEqual012(string))
 
# This code is contributed by
# sanjeev2552
#Output
2
#Time Complexity: O(N * log N)
#Auxiliary Space: O(N)

#This article is contributed by Utkarsh Trivedi. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks.