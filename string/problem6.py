#write  a program to uppercase  half string /half letter of the string is uppercased 
#like input--'geekforgeek'
#output--geekFORGEEKS

#this question is useful to learn   catitalize  the string 
#string.capitalize()---this function capitalizes the first chaterfirst charecter of a given string
#and also the upper function --- upper() ---this function uppercases the charecters.


#attempt 1
#using upper()+loop +len()
test_str="geeksforgeeks"
print("the original string is",test_str)
hlf_idx=len(test_str)/2
res=''
for idx in range (len(test_str)):
    if idx>=hlf_idx:
        res += test_str[idx].upper()
    else:
        res += test_str[idx]
print("the resultant string ", str(res))

#attempt 2
# using list comprehendion()+ join()+upper()
test_str="geeksforgeeks"
print("the original string is", str(test_str))
hlf_idx=len(test_str)/2
res=''
res=' '.join([test_str[idx].upper() if idx>= hlf_idx else test_str[idx] for idx in range (len(test_str))])
print("the resultant string ", str(res))


#attempt 3
# using slice() to cut string in half and the .upper() to uppercase the other half string
test_str="geeksforgeeks"
print("the original string is", str(test_str))
hlf_idx=len(test_str)/2
res=''
res=test_str[hlf_idx:] +test_str[hlf_idx:].upper()
print("the resultant string "+str(res))


