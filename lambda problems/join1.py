str=['a','b','c']
alphabets="/".join(str)
print(alphabets)

#output
#problems/join1.py"
#a/b/c
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> 


number=[1,2,3,4,6,6,7,7]
numbers='  '.join(number)
print(numbers)
#Traceback (most recent call last):
#  File "c:\Users\rekha\OneDrive\Desktop\lambda problems\join1.py", line 12, in <module>
#    numbers='  '.join(number)
#TypeError: sequence item 0: expected str instance, int found
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> 


#so thts mean join operator only adds string as we seen

number=['a','s','f','d','u','i']
numbers='  '.join(number)
print(numbers)





number=['a','s','f','d','u','i']
numbers=' '.join(reversed(number))#reverse(number)--reverses the sequence of number
print(numbers)




myname='alokepramanik'
mynames=''.join(reversed(myname))#reverse(number)--reverses the sequence of number
print(mynames)

#output
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> & C:/Users/rekha/AppData/Local/Microsoft/WindowsApps/python3.10.exe "c:/Users/rekha/OneDrive/Desktop/lambda problems/join1.py"
#a/b/c
#a  s  f  d  u  i
#i u d f s a
#kinamarpekola
#PS C:\Users\rekha\OneDrive\Desktop\lambda problems> 
