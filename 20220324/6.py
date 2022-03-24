score=int(input("성적을 입력하세요 : "))
if 100 >= score and score >= 81: 
    print("A 학점 입니다.")
elif 80 >= score and score >= 61:
    print("B 학점 입니다.")
elif 60 >= score and score >= 41:
    print("C 학점 입니다.")
elif 40 >= score and score >= 21:
    print("D 학점 입니다.")
elif 20 >= score and score >= 0:
    print("E 학점 입니다.")
else:
    print("성적을 제대로 입력하세요.")
    