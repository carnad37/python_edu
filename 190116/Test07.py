#주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
#사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.

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
    if int(sNum[0]) == 1:
        print("남성입니다.")
    else:
        print("여성입니다.")
"""
listNum = cityNum.split(seachBar)
sNum = listNum[1]
if int(sNum[0]) == 1:
    print("남성입니다.")
else:
    print("여성입니다.")
