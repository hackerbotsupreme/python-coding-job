#find the number occuring odd number of times using lambda expresssion and reduce function.


#Given an array of positive integers. All numbers occur even number of times except one number which occurs odd number of times. Find the number in O(n) time & constant space.

#Examples:

#Input :  [1, 2, 3, 2, 3, 1, 3]
#Output :  3

# Python program to Find the Number
# Occurring Odd Number of Times
# using Lambda expression and reduce function

from functools import reduce

def oddTimes(input):
	# write lambda expression and apply
	# reduce function over input list
	# until single value is left
	# expression reduces value of a ^ b into single value
	# a starts from 0 and b from 1
	# ((((((1 ^ 2)^3)^2)^3)^1)^3)
	print (reduce(lambda a, b: a ^ b, input))

# Driver program
if __name__ == "__main__":
	input = [1, 2, 3, 2, 3, 1, 3]
	oddTimes(input)


