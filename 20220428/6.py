import numpy as np
a=17
a_prime=True
for i in range(2,a):
    if a%1==0:
        a_prime=False
if a_prime==True:
    print("%d는 소수이다."%a)
else:
    print("%d는 소수가 아니다."%a)