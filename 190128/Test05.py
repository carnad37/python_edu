marketList = {"커피음료":7,"펜":3, "종이컵":2, "우유":1, "콜라":4, "책":5}

marketSearch = input("물건의 이름을 입력하시오: ")
#키값을 넣었을때 값을 출력.
searchRes = marketList[marketSearch]
print(searchRes)

marketSearch = int(input("물건의 갯수를 입력해주세요: "))
