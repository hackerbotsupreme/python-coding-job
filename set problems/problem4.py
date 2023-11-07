#write a program to remove items from the set 
#lets breakdown the question a  bit it says remove items from the set.,
#are we aloowed? yes, because we have set operators  , we can remove any of the items in one set
# from a ser from a target 


#now , first thing first  is there any in built function that can make job easier?
#tes , that is pop()method.
#concept
#how pop( ) works-- set to remove values from.pop()------ 
#quick revise
# the pop() can be used to pop out/remove the elements one by one from the set. when the pop is
# used the smallest in the set is removed first followed by  removing  removing elements in incresing order.

#attempt 1
def remove(initial_set):
    while initial_set:
        initial_set.pop()
        print(initial_set)
initial_set= set([12,13,14,6,8,9,])
print(remove(initial_set))
#result 

#{13, 14}
#{14}
#set()
#None

#umm , whatt is the none doing  here ?what does it mean ?
#need to find out-----