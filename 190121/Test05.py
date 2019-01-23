#0~100까지 넘어가면 종료.
#합계와 평균 출력
num = 0
sum = 0
count = 0
while True:
    num = int(input("정수를 입력해주세요: "))
    #종료코드
    if((num<0) | (num>100)):
        break
    sum = sum+num
    count+= 1

#평균구하기
avg = sum/count
avg = avg*10
avg = int(avg)
avg = avg/10
print("sum :",sum)
print("avg :",avg)