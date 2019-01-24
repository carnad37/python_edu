#서로다른 정수.
#큰수는 2로 나눠 몫을 저장.
#작은수는 2를 곱해서 저장.
#그리고 각각 출력

def my_system(num01,num02):
    num=[]
    num.append(num01)
    num.append(num02)
    num.sort()
    #구분 끝
    #큰수의 경우 maxresult로
    max = num[1]%2
    min = num[0]*2
    print("최대값 결과 :",max)
    print("최소값 결과 :",min)

num01 = int(input("첫번째 수를 입력해주세요: "))
num02 = int(input("두번째 수를 입력해주세요: "))

my_system(num01,num02)