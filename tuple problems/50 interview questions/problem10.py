#Python | Convert a list of Tuples into Dictionary

#Difficulty Level : Basic
#Sometimes you might need to convert a tuple to dict object to make it more readable. In this article, we will try to learn how to convert a list of tuples into a dictionary. Here we will find two methods of doing this. Examples:

#Input : [("akash", 10), ("gaurav", 12), ("anand", 14), 
#         ("suraj", 20), ("akhil", 25), ("ashish", 30)]
#Output : {'akash': [10], 'gaurav': [12], 'anand': [14], 
#          'ashish': [30], 'akhil': [25], 'suraj': [20]}

#Input : [('A', 1), ('B', 2), ('C', 3)]
#Output : {'B': [2], 'A': [1], 'C': [3]}

#Input : [("Nakul",93), ("Shivansh",45), ("Samved",65),
#             ("Yash",88), ("Vidit",70), ("Pradeep",52)]
#Output : {'Nakul': [93], 'Shivansh': [45], 'Samved': [65], 
#            'Yash': [88], 'Vidit': [70], 'Pradeep': [52]}

#Input : [('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]
#Output : {'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
#Recommended: Please try your approach on {IDE} first, before moving on to the solution.
#Method 1 : Use of setdefault()

#Here we have used the dictionary method setdefault() to convert the first parameter to key and the second to the value of the dictionary. setdefault(key, def_value) function searches for a key and displays its value and creates a new key with def_value if the key is not present. Using the append function we just added the values to the dictionary. Example 1: 

#Python3
# Python code to convert into dictionary
 
def Convert(tup, di):
    for a, b in tup:
        di.setdefault(a, []).append(b)
    return di
     
# Driver Code   
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
     ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))
#Output:

#{'akash': [10], 'gaurav': [12], 'anand': [14], 
# 'ashish': [30], 'akhil': [25], 'suraj': [20]}
#Example 2: 

#Python3
# Python code to convert into dictionary
list_1=[("Nakul",93), ("Shivansh",45), ("Samved",65),
           ("Yash",88), ("Vidit",70), ("Pradeep",52)]
dict_1=dict()
 
for student,score in list_1:
    dict_1.setdefault(student, []).append(score)
print(dict_1)
#Output:

#{'Nakul': [93], 'Shivansh': [45], 'Samved': [65], 'Yash': [88], 'Vidit': [70], 'Pradeep': [52]}
#Method 2 : Use of dict() method

#Example 1: 

#Python3
# Python code to convert into dictionary
def Convert(tup, di):
    di = dict(tup)
    return di
     
# Driver Code
tups = [("akash", 10), ("gaurav", 12), ("anand", 14),
    ("suraj", 20), ("akhil", 25), ("ashish", 30)]
dictionary = {}
print (Convert(tups, dictionary))
Output:

{'anand': 14, 'akash': 10, 'akhil': 25, 
 'suraj': 20, 'ashish': 30, 'gaurav': 12}
#Example 2: 

#Python3
# Python code to convert into dictionary
 
#print (dict([('Sachin', 10), ('MSD', 7), ('Kohli', 18), ('Rohit', 45)]))
#Output:

{'Sachin': 10, 'MSD': 7, 'Kohli': 18, 'Rohit': 45}
#This is a simple method of conversion from a list or tuple to a dictionary. Here we pass a tuple into the dict() method which converts the tuple into the corresponding dictionary.

#Method 3:

#You can use the itertools.groupby function from the itertools module to convert a list of tuples into a dictionary, where the keys are the unique values in the list and the values are lists of tuples that have the same value.

#Here is an example of how to use itertools.groupby to achieve this:

#Python3
from itertools import groupby
 
def convert_to_dict(tuple_list):
    # Group the tuples by their first element (the key)
    groups = groupby(tuple_list, key=lambda x: x[0])
     
    # Create an empty dictionary
    dictionary = {}
     
    # Iterate over the groups
    for key, group in groups:
        # Extract the second element of each tuple in the group and add it to the dictionary as the value for the key
        dictionary[key] = [tuple[1] for tuple in group]
     
    return dictionary
 
# Test the function
tuple_list = [("akash", 10), ("gaurav", 12), ("anand", 14), ("suraj", 20), ("akhil", 25), ("ashish", 30)]
print(convert_to_dict(tuple_list)) # {'akash':
Output
{'akash': [10], 'gaurav': [12], 'anand': [14], 'suraj': [20], 'akhil': [25], 'ashish': [30]}

