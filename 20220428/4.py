a=[1,2,3]
b=[2,3,4,5,6]
c=[]
for i in a:
    if i not in b:
        c.append(i)
print(c)

### remove
A=[1,2,3]
B=[2,3,4,5,6]
C=A+[]
for j in B:
    if j in A:
        C.remove(j)
print(C)