#Write your own atoi()
#The atoi() function in C takes a string (which represents an integer) as an argument and returns its value of type int. So basically the function is used to convert a string argument to an integer.

#Syntax:  

#int atoi(const char strn)
#Parameters: The function accepts one parameter strn which refers to the string argument that is needed to be converted into its integer equivalent.

#Return Value: If strn is a valid input, then the function returns the equivalent integer number for the passed string number. If no valid conversion takes place, then the function returns zero.


#Example: 

#in c++ language
#include <bits/stdc++.h>
#using namespace std;
  
#int main()
#{
#    int val;
#    char strn1[] = "12546";
#  
#    val = atoi(strn1);
#    cout <<"String value = " << strn1 << endl;
#    cout <<"Integer value = " << val << endl;
#  
#    char strn2[] = "GeeksforGeeks";
#    val = atoi(strn2);
#    cout <<"String value = " << strn2 << endl;
#    cout <<"Integer value = " << val <<endl;
  
 #   return (0);
#}
  
#// This code is contributed by shivanisinghss2110
#Output
#String value = 12546
#Integer value = 12546
#String value = GeeksforGeeks
#Integer value = 0
#Complexity Analysis:



#Time Complexity: O(n). 
#Only one traversal of the string is needed.
#Space Complexity: O(1). 
#As no extra space is required.
#Now let’s understand various ways in which one can create there own atoi() function supported by various conditions:

#Recommended Problem
#Implement Atoi
#Strings
#Design-Pattern
#+1 more
#Morgan Stanley
#Amazon
#+4 more
#Solve Problem
#Submission count: 1.3L
#Approach 1: Following is a simple implementation of conversion without considering any special case. 

#Initialize the result as 0.
#Start from the first character and update result for every character.
#For every character update the answer as result = result * 10 + (s[i] – ‘0’)

# Python program for implementation of atoi

# A simple atoi() function


def myAtoi(string):
	res = 0

	# Iterate through all characters of
	# input string and update result
	for i in range(len(string)):
		res = res * 10 + (ord(string[i]) - ord('0'))

	return res


# Driver program
string = "89789"

# Function call
print (myAtoi(string))

# This code is contributed by BHAVYA JAIN
#Output
#89789
------------------------------------------------------------
#Complexity Analysis:

#Time Complexity: O(n). 
#Only one traversal of the string is needed.
#Space Complexity: O(1). 
#As no extra space is required.
#Approach 2: This implementation handles the negative numbers. If the first character is ‘-‘ then store the sign as negative and then convert the rest of the string to number using the previous approach while multiplying sign with it. 


# Python program for implementation of atoi
# A simple atoi() function
  
  
def myAtoi(string):
    res = 0
    # initialize sign as positive
    sign = 1
    i = 0
  
    # if number is negative then update sign
    if string[0] == '-':
        sign = -1
        i += 1
  
    # Iterate through all characters 
    # of input string and update result
    for j in range(i, len(string)):
        res = res*10+(ord(string[j])-ord('0'))
  
    return sign * res
  
  
# Driver code
string = "-123"
  
# Function call
print (myAtoi(string))
  
# This code is contributed by BHAVYA JAIN
#Output
#-123
#Complexity Analysis:

#Time Complexity: O(n). 
#Only one traversal of the string is needed.
#Space Complexity: O(1). 
#As no extra space is required.
---------------------------------------------------------------

#Approach 3: Four corner cases needs to be handled: 

#Discards all leading whitespaces
#Sign of the number
#Overflow
#Invalid input
#To remove the leading whitespaces run a loop until a character of the digit is reached. If the number is greater than or equal to INT_MAX/10. Then return INT_MAX if the sign is positive and return INT_MIN if the sign is negative. The other cases are handled in previous approaches. 

#Dry Run: 



#Below is the implementation of the above approach: 


# A simple Python3 program for
# implementation of atoi
import sys
  
def myAtoi(Str):
  
    sign, base, i = 1, 0, 0
      
    # If whitespaces then ignore.
    while (Str[i] == ' '):
        i += 1
      
    # Sign of number
    if (Str[i] == '-' or Str[i] == '+'):
        sign = 1 - 2 * (Str[i] == '-')
        i += 1
  
    # Checking for valid input
    while (i < len(Str) and 
          Str[i] >= '0' and Str[i] <= '9'):
                
        # Handling overflow test case
        if (base > (sys.maxsize // 10) or
           (base == (sys.maxsize // 10) and 
           (Str[i] - '0') > 7)):
            if (sign == 1):
                return sys.maxsize
            else:
                return -(sys.maxsize)
          
        base = 10 * base + (ord(Str[i]) - ord('0'))
        i += 1
      
    return base * sign
  
# Driver Code
Str = list(" -123")
  
# Functional Code
val = myAtoi(Str)
  
print(val)
  
# This code is contributed by divyeshrabadiya07
#Output
# -123
#Complexity Analysis:

#Time Complexity: O(n). 
#O#nly one traversal of the string is needed.
#Space Complexity: O(1). 
#As no extra space is required.
#Recursive program for atoi().

#Exercise: 
#Write your won atof() that takes a string (which represents an floating point value) as an argument and returns its value as double.













































