##python program to multiply all the numbers in the list 
#lets understand the concept of the question deeply question says multiplication of the items in the list
#that means product



# attempt 1:first we want to know that is there any built in function that can make our job easy
#well yes there is multiple of them numpy.prod(),lambda,math.prod,mul() operator 
list=[1,2,3,4,5,6,7,8]
m=1
for i in list:
    M=i*m
print(M)





# attempt 2:first we want to know that is there any in built fuctions that rae\
# available to makr our job easy ,there is no straight forward function but 
#we can use loops ,with mitiplication to solve it.
def multiplylist(mylist):
    result=1
    for i in mylist:
        result=result*i
    return result
list =[1,2,3,4,5,6,78,9]# error: statements must be seperated by new lines or semicolons 
list=multiplylist(list )#"(" is not closed -- what does it mean ---i think that means the internal variable is is not valid
print(list)
#505440
#it works 







#attempt 3:using traversal by iindex
def multiplylist(mylist):
    result=1
    for i in range(0,len(mylist)):#note the statement structure from for to return very closely
        result=result*mylist[i] #because becase if the variable return is not placed correclt in the structure then the result  
    return result#will be wrong
list1=[1,2,3,4,5,6,78,9]
print(multiplylist(list1))


