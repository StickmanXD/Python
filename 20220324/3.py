
from tokenize import String

print("url = ",end='')
url=input()
index_url=len(url)
while index_url>0 :
    index_url = index_url-1
    print(index_url, end=' ')
if (url.rfind('kr') > 0):
    domain = url.rindex('kr')
    print("\n"+url[domain:(len(url))])
else:
    print("\nkr 도메인을 찾지 못했습니다.")
