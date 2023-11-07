#iterate over a set in python 
#lets broke down hthe question a little bit what does the iteration/iterating  means 
#here's what we gonna do we are gonna write a set of code with an intend and iteate over the set.
#here we have said an itent so tell me what are the things are allowed to do with set.
#like we can access the items,


#iteration inthe programming  is a process  wherein a set of instructions or structures are repeated
# in a sequence a specified number of times untill a specific condition is met.when the first set of instructions 
# executed again it iss called iteration. when a set of instructoin in a repeated manner  it is called a loop.
# to be specific i want to know what is the difference between loop and iteration. a loop is defined as a segment
# of code that exexcutes multiple times in a repeated manner. 
#where  iteration means the processs inwhich the code segment id executed once. 

#so does iteration means looop? 
#you can say each single execution of code is called iteration and  the repeated iteration is called a loop. 
#anothe difference is looops are single line commands that can executed repetedly but the iteration are multi line
# command that intended for a single condition .


##quick revise 
#how many types of loops are there . ther are two types of loops . that is for and while.
# and dont confuse loops with if ,remember nigga if is a statemeny. 
#attempt 1 
test_str= set("geeks")
com=list(val for val in test_str)#iterating using list comprehension 
print(*com)#what does this * operator do look below
#result-k s g e

#for seqences such as  string ,list,and tuple  *  is a repition operator .
# take the below example
s="hello"
print(s*3)
#hellohellohello it ca be used like this .
L1=[1,2,3,4]
print(L1*3)
#[1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
T1=(1,2,3,4,5)
print(T1*3)
#(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
def fuction(*arg):
    print(type(arg))
    for i in arg:
        print(i)
        
        
        
#attempt 2:
test_set=set("geeks")
for val in test_set:#iterating using for loop 
    print(val)
#e
#s
#k
#g

#attempt 3 
#iterating over a set using enumerated for loop.
test_set=set("geeks")  
for id , val in enumerate(test_set):
    print(id, val)
    
# 0 e
#1 s
#2 k
#3 g

#attempt 4
#iterating over a set as indexed list

test_set =set("geeks")
test_list=list(test_set)#iterating over a set as a indexed
for id in range (len(test_list)):
    print(test_list[id])
    KeyboardInterrupt
 
#g
# l
# o
# b
# a
# l
# s
