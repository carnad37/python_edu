#이름이 입력됬을때 각 라인의 첫번쨰 요소와 비교.

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

def array_List(aList):
    #행과 열을 바꿔주는 함수
    sum_List = []
    for i in aList[0]:
        array_check = [i]
        sum_List.append(array_check)
    for i in range(0,len(sum_List),1):
        for j in range(1,len(aList),1):
            sum_List[i].append(aList[j][i])
    return sum_List

def calculate_Avg(sList):
    #전과목 평균 리스트 제작
    #sList[0]은 이름을 가지고있다.
    #[1][1~끝]까지가 숫자다. 바꿔주자.
    avg_List=["score_avg"]
    sum_score = 0
    max = len(sList[0])
    print(max)
    for i in range(1,max,1):
        for j in range(1,len(sList),1):
            sum_score+=int(sList[j][i])
        sum_score=sum_score/(len(sList)-1)
        avg_List.append(sum_score)
        sum_score = 0
    return avg_List

def max_and_min_student(avgList,sList):
    check_List = sorted(avgList[1:])
    min_index = avgList.index(check_List[0])
    max_index = avgList.index(check_List[len(check_List)-1])
    min_student = sList[0][min_index]
    max_student = sList[0][max_index]
    return min_student,max_student

path_file = "D:\\workspace\\files\\subScore.txt"
student_pre_List = student_Data(path_file)
student_List = array_List(student_pre_List)
student_avg_List=calculate_Avg(student_List)
(min_name,max_name)=max_and_min_student(student_avg_List,student_List)
print(student_List)
print(student_avg_List)
print("평균 최저점의 학생은 %s이다"%min_name)
print("평균 최고점의 학생은 %s이다"%max_name)


#각 학생들의 평균 점수.
#평균점수가 가장 높은 학생의 이름.
#평균점수가 가장 낮은 학생의 이름.


#원하는 과목을 name key의 val에서 서치. 그 값을 대입.
#각 학생의 평균 점수 구하기
