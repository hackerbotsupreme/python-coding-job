#Program to accept the strings which contains all vowels



#Approach : Firstly, create set of vowels using set() function. Check for each character of the string is vowel
# or not, if vowel then add into the set s. After coming out of the loop, check length of the set s, if length 
# of set s is equal to the length of the vowels set then string is accepted otherwise not. 
#Below is the implementation : 
# Python program to accept the strings
# which contains all the vowels

# Function for check if string
# is accepted or not
def check(string) :

	string = string.lower()

	# set() function convert "aeiou"
	# string into set of characters
	# i.e.vowels = {'a', 'e', 'i', 'o', 'u'}
	vowels = set("aeiou")

	# set() function convert empty
	# dictionary into empty set
	s = set({})

	# looping through each
	# character of the string
	for char in string :

		# Check for the character is present inside
		# the vowels set or not. If present, then
		# add into the set s by using add method
		if char in vowels :
			s.add(char)
		else:
			pass
			
	# check the length of set s equal to length
	# of vowels set or not. If equal, string is
	# accepted otherwise not
	if len(s) == len(vowels) :
		print("Accepted")
	else :
		print("Not Accepted")


# Driver code
if __name__ == "__main__" :
	
	string = "SEEquoiaL"

	# calling function
	check(string)







def check(string):
	string = string.replace(' ', '')
	string = string.lower()
	vowel = [string.count('a'), string.count('e'), string.count(
		'i'), string.count('o'), string.count('u')]

	# If 0 is present int vowel count array
	if vowel.count(0) > 0:
		return('not accepted')
	else:
		return('accepted')


# Driver code
if __name__ == "__main__":

	string = "SEEquoiaL"

	print(check(string))





# Python program for the above approach
def check(string):
	if len(set(string.lower()).intersection("aeiou")) >= 5:
		return ('accepted')
	else:
		return ("not accepted")


# Driver code
if __name__ == "__main__":
	string = "geeksforgeeks"
	print(check(string))
 
 
 
 
 
 
 
#Alternate Implementation 3.0 (Using Regular Expressions):

#Compile a regular expression using compile() for “character is not a, e, i, o and u”.
#Use re.findall() to fetch the strings satisfying the above regular expression.
#Print output based on the result.
#import library
import re

sampleInput = "aeioAEiuioea"

# regular expression to find the strings
# which have characters other than a,e,i,o and u
c = re.compile('[^aeiouAEIOU]')

# use findall() to get the list of strings
# that have characters other than a,e,i,o and u.
if(len(c.findall(sampleInput))):
	print("Not Accepted") # if length of list > 0 then it is not accepted
else:
	print("Accepted") # if length of list = 0 then it is accepted






# Python | Program to accept the strings which contains all vowels


def all_vowels(str_value):

	new_list = [char for char in str_value.lower() if char in 'aeiou']

	if new_list:

		dic, lst = {}, []

		for char in new_list:
			dic['a'] = new_list.count('a')
			dic['e'] = new_list.count('e')
			dic['i'] = new_list.count('i')
			dic['o'] = new_list.count('o')
			dic['u'] = new_list.count('u')

		for i, j in dic.items():
			if j == 0:
				lst.append(i)

		if lst:
			return f"All vowels except {','.join(lst)} are not present"
		else:
			return 'All vowels are present'

	else:
		return "No vowels present"


# function-call
str_value = "geeksforgeeks"
print(all_vowels(str_value))

str_value = "ABeeIghiObhkUul"
print(all_vowels(str_value))

# contribute by saikot





#Alternate Approach (using set methods)

#The issubset() attribute of a set in Python3 checks if all the elements of a given set are present in another set.




# Python program to accept the strings
# which contains all the vowels

# Function for check if string
# is accepted or not
def check(string) :
	
	# Checking if "aeiou" is a subset of the set of all letters in the string
	if set("aeiou").issubset(set(string.lower())):
	 return "Accepted"
	return "Not accepted"


# Driver code
if __name__ == "__main__" :
	
	string = "SEEquoiaL"

	# calling function
	print(check(string))





#Using collections: One approach using the collections module could be to use a Counter object to count the occurrences of each character in the string. Then, we can check if the count for each vowel is greater than 0. If it is, we can add 1 to a counter variable. At the end, we can check if the counter variable is equal to the number of vowels. If it is, the string is accepted, otherwise it is not accepted.

#Here is an example of this approach:


import collections

def check(string):
	# create a Counter object to count the occurrences of each character
	counter = collections.Counter(string.lower())
	
	# set of vowels
	vowels = set("aeiou")
	
	# counter for the number of vowels present
	vowel_count = 0
	
	# check if each vowel is present in the string
	for vowel in vowels:
		if counter[vowel] > 0:
			vowel_count += 1
	
	# check if all vowels are present
	if vowel_count == len(vowels):
		print("Accepted")
	else:
		print("Not Accepted")

# test the function
string = "SEEquoiaL"
check(string)


#Alternate Approach (using  all () method) 
# Python program to accept the strings
# which contains all the vowels

# Function for check if string
# is accepted or not

#using all() method

def check(string):
	vowels = "aeiou" #storing vowels
	if all(vowel in string.lower() for vowel in vowels):
		return "Accepted"
	return "Not accepted"



#intitalizing string
string = "SEEquoiaL"
# test the function
print(check(string))

#this code contributed by tvsk
