#입력된 수까지의 5의 배수의 합
count = 1
sum = 0
num = int(input("정수를 입력해주세요: "))

while count <= num:
    if(count%5==0):
       sum = sum + count
    count+= 1

print(sum)