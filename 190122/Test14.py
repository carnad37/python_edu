#5,3,1순으로 출력(3)
#다음은 7,5,3,1(4)
#즉 출력되는 별의 갯수는 2n-1
#한번씩 띄어쓰기 반복

#숫자입력
num = int(input("숫자를 입력해주세요: "))
star = (num*2)-1
space = 0
#열 횟수만큼 반복시행
for i in range(1, num+1, 1):
    print((" "*space)+("*"*star))
    star -= 2
    space += 1