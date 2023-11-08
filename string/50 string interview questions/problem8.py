#Find an equal point in a string of brackets

#Given a string of brackets, the task is to find an index k which decides the number of opening brackets is equal to the number of closing brackets. 
#The string must be consists of only opening and closing brackets i.e. ‘(‘ and ‘)’.

#An equal point is an index such that the number of opening brackets before it is equal to the number of closing brackets from and after.

#Examples:  

#Input: str = “(())))(“
#Output:   4
#Explanation: After index 4, string splits into (()) and ))(. The number of opening brackets in the first part is equal to the number of closing brackets in the second part.
#Input: str = “))”
#Output: 2
#Explanation: As after 2nd position i.e. )) and “empty” string will be split into these two parts. So, in this number of opening brackets i.e. 0 in the first part is equal to the number of closing brackets in the second part i.e. also 0.



#Approach 1:

#Store the number of opening brackets that appear in the string up to every index, it must start from starting index.
#Similarly, Store the number of closing brackets that appear in the string up to each and every index but it should be done from the last index.
#Check if any index has the same value as opening and closing brackets.
#Below is the implementation of the above approach:

# Method to find an equal index
def findIndex(str):
	l = len(str)
	open = [0] * (l + 1)
	close = [0] * (l + 1)
	index = -1
	
	open[0] = 0
	close[l] = 0
	if (str[0]=='('):
		open[1] = 1
	if (str[l - 1] == ')'):
		close[l - 1] = 1
	
	# Store the number of
	# opening brackets
	# at each index
	for i in range(1, l):
		if (str[i] == '('):
			open[i + 1] = open[i] + 1
		else:
			open[i + 1] = open[i]
	
	# Store the number
	# of closing brackets
	# at each index
	for i in range(l - 2, -1, -1):
		if ( str[i] == ')'):
			close[i] = close[i + 1] + 1
		else:
			close[i] = close[i + 1]
	
	# check if there is no
	# opening or closing brackets
	if (open[l] == 0):
		return len
	if (close[0] == 0):
		return 0
	
	# check if there is any
	# index at which both
	# brackets are equal
	for i in range(l + 1):
		if (open[i] == close[i]):
			index = i
	
	return index
	
# Driver Code
str = "(()))(()()())))"
print(findIndex(str))

# This code is contributed
# by ChitraNayal
------------------------------------------------------
#Approach 2: 

#Count the total number of closed brackets in the string and store in a variable, let’s say cnt_close.
#So count of open brackets is length of (string – count) of closed brackets.
#Traverse string again but now keep count of open brackets in string, let’s say cnt_open.
#Now while traversing, let index be i, so count of closed brackets till that index will be (i+1 – cnt_open).
#Hence, we can check for what index, the count of open brackets in first part equals that of count of closed brackets in second part.
#Equation becomes cnt_close – (i+1 – cnt_open) = cnt_open, we have to find i.
#After evaluating above equation we can see cnt_open gets cancelled on both sides so no need.
#Implementation:

# Method to find an equal index
def findIndex(str):
	cnt_close = 0
	l = len(str)
	for i in range(0, l):
		if(str[i] == ')'):
			cnt_close = cnt_close + 1

	for i in range(0, l):
		if(cnt_close == i):
			return i
	# If no opening brackets
	return l


# Driver Code
str = "(()))(()()())))"
print(findIndex(str))

# This code is contributed by Aditya Kumar (adityakumar129) and Sankararaman (sankararamank).
-------------------------------------------------
#Output
#9
#Time Complexity: O(N), Where N is the size of given string
#Auxiliary Space: O(1)

#Approach 3: (Solution in 1 iteration) 

#Count the total number of closed brackets in string and store in variable, let’s say cnt_close.
#So count of open brackets is length of (string – count) of closed brackets.
#Traverse string again but now keep count of open brackets in string, let’s say cnt_open.
#Now while traversing, let index be i, so count of closed brackets till that index will be (i+1 – cnt_open).
#Hence, we can check for what index, the count of open brackets in first part equals that of count of closed brackets in second part.
#Equation becomes cnt_close – (i+1 – cnt_open) = cnt_open, we have to find i.
#After evaluating above equation we can see cnt_open gets cancelled on both sides so no need for the extra loop and simply return cnt_close.

# Method to find an equal index
def findIndex(str):
	cnt_close = 0
	l = len(str)
	for i in range(0, l):
		if(str[i] == ')'):
			cnt_close = cnt_close + 1

	return cnt_close

# Driver Code
str = "(()))(()()())))"
print(f"OP: {findIndex(str)}")
# This code is contributed by Sankararaman (sankararamank).


#Output
#OP: 9
#Time Complexity: O(N), Where N is the size of the given string
#Auxiliary Space: O(1)

#This article is contributed by Sahil Chhabra (akku)  and Sankararaman K. If you like GeeksforGeeks and would like to contribute, you can also write an article using write.geeksforgeeks.org or mail your article to review-team@geeksforgeeks.org. See your article appearing on the GeeksforGeeks main page and help other Geeks. 



