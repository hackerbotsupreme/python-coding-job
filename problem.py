#ways to sort list of dictionaries by values in python
#In this article, we will cover how to sort a dictionary by value in Python. 

#Sorting has always been a useful utility in day-to-day programming. Dictionary in Python is widely used in many applications ranging from competitive domain to developer domain(e.g. handling JSON data). Having the knowledge to sort dictionaries according to their values can prove useful in such cases.

#There are 2 ways to achieve this sorting:
#ways to sort list dictionary by value--
#1. using lambda function 
#2.using itemgetter

#What is the lambda function in python?
#This article deals with sorting using the lambda function and using the “sorted()” inbuilt function. Various variations can also be achieved for sorting the dictionaries. 
#For descending order : Use “reverse = True” in addition to the sorted() function.
#For sorting w.r.t multiple values: Separate by “comma” mentioning the correct order in which sorting has to be performed.
#Example:

# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
list = [{"name": "Nandini", "age": 20},
	{"name": "Manjeet", "age": 20},
	{"name": "Nikhil", "age": 19}]

# using sorted and lambda to print list sorted
# by age
print("The list printed sorting by age: ")
print(sorted(list, key=lambda i: i['age']))

print("\r")

# using sorted and lambda to print list sorted
# by both age and name. Notice that "Manjeet"
# now comes before "Nandini"
print("The list printed sorting by age and name: ")
print(sorted(list, key=lambda i: (i['age'], i['name'])))

print("\r")

# using sorted and lambda to print list sorted
# by age in descending order
print("The list printed sorting by age in descending order: ")
print(sorted(list, key=lambda i: i['age'], reverse=True))


#Output:

#The list printed sorting by age: 
#[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}]

#The list printed sorting by age and name: 
#[{'age': 19, 'name': 'Nikhil'}, {'age': 20, 'name': 'Manjeet'}, {'age': 20, 'name': 'Nandini'}]

#The list printed sorting by age in descending order: 
#[{'age': 20, 'name': 'Nandini'}, {'age': 20, 'name': 'Manjeet'}, {'age': 19, 'name': 'Nikhil'}]

























