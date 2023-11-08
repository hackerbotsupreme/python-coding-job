#Converting Roman Numerals to Decimal lying between 1 to 3999
#Example : 

#Input: IX
#Output: 9
#IX is a Roman symbol which represents 9 

#Input: XL
#Output: 40
#XL is a Roman symbol which represents 40

#Input: MCMIV
#Output: 1904
#M is a thousand, 
#CM is nine hundred and 
#IV is four

#Approach: A number in Roman Numerals is a string of these symbols written in descending order(e.g. M’s first, followed by D’s, etc.). However, in a few specific cases, to avoid four characters being repeated in succession(such as IIII or XXXX), subtractive notation is often used as follows: 

#I placed before V or X indicates one less, so four is IV (one less than 5) and 9 is IX (one less than 10).
#X placed before L or C indicates ten less, so forty is XL (10 less than 50) and 90 is XC (ten less than a hundred).
#C placed before D or M indicates a hundred less, so four hundred is CD (a hundred less than five hundred) and nine hundred is CM (a hundred less than a thousand).
#Algorithm to convert Roman Numerals to Integer Number:  

#Split the Roman Numeral string into Roman Symbols (character).
#Convert each symbol of Roman Numerals into the value it represents.
#Take symbol one by one from starting from index 0: 
#If current value of symbol is greater than or equal to the value of next symbol, then add this value to the running total.
#else subtract this value by adding the value of next symbol to the running total.




# Python program to convert Roman Numerals
# to Numbers

# This function returns value of each Roman symbol


def value(r):
	if (r == 'I'):
		return 1
	if (r == 'V'):
		return 5
	if (r == 'X'):
		return 10
	if (r == 'L'):
		return 50
	if (r == 'C'):
		return 100
	if (r == 'D'):
		return 500
	if (r == 'M'):
		return 1000
	return -1


def romanToDecimal(str):
	res = 0
	i = 0

	while (i < len(str)):

		# Getting value of symbol s[i]
		s1 = value(str[i])

		if (i + 1 < len(str)):

			# Getting value of symbol s[i + 1]
			s2 = value(str[i + 1])

			# Comparing both values
			if (s1 >= s2):

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s1
				i = i + 1
			else:

				# Value of current symbol is greater
				# or equal to the next symbol
				res = res + s2 - s1
				i = i + 2
		else:
			res = res + s1
			i = i + 1

	return res


# Driver code
print("Integer form of Roman Numeral is"),
print(romanToDecimal("MCMIV"))

Complexity Analysis: 

Time Complexity: O(n), where n is the length of the string. 
Only one traversal of the string is required.
Space Complexity: O(1). 
As no extra space is required.
Another solution –


# Program to convert Roman
# Numerals to Numbers
roman = {}
roman['I'] = 1
roman['V'] = 5
roman['X'] = 10
roman['L'] = 50
roman['C'] = 100
roman['D'] = 500
roman['M'] = 1000
     
# This function returns value
# of a Roman symbol
def romanToInt(s):
   sum = 0
   n = len(s)
 
   i = 0
   while i < n :
 
      # If present value is less than next value,
      # subtract present from next value and add the
      # resultant to the sum variable.
      # print(roman[s[i]],roman[s[i+1]])
      if (i != n - 1 and roman[s[i]] < roman[s[i + 1]]):
         sum += roman[s[i + 1]] - roman[s[i]]
         i += 2
         continue
      else:
         sum += roman[s[i]]
      i += 1
   return sum
 
# Driver Code
     
# Considering inputs given are valid
input = "MCMIV"
 
print(f"Integer form of Roman Numeral is {romanToInt(input)}")
 
# This code is contributed by shinjanpatra

#Output
#Integer form of Roman Numeral is 1904

def romanToInt(s):
		translations = {
			"I": 1,
			"V": 5,
			"X": 10,
			"L": 50,
			"C": 100,
			"D": 500,
			"M": 1000
		}
		number = 0
		s = s.replace("IV", "IIII").replace("IX", "VIIII")
		s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
		s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
		for char in s:
			number += translations[char]
		print(number)
		
romanToInt('MCMIV')
#Roman to integer using Ladder If-Else approach :
#This approach is basically follows the fundamental logic of roman numbers , just apply the condition in ladder form like if the first character is ‘I’ then next should be ‘V’ to make it 4 in number else it will be 1.


// Program to convert Roman
// Numerals to Numbers
#include <bits/stdc++.h>
using namespace std;

int romanToDecimal(string s) {
/* declare two variables first will calculate the number and second will help
	in iterating through the string character-wise*/
		int ans=0,i;
		for( i=0;i<s.size()-1;i++){
			if(s[i]=='I'&&s[i+1]=='V')
			{
				ans+=4;i++;continue;
			}
			else if(s[i]=='I'&&s[i+1]=='X')
			{
				ans+=9;i++;continue;
			}
			else if(s[i]=='X'&&s[i+1]=='L')
			{
				ans+=40;i++;continue;
			}
			else if(s[i]=='X'&&s[i+1]=='C')
			{
				ans+=90;i++;continue;
			}
			else if(s[i]=='C'&&s[i+1]=='D')
			{
				ans+=400;i++;continue;
			}
			else if(s[i]=='C'&&s[i+1]=='M')
			{
				ans+=900;i++;continue;
			}
		//till this we checked all the category like 4,9,40,90 etc.
			else if(s[i]=='I')
				ans+=1;
			else if(s[i]=='V')
				ans+=5;
			else if(s[i]=='X')
				ans+=10;
			else if(s[i]=='L')
				ans+=50;
			else if(s[i]=='C')
				ans+=100;
			else if(s[i]=='D')
				ans+=500;
			else if(s[i]=='M')
				ans+=1000;
		}
/* for last character that left in the string if last two char comes not in the category
	of 4,9,40,90 etc as loop is iterating till size-1*/
		if(s.size()>i){
			if(s[i]=='I')
				ans+=1;
			else if(s[i]=='V')
				ans+=5;
			else if(s[i]=='X')
				ans+=10;
			else if(s[i]=='L')
				ans+=50;
			else if(s[i]=='C')
				ans+=100;
			else if(s[i]=='D')
				ans+=500;
			else if(s[i]=='M')
				ans+=1000;
		}
		
		return ans;
	}

// Driver Code
int main()
{
	// Considering inputs given are valid
	string str = "MCMIV";
	cout << "Integer form of Roman Numeral is "
		<< romanToDecimal(str) << endl;

	return 0;
}
//this code is contributed by Prateek Kumar Singh


#Output
#Integer form of Roman Numeral is 1904

















































