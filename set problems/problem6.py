#write a python program to show the difference  between two lists .


#ok these problem is unexpected so what we gonna do is use operator like if, if - statement to know whether it is present or not , and 
# based on that we aer gonna print true or false

#attempt 2
#using in operator with loop like for 
li1=[1,2,3,4,5,6,8]
li2=[8,6,5,3,2,1,1]
temp=[]
for  element in li1:
    if element  in li2:
        temp.append(element)
print(temp)


#attempt 2
li1=[10,23,20,30,45]
li2=[25,40,35]
s=set(li2)
temp3=[x for x in li1  if x  not in s]
print(temp3)


#attempt4
#use list comprehension and set to find difference between lists
li1=[1,2,3,4,5,6,7,8]
li2=[1,2,3,4,5,6]
s=set(li2)
temp3=[x for x in li1 if x not in s]
print(temp3)

#attempt5
#as always we wanna use def function to find the solution
def diff(li1,li2):
    li_diff=[ i for i in (li1  + li2) if i not in li1 or i not in li2]
    return li_diff

li1=[10,15,27,56,34]
li2=[27,10,34]
li3=diff(li1,li2)
print(li3)

# this methood  is actually ceative

















