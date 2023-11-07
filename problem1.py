#given an integer N, the task pattern is to print half-diamond-star pattern.

#Given an integer N, the task is to print half-diamond-star pattern.

#  *
#  **
#  ***
#  ****
#  *****
#  ******
#  *****
#  ****
#  ***
#  **
#  *


#Examples:

#Input: N = 3
#Output:
# *
# **
# ***
# **
# *

#Input: N = 6
# Output:
#  *
#  **
#  ***
#  ****
#  *****
#  ******
#  *****
 # ****
#  ***
#  **
#  *


#Approach: The idea is to break the pattern into two halves that is upper half and lower half. Then print them separately with the help of the loops. The key observation for printing the upper half and lower half is described as below:



#Upper half: The upper half of the pattern contains star ‘*’ in increasing order where ith line contains following number of star:
#Number of '*' in ith line = i
#Lower Half: The lower half of the pattern contains star ‘*’ in decreasing order where ith line contains following number of star:
#Number of '*' in ith line = N - i


# Python3 implementation to print the
# half diamond star pattern

# Function to print the
# half diamond star pattern
def halfDiamondStar(N):
	
	# Loop to print the upper half
	# diamond pattern
	for i in range(N):

		for j in range(0, i + 1):
			print("*", end = "")
		print()

	# Loop to print the lower half
	# diamond pattern
	for i in range(1, N):

		for j in range(i, N):
			print("*", end = "")
		print()

# Driver Code
N = 5;

# Function Call
halfDiamondStar(N);

# This code is contributed by skylags


# Python3 implementation to print the
# half diamond star pattern
 
# Function to print the
# half diamond star pattern
def halfDiamondStar(N):
     
    # Loop to print the upper half
    # diamond pattern
    for i in range(N):
 
        for j in range(0, i + 1):
            print("*", end = "")
        print()
 
    # Loop to print the lower half
    # diamond pattern
    for i in range(1, N):
 
        for j in range(i, N):
            print("*", end = "")
        print()
 
# Driver Code
N = 5;
 
# Function Call
halfDiamondStar(N);
 
# This code is contributed by skylags
#Output
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *





















