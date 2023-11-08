#write a program to accept the strings ehich contains all vowels

#it is an interesting problem 

#her what we can do is to make a set  of vowels and traverse the i through set of vowels and string
#which could be done using loops 

#attempt 1
def vowel_count(str):
    count=0
    vowel=set("aeiouAEIOU")
    for i in str:
        if i in vowel:
            count=count+1
            print("no. of vowels:", count)
        else:
            pass
str="geeks for geeks "
print(vowel_count(str))
#we gotta loook after it later
