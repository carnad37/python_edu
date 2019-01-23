#0이 입력될때까지, 3과 5의 배수를 제외한 수들의 갯수

num = 0
count = 0

while True:
    num = int(input("정수를 입력해주세요: "))
    #종료코드
    if(num==0):
        break
    #3과 5의 배수를 카운트
    if((num%3!=0)&(num%5!=0)):
        count += 1
print(count)