price_list = [32100,32150,32000,32500]
for number in range(1,len(price_list)):
    print(((number-1)*10)+100, end=' ')
    print(price_list[number])
    