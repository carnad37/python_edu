#사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라.
#사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.

cashString = input("금액과 단위를 입력해주세요: ")
#입력된 문자열은 "금액(숫자) 단위(문자)"의 복합체.
#띄어쓰기를 find하고 슬라이싱으로 금액과 단위를 나눈다. 금액만 떨겨내 원으로 환산하고, 단위를 통해 환산을한다.
"""
#돈 나누기
findCash = " "
cashPos = cashString.find(findCash)
cash = int(cashString[:cashPos])

#단위 환산
cashType = cashString[(cashPos+1):]
"""
#split을 이용한 방법
#1. 문자열을 리스트화
cashList = cashString.split()
cash = int(cashList[0])
cashType = cashList[1]


if cashType=="달러":
    cashRes = cash*1167
    print("환전된 금액은", cashRes, "원입니다.")
elif cashType=="엔":
    cashRes = cash*1.096
    print("환전된 금액은", cashRes, "원입니다.")
elif cashType=="유로":
    cashRes = cahs*1268
    print("환전된 금액은", cashRes, "원입니다.")
elif cashType=="위안":
    cashRes = cash*171
    print("환전된 금액은", cashRes, "원입니다.")
else:
    print("잘못 입력되었습니다.")


