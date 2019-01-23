num=int(input("숫자를 입력해주세요: "))

if num==1:
    print(num,": 상품주문")
elif num==2:
    print(num, ": 상품교환")
elif num==3:
    print(num, ": 환불")
elif num==4:
    print(num, ": 주문 조회")
elif num==5:
    print(num, ": 직원연결")
elif num==6:
    print(num, ": 다시 듣기")
else:
    print("잘못 입력하였습니다.")