#######################

#math.sqrt(num) num에 넣은값의 루트값이 나온다.

#######################

#10이하의 두개의 정수를 입력받아서 작은 수부터 큰 수까지의 구구단을 차례로 출력하는 프로그램을 구조화하여 작성하시오.
# num = []
# num.append(int(input("첫번째 수를 입력해주세요: ")))
# num.append(int(input("두번째 수를 입력해주세요: ")))
# num.sort()
#구구단을 출력하는 함수. x부터 y까지의...
#일단 구분 하는 형식으로.
def gugu_calc(x, y):
    num = []
    num.append(int(x))
    num.append(int(y))
    num.sort()
    for i in range(1,10,1):
        for j in range(num[0],(num[1]+1),1):
            mul = i*j
            print("%d*%d=%d"%(j,i,mul),end="\t")
        print("")

# def gugu_calc(x, y):
#     for i in range(1,10,1):
#         for j in range(x,(y+1),1):
#             mul = i*j
#             print("%d*%d=%d"%(j,i,mul),end="\t")
#         print("")

# num01 = int(input("첫번째 수를 입력해주세요: "))
# num02 = int(input("첫번째 수를 입력해주세요: "))
# gugu_calc(num01,num02)

num = []
num.append(int(input("첫번째 수를 입력해주세요: ")))
num.append(int(input("첫번째 수를 입력해주세요: ")))
num.sort()
minNum = num[0]
maxNum = num[1]
gugu_calc(minNum,maxNum)