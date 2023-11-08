#write a python program to find least frequent numbers

#breaking down the question we can say that min() can be used because its asking least requent numbers
#and there are constant checking factor too which is fit into loop  category
#so we are gonna use loop with count and min function  to  do it


#attempt 1                                                                                      #need to correct  it
test_str="geeksforgeeks "
print("the original strinng is :", test_str)
all_freq={}
for i in test_str:
    if i in all_freq:
        all_freq+=1
    else:
        all_freq=1
        
res=min( all_freq,key= all_freq.get)#we need to figure this out too close
print("the minimum of all charecters in the geekforgeeks is:")

# using collections.counter()+min()
#the most suggested method that coould be used to find all occurances in this method, this actually gets
# all element frequency and could also be used to print single element  frequency if required . we find
# minimum occuring charecter by using min() on values.

#least frequent charecter in string
#collections.Counter()+min()
from collections import Counter
test_str="geeksforgeeks"
print("the original string is:"+ test_str)
#using collections.Counter()+min() to get least frequent charecters
res=Counter(test_str)
res= min(res,key=res.get)
print("the minimum of all charecters in geeks for geeks is :"+str(res))
