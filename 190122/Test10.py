#행과 열의 수를 입력받아서 출력

#줄마다 각기 시작숫자의 배수가 나열
#풀어쓰면
#1*1 1*2 1*3...
#2*1 2*2...
#같은 형식


numN = int(input("행을 입력해주세요: "))
numT = int(input("열을 입력해주세요: "))

mul = 0
for i in range(1,numN+1,1):
    for j in range(1,numT+1,1):
        mul = i*j
        print(mul,end="\t")
    print("")