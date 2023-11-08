#python program to find tuples with positive elements in list of tuples.
#Python program to find Tuples with positive elements in List of tuples



#Examples:

#Input : test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
#Output : [(4, 5, 9)] 
#Explanation : Extracted tuples with all positive elements.
#Input : test_list = [(-4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, -6)] 
#Output : [] 
#Explanation : No tuple with all positive elements. 



#Method #1 : Using list comprehension + all()

#In this, all() is used to check for all the tuples, list comprehension helps in the iteration of tuples.
# Python3 code to demonstrate working of
# Positive Tuples in List
# Using list comprehension + all()
 
# initializing list
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# all() to check each element
res = [sub for sub in test_list if all(ele >= 0 for ele in sub)]
 
# printing result
print("Positive elements Tuples : " + str(res))



#Output
#The original list is : [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)] 
#Positive elements Tuples : [(4, 5, 9), (4, 6)]
 
#Method #2 : Using filter() + lambda + all()

#In this, the task of filtration is performed using filter() and lambda function.
# Python3 code to demonstrate working of
# Positive Tuples in List
# Using filter() + lambda + all()
 
# initializing list
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
 
# printing original list
print("The original list is : " + str(test_list))
 
# all() to check each element
res = list(filter(lambda sub: all(ele >= 0 for ele in sub), test_list))
 
# printing result
print("Positive elements Tuples : " + str(res))



#Method #3 : Using find(),map(),list() and join()

#Convert each tuple element to string and then convert that tuple to a list.After that join elements of list using space.Now check if that joined list(which is a string) contains – sign in it.If – sign is found then tuple contains negative elements.Ignore such tuples and add the other tuples to output list

# Python3 code to demonstrate working of
# Positive Tuples in List
 
# initializing list
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
 
# printing original list
print("The original list is : " + str(test_list))
 
res=[]
for i in test_list:
    x=list(map(str,i))
    a=" ".join(x)
    if(a.find("-")==-1):
        res.append(i)
 
# printing result
print("Positive elements Tuples : " + str(res))

Method #4 : Using list(),map(),join() and startswith() methods

# Python3 code to demonstrate working of
# Positive Tuples in List
 
# initializing list
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
 
# printing original list
print("The original list is : " + str(test_list))
 
res = []
for i in test_list:
    x = sorted(i)
    x = list(map(str, x))
    b = "".join(x)
    if(not b.startswith("-")):
        res.append(i)
 
# printing result
print("Positive elements Tuples : " + str(res))


Method #5 :  By defining a function and using len() method

# Python3 code to demonstrate working of
# Positive Tuples in List
 
# initializing list
test_list = [(4, 5, 9), (-3, 2, 3), (-3, 5, 6), (4, 6)]
 
# printing original list
print("The original list is : " + str(test_list))
res = []
 
 
def fun(x):
    c = 0
    for i in x:
        if(i > 0):
            c += 1
    if(c == len(x)):
        return True
    return False
 
 
for i in test_list:
    if(fun(i)):
        res.append(i)
 
# printing result
print("Positive elements Tuples : " + str(res))








