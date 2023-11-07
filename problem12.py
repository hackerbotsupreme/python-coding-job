#python program to remove key from a dictionary.
#Dictionary is used in manifold practical applications such as day-day programming, web development, and AI/ML programming as well, making it a useful container overall. Hence, knowing shorthands for achieving different tasks related to dictionary usage always is a plus. This article deals with one such task of deleting/removing a dictionary key-value pair from a dictionary, we will discuss different methods to deal given task, and in Last we will see how can we delete all keys from Dictionary.

#Example:

#Before remove key:   {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}

#Operation Perform:   del test_dict['Mani']

#After removing key:  {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}
#Method 1: Remove a Key from a Dictionary using the del
#The del keyword can be used to in-place delete the key that is present in the dictionary in Python. One drawback that can be thought of using this is that it raises an exception if the key is not found and hence non-existence of the key has to be handled. Demonstrating key-value pair deletion using del.


# Initializing dictionary
test_dict = {"Arushi": 22, "Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : ", test_dict)

# Using del to remove a dict
# removes Mani
del test_dict['Mani']

# Printing dictionary after removal
print("The dictionary after remove is : ", test_dict)

# Using del to remove a dict
# raises exception
del test_dict['Mani']


#Output :

#The dictionary before performing remove is :  {'Arushi': 22, 'Mani': 21, 'Haritha': 21}
#The dictionary after remove is :  {'Arushi': 22, 'Haritha': 21}
#Exception : 

#Traceback (most recent call last):
#  File "/home/44db951e7011423359af4861d475458a.py", line 20, in 
#    del test_dict['Mani']
#KeyError: 'Mani'


#Method 2: Remove a Key from a Dictionary using pop() 
#The pop() can be used to delete a key and its value inplace. The advantage over using del is that it provides the mechanism to print desired value if tried to remove a non-existing dict. pair. Second, it also returns the value of the key that is being removed in addition to performing a simple delete operation. Demonstrating key-value pair deletion using pop() 

# Initializing dictionary
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : " + str(test_dict))

# Using pop() to remove a dict. pair
# removes Mani
removed_value = test_dict.pop('Mani')

# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))

print('\r')

# Using pop() to remove a dict. pair
# doesn't raise exception
# assigns 'No Key found' to removed_value
removed_value = test_dict.pop('Manjeet', 'No Key found')

# Printing dictionary after removal
print("The dictionary after remove is : " + str(test_dict))
print("The removed key's value is : " + str(removed_value))


#Output:

#The dictionary before performing remove is : {'Arushi': 22, 'Anuradha': 21,
# 'Mani': 21, 'Haritha': 21}
#The dictionary after remove is : {'Arushi': 22, 'Anuradha': 21, 'Haritha': 21}
#The removed key's value is : 21

#The dictionary after remove is : {'Arushi': 22, 'Anuradha': 21, 'Haritha': 21}
#The removed key's value is : No Key found
#Method 3: Using items() + dict comprehension to Remove a Key from a Dictionary
#items() coupled with dict comprehension can also help us achieve the task of key-value pair deletion but, it has the drawback of not being an in-place dict. technique. Actually, a new dict is created except for the key we don’t wish to include. Demonstrating key-value pair deletion using items() + dict comprehension.
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21,
			"Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing\
remove is : " + str(test_dict))

# Using items() + dict comprehension to remove a dict. pair
# removes Mani
new_dict = {key: val for key,
			val in test_dict.items() if key != 'Mani'}

# Printing dictionary after removal
print("The dictionary after remove is : " + str(new_dict))

#Output:

#The dictionary before performing remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22, 'Mani': 21}
#The dictionary after remove is : {'Anuradha': 21, 'Haritha': 21, 'Arushi': 22}
#Method 4: Use a Python Dictionary Comprehension to Remove a Key from a Dictionary
#In this example, we will use Dictionary Comprehension to remove a key from a dictionary.

# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}

# Printing dictionary before removal
print("The dictionary before performing remove is : \n" + str(test_dict))

a_dict = {key: test_dict[key] for key in test_dict if key != 'Mani'}

print("The dictionary after performing remove is : \n", a_dict)
#Output:

#The dictionary before performing remove is : 
#{'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
#The dictionary after performing remove is : 
# {'Arushi': 22, 'Anuradha': 21, 'Haritha': 21}
#Method 5: Iterating and Eliminating
#In this example, we will use a loop to remove a key from a dictionary.

# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)

# empty the dictionary d
y = {}
# eliminate the unrequired element
for key, value in test_dict.items():
	if key != 'Arushi':
		y[key] = value
print(y)



# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)
 
# empty the dictionary d
y = {}
# eliminate the unrequired element
for key, value in test_dict.items():
    if key != 'Arushi':
        y[key] = value
#print(y)
#Output:

#{'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
#{'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
#How to Delete all Keys from a Dictionary?
#Method 1: Delete all Keys from a Dictionary using the del
#The del keyword can also be used to delete a list, slice a list, delete dictionaries, remove key-value pairs from a dictionary, delete variables, etc.

# Initializing dictionary
# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)

# empty the dictionary d
del test_dict
try:
	print(test_dict)
except:
	print('Deleted!')



#Output:

#{'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
#Deleted!
#Method 2: Delete all Keys from a Dictionary using dict.clear()
#The clear() method removes all items from the dictionary. The clear() method doesn’t return any value.


# Initializing dictionary
test_dict = {"Arushi": 22, "Anuradha": 21, "Mani": 21, "Haritha": 21}
print(test_dict)

# empty the dictionary d
test_dict.clear()
print("Length", len(test_dict))
print(test_dict)


#Output:

#{'Arushi': 22, 'Anuradha': 21, 'Mani': 21, 'Haritha': 21}
#Length 0
#{}













