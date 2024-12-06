a=float(input("enter a number:"))
b=float(input("enter a number:"))
def add():
    sum=a+b
    print("sum=",sum)
 def subtraction():
    diff=a-b
    print("diff=",diff)
def product():
    product=a*b
    print("product=",product)
 def division():
    div=a/b
    print("div=",div)
for i in range(5):
    print("the operation arae 1.addition\n2.subtraction\n3.multiplication\n4.division\n5.exit")
    operation=int(input("enter the number:"))


