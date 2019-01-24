#1부터 n까지의 합.
#1000이하의 자연수를 입력받아 출력.

def targeSum(num):
    sum = 0
    for i in range(1,num+1,1):
        sum+=i
    return sum

num = int(input("1000이하의 정수를 입력해주세요: "))
result = targeSum(num)
print(result)