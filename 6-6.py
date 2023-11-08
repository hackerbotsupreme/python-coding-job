#write a program to calculate grade of student based on is marks from th following scheme
#90-100-ex, 80-90-A, 70-80- b, 60-70-c,50-60-d,40-50-fail
marks=int(input("enter your marks:"))
if marks >=90:
    grade="Ex"
elif marks >=80:
    grade="A"
elif marks>=70:
    grade="B"
elif marks>=60:
    grade="C"
elif marks>=50:
    grade="D"
else :
    grade="F"

print("your grade is ",grade)

