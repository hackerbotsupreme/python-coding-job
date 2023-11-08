#Encrypt the string – 2
#Given a string S consisting of N, lower case English alphabet, it is also given that a string is encrypted by first replacing every substring of the string consisting of the same character with the concatenation of that character and the hexadecimal representation of the size of the substring and then revering the whole string, the task is to find the encrypted string. 

#Examples:

#Input: S = “aaaaaaaaaaa”
#Output: ba  
#Explanation:


#First convert the given string to “a11” i.e. write, character along with its frequency.
$
#Then, change “a11” to “ab” because 11 is b in hexadecimal.
#Then, finally reverse the string i.e “ba”.
#Input: S = “abc”
#Output: 1c1b1a
-------------------------------------------------------------
 
#Approach: The problem can be solved by iterating over the characters of the string S. Follow the steps below to solve this problem:

#Initialize an empty string say, ans to store the answer.
#Iterate over the characters of the string S, using the variable i, and perform the following steps:
#Find the count of a substring with the same character, S[i], starting from index i and store it in a variable, say, count.
#Now convert the count to hexadecimal representation, and append the character S[i] along with its frequencies hexadecimal representation.
#Finally, reverse the string ans and then print it.
#Below is the implementation of the above approach:


# Python3 program for the above approach

# Function to convert Decimal to Hex
def convertToHex(num):

	temp = ""
	while (num != 0):
		rem = num % 16
		c = 0
		
		if (rem < 10):
			c = rem + 48
		else:
			c = rem + 87
			
		temp += chr(c)
		num = num // 16

	return temp

# Function to encrypt the string
def encryptString(S, N):

	ans = ""
	i = 0

	# Iterate the characters
	# of the string
	while (i<N): #changed from for i in range(N)
		ch = S[i]
		count = 0

		# Iterate until S[i] is equal to ch
		while (i < N and S[i] == ch):

			# Update count and i
			count += 1
			i += 1

		# Decrement i by 1
		#i -= 1 # not required

		# Convert count to hexadecimal
		# representation
		hex = convertToHex(count)

		# Append the character
		ans += ch

		# Append the characters frequency
		# in hexadecimal representation
		ans += hex

	# Reverse the obtained answer
	ans = ans[::-1]
	
	# Return required answer
	return ans

# Driver Code
if __name__ == '__main__':
	
	# Given Input
	S = "aaaaaaaaaaa"
	N = len(S)

	# Function Call
	print(encryptString(S, N))

# This code is contributed by mohit kumar 29


