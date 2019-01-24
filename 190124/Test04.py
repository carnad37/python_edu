#10이하의 정수 입력.
#a를 b승하여 나온 값을 리턴하는 함수
def dduble(x,y):
    result = x**y
    return result

num01 = int(input("첫번째 수를 입력해주세요: "))
num02 = int(input("두번째 수를 입력해주세요: "))

result = dduble(num01,num02)

print(result)