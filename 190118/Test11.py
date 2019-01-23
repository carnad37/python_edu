num01 = int(input("첫번째 정수를 입력해주세요: "))
num02 = int(input("두번째 정수를 입력해주세요: "))

sum = 0
max = 0
min = 0

if num01>num02:
    max = num01
    min = num02
else:
    max = num02
    min = num01

maxN = max
minN = min

while min <= max:
    sum = sum + min
    min = min + 1

print(minN,"부터",maxN,"까지의 합은",sum,"이다.")

