#python program to find difference between two lists.

li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

temp3 = []
for element in li1:
	if element not in li2:
		temp3.append(element)

print(temp3)


li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

s = set(li2)
temp3 = [x for x in li1 if x not in s]
print(temp3)
#Method 3:  Use a list comprehension and set to Find the Difference Between Two Lists in Python
#In this method, we convert the lists into sets explicitly and then simply reduce one from the other using the subtract operator. For more references on set visit Sets in Python. It is a similar technique that we used previously. The only difference is, that we replaced the nested loops with the list comprehension syntax.

li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

s = set(li2)
temp3 = [x for x in li1 if x not in s]
print(temp3)

#Method 4: Without using the set()
#In this method, we use the basic combination technique to copy elements from both lists with a regular check if one is present in the other or not. 

# Python code to get difference of two lists
# Not using set()
def Diff(li1, li2):
	li_dif = [i for i in li1 + li2 if i not in li1 or i not in li2]
	return li_dif

# Driver Code
li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]
li3 = Diff(li1, li2)
print(li3)

#The numpy.concatenate() function concatenate a sequence of arrays along an existing axis.



import numpy as np
li1 = np.array([10, 15, 20, 25, 30, 35, 40])
li2 = np.array([25, 40, 35])

dif1 = np.setdiff1d(li1, li2)
dif2 = np.setdiff1d(li2, li1)

temp3 = np.concatenate((dif1, dif2))
print(list(temp3))


#The elements that are either in the first set or the second set are returned using the symmetric_difference() technique. The intersection, unlike the shared items of the two sets, is not returned by this technique.



li1 = [10, 15, 20, 25, 30, 35, 40]
li2 = [25, 40, 35]

set_dif = set(li1).symmetric_difference(set(li2))
temp3 = list(set_dif)
print(temp3)
