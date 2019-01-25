#두값을 제곱으로 만들어서 뺄셈
def calcul(num01, num02):
    num01 = num01**2
    num02 = num02**2
    result = num01 - num02
    return result







num01 = int(input("첫번째 수를 입력해주세요: "))
num02 = int(input("두번째 수를 입력해주세요: "))
max=0
min=0
if(num01>num02):
    min = num02
    max = num01
else:
    max = num02
    min = num01
result = calcul(max,min)
print(result)