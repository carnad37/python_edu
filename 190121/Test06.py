#리스트를 써보자
#리스트
listCountry = ["Seoul","Washington","Tokyo","Beijing"]
num = 0
while True:
    print("1. Korea")
    print("2. USA")
    print("3. Japan")
    print("4. China")
    num = int(input("number? "))
    #종료코드
    if((num<1) | (num>4)):
        print("\n","none","\n")
        break
    #리스트안의 값을 출력
    print("\n",listCountry[(num-1)],"\n")
