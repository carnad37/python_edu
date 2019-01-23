#4칙연산 계산기 만들기.
#값입력
#함수내에 모든 계산 결과 출력.

def plus(num01,num02):
    res = num01+num02
    print("preResult :",res)
    return res

def minus(num01,num02):
    res = num01-num02
    print("preResult :",res)
    return res

def mul(num01,num02):
    res = num01*num02
    print("preResult :",res)
    return res

def div(num01,num02):
    res = num01/num02
    print("preResult :",res)
    return res

num01 = int(input("첫번째 정수를 입력해주세요: "))
num02 = int(input("두번째 정수를 입력해주세요: "))
res=plus(num01,num02)
print("plus :",res)
res=minus(num01,num02)
print("minus :",res)
res=mul(num01,num02)
print("mul :",res)
res=div(num01,num02)
print("div :",res)
