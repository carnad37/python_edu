#우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.

passNum = input("우편번호를 입력해주세요: " )

locNum = int(passNum[2])

if locNum > 5:
    locName = "노원구"
elif locNum > 2:
    locName = "도봉구"
else:
    locName = "강북구"

print(locName)


#0~2 강북, 3~5 도봉구, 6~9 노원구
