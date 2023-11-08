#Sum of two large numbers
#Given two numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find sum of these two numbers.

#Examples: 

#Input  : str1 = "3333311111111111", 
#         str2 =   "44422222221111"
#Output : 3377733333332222

#Input  : str1 = "7777555511111111", 
#         str2 =    "3332222221111"
#Output : 7780887733332222
#-------------------------------------------------------------------
#The idea is based on school mathematics. We traverse both strings from end, one by one add digits and keep track of carry. To simplify the process, we do following: 
#1) Reverse both strings. 
#2) Keep adding digits one by one from 0’th index (in reversed strings) to end of smaller string, append the sum % 10 to end of result and keep track of carry as sum/10. 
#3) Finally reverse the result. 


# Python3 program to find sum of
# two large numbers.

# Function for finding sum of
# larger numbers
def findSum(str1, str2):
	
	# Before proceeding further,
	# make sure length of str2 is larger.
	if (len(str1) > len(str2)):
		t = str1;
		str1 = str2;
		str2 = t;

	# Take an empty string for
	# storing result
	str = "";

	# Calculate length of both string
	n1 = len(str1);
	n2 = len(str2);

	# Reverse both of strings
	str1 = str1[::-1];
	str2 = str2[::-1];

	carry = 0;
	for i in range(n1):
		
		# Do school mathematics, compute
		# sum of current digits and carry
		sum = ((ord(str1[i]) - 48) +
			((ord(str2[i]) - 48) + carry));
		str += chr(sum % 10 + 48);

		# Calculate carry for next step
		carry = int(sum / 10);

	# Add remaining digits of larger number
	for i in range(n1, n2):
		sum = ((ord(str2[i]) - 48) + carry);
		str += chr(sum % 10 + 48);
		carry = (int)(sum / 10);

	# Add remaining carry
	if (carry):
		str += chr(carry + 48);

	# reverse resultant string
	str = str[::-1];

	return str;

# Driver code
str1 = "12";
str2 = "198111";
print(findSum(str1, str2));

# This code is contributed by mits

#Output: 

#198123
#Time Complexity: O(n1+n2) where n1 and n2 are lengths of two input strings representing numbers.

#Auxiliary Space: O(max(n1, n2))

#Optimization: 
#We can avoid the first two string reverse operations by traversing them from the end. Below is the optimized solution. 
#--------------------------------------------------------------------
# python 3 program to find sum of two large numbers.

# Function for finding sum of larger numbers
def findSum(str1, str2):

	# Before proceeding further, make sure length
	# of str2 is larger.
	if len(str1)> len(str2):
		temp = str1
		str1 = str2
		str2 = temp

	# Take an empty string for storing result
	str3 = ""

	# Calculate length of both string
	n1 = len(str1)
	n2 = len(str2)
	diff = n2 - n1

	# Initially take carry zero
	carry = 0

	# Traverse from end of both strings
	for i in range(n1-1,-1,-1):
	
		# Do school mathematics, compute sum of
		# current digits and carry
	
		sum = ((ord(str1[i])-ord('0')) +
				int((ord(str2[i+diff])-ord('0'))) + carry)
	
		str3 = str3+str(sum%10 )
		
		
		carry = sum//10

	# Add remaining digits of str2[]
	for i in range(n2-n1-1,-1,-1):
	
		sum = ((ord(str2[i])-ord('0'))+carry)
		str3 = str3+str(sum%10 )
		carry = sum//10

	# Add remaining carry
	if (carry):
		str3+str(carry+'0')

	# reverse resultant string
	str3 = str3[::-1]

	return str3

# Driver code
if __name__ == "__main__":
	str1 = "12"
	str2 = "198111"
	print(findSum(str1, str2))

# This code is contributed by ChitraNayal
#Output:

#198123
#Time Complexity: O(max(n1, n2)) where n1 and n2 are lengths of two input strings representing numbers.

#Auxiliary Space: O(max(n1, n2))