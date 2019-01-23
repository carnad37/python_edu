#n을 입력받아 별5줄 출력
star="*"
line=""
num = int(input("정수를 입력해 주세요: "))
for i in range(0,num,1):
    line = line+star
    print(line)


