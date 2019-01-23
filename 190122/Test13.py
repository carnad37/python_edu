num = int(input("정수를 입력해주세요: "))
space = 0
star = num
for i in range(1,num+1,1):
    print((" "*space)+("*"*star))
    space += 1
    star -= 1
