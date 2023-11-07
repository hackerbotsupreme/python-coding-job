t=int(input())
for i in range(t):
    w,x,y,z=map(int,input().split(","))
    if (x==(w+y*z)):
        print('the bucket is filled ')
    elif(x>=(w+y*z)):
        print('the bucket is not filled')   
    else:
        print('overflow')
        
