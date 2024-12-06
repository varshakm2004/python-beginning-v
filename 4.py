a='hello world from python'
print(a[::-1])
new=" "
for i in a:
    if i not in new:
        new +=i
print(new)  
new={}
for i in a:
    if i.isalpha():
        new[i]=new.get(i,0)+1
print(new)    