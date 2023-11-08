#check if the given number is present in the list=[1,2,3,4,5,6,7]
#attempt 1
a=int(input('enter your number :'))
list=[1,2,3,4,5,6,7]
#for a in list:
if a in list:
    print('the a is present in the list')
else:
    print('the a is not present in the list')
#it is giving syntax error -- i need to find out why


#attempt 2 :
list=[1,2,3,4,5,6,7,8,9]
b=7
for i in list:
    if(i==7):
        print('b is present in the  list')
    else:
        print('b is not ppresent in the list')
#b is not ppresent in the list
#b is not ppresent in the list
#b is not ppresent in the list
#b is not ppresent in the list
#b is not ppresent in the list
#b is not ppresent in the list
#b is present in the  list
#b is not ppresent in the list
#b is not ppresent in the list
#look at the result it is bcz for every num it is printing, gpotta fix it



#attempt 3
list=[1,2,3,4,5,6,7,8]
if (7 in list):#extraordinary approach#iets study the syntax of if statement again:
    print('7 is present')#if(condition) then print this else do this
else:
    pass

    
