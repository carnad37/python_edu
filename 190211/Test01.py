#딕셔너리에 studentScore를 저장.

def txt_toDic(path_file):
    openfile = open(path_file,'r')
    sum_List = []
    for line in openfile:
        dList = line.split()
        dList[1] = int(dList[1])
        print(dList)
        sum_List.append(dList)
    openfile.close()
    return sum_List

#딕셔너리에서 가장 낮은 v를 가진 k의 값을 리턴
def min_inList(sList):
    print(sList[0])
    max = sList[0]
    min = sList[0]
    for i in sList:
        if(max[1]<i[1]):
            max = i
            print(max)
        if(min[1]>i[1]):
            min = i
            print(min)
    return max, min
    #가장 낮은 값을 가진 k의 위치를 찾음.
def score_Avg(sList):
    sum = 0
    for i in sList:
        sum += i[1]
    avg = sum/len(sList)
    return avg

#점수가 높은 사람 : v만 뽑아내서 가장 높은 v의 위치 확인. k출력.
#낮은 사람 : 반대로.
#평균점수 : v값을 합친후에 len(v든 k든)재서 나눈다.

openfile = "d:\\hhs2\\file\\studentScore.txt"
ssDic = txt_toDic(openfile)

max = []
min = []
max, min = min_inList(ssDic)
avg = score_Avg(ssDic)
print("가장 점수가 높은 사람:",max[0])
print("가장 낮은 점수:",min[1])
print("평균 점수:",avg)
