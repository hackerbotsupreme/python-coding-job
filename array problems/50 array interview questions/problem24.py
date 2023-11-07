#Find the Factorial of a large number

#Difficulty Level : Medium
#---------------------------------------------------------------------------------
#Find the factorial of a large number. 

#What is Factorial of a number?
#Factorial of a non-negative integer, is the multiplication of all integers smaller than or equal to n. 

#Factorial of a number
#Factorial of a number

#Examples: 

#Input: 100
#Output: 933262154439441526816992388562667004-
#         907159682643816214685929638952175999-
#         932299156089414639761565182862536979-
#         208272237582511852109168640000000000-
#         00000000000000


#Input: 50
#Output: 3041409320171337804361260816606476884-
#         4377641568960512000000000000

#We have discussed a simple program for factorial.

#Why conventional way of computing factorial fails for large numbers?
#A factorial of 100 has 158 digits. It is not possible to store these many digits even if we use long int. 
#---------------------------------------------------------------------


#The idea is to use basic mathematics for multiplication.

#Illustration:

#Example to show working of multiply(res[], x)

#A number 5189 is stored in res[] as following: res[] = {9, 8, 1, 5}
#let x = 10
#Initialize carry = 0

 

#At i = 0, prod = res[0]*x + carry = 9*10 + 0 = 90.
#res[0] = 0, carry = 9
 


 

#At i = 1, prod = res[1]*x + carry = 8*10 + 9 = 89
#res[1] = 9, carry = 8

 

 

#At i = 2, prod = res[2]*x + carry = 1*10 + 8 = 18
#res[2] = 8, carry = 1

 

 


#At i = 3, prod = res[3]*x + carry = 5*10 + 1 = 51
#res[3] = 1, carry = 5

 

 

#res[4] = carry = 5
#res[] = {0, 9, 8, 1, 5} 

 

#Follow the steps below to solve the given problem:

#Create an array res[] of MAX size where MAX is a number of maximum digits in output. 
#Initialize value stored in res[] as 1 and initialize res_size (size of ‘res[]’) as 1. 
#Multiply x with res[] and update res[] and res_size to store the multiplication result for all the numbers from x = 2 to n.
#To multiply a number x with the number stored in res[], one by one multiply x with every digit of res[].
#To implement multiply function perform the following steps:
#Initialize carry as 0. 
#Do following for i = 0 to res_size – 1 
#Find value of res[i] * x + carry. Let this value be prod. 
#Update res[i] by storing the last digit of prod in it. 
#Update carry by storing the remaining digits in carry. 
#Put all digits of carry in res[] and increase res_size by the number of digits in carry.
#Below is the implementation of the above algorithm. 

#NOTE: In the below implementation, the maximum digits in the output are assumed as 500. To find a factorial of a much larger number ( > 254), increase the size of an array or increase the value of MAX. This can also be solved using Linked List instead of using res[] array which will not waste extra space.

# Python program to compute factorial
# of big numbers
 
import sys
 
# This function finds factorial of large
# numbers and prints them
 
 
def factorial(n):
    res = [None]*500
    # Initialize result
    res[0] = 1
    res_size = 1
 
    # Apply simple factorial formula
    # n! = 1 * 2 * 3 * 4...*n
    x = 2
    while x <= n:
        res_size = multiply(x, res, res_size)
        x = x + 1
 
    print("Factorial of given number is")
    i = res_size-1
    while i >= 0:
        sys.stdout.write(str(res[i]))
        sys.stdout.flush()
        i = i - 1
 
 
# This function multiplies x with the number
# represented by res[]. res_size is size of res[]
# or number of digits in the number represented
# by res[]. This function uses simple school
# mathematics for multiplication. This function
# may value of res_size and returns the new value
# of res_size
def multiply(x, res, res_size):
 
    carry = 0  # Initialize carry
 
    # One by one multiply n with individual
    # digits of res[]
    i = 0
    while i < res_size:
        prod = res[i] * x + carry
        res[i] = prod % 10  # Store last digit of
        # 'prod' in res[]
        # make sure floor division is used
        carry = prod//10  # Put rest in carry
        i = i + 1
 
    # Put carry in res and increase result size
    while (carry):
        res[res_size] = carry % 10
        # make sure floor division is used
        # to avoid floating value
        carry = carry // 10
        res_size = res_size + 1
 
    return res_size
 
 
# Driver program
factorial(100)
 
# This code is contributed by Nikita Tiwari.
#Output
#Factorial of given number is 
#93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
#Time Complexity: O(N log (N!)), where O(N) is for loop and O(log N!) is for nested while loop
#Auxiliary Space: O(max(digits in factorial))
#------------------------------------------------------------------------
#Find the Factorial of a large number using Basic BigInteger
#This problem can be solved using the below idea:

#Big Integer can also be used to calculate the factorial of large numbers.

#Illustration:

#N = 5

ans = 1

#At i = 2: ans = ans x i = 1 x 2 = 2
#At i = 3: ans = ans x i = 2 x 3 = 6
#At i = 4: ans = ans x i = 6 x 4 = 24
#At i = 5: ans = ans x i = 24 x 5 = 120

#Hence factorial of N is 120

#Follow the steps below to solve the given problem: 

#Declare a BigInteger f with 1 and perform the conventional way of calculating factorial
#Traverse a loop from x = 2 to N and multiply x with f and store the resultant value in f
#Below is the implementation of the above idea : 

# Python3 program to find large
# factorials
 
# Returns Factorial of N
def factorial(N):
 
    # Initialize result
    f =  1 
     
    # Multiply f with 2, 3, ...N
    for i in range(2, N + 1):
        f *= i
     
    return f;
 
 
# Driver method
N = 20;
print(factorial(N));
 
 
# This code is contributed by phasing17
#Output
#2432902008176640000
#Time Complexity: O(n)
#Auxiliary Space: O(1)
#-------------------------------------------------------------------

