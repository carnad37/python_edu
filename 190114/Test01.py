#투입금액 입력
#투입금액-물건값
#거스름돈/500->정수값만 출력
#나머지 값/100
#won500
#won100

inCash=int(input("투입한 금액: "))
price=int(input("물건 값: "))
outCash=(inCash-price)
won500=(outCash//500)
won100=int(((outCash%500)/100))

print("거스름돈:",outCash)
print("500원 동전의 개수:",won500)
print("100원 동전의 개수:",won100)

