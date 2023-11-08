#find odd frequency charecters in string
# it smells like count() method, counter( ) method


#attempt 1
#try with count()method
# i think its simple make the given string a set then pair a loop and count() with it

test_str="geeks for geeks "
x=set(test_str)
res=[]
for i in x:
    if test_str.count(i)%2!=0:
        res.append(i)
print("the odd frequency charecters are:",res)


#attempt 2
#try eith list comprehension()+.counter()
#look closely
from collections import Counter
test_str='geeksforgeeks is best for geeks '
print("the original string is :", test_str)
res=[ chr for chr ,count in counter(test_str).items() if count & 1]
print("the odd frequency charecters are :",str(res))



                                 