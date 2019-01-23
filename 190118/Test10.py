num = int(input("정수를 입력해주세요: "))
count = 1
sum = 0
while count <= num:
    sum = sum + count
    count = count + 1
print("1부터",num,"까지의 합은",sum,"이다.")
