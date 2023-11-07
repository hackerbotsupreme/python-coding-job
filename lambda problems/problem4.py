#python program to count even and odd numbers in a list.


#Given a list of numbers, write a Python program to count Even and Odd numbers in a List.

#Example:

#Input: list1 = [2, 7, 5, 64, 14]
#Output: Even = 3, odd = 2

#Input: list2 = [12, 14, 95, 3]
#Output: Even = 2, odd = 2


#Example 1: 

#Count Even and Odd numbers from the given list using for loop Iterate each element in the list using for loop and check if num % 2 == 0, the condition to check even numbers. If the condition satisfies, then increase the even count else increase odd count. 
# Python program to count Even
# and Odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 1]

even_count, odd_count = 0, 0

# iterating each number in list
for num in list1:

	# checking condition
	if num % 2 == 0:
		even_count += 1

	else:
		odd_count += 1

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
#Output:
#Even numbers in the list:  3
#Odd numbers in the list:  4
# Python program to count Even and Odd numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

even_count, odd_count = 0, 0
num = 0

# using while loop	
while(num < len(list1)):
	
	# checking condition
	if list1[num] % 2 == 0:
		even_count += 1
	else:
		odd_count += 1
	
	# increment num
	num += 1
	
print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
#Output:
#Even numbers in the list:  3
#Odd numbers in the list:  4

#Example 3: Using Python Lambda Expressions 
# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

odd_count = len(list(filter(lambda x: (x%2 != 0) , list1)))

# we can also do len(list1) - odd_count
even_count = len(list(filter(lambda x: (x%2 == 0) , list1)))

print("Even numbers in the list: ", even_count)
print("Odd numbers in the list: ", odd_count)
#Output:
#Even numbers in the list:  3
#Odd numbers in the list:  4
#Example 4: Using List Comprehension 
# Python program to print odd Numbers in a List

# list of numbers
list1 = [10, 21, 4, 45, 66, 93, 11]

only_odd = [num for num in list1 if num % 2 == 1]
odd_count = len(only_odd)

print("Even numbers in the list: ", len(list1) - odd_count)
print("Odd numbers in the list: ", odd_count)
#Output:
#Even numbers in the list:  3
#Odd numbers in the list:  4

Example 5: Using Recursion


# Python program to count Even
# and Odd numbers in a List
# using recursion
even_count = 0  # even counter
i = 0  # index, so that we can check if list[i] is even or odd
odd_count = 0  # odd counter
 
 
def evenoddcount(lst):
    # defining local counters as global variable
    global even_count
    global odd_count
    global i
    if lst[i] % 2 == 0:  # check if number is even
        even_count += 1
    else:  # if number is odd
        odd_count += 1
    if i in range(len(lst)-1):
        i += 1  # increment i
        evenoddcount(lst)  # calling fonction recursively
    else:
        print("Even numbers in the list: ", even_count)
        print("Odd numbers in the list: ", odd_count)
 
 
list1 = [10, 21, 4, 45, 66, 93, 1]
evenoddcount(list1)
#Output
#Even numbers in the list:  3
#Odd numbers in the list:  4


#Method: Using the enumerate function 

lst = [12, 14, 95, 3];c=0;c1=0
for i,a in enumerate(lst):
    if a%2==0:
        c+=1
    else:
        c1+=1
     
print("even number count",c,"odd number count",c1)
#Output
#even number count 2 odd number count 2

#Method: Using Numpy.Array : 

# Python program to Print Positive Numbers in a List
import numpy as np
 
# list of numbers
List = [10, 21, 4, 45, 66, 93, 11]
 
# using numpy Array
list1 = np.array(List)
Even_list = list1[list1 % 2 == 0]
 
print("Even numbers in the list: ", len(Even_list))
print("Odd numbers in the list: ", len(list1)-len(Even_list))
#Output:

#Even numbers in the list:  3
#Odd numbers in the list:  4




