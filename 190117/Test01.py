sumCount = 0
sumNum = 0
sum3 = 0
sum3Count = 0
for i in range(1,11,1):
    sumNum = sumNum+i
    sumCount += 1
    if i%3 == 0:
        sum3 = sum3+i
        sum3Count = sum3Count + 1
print(sumNum)
sumAvg = sumNum/sumCount
print(sumAvg)
sum3Avg = sum3/sum3Count
print(sum3Avg)

"""
for i in range(3, 11, 3

"""