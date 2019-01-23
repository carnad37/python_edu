#연산자...? string? char?
cul = input("연산자를 입력해주세요: ")
num01 = int(input("첫번째를 숫자를 입력해주세요: "))
num02 = int(input("두번째를 숫자를 입력해주세요: "))

#연산자에 따라 번호지정은 필요가 없고, String을 그대로 인식시켜도 충분했던것이다..
#+는 1, -는 2, *는 3, /는 4

if cul == "+":
    res = num01+num02
    print(res)
elif cul == "-":
    res = num01-num02
    print(res)
elif cul == "*":
    res = num01*num02
    print(res)
elif cul == "/":
    res = num01/num02
    print(res)
else:
    print("연산자가 잘못 입력되었습니다.")