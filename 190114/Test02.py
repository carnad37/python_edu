"""

#세 개의 정수를 입력 받아서 합계와 평균을 출력하시오
#10, 25, 33
num01 = int(input("첫 번째 수 입력: "))
num02 = int(input("두 번째 수 입력: "))
num03 = int(input("세 번째 수 입력: "))
numSum = num01 + num02 + num03
numAvg = int(numSum/3)
print("sum =",numSum)
print("avg =",numAvg)

"""

num=[]
num.append(int(input("첫 번째 수 입력: ")))
num.append(int(input("두 번째 수 입력: ")))
num.append(int(input("세 번째 수 입력: ")))

sumNum=sum(num)
numLen=len(num)
avgNum=int(sumNum/numLen)
print(sumNum)
print(avgNum)

"""

print("")

#정수 2개를 입력받아서 첫 번째 수에는 100을 증가시켜 저장하고
#두 번째 수는 10으로 나눈 나머지를 저장한 후  두 수를 차례로 출력하는 프로그램을 작성하시오.

num01 = int(input("첫 번째 수 입력: "))
num01 += 100
num02 = int(input("두 번째 수 입력: "))
num02 %= 10
print(num01, num02)

print("")

#국어 영어 수학 컴퓨터 과목의 점수를 정수로 입력받아서 총점과 평균을 구하는 프로그램을 작성하시오

sub_lit = int(input("국어 점수를 입력: "))
sub_eng = int(input("영어 점수를 입력: "))
sub_mat = int(input("수학 점수를 입력: "))
subSum = sub_eng + sub_lit + sub_mat
subAvg = int(subSum/3)
print("총점:",subSum,"\n평균:",subAvg)

#두 정수를 입력받아서 나눈 몫과 나머지를 다음과 같은 형식으로 출력하는 프로그램을 작성하시오

num01 = int(input("첫 번째 수 입력: "))
num02 = int(input("두 번째 수 입력: "))
numVal = num01//num02
numRem = num01%num02
print(num01,"/",num02,"=",numVal,"...",numRem)

#직사각형의 가로와 세로의 길이를 정수형 값으로 입력받은 후
#가로의 길이는 5 증가시키고 세로의 길이는 2배하여 저장한 후
#가로의 길이 세로의 길이 넓이를 차례로 출력하는 프로그램을 작성하시오.

rac_01 = int(input("가로의 길이: "))
rac_02 = int(input("세로의 길이: "))

width = rac_01+5
length = rac_02*2
area = width*length

print("width :",width,"\nlength :",length,"\narea :",area)

"""