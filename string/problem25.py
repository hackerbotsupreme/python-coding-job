#Minimum number of times A has to be repeated such that B is a substring of it


#Given two strings A and B. The task is to find the minimum number of times A has to be repeated such that B is a substring of it. If no such solution exists, print -1.

#Examples: 

#Input : A = “abcd”, B = “cdabcdab” 
#Output : 3 
#Repeating A three times (“abcdabcdabcd”), B is a substring of it. B is not a substring of A when it is repeated less than 3 times.

#Input : A = “ab”, B = “cab” 
#Output : -1 
#----------------------------------------------------------------------
#Approach : 
#Imagine we wrote S = A+A+A+… If B is a substring of S, we only need to check whether some index 0 or 1 or …. length(A) -1 starts with B, as S is long enough to contain B, and S has a period of length(A).
#Now, suppose ans is the least number for which length(B) <= length(A * ans). We only need to check whether B is a substring of A * ans or A * (ans+1). If we try k < ans, then B has a larger length than A * ans and therefore can’t be a substring. When k = ans+1, A * k is already big enough to try all positions for B( A[i:i+length(B)] == B for i = 0, 1, …, length(A) – 1).

#Below is the implementation of the above approach: 
# Python3 program to find minimum number
# of times 'A' has to be repeated
# such that 'B' is a substring of it

# Method to find Minimum number
# of times 'A' has to be repeated
# such that 'B' is a substring of it
def min_repetitions(a, b):
	len_a = len(a)
	len_b = len(b)
	
	for i in range(0, len_a):
		
		if a[i] == b[0]:
			k = i
			count = 1
			for j in range(0, len_b):
				
				# we are reiterating over A again and
				# again for each value of B
				# Resetting A pointer back to 0 as B
				# is not empty yet
				if k >= len_a:
					k = 0
					count = count + 1
					
				# Resetting A means count
				# needs to be increased
				if a[k] != b[j]:
					break
				k = k + 1
				
			# k is iterating over A
			else:
				return count
	return -1

# Driver Code
A = 'abcd'
B = 'cdabcdab'
print(min_repetitions(A, B))

# This code is contributed by satycool
#Output


#3
#Time Complexity: O(N * M) 
#Auxiliary Space: O(1).  
#------------------------------------------------------------------
#Approach 2:

#Idea here is to try and find the string using a brute force string searching algorithm (n * m). The only difference here is to calculate the modulus (i % n) when the counter reaches the end of the string.

# Python implementation of this approach
def repeatedStringMatch(A, B):
 
    m = len(A)
    n = len(B)
 
    count = 0
    found = False
 
    for i in range(m):
        j = i
        k = 0
        count = 1
 
        while k < n and A[j] == B[k] :
            if (k == n - 1) :
                found = True
                break
             
            j = (j + 1) % m
 
            if (j == 0):
                count = count + 1
 
            k = k + 1
         
        if (found):
            return count
    return -1
 
# Driver code
A = "abcd";
B = "cdabcdab";
 
print(repeatedStringMatch(A, B));
 
# This code is contributed by shinjanpatra
# Time Complexity: O(N * M) 

#Auxiliary Space: O(1). 

