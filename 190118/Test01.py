#팩토리얼 만들기

num = int(input("정수를 입력해주세요: "))
mul = 1
for i in range(1,(num+1),1):
    mul = mul*i
print(num,"!은", mul,"이다.")
