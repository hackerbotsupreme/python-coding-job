#create a class with a  class attribute a ; 
# create an object from it and set a directly using object. 
# a=0.does this changes the class attribute
class Sample:
    a="harry"

    
object=Sample()
object.a="Vikky"
#Sample.a = "Vikky"

print(Sample.a)
print(object.a)