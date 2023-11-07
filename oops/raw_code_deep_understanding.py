class Item:
    def total_quantity_price(self,x,y):
        pass
item=Item()
item.name='phone'
item.quantity=5
print(item.total_quantity_price())
#  File "c:\Users\rekha\OneDrive\Desktop\oops\raw_code_deep_understanding.py", line 7, in <module>
#    print(item.total_quantity_price())
#TypeError: Item.total_quantity_price() takes 0 positional arguments but 1 was give
# look why the error ? 
# it is because when we calls a method from the instance of an on=bject then object itself  passes first as the given argument .
# but there is no given argument which is self so that's why it's giving us error . 
# and in simple words what this line
# Item.total_quantity_price() takes 0 positional arguments but 1 was give
# means is python tries to pass one argument but none/0 arguments are given 
