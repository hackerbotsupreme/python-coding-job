#Find i’th index character in a binary string obtained after n iterations | Set 2



#Given a decimal number m, convert it into a binary string and apply n iterations, in each iteration 0 becomes “01” and 1 becomes “10”. Find ith(based indexing) index character in the string after nth iteration.
#Examples: 
 

#Input: m = 5 i = 5 n = 3
#Output: 1
#Explanation
#In the first case m = 5, i = 5, n = 3. 
#Initially, the string is  101  ( binary equivalent of 5 )
#After 1st iteration -   100110
#After 2nd iteration - 100101101001
#After 3rd iteration -   100101100110100110010110 
#The character at index 5 is 1, so 1 is the answer

#Input: m = 11 i = 6 n = 4
#Output: 1
#------------------------------------------------------------------------
#A naive approach to this problem has been discussed in the previous post. 
#Efficient algorithm: The first step will be to find which block the i-th character will be after N iterations are performed. In the n’th iteration distance between any two consecutive characters initially will always be equal to 2^n. For a general number m, the number of blocks will be ceil(log m). If M was 3, the string gets divided into 3 blocks. Find the block number in which kth character will lie by k / (2^n), where n is the number of iterations. Consider m=5, then the binary representation is 101. Then the distance between any 2 consecutive marked characters in any i’th iteration will be as follows
#0th iteration: 101, distance = 0 
#1st iteration: 10 01 1 0, distance = 2 
#2nd iteration: 1001 0110 1001, distance = 4 
#3rd iteration: 10010110 01101001 10010110, distance = 8 
#In the example k = 5 and n = 3, so Block_number, when k is 5, will be 0, as 5 / (2^3) = 0
#Initially, block numbers will be 
 

#Original String :    1   0    1
#Block_number    :    0   1    2
#There is no need to generate the entire string, only computing in the block in which the i-th character is present will give the answer. Let this character be root root = s[Block_number], where s is the binary representation of “m”. Now in the final string, find the distance of the kth character from the block number, call this distance as remaining. So remaining = k % (2^n) will be the index of i-th character in the block. If remaining is 0, the root will be the answer. Now, in order to check whether the root is the actual answer use a boolean variable flip which whether we need to flip our answer or not. Following the below algorithm will give the character at the i-th index. 

bool flip = true;
while(remaining > 1){
   if( remaining is odd ) 
        flip = !flip    
   remaining = remaining/2;
}
 



#Below is the implementation of the above approach: 
# Python3 program to find
# i’th Index character in
# a binary string obtained
# after n iterations

# Function to find
# the i-th character
def KthCharacter(m, n, k):

	# distance between two
	# consecutive elements
	# after N iterations
	distance = pow(2, n)
	Block_number = int(k / distance)
	remaining = k % distance

	s = [0] * 32
	x = 0

	# binary representation of M
	while(m > 0) :
		s[x] = m % 2
		m = int(m / 2)
		x += 1
		
	# kth digit will be derived
	# from root for sure
	root = s[x - 1 - Block_number]
	
	if (remaining == 0):
		print(root)
		return
	
	# Check whether there
	# is need to flip root
	# or not
	flip = True
	while (remaining > 1):
		if (remaining & 1):
			flip = not(flip)
		
		remaining = remaining >> 1
	
	if (flip) :
		print(not(root))
	
	else :
		print(root)
	
# Driver Code
m = 5
k = 5
n = 3
KthCharacter(m, n, k)

# This code is contributed
# by smita
#Output: 
#1
 

#Time Complexity: O(log Z), where Z is the distance between initially consecutive bits after N iterations
#Auxiliary Space: O(1) 
 
 