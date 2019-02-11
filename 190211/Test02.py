def student_Data(path_file):
    #첫번째 요소는 Key, 이후요소는 튜플로 묶어서 valuse로 만들기.
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

def student_Avg(sList):
    sum_List = []
    avg_List = []
    result_List = []
    for i in sList[1:]:
        for j in i[1:]:
            j = int(j)
            result_List.append(j)
        sum_List = sum(result_List)
        avg_List.append(sum_List)
    return  avg_List




path_file = "d:\\hhs2\\file\\subjectScore.csv"
student_List = student_Data(path_file)
print(student_List)

student_check = student_Avg(student_List)
print(student_check)
