#Rabin-Karp Algorithm for Pattern Searching
#Difficulty Level : Medium

#Given a text txt[0. . .n-1] and a pattern pat[0. . .m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

#Examples: 

#Input:  txt[] = “THIS IS A TEST TEXT”, pat[] = “TEST”
#Output: Pattern found at index 10

#Input:  txt[] =  “AABAACAADAABAABA”, pat[] =  “AABA”
#Output: Pattern found at index 0
#              Pattern found at index 9
#              Pattern found at index 12



#Rabin-Karp algorithm

#Approach: To solve the problem follow the below idea:

#The Naive String Matching algorithm slides the pattern one by one. After each slide, one by one checks characters at the current shift, and if all characters match then print the match

#Like the Naive Algorithm, the Rabin-Karp algorithm also slides the pattern one by one. But unlike the Naive algorithm, the Rabin Karp algorithm matches the hash value of the pattern with the hash value of the current substring of text, and if the hash values match then only it starts matching individual characters. So Rabin Karp algorithm needs to calculate hash values for the following strings.



#Pattern itself
#All the substrings of the text of length m
#Since we need to efficiently calculate hash values for all the substrings of size m of text, we must have a hash function that has the following property:

#Hash at the next shift must be efficiently computable from the current hash value and next character in text or we can say hash(txt[s+1 .. s+m]) must be efficiently computable from hash(txt[s .. s+m-1]) and txt[s+m] i.e., hash(txt[s+1 .. s+m]) = rehash(txt[s+m], hash(txt[s .. s+m-1])) and
#Rehash must be O(1) operation.
#Note: The hash function suggested by Rabin and Karp calculates an integer value. The integer value for a string is the numeric value of a string. 
#For example, If all possible characters are from 1 to 10, the numeric value of “122” will be 122. 

#The number of possible characters is higher than 10 (256 in general) and the pattern length can be large. So the numeric values cannot be practically stored as an integer. Therefore, the numeric value is calculated using modular arithmetic to make sure that the hash values can be stored in an integer variable (can fit in memory words). To do rehashing, we need to take off the most significant digit and add the new least significant digit for in hash value. Rehashing is done using the following formula:

#hash( txt[s+1 .. s+m] ) = ( d ( hash( txt[s .. s+m-1]) – txt[s]*h ) + txt[s + m] ) mod q
#hash( txt[s .. s+m-1] ) : Hash value at shift s
#hash( txt[s+1 .. s+m] ) : Hash value at next shift (or shift s+1) 
#d: Number of characters in the alphabet 
#q: A prime number 
#h: d(m-1)

#How does the above expression work? 

#This is simple mathematics, we compute the decimal value of the current window from the previous window. 
##Example: pattern length is 3 and string is “23456” 
#Y#ou compute the value of the first window (which is “234”) as 234. 
#How will you compute the value of the next window “345”? You will do (234 – 2*100)*10 + 5 and get 345.

#Follow the steps mentioned here to implement the idea:

#Initially calculate the hash value of the pattern.
##Start iterating from the starting of the string:
#Calculate the hash value of the current substring having length m.
#If the hash value of the current substring and the pattern are same check if the substring is same as the pattern.
#If they are same, store the starting index as a valid answer. Otherwise, continue for the next substrings.
#Return the starting indices as the required answer.
#Below is the implementation of the above approach:

# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book

# d is the number of characters in the input alphabet
d = 256

# pat -> pattern
# txt -> text
# q -> A prime number


def search(pat, txt, q):
	M = len(pat)
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash value for pattern
	t = 0 # hash value for txt
	h = 1

	# The value of h would be "pow(d, M-1)%q"
	for i in range(M-1):
		h = (h*d) % q

	# Calculate the hash value of pattern and first window
	# of text
	for i in range(M):
		p = (d*p + ord(pat[i])) % q
		t = (d*t + ord(txt[i])) % q

	# Slide the pattern over text one by one
	for i in range(N-M+1):
		# Check the hash values of current window of text and
		# pattern if the hash values match then only check
		# for characters one by one
		if p == t:
			# Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break
				else:
					j += 1

			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
			if j == M:
				print("Pattern found at index " + str(i))

		# Calculate hash value for next window of text: Remove
		# leading digit, add trailing digit
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M])) % q

			# We might get negative values of t, converting it to
			# positive
			if t < 0:
				t = t+q


# Driver Code
if __name__ == '__main__':
	txt = "GEEKS FOR GEEKS"
	pat = "GEEK"

	# A prime number
	q = 101

	# Function Call
	search(pat, txt, q)

# This code is contributed by Bhavya Jain

#Output
#Pattern found at index 0
#Pattern found at index 10
#Time Complexity: 

#The average and best-case running time of the Rabin-Karp algorithm is O(n+m), but its worst-case time is O(nm).
#The worst case of the Rabin-Karp algorithm occurs when all characters of pattern and text are the same as the hash values of all the substrings of txt[] match with the hash value of pat[]. 
#Auxiliary Space: O(1)

#Related Posts: 
#Searching for Patterns | Set 1 (Naive Pattern Searching) 
#Searching for Patterns | Set 2 (KMP Algorithm)
