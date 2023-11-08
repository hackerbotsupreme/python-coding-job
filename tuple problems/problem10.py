#python program  to remove tuples from the list having element true.
#Python – Remove Tuples from the List having every element as None



#Method #1 : Using all() + list comprehension

#In this, we use all() to check for all None values for 
# discarding and list comprehension does task of iteration.

 #Python3 code to demonstrate working of
# Remove None Tuples from List
# Using all() + list comprehension
 
# initializing list
test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
 
# printing original list
print("The original list is : " + str(test_list))
 
# negating result for discarding all None Tuples
res = [sub for sub in test_list if not all(ele == None for ele in sub)]
 
# printing result
print("Removed None Tuples : " + str(res))






#Method #2 : Using filter() + lambda + all()

#In this method, task of filtering None tuples is done 
# using filter() and lambda function to provide None checking 
# functionality using all().
# Python3 code to demonstrate working of
# Remove None Tuples from List
# Using filter() + lambda + all()
 
# initializing list
test_list = [(None, 2), (None, None), (3, 4), (12, 3), (None, )]
 
# printing original list
print("The original list is : " + str(test_list))
 
# filter() + lambda to drive logic of discarding tuples
res = list(filter(lambda sub : not all(ele == None for ele in sub), test_list))
 
# printing result
print("Removed None Tuples : " + str(res))



#Method #3: Using count() method

#If count of None in each tuple equals to length of tuple,
# then the entire tuple elements are None.Used this in if condition
# and appended other tuples to output list
# Python3 code to demonstrate working of
# Remove None Tuples from List
 
# initializing list
test_list = [(None, None), (None, None), (3, 4), (12, 3), (None, )]
 
# printing original list
print("The original list is : " + str(test_list))
 
# negating result for discarding all None Tuples
res=[]
for i in test_list:
    if not(i.count(None)== len(i)):
        res.append(i)
 
# printing result
print("Removed None Tuples : " + str(res))








