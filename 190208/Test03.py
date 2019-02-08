#딕셔너리에 studentScore를 저장.

def txt_toDic(url):
    openfile = open(url,'r')
    rDic = {}
    for line in openfile:
        dList = line.split()
        print(dList)
        rDic[dList[0]] = int(dList[1])
    openfile.close()
    return rDic

#딕셔너리에서 가장 낮은 v를 가진 k의 값을 리턴
def min_inDic(dic):
    vList = dic.values()
    vList = list(vList)
    vsList = sorted(vList)
    search = vList.index(vsList[0])
    kList = dic.keys()
    kList = list(kList)
    result = kList[search]
    return result
    #가장 낮은 값을 가진 k의 위치를 찾음.


#점수가 높은 사람 : v만 뽑아내서 가장 높은 v의 위치 확인. k출력.
#낮은 사람 : 반대로.
#평균점수 : v값을 합친후에 len(v든 k든)재서 나눈다.

openfile = "d:\\hhs2\\file\\studentScore.txt"
ssDic = txt_toDic(openfile)
name = min_inDic(ssDic)
print(name)
