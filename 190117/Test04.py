num = []
num.append(int(input("첫번째 정수를 입력해주세요: ")))
num.append(int(input("두번째 정수를 입력해주세요: ")))

#num.sort()
#minNum = num[0]
#maxNum = num[1]+1

minNum = min(num)
maxNum = (max(num)+1)

sumNum = 0
for i in range(minNum, maxNum, 1):
    sumNum = sumNum + i

print(sumNum)
