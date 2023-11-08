#write a function  to remove a given word from a list and strip it at the same time 
# what is strip? strip is  to remove the extra space from the edge of strings.
#how to do that 
def remove_and_strip(word,string):
    newstring=string.replace(word," ")
    return newstring.strip()
this="    aloke          is      excellent       hacker      "

print(remove_and_strip("excellent",this))   





