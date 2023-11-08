# a spam comment is defiined as a text  containing follwing keywords.
#"make a lot of money","buy now", sbscribe this", "click this".
#so check that if the user entered word is spam or not 
text=input("enter the text :")
#setting false as default
if("make a lot of money"in text ):
    spam=True
elif("buy now"in text ):
    spam=True
elif("subscribe this"in text ):
    spam=True
elif("click this"in text ):
    spam=True
else:
    spam=False
    
if(spam):
    print("the text is a spam")
else:
    print("the text is not spam")