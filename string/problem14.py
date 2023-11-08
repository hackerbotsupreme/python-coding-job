#check if given string is  binary or not


#sowhats we goona do here is we gonna take a string from the user and check if the se t if it oonly consists of 1 and/or 0 only.
def  check(string):
    p=set(string)
    s={0,1}
    if s==p or p=={'0'} or p== {'1'}:                                #need to figure out
        return("yes")
    else:
        return("no")
if __name__=="__main__":
 string='010101010'
check(string)




#attempt 2
def check2(string):
    t='01'
    count=0
    for char in string:
        if char not in t:
            count=1
            break
        else:
            pass
    if count:
        print("no")
    else:
        print("yes")
if __name__=="__main__":
    string='01101001010'
    check2(string)

    
#attempt 3 #most satisfying one  
string='101000101000'
if (string.count('0')+string.count('1')==len(string)):
    print("yes")
else:
    print("no")