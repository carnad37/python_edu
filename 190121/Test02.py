#한개의 숫자를 입력.
#양수인지 음수인지 판별하다 0이되면 종료.
#while쓰자 골아프다
while True:
    num = int(input("number? "))
    if(num == 0):
        break
    elif(num<0):
        print("negative number")
    else:
        print("positive integer")