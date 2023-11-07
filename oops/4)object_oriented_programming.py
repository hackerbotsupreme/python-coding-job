class item :
    def __init__(self,name,price, quantity=0):
        #print(f'an instance created :{name}')#we can call it --{}--- "refer to the "---in this case it is name of the assignes instance 
        self.name=name
        self.price=price
        self.quantity=quantity 
        
    def calculate_total_price(self): 
     return self.price*self.quantity
 
 

Item2=item('laptop',1000,3)#instance 



Item1=item('phone',100,5)#instance 

Item2._has_numpad=False
print(Item1.calculate_total_price())#500  output
print(Item2.calculate_total_price())#3000  output



#one more important side note here is that we can set default values to the parameter as --quantity--=0 so here 
#when we dont give any input and ask for the output then computer will return 0 as we  already set it to default .
#and if we assign any value then the previous input is gonna replace by new one also will return thst too when we ask.



#the second important sidenote is we can assign attributes to specific instances individually .so say that like  you want to know if the 
#laptop has the numpad or not because some laptop are not having the numpad on the keyboard , and at the same time that is not one ralistic attribute you
#assign to a phone and that is why you can go ahead and delette those print lines and sayy something like . --lliine 19

#and this is something you want to remen=mber that you want to remember , because the fact that you use  some attribute assignments in the constructor 
#that  doesnot mean that you cannot add some more attribute outside of the construvtor after you instantiatw the instances you like to add 


#now there is one problem pay attention that how we the calculate total price calculates  , it still uses x and y as the parameters . 
#and sthe question that arrives now is why it still should use those parameters ?
#now if we have completely understand that how the init works --as we know as each attribute we design in classes then the object itself is passed in
#as argument keep that in check so that is why we receive self so this means that now we could just return self dot price multiplied by sef dot quantity fo find the total price .
#and that means we no llonger have need for the x and y as we have assigned those attributes once the instance is graded. 



#in order to check thst it workd we are gonna hash the --line19---now and say print item1.calculate_total_price

#and as we can see it worked. 


#noow  w e have totally learned how to work with contructors and the best practices . 




  