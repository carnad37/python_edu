#사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.(세개의 수는 변수에 저장후 이후 크기 비교)

number = []
number.append(int(input("첫번째 숫자를 입력해주세요: ")))
number.append(int(input("두번째 숫자를 입력해주세요: ")))
number.append(int(input("세번째 숫자를 입력해주세요: ")))
"""
if num01>num02:
    max = num01
else:
    max = num02

if num03>max:
    max = num03
"""
number.sort()
maxNum = number[(len(number)-1)]

print(maxNum)