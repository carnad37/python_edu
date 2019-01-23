num01=int(input("첫번째 숫자를 입력해주세요: "))
num02=int(input("두번째 숫자를 입력해주세요: "))
num03=int(input("세번째 숫자를 입력해주세요: "))

if num01 > num02:
    minNum = num02
else:
    minNum = num01
if num03 < minNum:
    minNum = num03



"""
num = []
num.append(int(input("첫번째 숫자를 입력해주세요: ")))
num.append(int(input("두번째 숫자를 입력해주세요: ")))
num.append(int(input("세번째 숫자를 입력해주세요: ")))

#num.sort()
#minNum = num[0]
#로 정렬시켜준뒤, 인덱스 0의 숫자를 추출.
minNum=min(num)
"""



print(minNum)