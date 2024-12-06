
x=int(input("enter the 1st number:"))
y=int(input("enter the 2nd number:"))
a=int(input("enter the operation:"))
if a==1:
        sum=x+y
        print(sum)
elif a==2:
         sub=x-y
         print(sub)
elif a==3:
         mul=x*y
         print(mul)
elif a==4:
     if y==0 or x==0:
            print('div is not possible')
     else:
            div=x/y
            print(div)
else:
     exit()           
    
    