#Find Excel column name from a given column number
#MS Excel columns have a pattern like A, B, C, …, Z, AA, AB, AC, …., AZ, BA, BB, … ZZ, AAA, AAB ….. etc. In other words, column 1 is named “A”, column 2 as “B”, and column 27 as “AA”.
#Given a column number, find its corresponding Excel column name. The following are more examples.

#Input          Output
# 26             Z
# 51             AY
# 52             AZ
# 80             CB
# 676            YZ
# 702            ZZ
# 705            AAC
#-----------------------------------------------------------------------------
#Thanks to Mrigank Dembla for suggesting the below solution in a comment.
#Suppose we have a number n, let’s say 28. so corresponding to it we need to print the column name. We need to take the remainder with 26. 

#If the remainder with 26 comes out to be 0 (meaning 26, 52, and so on) then we put ‘Z’ in the output string and new n becomes n/26 -1 because here we are considering 26 to be ‘Z’ while in actuality it’s 25th with respect to ‘A’.

#Similarly, if the remainder comes out to be non-zero. (like 1, 2, 3, and so on) then we need to just insert the char accordingly in the string and do n = n/26.


#Finally, we reverse the string and print. 

#Example: 
#n = 700
#The remainder (n%26) is 24. So we put ‘X’ in the output string and n becomes n/26 which is 26. 
#Remainder (26%26) is 0. So we put ‘Z’ in the output string and n becomes n/26 -1 which is 0.

#Following is the implementation of the above approach.


# Python program to find Excel column name from a
# given column number

MAX = 50

# Function to print Excel column name
# for a given column number
def printString(n):

	# To store result (Excel column name)
	string = ["\0"] * MAX

	# To store current index in str which is result
	i = 0

	while n > 0:
		# Find remainder
		rem = n % 26

		# if remainder is 0, then a
		# 'Z' must be there in output
		if rem == 0:
			string[i] = 'Z'
			i += 1
			n = (n / 26) - 1
		else:
			string[i] = chr((rem - 1) + ord('A'))
			i += 1
			n = n / 26
	string[i] = '\0'

	# Reverse the string and print result
	string = string[::-1]
	print "".join(string)

# Driver program to test the above Function
printString(26)
printString(51)
printString(52)
printString(80)
printString(676)
printString(702)
printString(705)

# This code is contributed by BHAVYA JAIN
#Output
#Z
#AY
#AZ
#CB
#YZ
#ZZ
#AAC
#Time Complexity: O(log26n), as we are using a loop and in each traversal, we decrement by floor division of 26.

#Auxiliary Space: O(50), as we are using extra space for storing the result.
#Method 2 
##The problem is similar to converting a decimal number to its binary representation but instead of a binary base system where we have two digits only 0 and 1, here we have 26 characters from A-Z.
#So, we are dealing with base 26 instead of base binary. 
#That’s not where the fun ends, we don’t have zero in this number system, as A represents 1, B represents 2 and so on Z represents 26. 
#To make the problem easily understandable, we approach the problem in two steps:
#---------------------------------------------------------------------------
#Convert the number to base 26 representation, considering we have 0 also in the system.
#Change the representation to the one without having 0 in its system.
#HOW? Here is an example

#Step 1: 
#Consider we have number 676, How to get its representation in the base 26 system? In the same way, we do for a binary system, Instead of division and remainder by 2, we do division and remainder by 26.

#Base 26 representation of 676 is : 100 
#Step2
#But Hey, we can’t have zero in our representation. Right? Because it’s not part of our number system. How do we get rid of zero? Well it’s simple, but before doing that let’s remind one simple math trick:


#Subtraction: 
#5000 - 9, How do you subtract 9 from 0 ? You borrow
#from next significant bit, right.  
#In a decimal number system to deal with zero, we borrow 10 and subtract 1 from the next significant.
#In the Base 26 Number System to deal with zero, we borrow 26 and subtract 1 from the next significant bit.
#So Convert 10026 to a number system that does not have ‘0’, we get (25 26)26 
#Symbolic representation of the same is: YZ 

#Here is the implementation of the same:
def printString(n):
	
	arr = [0] * 10000
	i = 0

	# Step 1: Converting to number
	# assuming 0 in number system
	while (n > 0):
		arr[i] = n % 26
		n = int(n // 26)
		i += 1
		
	#Step 2: Getting rid of 0, as 0 is
	# not part of number system
	for j in range(0, i - 1):
		if (arr[j] <= 0):
			arr[j] += 26
			arr[j + 1] = arr[j + 1] - 1

	for j in range(i, -1, -1):
		if (arr[j] > 0):
			print(chr(ord('A') +
				(arr[j] - 1)), end = "");

	print();

# Driver code
if __name__ == '__main__':
	
	printString(26);
	printString(51);
	printString(52);
	printString(80);
	printString(676);
	printString(702);
	printString(705);

# This code is contributed by Princi Singh
#Output
#Z
#AY
#AZ
#CB
#YZ
#ZZ
#AAC
#Time Complexity: O(log26n), as we are using a loop and in each traversal, we decrement by floor division of 26.

#Auxiliary Space: O(10000), as we are using extra space for the array.

#----------------------------------------------------------------------
#Method 3:

#We can use a recursive function which definitely reduces the time and  increase the efficiency:

#Alphabets are in sequential order like: ‘ABCDEFGHIJKLMNOPQRSTUVWXYZ’. You have experienced while using excel when you see columns and rows numbering are done in  Alphabetical ways.

#Here’s How I purposefully think about the logic of how it is arranged.

#(In Mathematical  terms, [a , b ] means from ‘a’ to ‘b’).

#[1,26] = [A,Z] (Understand by ‘1’ stands for ‘A’ and ’26” stands for “Z”). For [27,52] ,it will be like [AA,AZ], For [57,78] it will be [BA,BZ]

#Logic is to append an Alphabet sequentially whenever it ends up numbering at 26.

#For example, if the number is ’27’ which is greater than  ’26’, then we simply need to divide by 26, and we get the remainder as 1, We see “1” as “A” and can be recursively done.

#we will be using python for this.

#Algorithm is:

#1. Take an array and Sort the letters from A to Z . (You can also use the import string and string function to get “A to Z” in uppercase.)

#2. If the number is less than or equal to ’26’, simply get the letter from the array and print it.

#3. If it is greater than 26, use the Quotient  Remainder rule, if the remainder is zero, there are 2 possible ways, if the quotient is “1”, simply hash out the letter from the index [r-1]( ‘r’ is remainder), else call out the function from the num =(q-1) and append at the front to the letter indexing [r-1].

#4. If the remainder is not equal to “0”, call the function for the num = (q) and append at the front to the letter indexing [r-1].

#The code concerned with this is:
# Or you can simply take a string and perform this logic ,no issue i found in here.
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# defined a recursive function here.
# if number is less than "26", simply hash out (index-1)
# There are sub possibilities in possibilities,
# 1.if remainder is zero(if quotient is 1 or not 1) and
# 2. if remainder is not zero

def num_hash(num):
	if num < 26:
		return alpha[num-1]
	else:
		q, r = num//26, num % 26
		if r == 0:
			if q == 1:
				return alpha[r-1]
			else:
				return num_hash(q-1) + alpha[r-1]
		else:
			return num_hash(q) + alpha[r-1]


# Calling the function out here and printing the ALphabets
# This code is robust ,work for any positive integer only.
# You can try as much as you want
print(num_hash(26))
print(num_hash(51))
print(num_hash(52))
print(num_hash(80))
print(num_hash(676))
print(num_hash(702))
print(num_hash(705))
#Output
##Z
#AY
#AZ
#CB
#YZ
#ZZ
#AAC
#Time Complexity: O(log26n), as we are using recursion and in each recursive call, we decrement by floor division of 26.

#Auxiliary Space: O(1), as we are not using any extra space.