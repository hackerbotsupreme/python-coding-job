                                  #len() func in string 
print(len("aloke"))                                 
                                
                                #slicing with skip value   
#we can provide a skip value as a part of our slice like this :word[start-index::end-index:skip index]    
word="amazing"
print(word[2:5:])
quality="iamamazing"   
print(quality[1::])   
print(quality[0::2]) #immzn#2-1=1 skips every 1st indexed num from the 0th indexed num   
print (quality[0:7:2])#tip: it is like a trend(jump) on to another 

story="once upon a time there was a youtuber named harry who uploaded python course with notes" 
print(story[0:6])#result:once u # note that : here spaces are also printed that means spaces are also indexed 

                             
print (len(story))      #returns how many charecters are present in the container 

print(story.endswith("shfks")) # will return-- false-- bcz the story string is not ending with shfks
print(story.endswith("notes")) # wii return ---true--as our story string ends with notes
print(story.count("s")) # tells how many s are present in the string 
print(story.count("as"))#occurance of as 
print(story.capitalize())# o was in small case and after this o is in capital case so it #returns the string with first letter as a capital letter.
print(story.find("harry"))#44 so it # returns the index number of the first occurance of the  given string 
print(story.find("harri")) #-1 so -1 means that harri string is not present in the  string named story 
print(story.replace("harry","divya"))# replaces harry by divya 

               