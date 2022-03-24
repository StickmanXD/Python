from re import search


warn_investment_list=["Microsoft","Google","Naver","Kakao","Samsung","LG"]

print("투자할 종목을 입력하세요 : ",end='')
investment=input()

if investment in warn_investment_list : 
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")