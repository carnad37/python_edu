max = 0
min = 0
sum = 0
count = 0
num01 = int(input("첫번째 정수를 입력해주세요: "))
num02 = int(input("두번째 정수를 입력해주세요: "))
if num01>num02:
    max = num01
    min = num02
else:
    max = num02
    min = num01
for i in range(min,max+1,1):
    if(i%3==0)|(i%5==0):
        sum += i
        count += 1
avg = sum/count
print("Sum : %d"%sum)
print("AVg : %d"%avg)