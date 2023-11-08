#write a program to generate multiplication tables from 2 to 20 and write the different files ,  place these files in a folder for a 13 year old.
for i in range (2,21):
    with open(f"tables/Multiplication_table_of_{i}","w")as f:
        for j in range (1,11):
           f.write(f"{i}X{j}={i*j}")
    break    
#the result are printed in the multiplication_table_of_2 ---file        