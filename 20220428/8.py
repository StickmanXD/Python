a=24
aa=range(1,a)
a_factors=[]
for i in aa:
    if a%i==0:
        a_factors.append(i)
a_factors.append(a)
print(a_factors)

b=36
bb=range(1,b)
b_factors=[]
for i in bb:
    if b%i==0:
        b_factors.append(i)
b_factors.append(b)
print(b_factors)

common = []
for i in a_factors:
    if i in b_factors:
        common.append(i)
common.sort()
print(common[-1])


M=a*b
GCD = common[-1]
LCM = M/GCD
print("%d 와 %d 의 최소공배수는 %d 이다."%(a,b,LCM))