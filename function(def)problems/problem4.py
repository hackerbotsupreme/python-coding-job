#python program for functions that accept variable length key value pair as arguments.


#To pass a variable-length key-value pair as an argument to a function, Python provides a feature called **kwargs.
#kwargs stands for Keyword arguments. It proves to be an efficient solution when one wants to deal with named arguments in their function.

#Syntax:

def functionName(**anything):
    statement(s)
#Note: adding ‘**‘ to any term makes it a kwargs parameter. It accepts keywords as arguments. 

#Example #1: 
# using kwargs
# in functions


def printKwargs(**kwargs):
	print(kwargs)


# driver code
if __name__ == "__main__":
	printKwargs(Argument_1='gfg', Argument_2='GFG')


#Output:

#{'Argument_1': 'gfg', 'Argument_2': 'GFG'}
#Example #2:
# using kwargs
# in functions


def printValues(**kwargs):
	for key, value in kwargs.items():
		print("The value of {} is {}".format(key, value))


# driver code
if __name__ == '__main__':
	printValues(abbreviation="GFG", full_name="geeksforgeeks")


#Output:

#The value of abbreviation is GFG
#The value of full_name is geeksforgeeks
#Example #3:

# using kwargs
# in functions
# to concatenate


def concatenate(**arguments):
	# initialising empty string
	final_str = ""
	
	# Iterating over the Python kwargs
	# dictionary
	for elements in arguments.values():
		final_str += elements
	return final_str


# driver code
if __name__ == '__main__':
	print(concatenate(a="g", b="F", c="g"))


#Output:

#gFg
#Example #4:

# using kwargs
# to multiply


def multiply(**kwargs):

	# initialising answer
	answer = 1
	
	# Iterating over the Python kwargs
	# dictionary
	for elements in kwargs.values():
		answer *= elements
	return answer


# driver code
if __name__ == '__main__':
	print(multiply(a=1, b=2, c=3, d=4, e=5))




