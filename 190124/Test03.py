#두개의 정수를 입력받아 최대값을 구함.
#그걸 이용해서 3개를 비교 최대값을 뽑아내라


def selectNum(num01, num02):
    if (num01 < num02):
        num01 = num02
    return num01

num01 = int(input("첫번째 수를 입력해주세요: "))
num02 = int(input("두번째 수를 입력해주세요: "))
num03 = int(input("세번째 수를 입력해주세요: "))

max = selectNum(num01,num02)
max = selectNum(max, num03)

print(min)
