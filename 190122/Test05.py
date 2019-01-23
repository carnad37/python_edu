#자연수를 입력받아 10의 배수까지 배수출력
res = 0
num = int(input("정수를 입력해주세요: "))
for i in range(1,11,1):
    res = num*i
    print(res,end=" ")
