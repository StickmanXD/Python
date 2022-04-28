import numpy as np
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)


d=[1,2,3]
e=[2,3,4,5,6]
k=[]
for i in d:
    if i not in e:
        k.append(i)
print(k)
k=k+e
print(k)


A=['apple','melon','orange']
B=['chicken', 'pig', 'cow']
C=[]
C=A+B
print(C)