#python program to print negative numbers in the list 

# first thing first that is there is any function that can make my life easy
#well yes  that is using  loops  to iterate the lists  and pair it with the 
#codition and take your win
#attempt 1 
list=[1,2,3,4,5,6,7,-2,-3,-4,-5] 
for num in list:#iterate using  for loops
    if num<0 #or here we can write num!=0
    print(num,end=" ")

#attempt 2
#using while loops 
#while(codition):-- do this
#quick revise in while loops we have to be careful about the conditions and 
# as for the while loop it should be limiting becuse if the loop dont meet false then it will continue itself to the infinity
list=[1,2,3,4,5,6,7,-2,-3,-4,-5] 
while (num< len(list)):
    if list[num]<0:
        print(list[num], end=" ")
        num+=1#limiting factor for while loops 
        
#using list comprehrnsion 
list=[1,2,3,4,5,6,7,-2,-3,-4,-5]       
neg_num=[num for num in list if num< 0]
print("negative numbers in the list :", *neg_num)

#using startswith()
list1=[1,2,3,4,5,6,7,-2,-3,-4,-5]   
res=[]
list2=list(map(str, list1))#need to know that how this syntax works
for i in range (0, len(list2)):
   if (list[i].startswith("-")):
       res.append(str(list1[i]))
res=" ".join(res)
print(res)



    