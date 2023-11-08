#Multiply Large Numbers represented as Strings
#Given two positive numbers as strings. The numbers may be very large (may not fit in long long int), the task is to find product of these two numbers.
#Examples: 

#Input : num1 = 4154  
#        num2 = 51454
#Output : 213739916 

#Input :  num1 = 654154154151454545415415454  
#         num2 = 63516561563156316545145146514654 
#Output : 41549622603955309777243716069997997007620439937711509062916
#-----------------------------------------------------------------------
#The idea is based on school mathematics. 

#We start from last digit of second number multiply it with first number. Then we multiply second digit of second number with first number, and so on. We add all these multiplications. While adding, we put i-th multiplication shifted.
#The approach used in below solution is to keep only one array for result. We traverse all digits first and second numbers in a loop and add the result at appropriate position. 


# Python3 program to multiply two numbers
# represented as strings.

# Multiplies str1 and str2, and prints result.
def multiply(num1, num2):
	len1 = len(num1)
	len2 = len(num2)
	if len1 == 0 or len2 == 0:
		return "0"

	# will keep the result number in vector
	# in reverse order
	result = [0] * (len1 + len2)
	
	# Below two indexes are used to
	# find positions in result.
	i_n1 = 0
	i_n2 = 0

	# Go from right to left in num1
	for i in range(len1 - 1, -1, -1):
		carry = 0
		n1 = ord(num1[i]) - 48

		# To shift position to left after every
		# multiplication of a digit in num2
		i_n2 = 0

		# Go from right to left in num2
		for j in range(len2 - 1, -1, -1):
			
			# Take current digit of second number
			n2 = ord(num2[j]) - 48
		
			# Multiply with current digit of first number
			# and add result to previously stored result
			# at current position.
			summ = n1 * n2 + result[i_n1 + i_n2] + carry

			# Carry for next iteration
			carry = summ // 10

			# Store result
			result[i_n1 + i_n2] = summ % 10

			i_n2 += 1

			# store carry in next cell
		if (carry > 0):
			result[i_n1 + i_n2] += carry

			# To shift position to left after every
			# multiplication of a digit in num1.
		i_n1 += 1
		
		# print(result)

	# ignore '0's from the right
	i = len(result) - 1
	while (i >= 0 and result[i] == 0):
		i -= 1

	# If all were '0's - means either both or
	# one of num1 or num2 were '0'
	if (i == -1):
		return "0"

	# generate the result string
	s = ""
	while (i >= 0):
		s += chr(result[i] + 48)
		i -= 1

	return s

# Driver code
str1 = "1235421415454545454545454544"
str2 = "1714546546546545454544548544544545"

if((str1[0] == '-' or str2[0] == '-') and
(str1[0] != '-' or str2[0] != '-')):
	print("-", end = '')


if(str1[0] == '-' and str2[0] != '-'):
	str1 = str1[1:]
elif(str1[0] != '-' and str2[0] == '-'):
	str2 = str2[1:]
elif(str1[0] == '-' and str2[0] == '-'):
	str1 = str1[1:]
	str2 = str2[1:]
print(multiply(str1, str2))

# This code is contributed by ankush_953
#Output: 

#2118187521397235888154583183918321221520083884298838480662480
#The above code is adapted from the code provided by Gaurav.
#Time Complexity: O(m*n), where m and n are length of two number that need to be multiplied. 
#Auxiliary Space: O(m+n), where m and n are length of two number that need to be multiplied.

#The Way to understand:



#     The Approach:

#     Compute the ones-digit, then the tens-digit, then the hundreds-digit, etc. For example when multiplying 1234 with 5678, the thousands-digit of     the product is 4*5 + 3*6 + 2*7 + 1*8 (plus what got carried from the hundreds-digit).
#include <iostream>
#include<bits/stdc++.h>
#using namespace std;

#int main() {
#string a = "1235421415454545454545454544";
#string b = "1714546546546545454544548544544545";
if (a=="0" || b=="0"){
	cout<<0<<endl;
	return 0;
}
	int m = a.size() - 1, n = b.size() - 1, carry = 0;
	string product;
	for (int i=0; i<=m+n || carry; ++i) {
		for (int j=max(0, i-n); j<=min(i, m); ++j)
			carry += (a[m-j] - '0') * (b[n-i+j] - '0');
		product += carry % 10 + '0';
		carry /= 10;
	}
	reverse(begin(product), end(product));
cout<<"The Product is: ";
cout<<product<<endl;
//code given by sanket gode
	return 0;
}
#Time Complexity: O(m*n), where m and n are length of two number that need to be multiplied.
#Auxiliary Space: O(m+n), where m and n are length of two number that need to be multiplied.
#--------------------------------------------------------------------------
Method 2:


# Python3 program to implement the above approach
 
# function to reverse the string
def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
num1 = "1235421415454545454545454544"
tempnum1 = num1
num2 = "1714546546546545454544548544544545"
tempnum2 = num2
 
# Check condition if one string is negative
if (num1[0] == '-' and num2[0] != '-'):
    num1 = num1[1:]
elif (num1[0] != '-' and num2[0] == '-'):
    num2 = num2[1:]
elif (num1[0] == '-' and num2[0] == '-'):
    num1 = num1[1:]
    num2 = num2[1:]
  
s1 = num1
s2 = num2
s1 = reverse(s1)
s2 = reverse(s2)
m = [0]*(len(s1)+len(s2))
 
# Go from right to left in num1
for i in range(len(s1)):
   
    # Go from right to left in num2
    for j in range(len(s2)):
        m[i + j] = m[i + j] + (ord(s1[i]) - 48) * (ord(s2[j]) - 48)
       
     
product = ""
# Multiply with current digit of first number
# and add result to previously stored product
# at current position.
for i in range(len(m)):
    digit = m[i] % 10
    carry = m[i] // 10
    if (i + 1 < len(m)):
        m[i + 1] = m[i + 1] + carry
    product = str(digit) + product
   
# ignore '0's from the right
while (len(product) > 1 and product[0] == '0'):
    product = product[1:]
    
#check condition if one string is negative
if (tempnum1[0] == '-' and tempnum2[0] != '-'):
    product = "-" + product
     
elif (tempnum1[0] != '-' and tempnum2[0] == '-'):
    product = "-" + product
     
 
print("Product of the two numbers is :")
print(product)
 
 
# This code is contributed by Abhijeet Kumar(abhijeet19403)
#Output: 

#2118187521397235888154583183918321221520083884298838480662480
#Time Complexity: O(m*n), where m and n are length of two number that need to be multiplied. 
#Auxiliary Space: O(m+n), where m and n are length of two number that need to be multiplied.

