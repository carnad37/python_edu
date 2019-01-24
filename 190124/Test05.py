#n을 입력받아 숫자 사각형 만들기
#2중 반복문
#내부는 4행후 1행으로

def numberRac(num):
    count = 1
    #외부 반복문 num만큼 시행
    #숫자값은 따로 카운트한다 계속 늘어야함.
    for i in range(0,num,1):
        for j in range(0,num,1):
            print(count,end="\t")
            count+=1
        print("")


num = int(input("숫자를 입력해주세요: "))
numberRac(num)