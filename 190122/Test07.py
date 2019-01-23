#1~100사이의 수 입력.
#100보다 작은 배수 출력
mul = 0
num = int(input("정수를 입력해주세요: "))
for i in range (1,11,1):
    mul = i*num
    if(mul>100):
        break
    print(mul,end=" ")
