#정수 20개 입력.
#0이 입력되면 종료.
#그때까지의 합과 평균 출력
count = 0
sum = 0

while count<20:
    count+=1
    num = int(input("%d번째 정수를 입력해주세요: " % count))
    #종료코드
    if(num == 0):
        break
    sum += num
avg = sum/(count-1)
print("Sum :",sum)
print("Avg :",avg)
