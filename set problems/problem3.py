#maximum and minimum in a set

#first thing first is ther any in built function that can make it happen for me 
#well yes there is that is max and min 

#attempt 1 
s={1,2,3,45,6,78,9}
print(max(s))
print(min(s))


#attempt 2 
#we will pair the max nd min functions with the def  function so we dont have write the 
# same code over and over again and just call the function andwe will got what we need 
def MAX( seats):
    return max(seats)
seats={1,3,4,56,67,34,23,23,45} 
print(MAX(seats))


def  details_of(seats):
     miaximum_of_seats  =max(seats)
     minimum_of_seats = min(seats)
     return print(miaximum_of_seats,minimum_of_seats)
seats={1,3,4,56,67,34,23,23,45} 
print(details_of(seats))



















