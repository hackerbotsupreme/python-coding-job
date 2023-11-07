#Given a sorted array and a number x, find the pair in array whose sum is closest to x

#Difficulty Level : Easy
#-----------------------------------------------------------------------
#Given a sorted array and a number x, find a pair in an array whose sum is closest to x.

#Examples:

#Input: arr[] = {10, 22, 28, 29, 30, 40}, x = 54
#Output: 22 and 30

#Input: arr[] = {1, 3, 4, 7, 10}, x = 15
#Output: 4 and 10
#A simple solution is to consider every pair and keep track of the closest pair (the absolute difference between pair sum and x is minimum). Finally, print the closest pair. The time complexity of this solution is O(n2)

#An efficient solution can find the pair in O(n) time. The idea is similar to method 1 of this post. The following is a detailed algorithm. 

#1) Initialize a variable diff as infinite (Diff is used to store the 
#   difference between pair and x).  We need to find the minimum diff.
#2) Initialize two index variables l and r in the given sorted array.
#       (a) Initialize first to the leftmost index:  l = 0
#       (b) Initialize second  the rightmost index:  r = n-1
#3) Loop while l < r.
#       (a) If  abs(arr[l] + arr[r] - sum) < diff  then 
#           update diff and result 
#       (b) If(arr[l] + arr[r] <  sum )  then l++
#       (c) Else r--    



# Python3 program to find the pair
# with sum
# closest to a given no.

# A sufficiently large value greater
# than any
# element in the input array
MAX_VAL = 1000000000


#Prints the pair with sum closest to x

def printClosest(arr, n, x):
	
	# To store indexes of result pair
	res_l, res_r = 0, 0
	
	#Initialize left and right indexes
	# and difference between
	# pair sum and x
	l, r, diff = 0, n-1, MAX_VAL
	
	# While there are elements between l and r
	while r > l:
		# Check if this pair is closer than the
		# closest pair so far
		if abs(arr[l] + arr[r] - x) < diff:
			res_l = l
			res_r = r
			diff = abs(arr[l] + arr[r] - x)
	
		if arr[l] + arr[r] > x:
		# If this pair has more sum, move to
		# smaller values.
			r -= 1
		else:
		# Move to larger values
			l += 1
		
	print('The closest pair is {} and {}'
		.format(arr[res_l], arr[res_r]))


# Driver code to test above
if __name__ == "__main__":
	arr = [10, 22, 28, 29, 30, 40]
	n = len(arr)
	x=54
	printClosest(arr, n, x)

# This code is contributed by Tuhin Patra
#-----------------------------------------------------------------------------------

