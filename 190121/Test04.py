#정수를 입력받다 0이 입력되면 stop
#짝수(even) 와 홀수(odd)의 갯수를 출력
even = 0
odd = 0
num = 0

while True:
    num = int(input("정수를 입력해주세요: "))
    #종료코드
    if num == 0:
        break
    if num%2 == 0:
        even += 1
    else:
        odd += 1
print("odd :", odd)
print("even :", even)