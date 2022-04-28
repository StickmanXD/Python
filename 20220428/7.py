a=24
b=range(1,a)
factors=[]
for i in b:
    if a%i==0:
        factors.append(i)
factors.append(a)
print(factors)