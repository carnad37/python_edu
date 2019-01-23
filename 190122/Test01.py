#10이하의 과목수를 입력받음.
#과목 수만큼 점수를 입력받음
#평균을 구하고, 80점 이상 pass, 이하 fail출력
score=0
sum = 0
res = ""
num = int(input("과목 수를 입력해주세요: "))
#과목 수만큼 반복해서 점수를 입력받음
for i in range(1,num+1,1):
    score = int(input("%d번째 과목을 입력해주세요: "%i))
    sum = sum+score
#평균 구하기
avg = sum/i
if avg>=80:
    res = "pass"
else:
    res = "fail"
print("평균 점수 :",avg)
print("결과 : "+res)