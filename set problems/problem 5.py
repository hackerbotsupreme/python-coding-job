#check if the two sets are smae element in common
#first thing first is ther any in built function  that can make our livces easy
#well yes first we can do this with set intersection secondly  loops
#attempt 1-- using loops
#we can do it traverse  the lis t
def common_data(list1,list2):
    result =False
    for  x in list1:
     for y in list2:
            if x==y:
                result =True
                return result
            else :
                pass
a=[1,2,3,4,5,6]
c=[2,3,5,6,7,8]
b=[8,6,5,4,3,2,1]
print(common_data(a,b))
print(common_data(a,c))
#attempt 2 -- using  set intersecton
def common_number(a,b):
    a_set=set(a)
    b_set=set(b)
    if len(a_set.intersection(b_set))>0:
        return True
    else:
        return False

b=[8,6,5,4,3,2,1]
a=[1,2,3,4,5,6]
print(common_data(a,b))

#quick revise
#set intersection syntax-- set.intersection(set)-- two sets we want to compare


#attempt 3
#we looked atanother method lets look at it if we find something useful and unique
def common_number(a,b):
    a_set=set(a)
    b_set=set(b)
    if(a_set&b_set):
        return True
    else:
        return False
a=[1,2,3,4,5,6]
b=[6,5,4,3,2,1,8]
print(common_number(a,b))

# sothis  we are making lists sets and using &  to find  intersection and printing 
# trye or fallse based on intersection happened or not 


     













                 