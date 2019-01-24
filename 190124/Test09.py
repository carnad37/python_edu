#100이하의 자연수를 입력.
#행과 열을 곱한값이 출력

def numberRac(num):
    mul = 0
    for i in range(1,num+1,1):
        for j in range(1,num+1,1):
            mul = i*j
            print(mul,end="\t")
        print("")

num = int(input("100이하의 자연수를 입력해주세요: "))
numberRac(num)