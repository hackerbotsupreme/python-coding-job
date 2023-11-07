#python program to sort python dictionaries 
#Python | Sort Python Dictionaries by Key or Value

#Need for Sorting in Dictionary
#We need sorting of data to reduce the complexity of the data and make queries faster and more efficient. Therefore sorting is very important when we are dealing with a large amount of data. Here, we will use the following approach:

#First, sort the keys alphabetically using key_value.iterkeys() function.
#Second, sort the keys alphabetically using the sorted (key_value) function & print the value corresponding to it.
#Third, sort the values alphabetically using key_value.iteritems(), key = lambda (k, v) : (v, k))
#Here are the major tasks that are needed to be performed sort a dictionary by value and keys in Python.

#Create a dictionary and display its list-keys alphabetically.
#Display both the keys and values sorted in alphabetical order by the key.
#Same as part (ii), but sorted in alphabetical order by the value.
#Example 1: Sort Dictionary By Key in Python
#In this example, we will sort the dictionary by keys and the result type will be a dictionary. 





#Input:
#{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}

#Output: 
#{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}

myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)
#Output
#{'rajnish': 9, 'ravi': 10, 'sanjeev': 15, 'suraj': 32, 'yash': 2}
#Example 2: Displaying the Keys in sorted order
#In this example, we are trying to sort the dictionary by keys and values in Python. Here, iterkeys() returns an iterator over the dictionary’s keys.

#Input:
#key_value[2] = '56'       
#key_value[1] = '2'
#key_value[4] = '12'
#key_value[5] = '24'
#key_value[6] = '18'
#key_value[3] = '323'

#Output:
#1 2 3 4 5 6 

# Function calling
def dictionary():
    # Declare hash function
    key_value = {}
 
# Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
 
    print("Task 1:-\n")
 
    print("key_value", key_value)
 
    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted(key_value.keys()):
        print(i, end=" ")
 
 
def main():
    # function calling
    dictionairy()
 
 
# Main function calling
if __name__ == "__main__":
    main()
#Output
#Task 1:-

#key_value {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
#1 2 3 4 5 6 




#Example 3: Sort the dictionary by key 
#In this example, we will sort in lexicographical order Taking the key’s type as a string.

#Input:
#key_value['ravi'] = '10'       
#key_value['rajnish'] = '9'
#key_value['sanjeev'] = '15'
#key_value['yash'] = '2'
#key_value'suraj'] = '32'

#Output:
#[('rajnish', '9'), ('ravi', '10'), ('sanjeev', '15'), ('suraj', '32'), ('yash', '2')]




# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict

dict = {'ravi': '10', 'rajnish': '9',
		'sanjeev': '15', 'yash': '2', 'suraj': '32'}
dict1 = OrderedDict(sorted(dict.items()))
print(dict1)
#Output
#OrderedDict([('rajnish', '9'), ('ravi', '10'), ('sanjeev', '15'), ('suraj', '32'), ('yash', '2')])
#Example 4: Sorting the Keys and Values in Alphabetical Order using the Key
#In this example, we are trying to sort the dictionary by keys and values in Python. Here we are using an iterator over the Dictionary’s value to sort the keys.

#Input:
#key_value[2] = '56'       
#key_value[1] = '2'
#key_value[4] = '12'
#key_value[5] = '24'
#key_value[6] = '18'
#key_value[3] = '323'

#Output:
#(1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18) 



# function calling
def dictionairy():

	# Declaring the hash function
	key_value = {}

# Initialize value
	key_value[2] = 56
	key_value[1] = 2
	key_value[5] = 12
	key_value[4] = 24
	key_value[6] = 18
	key_value[3] = 323
	
	print("key_value",key_value)

	print("Task 2:-\nKeys and Values sorted in",
		"alphabetical order by the key ")
	

	# sorted(key_value) returns an iterator over the
	# Dictionary’s value sorted in keys.
	for i in sorted(key_value):
		print((i, key_value[i]), end=" ")


def main():
		# function calling
	dictionairy()


# main function calling
if __name__ == "__main__":
	main()



# function calling
def dictionairy():
 
    # Declaring the hash function
    key_value = {}
 
# Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
     
    print("key_value",key_value)
 
    print("Task 2:-\nKeys and Values sorted in",
          "alphabetical order by the key  ")
     
 
    # sorted(key_value) returns an iterator over the
    # Dictionary’s value sorted in keys.
    for i in sorted(key_value):
        print((i, key_value[i]), end=" ")
 
 
def main():
        # function calling
    dictionairy()
 
 
# main function calling
if __name__ == "__main__":
    main()
#Output
#key_value {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
#Task 2:-
#Keys and Values sorted in alphabetical order by the key  
#(1, 2) (2, 56) (3, 323) (4, 24) (5, 12) (6, 18) 
#Example 5: Sorting the Keys and Values alphabetically using the value
#In this example, we are trying to sort the dictionary by keys and values in Python. Here we are using to sort in lexicographical order.



Input:
key_value[2] = '56'       
key_value[1] = '2'
key_value[4] = '12'
key_value[5] = '24'
key_value[6] = '18'
key_value[3] = '323'

Output:
[(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]

# Function calling
def dictionairy():
 
    # Declaring hash function
    key_value = {}
 
# Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323
     
    print("key_value",key_value)
 
    print("Task 3:-\nKeys and Values sorted",
          "in alphabetical order by the value")
 
    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key=lambda kv:
                 (kv[1], kv[0])))
 
 
def main():
    # function calling
    dictionairy()
 
 
# main function calling
if __name__ == "__main__":
    main()
Output
#key_value {2: 56, 1: 2, 5: 12, 4: 24, 6: 18, 3: 323}
#Task 3:-
#Keys and Values sorted in alphabetical order by the value
#[(1, 2), (5, 12), (6, 18), (4, 24), (2, 56), (3, 323)]
#Example 6: Sort Dictionary By Value in Python
#In this example, we are trying to sort the dictionary by values in Python. Here we are using dictionary comprehension to sort our values.

#Input:
#key_value['ravi'] = 10       
#key_value['rajnish'] = 9
#key_value['sanjeev'] = 15
#key_value['yash'] = 2
#key_value['suraj'] = 32

#Output:
{'ravi': 2, 'rajnish': 9, 'sanjeev': 10, 'yash': 15, 'suraj': 32}
# Creates a sorted dictionary (sorted by key)
from collections import OrderedDict
import numpy as np
 
dict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
print(dict)
 
keys = list(dict.keys())
values = list(dict.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}
 
print(sorted_dict)
#Output:

#{'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
#{'ravi': 2, 'rajnish': 9, 'sanjeev': 10, 'yash': 15, 'suraj': 32}









