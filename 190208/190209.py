#이름이 입력됬을때 각 라인의 첫번쨰 요소와 비교.

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

def array_List(aList):
    sum_List = []
    for i in aList[0]:
        array_check = [i]
        sum_List.append(array_check)
    for j in
    print(sum_List)
    return sum_List

path_file = "d:\\hhs2\\file\\subjectScore.csv"
student_Dic = student_Data(path_file)
#조건이 너무 심하다.
auuuut = array_List(student_Dic)

print(student_Dic)


#원하는 과목을 name key의 val에서 서치. 그 값을 대입.
#각 학생의 평균 점수 구하기
