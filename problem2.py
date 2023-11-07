#problems for printing  pyramid patterns .
#Patterns can be printed in python using simple for loops. First outer loop is used to handle the number of rows and the Inner nested loop is used to handle the number of columns. Manipulating the print statements, different number patterns, alphabet patterns, or star patterns can be printed. 

#Some of the Patterns are shown in this article. 

#Simple pyramid pattern

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	
	# outer loop to handle number of rows
	# n in this case
	for i in range(0, n):
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ",end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
pypart(n)


#Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# Approach 2: Using List in Python 3, this could be done in a simpler way
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern
def pypart(n):
	myList = []
	for i in range(1,n+1):
		myList.append("*"*i)
	print("\n".join(myList))

# Driver Code
n = 5
pypart(n)

#Output
# *
# **
# ***
# ****
# *****


# Approach 3: Using recursion


#python3 code to print pyra

#python3 code to print pyramid pattern using recursion
def pypart(n):
	if n==0:
		return
	else:
		pypart(n-1)
		print("* "*n)

# Driver Code
n = 5
pypart(n)
#this code is contributed by Shivesh Kumar Dwivedi
# Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
#Approach 4: Using while loop 
# python3 code to print pyramid pattern using while loop

# input
n=5

i=1;j=0
# while loop check the condition until the
# condition become false. if it is true then
# enter in to loop and print the pattern
while(i<=n):
	while(j<=i-1):
		print("* ",end="")
		j+=1
	# printing next line for each row
	print("\r")
	j=0;i+=1

	
	
# this code is contributed by gangarajula laxmi
#Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
#After 180 degrees rotation

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern
def pypart2(n):
     
    # number of spaces
    k = 2*n - 2
 
    # outer loop to handle number of rows
    for i in range(0, n):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 2
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
pypart2(n)
# Output
#        * 
#      * * 
#     * * * 
#   * * * * 
# * * * * * 

#Optimized Solution:

#Here, we have to print a space (height – row) times and then print “*” row times.

#For example: let height of the pyramid is 5

#then , on the row number 1 we print blank space 4 times(that is 5-1 or height -row)

#and then we print star 1 time(that is row times) and then a new line

#then , on the row number 2 we print blank space 3 times(that is 5-2 or height -row)

#and then we print star 2 times (that is row times) and then a new line

#and so on….


#Method: Using while loop
# python3 code to print pyramid pattern using while loop
n=5;i=0
while(i<=n):
print(" " * (n - i) +"*" * i)
i+=1

#Output
     
#    *
#   **
#  ***
# ****
#*****
#Method: Using for loop

#python3 code to implement above approach
height = 5
for row in range(1, height+ 1):
    print(" " * (height - row) +"*" * row)
#this code is contributed by Shivesh kumar dwivedi
#Output

#    *
#   **
#  ***
# ****
#*****

#Printing Triangle
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern triangle
def triangle(n):
	
	# number of spaces
	k = n - 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# inner loop to handle number spaces
		# values changing acc. to requirement
		for j in range(0, k):
			print(end=" ")
	
		# decrementing k after each loop
		k = k - 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing stars
			print("* ", end="")
	
		# ending line after each row
		print("\r")

# Driver Code
n = 5
triangle(n)
#Output
#    * 
#   * * 
#  * * * 
# * * * * 
#* * * * * 
#Number Pattern
# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	# initialising starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		num = 1
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

# Driver code
n = 5
numpat(n)

# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
	
	# initialising starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# re assigning num
		num = 1
	
		# inner loop to handle number of columns
			# values changing acc. to outer loop
		for j in range(0, i+1):
		
				# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

# Driver code
n = 5
numpat(n)

#Output
#1 
#1 2 
#1 2 3 
#1 2 3 4 
#1 2 3 4 5 
#Numbers without reassigning


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def contnum(n):
	
	# initializing starting number
	num = 1

	# outer loop to handle number of rows
	for i in range(0, n):
	
		# not re assigning num
		# num = 1
	
		# inner loop to handle number of columns
		# values changing acc. to outer loop
		for j in range(0, i+1):
		
			# printing number
			print(num, end=" ")
		
			# incrementing number at each column
			num = num + 1
	
		# ending line after each row
		print("\r")

n = 5

# sending 5 as argument
# calling Function
contnum(n)
#Output
#1 
#2 3 
#4 5 6 
#7 8 9 10 
#11 12 13 14 15 
Character Pattern

# Python 3.x code to demonstrate star pattern
 
# Function to demonstrate printing pattern of alphabets
def alphapat(n):
     
    # initializing value corresponding to 'A'
    # ASCII value
    num = 65
 
    # outer loop to handle number of rows
    # 5 in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # explicitly converting to char
            ch = chr(num)
         
            # printing char value
            print(ch, end=" ")
     
        # incrementing number
        num = num + 1
     
        # ending line after each row
        print("\r")
 
# Driver Code
n = 5
alphapat(n)

#Output
#A 
#B B 
#C C C 
#D D D D 
#E E E E E 

#Continuous Character pattern
# Python code 3.x to demonstrate star pattern

# Function to demonstrate printing pattern of alphabets


def contalpha(n):

	# initializing value corresponding to 'A'
	# ASCII value
	num = 65


	# outer loop to handle number of rows
- for i in range(0, n):

	# inner loop to handle number of columns
	# values changing acc. to outer loop
	for j in range(0, i+1):

		# explicitly converting to char
		ch = chr(num)

		# printing char value
		print(ch, end=" ")

		# incrementing at each column
		num = num + 1

	# ending line after each row
	print("\r")

# Driver code
n = 5
contalpha(n)


#Output:

#A 
#B C 
#D E F 
#G H I J 
#K L M N O