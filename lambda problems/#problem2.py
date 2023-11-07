#python ,sorting string using order defined by another defined by another string
#Given two strings (of lowercase letters), a pattern and a string. The task is to sort string according to the order defined by pattern and return the reverse of it. It may be assumed that pattern has all characters of the string and all characters in pattern appear only once. Examples:

#Input : pat = "asbcklfdmegnot", str = "eksge" 
#Output : str = "geeks"
#(after sorting, str becomes "skeeg" and return its reverse)

#Input : pat = "mgewqnasibkldjxruohypzcftv", str = "niocgd"
#Output : str = "coding"


#The idea is to first maintain a dictionary according to the index provided in Pattern and then passing the lambda function(which uses utility of dictionary) into the sort function. Below is the implementation of above idea. 

# Python program to sort a string and return
# its reverse string according to pattern string

# This function will return the reverse of sorted string
# according to the pattern

def sortbyPattern(pat, str):

	priority = list(pat)

	# Create a dictionary to store priority of each character
	myDict = { priority[i] : i for i in range(len(priority))}

	str = list(str)

	# Pass lambda function as key in sort function
	str.sort( key = lambda ele : myDict[ele])

	# Reverse the string using reverse()
	str.reverse()

	new_str = ''.join(str)
	return new_str


if __name__=='__main__':
	pat = "asbcklfdmegnot"
	str = "eksge"
	new_str = sortbyPattern(pat, str)
	print(new_str)

#Output:

#geeks



