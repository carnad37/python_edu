count = 1
sum = 0
sum3 = 0
count3 = 0
while count<11:
    sum += count
    if (count%3) == 0:
        sum3 = sum3 + count
        count3 = count3 + 1
    count += 1
avg = sum/count
avg3 = sum3/count3
print("1부터 10까지의 합은",sum)
print("1부터 10까지의 합의 평균은",avg)
print("1부터 10까지의 3의 배수들의 합은",sum3)
print("1부터 10까지의 3의 배수들의 평균은", avg3)
