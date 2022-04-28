u = [1,2,3,4,5]
a=[1,2,3]
a_com=[]
for i in u:
    if i not in a:
        a_com.append(i)
print(a_com)

u = [1,2,3,4,5]
a=[1,2,3]
rest=u+[]
for i in u:
    if i in a:
        rest.remove(i)
print(rest)
