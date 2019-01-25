#두개의 정수를 입력
#절대값이 큰 수 출력

def maxAbs(num01,num02):
    maxNum = 0
    # if(abs(num01)>abs(num02)):
    #     maxNum = num01
    # else:
    #     maxNum = num02
    # return maxNum
    if(abs(num01)>abs(num02)):
        num02 = num01
    return num02


def minAbs(num01,num02):
    minNum = 0
    if(abs(num01)>abs(num02)):
        minNum = num02
    else:
        minNum = num01
    return minNum

num01 = int(input("자연수를 입력해주세요: "))
num02 = int(input("자연수를 입력해주세요: "))
result01 = maxAbs(num01,num02)
num03 = float(input("실수를 입력해주세요: "))
num04 = float(input("실수를 입력해주세요: "))
result02 = minAbs(num03,num04)
print(result01)
print(result02)