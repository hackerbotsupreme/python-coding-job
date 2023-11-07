class item :
    # dynamically assigning attributes 
    def __init__(self,name,price,quantity=0):
       self.name=name
       self.price=price
       self.quantity=quantity
       
       
    def calculate_total_price(self,x,y): 
     return x*y
item2=item('laptop',1000,4)
item1=item('ipad',5000)
print(item1.name)
print(item2.name)
print(item1.price)
print(item1.quantity)
#PS C:\Users\rekha\OneDrive\Desktop\oops> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/rekha/OneDrive/Desktop/oops/ite.py
#ipad
#laptop
#5000
#10

# 