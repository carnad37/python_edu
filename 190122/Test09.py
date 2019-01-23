#2~9까지의 수 중 2개를 입력받아 두 수 사이의 구구단 출력

num=[]
num.append(int(input("구구단 시작: ")))
num.append(int(input("구구단 종료: ")))
num.sort()
mul = 0
for i in range(1,10,1):
    j=num[0]
    while j<(num[1]+1):
        mul = i*j
        print("%d * %d = %d"%(j,i,mul),end="\t")
        j+=1
    print("")