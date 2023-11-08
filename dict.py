mydict={
    "dabba":"box",#dont forget this comma--,--at ech end of the key,value pair if ignored can cause errors 
    "pankha":"fan",
    "talent":"aloke",#we  can add dictionary and list inside of dictionary
    "win":[1,2,3],#list inside of dictionary
    "anotherdict":{"aloke":"hacker"}#dictionary inside of dictionary 
}
print(mydict)

#printing a value of a key in dictionary 
print(mydict["dabba"])
print(mydict["pankha"])
print(mydict["anotherdict"]["aloke"])#printing/accessing  a value inin the dictionary which is on the dictionary
                                    #which is also known as  nested dictionary
#properties of a python dictionaries 
#1. it is unordered #the difference between ordered and indexed is ordered means this item is after this item where 
#2. it is indexed# indexed means this item will hold this position 
#3. it is not changable 
#4. dictionay cannot contain duplicate keys 


#printing the keys as a list
print(list(mydict.keys()))  # ['dabba', 'pankha', 'talent', 'win', 'anotherdict']   , similarly you can print lists of the alues too 
print(list(mydict.values())) # ['box', 'fan', 'aloke', [1, 2, 3], {'aloke': 'hacker'}]


#updating the list 
updatedict={
    "shiva":"aloke"
}
mydict.update(updatedict)#updates mydict from updatedict
print(mydict)                         

#what is the difference between mydict.get["key"] and mydict["key"]     
#ok we can look at iit as .get means i am asking program that if he has the value for corresponding key but  
#where in mydict["key"] means i am commanding program to give me the value for corresponding value-- so
print(mydict.get("dabba"))#box
print(mydict["dabba"])#box

print(mydict.get("dsj"))# so as we explained above and returning ---none---- while
print(mydict["dsj"])#this gives error in programming we should always try to avoid errors 
                              
