def makesort(mList=[]):
    max = 0
    min = 0
    # 첫번쨰 반복문-총 요소의 갯수만큼 반복
    for i in range(0, len(mList)-1, 1):
        for j in range(i, len(mList), 1):
            if (j == i):
                max = i
            elif ((mList[j] > mList[max])):
                max = j
        min = mList[i]
        mList[i] = mList[max]
        mList[max] = min
    return mList

#     k=0
#     for i in range(0, len(mList)-1, 1):
#         for j in range(i, len(mList)-1, 1):
#             if mList[i]<mList[j+1]:
#                 k = numList[i]
#                 numList[i] = numList[j+1]
#                 numList[j+1] = k
#     return mList

#자연수 10이하의 n을 입력받아서. n만큼 대입
num = int(input("자연수를 입력해주세요: "))
numList = []
for i in range(0,num,1):
    numList.append(int(input("%d번째 자연수를 입력해주세요: "%(i+1))))
result = makesort(numList)
print(result)
#join