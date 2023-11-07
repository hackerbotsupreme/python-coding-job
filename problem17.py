#python program to convert string to dictionary 

#Interconversions of data types have been discussed many times and have been quite a popular problem to solve. This article discusses yet another problem of interconversion of the dictionary, in string format to a dictionary. Let’s discuss certain ways in which this can be done.

#Method #1 : Using json.loads() 

#This task can easily be performed using the inbuilt function of loads of json library of python which converts the string of valid dictionary into json form, dictionary in Python. 

# Python3 code to demonstrate
# convert dictionary string to dictionary
# using json.loads()
import json

# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

# printing original string
print("The original string : " + str(test_string))

# using json.loads()
# convert dictionary string to dictionary
res = json.loads(test_string)

# print result
print("The converted dictionary : " + str(res))
#Output : 

#The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
#The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}



#Method #2: Using ast.literal_eval() 

#The above method can also be used to perform a similar conversion. Function safer than the eval function and can be used for interconversion of all data types other than dictionary as well. 
# Python3 code to demonstrate
# convert dictionary string to dictionary
# using ast.literal_eval()
import ast

# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

# printing original string
print("The original string : " + str(test_string))

# using ast.literal_eval()
# convert dictionary string to dictionary
res = ast.literal_eval(test_string)

# print result
print("The converted dictionary : " + str(res))
#Output : 
#The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
#The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}
#Method #3: Using eval() The above method can also be used to perform a similar conversion. The eval() function parse the argument passed and converts it to a python  expression and runs the python expression.

# Python3 code to demonstrate
# convert dictionary string to dictionary
# using eval()

# initializing string
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'

# printing original string
print("The original string : " + str(test_string))

# using eval()
# convert dictionary string to dictionary
res = eval(test_string)

# print result
print("The converted dictionary : " + str(res))
#Output:

#The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
#The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}
#Method #4: Using the split() method and a dictionary comprehension:

#First, we remove the curly braces from the string using the strip() method. Then, we split the string into a list of key-value pairs using the split() method. Finally, we use a dictionary comprehension to iterate over the pairs, split them into separate key and value strings, and convert the values to integers before adding them to the dictionary. The resulting dictionary is returned.


def str_to_dict(string):
     # remove the curly braces from the string
    string = string.strip('{}')
 
    # split the string into key-value pairs
    pairs = string.split(', ')
 
    # use a dictionary comprehension to create the dictionary, converting the values to integers and removing the quotes from the keys
    return {key[1:-2]: int(value) for key, value in (pair.split(': ') for pair in pairs)}
 
 
# test the function
test_string = '{"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}'
print("The original string : " + str(test_string))
print("The converted dictionary : " + str(
    str_to_dict(test_string)))  # The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
# The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}
#This code is contributed by Edula Vinay Kumar Reddy

#Output
#The original string : {"Nikhil" : 1, "Akshat" : 2, "Akash" : 3}
#The converted dictionary : {'Nikhil': 1, 'Akshat': 2, 'Akash': 3}