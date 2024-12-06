weight=int(input("entr the weight:"))
height=float(input("enter the weight:"))
def calculated_bmi(weight,height):
    bmi=weight/(height**2)
    return(bmi)
result=calculated_bmi(weight,height)
print(result)    
############################################################################################
s={1,2,3,4,5,6}
s.discard(5)
print(s)
###########################
t=(1,2,3,4,5)
for i in t:
    t=i*2
print(t)    
