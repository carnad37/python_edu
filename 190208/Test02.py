#1.딕셔너리에 저장해주는 함수
#2.

def txt_toDic(url):
    openfile = open(url,'r')
    rDic = {}
    for line in openfile:
        dList = line.split()
        print(dList)
        rDic[dList[0]] = dList[1]
    openfile.close()
    return rDic

openUrl = "d:\\hhs2\\file\\user.txt"
user_Dic = txt_toDic(openUrl)
print(user_Dic)