year=int(input("연도를 입력하시오: "))

#4년으로 떨어진다 true
#100으로 나눠서 떨어지지 않고 4년으로 나눠 떨어지는경우.
#400으로 나눠서 떨어진다 ture
#ture false일땐 ture

#not, != 같당

if (year%4==0 and not year%100==0) or year%400==0:
    print(year,"년은 윤년입니다.")
else:
    print(year,"년은 윤년이 아닙니다.")