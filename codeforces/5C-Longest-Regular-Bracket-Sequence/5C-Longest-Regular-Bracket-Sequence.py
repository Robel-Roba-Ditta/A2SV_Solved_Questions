s= input().strip()
n=len(s)
p=[0]*n
l=0
for i in range(n):
    if s[i]==')' and i>0:
        j=i-p[i-1]-1
        if j>=0 and s[j]=='(':
            p[i]=p[i-1]+2+(p[j-1] if j>0 else 0)
            if p[i]>l:
                l=p[i]
if l==0:
    print(0,1)
else:
    count=0
    for x in p:
        if x==l:
            count+=1
    print(l,count)