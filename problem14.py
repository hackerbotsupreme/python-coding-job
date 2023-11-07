#python  program to  convert key-value list dictionary to list of liats.

#Sometimes, while working with a Python dictionary, we can have a problem in which we need to perform the flattening of a key-value pair of dictionaries to a list and convert it to a list of lists. This can have applications in domains in which we have data. Let’s discuss certain ways in which this task can be performed.

#Method #1: Using loop + items() This brute force way in which we can perform this task. In this, we loop through all the pairs and extract list value elements using items() and render them in a new list. 


# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using loop + items()
res = []
for key, val in test_dict.items():
	res.append([key] + val)

# printing result
print("The converted list is : " + str(res))

#Output
#The original dictionary is : {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
#The converted list is : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]
#Method #2: Using list comprehension This task can also be performed using list comprehension. In this, we perform the task similar to the above method just in a one-liner shorter way. 

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
# Using list comprehension
res = [[key] + val for key, val in test_dict.items()]

# printing result
print("The converted list is : " + str(res))

#Output
#The original dictionary is : {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
#The converted list is : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]
#Method #3: Using map and dict.keys() This task can also be performed. In this, we get the keys value of dict and iterate over the list of keys and get the values of corresponding values and concatenate both key and value, and form a list of lists. 
# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List
# Using map + keys()

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

temp1 = list(test_dict.keys())
# Convert Key-Value list Dictionary to Lists of List
# Using map + keys()
res = list(map(lambda i: [i] + test_dict[i], temp1))

# printing result
print("The converted list is : " + str(res))
#Output
#The original dictionary is : {'is': [7, 6], 'gfg': [1, 3, 4], 'best': [4, 5]}
#The converted list is : [['is', 7, 6], ['gfg', 1, 3, 4], ['best', 4, 5]]
#Method #4 : Using keys() and insert() method

# Python3 code to demonstrate working of
# Convert Key-Value list Dictionary to Lists of List

# initializing Dictionary
test_dict = {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Convert Key-Value list Dictionary to Lists of List
res = []
for i in test_dict.keys():
	test_dict[i].insert(0, i)
	res.append(test_dict[i])
# printing result
print("The converted list is : " + str(res))


#Output
#The original dictionary is : {'gfg': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
#The converted list is : [['gfg', 1, 3, 4], ['is', 7, 6], ['best', 4, 5]]
























