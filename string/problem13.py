#split and join the string
#its  very intuitive , split it using .split() and join using 

#attempt 1
def split_string (string):
    list_string=string.split(' ')
    return list_string
def join_string(list_string):
    string='-'.join(list_string)
    return string
if __name__=="__main__":
 string='geeksforgeeks'
list_string=split_string(string)
print(list_string)
new_string=join_string(list_string)
print(new_string)

#attempt 2
#the most easy way is 
s='geeksforgeeks'
print(s.split(" "))
print("_".join(s.split()))


