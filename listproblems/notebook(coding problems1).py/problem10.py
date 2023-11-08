#python prograam to find avg and sum of numbers 

#attempt 1
#first thing first 
#is there any inbuit function that can make our lives easy
#yes that is using for with count and len function  or using sum function itself
l=[1,2,3,4,5,6,7,8] 
count=0
for i in l:
    count+=i
avg=count/len(l)
print("sum is",count)
print("avg",avg)

#attempt 2 
#using def(as we kow it comes handyt in every case)
#sum,avg
# hare we need to notice some points, that def fuction reurns one value 
#and whatever we need to have to define while 
# inside of def other wise it can end up being a mess


#attempt 3
#using  sum() function
#sum(list) ---- the list we need to find sum of 
l=[1,2,3,4,5,6,7,8] 
sum=sum(l)
avg=sum/len(l)
print("sum is",sum)
print("avg",avg)




