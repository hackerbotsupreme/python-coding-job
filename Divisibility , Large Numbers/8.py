Check if a large number is divisible by 13 or not

Difficulty Level : Easy
Last Updated : 22 Aug, 2022
Read
Discuss
Courses
Practice
Video
Given a large number, the task is to check if the number is divisible by 13 or not. 

Examples : 

Input :  637
Output : 637 is divisible by 13.

Input :  920
Output : 920 is not divisible by 13.

Input  : 83959092724
Output : 83959092724 is divisible by 13.
Recommended: Please try your approach on {IDE} first, before moving on to the solution.
If the given number num is small, we can easily find whether it is divisible by 13 or not by doing num % 13 and checking whether the result is 0 or not. But what about very large numbers? Let’s discuss large numbers.

Below are some interesting facts about the divisibility of 13. 

A number is divisible by 13 if and if the alternating sum (alternatively adding and subtracting) of blocks of three from right to left is divisible by 13. For example, 2911285 is divisible by 13 because the alternating sum of blocks of size 3 is 2 – 911 + 285 = -650 which is divisible by 13.
A number is divisible by 13 if and only if the number obtained by adding the last digit multiplied by 4 to the rest is also divisible by 13. 
For example, consider 2353. Applying above rule, we get 235 + 3*4 = 247. Again we apply the rule and get 24 + 7*4 = 52. Since 52 is divisible by 13, the given number is divisible by 13. 
Below is the implementation based on first fact above (Finding the alternating sum of blocks of size 3) 

C++
Java
Python3
# Python 3 program to check whether a
# number is divisible by 13 or not
 
# Returns true if number is divisible
# by 13 else returns false
def checkDivisibility( num):
    length = len(num)
    if (length == 1 and num[0] == '0'):
        return True
 
    # Append required 0s at the beginning.
    if (length % 3 == 1):
         
        # Same as strcat(num, "00");
        # in c.
        num = str(num) + "00"
        length += 2
     
    elif (length % 3 == 2):
         
        # Same as strcat(num, "0");
        # in c.
        num = str(num) + "0"
        length += 1
 
    # Alternatively add/subtract digits 
    # in group of three to result.
    sum = 0
    p = 1
    for i in range(length - 1, -1 , -1) :
         
        # Store group of three
        # numbers in group variable.
        group = 0
        group += ord(num[i]) - ord('0')
        i -= 1
        group += (ord(num[i]) - ord('0')) * 10
        i -= 1
        group += (ord(num[i]) - ord('0')) * 100
 
        sum = sum + group * p
 
        # Generate alternate series
        # of plus and minus
        p *= (-1)
    sum = abs(sum)
    return (sum % 13 == 0)
 
# Driver code
if __name__ == "__main__":
    number = "83959092724"
    if (checkDivisibility(number)):
        print( number , "is divisible by 13.")
    else:
        print( number ,"is not divisible by 13.")
 
# This code is contributed by ChitraNayal
C#
PHP
Javascript
Output
83959092724 is divisible by 13.
Time Complexity:  O(length(number))
Auxiliary Space: O(1)

Method: Checking given number is divisible by 13 or not by using the modulo division operator “%”.  

C++
Java
Python3
# Python code
# To check whether the given number is divisible by 13 or not
 
#input
n=83959092724
# the above input can also be given as n=input() -> taking input from user
# finding given number is divisible by 13 or not
if int(n)%13==0:
  print("Yes")
else:
  print("No")
 
  # this code is contributed by gangarajula laxmi
C#
PHP
Javascript
Output
Yes
Time Complexity: O(1)
Auxiliary Space: O(1)



Like
Previous
Count rotations divisible by 8
Next
Program to find remainder when large number is divided by 11
Related Articles
1.
Check if a large number is divisible by 8 or not
2.
Check if a large number is divisible by 6 or not
3.
Check if a large number is divisible by 5 or not
4.
Check a large number is divisible by 16 or not
5.
Check if the large number formed is divisible by 41 or not
6.
Check if any large number is divisible by 19 or not
7.
Check if any large number is divisible by 17 or not
8.
Check if a large number is divisible by 2, 3 and 5 or not
9.
Check if a large number is divisible by 75 or not
10.
Check whether a large number is divisible by 53 or not
Article Contributed By :
https://media.geeksforgeeks.org/auth/avatar.png
pawan_asipu
@pawan_asipu
Vote for difficulty
Current difficulty : Easy
Easy
Normal
Medium
Hard
Expert
Improved By :
jit_t
Sam007
Mithun Kumar
ukasp
_saurabh_jaiswal
surindertarika1234
laxmigangarajula03
hasani
satwik4409
varshagumber28
Article Tags :
divisibility
large-numbers
Mathematical
Practice Tags :
Mathematical