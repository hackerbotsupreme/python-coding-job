#count occurances in python
#lets understand the question 
#count means how many times and occurances means present so 
#all in all the question becomes write a program that how many times a 
# given item is present in the list
l=[1,2,3,4,5,6,7,1,2,3,4,3,1,2,3,1,7]

#attempt 1                                                                        #works
#first i will think abvout is there any in-built fuction in the
# list that can make our lise easy 
#well yes that is----l.count(item)
l=[1,2,3,4,5,6,7,1,2,3,4,3,1,2,3,1,7]
c=l.count(1) 
print(c)

 
#attempt 2
#second method is  using for loop and traversing concept
l=[1,2,3,4,5,6,7,1,2,3,4,3,1,2,3,1,7]
n=int(input('enter the number:'))
count=0
for i in  l:
    if(i==n):
        count +=1
    else:
        pass
    
print("the count of n is",count)
#attempt 3
# third is using def function(its always comes handy) like to find when ever it finds the item add i to the countdown 
def count(list,x):
    count=0
    for  i in list :
        if(i==x):
            count+=1
    return count
list=[1,2,3,4,5,6,7,1,2,3,4,3,1,2,3,1,7]
o=count(list,2)
print('the  occurance of x is',o)      
     
#another way can be quite similar
def count(list,x):
    return list.count(x)
v=count(list,4)
print('the occurance of x is ', v)      


#oh, i just missed one more thing 
#that is we dont need to separately write ,store then print when we can itegrate that step 
#with the print statement
#here we go
print('{} has occoured {} times'.format(2,count(list,2)))

# its cool