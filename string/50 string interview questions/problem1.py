#reverse words in a given string

#Given a string, the task is to reverse the order of the words in the given string. 

#Examples:

#Input: s = “geeks quiz practice code” 
#Output: s = “code practice quiz geeks”

#Input: s = “i love programming very much” 
#Output: s = “much very programming love i” 


#Approach:

#Initially, reverse the individual words of the given string one by one, for the above example, after reversing individual words the string should be “i ekil siht margorp yrev hcum”.
#Reverse the whole string from start to end to get the desired output “much very program this like i” in the above example.
#Follow the below steps to solve the problem:



#Run a for loop to traverse the string and create a temporary string to store the words
#If the current character is a space then add the current string to the answer and empty the string
#Else push the character into the string
#Print the answer array in reverse order 
#Below is the implementation of the above approach: 

# Python3 program to reverse a string

# Function to reverse each word in the string


from ast import If


def reverse_word(s, start, end):
	while start < end:
		s[start], s[end] = s[end], s[start]
		start = start + 1
		end -= 1


s = "i like this program very much"

# Convert string to list to use it as a char array
s = list(s)
start = 0
while True:

	# We use a try catch block because for
	# the last word the list.index() function
	# returns a ValueError as it cannot find
	# a space in the list
	try:
		# Find the next space
		end = s.index(' ', start)

		# Call reverse_word function
		# to reverse each word
		reverse_word(s, start, end - 1)

		# Update start variable
		start = end + 1

	except ValueError:

		# Reverse the last word
		reverse_word(s, start, len(s) - 1)
		break

# Reverse the entire list
s.reverse()

# Convert the list back toj
#================================================================================================================================================
# string using string.join() function
s = "".join(s)

print(s)

# Solution contributed by Prem Nagdeo


#Output
#much very program this like i
#Time complexity: O(N)
#Auxiliary Space: O(N)

#Note: The above code doesn’t handle the cases when the string starts with space. 
#================================================================================================================================================
#Below is the implementation of the approach that handles this specific case and doesn’t make unnecessary calls to reverse function in the case of multiple spaces in between. Thanks to rka143 for providing this version. 
# Python3 program to reverse a string

# Reverse the letters
# of the word
def reverse(str, start, end):
	# Temporary variable
	# to store character
	temp = ''
	str1 = ""

	while (start <= end):
		# Swapping the first
		# and last character
		temp = str[start]
		str[start] = str[end]
		str[end] = temp
		start+=1
		end-=1
	return str1.join(str)

def reverseWords(s):
	
	word_begin = -1

	# temp is for word boundary
	i = 0

	# STEP 1 of the above algorithm
	while (i < len(s)):

		''' This condition is to make sure that the
				string start with valid character (not
				space) only '''
		if ((word_begin == -1) and (s[i] != ' ')):
			word_begin = i
		if (word_begin != -1 and ((i + 1 == len(s)) or (s[i + 1] == ' '))):
			s = reverse(list(s), word_begin, i)
			word_begin = -1
		i+=1
	''' End of while '''

	# STEP 2 of the above algorithm
	s = reverse(list(s), 0, (len(s) - 1))
	return s

# Driver Code
s = "i like this program very much"

# Function call
p = reverseWords(list(s))
print(p)

# This code is contributed by akashish__

#Output

#much very program this like i

# Python3 program to reverse a string
# s = input()
s = "i like this program very much"
words = s.split(' ')
string = []
for word in words:
	string.insert(0, word)


print(" ".join(string))

# Solution proposed bu Uttam


#Reverse words in a given string using the swap operation:
#The above task can also be accomplished by splitting the words separately and directly swapping the string starting from the middle.

#Follow the below steps to solve the problem:

#Store the string in the form of words
#Swap the words with each other starting from the middle
#Print the string



# Python3 code to reverse a string

# Reverse the string


def RevString(s, l):

	# Check if number of words is even
	if l % 2 == 0:

		# Find the middle word
		j = int(l/2)

		# Starting from the middle
		# start swapping words
		# at jth position and l-1-j position
		while(j <= l - 1):
			s[j], s[l - j - 1] = s[l - j - 1], s[j]
			j += 1

	# Check if number of words is odd
	else:

		# Find the middle word
		j = int(l/2 + 1)

		# Starting from the middle
		# start swapping the words
		# at jth position and l-1-j position
		while(j <= l - 1):
			s[j], s[l - 1 - j] = s[l - j - 1], s[j]
			j += 1

		# return the reversed sentence
		return s


# Driver Code
s = 'i like this program very much '
string = s.split(' ')
string = RevString(string, len(string))
print(" ".join(string))



#Output
#much very program this like If





#Reverse words in a given string using constant space:
##Follow the below steps to solve the problem:

#Go through the string and mirror each word in the string, 
#Then, in the end, mirror the whole string.
#Below is the implementation of the above approach:


# Python code for the above apporach
 
def reverse_words(s):
    left = 0
    i = 0
    s = list(s)
    n = len(s)
     
    while(s[i] == ' '):
        i = i+1
         
    left = i
     
    while(i < n):
        if(i+1 == n or s[i] == ' '):
            j = i-1
            if i+1 == n:
                j = j+1
             
            while left < j:
                s[left], s[j] = s[j], s[left]
                left = left+1
                j = j-1
             
            left = i + 1
         
        if(i > left and s[left] == ' '):
            left = i
         
        i = i+1
    s = ''.join(s)
    s = s[::-1]
    return s
 
s1 = "i like this program very much"
s1 = reverse_words(s1)
print(s1)
     
# This Code is contributed by Yash Agarwal(yashagarwal2852002)
#Output
#much very program this like i


#Reverse words in a given string using constant space: using the slicing method and join functions:
#Below is the implementation of the above approach:


# python code to reverse words in a given str
# python code to reverse words in a given string

# input string
string = "i like this program very much"

# spliting words in the given string
# using slicing reverse the words
s = string.split()[::-1]

# joining the reversed string and
# printing the output
print(" ".join(s))


























