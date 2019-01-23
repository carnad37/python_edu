#주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
#주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라

cityNum = input("주민등록번호를 입력해주세요(-포함): ")
seachBar = "-"
#searchRes = cityNum.find(seachBar)
#입력판별
"""
if searchRes == -1:
    print("잘못 입력하셨습니다. 프로그램을 종료합니다.")
else:
    listNum = cityNum.split(seachBar)
    sNum = listNum[1]
    locNum = int(sNum[1:3])
    if locNum > 8:
        print(cityNum + "은 서울 출생이 아닙니다.")
    else:
        print(cityNum + "은 서울입니다.")
    print(locNum)

"""
listNum = cityNum.split(seachBar)
sNum = listNum[1]
locNum = int(sNum[1:3])
if locNum > 8:
    print(cityNum + "은 서울 출생이 아닙니다.")
else:
    print(cityNum + "은 서울입니다.")

