a=int(input("enter the operation:"))
if a==5:
    print('exit')
else:
    x=int(input("enter the 1st number:"))
    y=int(input("enter the 2nd number:"))
    if a==1:
        i=x+y
        print(i)
    elif a==2:
        i=x-y
        print(i)
    elif a==3:
        i=x*y
        print(i)
    elif a==4:
        if x==0 or y==0:
           print('operation cannot be performed')
        else:
            i=x/y
            print(i)
    
       



    