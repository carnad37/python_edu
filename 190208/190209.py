#이름이 입력됬을때 각 라인의 첫번쨰 요소와 비교.

def student_Data(url):
    #첫번째 요소는 Key, 이후요소는 튜플로 묶어서 valuse로 만들기.
    readfile = open(url,'r')
    checkList = []
    sumTuple = ()
    saveDic = {}
    for line  in readfile:
        checkList = line.split(",")
        sumTuple = tuple(checkList[1:])
        saveDic[checkList[0]] = 



