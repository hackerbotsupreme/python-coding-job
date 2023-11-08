#write a program to remove i th charecter from  string in pyrhon 



#attempt 1 
test_str="geeks for geeks "
new_str=" "
for i in range (len(test_str)):
    if i==2:
        pass
    else:
        new_str=new_str+test_str[i]
print("the string afterremoval if ith cahrecter is ",new_str)
#result--geks for geeks
#the alternative can be
test_str="geeks for geeks "
new_str=" "
for i in range (len(test_str)):
    if  i!=2:
        pass#new_str=new_str+test_str[i]
    else:
         new_str=new_str+test_str[i]
print("the string afterremoval if ith cahrecter is ",new_str)
#e

#joining methods
#slice and concatenate
#quick revise: starting with concatenate  this just contains two this you can only  add lists with lists
# and strings with strings  with end to end and we can do it with + operator and slicing means we are gonna 
# slice the given string and add it to the string i want to make and note her the [endindex]  does not gets printed 
test_str="geeks for geeks "
new_str=[]
new_str=test_str[:2]+test_str[3:]#note position 2 will not printed and at the same time we dont to the same element to be repeated into new str thats why did it like it
print()

#joining methods
#.join() and list comprehension 
test_str="geeks for geeks"#seperater/joiner . join(list/string)
new_str=" ".join([test_str[i] for i in range(len(test_str))if i!=0])
print("the string after removal of ith charecter:",new_str)




