def student_Data(path_file):
    #데이터를 리스트로 만들어주는 함수
    readfile = open(path_file,'r')
    checkList = []
    sumTuple = ()
    save_List = []
    count = 0
    for line in readfile:
        line = line.rstrip("\n")
        checkList = line.split(",")
        if count > 0:
            indexCount = 0
            for i in checkList[1:]:
                i = int(i)
                indexCount += 1
                checkList[indexCount] = i
        count += 1
        #count는 행의 갯수. incount는 리스트 내의 인덱스
        save_List.append(checkList)
    #여기서
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

def calculate_pre_Avg(sList):
    save_List = ["score_avg"]
    for i in range(1,len(sList),1):
        sum_score = sum(sList[i][1:])
        sum_score = sum_score/(len(sList[0])-1)
        save_List.append(sum_score)
    return save_List

def calculate_Avg(sList):
    #전과목 평균 리스트 제작
    #sList[0]은 이름을 가지고있다.
    #[1][1~끝]까지가 숫자다. 바꿔주자.
    avg_List=["score_avg"]
    sum_score = 0
    max = len(sList[0])
    for i in range(1,max,1):
        for j in range(1,len(sList),1):
            sum_score+=sList[j][i]
        sum_score=sum_score/(len(sList)-1)
        avg_List.append(sum_score)
        sum_score = 0
    return avg_List

def max_and_min_student(avgList,sList):
    #최고점과 최저점 학생의 이름 호출
    check_List = sorted(avgList[1:])
    min_index = avgList.index(check_List[0])
    max_index = avgList.index(check_List[len(check_List)-1])
    min_student = sList[0][min_index]
    max_student = sList[0][max_index]
    return min_student,max_student

def print_avg_scroe(avgList,sList):
    #모든 학생의 평균점수를 호출
    for i in range(1,len(avgList),1):
        name = sList[0][i]
        avg = avgList[i]
        print("%s의 평균점수는 %d이다"%(name,avg))

path_file = "d:\\hhs2\\file\\subjectScore.csv"
student_pre_List = student_Data(path_file)
print(student_pre_List)
student_pre_avg_List = calculate_pre_Avg(student_pre_List)
print(student_pre_avg_List)
student_List = array_List(student_pre_List)
print(student_List)
student_avg_List=calculate_Avg(student_List)
print(student_avg_List)
# print_avg_scroe(student_avg_List,student_List)
(min_name,max_name)=max_and_min_student(student_avg_List,student_List)

# print("")
# print("평균 최저점의 학생은 %s이다"%min_name)
# print("평균 최고점의 학생은 %s이다"%max_name)