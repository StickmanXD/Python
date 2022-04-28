import numpy as np

a=[1,2,3]
b=[4,5,6]
c=[1,2,3,1,2]
d=[3,3,4,5,6,6,6,7,8,8,9]

new_c=[]
for i in c:
    if i not in new_c:
        new_c.append(i)
print(new_c)
new_d=[]
for i in d:
    if i not in new_d:
        new_d.append(i)
print(new_d)
