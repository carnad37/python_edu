#

def student_Data(path_file):
    #데이터를 리스트로 만들어주는 함수
    readfile = open(path_file,'r')
    checkList = []
    sumTuple = ()
    save_List = []
    for line  in readfile:
        line = line.rstrip("\n")
        checkList = line.split(",")
        # sumTuple = tuple(checkList[1:])
        # saveDic[checkList[0]] = sumTuple
        save_List.append(checkList)
    readfile.close()
    return save_List