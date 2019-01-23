#사칙연산 함수 4개
#메뉴 함수
#메뉴함수는 1~4까지만 무한반복. 5에선 종료. 1~5 외의 숫자일땐 재입력을 받게함.

def plus(num01,num02):
    res = num01+num02
    return res

def minus(num01,num02):
    res = num01-num02
    return res

def mul(num01,num02):
    res = num01*num02
    return res

def div(num01,num02):
    res = num01/num02
    return res

def print_menu():
    print("1.add")
    print("2.sub")
    print("3.mul")
    print("4.div")
    print("5.종료")

#==============================================================================

#전체식 전개
#반복문으로 시작된다
select = 0
num01 = int(input("첫번째 정수를 입력해주세요: "))
num02 = int(input("두번째 정수를 입력해주세요: "))

while(True):
    print_menu()
    #선택
    select = int(input(">"))
    #각각의 경우를 시행
    if(select==1):
        res = plus(num01,num02)
        print("Add :",res)
    elif(select==2):
        res = minus(num01,num02)
        print("Sub :",res)
    elif(select==3):
        res = mul(num01,num02)
        print("Mul :",res)
    elif(select==4):
        res = div(num01,num02)
        print("Div :",res)
    elif(select==5):
        break
    else:
        print("잘못된 명령입니다. 다시 입력해주세요.")
print("프로그램 종료")
