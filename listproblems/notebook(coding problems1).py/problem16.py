#write program to print odd numbers 


#same as problem 15
#first thing is first is there anny in built functions that can make our job easy
#yes that is using and coditions , loops -- while loops
#attempt 1 
#using loops 
#the concept behind loops is we will iterate through each element 
# and check if num%2==o or not
list=[2,3,4,5,6,7,6,0,10]
for i in list:#iterating each element
    if i%2==0:
        pass
    else:
        print(i,end=" ")
#2 4 6 6 0 10 # its done

#attempt 2
#using while loop # while syntax --- while(codition)--do this 
# dont confuse while with if 
#if is a statement that mens it checks if the expression is true or false and runs the 
#code inside only if it is true.
#and while is a lop basically, it continues to execute  the code  in the while 
# statement for however long the expression is true  
#while (i%2==0):# and the reason above is exactly why the loop is is infinite as it is always true
## ok but we can use loop in  diifferent sense and this time the codition should be like something 
#that ends like
list= [2,3,4,5,6,7,6,0,10]
num=0
while(num<len(list)):
    if  list[num]%2==0:
        pass
    else:
        print(list[num],end=" ")
    num+=1
    
    
#attempt 4
#using  a new method:list comparison
list= [2,3,4,5,6,7,6,0,10]
odd_number=[i for i in list if i%2!=0]# error:when "[" is not closed this can mean whatever is in bracket is not in valid syntax 
print("even numbers in the list is",odd_number)
#fucking did it 


#whenever there is math concepts involved and there is a trend we shuld think 
#about can recusion help me to solve this 
#so how recursion works? recursion  is a  mathemetical formula that calls itself 
# and repeat itself untill the resulit is met  
#but how can we use it to find and print even number
#well for this case it doesnot works but keep looking at it bcz breakthrough can come in any form 



#attempt 3
#using def function 
# we are gonna learn  a new way to use in def
#we can set base value in def
def evennumbers(list,n=0):#base case
    if n==len(list) :
        exit()
    if list[n]%2!=0:
        print(list[n],end=" ")
 
 
evennumbers(list,n+1)#here is showing that  evennumbers(list,n+1)
                      #NameError: name 'n' is not defined
list= [2,3,4,5,6,7,6,0,10]#as i told you earlier that if we dont define a variable while it is under 
print("even numbers ",end=" ") #def then it will give error and exactly that is what is also happening here
#need to find out why it is like this  
        

#attempt 4
list=[2,3,4,5,6,7,6,0,10]
for i in list:
    if i%2==0:
        print(i,end=" ")
    else:
        pass