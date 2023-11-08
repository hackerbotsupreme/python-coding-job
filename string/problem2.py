#write a program to reverse words given string.



#concept
#here we gonna learn  about split function for the string
#string.split()---Python String split () Method

#Definition and Usage The split () method splits a string into a list. You can specify the separator,
# default separator is any whitespace. Note: When maxsplit is specified, the list will contain 
# the specified number of elements plus one.
#str.split(seperator,maxsplit)


string="geek quiz practice code"
s=string.split()#['geek', 'quiz', 'practice', 'code']# as we said it takes elements and convert it into strings and makes a list
s=string.split()[::-1]#['code', 'practice', 'quiz', 'geek']# as we said it takes elements and convert it into strings and makes a list
l=[]
for i in s:
    l.append(i)
    print("".join(l))


#attempt 2
#what does __name__=="__main__" this function does 
#basically when we need to import functions from the another file then with the functions the extra this comes
# too so wwhen we need to use import but we dont want to use them in our current function we use this function
# to tell computer to inly execte this this string and that is also the reason wht main is here it indicates this is the script to execute
def rev_sentence(sentence):
    words=sentence.split(' ')
    reverse_sentence=' '.join(reversed(words))
    return reverse_sentence
if __name__=="__main__":
 input="geeks quiz practice code"#expected indented block 
print(rev_sentence(input))

#attempt 3 
#in this wwe are gonna learn about the join function for sstring
#concet; join() is an inbuilt string function in python used to join elements of the sequence seperated by 
# a string seperator . this function jooins  elements of a sequence and makes it a string.
#string_name.join(iterable)
#as this method is critical i am going to present some of the examples containig join func
#seperator.join(jei list are element der join korte hobe)----so
#seperator.join(list name)
list=['g','e','e','k','s']#joining with empty seperator
print(" ".join(list))
list1='geeks'
print('$'.join(list1))
#g e e k s
#g$e$e$k$s


list=('1','2','3','4','6')
#putting the seperator 
s='-'
#joins elements of list by '-'
s=s.join(list)
print(s)
1-2-3-4-6



