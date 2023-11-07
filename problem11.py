#python program to find all duplicate charecters  in the string.


#Given a string, find all the duplicate characters which are similar to each other. Let us look at the example. 

#Examples:

#Input : hello
#Output : l

#Input : geeksforgeeeks
#Output : e g k s


#We have discussed a solution in the below post. Print all the duplicates in the input string We can solve this problem quickly using the python Counter() method. 

#The approach is very simple. 

#Create a dictionary using the Counter method having strings as keys and their frequencies as values.
#Declare a temp variable.
#Print all the indexes from the keys which have values greater than 1. 

from collections import Counter


def find_dup_char(input):

	# now create dictionary using counter method
	# which will have strings as key and their
	# frequencies as value
	WC = Counter(input)

	# Finding no. of occurrence of a character
	# and get the index of it.
	for letter, count in WC.items():
		if (count > 1):
			print(letter)


# Driver program
if __name__ == "__main__":
	input = 'geeksforgeeks'
	find_dup_char(input)


#Approach : Using count() method


def find_dup_char(input):
    x=[]
    for i in input:
        if i not in x and input.count(i)>1:
            x.append(i)
    print(" ".join(x))
 
# Driver program
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)

#Approach : Using filter() method


def find_dup_char(input):
    x = filter(lambda x: input.count(x) >= 2, input)
    print(' '.join(set(x)))
 
 
# Driver Code
if __name__ == "__main__":
    input = 'geeksforgeeks'
    find_dup_char(input)
    
    
    
#Output
#k e s g







