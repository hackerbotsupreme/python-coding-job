#concatenated string uncommon charecters in python 


#One of the string operation can be computing the uncommon characters of two strings i.e, output the uncommon
# values that appears in both the strings. This article deals with computing the same through different ways.
# Method 1 : Using set() + symmetric_difference() Set in python usually can perform the task of performing set
# operations such as set symmetric difference. This utility of sets can be used to perform this task as well. 
# Firstly, both the strings are converted into sets using set() and then symmetric difference is performed using
# symmetric_difference(). Returns the sorted set. 


# Python 3 code to demonstrate
# String uncommon characters
# using set() + symmetric_difference()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# Printing initial strings
print ("The original string 1 is : " + test_str1)
print ("The original string 2 is : " + test_str2)

# String uncommon characters
# using set() + symmetric_difference()
res = set(test_str1).symmetric_difference(test_str2)

# printing symmetric_difference
print ("The string uncommon elements are : " + str(res))

# Method 2 : Using join() join() performs the task similar to list comprehension in case of lists.
# This encapsulates whole symmetric_difference logic and joins together each element filtered through
# the symmetric_difference logic into one string, hence computing the symmetric_difference. It converts 
# the strings into set and then computed ^ operation on them. 



# Python 3 code to demonstrate
# String uncommon characters
# using join()

# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# Printing initial strings
print ("The original string 1 is : " + test_str1)
print ("The original string 2 is : " + test_str2)

# using join() to
# String uncommon characters
res = ''.join(sorted(set(test_str1) ^ set(test_str2)))

# printing symmetric_difference
print ("The string uncommon elements are : " + str(res))





#Method #3: Using Counter() function
# Python 3 code to demonstrate
# String uncommon characters
from collections import Counter
# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# Printing initial strings
print("The original string 1 is : " + test_str1)
print("The original string 2 is : " + test_str2)

frequency_str1 = Counter(test_str1)
frequency_str2 = Counter(test_str2)
result = []

for key in frequency_str1:
	if key not in frequency_str2:
		result.append(key)
		for key in frequency_str2:
			if key not in frequency_str1:
				result.append(key)

# Sorting the result
result.sort()
# printing symmetric_difference
print("The string uncommon elements are : " + str(result))








