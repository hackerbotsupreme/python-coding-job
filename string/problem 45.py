#Reduce the string by removing K consecutive identical characters
#Given a string str and an integer K, the task is to reduce the string by applying the following operation any number of times until it is no longer possible:

#Choose a group of K consecutive identical characters and remove them from the string.

#Finally, print the reduced string.

#Examples:  


#Input: K = 2, str = “geeksforgeeks” 
##Output: gksforgks 
#Explanation: After removal of both occurrences of the substring “ee”, the string reduces to “gksforgks”.

#Input: K = 3, str = “qddxxxd” 
#Output: q 
#Explanation: 
#Removal of “xxx” modifies the string to “qddd”. 
#Again, removal of “ddd”modifies the string to “q”. 

#----------------------------------------------------------------------


#Approach: This problem can be solved using the Stack data structure. Follow the steps below to solve the problem:
#Initialize a stack of pair<char, int>, to store characters and their respective consecutive frequencies.
#Iterate over the characters of the string.
#If the current character is different from the character present currently at the top of the stack, then set its frequency to 1.
#Otherwise, if the current character is the same as the character at the top of the stack, then increase its frequency by 1.
#If the frequency of the character at the top of the stack is K, pop that out of the stack.
#Finally, print the characters which are remaining in the stack as the resultant string.

# Python3 implementation of the approach

# Pair class to store character and freq
class Pair:
	def __init__(self,c ,ctr):
		self.c= c
		self.ctr = ctr

class Solution:
	
	# Function to find the reduced string
	def reduced_String(self , k , s):
		
		#Base Case
		if (k == 1):
			return ""

		# Creating a stack of type Pair
		st = []
	
		# iterate through given string
		for i in range(len(s)):
			
			# if stack is empty then simply add the
			# character with count 1 else check if
			# character is same as top of stack
			if (len(st) == 0):
				st.append((Pair(s[i] , 1)))
				continue
				
			
			# if character at top of stack is same as
			# current character increase the number of
			# repetitions in the top of stack by 1
			if (st[-1].c == s[i]):
				
				pair = st.pop()
				pair.ctr +=1
				
				if (pair.ctr == k):
					continue
				
				else:
					st.append(pair)
	
			
			else:
				
				# if character at top of stack is not
				# same as current character push the
				# character along with count 1 into the
				# top of stack
				st.append((Pair(s[i] , 1)))
	
	
		# Iterate through the stack
		# Use string(int,char) in order to replicate the
		# character multiple times and convert into string
		# then add in front of output string
		ans = ""
		while(len(st) > 0):
			
			c = st[-1].c
			cnt = st[-1].ctr
			
			while(cnt >0):
				ans = c + ans
				cnt -= 1
			
			st.pop()
		
		return (ans)

# Driver code
if __name__ == "__main__":
	
	k = 2
	s = "geeksforgeeks"
	obj = Solution()
	print(obj.reduced_String(k,s))

	# This code is contributed by chantya17.

#Output
#gksforgks
#Time Complexity: O(N) 