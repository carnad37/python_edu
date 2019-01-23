num = int(input("정수를 입력해주세요: "))
star = "*"
#내 for문에서 star를 3번 출력
#외 for문에서는 이전 수 -1만큼 반복시킴
count = num
for i in range(1,num+1,1):
    for j in range(1,count+1,1):
        print(star,end="")
    print("")
    count -= 1
line=""
for i in range(0,num,1):
    line = line+star
    print(line)