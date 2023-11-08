# write a program to find out whether a student is passed or failed if 
# it requires total 40% and at least 33% in each subto pass assume 3 subjects and take marks as an  the user
bengali= int(input("enter the bengali:"))
english= int(input("enter the english:"))
maths= int(input("enter the maths:"))
#as their is two conditions  that is total 40% and at least 33%
if( bengali<33 or english<33 or maths<33):
    print("you are failed")
if(( bengali+english+maths)/3 < 40):
    print("you  are failed due to total percentage is less than 40")
else:
    print("you are passed ")



