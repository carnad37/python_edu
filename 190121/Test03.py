num = 0
sum = 0
count = 0

def banNum(number):
    numberCout = int(number)
    number = number*10
    number = int(number)
    #1.5가 15가됨.
    number =

while True:
    num = int(input("정수를 입력해주세요: "))
    sum = sum+num
    count+= 1
    # 종료코드
    if(num>=100):
        break

#평균구하기
avg = sum/count
avg = avg*10
avg = int(avg)
avg = avg/10
print(sum)
print(avg)
