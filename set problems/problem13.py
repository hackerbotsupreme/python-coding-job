# python program to check if a given string is a binary string.



#Approach 1: Using Set  
#Insert the given string in a set
#Check if the set characters consist of 1 and/or 0 only.



# Python program to check
# if a string is binary or not

# function for checking the
# string is accepted or not


def check(string):

	# set function convert string
	# into set of characters .
	p = set(string)

	# declare set of '0', '1' .
	s = {'0', '1'}

	# check set p is same as set s
	# or set p contains only '0'
	# or set p contains only '1'
	# or not, if any one condition
	# is true then string is accepted
	# otherwise not .
	if s == p or p == {'0'} or p == {'1'}:
		print("Yes")
	else:
		print("No")


# driver code
if __name__ == "__main__":

	string = "101010000111"

	# function calling
	check(string)


#Approach 2: Simple Iteration 
#Iterate for every character and check if the character is 0 or 1.
#If it is not then set a counter and break.
#After iteration check whether the counter is set or not.



# Python program to check
# if a string is binary or not

# function for checking the
# string is accepted or not


def check2(string):

	# initialize the variable t
	# with '01' string
	t = '01'

	# initialize the variable count
	# with 0 value
	count = 0

	# looping through each character
	# of the string .
	for char in string:

		# check the character is present in
		# string t or not.
		# if this condition is true
		# assign 1 to the count variable
		# and break out of the for loop
		# otherwise pass
		if char not in t:
			count = 1
			break
		else:
			pass

	# after coming out of the loop
	# check value of count is non-zero or not
	# if the value is non-zero the en condition is true
	# and string is not accepted
	# otherwise string is accepted
	if count:
		print("No")
	else:
		print("Yes")


# driver code
if __name__ == "__main__":

	string = "001021010001010"

	# function calling
	check2(string)





#Approach 3: Regular Expressions
#Compile a regular expression using compile() for “character is not 0 or 1”.
#se re.findall() to fetch the strings satisfying the above regular expression.
#Print output based on the result.


#import library
import re
 
sampleInput = "1001010"
 
# regular expression to find the strings
# which have characters other than 0 and 1
c = re.compile('[^01]')
 
# use findall() to get the list of strings
# that have characters other than 0 and 1.
if(len(c.findall(sampleInput))):
    print("No") # if length of list > 0 then it is not binary
else:
    print("Yes") # if length of list = 0 then it is binary
    
    
    
#Approach 4: Using exception handling and int

#Python has a built in method to convert a string of a 
# specific base to a decimal integer, using int(string,
# base). If the string passed as an argument is not of 
# the specified base, then a ValueError is raised.

# Python program to check
# if a string is binary or not
 
# function for checking the
# string is accepted or not
 
 
def check(string):
    try:
        # this will raise value error if
        # string is not of base 2
        int(string, 2)
    except ValueError:
        return "No"
    return "Yes"
 
 
# driver code
if __name__ == "__main__":
 
    string1 = "101011000111"
    string2 = "201000001"
 
    # function calling
    print(check(string1))
    print(check(string2))
 
 
# this code is contributed by phasing17




#Approach 5 : Using count() function
string = "01010101010"
if(string.count('0')+string.count('1')==len(string)):
    print("Yes")
else:
    print("No")
    
    
    
#Approach 6 : Using replace() and len() methods

#Python program to check string is binary or not
string = "01010121010"
binary="01"
for i in binary:
    string=string.replace(i,"")
if(len(string)==0):
    print("Yes")
else:
    print("No")
    
    
#Approach 7: Using all()
#The all() method in Python3 can be used to evaluate 
# if all the letters in the string are 0 or 1.


# Python program to check
# if a string is binary or not
 
# function for checking the
# string is accepted or not
 
 
def check(string):
    if all((letter in "01") for letter in string):
        return "Yes"
    return "No"
 
 
# driver code
if __name__ == "__main__":
 
    string1 = "101011000111"
    string2 = "201000001"
 
    # function calling
    print(check(string1))
    print(check(string2))
 
 
# this code is contributed by phasing17





