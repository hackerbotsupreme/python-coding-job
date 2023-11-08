#python program to sort by total digita.

#Examples:

#Input : test_list = [(3, 4, 6, 723), (1, 2), (134, 234, 34)] 
#Output : [(1, 2), (3, 4, 6, 723), (134, 234, 34)] 
#Explanation : 2 < 6 < 8, sorted by increasing total digits.
 

#Input : test_list = [(1, 2), (134, 234, 34)] 
#Output : [(1, 2), (134, 234, 34)] 
#Explanation : 2 < 8, sorted by increasing total digits. 


#Method #1: Using sort() + len() + sum()

#In this, we get all sum of all lengths of each element in the tuple by string conversion and len(). Then sort() is used with key to solve this problem.

# Python3 code to demonstrate working of 
# Sort Tuples by Total digits
# Using sort() + len() + sum()
  
def count_digs(tup):
      
    # gets total digits in tuples
    return sum([len(str(ele)) for ele in tup ])
  
# initializing list
test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# performing sort 
test_list.sort(key = count_digs)
  
# printing result 
print("Sorted tuples : " + str(test_list))




# Method #2 : Using sorted() + lambda + sum() + len()

#In this, we perform task of sorting using sorted(), and the lambda function performs the task of computation of total digits in tuples.


# Python3 code to demonstrate working of 
# Sort Tuples by Total digits
# Using sorted() + lambda + sum() + len()
  
# initializing list
test_list = [(3, 4, 6, 723), (1, 2), (12345,), (134, 234, 34)]
  
# printing original list
print("The original list is : " + str(test_list))
  
# performing sort, lambda function provides logic
res = sorted(test_list, key = lambda tup : sum([len(str(ele)) for ele in tup ]))
  
# printing result 
print("Sorted tuples : " + str(res))


