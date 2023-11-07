#python program to find pairs of complete strings  in two sets


#Consider all pairs of strings, concatenate them one by one and converts it into set.
#Now one by one add all alphabets in concatenated string into set. Since set contains unique values so if length of set is equal to 26 that means set contains all 26 english alphabets.


# Function to find pairs of complete strings
# in two sets of strings
  
def completePair(set1,set2):
      
    # consider all pairs of string from
    # set1 and set2
    count = 0
    for str1 in set1:
        for str2 in set2:
            result = str1 + str2
  
            # push all alphabets of concatenated 
            # string into temporary set
            tmpSet = set([ch for ch in result if (ord(ch)>=ord('a') and ord(ch)<=ord('z'))])
            if len(tmpSet)==26:
                count = count + 1
    print (count)
  
# Driver program
if __name__ == "__main__":
    set1 = ['abcdefgh', 'geeksforgeeks','lmnopqrst', 'abc']
    set2 = ['ijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz','defghijklmnopqrstuvwxyz']
    completePair(set1,set2)