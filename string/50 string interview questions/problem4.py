#Converting Decimal Number lying between 1 to 3999 to Roman Numerals

#Examples: 

#Input : 9
#Output : IX

#Input : 40
#Output : XL

#Input :  1904
#Output : MCMIV

#Idea is to convert the units, tens, hundreds, and thousands of places of the given number separately. If the digit is 0, then there’s no corresponding Roman numeral symbol. The conversion of digit’s 4’s and 9’s are little bit different from other digits because these digits follow subtractive notation. 

#Algorithm to convert decimal number to Roman Numeral 
#Compare given number with base values in the order 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1. Base value which is just smaller or equal to the given number will be the initial base value (largest base value) .Divide the number by its largest base value, the corresponding base symbol will be repeated quotient times, the remainder will then become the number for future division and repetitions.The process will be repeated until the number becomes zero.

#Example to demonstrate above algorithm: 

#Convert 3549 to its Roman Numerals
#Explanation: 

#Explanation:

#Step 1

#Initially number = 3549
#Since 3549 >= 1000 ; largest base value will be 1000 initially.
#Divide 3549/1000. Quotient = 3, Remainder =549. The corresponding symbol M will be repeated thrice.
#We append the Result value in the 2nd List.
#Now Remainder is not equal to 0 so we call the function again.
#Step 2

#Now, number = 549
#1000 > 549 >= 500 ; largest base value will be 500.
#Divide 549/500. Quotient = 1, Remainder =49. The corresponding symbol D will be repeated once & stop the loop.
#We append the Result value in the 2nd List.
#Now Remainder is not equal to 0 so we call the function again.
#Step 3

#Now, number = 49
#50 > 49 >= 40 ; largest base value is 40.
#Divide 49/40. Quotient = 1, Remainder = 9. The corresponding symbol XL will be repeated once & stop the loop.
#We append the Result value in the 2nd List.
#Now Remainder is not equal to 0 so we call the function again.
#Step 4

#Now, number = 9
#Number 9 is present in list ls so we directly fetch the value from dictionary dict and set Remainder=0 & stop the loop.
#Remainder = 0. The corresponding symbol IX will be repeated once and now remainder value is 0 so we will not call the function again.
#Step 5

#Finally, we join the 2nd list values.
#The output obtained MMMDXLIX.
#Following is the implementation of the above algorithm: 

# Python3 program to convert
# decimal number to roman numerals

ls=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
dict={1:"I",4:"IV",5:"V",9:"IX",10:"X",40:"XL",50:"L",90:"XC",100:"C",400:"CD",500:"D",900:"CM",1000:"M"}
ls2=[]

# Function to convert decimal to Roman Numerals
def func(no,res):
	for i in range(0,len(ls)):
		if no in ls:
			res=dict[no]
			rem=0
			break
		if ls[i]<no:
			quo=no//ls[i]
			rem=no%ls[i]
			res=res+dict[ls[i]]*quo
			break
	ls2.append(res)
	if rem==0:
		pass
	else:
		func(rem,"")


# Driver code
if __name__ == "__main__":
	func(3549, "")
	print("".join(ls2))

# This code is contributed by
# VIKAS CHOUDHARY(vikaschoudhary344)


#Another Approach 1:
#In this approach, we have to first observe the problem. The number given in problem statement can be maximum of 4 digits. The idea to solve this problem is: 

#Divide the given number into digits at different places like one’s, two’s, hundred’s or thousand’s.
#Starting from the thousand’s place print the corresponding roman value. For example, if the digit at thousand’s place is 3 then print the roman equivalent of 3000.
#Repeat the second step until we reach one’s place.
#Example: 
#Suppose the input number is 3549. So, starting from thousand’s place we will start printing the roman equivalent. In this case we will print in the order as given below: 
#First: Roman equivalent of 3000 
#Second: Roman equivalent of 500 
#Third: Roman equivalent of 40 
#Fourth: Roman equivalent of 9 
#So, the output will be: MMMDXLIX

#Below is the implementation of above idea. 
# Python3 program for above approach

# Function to calculate roman equivalent


def intToRoman(num):

	# Storing roman values of digits from 0-9
	# when placed at different places
	m = ["", "M", "MM", "MMM"]
	c = ["", "C", "CC", "CCC", "CD", "D",
		"DC", "DCC", "DCCC", "CM "]
	x = ["", "X", "XX", "XXX", "XL", "L",
		"LX", "LXX", "LXXX", "XC"]
	i = ["", "I", "II", "III", "IV", "V",
		"VI", "VII", "VIII", "IX"]

	# Converting to roman
	thousands = m[num // 1000]
	hundreds = c[(num % 1000) // 100]
	tens = x[(num % 100) // 10]
	ones = i[num % 10]

	ans = (thousands + hundreds +
		tens + ones)

	return ans


# Driver code
if __name__ == "__main__":

	number = 3549

	print(intToRoman(number))

# This code is contributed by rutvik_56
#Output
#MMMDXLIX


#Another Approach 2:
#In this approach we consider the main significant digit in the number. Ex: in 1234, main significant digit is 1. Similarly in 345 it is 3. 
#In order to extract main significant digit out, we need to maintain a divisor (lets call it div) like 1000 for 1234 (since 1234 / 1000 = 1) and 100 for 345 (345 / 100 = 3). 
#Also, lets maintain a dictionary called romanNumeral = {1 : ‘I’, 5: ‘V’, 10: ‘X’, 50: ‘L’, 100: ‘C’, 500: ‘D’, 1000: ‘M’} 

#Following is the algorithm: 

#if main significant digit <= 3

#romanNumeral[div] * mainSignificantDigit 
#if main significant digit == 4

#romanNumeral[div] + romanNumeral[div * 5] 
#if 5 <= main significant digit <=8

#romanNumeral[div * 5] + (romanNumeral[div] * ( mainSignificantDigit-5))
#if main significant digit ==9

#romanNumeral[div] + romanNumeral[div*10]
#Example: 
#Suppose the input number is 3649. 

#Iter 1
 

#Initially number = 3649
#main significant digit is 3. Div = 1000.
#So, romanNumeral[1000] * 3
#gives: MMM 
#Iter 2

#now, number = 649
#main significant digit is 6. Div = 100.
#So romanNumeral[100*5] + (romanNumeral[div] * ( 6-5))
#gives: DC 
#Iter 3

#now, number = 49
#main significant digit is 4. Div = 10.
#So romanNumeral[10] + romanNumeral[10 * 5]
#gives: XL
#Iter 4

#now, number = 9
#main significant digit is 9. Div = 1.
#So romanNumeral[1] * romanNumeral[1*10]
#gives: IX
#Final result by clubbing all the above: MMMDCXLIX  

#Below is the Python implementation of above idea.

# Python 3 program to convert Decimal
# number to Roman numbers.
import math
 
def integerToRoman(A):
    romansDict = \
        {
            1: "I",
            5: "V",
            10: "X",
            50: "L",
            100: "C",
            500: "D",
            1000: "M",
            5000: "G",
            10000: "H"
        }
 
    div = 1
    while A >= div:
        div *= 10
 
    div //= 10
 
    res = ""
 
    while A:
 
        # main significant digit extracted
        # into lastNum
        lastNum = (A // div)
 
        if lastNum <= 3:
            res += (romansDict[div] * lastNum)
        elif lastNum == 4:
            res += (romansDict[div] +
                          romansDict[div * 5])
        elif 5 <= lastNum <= 8:
            res += (romansDict[div * 5] +
            (romansDict[div] * (lastNum - 5)))
        elif lastNum == 9:
            res += (romansDict[div] +
                         romansDict[div * 10])
 
        A = math.floor(A % div)
        div //= 10
         
    return res
 
# Driver code
print("Roman Numeral of Integer is:"
                   + str(integerToRoman(3549)))
#Output
#Roman Numeral of Integer is:MMMDXLIX
#Time Complexity: O(N), where N is the length of res string that stores the conversion.
#Auxiliary Space: O(N)

#Thanks to Sriharsha Sammeta for providing the above solution approach.


-----------------------------------------------------------------

#Approach 3: Using Ladder if-else

#The idea is simple, it follows the basic fundamentals of roman numbers as iterating through the greatest to smallest number using if else and check of it exist then add that roman symbol to the answer and decrement that number.

#Steps to solve the problem:

#Declare ans variable to store the roman symbol.
#Iterate through all the roman integer value from greatest to smallest until the number is not equal to zero:
#If num>=1000 then ans+=”M” and num-=1000.
#else if num>=900 && num<1000 then ans+=”CM” and num-=900, and so on till num is not zero
#4. Return the ans
#Implementation of the approach:


# Python Program for above approach
# Function to calculate roman equivalent
def intToRoman(num):
   
    # Initialize the ans string
    ans = ""
     
    # calculate the roman numbers
    while(num > 0):
        if(num >= 1000):
            ans += "M"
            num -= 1000
             
        # check for all the corner cases like 900,400,90,40,9,4 etc.
        elif(num >= 900 and num < 1000):
            ans += "CM"
            num -= 900
 
        elif(num >= 500 and num < 900):
            ans += "D"
            num -= 500
 
        elif(num >= 400 and num < 500):
            ans += "CD"
            num -= 400
 
        elif(num >= 100 and num < 400):
            ans += "C"
            num -= 100
 
        elif(num >= 90 and num < 100):
            ans += "XC"
            num -= 90
 
        elif(num >= 50 and num < 90):
            ans += "L"
            num -= 50
 
        elif(num >= 40 and num < 50):
            ans += "XL"
            num -= 40
 
        elif(num >= 10 and num < 40):
            ans += "X"
            num -= 10
 
        elif(num == 9):
            ans += "IX"
            num -= 9
 
        elif(num >= 5 and num < 9):
            ans += "V"
            num -= 5
 
        elif(num == 4):
            ans += "IV"
            num -= 4
 
        elif(num < 4):
            ans += "I"
            num = num - 1
 
    # return the result
    return ans
 
number = 3549
print(intToRoman(number))
 
# This code is contributed by Yash Agarwal(yashagarwal2852002)
#Output
#MMMDXLIX
#Time Complexity: O(N), where N is the length of ans string that stores the conversion.
