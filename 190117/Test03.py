num01 = int(input("첫번째 정수를 입력해주세요: "))
num02 = int(input("두번째 정수를 입력해주세요: "))
sumNum = 0


for i in range(num01,(num02+1),1):
    sumNum = sumNum + i
print(sumNum)
"""
if num01 > num02:
    min = num02
    max = num01+1
else:
    min = num01
    max = num02+1
for i in range(min, max, 1):
    sumNum = sumNum+i
print(sumNum)
"""